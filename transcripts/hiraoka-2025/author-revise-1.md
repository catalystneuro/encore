# hiraoka-2025 · author-revise-1 · run 44966869542

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md | head -c 100000 | wc -c; ls entries/hiraoka-2025 transcripts/hiraoka-2025 questions 2>/dev/null | head -50
```

```
Sun Nov 22 00:33:11 UTC 2026
47547
entries/hiraoka-2025:
README.md
bursttree.py
entry.yaml
model.ipynb
other_neurons.ipynb
reproduce_hiraoka_2025.ipynb
requirements.in
requirements.lock.txt

questions:
README.md
asari-2009.yaml
ashworth-2025.yaml
athalye-2023.yaml
bech-2026.yaml
bellvila-2026.yaml
bennett-2024.yaml
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
ls transcripts/hiraoka-2025; cat transcripts/hiraoka-2025/verifier-1-report.md
```

```
author-report.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
**A. Outcomes**

The claims file has 14 claims. The notebooks test 12, and 2 are blocked.

| Claim | My outcome | Reason |
|---|---|---|
| fig2-neuron-representative-sequence | reproduced | Under O1 reading (b), row 9 counted from 0 (units id 18), the unit has n = 228 356, τmin = 1.050 ms and τmax = 18 229.7 ms (main nb cell 9). It is the only unit in the session that matches. The three epoch counts add up to 228 356 exactly (cell 27), which confirms O2. |
| fig2-iet-broad | reproduced | τmax/τmin = 17 362, which is 4.24 decades, against ≥10³ required (cell 11). |
| fig2-neuron-burst-size-heavy-tail | reproduced | Under both KS readings and both grids, the power law is supported at every δ: 8/8 (grid a) and 40/40 (grid b), including every δ below 3000 ms (cell 15). The xmin = 1 readings fail below 3000 ms. The renewal (shuffled) reference supports a power law at 0 timescales in all 5 seeds. |
| fig2-neuron-beta-stable | not_reproduced | Neither reading holds under any fit reading or grid (cell 17). For example, ks_discrete on grid b has median 2.354, which is in the band, but its range is 0.705 against <0.47 allowed. β is 2.6–2.9 for δ ≲ 130–180 ms, and only from 126–183 ms to 3000 ms (about 1.2 decades) do all estimates sit within 2.35 ± 0.235. Removing the cap in problem 1 would only widen the range. |
| fig2-neuron-beta-decrease-follows-gamma | reproduced | Grid (a) has only 1 point above 3000 ms, so it is not judged. On grid (b) under both KS readings: (1) 38/57 and 40/57 pairs have β(δ′) < γ; (2) ρβ = −0.83 (p = 0.042, 6 points); (3) ργ < 0 for all three ratios (cell 25). |
| fig2-neuron-merging-heavy-tail | partially_reproduced | Support is robust: 15/15 (ks_continuous, grid a) and 72/76 (grid b). The IQR condition (0.38–0.43 against <0.5) depends on an estimator that is bounded at α < 3 (problem 1). Six of the 15 grid-(a) γ values si
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md
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
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
755:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 199,640p docs/protocol.md
```

```
<persisted-output>
Output too large (29.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ffb0384b-d021-4d0a-a148-6152ae3e7e25/tool-results/b2ez9jqox.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 700,800p docs/protocol.md
```

```
change. The author is started with `-f version=draft` (or a version number),
and `docs/agents/author-again.md` is its prompt.

## Local and remote datasets

`encore check` ([encore.md](encore.md)) runs this protocol on someone's own
machine, on a dataset that may be in no archive: a directory of files on that
machine (archive `local`), or files at a URL (archive `remote`). The paper
comes from the person running it and is put under `paper/` as usual. Such an
attempt is never deposited in the registry, and every rule here applies to it,
with these exceptions:

- **Reading the data.** For a `local` dataset, read the files in place, at the
  path the prompt gives. Never copy, move or change them. Naming that path in
  the notebooks is allowed; naming any other local path is not. For a
  `remote` dataset, stream the files from the URL the prompt gives. In
  neither case look for the dataset in an archive, even when it looks like
  one you know.
- **The version.** There is none to choose or pin. The prompt gives the
  fingerprint of the files; record it wherever a version is asked for: in the
[... 60 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ffb0384b-d021-4d0a-a148-6152ae3e7e25/tool-results/b2ez9jqox.txt"
}
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
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
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
[... 465 more lines not kept]
```

**Agent**

I've read the protocol and the round-1 report. This is the round-1 revision, so outcomes can still change. Next I'll look at the attempt record and the entry.

**Agent calls Bash**

```bash
ls attempts | grep hiraoka; cat attempts/hiraoka-2025-01.yaml; cat entries/hiraoka-2025/entry.yaml entries/hiraoka-2025/requirements.in; ls executed/hiraoka-2025 2>/dev/null; cat questions/hiraoka-2025.yaml 2>/dev/null
```

```
Exit code 1
hiraoka-2025-01.yaml
schema_version: 3
id: hiraoka-2025-01
datasets:
- archive: dandi
  id: "000044"
  version: 0.210812.1516
  doi: 10.48324/dandi.000044/0.210812.1516
  relation: reuses
paper: doi:10.1063/5.0296506
date: 2026-11-21
entry: hiraoka-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 95,260p attempts/hiraoka-2025-01.yaml; grep -i powerlaw entries/hiraoka-2025/requirements.lock.txt; cat executed/hiraoka-2025/result.json | head -50
```

```
with delta for each ratio (rho -0.714, -0.964 and -0.943). Grid (a) has one point above 3000 ms,
    so parts (2) and (3) are not judged on it; its part (1) holds (7 and 8 of 12). Under xmin = 1
    part (1) fails (24 of 57), so the outcome rests on the KS fits, as O3 allows for a claim on
    exponents. The paper names no test; the claim's "seems to be driven" is not tested beyond
    these correlations.
- claim: fig2-neuron-merging-heavy-tail
  outcome: reproduced
  notebook: reproduce_hiraoka_2025.ipynb
  output: claim:fig2-neuron-merging-heavy-tail
  notes: Under the KS fits the power law is supported for 14 (discrete) and 15 (continuous) of 15
    pairs on grid (a) and 71 and 72 of 76 on grid (b); the gamma of the supported pairs has an
    interquartile range of 0.383 to 0.426 and a median of 2.633 to 2.752. With xmin = 1 the
    discrete fit is supported for 6 of 15 and 19 of 76 pairs, and the continuous fit has an
    interquartile range of 0.673 and 0.597.
- claim: fig2-neuron-merging-collapse
  outcome: reproduced
  notebook: reproduce_hiraoka_2025.ipynb
  output: claim:fig2-neuron-merging-collapse
  notes: Reproduced by reading (b) under the discrete KS fit alone, with no margin. The gamma of the
    15 pairs of Figure 2 lie within 0.490 of their median of 2.610 (the band is 0.5); under the
[... 176 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; wc -l bursttree.py; cat bursttree.py
```

```
393 bursttree.py
"""Bursty trains, merging numbers and power-law fits for Hiraoka & Jo (2025) on DANDI:000044.

Paper: T. Hiraoka and H.-H. Jo, "Hierarchical organization of bursty trains in event
sequences", doi:10.1063/5.0296506 (text read: the arXiv preprint body under paper/).
Claims: claims/hiraoka-2025.yaml. Where a parameter comes from is said beside it:

- "Methods" means Section II of the paper, as the claims file's opening comment gives it.
- O1 to O4 are the open details named in the claims file's opening comment.
- "Assumption" marks a choice this attempt made where neither source fixes it.
- "Standard choice" marks a detail that cannot change an outcome.

Data are streamed from the DANDI archive at the pinned version (DANDI_VERSION); nothing is
written to disk.
"""
from __future__ import annotations

import warnings

import h5py
[... 374 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import powerlaw,sys;print(powerlaw.__version__, powerlaw.__file__, sys.version)" 2>&1; ls -a; ls ~/.cache 2>/dev/null; sed -n 1,80p tools/entry.py | head -80
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import powerlaw,sys;print(powerlaw.__version__, powerlaw.__file__, sys.version)
    ^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'powerlaw'
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
[... 126 more lines not kept]
```

**Agent**

Let me make a dev venv from the lock file to probe powerlaw 2.0.0.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 dev && . dev/bin/activate && uv pip install -q -r entries/hiraoka-2025/requirements.lock.txt ipykernel nbconvert 2>&1 | tail -3; python -c "import powerlaw;print(powerlaw.__version__)"; grep -n "DEFAULT_PARAMETER_RANGES\|def in_range\|parameter_range" $TMPDIR/dev/lib/python3.13/site-packages/powerlaw*.py $TMPDIR/dev/lib/python3.13/site-packages/powerlaw/*.py 2>/dev/null | head -40
```

```
2.0.0
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:66:    parameter_ranges : dict, optional
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:149:                 parameter_ranges=None,
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:162:        #DEFAULT_PARAMETER_RANGES = {}
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:221:        # This sets the variable `self.parameter_ranges`
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:222:        self.initialize_parameter_ranges(parameter_ranges)
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:417:    def initialize_parameter_ranges(self, ranges=None):
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:423:        more information, see the variable ``DEFAULT_PARAMETER_RANGES`` in
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:441:            ``self.DEFAULT_PARAMETER_RANGES``.
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:448:        ranges_dict = dict(self.DEFAULT_PARAMETER_RANGES)
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:477:        self.parameter_ranges = ranges_dict
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:648:        Bounds defined in ``self.parameter_ranges`` are used explicitly during
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:692:        bounds = [b for b in self.parameter_ranges.values()]
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:798:            if self.parameter_ranges[p][0] is not None:
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:799:                nearBoundary += getattr(self, p) - eps < self.parameter_ranges[p][0]
/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/distributions.py:801: 
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
P=$TMPDIR/dev/lib/python3.13/site-packages/powerlaw; sed -n 300,460p $P/fitting.py; sed -n 640,720p $P/distributions.py; sed -n 1760,1900p $P/distributions.py
```

```
distribution is called, like `fit.power_law`. This means we
        normally can't autocomplete the distribution names since they
        don't exist until we actually call them.

        As such, we add the list of distribution names to the __dir__
        function used for autocomplete so we can autocomplete them
        before they exist. That being said, this still only works after the
        Fit object is created.
        """
        current_attrs = self.__dict__.keys()
        total_attrs = list(current_attrs) + list(self.supported_distributions)

        # Take unique values and cast to tuple
        return tuple(np.unique(total_attrs))


    def __getattr__(self, name):
        """
        This function is redefined such that we can access the supported
        distributions and have them inherit the data and options from the
[... 362 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; grep -il "powerlaw\|alstott" paper/* | head; grep -n -i "alstott\|powerlaw\|clauset\|maximum likelihood\|python" paper/*.md paper/*.txt 2>/dev/null | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "\[36\]\|\[37\]\|arXiv\|received\|submitted\|2024\|2025" paper/10.1063-5.0296506.txt | head -30; grep -n -B3 -A12 "exponents are indicated" paper/10.1063-5.0296506.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "exponent\|≈\|approx" paper/10.1063-5.0296506.txt | sed -n 1,80p
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 355,460p paper/10.1063-5.0296506.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python - <<'EOF'
import nbformat
for nb in ["reproduce_hiraoka_2025.ipynb","other_neurons.ipynb","model.ipynb"]:
    n=nbformat.read(nb,4)
    print("=====",nb,len(n.cells))
    for i,c in enumerate(n.cells):
        print(f"--- [{i}] {c.cell_type} {c.metadata.get('tags',[])} len={len(c.source)}")
        print(c.source[:300])
EOF
```

```
===== reproduce_hiraoka_2025.ipynb 39
--- [0] markdown [] len=2726
# Reproducing Hiraoka & Jo (2025) on DANDI:000044: the representative neuron

Paper: Takayuki Hiraoka and Hang-Hyun Jo, "Hierarchical organization of bursty trains in event
sequences", doi:10.1063/5.0296506. The claims file (`claims/hiraoka-2025.yaml`) was written from
`paper/10.1063-5.0296506.txt`,
--- [1] code [] len=344
import time, resource, zlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
import bursttree as bt

T0 = time.time()
pd.set_option("display.width", 200, "display.max_columns", 30, "display.max_rows", 200)
PAPER = "hiraoka-2025"
print("dandiset
--- [2] markdown [] len=555
[... 399 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,400p claims/hiraoka-2025.yaml
```

```
# Claims for Hiraoka & Jo (2025), "Hierarchical organization of bursty trains in event
# sequences", doi:10.1063/5.0296506, on dandiset 000044.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: paper/10.1063-5.0296506.txt. Its header says "version of record", but only its
# first part (abstract and a 54-item reference list) is from the version of record. The body
# that follows is the arXiv preprint (stamp arXiv:2508.18281v1, dated September 22, 2025, 50
# references), and its abstract is worded differently. Every claim and quote below comes from
# that preprint body: Sections I to V, Algorithms 1 and 2, and the legends of Figures 1 to 4.
# The paper has no supplement. No PDF was supplied, so the figure panels were read only from
# the labels the text extraction keeps (the delta values in the legends, n, tau_min, tau_max).
# The paper links no analysis code. Its fits use the maximum likelihood estimator and the
# likelihood ratio test of Clauset et al. (ref. 36), citing the Python package powerlaw
# (Alstott et al., ref. 37). No version of that package is given. No code was read.
#
# Data the paper used. Three kinds of event sequence. (1) Neuronal spikes (refs. 38 and 39,
# Grosmark & Buzsaki 2016, DANDI 000044 version 0.210812.1516). These are electrophysiological
# recordings of pyramidal cells in rat hippocampus. Each session is two four-hour rest and sleep
# periods with a 45-minute exploration of a novel maze between them. The spike train of each
[... 339 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t1.py <<'EOF'
import numpy as np, powerlaw, warnings, time
from scipy.stats import zipf
warnings.simplefilter("ignore")
rng=np.random.default_rng(1)
for g in (2.5,3.3,3.8):
    x=zipf.rvs(g,size=20000,random_state=rng)
    for disc in (True,False):
        for pr in (None,{'alpha':[1,None]}):
            t=time.time()
            F=powerlaw.Fit(x,discrete=disc,verbose=False,parameter_ranges=pr)
            F1=powerlaw.Fit(x,discrete=disc,xmin=1,verbose=False,parameter_ranges=pr)
            R,p=F.distribution_compare('power_law','exponential')
            print(g,disc,pr,round(F.power_law.alpha,3),F.xmin,F.power_law.in_range(),"x1",round(F1.power_law.alpha,3),round(R,1),round(p,4),f"{time.time()-t:.2f}s")
EOF
python t1.py
```

```
2.5 True None 2.514 1.0 True x1 2.514 5696.4 0.0 0.06s
2.5 True {'alpha': [1, None]} 2.514 1.0 True x1 2.514 5696.4 0.0 0.06s
2.5 False None 2.727 7.0 True x1 3.0 213.4 0.0 0.04s
2.5 False {'alpha': [1, None]} 2.727 7.0 True x1 4.523 213.4 0.0 0.03s
3.3 True None 2.871 20.0 True x1 3.0 -0.8 0.3488 0.04s
3.3 True {'alpha': [1, None]} 3.304 1.0 True x1 3.304 1445.3 0.0 0.06s
3.3 False None 2.964 20.0 True x1 3.0 -0.7 0.439 0.04s
3.3 False {'alpha': [1, None]} 4.141 8.0 True x1 9.246 17.1 0.0005 0.03s
3.8 True None 3.0 17.0 True x1 3.0 -0.7 0.0274 0.04s
3.8 True {'alpha': [1, None]} 3.817 1.0 True x1 3.817 812.5 0.0 0.06s
3.8 False None 3.0 17.0 True x1 3.0 -0.8 0.0737 0.04s
3.8 False {'alpha': [1, None]} 4.584 5.0 True x1 14.345 20.4 0.0 0.03s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd executed/hiraoka-2025; python - <<'EOF'
import nbformat
for nb in ["model.ipynb","other_neurons.ipynb"]:
    n=nbformat.read(nb,4)
    for i,c in enumerate(n.cells):
        if c.cell_type=="code":
            print(f"=== {nb} [{i}]"); print(c.source)
            for o in c.get("outputs",[]):
                t=o.get("text") or o.get("data",{}).get("text/plain","")
                print("OUT:", t[:3500])
EOF
```

```
=== model.ipynb [1]
import time, resource, zlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import bursttree as bt

T0 = time.time()
pd.set_option("display.width", 200, "display.max_columns", 30, "display.max_rows", 300)
PAPER = "hiraoka-2025"
N, GAMMA = 10**6, 2.5
SERIES = ("linear", "quadratic", "exponential")
# Figure 4 legends: merging-number pairs delta = r * delta' per series.
RATIOS = {"linear": (1.8, 2.4, 3.3), "quadratic": (3.3, 5.9, 11.0), "exponential": (5.3, 12.0, 28.0)}
OFFSETS = (0, 1000, 2000, 3000, 4000)
def seed_of(claim):
    return zlib.crc32(f"{PAPER}/{claim}".encode())
=== model.ipynb [2]
print("dandiset", bt.DANDISET, "version", bt.DANDI_VERSION, "(not used by these claims)")
[... 372 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025 && python - <<'EOF'
p="bursttree.py"; s=open(p).read()
old='''# Claims file, O3: the four fit readings (xmin by KS or xmin = 1; discrete or continuous).
READINGS = {
    "ks_discrete": dict(xmin=None, discrete=True),
    "ks_continuous": dict(xmin=None, discrete=False),
    "x1_discrete": dict(xmin=1, discrete=True),
    "x1_continuous": dict(xmin=1, discrete=False),
}
'''
new='''# Claims file, O3: the four fit readings (xmin by KS or xmin = 1; discrete or continuous).
# Assumption, the range of the exponent (raised by the round-1 verifier). The locked release of
# powerlaw, 2.0.0, bounds the power-law alpha to [0, 3] by default (Power_Law.DEFAULT_PARAMETER_RANGES),
# so no fit can exceed 3, and its find_xmin discards every candidate xmin whose fit reaches the
# bound. The estimator the paper cites (Clauset et al., ref. 36, Section 3) has no upper bound,
# and neither had the package as its paper describes it (Alstott et al., ref. 37; releases 1.x
# require only alpha > 1). The paper gives no version. Adopted: alpha in [1, inf), the method as
# cited. The release's default cap is run as a variant, the same readings with suffix "_cap3".
ALPHA_RANGES = {"": {"alpha": [1, None]}, "_cap3": None}
_BASE_READINGS = {
    "ks_discrete": dict(xmin=None, discrete=True),
    "ks_continuous": dict(xmin=None, discrete=False),
    "x1_discrete": dict(xmin=1, discrete=True),
    "x1_continuous": dict(xmin=1, discrete=False),
}
READINGS = {name + sfx: dict(kw, parameter_ranges=pr)
            for sfx, pr in ALPHA_RANGES.items() for name, kw in _BASE_READINGS.items()}
ADOPTED_READINGS = tuple(_BASE_READINGS)                       # unbounded exponent
CAPPED_READINGS = tuple(r + "_cap3" for r in _BASE_READINGS)    # powerlaw 2.0.0 default, a variant
CAP = 3.0
'''
assert old in s; s=s.replace(old,new)
old='''    out.update(
        alpha=float(F.power_law.alpha),'''
new='''    a_ = float(F.power_law.alpha)
    out.update(
        alpha=a_,
        in_range=bool(F.power_law.in_range()),
        at_cap=bool(kw["parameter_ranges"] is None and a_ > CAP - 0.01),'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    lower cutoff and of discreteness are those of the claims file, O3.
    """''','''    lower cutoff and of discreteness are those of the claims file, O3; the range of the exponent
    is unbounded, or capped at 3 in the "_cap3" variants (see READINGS). `at_cap` marks a capped
    fit within 0.01 of the cap.
    """''')
s=s.replace('''        out.update(alpha=np.nan, sigma=np.nan, xmin=np.nan, n_tail=0, R=np.nan, p=np.nan, supported=False)''','''        out.update(alpha=np.nan, in_range=False, at_cap=False, sigma=np.nan, xmin=np.nan, n_tail=0, R=np.nan,
                   p=np.nan, supported=False)''')
old='''def unit_all_patterns(times_ms) -> list[dict]:
    """unit_pattern under both grids (O4) and the four fit readings (O3), for a worker pool."""
    out = []
    for g in GRIDS:
        for r in READINGS:'''
new='''def unit_all_patterns(times_ms, readings=ADOPTED_READINGS) -> list[dict]:
    """unit_pattern under both grids (O4) and the given fit readings (O3), for a worker pool."""
    out = []
    for g in GRIDS:
        for r in readings:'''
assert old in s; s=s.replace(old,new)
old='''    betas = [x["alpha"] for x in bf if np.isfinite(x["alpha"])]
    out.update(used=True, n_pairs=len(prs), b_supported=nb, k_supported=nk,'''
new='''    betas = [x["alpha"] for x in bf if np.isfinite(x["alpha"])]
    out.update(used=True, n_pairs=len(prs), b_supported=nb, k_supported=nk,
               n_at_cap=sum(x["at_cap"] for x in bf + kf), n_fits=len(bf) + len(kf),'''
assert old in s; s=s.replace(old,new)
open(p,"w").write(s)
EOF
grep -n "readings=tuple(READINGS)" bursttree.py
```

```
221:def analyse_sequence(times_ms, grid_name="b", ratios=NEURON_RATIOS, readings=tuple(READINGS),
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/t2.py <<'EOF'
import time, numpy as np, pandas as pd, pickle, os
import bursttree as bt
pd.set_option("display.width",250,"display.max_rows",300)
a=[a for a in bt.list_assets() if "Achilles-10252013" in a["path"]][0]
U=bt.load_units(bt.open_nwb(a["url"]))
spk=U["spikes"][9]*1e3
pickle.dump(dict(spk=spk, units=U), open(os.environ["TMPDIR"]+"/ach.pkl","wb"))
t=time.time(); r=bt.analyse_sequence(spk,"a"); print("grid a 8 readings", time.time()-t)
B=pd.DataFrame(r["bursts"]); B=B[B.on_grid]
print(B.pivot_table(index="delta",columns="reading",values="alpha").round(3).to_string())
print(B.groupby("reading")[["supported","at_cap","in_range"]].sum())
P=pd.DataFrame(r["pairs"])
print(P.groupby("reading").apply(lambda d: pd.Series(dict(n=len(d),sup=d.supported.sum(),cap=d.at_cap.sum(),med=d.alpha.median(),iqr=np.subtract(*np.percentile(d[d.supported].alpha,[75,25])) if d.supported.any() else np.nan))).round(3))
EOF
python $TMPDIR/t2.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t2.py", line 2, in <module>
    import bursttree as bt
ModuleNotFoundError: No module named 'bursttree'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/t2.py
```

```
grid a 8 readings 16.883996725082397
reading      ks_continuous  ks_continuous_cap3  ks_discrete  ks_discrete_cap3  x1_continuous  x1_continuous_cap3  x1_discrete  x1_discrete_cap3
delta                                                                                                                                          
55.250000            3.674               2.615        3.349             2.907          2.615               2.615        1.948             1.948
100.555000           2.878               2.878        2.684             2.684          2.313               2.313        1.825             1.825
183.010100           2.574               2.574        2.449             2.449          1.965               1.965        1.663             1.663
333.078382           2.433               2.433        2.308             2.308          1.750               1.750        1.549             1.549
606.202655           2.357               2.357        2.284             2.284          1.571               1.571        1.444             1.444
1103.288832          2.343               2.343        2.272             2.272          1.428               1.428        1.350             1.350
2007.985675          2.326               2.326        2.316             2.316          1.314               1.314        1.269             1.269
3654.533929          2.219               2.219        2.218             2.218          1.233               1.233        1.207             1.207
                    supported  at_cap  in_range
reading                                        
ks_continuous               8       0         8
ks_continuous_cap3          8       0         8
ks_discrete                 8       0         8
ks_discrete_cap3            8       0         8
x1_continuous               7       0         8
x1_continuous_cap3          7       0         8
x1_discrete                 5       0         8
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/t3.py <<'EOF'
import time, numpy as np, pickle, os
import bursttree as bt
U=pickle.load(open(os.environ["TMPDIR"]+"/ach.pkl","rb"))["units"]
idx=[i for i in range(len(U["id"])) if U["cell_type"][i]=="excitatory"][::15][:8]
for rd in (bt.ADOPTED_READINGS, bt.CAPPED_READINGS):
    t=time.time()
    for i in idx:
        rr=bt.unit_all_patterns(U["spikes"][i]*1e3, rd)
    print(rd[0], f"{(time.time()-t)/len(idx):.2f} s/unit", [ (r["reading"],r["grid"],r.get("pattern")) for r in rr][:4])
EOF
PYTHONPATH=. python $TMPDIR/t3.py
```

```
ks_discrete 5.81 s/unit [('ks_discrete', 'a', False), ('ks_continuous', 'a', False), ('x1_discrete', 'a', False), ('x1_continuous', 'a', True)]
ks_discrete_cap3 6.57 s/unit [('ks_discrete_cap3', 'a', False), ('ks_continuous_cap3', 'a', False), ('x1_discrete_cap3', 'a', False), ('x1_continuous_cap3', 'a', True)]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python - <<'EOF'
import nbformat
n=nbformat.read("reproduce_hiraoka_2025.ipynb",4)
for i in [0,1,15,17,20,23,26,29,32,35,37]:
    print(f"=== [{i}]"); print(n.cells[i].source)
EOF
```

```
=== [0]
# Reproducing Hiraoka & Jo (2025) on DANDI:000044: the representative neuron

Paper: Takayuki Hiraoka and Hang-Hyun Jo, "Hierarchical organization of bursty trains in event
sequences", doi:10.1063/5.0296506. The claims file (`claims/hiraoka-2025.yaml`) was written from
`paper/10.1063-5.0296506.txt`, whose body is the arXiv preprint (arXiv:2508.18281v1, dated
September 22, 2025); the paper has no supplement and links no code.

Dataset: DANDI:000044 (Grosmark and Buzsaki 2016), version 0.210812.1516, DOI
10.48324/dandi.000044/0.210812.1516. Why this version: the paper cites it (ref. 39,
https://dandiarchive.org/dandiset/000044/0.210812.1516), and the claims file gives it. Later
versions exist (latest 0.261106.0236); they re-export the files, renumber the units and rename
the cell types, which matters for finding "unit 9" (shown in the version check below). The spike
trains themselves are the same in the representative session.

Files are streamed from the archive with `remfile` and `h5py`; nothing is downloaded to disk.
The helper `bursttree.py` holds the loading, the burst and merging-number measures, the fits and
the paper's two algorithms, and says where each parameter comes from.

Notebooks of this entry: this one (data check and the representative neuron),
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def entry_hash" -A40 tools/entry.py | head -70; grep -n "max-minutes\|max_minutes" tools/entry.py | head
```

```
564:def entry_hash(entry_dir: Path) -> str:
565-    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
566-    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
567-    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
568-    import hashlib
569-    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
570-    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
571-        rel = path.relative_to(entry_dir)
572-        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
573-            continue
574-        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
575-    return h.hexdigest()
576-
577-
578-def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
579-    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
580-    the run left it, each within the time limit asked for now, and not older than REUSE_DAYS. Else None."""
581-    try:
582-        stamp = json.loads((output_dir / STAMP).read_text())
583-        entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025 && python - <<'EOF'
p="bursttree.py"; s=open(p).read()
old='''def unit_all_patterns(times_ms, readings=ADOPTED_READINGS) -> list[dict]:
    """unit_pattern under both grids (O4) and the given fit readings (O3), for a worker pool."""
    out = []
    for g in GRIDS:
        for r in readings:'''
new='''def unit_all_patterns(times_ms, readings=ADOPTED_READINGS, grids=tuple(GRIDS)) -> list[dict]:
    """unit_pattern under the given grids (O4) and fit readings (O3), for a worker pool."""
    out = []
    for g in grids:
        for r in readings:'''
assert old in s; s=s.replace(old,new)
s=s.replace('''def ccdf_at(x''','''def capped_patterns(times_ms) -> list[dict]:
    """The capped variant (powerlaw 2.0.0 default range) on grid (a) alone, for a worker pool."""
    return unit_all_patterns(times_ms, CAPPED_READINGS, ("a",))


def cdf_int(x: np.ndarray) -> np.ndarray:
    """Empirical CDF of positive integers at 0, 1, ..., max(x)."""
    c = np.bincount(x).cumsum()
    return c / c[-1]


def ks_d_int(c1: np.ndarray, c2: np.ndarray) -> float:
    """Two-sample KS statistic from two integer CDFs (cdf_int), padded with 1."""
    n = max(len(c1), len(c2))
    return float(np.abs(np.pad(c1, (0, n - len(c1)), constant_values=1) - np.pad(c2, (0, n - len(c2)), constant_values=1)).max())


def ccdf_at(x''')
open(p,"w").write(s)
EOF
python -c "import ast;ast.parse(open('entries/hiraoka-2025/bursttree.py').read())" 2>&1 || true
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import ast;ast.parse(open('entries/hiraoka-2025/bursttree.py').read())
                         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'entries/hiraoka-2025/bursttree.py'
```

**Agent**

Now the notebook edits.

**Agent calls Bash**

```bash
python -c "import ast;ast.parse(open('bursttree.py').read())" && python - <<'EOF'
import nbformat
p="reproduce_hiraoka_2025.ipynb"; n=nbformat.read(p,4)
c=n.cells[1]; c.source=c.source.replace('import bursttree as bt\n','import powerlaw\nimport bursttree as bt\n')+'\nprint("powerlaw", powerlaw.__version__, "; adopted readings (unbounded exponent):", bt.ADOPTED_READINGS, "; capped variant:", bt.CAPPED_READINGS)'
c=n.cells[15]
c.source+='''
# the exponent range (helper, READINGS): capped fits at the bound of powerlaw 2.0.0, and capped fits that differ from the unbounded ones
cap = []
for nm, D in (("bursts", B), ("pairs", P)):
    key_ = ["grid", "delta"] + (["dprime"] if nm == "pairs" else [])
    for r in bt.ADOPTED_READINGS:
        u = D[D.reading == r].set_index(key_).alpha; c3 = D[D.reading == r + "_cap3"].set_index(key_)
        cap.append(dict(fits=nm, reading=r, n=len(u), unbounded_above_3=int((u > 3).sum()), unbounded_max=round(u.max(), 3),
                        capped_at_bound=int(c3.at_cap.sum()), capped_differs_by_0_01=int(((c3.alpha - u).abs() > 0.01).sum())))
print("\\nexponent range, unbounded against capped at 3 (both grids, Figure 2 pairs included):"); print(pd.DataFrame(cap).to_string())
print("unbounded fits out of the range [1, inf):", int((~B[B.reading.isin(bt.ADOPTED_READINGS)].in_range).sum() + (~P[P.reading.isin(bt.ADOPTED_READINGS)].in_range).sum()))'''
nbformat.write(n,p)

p="other_neurons.ipynb"; n=nbformat.read(p,4)
for i in (0,2,4): print(f"--[{i}]\n", n.cells[i].source)
EOF
```

```
--[0]
 # Hiraoka & Jo (2025) on DANDI:000044: the other neurons

Paper: T. Hiraoka and H.-H. Jo, "Hierarchical organization of bursty trains in event
sequences", doi:10.1063/5.0296506, read from the arXiv preprint body under `paper/`.
Dataset: DANDI:000044 version 0.210812.1516, the version the paper cites (ref. 39); see the
header of `reproduce_hiraoka_2025.ipynb` for the choice of version and the claims table.
This notebook tests one claim, `fig2-other-neurons-similar`, which needs a fit of every
pyramidal unit and is kept apart for its run time (about 25 minutes on 4 processes).
--[2]
 ## Data check

The units tables of all eight sessions: counts by cell type, and spike trains that are not
sorted in time (the burst analysis sorts each train before taking IETs).
--[4]
 ## fig2-other-neurons-similar

> Other neurons of the recordings show patterns similar to the representative unit, with
> heavy-tailed burst-size and merging-number distributions across timescales.

[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p="other_neurons.ipynb"; n=nbformat.read(p,4)
n.cells[0].source=n.cells[0].source.replace("pyramidal unit and is kept apart for its run time (about 25 minutes on 4 processes).",
 "unit and is kept apart for its run time (about 45 minutes on 4 processes). Every unit of the\neight sessions is fitted, so that the claim's pyramidal sets can be shown beside the\ninhibitory units and all units (the paper's representative unit is labelled inhibitory).")
n.cells[3].source='''assets = bt.list_assets()
trains, rows = [], []
for a in assets:
    ses = a["path"].split("ses-")[1].split("_")[0]
    U = bt.load_units(bt.open_nwb(a["url"]))
    uns = [int(U["id"][i]) for i, s in enumerate(U["spikes"]) if np.any(np.diff(s) < 0)]
    rows.append(dict(session=ses, units=len(U["id"]), excitatory=int((U["cell_type"] == "excitatory").sum()),
                     inhibitory=int((U["cell_type"] == "inhibitory").sum()), unsorted_unit_ids=uns))
    for i, s in enumerate(U["spikes"]):
        trains.append(dict(session=ses, row=i, id=int(U["id"][i]), cell_type=U["cell_type"][i], n=len(s),
                           unsorted=int(U["id"][i]) in uns, spikes_ms=s * 1e3))
print(pd.DataFrame(rows).to_string())
print("units:", len(trains), "; by cell type:", pd.Series([t["cell_type"] for t in trains]).value_counts().to_dict(),
      "; with unsorted spike times:", [(t["session"], t["id"], t["cell_type"]) for t in trains if t["unsorted"]])
for ct in ("excitatory", "inhibitory"):
    ns = [t["n"] for t in trains if t["cell_type"] == ct]
    print(f"spikes per {ct} unit: min", min(ns), "median", int(np.median(ns)), "max", max(ns))'''
n.cells[4].source+='''

The adopted fit has no upper bound on the exponent (helper, `READINGS`). Beside the claim's sets,
the same summary is shown for the inhibitory units and for all units, of the representative
session and of every session, because the paper's own representative unit is labelled
inhibitory (a question to a reader on the claims file's "pyramidal"). The powerlaw 2.0.0 default,
with the exponent capped at 3, is a variant run on grid (a) alone, for run time.'''
n.cells[5].source='''t1 = time.time()
with ProcessPoolExecutor(max_workers=4) as ex:
    res = list(ex.map(bt.unit_all_patterns, [t["spikes_ms"] for t in trains], chunksize=2))
print(f"{len(trains)} units fitted (unbounded exponent, both grids) in {(time.time() - t1) / 60:.1f} min")
R = pd.DataFrame([dict(session=t["session"], id=t["id"], cell_type=t["cell_type"], n_spikes=t["n"], unsorted=t["unsorted"], **r)
                  for t, rr in zip(trains, res) for r in rr])

def summarise(d):
    used = d[d.used]
    return pd.Series(dict(units=len(d), used=len(used), pattern=int(used.pattern.sum()),
                          frac_pattern=round(used.pattern.mean(), 3) if len(used) else np.nan,
                          median_b_frac=round(used.b_frac.median(), 3), median_k_frac=round(used.k_frac.median(), 3),
                          beta_q25=round(used.median_beta.quantile(0.25), 3), beta_median=round(used.median_beta.median(), 3),
                          beta_q75=round(used.median_beta.quantile(0.75), 3)))

SETS = {"(a) pyramidal, Achilles-10252013": lambda d: d[(d.session == "Achilles-10252013") & (d.cell_type == "excitatory")],
        "(b) pyramidal, all sessions": lambda d: d[d.cell_type == "excitatory"],
        "variant: inhibitory, Achilles-10252013": lambda d: d[(d.session == "Achilles-10252013") & (d.cell_type == "inhibitory")],
        "variant: inhibitory, all sessions": lambda d: d[d.cell_type == "inhibitory"],
        "variant: all units, Achilles-10252013": lambda d: d[d.session == "Achilles-10252013"],
        "variant: all units, all sessions": lambda d: d}
for name, sel in SETS.items():
    print(f"\\nset {name}:")
    print(sel(R).groupby(["grid", "reading"]).apply(summarise).to_string())
Rb = SETS["(b) pyramidal, all sessions"](R)
print("\\nset (b) by session, fraction of used units showing the pattern:")
print(Rb[Rb.used].pivot_table(index="session", columns=["grid", "reading"], values="pattern", aggfunc="mean").round(3).to_string())
print("\\nset (b) by session, median over units of the median beta:")
print(Rb[Rb.used].pivot_table(index="session", columns=["grid", "reading"], values="median_beta", aggfunc="median").round(3).to_string())
print("\\nunits dropped (fewer than three grid points), by cell type:")
print(R[~R.used].groupby(["grid", "cell_type"]).id.count().to_string())
print("\\nwithout the units with unsorted spike times, set (b):")
print(Rb[~Rb.unsorted].groupby(["grid", "reading"]).apply(summarise)[["used", "pattern", "frac_pattern"]].to_string())'''
cap=nbformat.v4.new_markdown_cell('''### Variant: the exponent capped at 3 (powerlaw 2.0.0 default)

The same test with the release's default range of the exponent, [0, 3], on grid (a), with the
number of fits at the bound.''')
capc=nbformat.v4.new_code_cell('''t1 = time.time()
with ProcessPoolExecutor(max_workers=4) as ex:
    resc = list(ex.map(bt.capped_patterns, [t["spikes_ms"] for t in trains], chunksize=2))
print(f"{len(trains)} units fitted (capped exponent, grid a) in {(time.time() - t1) / 60:.1f} min")
RC = pd.DataFrame([dict(session=t["session"], id=t["id"], cell_type=t["cell_type"], n_spikes=t["n"], unsorted=t["unsorted"], **r)
                   for t, rr in zip(trains, resc) for r in rr])
for name, sel in SETS.items():
    d = sel(RC)
    s_ = d.groupby("reading").apply(summarise)[["used", "pattern", "frac_pattern", "beta_median"]]
    u_ = d[d.used].groupby("reading")[["n_at_cap", "n_fits"]].sum()
    print(f"\\nset {name}, capped, grid (a):"); print(s_.join(u_).to_string())''')
capc.metadata["tags"]=["claim:fig2-other-neurons-similar"]
n.cells[8].source='''used = R[R.used]
def parts(d):
    return d.assign(burst_ok=d.b_frac > 0.5, merge_ok=d.k_frac > 0.5).groupby(["grid", "reading"]).agg(
        used=("id", "size"), burst_ok=("burst_ok", "mean"), merge_ok=("merge_ok", "mean"), both=("pattern", "mean"))
for name, sel in SETS.items():
    print(f"\\nset {name}:"); print(parts(sel(used)).round(3).to_string())
print(f"\\nnotebook time {(time.time() - T0) / 60:.1f} min, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB (main process)")'''
n.cells.insert(7,cap); n.cells.insert(8,capc)
nbformat.write(n,p)
for i,c in enumerate(n.cells): print(i,c.cell_type,c.metadata.get("tags"),c.source[:60].replace("\n"," "))
EOF
```

```
0 markdown None # Hiraoka & Jo (2025) on DANDI:000044: the other neurons  Pa
1 code None import os os.environ.setdefault("OMP_NUM_THREADS", "1"); os.
2 markdown None ## Data check  The units tables of all eight sessions: count
3 code ['sanity'] assets = bt.list_assets() trains, rows = [], [] for a in ass
4 markdown None ## fig2-other-neurons-similar  > Other neurons of the record
5 code ['claim:fig2-other-neurons-similar'] t1 = time.time() with ProcessPoolExecutor(max_workers=4) as 
6 markdown None **Result: not reproduced under the discrete KS fit adopted h
7 markdown None ### Variant: the exponent capped at 3 (powerlaw 2.0.0 defaul
8 code ['claim:fig2-other-neurons-similar'] t1 = time.time() with ProcessPoolExecutor(max_workers=4) as 
9 markdown None ### Burst sizes and merging numbers taken apart  The pattern
10 code None used = R[R.used] def parts(d):     return d.assign(burst_ok=
11 markdown None **Result (parts).** Under the discrete KS fit, the burst-siz
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p="other_neurons.ipynb"; n=nbformat.read(p,4)
r=n.cells.pop(6); n.cells.insert(8,r); nbformat.write(n,p)
p="model.ipynb"; n=nbformat.read(p,4)
for i in (0,3,5,7,10,12): print(f"--[{i}]\n", n.cells[i].source)
EOF
```

```
--[0]
 # Hiraoka & Jo (2025): the dynamic generative algorithms (Section IV, Figure 4)

Paper: T. Hiraoka and H.-H. Jo, "Hierarchical organization of bursty trains in event
sequences", doi:10.1063/5.0296506, read from the arXiv preprint body under `paper/`.
These claims are `data: elsewhere` in the claims file: their data are not deposited and are
generated here by the paper's Algorithms 1 and 2, for which no code is linked. They do not use
DANDI:000044 (version 0.210812.1516, the subject of `reproduce_hiraoka_2025.ipynb`); the helper
names it, and the sanity cell below only checks that the pinned version is reachable.

Set-up from Section IV, paragraph 9: n = 10^6 events, gamma = 2.5, delta_0 = 1, uniform IETs
(Eq. 10), linear (Eq. 12) and quadratic (Eq. 13) timescales with w = 100, exponential (Eq. 14)
with w = 2, merging numbers zeta-distributed (Eq. 15) with the memory function of Eq. 16 for the
incremental algorithm (Algorithm 2), which Figure 4 uses.

Claims tested here: fig4-model-heavy-tails, fig4-model-iet-shapes, model-decremental-equivalent.
--[3]
 ## fig4-model-heavy-tails

> Event sequences generated by the incremental dynamic algorithm, with linear, quadratic or
[... 58 more lines not kept]
```

**Agent**

Now the model notebook edits (cap variant in cell 4, permutation test in cell 11).

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p="model.ipynb"; n=nbformat.read(p,4)
c=n.cells[4]
old='''        for g in (("a", "b") if off == 0 else ("a",)):
            res = bt.analyse_sequence(t, g, ratios=RATIOS[s])'''
new='''        for g in (("a", "b") if off == 0 else ("a",)):
            # unbounded exponent (adopted) under every seed; the capped variant (powerlaw 2.0.0 default) under the claim's seed, grid (a)
            rd = bt.ADOPTED_READINGS + (bt.CAPPED_READINGS if (off == 0 and g == "a") else ())
            res = bt.analyse_sequence(t, g, ratios=RATIOS[s], readings=rd)'''
assert old in c.source; c.source=c.source.replace(old,new)
old='''        out.append(dict(reading=r, n_delta=len(b),'''
new='''        out.append(dict(reading=r, n_at_cap=int(b.at_cap.sum() + p.at_cap.sum()), n_delta=len(b),'''
assert old in c.source; c.source=c.source.replace(old,new)
c.source=c.source.replace('''one = H.groupby(["seed", "grid", "reading"]).holds.all().unstack("reading")''','''one = H.groupby(["seed", "grid", "reading"]).holds.all().unstack("reading")
print("\\nholds for each series, by reading and seed (grid a):"); print(H[H.grid == "a"].pivot_table(index=["seed", "series"], columns="reading", values="holds", aggfunc="first").to_string())
print("\\nexponential series, gamma interquartile range by reading and seed (grid a):"); print(H[(H.grid == "a") & (H.series == "exponential")].pivot_table(index="seed", columns="reading", values="gamma_iqr").to_string())''')
n.cells[3].source=n.cells[3].source.replace("run; under the four further seeds, grid (a) with all four readings (a choice for run time).",
 "run, with the exponent unbounded, and on grid (a) also with the exponent capped at 3 (powerlaw\n2.0.0 default, a variant); under the four further seeds, grid (a) with the four unbounded readings\n(a choice for run time).")
c=n.cells[11]
old='''            ta, tb = np.diff(ti), np.diff(td)'''
new='''            ta, tb = np.diff(ti), np.diff(td)
            RUNS.setdefault((v, s), {"inc": [], "other": []}); RUNS[(v, s)]["inc"].append(ta); RUNS[(v, s)]["other"].append(tb)'''
assert old in c.source; c.source=c.source.replace(old,new)
c.source=c.source.replace('''rows = []
t1 = time.time()''','''rows = []
RUNS = {}  # IETs of every run, kept for the calibrated test below
t1 = time.time()''',1)
c.source=c.source.replace('''\nprint(f"\\nnotebook time''','''\nprint(f"\\ntime so far''')
n.cells[11].source=c.source
md=nbformat.v4.new_markdown_cell('''### Variant: a test calibrated across independent runs

The criterion's KS test treats every burst of one run as an independent draw, which the
reference N shows is not so: two runs of the same algorithm differ at p as low as 10^-164. As a
variant asked for by the verifier (not the criterion), each algorithm is taken as five
independent runs (the five seeds), and runs, not bursts, are the units of the test. At each
point of grid (a) of the claim's-seed incremental run, the KS distance D is taken between every
two of the ten runs. The statistic is the mean D between runs of different algorithms less the
mean D between runs of the same algorithm, averaged over the timescales. Its null is the 126
distinct splits of the ten runs into two groups of five (an exact permutation test; the
smallest possible p is 1/126 = 0.0079). Bonferroni over the three series. N is the check that
the test does not reject two runs of one algorithm.''')
code=nbformat.v4.new_code_cell('''from itertools import combinations
splits = [set(c_) for c_ in combinations(range(10), 5) if 0 in c_]  # 126 distinct splits
perm = []
for (v, s), rr in RUNS.items():
    runs = rr["inc"] + rr["other"]
    lo, hi = bt.relevant_range(runs[0])
    G = [d for d in bt.grid(lo, hi, "a") if all(len(bt.burst_sizes(x, d)) >= bt.MIN_BURSTS for x in runs)]
    Dm = np.zeros((len(G), 10, 10))
    for gi, d in enumerate(G):
        cd = [bt.cdf_int(bt.burst_sizes(x, d)) for x in runs]
        for i, j in combinations(range(10), 2):
            Dm[gi, i, j] = Dm[gi, j, i] = bt.ks_d_int(cd[i], cd[j])
    Dbar = Dm.mean(axis=0)
    def stat(A):
        B_ = [i for i in range(10) if i not in A]; A = sorted(A)
        between = Dbar[np.ix_(A, B_)].mean()
        within = np.mean([Dbar[i, j] for grp in (A, B_) for i, j in combinations(grp, 2)])
        return between - within
    obs = stat({0, 1, 2, 3, 4}); null = np.array([stat(A) for A in splits])
    p = float((null >= obs - 1e-15).mean())
    perm.append(dict(variant=v, series=s, n_timescales=len(G), D_between=round(Dbar[:5, 5:].mean(), 4),
                     D_within_inc=round(Dbar[:5, :5][np.triu_indices(5, 1)].mean(), 4), D_within_other=round(Dbar[5:, 5:][np.triu_indices(5, 1)].mean(), 4),
                     stat=round(obs, 4), p=round(p, 4), p_bonf=round(min(1, 3 * p), 4), differ=bool(3 * p < 0.05)))
PM = pd.DataFrame(perm); print(PM.to_string())
print("\\nseries where the runs differ (Bonferroni p < 0.05), by variant:", PM.groupby("variant").differ.sum().to_dict())
del RUNS
print(f"\\nnotebook time {(time.time() - T0) / 60:.1f} min, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")''')
code.metadata["tags"]=["claim:model-decremental-equivalent"]
n.cells.insert(12,md); n.cells.insert(13,code)
nbformat.write(n,p)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/t4.py <<'EOF'
import numpy as np, pandas as pd, time
from itertools import combinations
import bursttree as bt
t0=time.time()
RUNS={}
for off in range(5):
    for v in ("L","N"):
        s="linear"
        ta=np.diff(bt.simulate_incremental(10**5,s,2.5,np.random.default_rng(off*2)))
        rng2=np.random.default_rng(off*2+1)
        tb=np.diff(bt.simulate_decremental(10**5,s,2.5,rng2) if v=="L" else bt.simulate_incremental(10**5,s,2.5,rng2))
        RUNS.setdefault((v, s), {"inc": [], "other": []}); RUNS[(v, s)]["inc"].append(ta); RUNS[(v, s)]["other"].append(tb)
splits = [set(c_) for c_ in combinations(range(10), 5) if 0 in c_]
print(len(splits))
for (v, s), rr in RUNS.items():
    runs = rr["inc"] + rr["other"]
    lo, hi = bt.relevant_range(runs[0])
    G = [d for d in bt.grid(lo, hi, "a") if all(len(bt.burst_sizes(x, d)) >= bt.MIN_BURSTS for x in runs)]
    Dm = np.zeros((len(G), 10, 10))
    for gi, d in enumerate(G):
        cd = [bt.cdf_int(bt.burst_sizes(x, d)) for x in runs]
        for i, j in combinations(range(10), 2):
            Dm[gi, i, j] = Dm[gi, j, i] = bt.ks_d_int(cd[i], cd[j])
    Dbar = Dm.mean(axis=0)
    def stat(A):
        B_ = [i for i in range(10) if i not in A]; A = sorted(A)
        return Dbar[np.ix_(A, B_)].mean() - np.mean([Dbar[i, j] for grp in (A, B_) for i, j in combinations(grp, 2)])
    obs = stat({0, 1, 2, 3, 4}); null = np.array([stat(A) for A in splits])
    print(v, s, len(G), round(obs,4), (null >= obs - 1e-15).mean())
from scipy.stats import ks_2samp
b1=bt.burst_sizes(RUNS[("L","linear")]["inc"][0],G[0]); b2=bt.burst_sizes(RUNS[("L","linear")]["other"][0],G[0])
print(ks_2samp(b1,b2).statistic, bt.ks_d_int(bt.cdf_int(b1),bt.cdf_int(b2)), time.time()-t0)
EOF
PYTHONPATH=. python $TMPDIR/t4.py
```

```
126
L linear 4 0.1615 0.007936507936507936
N linear 4 -0.0017 0.9682539682539683
0.12602617101027125 0.12602617101027125 6.964706659317017
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/dev/bin/activate && mkdir -p $TMPDIR/devout && cd entries/hiraoka-2025 && for nb in reproduce_hiraoka_2025 other_neurons model; do (jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=-1 --output-dir $TMPDIR/devout $nb.ipynb > $TMPDIR/devout/$nb.log 2>&1; echo "$nb exit $? $(date -u +%H:%M)") & done; wait; date -u; tail -3 $TMPDIR/devout/*.log
```

```
Exit code 1
Sun Nov 22 00:40:58 UTC 2026
reproduce_hiraoka_2025 exit 0 00:48
model exit 0 01:20
other_neurons exit 0 01:49
Sun Nov 22 01:49:27 UTC 2026
error: unexpected argument '-3' found

  tip: to pass '-3' as a value, use '-- -3'

Usage: tail [OPTION]... [FILE]...

For more information, try '--help'.
```

**Agent**

The development run finished at 01:49 UTC with all three notebooks passing. other_neurons took 68 minutes running alongside the others, so it should be shorter alone. Reading the outputs now.

**Agent calls Bash**

```bash
cd $TMPDIR/devout && cat > $TMPDIR/show.py <<'EOF'
import nbformat, sys
n=nbformat.read(sys.argv[1],4)
cells=[int(x) for x in sys.argv[2].split(",")] if len(sys.argv)>2 else range(len(n.cells))
for i in cells:
    c=n.cells[i]
    if c.cell_type!="code": continue
    print(f"=== [{i}]")
    for o in c.get("outputs",[]):
        t=o.get("text") or o.get("data",{}).get("text/plain","") or str(o.get("evalue",""))
        print(t)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/show.py reproduce_hiraoka_2025.ipynb 1,15,17
```

```
=== [1]
dandiset 000044 version 0.210812.1516
powerlaw 2.0.0 ; adopted readings (unbounded exponent): ('ks_discrete', 'ks_continuous', 'x1_discrete', 'x1_continuous') ; capped variant: ('ks_discrete_cap3', 'ks_continuous_cap3', 'x1_discrete_cap3', 'x1_continuous_cap3')

=== [15]
fits done in 304 s
relevant timescales: 55.25 ms (smallest delta with a burst of >= 100 events) to 6282.75 ms (the 99th largest IET; delta must stay below it for >= 100 bursts)
paper (Figure 2 labels): about 55 to 6300 ms
grid (a): 8 points, step log10 0.2601: [  55.2  100.6  183.   333.1  606.2 1103.3 2008.  3654.5]
grid (b): 40 points, step log10 0.0514: [  55.2   62.2   70.    78.8   88.7   99.8  112.4  126.5  142.4  160.3
  180.4  203.1  228.6  257.3  289.6  326.   367.   413.1  465.   523.4
  589.2  663.2  746.5  840.3  945.9 1064.7 1198.4 1349.  1518.5 1709.2
 1924.  2165.7 2437.7 2744.  3088.7 3476.7 3913.5 4405.2 4958.6 5581.5]
fits with a failed test (R or p not finite): 0 of 2096

exponent range, unbounded against capped at 3 (both grids, Figure 2 pairs included):
     fits        reading    n  unbounded_above_3  unbounded_max  capped_at_bound  capped_differs_by_0_01
0  bursts    ks_discrete  156                  4          3.358                0                       4
1  bursts  ks_continuous  156                  7          3.694                1                       7
2  bursts    x1_discrete  156                  0          1.948                0                       0
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/devout && . $TMPDIR/dev/bin/activate; python $TMPDIR/show.py reproduce_hiraoka_2025.ipynb 20,23 | grep -v "^$" | head -120
```

```
=== [20]
   grid             reading   n  median    min    max  range  max_sigma  n_in_band  first_delta_all_in_band_after  all_in_band  median_in_band_range_ok
0     a       ks_continuous   7   2.433  2.326  3.674  1.348      0.061          5                          183.0        False                    False
1     a  ks_continuous_cap3   7   2.433  2.326  2.878  0.552      0.061          5                          183.0        False                    False
2     a         ks_discrete   7   2.316  2.272  3.349  1.077      0.061          5                          183.0        False                    False
3     a    ks_discrete_cap3   7   2.316  2.272  2.907  0.635      0.061          5                          183.0        False                    False
4     a       x1_continuous   7   1.750  1.314  2.615  1.301      0.007          1                            NaN        False                    False
5     a  x1_continuous_cap3   7   1.750  1.314  2.615  1.301      0.007          1                            NaN        False                    False
6     a         x1_discrete   7   1.549  1.269  1.948  0.679      0.006          0                            NaN        False                    False
7     a    x1_discrete_cap3   7   1.549  1.269  1.948  0.679      0.006          0                            NaN        False                    False
8     b       ks_continuous  34   2.411  2.314  3.674  1.360      0.088         24                          180.4        False                    False
9     b  ks_continuous_cap3  34   2.411  2.314  2.999  0.685      0.088         24                          180.4        False                    False
10    b         ks_discrete  34   2.354  2.270  3.349  1.079      0.088         27                          126.5        False                    False
11    b    ks_discrete_cap3  34   2.354  2.270  2.975  0.705      0.088         27                          126.5        False                    False
12    b       x
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/devout && . $TMPDIR/dev/bin/activate; python $TMPDIR/show.py reproduce_hiraoka_2025.ipynb 26,29,32,35,38 | grep -v "^$" | grep -v "^[0-9]* *[ab] *[a-z_0-9]* *[0-9.]* *[0-9.]* *[0-9.]* *[0-9.]* *[0-9.]* *[0-9.]* *[0-9.]* *\(True\|False\) *\(True\|False\)$" | head -150
```

```
=== [26]
pairs: 15; points where all CCDFs exceed 1e-3: 123 (k/<k> from 0.010 to 11.62)
largest ratio between the highest and lowest CCDF at those points: 12.54 at k/<k> = 10.35; median ratio 1.63
(a) holds: False
in the tail alone (k/<k> >= 1): max ratio 12.54
              reading  median  max_dev  within_05  supported  m_min
0       ks_continuous   2.779    1.742      False         14     89
1  ks_continuous_cap3   2.752    0.626      False         15     89
2         ks_discrete   2.610    0.538      False         15     89
3    ks_discrete_cap3   2.610    0.490       True         15     89
4       x1_continuous   1.828    1.249      False         12     89
5  x1_continuous_cap3   1.828    1.172      False         12     89
6         x1_discrete   1.592    0.521      False          6     89
7    x1_discrete_cap3   1.592    0.521      False          6     89
reading       ks_continuous  ks_continuous_cap3  ks_discrete  ks_discrete_cap3  x1_continuous  x1_continuous_cap3  x1_discrete  x1_discrete_cap3
dprime ratio                                                                                                                                    
55.0   3.3            3.109               2.963        2.648             2.648          3.076               3.000        2.112             2.112
       5.9            2.779               2.779        2.517             2.517          2.344               2.344        1.838             1.838
       11.0           2.487               2.487        2.375             2.375          1.878               1.878        1.618             1.618
100.0  3.3            3.282               2.752        2.872             2.872          2.752               2.752        1.999             1.999
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/devout && . $TMPDIR/dev/bin/activate; python $TMPDIR/show.py reproduce_hiraoka_2025.ipynb 29 | head -18; python $TMPDIR/show.py reproduce_hiraoka_2025.ipynb 32,35,38
```

```
=== [29]
   grid             reading  n_pairs  both_gt2  eq8_within10  median_rel_err  cond1  cond2
0     a       ks_continuous       15        15             9           0.085   True   True
1     a  ks_continuous_cap3       15        15            11           0.067   True   True
2     a         ks_discrete       15        15            12           0.058   True   True
3     a    ks_discrete_cap3       15        15            12           0.058   True   True
4     a       x1_continuous       15         4             1           0.171  False  False
5     a  x1_continuous_cap3       15         4             1           0.171  False  False
6     a         x1_discrete       15         0             2           0.126  False  False
7     a    x1_discrete_cap3       15         0             2           0.126  False  False
8     b       ks_continuous       76        76            45           0.089   True   True
9     b  ks_continuous_cap3       76        76            48           0.084   True   True
10    b         ks_discrete       76        76            58           0.067   True   True
11    b    ks_discrete_cap3       76        76            58           0.067   True   True
12    b       x1_continuous       76        17             6           0.163  False  False
13    b  x1_continuous_cap3       76        17             6           0.163  False  False
14    b         x1_discrete       76         0            20           0.120  False  False
15    b    x1_discrete_cap3       76         0            20           0.120  False  False
=== [32]
   grid             reading  pairs_below3000  beta_dprime_lt_gamma  cond1  n_grid_above3000  rho_beta  p_beta cond2                                                                          gamma_by_ratio cond3
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/devout && . $TMPDIR/dev/bin/activate; python $TMPDIR/show.py other_neurons.ipynb
```

```
=== [1]
dandiset 000044 version 0.210812.1516

=== [3]
             session  units  excitatory  inhibitory unsorted_unit_ids
0  Achilles-10252013    137         120          17                []
1  Achilles-11012013    104          92          12                []
2     Buddy-06272013     68          48          20               [2]
3    Cicero-09012014     73          55          18               [2]
4    Cicero-09102014    105          81          24                []
5    Cicero-09172014     72          59          13                []
6    Gatsby-08022013     80          66          14               [2]
7    Gatsby-08282013     51          41          10                []
units: 690 ; by cell type: {np.str_('excitatory'): 562, np.str_('inhibitory'): 128} ; with unsorted spike times: [('Buddy-06272013', 2, np.str_('excitatory')), ('Cicero-09012014', 2, np.str_('excitatory')), ('Gatsby-08022013', 2, np.str_('inhibitory'))]
spikes per excitatory unit: min 2130 median 18690 max 134385
spikes per inhibitory unit: min 14678 median 311058 max 1102265

=== [5]
690 units fitted (unbounded exponent, both grids) in 57.8 min

[... 242 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/devout && . $TMPDIR/dev/bin/activate; python $TMPDIR/show.py model.ipynb 4,11,13
```

```
=== [4]
seed offset 0 done, 14.2 min

seed offset 1000 done, 16.8 min

seed offset 2000 done, 18.9 min

seed offset 3000 done, 21.2 min

seed offset 4000 done, 23.7 min
          seed       series grid     lo       hi             reading  n_at_cap  n_delta  b_supported  n_pairs  k_supported  beta_median  beta_iqr  gamma_median  gamma_iqr  holds
0   4174482686       linear    a  92.19    853.1       ks_continuous         0        4            3        8            8        2.516     1.327         2.351      0.227  False
1   4174482686       linear    a  92.19    853.1  ks_continuous_cap3         0        4            4        8            8        2.516     0.538         2.351      0.227  False
2   4174482686       linear    a  92.19    853.1         ks_discrete         0        4            4        8            8        2.203     0.183         2.320      0.249   True
3   4174482686       linear    a  92.19    853.1    ks_discrete_cap3         0        4            4        8            8        2.203     0.183         2.320      0.249   True
4   4174482686       linear    a  92.19    853.1       x1_continuous         0        4            4        8            8        1.916     0.875         1.893      0.828  False
5   4174482686       linear    a  92.19    853.1  x1_continuous_cap3         2        4            4        8            8        1.916     0.817         1.893      0.828  False
6   4174482686       linear    a  92.19    853.1         x1_discrete         0        4            4        8            7        1.629     0.429         1.626      0.397   True
7   4174482686       linear    a  92.19    853.1    x1_discrete_cap3         0        4            4        8            7        1.629     0.429         1.626      0.397   True
8   4174482686       linear    b  92.19    853.1       ks_continuous         0       19           18       35           33        2.505     0.356         2.429      0.563  False
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/hiraoka-2025 && python - <<'EOF'
import nbformat, copy
p="other_neurons.ipynb"; n=nbformat.read(p,4)
# new notebook for the capped variant
m=nbformat.v4.new_notebook(); m.metadata=copy.deepcopy(n.metadata)
hdr=nbformat.v4.new_markdown_cell('''# Hiraoka & Jo (2025) on DANDI:000044: the other neurons, exponent capped at 3 (a variant)

Paper: T. Hiraoka and H.-H. Jo, "Hierarchical organization of bursty trains in event
sequences", doi:10.1063/5.0296506, read from the arXiv preprint body under `paper/`.
Dataset: DANDI:000044 version 0.210812.1516, the version the paper cites (ref. 39); see the
header of `reproduce_hiraoka_2025.ipynb` for the choice of version and the claims table.
This notebook is a variant of `other_neurons.ipynb` for `fig2-other-neurons-similar`: the same
test with the default range of the exponent of powerlaw 2.0.0, [0, 3], which the adopted fit
does not use (helper, `READINGS`). It runs on grid (a) alone, for run time (about 11 minutes on
4 processes), and counts the fits at the bound.''')
m.cells=[hdr, copy.deepcopy(n.cells[1]), copy.deepcopy(n.cells[2]), copy.deepcopy(n.cells[3])]
m.cells[1].source=m.cells[1].source.replace('import bursttree as bt','import powerlaw\nimport bursttree as bt')+'\nprint("powerlaw", powerlaw.__version__, "; capped readings:", bt.CAPPED_READINGS)'
summ=n.cells[5].source.split("def summarise")[1].split("Rb = SETS")[0]
code=copy.deepcopy(n.cells[8])
code.source="def summarise"+summ.split("for name, sel in SETS.items():")[0]+code.source+'''
print(f"\\nnotebook time {(time.time() - T0) / 60:.1f} min, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB (main process)")'''
md=nbformat.v4.new_markdown_cell('''## fig2-other-neurons-similar, exponent capped at 3

The criterion as in `other_neurons.ipynb`, on grid (a), with the sets of that notebook.''')
m.cells += [md, code]
nbformat.write(m,"other_neurons_cap3.ipynb")
# remove from other_neurons
del n.cells[6:9]
nbformat.write(n,p)
for i,c in enumerate(n.cells): print(i,c.cell_type,c.source[:70].replace("\n"," "))
print(m.cells[5].source[:2500])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

The clock reads 01:51 UTC, more time than I had estimated. I also copied the wrong cell into the capped notebook, so I'm rebuilding that cell.

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
m=nbformat.read("other_neurons_cap3.ipynb",4)
n=nbformat.read("other_neurons.ipynb",4)
summ="def summarise"+n.cells[5].source.split("def summarise")[1].split("for name, sel in SETS.items():")[0]
c=nbformat.v4.new_code_cell(summ+'''t1 = time.time()
with ProcessPoolExecutor(max_workers=4) as ex:
    resc = list(ex.map(bt.capped_patterns, [t["spikes_ms"] for t in trains], chunksize=2))
print(f"{len(trains)} units fitted (capped exponent, grid a) in {(time.time() - t1) / 60:.1f} min")
RC = pd.DataFrame([dict(session=t["session"], id=t["id"], cell_type=t["cell_type"], n_spikes=t["n"], unsorted=t["unsorted"], **r)
                   for t, rr in zip(trains, resc) for r in rr])
for name, sel in SETS.items():
    d = sel(RC)
    s_ = d.groupby("reading").apply(summarise)[["used", "pattern", "frac_pattern", "beta_median"]]
    u_ = d[d.used].groupby("reading")[["n_at_cap", "n_fits"]].sum()
    print(f"\\nset {name}, capped, grid (a):"); print(s_.join(u_).to_string())
print(f"\\nnotebook time {(time.time() - T0) / 60:.1f} min, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB (main process)")''')
c.metadata["tags"]=["claim:fig2-other-neurons-similar"]
m.cells[5]=c
nbformat.write(m,"other_neurons_cap3.ipynb")
for i,x in enumerate(m.cells): print(i,x.cell_type,x.metadata.get("tags"),x.source[:80].replace("\n"," "))
EOF
```

```
0 markdown None # Hiraoka & Jo (2025) on DANDI:000044: the other neurons, exponent capped at 3 (
1 code None import os os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("
2 markdown None ## Data check  The units tables of all eight sessions: counts by cell type, and 
3 code ['sanity'] assets = bt.list_assets() trains, rows = [], [] for a in assets:     ses = a["pa
4 markdown None ## fig2-other-neurons-similar, exponent capped at 3  The criterion as in `other_
5 code ['claim:fig2-other-neurons-similar'] def summarise(d):     used = d[d.used]     return pd.Series(dict(units=len(d), u
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
n=nbformat.read("reproduce_hiraoka_2025.ipynb",4)
for i in (10,14,16,18,19,22,25,33,36): print(f"--[{i}]\n"+n.cells[i].source)
EOF
```

```
--[10]
**Result: reproduced.** Under reading (b) of O1, row 9 of the units table counted from 0 (unit id
18), the unit has 228 356 spikes, tau_min 1.050 ms and tau_max 18 229.7 ms, all within tolerance,
and it is the only unit of the session that matches. Readings (a), (c) and (d) do not match. The
files label this unit `inhibitory` (`interneuron` in the latest version), while the paper
describes its neuronal data as pyramidal cells. In the latest version the same row has id 119 and
no unit has id 9.
--[14]
## Bursts and merging numbers of the representative unit

Relevant timescales, grids, bursts and fits as in the Methods and in O3 and O4 of the claims
file (the helper says where each detail comes from). Both grids are run under the four fit
readings. The pairs of Figure 2 (delta' = 55, 100, 180, 330, 590 ms; delta = 3.3, 5.9 and 11
delta') are added as fixed pairs for fig2-neuron-merging-collapse.
--[16]
## fig2-neuron-burst-size-heavy-tail

> For the representative neuron, the burst size distributions are heavy-tailed across different
> timescales.

[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p="reproduce_hiraoka_2025.ipynb"; n=nbformat.read(p,4)
C=n.cells
C[14].source=C[14].source.replace("Both grids are run under the four fit\nreadings.","Both grids are run under the four fit\nreadings, each with the exponent unbounded (adopted) and capped at 3 (suffix `_cap3`, the default of\nthe locked powerlaw 2.0.0; helper, `READINGS`).")
C[18].source='''**Result: reproduced.** With xmin chosen by the KS distance, discrete or continuous, the power
law is supported at every relevant timescale on both grids (8 of 8 on grid (a), 40 of 40 on grid
(b)), so at every one below 3000 ms, with the exponent unbounded or capped. The claim holds under
one reading of O3, as the claims file's rule asks. With xmin = 1 the discrete fit is supported at
5 of 8 and 29 of 40 timescales, not all below 3000 ms; the continuous fit at 7 of 8 (all 7 below
3000 ms) on grid (a) and 32 of 40 (32 of 34 below 3000 ms) on grid (b). The shuffled-IET
reference has no supported timescale under any of the five seeds (0 of 5 or 6).'''
C[21].source='''**Result: not reproduced.** Neither reading of the criterion holds under any fit or grid. Under
the discrete KS fit on grid (b) the median beta below 3000 ms is 2.354, inside the band, and 27
of 34 estimates lie within 2.35 +/- 0.235, every one from 126.5 ms to 3000 ms (1.4 decades). At
the lower end beta is higher (3.349 at 55 ms), so the range is 1.079 against the 0.47 of reading
(b). With the exponent unbounded the ranges are 0.679 to 1.360 over the fits and grids (medians
2.316 to 2.433 under the KS fits, 1.521 to 1.750 with xmin = 1). Capped at 3, the KS ranges are
0.552 to 0.705, which still fail. The standard errors are at most 0.088.'''
C[24].source='''**Result: reproduced, under the discrete KS fit.** With the exponent unbounded, the discrete KS
fit supports the power law for 13 of 15 pairs (grid (a)) and 70 of 76 (grid (b)), and the gamma of
the supported pairs has an interquartile range of 0.378 and 0.415 (median 2.618 and 2.644). The
continuous KS fit supports 15 of 15 and 69 of 76, but its interquartile range is 0.642 and 0.546;
capped at 3 it was 0.408 and 0.426, so the cap decides that reading but not the discrete one
(0.383 and 0.401 capped). With xmin = 1 the discrete fit is supported for 6 of 15 and 19 of 76
pairs, and the continuous fit has an interquartile range of 0.673 and 0.597.'''
C[27].source='''**Result: not reproduced with the exponent unbounded (an assumption); reproduced only when it is
capped at 3.** Reading (b): with the exponent unbounded, the gamma of the 15 pairs of Figure 2
lie up to 0.538 from their median under the discrete KS fit (median 2.610), 1.742 under the
continuous KS fit, 0.521 under the discrete fit from xmin = 1 and 1.249 under the continuous one,
all outside the band of 0.5. The deviation of 0.538 is the pair delta' 180 ms, delta 594 ms
(gamma 3.148), which the cap holds at 2.843, giving the 0.490 of the capped discrete KS fit, the
only fit within the band. Reading (a) fails: the CCDFs of k / <k> differ by up to a factor of
12.54 (median 1.63) where all exceed 10^-3. One pair of Figure 2 (delta' 590 ms, delta 6490 ms)
lies above the relevant range, with 89 bursts.'''
C[30].source='''**Result: reproduced, under the KS fits.** Both gamma and beta(delta') exceed 2 in 15 of 15 pairs
on grid (a) and 76 of 76 on grid (b), and with the exponent unbounded beta(delta) is within 10% of
min(gamma, beta(delta')) in 9 (continuous) and 12 (discrete) of 15 and in 45 and 58 of 76 pairs
(median relative error 0.058 to 0.089); capped, in 11 and 12 of 15 and 48 and 58 of 76. Under
xmin = 1 both conditions fail (both above 2 in 0 to 17 pairs).'''
C[33].source='''**Result: reproduced, on grid (b) under the KS readings of the fit; not judged on grid (a).** For
pairs with delta < 3000 ms, beta(delta') < gamma in 40 of 57 under both KS fits with the
exponent unbounded (38 for the capped continuous fit). Above 3000 ms grid (b) has 6 points; beta
falls from 2.064 to 1.867 (discrete fit), Spearman rho = -0.829 (p = 0.0416), and gamma falls
with delta for each ratio (rho -0.714, -0.964 and -0.943). Grid (a) has one point above 3000 ms,
so parts (2) and (3) are not judged there; its part (1) holds (7 of 12). Under xmin = 1, part
(1) fails (24 of 57) while parts (2) and (3) hold. Part (2) rests on 6 points at p = 0.0416.'''
C[36].source='''### Note on the variant

Taken epoch by epoch, the representative unit has 96 875 spikes in the first rest period, 44 099
in the maze and 87 382 in the second rest period, which sum to the 228 356 of Figure 2: the
paper used the whole session (O2). The maze epoch alone has a relevant range of only 55.2 to
812.3 ms and a median beta below 3000 ms of 1.776 to 1.950; the rest periods give 2.499 to 2.829.'''
nbformat.write(n,p)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p="reproduce_hiraoka_2025.ipynb"; n=nbformat.read(p,4)
note=nbformat.v4.new_markdown_cell('''**The range of the exponent.** The locked powerlaw 2.0.0 caps the power-law exponent at 3 by
default, and its choice of xmin by the KS distance discards every candidate whose fit reaches the
cap. The table above compares the capped fits with the unbounded ones adopted here: under the
discrete KS fit 4 of 156 burst-size fits and 14 of 106 merging-number fits exceed 3 when
unbounded (largest 3.358 and 3.795), and the capped fits differ from them in exactly those cases,
though none of them sits at the bound, because the cap moves xmin. Under the continuous KS fit
7 and 33 fits exceed 3. No unbounded fit is out of its range.''')
n.cells.insert(16,note)
nbformat.write(n,p)

p="other_neurons.ipynb"; n=nbformat.read(p,4)
n.cells[1].source=n.cells[1].source.replace('import bursttree as bt','import powerlaw\nimport bursttree as bt')
n.cells[1].source+='\nprint("powerlaw", powerlaw.__version__, "; adopted readings (unbounded exponent):", bt.ADOPTED_READINGS)'
n.cells[4].source=n.cells[4].source.replace('''inhibitory (a question to a reader on the claims file's "pyramidal"). The powerlaw 2.0.0 default,
with the exponent capped at 3, is a variant run on grid (a) alone, for run time.''','''inhibitory (a question to a reader on the claims file's "pyramidal"). The powerlaw 2.0.0 default,
with the exponent capped at 3, is a variant run on grid (a) alone in `other_neurons_cap3.ipynb`.''')
res=nbformat.v4.new_markdown_cell('''**Result: reproduced, under the continuous fit from xmin = 1 alone.** With the exponent unbounded,
502 of 554 (grid (a)) and 502 of 562 (grid (b)) pyramidal units of all sessions show the pattern
under the continuous fit from xmin = 1 (0.906 and 0.893), and 107 and 106 of 120 in
Achilles-10252013 (0.892 and 0.883), so the criterion's "under one reading" is met for both sets.
No other reading meets it: in set (b) the continuous KS fit gives 0.449 and 0.454, the discrete
KS fit 0.233 and 0.240, and the discrete fit from xmin = 1 0.211 and 0.215; in set (a) they give
0.342 and 0.292, 0.117 and 0.083, and 0.017. The pass is fragile: the continuous fit from
xmin = 1 treats integer sizes as continuous down to 1, where Clauset et al. (ref. 36, Section 3)
find the continuous approximation poor, and its exponents (median over units of the median beta
1.744 to 1.778) are far from the paper's 2.35. The inhibitory units, the class the files give the
paper's own representative unit, show the pattern far more often: 92 and 87 of 128 under the
discrete KS fit (0.719 and 0.680) and 95 of 128 under the continuous one (0.742); over all 690
units the continuous KS fit gives 0.504 and 0.507. Under the discrete KS fit the median over
pyramidal units of the median beta is 2.471 and 2.459 (interquartile range 2.216 to 2.789 on grid
(a)), and 2.284 to 2.600 by session. 32 pyramidal units have fewer than three points on grid (a)
and are not used there. Leaving out the two pyramidal units with unsorted spike times changes no
fraction by more than 0.003.''')
n.cells.insert(6,res)
n.cells[9].source='''**Result (parts).** With the exponent unbounded and the discrete KS fit, the burst-size part of the
pattern holds in 0.744 and 0.770 of the pyramidal units of set (b), and the merging-number part in
0.251 and 0.249: it is the merging numbers that fail. In set (a) the merging part holds in 0.117
and 0.083. In the inhibitory units of all sessions the parts hold in 0.906 and 0.977 (burst sizes)
and 0.781 and 0.695 (merging numbers).'''
nbformat.write(n,p)
for i,c in enumerate(n.cells): print(i,c.cell_type,c.source[:60].replace("\n"," "))

p="other_neurons_cap3.ipynb"; m=nbformat.read(p,4)
m.cells.append(nbformat.v4.new_markdown_cell('''**Result (variant).** With the exponent capped at 3, on grid (a), the fraction of pyramidal units
showing the pattern in set (b) is 0.547 under the continuous KS fit, 0.233 under the discrete KS
fit, 0.906 under the continuous fit from xmin = 1 and 0.211 under the discrete one; in set (a)
0.400, 0.117, 0.892 and 0.017. The cap lifts the continuous KS fit above one half in set (b)
(0.547, against 0.449 unbounded); that fit sits at the bound in 1034 of the 9576 fits of set (b),
and the discrete KS fit in 78. The outcome does not depend on the cap: the continuous fit from
xmin = 1 passes under both ranges.'''))
nbformat.write(m,p)
EOF
```

```
0 markdown # Hiraoka & Jo (2025) on DANDI:000044: the other neurons  Pa
1 code import os os.environ.setdefault("OMP_NUM_THREADS", "1"); os.
2 markdown ## Data check  The units tables of all eight sessions: count
3 code assets = bt.list_assets() trains, rows = [], [] for a in ass
4 markdown ## fig2-other-neurons-similar  > Other neurons of the record
5 code t1 = time.time() with ProcessPoolExecutor(max_workers=4) as 
6 markdown **Result: reproduced, under the continuous fit from xmin = 1
7 markdown ### Burst sizes and merging numbers taken apart  The pattern
8 code used = R[R.used] def parts(d):     return d.assign(burst_ok=
9 markdown **Result (parts).** With the exponent unbounded and the disc
```

**Agent**

Now the model notebook's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p="model.ipynb"; n=nbformat.read(p,4)
C=n.cells
C[1].source=C[1].source.replace('import bursttree as bt','import powerlaw\nimport bursttree as bt')+'\nprint("powerlaw", powerlaw.__version__)'
C[5].source='''**Result: partially reproduced under the claim's seed, and seed sensitive.** With the exponent
unbounded, no single reading of the fit holds for all three series under the claim's seed, on
either grid. Under the discrete KS fit the linear and quadratic series hold on grid (a), and the
exponential series has heavy tails (supported at 8 of 11 timescales and 17 of 20 pairs on grid
(a), 42 of 52 and 79 of 94 on grid (b)) but its gamma has an interquartile range of 0.544 and
0.508, above 0.5; on grid (b) the linear series also fails (gamma interquartile range 0.511). The
fits from xmin = 1 hold for the exponential series but not the quadratic one (beta interquartile
range 0.508 to 0.953). Capped at 3 (grid (a)), the discrete KS fit gives 0.522 for the
exponential gamma and still fails. Under the four further seeds the discrete KS fit holds for all
three series under seeds + 1000, + 2000 and + 3000, and not under + 4000, where the linear series
fails; the exponential gamma interquartile range runs from 0.203 to 0.544 over the five seeds.
Taking for each series whichever reading holds, every series holds under every seed on grid (a);
the claim is judged under one reading for all three series.'''
C[13].source=C[13].source  # code
C[12].source=C[12].source.replace("with its run time","")
res=nbformat.v4.new_markdown_cell('''**Result (calibrated variant).** With the five runs of each algorithm as the units, the literal
set-up (L) differs in all three series (statistic 0.169 to 0.236, p = 0.0079, the smallest
possible, 0.024 after Bonferroni), while two runs of one algorithm (N) differ in none (p 0.373 to
0.913), so this test keeps its level where the criterion's does not. With both algorithms on the
zeta distribution (Z) no series differs (p 0.429 to 0.857). With both on Eq. 16 (Q) the linear
series differs (p = 0.0079; mean D 0.0078 between the algorithms against 0.0077 and 0.0053 within
each) and the other two do not. The variant agrees with the criterion on L, and it finds the two
algorithms equivalent under Z, as the paper says they are when both use one distribution; it does
not decide the outcome, which the criterion gives.''')
n.cells.append(res)
nbformat.write(n,p)
for i,c in enumerate(n.cells): print(i,c.cell_type,c.metadata.get("tags"),c.source[:60].replace("\n"," "))
EOF
```

```
0 markdown None # Hiraoka & Jo (2025): the dynamic generative algorithms (Se
1 code None import time, resource, zlib import numpy as np import pandas
2 code ['sanity'] print("dandiset", bt.DANDISET, "version", bt.DANDI_VERSION, 
3 markdown None ## fig4-model-heavy-tails  > Event sequences generated by th
4 code ['claim:fig4-model-heavy-tails'] def judge_series(res):     B = pd.DataFrame(res["bursts"]); 
5 markdown None **Result: partially reproduced under the claim's seed, and s
6 code None fig, axs = plt.subplots(1, 3, figsize=(11, 3)) for ax, s in 
7 markdown None ## fig4-model-iet-shapes  > The IET distribution of the mode
8 code ['claim:fig4-model-iet-shapes'] S2 = seed_of("fig4-model-iet-shapes") EXP = {"linear": 1960,
9 markdown None **Result: partially reproduced, and seed sensitive.** Under 
10 markdown None ## model-decremental-equivalent  > The decremental algorithm
11 code ['claim:model-decremental-equivalent'] S3 = seed_of("model-decremental-equivalent") VARIANTS = {"L"
12 markdown None ### Variant: a test calibrated across independent runs  The 
13 code ['claim:model-decremental-equivalent'] from itertools import combinations splits = [set(c_) for c_ 
14 markdown None **Result: not reproduced.** Under the literal set-up (L) and
15 markdown None **Result (calibrated variant).** With the five runs of each
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p="model.ipynb"; n=nbformat.read(p,4)
r=n.cells.pop(14); n.cells.insert(12,r); nbformat.write(n,p)
print(n.cells[0].source[-400:])
EOF
python - <<'EOF'
import nbformat
n=nbformat.read("reproduce_hiraoka_2025.ipynb",4)
print(n.cells[38].source)
EOF
```

```
10^6 events, gamma = 2.5, delta_0 = 1, uniform IETs
(Eq. 10), linear (Eq. 12) and quadratic (Eq. 13) timescales with w = 100, exponential (Eq. 14)
with w = 2, merging numbers zeta-distributed (Eq. 15) with the memory function of Eq. 16 for the
incremental algorithm (Algorithm 2), which Figure 4 uses.

Claims tested here: fig4-model-heavy-tails, fig4-model-iet-shapes, model-decremental-equivalent.
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome | Rests on |
|---|---|---|
| fig2-neuron-representative-sequence | reproduced | O1 reading (b), row 9 counted from 0 (unit id 18) |
| fig2-iet-broad | reproduced | |
| fig2-neuron-burst-size-heavy-tail | reproduced | KS fits (assumption: the discrete KS fit); xmin = 1 gives partial |
| fig2-neuron-beta-stable | partially reproduced | median 2.354, but beta near 2.9 at 55 ms |
| fig2-neuron-beta-decrease-follows-gamma | reproduced | grid (b), KS fits |
| fig2-neuron-merging-heavy-tail | reproduced | KS fits |
| fig2-neuron-merging-collapse | reproduced | reading (b), discrete KS fit, max deviation 0.490 against 0.5 |
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p="reproduce_hiraoka_2025.ipynb"; n=nbformat.read(p,4)
h=n.cells[0]
h.source=h.source.replace("Notebooks of this entry: this one (data check and the representative neuron),\n`other_neurons.ipynb` (fig2-other-neurons-similar) and `model.ipynb` (Section IV, Figure 4).",
"Notebooks of this entry: this one (data check and the representative neuron),\n`other_neurons.ipynb` (fig2-other-neurons-similar), `other_neurons_cap3.ipynb` (its variant with the\nexponent capped at 3) and `model.ipynb` (Section IV, Figure 4).")
h.source=h.source.replace("| fig2-other-neurons-similar | other_neurons.ipynb | tested |","| fig2-other-neurons-similar | other_neurons.ipynb, other_neurons_cap3.ipynb | tested |")
h.source=h.source.replace("blocked (`other`): the SCSN catalog is public but continuously revised and has no pinned version |","blocked (`other`): the SCSN catalog is public but continuously revised and has no versioned release to pin (author, step 1.4) |")
s=n.cells[38]
old=s.source.split("How the analysis differs from the paper's:")[0]
table='''## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome | Rests on |
|---|---|---|
| fig2-neuron-representative-sequence | reproduced | O1 reading (b), row 9 counted from 0 (unit id 18) |
| fig2-iet-broad | reproduced | |
| fig2-neuron-burst-size-heavy-tail | reproduced | KS fits, exponent unbounded or capped; xmin = 1 gives partial on grid (b) |
| fig2-neuron-beta-stable | not reproduced | median 2.354, but beta 3.349 at 55 ms; no reading holds |
| fig2-neuron-beta-decrease-follows-gamma | reproduced | grid (b), KS fits |
| fig2-neuron-merging-heavy-tail | reproduced | discrete KS fit (interquartile range 0.378 and 0.415) |
| fig2-neuron-merging-collapse | not reproduced | assumption: exponent unbounded (max deviation 0.538); capped at 3 it passes at 0.490 |
| fig2-exponents-above-two | reproduced | KS fits |
| fig2-other-neurons-similar | reproduced | continuous fit from xmin = 1 alone (0.883 to 0.906); KS fits 0.083 to 0.454 (`other_neurons.ipynb`) |
| fig2-wikipedia-beta | blocked (too_large) | |
| fig2-earthquake-beta | blocked (other) | |
| fig4-model-heavy-tails | partially reproduced | one reading for all three series; seed sensitive (`model.ipynb`) |
| fig4-model-iet-shapes | partially reproduced | seed sensitive (`model.ipynb`) |
| model-decremental-equivalent | not reproduced | literal set-up of Section IV (`model.ipynb`) |

'''
rest=s.source.split("How the analysis differs from the paper's:")[1]
oldfit=rest.split("- The grid of delta")[0]
newfit='''

- The fit is the `powerlaw` package, as the paper cites, under the four readings of O3; a claim
  holds when it holds under one of them, as O3 says. The package's release 2.0.0, locked here,
  caps the exponent at 3 by default and lets the cap move xmin; the method the paper cites
  (Clauset et al., ref. 36) has no such cap, and the paper gives no version. The fits here leave
  the exponent unbounded (an assumption), and the capped fits are shown beside them. The cap
  decides one outcome, fig2-neuron-merging-collapse.
'''
s.source=table+"How the analysis differs from the paper's:"+newfit+"- The grid of delta"+rest.split("- The grid of delta")[1]
s.source=s.source.replace('''- The paper's "unit 9" is row 9 of the units table counted from 0 (id 18). It is labelled
  inhibitory, though the paper describes the data as pyramidal cells.''','''- The paper's "unit 9" is row 9 of the units table counted from 0 (id 18). It is labelled
  inhibitory, though the paper describes the data as pyramidal cells; the inhibitory units show
  the paper's pattern far more often than the pyramidal ones (`other_neurons.ipynb`).''')
nbformat.write(n,p)
print(s.source[:4000])
EOF
```

```
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome | Rests on |
|---|---|---|
| fig2-neuron-representative-sequence | reproduced | O1 reading (b), row 9 counted from 0 (unit id 18) |
| fig2-iet-broad | reproduced | |
| fig2-neuron-burst-size-heavy-tail | reproduced | KS fits, exponent unbounded or capped; xmin = 1 gives partial on grid (b) |
| fig2-neuron-beta-stable | not reproduced | median 2.354, but beta 3.349 at 55 ms; no reading holds |
| fig2-neuron-beta-decrease-follows-gamma | reproduced | grid (b), KS fits |
| fig2-neuron-merging-heavy-tail | reproduced | discrete KS fit (interquartile range 0.378 and 0.415) |
| fig2-neuron-merging-collapse | not reproduced | assumption: exponent unbounded (max deviation 0.538); capped at 3 it passes at 0.490 |
| fig2-exponents-above-two | reproduced | KS fits |
| fig2-other-neurons-similar | reproduced | continuous fit from xmin = 1 alone (0.883 to 0.906); KS fits 0.083 to 0.454 (`other_neurons.ipynb`) |
| fig2-wikipedia-beta | blocked (too_large) | |
| fig2-earthquake-beta | blocked (other) | |
| fig4-model-heavy-tails | partially reproduced | one reading for all three series; seed sensitive (`model.ipynb`) |
| fig4-model-iet-shapes | partially reproduced | seed sensitive (`model.ipynb`) |
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p="reproduce_hiraoka_2025.ipynb"; n=nbformat.read(p,4)
s=n.cells[38]
s.source=s.source.replace("the inhibitory units show\n  the paper's pattern far more often than the pyramidal ones","under the KS fits the\n  inhibitory units show the paper's pattern far more often than the pyramidal ones")
s.source=s.source.replace("xmin = 1 gives partial on grid (b) |","xmin = 1 gives partial except the continuous fit on grid (a) |")
nbformat.write(n,p)
EOF
cat README.md; date -u
```

```
# Hiraoka and Jo (2025) on DANDI:000044

Tests the findings of T. Hiraoka and H.-H. Jo, "Hierarchical organization of bursty trains in
event sequences" (doi:10.1063/5.0296506), on dandiset 000044 version 0.210812.1516, the version the
paper cites: the hippocampal recordings of Grosmark and Buzsaki (2016). The claims are in
`claims/hiraoka-2025.yaml` and the record in `attempts/hiraoka-2025-01.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

- `reproduce_hiraoka_2025.ipynb`: the data check, the paper's representative unit (row 9 of
  session Achilles-10252013), and its bursty trains, merging numbers and power-law fits (Figure 2).
- `other_neurons.ipynb`: the same pattern in every pyramidal unit of the eight sessions (about
  30 minutes on 4 processes).
- `model.ipynb`: the paper's two generative algorithms (Section IV, Figure 4), simulated here.
- `bursttree.py`: loading, bursts, merging numbers, fits and the algorithms, with the source of
  each parameter.

The Wikipedia and earthquake sequences of the paper are not tested.

[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p="README.md"; s=open(p).read()
s=s.replace('''- `other_neurons.ipynb`: the same pattern in every pyramidal unit of the eight sessions (about
  30 minutes on 4 processes).''','''- `other_neurons.ipynb`: the same pattern in every unit of the eight sessions, pyramidal and
  inhibitory (about 45 minutes on 4 processes).
- `other_neurons_cap3.ipynb`: the same test with the power-law exponent capped at 3, the default
  of the locked powerlaw 2.0.0, as a variant (about 11 minutes on 4 processes).''')
open(p,"w").write(s)
p="entry.yaml"; s=open(p).read()
s=s.replace('''- path: other_neurons.ipynb
  title: Hiraoka and Jo (2025) on dandiset 000044, the other pyramidal units
  runtime_minutes: 40''','''- path: other_neurons.ipynb
  title: Hiraoka and Jo (2025) on dandiset 000044, the other units
  runtime_minutes: 45
- path: other_neurons_cap3.ipynb
  title: Hiraoka and Jo (2025) on dandiset 000044, the other units with the exponent capped at 3
  runtime_minutes: 11''')
s=s.replace("runtime_minutes: 20","runtime_minutes: 30").replace("runtime_minutes: 3\n","runtime_minutes: 6\n")
s=s.replace("checks whether other pyramidal units show the same pattern","checks whether the other units, pyramidal and inhibitory, show the same pattern")
open(p,"w").write(s)
EOF
cat entry.yaml | head -30; cd  && python tools/entry.py check entries/hiraoka-2025 2>&1 | tail -20
```

```
schema_version: 1
name: hiraoka-2025
type: reproduction
title: Hierarchical organization of bursty trains in hippocampal spike trains (Hiraoka and Jo 2025)
description: Tests the neuronal findings of Hiraoka and Jo (2025) on dandiset 000044, the hippocampal
  recordings of Grosmark and Buzsaki (2016) that the paper analyses. It finds the paper's
  representative unit, measures bursty trains and merging numbers across timescales, fits their
  power-law tails, and checks whether the other units, pyramidal and inhibitory, show the same pattern. It also runs the
  paper's two generative algorithms. The Wikipedia and earthquake sequences of the paper are not
  tested.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_hiraoka_2025.ipynb
  title: Hiraoka and Jo (2025) on dandiset 000044, the representative neuron
  runtime_minutes: 6
- path: other_neurons.ipynb
  title: Hiraoka and Jo (2025) on dandiset 000044, the other units
  runtime_minutes: 45
- path: other_neurons_cap3.ipynb
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025 && python - <<'EOF'
import nbformat
for p in ["reproduce_hiraoka_2025.ipynb","other_neurons.ipynb","other_neurons_cap3.ipynb","model.ipynb"]:
    n=nbformat.read(p,4)
    for i,c in enumerate(n.cells):
        if c.cell_type=="code": compile(c.source,f"{p}[{i}]","exec")
    print(p,"ok", sum(c.cell_type=="code" and bool(c.get("outputs")) for c in n.cells))
EOF
date -u
```

```
reproduce_hiraoka_2025.ipynb ok 0
other_neurons.ipynb ok 0
other_neurons_cap3.ipynb ok 0
model.ipynb ok 0
Sun Nov 22 01:53:46 UTC 2026
```

**Agent**

Entry checks pass, and every code cell compiles. Starting the final clean run, `tools/entry.py all`, at 01:54 UTC; estimate about 90 minutes run one notebook after another.

**Agent calls Bash**

```bash
cd  && python tools/entry.py all entries/hiraoka-2025 2>&1 | tail -25; date -u
```

```
Installed kernelspec registry-hiraoka-2025 in executed/hiraoka-2025/.venv/share/jupyter/kernels/registry-hiraoka-2025
0 error(s)
pass  reproduce_hiraoka_2025.ipynb  (182 s)
pass  other_neurons.ipynb  (3009 s)
pass  other_neurons_cap3.ipynb  (639 s)
pass  model.ipynb  (1031 s)
Sun Nov 22 03:15:02 UTC 2026
```

**Agent**

All four notebooks passed: 3, 50, 11 and 17 minutes. Now checking that the executed outputs match the development numbers the conclusions were written from.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd  for nb in reproduce_hiraoka_2025 other_neurons model; do python $TMPDIR/show.py executed/hiraoka-2025/$nb.ipynb | grep -v "min\b\|done in\| s$\|seconds\|fitted\|time" > $TMPDIR/a.txt; python $TMPDIR/show.py $TMPDIR/devout/$nb.ipynb | grep -v "min\b\|done in\| s$\|seconds\|fitted\|time" > $TMPDIR/b.txt; echo "== $nb"; diff $TMPDIR/a.txt $TMPDIR/b.txt | head -20; done; python $TMPDIR/show.py executed/hiraoka-2025/other_neurons_cap3.ipynb | head -60
```

```
== reproduce_hiraoka_2025
22a23
> 
106a108
> 
131c133
< === [18]
---
> === [17]
256c258
< === [21]
---
> === [20]
287c289
< === [24]
---
> === [23]
343c345
< === [27]
---
[... 92 more lines not kept]
```

**Agent**

The executed outputs match the development run exactly, apart from cell numbering. Now the record and the questions file.

**Agent calls Bash**

```bash
cd  sed -n 60,96p attempts/hiraoka-2025-01.yaml; grep -n "verifications\|^[a-z_]*:" attempts/hiraoka-2025-01.yaml; ls attempts | head -3; grep -l "verifications:" attempts/*.yaml | head -3; cat questions/README.md | head -60
```

```
shuffled in time, a renewal reference, no timescale is supported under any of the five seeds
    (0 of 5 or 6, grid (a)).
  deviations:
  - The fit reading is open (claims file, O3) and the readings differ in outcome here, with no
    rule in the claims file for a claim that counts tests. Assumed the discrete maximum-likelihood
    fit with xmin chosen by the KS distance, because burst sizes and merging numbers are integers,
    the method the paper cites for its fits (Clauset et al., ref. 36, through the powerlaw package,
    ref. 37) gives the discrete estimator for integer data, and this reading gives the paper's beta
    for the representative unit (median 2.354 against 2.35). The paper does not say which it used.
  - The grid of delta is open (O4). Grid (b) fits a whole number of log10 steps near 0.052 between
    the ends of the relevant range (40 steps of 0.0514 for this unit), as the Figure 2 legend says
    the values shown span the entire range of relevant timescales; every 5th point then gives the
    delta' labels of Figure 2 and every 8th the delta labels.
- claim: fig2-neuron-beta-stable
  outcome: partially_reproduced
  notebook: reproduce_hiraoka_2025.ipynb
  output: claim:fig2-neuron-beta-stable
  measured: 2.354
  notes: Under the discrete KS fit on grid (b) the median beta below 3000 ms is 2.354 and 27 of 34
    estimates are within 2.35 +/- 0.235, every one from 126.5 ms to 3000 ms (1.4 decades). At the
[... 44 more lines not kept]
```

**Agent**

Let me look at the schema for `verifications` and an example.

**Agent calls Bash**

```bash
cd  ls schemas; python - <<'EOF'
import json,glob
for f in glob.glob("schemas/*attempt*"):
    s=json.load(open(f)); 
    def find(o,path=""):
        if isinstance(o,dict):
            for k,v in o.items():
                if k in("verifications","proposed"): print(path+"/"+k, json.dumps(v)[:3000])
                find(v,path+"/"+k)
    find(s)
EOF
f=$(grep -l "verifications:" attempts/*.yaml | tail -1); echo $f; awk '/^verifications:/,0' $f | head -60; cat questions/asari-2009.yaml | head -30
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
/properties/outcomes/items/properties/proposed {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "reason": {"type": "string", "minLength": 1}}}
/properties/verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}, "findings": {"description": "From protocol pilot-18, in round 2: what the verifier said of each finding the record rates `critical` (docs/protocol.md, the attempt record).", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["finding", "agrees"], "properties": {"finding": {"descript
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -c 1500 transcripts/hiraoka-2025/verifier-1.md; git log --format="%ad %s" --date=iso | head -3; sed -n 140,230p attempts/hiraoka-2025-01.yaml | grep -n "claim:"
```

````
# hiraoka-2025 · verifier-1 · run 44961875683

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat *.md 2>/dev/null | head -300
```

```
total 408
drwxr-xr-x 6 runner runner    4096 Nov 22 00:24 .
drwxr-xr-x 8 runner runner    4096 Nov 22 00:24 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 23:24 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 23:24 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 22 00:24 .claude
-rw-r--r-- 1 runner runner       0 Nov 22 00:24 .env
-rw-r--r-- 1 runner runner       0 Nov 22 00:24 .env.development
-rw-r--r-- 1 runner runner       0 Nov 22 00:24 .env.development.local
[... 17 more lines not kept]
````

**Agent**

Writing the record update.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
p="attempts/hiraoka-2025-01.yaml"
R=yaml.safe_load(open(p))
O={o["claim"]:o for o in R["outcomes"]}
CAPDEV=("The exponent of every fit is unbounded (alpha in [1, inf)), an assumption: the locked powerlaw 2.0.0 caps the "
 "power-law alpha at 3 by default (Power_Law.DEFAULT_PARAMETER_RANGES) and its find_xmin discards every candidate xmin "
 "whose fit reaches the cap, while the estimator the paper cites (Clauset et al., ref. 36, Section 3) has no upper bound and "
 "neither had the package as its paper describes it (Alstott et al., ref. 37; releases 1.x require only alpha > 1). The paper "
 "gives no version. The capped fits are run beside the unbounded ones (readings with suffix _cap3).")

o=O["fig2-neuron-burst-size-heavy-tail"]
o.pop("assumed",None)
o["notes"]=("With xmin chosen by the KS distance, discrete or continuous, the power law is supported (R > 0, p < 0.05) at 8 of 8 "
 "timescales of grid (a) and 40 of 40 of grid (b), all of those below 3000 ms included, with the exponent unbounded or capped at 3. "
 "The claim holds under one reading of O3, as the claims file's rule asks. With xmin = 1 the discrete fit is supported at 5 of 8 and "
 "29 of 40, not all below 3000 ms; the continuous fit at 7 of 8 with all 7 below 3000 ms (grid a) and 32 of 40 with 32 of 34 below "
 "3000 ms (grid b). On the IETs shuffled in time, a renewal reference, no timescale is supported under any of the five seeds "
 "(0 of 5 or 6, grid (a)).")
o["deviations"]=[CAPDEV, o["deviations"][1]]

o=O["fig2-neuron-beta-stable"]
o["outcome"]="not_reproduced"
o["notes"]=("Neither reading of the criterion holds under any fit or grid. Under the discrete KS fit on grid (b) the median beta "
 "below 3000 ms is 2.354, inside the band, and 27 of 34 estimates are within 2.35 +/- 0.235, every one from 126.5 ms to 3000 ms "
 "(1.4 decades); at 55 ms beta is 3.349, so the range is 1.079 against the 0.47 of reading (b). With the exponent unbounded the "
 "ranges are 0.679 to 1.360 over the fits and grids (medians 2.316 to 2.433 under the KS fits, 1.521 to 1.750 with xmin = 1); "
 "capped at 3 the KS ranges are 0.552 to 0.705 and also fail. The standard errors are at most 0.088. The paper's value holds "
 "from about 130 to 3000 ms but not at the lower end of the relevant range.")
o["deviations"]=["Measured is the median under the discrete KS fit on grid (b); the other readings are in the notebook.", CAPDEV]

o=O["fig2-neuron-beta-decrease-follows-gamma"]
o["notes"]=("On grid (b), under both KS fits with the exponent unbounded, beta at delta' is below gamma for 40 of 57 pairs with "
 "delta < 3000 ms (38 for the capped continuous fit); above 3000 ms the 6 grid points give a Spearman rho of -0.829 (p = 0.042) "
 "for beta, which falls from 2.064 to 1.867 (discrete), and gamma falls with delta for each ratio (rho -0.714, -0.964 and "
 "-0.943). Part (2) rests on 6 points at p = 0.042. Grid (a) has one point above 3000 ms, so parts (2) and (3) are not judged on "
 "it; its part (1) holds (7 of 12). Under xmin = 1 part (1) fails (24 of 57), so the outcome rests on the KS fits, as O3 allows "
 "for a claim on exponents. The paper names no test; the claim's \"seems to be driven\" is not tested beyond these correlations.")

o=O["fig2-neuron-merging-heavy-tail"]
o["notes"]=("With the exponent unbounded, the discrete KS fit supports the power law for 13 of 15 pairs on grid (a) and 70 of 76 "
 "on grid (b), and the gamma of the supported pairs has an interquartile range of 0.378 and 0.415 (median 2.618 and 2.644), so "
 "both conditions hold under that reading of O3. The continuous KS fit supports 15 of 15 and 69 of 76, but its interquartile "
 "range is 0.642 and 0.546; capped at 3 it was 0.408 and 0.426, so the cap decides that reading and not the discrete one "
 "(0.383 and 0.401 capped). With xmin = 1 the discrete fit is supported for 6 of 15 and 19 of 76 pairs, and the continuous fit "
 "has an interquartile range of 0.673 and 0.597.")
o["deviations"]=[CAPDEV]

o=O["fig2-neuron-merging-collapse"]
o["outcome"]="not_reproduced"; o["assumed"]=True
o["notes"]=("Reading (b) fails with the exponent unbounded: the gamma of the 15 pairs of Figure 2 lie up to 0.538 from their "
 "median under the discrete KS fit (median 2.610), 1.742 under the continuous KS fit, 0.521 under the discrete fit from xmin = 1 "
 "and 1.249 under the continuous one, all outside the band of 0.5. The deviation of 0.538 is the pair delta' 180 ms, delta 594 ms "
 "(gamma 3.148), which the cap at 3 holds at 2.843; the capped discrete KS fit, at 0.490, is the only fit within the band, so "
 "the outcome rests on the unbounded exponent. Reading (a) fails, as the complementary cumulative distributions of k over its "
 "mean differ by up to a factor of 12.54 (median 1.63) where all exceed 10^-3. One pair of Figure 2 (delta' 590 ms, delta "
 "6490 ms) lies above the relevant range, with 89 bursts.")
o["deviations"]=[o["deviations"][0], CAPDEV]

o=O["fig2-exponents-above-two"]
o["notes"]=("Under the KS fits with the exponent unbounded both gamma and beta at delta' exceed 2 in 15 of 15 pairs (grid a) and "
 "76 of 76 (grid b), and beta at delta is within 10% of the smaller of the two in 9 (continuous) and 12 (discrete) of 15 and in "
 "45 and 58 of 76 pairs (median relative error 0.058 to 0.089); capped at 3, in 11 and 12 of 15 and 48 and 58 of 76. Under "
 "xmin = 1 both conditions fail (both above 2 in 0 to 17 pairs).")

o=O["fig2-other-neurons-similar"]
o["outcome"]="reproduced"; o.pop("assumed",None)
o["notebook"]="other_neurons.ipynb"
o["notes"]=("Reproduced under the continuous fit from xmin = 1 alone, which meets the criterion's \"under one reading\": with the "
 "exponent unbounded, 502 of 554 (grid a) and 502 of 562 (grid b) pyramidal units of all sessions show the pattern (0.906 and "
 "0.893), and 107 and 106 of 120 in Achilles-10252013 (0.892 and 0.883). No other reading meets it: in set (b) the continuous KS "
 "fit gives 0.449 and 0.454, the discrete KS fit 0.233 and 0.240, the discrete fit from xmin = 1 0.211 and 0.215; in set (a) "
 "0.342 and 0.292, 0.117 and 0.083, and 0.017. The pass is fragile: the continuous fit from xmin = 1 treats integer sizes as "
 "continuous down to 1, where Clauset et al. (ref. 36) find the continuous approximation poor, and its exponents (median over "
 "units of the median beta 1.744 to 1.778) are far from the paper's 2.35. Capped at 3 (other_neurons_cap3.ipynb, grid a) the "
 "continuous KS fit passes in set (b) (0.547) and the continuous fit from xmin = 1 gives 0.906, so the outcome does not depend on "
 "the cap. The inhibitory units, the class the files give the paper's representative unit, show the pattern far more often under "
 "the KS fits: 92 and 87 of 128 (0.719 and 0.680, discrete) and 95 of 128 (0.742, continuous); over all 690 units the "
 "continuous KS fit gives 0.504 and 0.507. Under the discrete KS fit the median over pyramidal units of each unit's median beta "
 "is 2.471 and 2.459 (interquartile range 2.216 to 2.789, grid a), and 2.284 to 2.600 by session; the burst-size part holds in "
 "0.744 and 0.770 of the units and the merging-number part in 0.251 and 0.249. 32 pyramidal units have fewer than three points "
 "on grid (a) and are not used there. Whether the set should hold the inhibitory units is asked of a reader (questions).")
o["deviations"]=[
 "Pyramidal units are read as those with cell_type excitatory, the only label for principal cells in this version (562 of 690 "
 "units). The paper's own representative unit is labelled inhibitory, so the inhibitory units (128) and all units (690) are run "
 "as variants.",
 "Two of the 562 pyramidal units have unsorted spike times (data finding); the trains are sorted before the IETs are taken, and "
 "leaving them out changes no fraction by more than 0.003.",
 CAPDEV + " The capped variant is run on grid (a) alone, for run time."]

o=O["fig2-wikipedia-beta"]
o["notes"]+=(" The verifier would give data_missing, as the preprocessed edit histories were never deposited; the code stays "
 "too_large, as the claims file has this claim as data elsewhere, for which the protocol does not use data_missing, and the public "
 "dump it would be rebuilt from is what does not fit the run.")
o=O["fig2-earthquake-beta"]
o["notes"]=("The Southern California Seismic Network catalog is public (the SCEDC event service answered a query for 1993) but it "
 "is revised continuously and has no versioned release, and the paper gives no retrieval date or event identifiers, so it cannot "
 "be pinned as the protocol requires for outside data (author, step 1.4). Not tested. The verifier finds this reason weak, since "
 "the 10% tolerance on n would allow an approximate test on the current catalog; such a test would rest on unpinned data and was "
 "not run.")

o=O["fig4-model-heavy-tails"]
o["notes"]=("Sequences generated here by Algorithm 2 with the set-up of Section IV. With the exponent unbounded, no single reading "
 "of the fit holds for all three series under the claim's seed, on either grid. Under the discrete KS fit the linear and "
 "quadratic series hold on grid (a); the exponential series has heavy tails (supported at 8 of 11 timescales and 17 of 20 pairs "
 "on grid a, 42 of 52 and 79 of 94 on grid b) but its gamma has an interquartile range of 0.544 and 0.508, above the 0.5 of the "
 "criterion, and on grid (b) the linear series also fails (0.511). The fits from xmin = 1 hold for the exponential series but not "
 "the quadratic one (beta interquartile range 0.508 to 0.953). Capped at 3 (grid a), the discrete KS fit gives 0.522 for the "
 "exponential gamma. Under the four further seeds the discrete KS fit holds for all three series under seeds + 1000, + 2000 and "
 "+ 3000 and not under + 4000 (the linear series fails); the exponential gamma interquartile range runs from 0.203 to 0.544 over "
 "the five seeds. Each series holds under some reading under every seed on grid (a).")
o["deviations"]=[o["deviations"][0], "Under the four further seeds only grid (a) was run, with the exponent unbounded, for run time.",
 o["deviations"][2], CAPDEV + " The capped fits are run under the claim's seed on grid (a)."]

o=O["model-decremental-equivalent"]
o["notes"]+=(" As a variant the verifier asked for, a test calibrated across runs takes the five runs of each algorithm as the "
 "units (mean KS distance between algorithms less within, averaged over grid (a), exact permutation over the 126 splits): L "
 "differs in all three series (p = 0.0079, the smallest possible, 0.024 after Bonferroni), two runs of one algorithm (N) differ in "
 "none (p 0.373 to 0.913), Z in none (p 0.429 to 0.857), and Q in the linear series only (p = 0.0079). It agrees with the "
 "criterion on L and finds the algorithms equivalent under Z; it does not decide the outcome.")

# findings
F=R["findings"]
for f in F:
    if f.get("kind")=="methods_unavailable" and "discrete or continuous" in f["statement"]:
        f["statement"]=("Question for the authors. Which power-law fit was used for burst sizes and merging numbers, discrete or "
         "continuous, and with xmin chosen by the KS distance or fixed? The paper cites Clauset et al. and the powerlaw package "
         "without its options or version. On this dataset the discrete fit with xmin by the KS distance gives the paper's beta of "
         "2.35 for unit 9, and the choice decides whether other neurons show the pattern (23% of pyramidal units under it, 45% under "
         "the package's continuous default with xmin by the KS distance, 89% to 91% with the continuous fit from xmin = 1).")
    if f.get("about")=="paper" and f.get("kind")=="other" and "pyramidal" in f["statement"]:
        f["statement"]+=(" Under the KS fits the inhibitory units show the paper's pattern far more often than the pyramidal ones "
         "(0.68 to 0.74 of 128 against 0.08 to 0.45 of 562).")
F.append(dict(kind="methods_unavailable", statement=(
 "Question for the authors. Which release of powerlaw was used, and was the exponent bounded? Release 2.0.0 caps the power-law "
 "exponent at 3 by default and lets the cap move the KS choice of xmin; the method of Clauset et al. that the paper cites has no "
 "cap. On the representative unit the cap decides the collapse of the merging-number exponents (largest deviation from the "
 "median 0.490 capped, 0.538 unbounded, against a band of 0.5) and narrows the spread of beta at the smallest timescales "
 "(2.907 capped, 3.349 unbounded at 55 ms). This attempt assumed an unbounded exponent.")))

V=dict(date="2026-11-22", kind="agent",
 by="Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)",
 reviewed=("Round 1: the handover of the first run (the executed notebooks with the conclusions and summary removed, the helper "
  "module and the claims file), with the paper under paper/. The verifier also queried the DANDI API for the dandiset's assets "
  "and ran powerlaw 2.0.0 on synthetic zeta samples."),
 results=[])
def add(c,ag,out,reason,resp): V["results"].append(dict(claim=c,agrees=ag,outcome=out,reason=reason,response=resp))
add("fig2-neuron-representative-sequence",True,"reproduced",
 "Under O1 reading (b), row 9 counted from 0 (units id 18), the unit has n = 228 356, tau_min = 1.050 ms and tau_max = 18 229.7 ms. "
 "It is the only unit in the session that matches. The three epoch counts add up to 228 356 exactly, which confirms O2.",
 "No change.")
add("fig2-iet-broad",True,"reproduced","tau_max/tau_min = 17 362, which is 4.24 decades, against >= 10^3 required.","No change.")
add("fig2-neuron-burst-size-heavy-tail",True,"reproduced",
 "Under both KS readings and both grids, the power law is supported at every delta, 8/8 (grid a) and 40/40 (grid b), including "
 "every delta below 3000 ms. The xmin = 1 readings fail below 3000 ms. The renewal (shuffled) reference supports a power law at 0 "
 "timescales in all 5 seeds.",
 "No change of outcome. All fits are rerun with the exponent unbounded (problem 1), with the capped fits beside them; the counts "
 "are the same under both. The outcome now rests on the claims file's one-reading rule (O3), not on adopting the discrete fit, so "
 "it is no longer marked as assumed.")
add("fig2-neuron-beta-stable",False,"not_reproduced",
 "Neither reading holds under any fit reading or grid. For example, ks_discrete on grid b has median 2.354, which is in the band, "
 "but its range is 0.705 against < 0.47 allowed. Beta is 2.6 to 2.9 for delta below about 130 to 180 ms, and only from 126 to 183 ms "
 "to 3000 ms (about 1.2 decades) do all estimates sit within 2.35 +/- 0.235. Removing the cap in problem 1 would only widen the range.",
 "Outcome changed to not_reproduced: the criterion gives no partial outcome and neither reading holds. With the exponent unbounded "
 "the range is 1.079 (beta 3.349 at 55 ms), as the verifier expected.")
add("fig2-neuron-beta-decrease-follows-gamma",True,"reproduced",
 "Grid (a) has only 1 point above 3000 ms, so it is not judged. On grid (b) under both KS readings, (1) 38/57 and 40/57 pairs have "
 "beta(delta') < gamma, (2) rho_beta = -0.83 (p = 0.042, 6 points), (3) rho_gamma < 0 for all three ratios.",
 "No change of outcome. With the exponent unbounded part (1) is 40 of 57 under both KS fits; parts (2) and (3) are unchanged. The "
 "notes and the conclusion now say part (2) rests on 6 points at p = 0.042 (problem 10).")
add("fig2-neuron-merging-heavy-tail",False,"partially_reproduced",
 "Support is robust, 15/15 (ks_continuous, grid a) and 72/76 (grid b). The IQR condition (0.38 to 0.43 against < 0.5) depends on an "
 "estimator that is bounded at alpha < 3 (problem 1). Six of the 15 grid-(a) gamma values sit at 2.93 to 2.99, which is that bound. "
 "Without the cap the IQR would very likely exceed 0.5, so only the first condition is secure.",
 "Outcome kept as reproduced, with the disagreement recorded. The fits were rerun without the cap: the continuous KS fit's "
 "interquartile range does exceed 0.5 (0.642 and 0.546), as the verifier expected, but the discrete KS fit keeps it below 0.5 "
 "(0.378 and 0.415, with 13 of 15 and 70 of 76 pairs supported), and one reading suffices under O3.")
add("fig2-neuron-merging-collapse",True,"reproduced",
 "Reproduced (marginal). Reading (a) fails clearly, the CCDFs differ by up to 12.5x at k/<k> of about 10. Reading (b) holds only for "
 "ks_discrete, with max deviation 0.490 against +/- 0.5. The most deviant pair, (590, 6490 ms), lies outside the relevant range "
 "(delta > 6283 ms, m = 89 bursts), although the claims file lists it. The result is fragile and also exposed to problem 1.",
 "Outcome changed to not_reproduced, resting on the unbounded exponent (assumed). Without the cap no fit meets reading (b): the "
 "discrete KS fit deviates by 0.538, at the pair delta' 180 ms, delta 594 ms (gamma 3.148, held at 2.843 by the cap). The pair "
 "(590, 6490 ms) is kept as the criterion lists it and is not the most deviant under the unbounded fit.")
add("fig2-exponents-above-two",True,"reproduced",
 "Under the KS readings, both gamma and beta(delta') exceed 2 in 15/15 pairs on grid (a) and 76/76 on grid (b). Eq. 8 holds within "
 "10% in 11 to 12 of 15 and 48 to 58 of 76 pairs.",
 "No change of outcome. With the exponent unbounded Eq. 8 holds in 9 and 12 of 15 and 45 and 58 of 76 pairs.")
add("fig2-other-neurons-similar",False,"reproduced",
 "Reproduced (fragile). The criterion is met under one reading. In set (b), ks_continuous gives 0.547 (grid a) and 0.560 (grid b), "
 "and x1_continuous gives 0.89 to 0.91. Set (a) passes only under x1_continuous (0.89). ks_discrete, the natural fit for integer "
 "data, gives 0.08 to 0.23. The set itself is questionable (problem 2).",
 "Outcome changed to reproduced: the criterion says more than half under one reading, which the round-1 assumption of the discrete "
 "fit overrode. With the exponent unbounded only the continuous fit from xmin = 1 passes (0.883 to 0.906); the continuous KS fit "
 "falls to 0.449 and 0.454, so the notes call the pass fragile. All 690 units are now fitted and the inhibitory units and all units "
 "are shown as variants (problem 2); whether the claim's set should be the pyramidal units is asked of a reader.")
add("fig2-wikipedia-beta",True,"blocked",
 "Blocked (data_missing). The archive's API lists only 8 NWB files of spike, LFP and behaviour data, so there is no Wikipedia data. "
 "The preprocessed edit histories came from a third party and were never deposited. The notebook's code too_large is less apt, as "
 "the raw dump exists, but the preprocessing that selects editors is not specified.",
 "Kept blocked as too_large, with the disagreement in the notes. The claims file has the claim as data elsewhere, for which the "
 "protocol does not use data_missing, and what stops a test from the public dump is its size (47.4 GB compressed).")
add("fig2-earthquake-beta",True,"blocked",
 "Not in the dandiset (confirmed via the API). The notebook's reason, that the catalog is revised and has no pinned version, is "
 "weak. The SCSN/SCEDC catalog for 1993 to 2020 is public, and the claim has a 10% tolerance on n, so it was testable approximately.",
 "Kept blocked as other, with the disagreement in the notes: the protocol allows outside data only when pinned, and the catalog has "
 "no versioned release. The count of the south cluster the verifier asked for was not made, for that reason.")
add("fig4-model-heavy-tails",True,"partially_reproduced",
 "Heavy tails are supported at more than half of the timescales and pairs for every series and seed. Under the claim's seed, "
 "however, no single fit reading meets the IQR < 0.5 condition for all three series. ks_discrete fails only on the exponential "
 "series' gamma IQR, 0.522 (grid a) and 0.502 (grid b). It holds for all three series in 4/4 further seeds on grid (a). Holds per "
 "series under any reading mixes readings across series.",
 "No change of outcome. With the exponent unbounded the exponential gamma interquartile range under the discrete KS fit is 0.544 "
 "and 0.508, and the discrete KS fit holds for all three series in 3 of the 4 further seeds (not + 4000). The cell now prints the "
 "result per series and reading for every seed.")
add("fig4-model-iet-shapes",True,"partially_reproduced",
 "Under the claim's seed only quadratic tau_max is within 10%, 21 391 against 20 800. Linear is 1711 against 1960 and exponential "
 "61 320 against 81 600. Across 5 seeds, within-tolerance counts are linear 2/5, quadratic 2/5, exponential 0/5. A single-realization "
 "maximum varies by about 3 to 20x across seeds, so a 10% tolerance is hardly testable. The shape comparison is not judged.",
 "No change.")
add("model-decremental-equivalent",True,"not_reproduced",
 "Under the literal reading (L), every timescale differs, with D up to 0.45. Under readings Z and Q, 0 to 11 rejections per seed. The "
 "same-algorithm reference (N) also rejects 1 to 14 per seed, so the criterion cannot be met even by identical generators (problem "
 "4). Under Z and Q the result is indistinguishable from N.",
 "No change of outcome. A test calibrated across runs was added as a variant (problem 4): with the five runs of each algorithm as "
 "units and an exact permutation test, N differs in no series, L in all three (p = 0.0079 each), Z in none and Q in the linear "
 "series only.")
R["verifications"]=[V]
class D(yaml.SafeDumper): pass
def str_rep(d,s):
    return d.represent_scalar("tag:yaml.org,2002:str",s)
D.add_representer(str,str_rep)
open(p,"w").write(yaml.dump(R,Dumper=D,sort_keys=False,width=100,allow_unicode=True,default_flow_style=False))
PYEOF
python $TMPDIR/rec.py && grep -n ": .*: " attempts/hiraoka-2025-01.yaml | grep -v "^\s*[0-9]*:\s*-\? *[a-z_]*: ['\"]" | head; python tools/entry.py check entries/hiraoka-2025 2>&1 | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent**

Record written and checks pass. Now the questions file for the claims-file point (pyramidal set excludes the representative unit's class).

**Agent calls Bash**

```bash
cd  cat > questions/hiraoka-2025.yaml <<'EOF'
questions:
- claim: fig2-other-neurons-similar
  question: The criterion reads the set of other neurons as the pyramidal units, of session
    Achilles-10252013 or of every session. The paper's own representative unit (unit 9 of
    Achilles-10252013, found by its spike count and IETs as row 9 of the units table) is labelled
    inhibitory in the version the paper cites and interneuron in the latest. Since the paper's
    "other sequences in the datasets" are compared with a unit the files call inhibitory, should
    the set be all units of the recordings, or include the inhibitory units, and not the
    pyramidal units alone?
  passage: Section III, paragraphs 2 and 5. "The first dataset consists of neuronal firing
    obtained from electrophysiological recordings of pyramidal cell activity in rat
    hippocampus" and "we show the results for a representative event sequence for each dataset
    ... unit 9 in the Achilles-10252013 session ... Other sequences in the datasets show similar
    patterns."
  why: The paper calls all its neuronal data pyramidal, but the unit it shows is not labelled so,
    which suggests it analysed every unit without the cell types. The fraction of units showing
    the pattern differs by class. With the exponent unbounded, under the KS fits it is 0.68 to
    0.74 for the 128 inhibitory units against 0.08 to 0.45 for the 562 pyramidal ones, and 0.32
    to 0.51 for all 690 units. The claim is reproduced under every set by the continuous fit
    from xmin = 1 (0.78 to 0.91), so the outcome does not change, but the set decides whether
    any KS reading of the fit passes.
EOF
python -c "import yaml;yaml.safe_load(open('questions/hiraoka-2025.yaml'))"; grep -rn "—\|rather" questions/hiraoka-2025.yaml attempts/hiraoka-2025-01.yaml entries/hiraoka-2025/*.ipynb entries/hiraoka-2025/*.py entries/hiraoka-2025/README.md | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/hiraoka-2025 2>&1 | tail -3; python -c "
import yaml;R=yaml.safe_load(open('attempts/hiraoka-2025-01.yaml'))
for o in R['outcomes']: print(o['claim'],o['outcome'],o.get('assumed',''),o.get('seed_sensitive',''),o.get('blocked_by',''))
print(len(R['findings']), len(R['verifications'][0]['results']))"; git status --short; date -u
```

```
0 error(s)
fig2-neuron-representative-sequence reproduced   
fig2-iet-broad reproduced   
fig2-neuron-burst-size-heavy-tail reproduced   
fig2-neuron-beta-stable not_reproduced   
fig2-neuron-beta-decrease-follows-gamma reproduced   
fig2-neuron-merging-heavy-tail reproduced   
fig2-neuron-merging-collapse not_reproduced True  
fig2-exponents-above-two reproduced   
fig2-other-neurons-similar reproduced   
fig2-wikipedia-beta blocked   too_large
fig2-earthquake-beta blocked   other
fig4-model-heavy-tails partially_reproduced True True 
fig4-model-iet-shapes partially_reproduced  True 
model-decremental-equivalent not_reproduced  True 
10 14
 M attempts/hiraoka-2025-01.yaml
 M entries/hiraoka-2025/README.md
 M entries/hiraoka-2025/bursttree.py
 M entries/hiraoka-2025/entry.yaml
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py run entries/hiraoka-2025 2>&1 | tail -3
```

```
pass  other_neurons_cap3.ipynb  (639 s, reused)
pass  model.ipynb  (1031 s, reused)
reused the executed copies of 2026-11-22 03:15 UTC: nothing the run reads has changed since (hash 603acfeb8553). Nothing was executed and no environment was built; --fresh runs it again.
```

**Agent**

I worked through every point in the round-1 report. The entry ran clean with `tools/entry.py all`: all four notebooks pass, the longest taking 50 minutes. The conclusions match the executed outputs, and `entry.py check` reports no errors.

**What changed in the outcomes**
- **fig2-neuron-beta-stable:** now `not_reproduced` (was `partially_reproduced`), as the verifier gave. The criterion has no partial outcome and neither of its readings holds.
- **fig2-neuron-merging-collapse:** now `not_reproduced` (was `reproduced`), resting on an assumption (`assumed: true`). Without the cap no fit stays within the 0.5 band: the closest misses at 0.538, against 0.490 with the cap.
- **fig2-other-neurons-similar:** now `reproduced` (was `not_reproduced`), as the verifier gave. The criterion counts a pass under any one fit reading, and my round-1 choice of the discrete KS fit overrode that. Only the continuous fit from xmin = 1 passes (0.883 to 0.906), so the notes call it fragile.
- **fig2-neuron-merging-heavy-tail:** kept `reproduced`, with the verifier's disagreement recorded. Without the cap, the discrete KS fit still keeps the γ IQR below 0.5 (0.378 and 0.415).
- **The two blocked claims:** kept as they were, with the disagreements recorded.
  - Wikipedia stays `too_large`: the claim is "data elsewhere", for which the protocol does not use `data_missing`.
  - Earthquakes stay `other`: the catalog has no versioned release, and the protocol only allows pinned outside data.
- **The other seven:** unchanged. fig2-neuron-burst-size-heavy-tail no longer needs an assumption, because every KS reading gives it.

**What I added or corrected**
- **The cap on the exponent (problem 1):** the verifier was right. The locked powerlaw 2.0.0 caps the exponent at 3 by default, and the cap also moves the choice of xmin. The fits now leave the exponent unbounded, as in the method the paper cites (Clauset et al.). The capped fits run beside them as a variant, and the notebooks print the powerlaw version and how many fits hit the cap.
- **Other neurons (problem 2):** all 690 units are now fitted. Inhibitory units and all units are shown beside the claim's pyramidal sets. A new notebook, `other_neurons_cap3.ipynb`, holds the capped variant on grid (a) only, to keep each notebook under 60 minutes.
- **Decremental model (problem 4):** a test calibrated across runs is added as a variant. It finds no difference between two runs of one algorithm, and a difference in all three series under the literal set-up. It does not decide the outcome.
- **Fig. 4 heavy tails:** the model notebook now prints the result for each series and fit reading under every seed.
- **Questions and findings:** added `questions/hiraoka-2025.yaml`. It asks a reader whether "pyramidal" misreads the paper, since the paper's own representative unit is labelled inhibitory. Under the KS fits the inhibitory units show the pattern in 0.68 to 0.74 of units, against 0.08 to 0.45 for pyramidal ones. I added a finding at the end that asks the paper's authors which powerlaw release they used and whether the exponent was bounded.
- **Record:** round 1 is recorded under `verifications`, with the verifier's reasons for all 14 claims and my responses. All notes and conclusions are rewritten to the new numbers.

**What I did not do**
- I did not count the earthquake south cluster from the current SCEDC catalog. That would rest on unpinned outside data, which the protocol does not allow.
- The verifier's other unanswered item, which circles in Figures 2 and 4 are filled, needs the paper's PDF, which was not supplied.
- I made no commits, as instructed.

## End of run

60 turns, 164 minutes, $7.23 at API prices, result: success.
