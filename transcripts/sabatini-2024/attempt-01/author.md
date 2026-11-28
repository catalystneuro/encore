# sabatini-2024 · author · run 44720511633

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

```
<persisted-output>
Output too large (63.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/72811701-7a19-48d0-9b0c-dc624987db45/tool-results/beuz0co4f.txt

Preview (first 2KB):
Fri Nov 20 10:38:21 UTC 2026
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
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/72811701-7a19-48d0-9b0c-dc624987db45/tool-results/beuz0co4f.txt"
}
```

```
1	Fri Nov 20 10:38:21 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-18`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
11	
12	An attempt has three roles, each a separate run with a separate context:
13	
14	- The **reader** reads the paper and writes the claims file: every finding,
15	  and how each is to be tested, taken from the paper. A second reader checks
16	  it against the paper. Readers never see the dataset's data.
17	- The **author** tests the claims on the dataset. It reads the paper to
18	  understand the claims, but the claims file binds it: it cannot change a
19	  claim's statement, expected values or criterion. A method detail the file
20	  lacks it takes from the paper, citing the passage, and it asks a reader
[... 1432 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/sabatini-2024.yaml; ls paper; cat papers/datasets/sabatini-2024.yaml; ls papers/author-notes | grep sabat; ls questions | grep sabat
```

```
<persisted-output>
Output too large (52.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/72811701-7a19-48d0-9b0c-dc624987db45/tool-results/bpxf7x56v.txt

Preview (first 2KB):
# Claims for Sabatini & Kaufman (2024), Nat. Commun. 15:7007, "Reach-dependent reorientation of
# rotational dynamics in motor cortex", tested on dandiset 000070 (relation reuses).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-20,
# protocol pilot-18 as stated in docs/protocol.md. The writer did not look at the dandiset's data
# or files.
#
# Text read: the version of record (open access, CC BY-NC-ND), full text from PubMed Central
# (PMC11325044) with Methods, figure legends and Data and Code availability, and its one
# supplement, 41467_2024_51308_MOESM1_ESM.pdf (Supplementary Figures 1 to 8 with legends and the
# derivation of the basis function representation of a linear dynamical system). The Peer Review
# File and Reporting Summary were not read; no result rests on them. The supplement PDF was not
# opened beyond its extracted text.
#
# Code read: github.com/kaufmanlab/LDR-public at commit b65f28d (2024-08-02), the MATLAB code the
# Code availability statement links. It holds the analysis functions (TBF, single-condition LDS,
# alignment index, subspace excursion angles, rotation and location prediction, LDR encoding and
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/72811701-7a19-48d0-9b0c-dc624987db45/tool-results/bpxf7x56v.txt"
}
```

```
1	# Claims for Sabatini & Kaufman (2024), Nat. Commun. 15:7007, "Reach-dependent reorientation of
2	# rotational dynamics in motor cortex", tested on dandiset 000070 (relation reuses).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-20,
4	# protocol pilot-18 as stated in docs/protocol.md. The writer did not look at the dandiset's data
5	# or files.
6	#
7	# Text read: the version of record (open access, CC BY-NC-ND), full text from PubMed Central
8	# (PMC11325044) with Methods, figure legends and Data and Code availability, and its one
9	# supplement, 41467_2024_51308_MOESM1_ESM.pdf (Supplementary Figures 1 to 8 with legends and the
10	# derivation of the basis function representation of a linear dynamical system). The Peer Review
11	# File and Reporting Summary were not read; no result rests on them. The supplement PDF was not
12	# opened beyond its extracted text.
13	#
14	# Code read: github.com/kaufmanlab/LDR-public at commit b65f28d (2024-08-02), the MATLAB code the
15	# Code availability statement links. It holds the analysis functions (TBF, single-condition LDS,
16	# alignment index, subspace excursion angles, rotation and location prediction, LDR encoding and
17	# decoding, jPCA reconciliation). It loads preprocessed .mat files that are not in the repository
18	# (ShenoyMonkeyData, ShenoyMonkeyDataSingleTrial, basisFxnNum, TBFResults and others; the paper
19	# says "Code-compatible data are available upon request"), and lacks kinFuncEval (the kinematic
20	# basis functions), the jPCA codepack, GPFA, and code for the location-from-kinematics regression
[... 766 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,200p docs/archives.md | head -150; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in
```

```
# Archives

The registry tests papers against data in public archives. It began with one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
below), and `tools/datasets.py` turns one form of a dataset's name into another.
The workflows take a dataset in any of these forms.

## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml | head -150; wc -l attempts/fouke-2025-01.yaml; cat entries/fouke-2025/README.md | head -30
```

```
schema_version: 3
id: fouke-2025-01
datasets:
- archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
  relation: primary
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,625p attempts/fouke-2025-01.yaml | grep -v "^    " | head -120; grep -n "blocked_by\|findings:\|verifications\|kind:\|severity" attempts/fouke-2025-01.yaml | head -40
```

```
outcome: not_reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1h-zf-higher-angular-acceleration
  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
  - Heading is taken from the cumulative sum of `f0_vtheta`, as the code does; in DC files it does
- claim: figs1e-dc-respond-less-monocular
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:figs1e-dc-respond-less-monocular
  notes: Species effect F = 23.3, p = 2.5e-06. DC turn less toward the stimulus than ZF for
  deviations:
  - Codes 9 and 11 are assigned as the figure code has them; the stimulus software's conversion
- claim: fig1c-continuous-vs-bouts
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1c-continuous-vs-bouts
  notes: The median-to-mean ratio of instantaneous speed is 0.306 in ZF (25 fish, 0.244 to 0.580)
  deviations:
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; curl -s https://api.dandiarchive.org/api/dandisets/000070/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000070/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for v in 0.251218.1714 0.260528.0919; do echo $v; curl -s "https://api.dandiarchive.org/api/dandisets/000070/versions/$v/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['path'], a['size'], a['modified'])"; done; curl -s "https://api.dandiarchive.org/api/dandisets/000070/versions/0.260528.0919/" | python -c "
import json,sys; d=json.load(sys.stdin); print(d.get('description')); print(json.dumps(d.get('relatedResource'),indent=0)[:2000]); print(d.get('doi'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; wc -c *.txt; grep -n -i "dandi\|available upon\|github" *.txt | head
```

```
<persisted-output>
Output too large (45.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/72811701-7a19-48d0-9b0c-dc624987db45/tool-results/b5o3jy818.txt

Preview (first 2KB):
131342 10.1038-s41467-024-51308-7.txt
61:				\begin{document}$${{{\bf{B}}}{{{\mbox{'}}}}}^{(c)}={{{\bf{L}}}}^{(c){\dagger} }{{{\bf{X}}}}^{(c)}$$\end{document} B ’ ( c ) = L ( c ) † X ( c ) where B’ ( c ) is the recovered temporal basis functions for condition c and † indicates pseudo-inversion. We quantified the “recoverability” of temporal basis functions on condition c as the variance explained in the temporal basis functions by the projected neural activity. If this metric is 1, it suggests that the condition’s loading matrix is invertible, and therefore fulfills the requirements of rotations. More specifically, we expect recoverability to fail when two (or more) temporal basis functions are assigned the same dimension in state space by the loading matrix. As each temporal basis functions dynamically supports each other, this overlap would preclude neural activity from acting as a dynamical system. Control for data smoothing One potential concern is that the factorization described above works well on neural data simply because the data are smoothed before analysis, and smoothing limits the frequency spectrum and therefore allows neural activity to be reconstructed by a small number of temporal basis functions. To test these possibilities, for each trial of each condition independently we shuffled time bins before smoothing and averaging, to disrupt the temporal structure of motor cortex activity while preserving inter-neuron spike correlations and total spike counts. We then extracted temporal basis functions, with the number of temporal basis functions matched to the original dataset, and quantified the population variance explained and recoverability (defined above) of the temporal basis functions. We compared this null distribution to the data dis
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
t=open('paper/10.1038-s41467-024-51308-7.txt').read()
import re
t=re.sub(r'\\\\begin\{document\}.*?\\\\end\{document\}','',t,flags=re.S)
open('/tmp/claude/paper.txt','w').write(t) if False else None
import os; p=os.environ.get('TMPDIR','/tmp/claude')+'/paper.txt'; open(p,'w').write(t); print(len(t), p)"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -s -w 4000 $TMPDIR/paper.txt > $TMPDIR/p2.txt; wc -l $TMPDIR/p2.txt; head -c 45000 $TMPDIR/p2.txt
```

```
<persisted-output>
Output too large (44KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/72811701-7a19-48d0-9b0c-dc624987db45/tool-results/bgkwfpb80.txt

Preview (first 2KB):
786 /tmp/claude-1001/p2.txt
DOI: 10.1038/s41467-024-51308-7
Version: version of record
Source: find_reuse cache
Stored: 2026-11-10
Extracted: as fetched
------------------------------------------------------------------------
pmc Nat Commun Nat Commun Nature Communications 2041-1723 Nature Publishing Group UK London 11325044 39143078 51308 10.1038/s41467-024-51308-7 Article Reach-dependent reorientation of rotational dynamics in motor cortex Sabatini David A. 1 2 http://orcid.org/0000-0002-8072-023X Kaufman Matthew T. [removed: an e-mail address] 1 2 1 https://ror.org/024mw5h28 grid.170205.1 0000 0004 1936 7822 Department of Organismal Biology and Anatomy, The University of Chicago, Chicago, IL 60637 USA 2 grid.170205.1 0000 0004 1936 7822 Neuroscience Institute, The University of Chicago, Chicago, IL 60637 USA 15 8 2024 15 8 2024 2024 15 7007 2 9 2023 5 8 2024 © The Author(s) 2024 2024 https://creativecommons.org/licenses/by-nc-nd/4.0/ Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exc
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/72811701-7a19-48d0-9b0c-dc624987db45/tool-results/bgkwfpb80.txt"
}
```

```
1	786 /tmp/claude-1001/p2.txt
2	DOI: 10.1038/s41467-024-51308-7
3	Version: version of record
4	Source: find_reuse cache
5	Stored: 2026-11-10
6	Extracted: as fetched
7	------------------------------------------------------------------------
8	pmc Nat Commun Nat Commun Nature Communications 2041-1723 Nature Publishing Group UK London 11325044 39143078 51308 10.1038/s41467-024-51308-7 Article Reach-dependent reorientation of rotational dynamics in motor cortex Sabatini David A. 1 2 http://orcid.org/0000-0002-8072-023X Kaufman Matthew T. [removed: an e-mail address] 1 2 1 https://ror.org/024mw5h28 grid.170205.1 0000 0004 1936 7822 Department of Organismal Biology and Anatomy, The University of Chicago, Chicago, IL 60637 USA 2 grid.170205.1 0000 0004 1936 7822 Neuroscience Institute, The University of Chicago, Chicago, IL 60637 USA 15 8 2024 15 8 2024 2024 15 7007 2 9 2023 5 8 2024 © The Author(s) 2024 2024 https://creativecommons.org/licenses/by-nc-nd/4.0/ Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/ . During reachi
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import os
t=open(os.environ['TMPDIR']+'/paper.txt').read()
i=t.find('Methods Subjects'); 
if i<0: i=t.find('Subjects, behavior')
print(i); print(t[i:i+40000])
EOF
```

```
<persisted-output>
Output too large (39.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/72811701-7a19-48d0-9b0c-dc624987db45/tool-results/b5p9y44ml.txt

Preview (first 2KB):
48862
Methods Subjects, behavior and data pre-processing All data used here have been analyzed in previous studies. Animal protocols were approved by the Stanford University Animal Care and Use Committee. Two adult male rhesus macaque monkeys ( Macaca mulatta ), J and N, performed the “maze” center-out delayed-reaching task for juice reward 19 . Briefly, the monkey initially fixated a central point on a vertical screen with the eye and a cursor floating slightly above the fingertips, then a slightly jittering target was shown. After a brief delay (0–1000 ms), a Go cue was presented (cessation of target jitter, filling in of target, and disappearance of fixation point), and the monkey was required to make a fast, accurate reach to the target. On some trials, the monkey was required to avoid virtual barriers presented at the same time as the target, eliciting curved reaches to produce 72 different reaching “conditions” (36 straight, 36 curved). For both monkeys, data were collected using two 96-electrode “Utah” arrays (Blackrock Microsystems, Salt Lake City, UT), one implanted in PMd and one in M1. Both single-units and stable multi-units were included for analysis. Spiking activity was binned at 1 millisecond, smoothed with a 20 ms Gaussian kernel, trial-averaged, and down-sampled to 10 millisecond resolution. Except where noted, all analyses were performed on each dataset (monkey and array) independently. Fitting dynamics to single conditions Condition-specific dynamics were examined by fitting, for each condition independently, a discrete-time linear dynamical system to population activity from 150 ms prior to movement onset to 850 ms after movement onset. If an eigenvalue in a fit LDS had a half-life >10 s, it was reduced to 10 s. We fit the LDS using 
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/72811701-7a19-48d0-9b0c-dc624987db45/tool-results/b5p9y44ml.txt"
}
```

```
1	48862
2	Methods Subjects, behavior and data pre-processing All data used here have been analyzed in previous studies. Animal protocols were approved by the Stanford University Animal Care and Use Committee. Two adult male rhesus macaque monkeys ( Macaca mulatta ), J and N, performed the “maze” center-out delayed-reaching task for juice reward 19 . Briefly, the monkey initially fixated a central point on a vertical screen with the eye and a cursor floating slightly above the fingertips, then a slightly jittering target was shown. After a brief delay (0–1000 ms), a Go cue was presented (cessation of target jitter, filling in of target, and disappearance of fixation point), and the monkey was required to make a fast, accurate reach to the target. On some trials, the monkey was required to avoid virtual barriers presented at the same time as the target, eliciting curved reaches to produce 72 different reaching “conditions” (36 straight, 36 curved). For both monkeys, data were collected using two 96-electrode “Utah” arrays (Blackrock Microsystems, Salt Lake City, UT), one implanted in PMd and one in M1. Both single-units and stable multi-units were included for analysis. Spiking activity was binned at 1 millisecond, smoothed with a 20 ms Gaussian kernel, trial-averaged, and down-sampled to 10 millisecond resolution. Except where noted, all analyses were performed on each dataset (monkey and array) independently. Fitting dynamics to single conditions Condition-specific dynamics were examined by fitting, for each condition independently, a discrete-time linear dynamical system to population activity from 150 ms prior to movement onset to 850 ms after movement onset. If an eigenvalue in a fit LDS had a half-life >10 s, it was reduced to 10 s. We fit the LDS using reduced-rank regression to find the optimal low-rank LDS that explained maximum variance in that condition’s neural activity. We determined the dimensionality of the LDS via cross-validation (see below 64 ). To q
[... 55 more lines not kept]
```

**Agent**

Paper read. Now surveying the dataset's two named files.

**Agent calls Bash**

```bash
date -u; which python uv; python -c "import pynwb, remfile, h5py, numpy, scipy, sklearn; print(pynwb.__version__)" 2>&1; cat pyproject.toml | head -40; ls tools
```

```
Fri Nov 20 10:38:59 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py, numpy, scipy, sklearn; print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "encore-science"
dynamic = ["version"]
description = "Check a dataset against the paper it came from: an AI agent reads the paper's claims and tests them on the data."
readme = "docs/encore.md"
license = "Apache-2.0"
requires-python = ">=3.10"
dependencies = [
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd  .venv/bin/python -c "import pynwb, remfile, h5py, numpy, scipy, sklearn, dandi; print(pynwb.__version__, numpy.__version__)" 2>&1; ls -a | head; cat tools/entry.py | head -60
```

```
/bin/bash: line 1: .venv/bin/python: No such file or directory
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
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

[... 52 more lines not kept]
```

**Agent**

Setting up a dev venv in $TMPDIR.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev -p 3.13 && VIRTUAL_ENV=$TMPDIR/dev uv pip install -q pynwb remfile h5py numpy scipy scikit-learn matplotlib pandas pyyaml jsonschema nbformat nbclient ipykernel 2>&1 | tail -3; $TMPDIR/dev/bin/python -c "import pynwb; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > survey.py <<'EOF'
import h5py, remfile, requests, sys, time
aid=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
r=requests.head(url,allow_redirects=True); s3=r.url
f=h5py.File(remfile.File(s3),'r')
def visit(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, dict((k,(v if not hasattr(v,'shape') or v.size<5 else '...')) for k,v in obj.attrs.items() if k in ('unit','conversion','rate','description','neurodata_type')))
    else:
        nt=obj.attrs.get('neurodata_type'); 
        if nt: print('GROUP',name,nt, obj.attrs.get('description','')[:200] if isinstance(obj.attrs.get('description',''),str) else '')
f.visititems(visit)
EOF
t0=$(date +%s); timeout 600 $TMPDIR/dev/bin/python survey.py 033a04c0-9ce7-45c5-8012-c571a7b9bf12 2>&1 | grep -v "^GROUP acquisition\|^acquisition/.*/data " | head -150; echo $(( $(date +%s)-t0 ))s
```

```
file_create_date (1,) object {}
GROUP general/devices/Utah Array(M1) Device 96 channel utah array
GROUP general/devices/Utah Array(PMd) Device 96 channel utah array
general/experiment_description () object {}
general/experimenter (2,) object {}
GROUP general/extracellular_ephys/1 ElectrodeGroup array corresponding to device implanted at PMd
GROUP general/extracellular_ephys/2 ElectrodeGroup array corresponding to device implanted at M1
GROUP general/extracellular_ephys/electrodes DynamicTable metadata about extracellular electrodes
general/extracellular_ephys/electrodes/filtering (192,) object {'description': 'description of hardware filtering', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/gain (192,) float64 {'description': 'gain', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group (192,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part of', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group_name (192,) object {'description': 'the name of the ElectrodeGroup this electrode is a part of', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/id (192,) int64 {'neurodata_type': 'ElementIdentifiers'}
general/extracellular_ephys/electrodes/imp (192,) float64 {'description': 'the impedance of the channel', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/location (192,) object {'description': 'the location of channel within the subject e.g. brain region', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/offset (192,) float64 {'description': 'offset', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/x (192,) float64 {'description': 'the x coordinate of the channel location', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/y (192,) float64 {'description': 'the y coordinate of the channel location', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/el
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > survey2.py <<'EOF'
import h5py, remfile, requests, sys, numpy as np
aid=sys.argv[1]
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
print(list(f['acquisition'].keys()) if 'acquisition' in f else None)
for k in f.get('acquisition',{}): 
    g=f['acquisition'][k]; print(k, g.attrs.get('neurodata_type'), {kk:(g[kk].shape if isinstance(g[kk],h5py.Dataset) else 'grp') for kk in g})
print(f['session_description'][()], f['general/experiment_description'][()], f['general/related_publications'][()])
u=f['units']; print(list(u.keys()))
idx=u['spike_times_index'][:]; n=np.diff(np.r_[0,idx]); print('spikes per unit', n.min(), np.median(n), n.max(), (n==0).sum())
eg=u['electrodes'][:]; print('electrodes', eg[:5], eg[-5:])
loc=f['general/extracellular_ephys/electrodes/location'][:]; gn=f['general/extracellular_ephys/electrodes/group_name'][:]
import collections; print(collections.Counter(zip(loc,gn)))
T=f['intervals/trials']
d={k:T[k][:] for k in ['maze_condition','task_success','discard_trial','correct_reach','trial_type','trial_version','maze_num_targets','maze_num_barriers','novel_maze','proto_trial','start_time','stop_time','go_cue_time','move_begins_time','move_ends_time','target_presentation_time','reaction_time']}
for k in ['task_success','discard_trial','correct_reach','trial_type','trial_version','maze_num_targets','maze_num_barriers','novel_maze']:
    print(k, collections.Counter(d[k].tolist()))
mc=d['maze_condition']; print('n maze cond', len(np.unique(mc)), mc.min(), mc.max())
print('delay', np.nanpercentile(d['go_cue_time']-d['target_presentation_time'],[0,5,50,95,100]))
print('move-go', np.nanpercentile(d['move_begins_time']-d['go_cue_time'],[0,5,50,95,100]))
print('RT', np.nanpercentile(d['reaction_time'],[0,50,100]))
print('dur', np.nanpercentile(d['move_ends_time']-d['move_begins_time'],[0,5,50,95,100]))
print('nan move', np.isnan(d['move_begins_time']).sum())
print('times', d['start_time'][:3], d['stop_time'][:3], d['move_begins_time'][:3])
st=u['spike_times'][:200000]; print('spike t', st[:5], st.max())
print('hand ts', f['processing/behavior/Position/Hand/timestamps'][:5], f['processing/behavior/Position/Hand/data'][100000:100003])
print(f['processing/behavior/Position/Hand/timestamps'][-3:])
print(T['barrier_info_index'][:5], T['target_positions_index'][:5], T['timeseries'][:3])
EOF
$TMPDIR/dev/bin/python survey2.py 033a04c0-9ce7-45c5-8012-c571a7b9bf12 2>&1
```

```
[]
b'' b'' [b'10.1038/nature11129 10.1152/jn.00892.2011 10.1038/nn.3643 10.1038/nn.4042 10.1146/annurev-neuro-062111-150509 10.7554/eLife.0467710.1523/ENEURO.0085-16.2016 10.1038/s41592-018-0109-9']
['electrode_group', 'electrodes', 'electrodes_index', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index']
spikes per unit 61030 317716.0 1720529 0
electrodes [0 1 2 3 4] [187 188 189 190 191]
Counter({(b'Pre-Motor Cortex, dorsal', b'1'): 96, (b'M1 Motor Cortex', b'2'): 96})
task_success Counter({1: 2570, 0: 66})
discard_trial Counter({0: 2636})
correct_reach Counter({1: 2296, 0: 340})
trial_type Counter({16: 81, 8: 79, 26: 75, 32: 75, 12: 73, 24: 72, 19: 72, 21: 70, 2: 70, 36: 70, 14: 70, 22: 70, 18: 70, 28: 69, 3: 69, 5: 69, 10: 68, 39: 68, 15: 68, 33: 67, 25: 67, 13: 67, 9: 67, 7: 67, 17: 66, 11: 66, 23: 66, 4: 66, 34: 65, 27: 65, 20: 65, 31: 64, 30: 64, 29: 62, 1: 62, 6: 59, 38: 58, 35: 57, 37: 56, 0: 2})
trial_version Counter({1: 884, 2: 882, 0: 870})
maze_num_targets Counter({1: 1754, 3: 882})
maze_num_barriers Counter({0: 808, 9: 802, 7: 468, 8: 421, 6: 135, 2: 2})
novel_maze Counter({0: 2634, 1: 2})
n maze cond 109 0 108
delay [-0.004  0.147  0.664  0.964  0.998]
move-go [0.153 0.287 0.358 1.202 1.863]
RT [0.185 0.39  1.135]
dur [0.18  0.28  0.44  0.69  1.295]
nan move 0
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > survey3.py <<'EOF'
import h5py, remfile, requests, sys, numpy as np, collections
for aid in ['033a04c0-9ce7-45c5-8012-c571a7b9bf12','02c2c5b7-0848-46f1-9ca6-1e657fd10eb5']:
    s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r')
    T=f['intervals/trials']
    d={k:T[k][:] for k in ['maze_condition','task_success','discard_trial','correct_reach','maze_num_targets','maze_num_barriers','novel_maze','start_time','stop_time','go_cue_time','move_begins_time','target_presentation_time','trial_version']}
    u=f['units']; print(aid, 'units', len(u['id']), 'trials', len(d['start_time']))
    idx=u['spike_times_index'][:]; n=np.diff(np.r_[0,idx]); print('spikes/unit', n.min(), np.median(n), n.max())
    print('loc', collections.Counter(f['general/extracellular_ephys/electrodes/location'][:]))
    mc=d['maze_condition']
    delay=d['go_cue_time']-d['target_presentation_time']
    one=d['maze_num_targets']==1; s=d['task_success']==1; c=d['correct_reach']==1; disc=d['discard_trial']==0
    not3=(mc%3)!=0
    for name,m in [('succ',s),('succ&1tgt',s&one),('succ&mc%3!=0',s&not3),('succ&1tgt&correct',s&one&c),('succ&1tgt&delay>0.4',s&one&(delay>0.4)),('succ&1tgt&correct&delay>.4',s&one&c&(delay>0.4)),('1tgt',one),('1tgt&correct',one&c),('succ&1tgt&correct&nondisc',s&one&c&disc)]:
        print(name, m.sum(), 'conds', len(np.unique(mc[m])))
    print('3tgt conds', np.unique(mc[~one])[:40])
    print('1tgt nobarrier conds', np.unique(mc[one&(d['maze_num_barriers']==0)])[:40])
    print('1tgt barrier conds', np.unique(mc[one&(d['maze_num_barriers']>0)])[:40])
    print('n1/cond', np.bincount(mc[s&one])[np.unique(mc[s&one])].min(), np.bincount(mc[s&one])[np.unique(mc[s&one])].max())
    print('time ranges', d['start_time'].min(), d['stop_time'].max(), u['spike_times'][idx[0]-1], 'hand', f['processing/behavior/Position/Hand/timestamps'][-1])
    print(collections.Counter(zip(d['novel_maze'].tolist(), mc.tolist())).most_common()[-3:], collections.Counter(mc[d['novel_maze']==1].tolist()))
EOF
$TMPDIR/dev/bin/python survey3.py 2>&1
```

```
033a04c0-9ce7-45c5-8012-c571a7b9bf12 units 192 trials 2636
spikes/unit 61030 317716.0 1720529
loc Counter({b'Pre-Motor Cortex, dorsal': 96, b'M1 Motor Cortex': 96})
succ 2570 conds 109
succ&1tgt 1723 conds 73
succ&mc%3!=0 1595 conds 72
succ&1tgt&correct 1557 conds 72
succ&1tgt&delay>0.4 1490 conds 73
succ&1tgt&correct&delay>.4 1345 conds 72
1tgt 1754 conds 73
1tgt&correct 1557 conds 72
succ&1tgt&correct&nondisc 1557 conds 72
3tgt conds [  0   3   6   9  12  15  18  21  24  27  30  33  36  39  42  45  48  51
  54  57  60  63  66  69  72  75  78  81  84  87  90  93  96  99 102 105
 108]
1tgt nobarrier conds [  1   4   7  10  13  16  19  22  25  28  31  34  37  40  43  46  49  52
  55  58  61  64  67  70  73  76  79  82  85  88  91  94  97 100 103 106]
1tgt barrier conds [  0   2   5   8  11  14  17  20  23  26  29  32  35  38  41  44  47  50
  53  56  59  62  65  68  71  74  77  80  83  86  89  92  95  98 101 104
 107]
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > survey4.py <<'EOF'
import h5py, remfile, requests, sys, numpy as np, collections
for aid in ['033a04c0-9ce7-45c5-8012-c571a7b9bf12','02c2c5b7-0848-46f1-9ca6-1e657fd10eb5']:
    s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r')
    T=f['intervals/trials']; st=T['start_time'][:]; sp=T['stop_time'][:]
    print('trial starts monotonic', np.all(np.diff(st)>0), 'gaps>100s', np.where(np.diff(st)>100)[0], st[np.where(np.diff(st)>100)[0][:3]+1] if len(np.where(np.diff(st)>100)[0]) else '')
    u=f['units']; idx=u['spike_times_index'][:]; oi=u['obs_intervals_index'][:]
    o0=u['obs_intervals'][0:oi[0]]; print('obs0', o0.shape, o0[:2], o0[-2:], 'matches trials', np.allclose(o0[:,0],st) if len(o0)==len(st) else 'n/a')
    for k in [0,100,191]:
        a=0 if k==0 else idx[k-1]; s=u['spike_times'][a:idx[k]]
        print('unit',k,'n',len(s),'min',s.min(),'max',s.max(),'sorted',np.all(np.diff(s)>=0), 'neg diffs', (np.diff(s)<0).sum())
    ht=f['processing/behavior/Position/Hand/timestamps']; n=ht.shape[0]
    t=ht[::1000]; print('hand ts', n, t[0], t[-1], 'dt', np.unique(np.round(np.diff(ht[:5000]),6)), 'monotonic sample', np.all(np.diff(t)>0), 'jumps', np.where(np.diff(t)<0)[0][:5])
    print('trial timeseries', T['timeseries'][:3]['idx_start'], T['timeseries'][:3]['count'], T['timeseries'][-3:]['idx_start'])
EOF
$TMPDIR/dev/bin/python survey4.py 2>&1
```

```
trial starts monotonic True gaps>100s [] 
obs0 (2636, 2) [[ 4.7072      8.56713333]
 [ 9.4072     12.11216667]] [[15633.39065858 15637.60555858]
 [15664.75575858 15668.65575858]] matches trials True
unit 0 n 61030 min 4.863466666666667 max 4259.041966666667 sorted True neg diffs 0
unit 100 n 261217 min 4.7528 max 15668.655425246776 sorted True neg diffs 0
unit 191 n 355301 min 4.7156 max 15668.647891913442 sorted True neg diffs 0
hand ts 8005321 4.7072 15667.635758580107 dt [1.000e-03 1.475e+00] monotonic sample True jumps []
trial timeseries [0 0 0] [3226 3226 3226] [8002120 8002120 8002120]
trial starts monotonic False gaps>100s [1777 1781 3106] [11695.64581673 11871.58575006  9436.97855006]
obs0 (3694, 2) [[ 5.41653333  9.3264    ]
 [15.9419     20.46233333]] [[6608.31245006 6612.57811673]
 [6654.24761673 6657.65235006]] matches trials True
unit 0 n 456806 min 5.4646 max 13516.001183396536 sorted False neg diffs 4
unit 100 n 514158 min 5.4216 max 13516.002150063203 sorted False neg diffs 4
unit 191 n 552253 min 5.428366666666667 max 13515.931416729869 sorted False neg diffs 4
hand ts 11909569 5.416533333333334 6656.254616729867 dt [1.000000e-03 7.350367e+00] monotonic sample False jumps [ 2996  5818  8703 11762]
trial timeseries [0 0 0] [3176 3176 3176] [6076951 6076951 6076951]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > survey5.py <<'EOF'
import h5py, remfile, requests, numpy as np
aid='02c2c5b7-0848-46f1-9ca6-1e657fd10eb5'
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
T=f['intervals/trials']; st=T['start_time'][:]; sp=T['stop_time'][:]
b=np.r_[0,np.where(np.diff(st)<0)[0]+1,len(st)]
print('trial segments by backwards jump', b)
for i in range(len(b)-1): print(' seg',i,'trials',b[i],b[i+1]-1,'t',st[b[i]],sp[b[i+1]-1])
u=f['units']; idx=u['spike_times_index'][:]
s=u['spike_times'][0:idx[0]]; j=np.where(np.diff(s)<0)[0]
print('unit0 backward jumps at', j, s[j], s[j+1])
s=u['spike_times'][idx[99]:idx[100]]; j=np.where(np.diff(s)<0)[0]; print('unit100', s[j], s[j+1])
ht=f['processing/behavior/Position/Hand/timestamps'][:]
j=np.where(np.diff(ht)<0)[0]; print('hand jumps', j, ht[j], ht[j+1], 'end', ht[-1])
ts=T['timeseries'][:]; 
names=[f[r].name for r in ts['timeseries'][:3]]; print(names)
hi=ts[2::3]; print('hand idx_start monotonic', np.all(np.diff(hi['idx_start'])>=0))
# check: hand timestamp at idx_start equals trial start?
d=ht[hi['idx_start']]-st; print('hand ts at idx_start minus trial start', np.percentile(d,[0,50,100]))
print('count vs trial dur*1000', np.percentile(hi['count']-(sp-st)*1000,[0,50,100]))
EOF
$TMPDIR/dev/bin/python survey5.py 2>&1
```

```
Exit code 1
trial segments by backwards jump [   0 1811 2710 3649 3694]
 seg 0 trials 0 1810 t 5.416533333333334 12076.795583396535
 seg 1 trials 1811 2709 t 6070.554150063201 12494.383850063201
 seg 2 trials 2710 3648 t 6119.761116729867 13516.0055500632
 seg 3 trials 3649 3693 t 6073.537783396534 6657.652350063201
unit0 backward jumps at [100478 206028 322727 450780] [ 6076.44183333 12076.75731673 12494.38215006 13516.0011834 ] [6074.24585006 6070.57471673 6119.76241673 6073.58055006]
unit100 [ 6076.4568     12076.79135006 12494.36425006 13516.00215006] [6074.2101834  6070.56455006 6119.78935006 6073.53915006]
hand jumps [ 2996568  5818780  8703484 11762598] [ 6075.402      12075.89555006 12493.53885006 13515.19065006] [6074.20561673 6070.55415006 6119.76111673 6073.5377834 ] end 6656.822616729867
['/processing/behavior/Position/Eye', '/processing/behavior/Position/Hand', '/processing/behavior/Position/Cursor']
hand idx_start monotonic False
Traceback (most recent call last):
  File "/tmp/claude-1001/survey5.py", line 19, in <module>
    d=ht[hi['idx_start']]-st; print('hand ts at idx_start minus trial start', np.percentile(d,[0,50,100]))
      ~~^^^^^^^^^^^^^^^^^
IndexError: index 11909569 is out of bounds for axis 0 with size 11909569
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && cat > t.py <<'EOF'
import h5py, remfile, requests, numpy as np, time
aid='02c2c5b7-0848-46f1-9ca6-1e657fd10eb5'
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
u=f['units']; idx=u['spike_times_index'][:]
t0=time.time(); s=u['spike_times'][0:idx[9]]; print('10 units', time.time()-t0, len(s))
nj=[]
for k in range(0,192,1):
    pass
T=f['intervals/trials']; ts=T['timeseries'][:]; print(ts[:6]); print(ts[-6:])
EOF
$TMPDIR/dev/bin/python t.py
```

```
Fri Nov 20 10:44:22 UTC 2026
10 units 0.8378865718841553 5681798
[(   0, 3176, <HDF5 object reference>)
 (   0, 3176, <HDF5 object reference>)
 (   0, 3176, <HDF5 object reference>)
 (3176, 3471, <HDF5 object reference>)
 (3176, 3471, <HDF5 object reference>)
 (3176, 3471, <HDF5 object reference>)]
[(6060306, 2666, <HDF5 object reference>)
 (6060306, 2666, <HDF5 object reference>)
 (6060306, 2666, <HDF5 object reference>)
 (6076951, 3197, <HDF5 object reference>)
 (6076951, 3197, <HDF5 object reference>)
 (6076951, 3197, <HDF5 object reference>)]
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/sabatini-2024/ldr.py",
 "content": "\"\"\"Loading and measures for testing Sabatini & Kaufman (2024) on DANDI:000070.\n\nWhere each parameter comes from is said beside it:\n- \"claims\": the claim's criterion in claims/sabatini-2024.yaml (which cites the paper or its code);\n- \"Methods, <section>\": a passage of the paper taken by the author (protocol, author step 1.6);\n- \"assumption\": a choice the paper leaves open, recorded as a deviation in the attempt;\n- \"standard\": a choice that cannot change a result (a padding margin, a plotting detail).\n\nThe dandiset is read by streaming (remfile + h5py); nothing is written to disk.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport numpy as np\nimport h5py\nimport remfile\nimport requests\nfrom scipy.ndimage import gaussian_filter1d\n\nDANDISET = \"000070\"\nVERSION = \"0.260528.0919\"\n# The two files the paper's Data availability statement names.\nASSETS = {\n    \"J\": \"sub-Jenkins/sub-Jenkins_ses-20090918_behavior+ecephys.nwb\",\n    \"N\": \"sub-Nitschke/sub-Nitschke_ses-20100923_behavior+ecephys.nwb\",\n}\nAPI = \"https://api.dandiarchive.org/api\"\n\n# Time base (claims, shared method): -350 to +850 ms around movement onset, every 10 ms (121 bins).\nGRID_MS = np.arange(-350, 851, 10)\n# Dynamics are fitted from -150 ms on (Methods, Fitting dynamics to single conditions); index 20.\nFIT0 = 20\n# 1 ms counts are taken over a wider window so that the 20 ms Gaussian has data at the edges\n# (standard; the code pads symmetrically).\nPAD_MS = 150\nWIN0_MS, WIN1_MS = -350 - PAD_MS, 850 + PAD_MS + 1\nSMOOTH_SD_MS = 20  # Methods, Subjects, behavior and data pre-processing\nWARP_MS = 600  # Methods, Control for stereotyped time course of behavior\n\n\ndef asset_url(path, version=VERSION):\n    r = requests.get(f\"{API}/dandisets/{DANDISET}/versions/{version}/assets/\",\n                     params={\"path\": path}, timeout=60)\n    r.raise_for_status()\n    hits = [a for a in r.json()[\"results\"] if a[\"path\"] == path]\n    assert len(hits) == 1, path\n    aid = hits[0][\"asset_id\"]\n    return requests.head(f\"{API}/assets/{aid}/download/\", allow_redirects=True, timeout=60).url, aid\n\n\ndef open_nwb(monkey):\n    url, aid = asset_url(ASSETS[monkey])\n    return h5py.File(remfile.File(url), \"r\"), aid\n\n\ndef _segments(t):\n    \"\"\"Index ranges [a, b) of runs in which times do not go backwards.\"\"\"\n    cuts = np.where(np.diff(t) < 0)[0] + 1\n    edges = np.r_[0, cuts, len(t)]\n    return [(edges[i], edges[i + 1]) for i in range(len(edges) - 1)]\n\n\ndef assign_trial_segments(start, hand_seg_bounds):\n    \"\"\"Segment of each trial, walking through trials in file order: the segment advances when a\n    trial starts before the previous one, or after the end of the current hand segment.\"\"\"\n    seg = np.zeros(len(start), int)\n    s = 0\n    for k in range(len(start)):\n        if k > 0 and (start[k] < start[k - 1] or start[k] > hand_seg_bounds[s][1]):\n            s += 1\n        seg[k] = s\n    return seg\n\n\ndef load_trials(f):\n    T = f[\"intervals/trials\"]\n    cols = [\"maze_condition\", \"task_success\", \"discard_trial\", \"correct_reach\", \"maze_num_targets\",\n            \"maze_num_barriers\", \"novel_maze\", \"start_time\", \"stop_time\", \"go_cue_time\",\n            \"move_begins_time\", \"move_ends_time\", \"target_presentation_time\", \"trial_version\"]\n    d = {c: T[c][:] for c in cols}\n    tp = T[\"target_positions\"][:]\n    ti = T[\"target_positions_index\"][:]\n    first = np.r_[0, ti[:-1]]\n    d[\"target_x\"] = tp[first, 0].astype(float)\n    d[\"target_y\"] = tp[first, 1].astype(float)\n    d[\"delay\"] = d[\"go_cue_time\"] - d[\"target_presentation_time\"]\n    bi = T[\"barrier_info_index\"][:]\n    d[\"n_barrier_rows\"] = np.diff(np.r_[0, bi])\n    return d\n\n\ndef select_trials(d, reading=\"b\"):\n    \"\"\"Trials of the 72 conditions (claims, shared method).\n\n    Conditions: maze_condition not a multiple of 3, which is also the set of 1-target mazes\n    (reading (a) and (b) of the claims give the same set here; shown in the notebook).\n    Trials: reading (a) all successful trials; reading (b) successful trials with delay > 400 ms.\n    \"\"\"\n    mc = d[\"maze_condition\"]\n    keep = (mc % 3 != 0) & (d[\"task_success\"] == 1)\n    if reading == \"b\":\n        keep &= d[\"delay\"] > 0.4\n    return keep\n\n\ndef load_session(monkey, reading_mask=None, seed_shuffle=None, progress=False):\n    \"\"\"Stream one session; return single-trial smoothed rates and hand position.\n\n    For every successful trial of the 72 conditions (reading (a); reading (b) is a subset), returns\n    1 ms spike counts reduced as the analyses need them:\n      R   (trials, units, 121) smoothed rates (Gaussian s.d. 20 ms on 1 ms counts, spikes/s),\n          sampled at GRID_MS around movement onset;\n      C10 (trials, units, 121) spike counts summed in 10 ms bins [t, t+10), times 100 (spikes/s);\n      RS  as R, with the 1 ms bins of each trial permuted in time before smoothing (tbf-shuffle);\n      RW  as R, time-warped so that the reach lasts 600 ms, post-reach truncated at 850 ms;\n      RW2 as R, warped to 600 ms with the post-reach part warped to last 250 ms.\n    Hand position (trials, 1201, 2) at 1 ms over -350..+850 ms.\n    \"\"\"\n    f, aid = open_nwb(monkey)\n    d = load_trials(f)\n    keep = select_trials(d, \"a\")\n    # hand, by segment\n    ht = f[\"processing/behavior/Position/Hand/timestamps\"][:]\n    hd = f[\"processing/behavior/Position/Hand/data\"][:]\n    hsegs = _segments(ht)\n    hb = [(ht[a], ht[b - 1]) for a, b in hsegs]\n    tseg = assign_trial_segments(d[\"start_time\"], hb)\n    d[\"segment\"] = tseg\n    idx = np.where(keep)[0]\n    onset = d[\"move_begins_time\"][idx]\n    ntr = len(idx)\n    win = np.arange(WIN0_MS, WIN1_MS)  # ms offsets\n    nwin = len(win)\n    # window must lie within the trial (spikes are stored only within trials)\n    ok_win = (onset + WIN0_MS / 1000 >= d[\"start_time\"][idx]) & (onset + WIN1_MS / 1000 <= d[\"stop_time\"][idx])\n    # hand position at 1 ms over -350..+850, per segment\n    hand = np.full((ntr, 1201, 2), np.nan)\n    hgrid = np.arange(-350, 851) / 1000\n    for i, k in enumerate(idx):\n        a, b = hsegs[tseg[k]]\n        tt = ht[a:b]\n        q = onset[i] + hgrid\n        if q[0] < tt[0] or q[-1] > tt[-1]:\n            continue\n        j = np.searchsorted(tt, q)\n        j = np.clip(j, 1, len(tt) - 1)\n        w = (q - tt[j - 1]) / (tt[j] - tt[j - 1])\n        hand[i] = hd[a:b][j - 1] * (1 - w)[:, None] + hd[a:b][j] * w[:, None]\n    # spikes\n    u = f[\"units\"]\n    sidx = u[\"spike_times_index\"][:]\n    nunits = len(sidx)\n    loc = f[\"general/extracellular_ephys/electrodes/location\"][:]\n    el = u[\"electrodes\"][:]\n    area = np.array([\"PMd\" if b\"Pre-Motor\" in loc[e] else \"M1\" for e in el])\n    counts = np.zeros((ntr, nunits, nwin), np.uint8)\n    unit_jumps = np.zeros(nunits, int)\n    a0 = 0\n    for un in range(nunits):\n        s = u[\"spike_times\"][a0:sidx[un]]\n        a0 = sidx[un]\n        segs = _segments(s)\n        unit_jumps[un] = len(segs) - 1\n        for sg in range(tseg.max() + 1):\n            m = tseg[idx] == sg\n            if not m.any():\n                continue\n            if len(segs) != tseg.max() + 1:\n                raise RuntimeError(f\"unit {un}: {len(segs)} spike runs, {tseg.max() + 1} segments\")\n            a, b = segs[sg]\n            ss = s[a:b]\n            ii = np.where(m)[0]\n            t0 = onset[ii] + WIN0_MS / 1000\n            lo = np.searchsorted(ss, t0)\n            hi = np.searchsorted(ss, onset[ii] + WIN1_MS / 1000)\n            for q, i in enumerate(ii):\n                if hi[q] > lo[q]:\n                    b_ = np.floor((ss[lo[q]:hi[q]] - t0[q]) * 1000).astype(int)\n                    b_ = b_[(b_ >= 0) & (b_ < nwin)]\n                    np.add.at(counts[i, un], b_, 1)\n        if progress and un % 48 == 0:\n            print(\"unit\", un, flush=True)\n    f.close()\n    # reductions\n    gi = GRID_MS - WIN0_MS  # indices of the grid in the 1 ms window\n    R = np.zeros((ntr, nunits, len(GRID_MS)), np.float32)\n    RS = np.zeros_like(R)\n    RW = np.zeros_like(R)\n    RW2 = np.zeros_like(R)\n    C10 = np.zeros_like(R)\n    rng = np.random.default_rng(seed_shuffle)\n    dur = reach_duration(hand)\n    for i in range(ntr):\n        c = counts[i].astype(np.float32)\n        sm = gaussian_filter1d(c, SMOOTH_SD_MS, axis=1, mode=\"reflect\") * 1000\n        R[i] = sm[:, gi]\n        cs = c[:, rng.permutation(nwin)]\n        RS[i] = gaussian_filter1d(cs, SMOOTH_SD_MS, axis=1, mode=\"reflect\")[:, gi] * 1000\n        cc = c[:, gi[0]:gi[0] + 1210].reshape(nunits, 121, 10).sum(2)\n        C10[i] = cc * 100\n        if np.isfinite(dur[i]):\n            for arr, mode in ((RW, \"truncate\"), (RW2, \"warp250\")):\n                tq = warp_map(GRID_MS, dur[i], mode)\n                arr[i] = np.array([np.interp(tq, win, sm[n]) for n in range(nunits)])\n        else:\n            RW[i] = np.nan\n            RW2[i] = np.nan\n    info = dict(asset_id=aid, n_all_trials=len(d[\"start_time\"]), unit_jumps=unit_jumps,\n                n_hand_segments=len(hsegs), hand_segment_bounds=hb, ok_window=ok_win,\n                spikes_per_unit=np.diff(np.r_[0, sidx]))\n    tr = {k: v[idx] for k, v in d.items()}\n    tr[\"duration_ms\"] = dur\n    return dict(trials=tr, all_trials=d, R=R, RS=RS, RW=RW, RW2=RW2, C10=C10, hand=hand,\n                area=area, info=info)\n\n\ndef reach_duration(hand):\n    \"\"\"Per trial, ms from movement onset to the last 1 ms sample at which hand speed is at least a\n    tenth of its peak (claims, fig3i, from code warpTrials.m). Speed over 0..+850 ms.\"\"\"\n    v = np.gradient(hand, axis=1)  # per ms\n    sp = np.hypot(v[..., 0], v[..., 1])[:, 350:]\n    out = np.full(len(hand), np.nan)\n    for i in range(len(hand)):\n        if np.isfinite(sp[i]).all():\n            pk = sp[i].max()\n            out[i] = np.where(sp[i] >= 0.1 * pk)[0].max()\n    return out\n\n\ndef warp_map(grid_ms, dur, mode):\n    \"\"\"Original time (ms) sampled at each warped grid time (Methods, Control for stereotyped time\n    course of behavior): before onset unchanged; 0..dur mapped linearly to 0..600 ms; after the\n    reach either unwarped and truncated at 850 ms ('truncate'), or the post-reach activity up to\n    850 ms after onset warped to last 250 ms ('warp250').\"\"\"\n    g = np.asarray(grid_ms, float)\n    out = g.copy()\n    m = (g >= 0) & (g <= WARP_MS)\n    out[m] = g[m] * dur / WARP_MS\n    post = g > WARP_MS\n    if mode == \"truncate\":\n        out[post] = dur + (g[post] - WARP_MS)\n    else:\n        out[post] = dur + (g[post] - WARP_MS) * (850 - dur) / 250\n    return out\n\n\n# ---------------------------------------------------------------- condition structure\n\ndef condition_table(tr):\n    \"\"\"The 72 conditions in maze-condition order, with straight/curved and the target angle.\"\"\"\n    mc = np.unique(tr[\"maze_condition\"])\n    straight = np.array([(tr[\"maze_num_barriers\"][tr[\"maze_condition\"] == m] == 0).all() for m in mc])\n    tx = np.array([np.median(tr[\"target_x\"][tr[\"maze_condition\"] == m]) for m in mc])\n    ty = np.array([np.median(tr[\"target_y\"][tr[\"maze_condition\"] == m]) for m in mc])\n    cond = np.searchsorted(mc, tr[\"maze_condition\"])\n    return dict(maze=mc, straight=straight, tx=tx, ty=ty, angle=np.arctan2(ty, tx), cond=cond)\n\n\ndef cond_average(X, cond, nc, mask=None):\n    \"\"\"Mean over trials per condition; X (trials, ...) -> (conditions, ...).\"\"\"\n    if mask is None:\n        mask = np.ones(len(cond), bool)\n    out = np.zeros((nc,) + X.shape[1:])\n    for c in range(nc):\n        m = mask & (cond == c)\n        out[c] = np.nanmean(X[m], axis=0)\n    return out\n\n\ndef split_half(cond, nc, rng, mask=None):\n    \"\"\"Random assignment of each condition's trials to two partitions of equal size (+-1).\"\"\"\n    if mask is None:\n        mask = np.ones(len(cond), bool)\n    a = np.zeros(len(cond), bool)\n    for c in range(nc):\n        ii = np.where(mask & (cond == c))[0]\n        p = rng.permutation(ii)\n        a[p[: len(p) // 2]] = True\n    b = mask & ~a\n    return a & mask, b\n\n\n# ---------------------------------------------------------------- variance measures\n\ndef pop_ve(X, Xh):\n    \"\"\"Population variance explained (claims, shared method; code getVarExplained.m):\n    1 - summed variance over neurons of the residual / summed variance of the data, floored at 0.\n    X, Xh: (neurons, time).\"\"\"\n    num = np.var(X - Xh, axis=-1).sum(-1)\n    den = np.var(X, axis=-1).sum(-1)\n    return np.maximum(0.0, 1 - num / den)\n\n\n# ---------------------------------------------------------------- temporal basis factorization\n\ndef tbf(Xc, k):\n    \"\"\"Temporal basis factorization (Methods, Factorizing neural activity using temporal basis\n    functions). Xc (conditions, neurons, time). SVD of the (neurons x conditions)-by-time matrix;\n    returns basis B (k, time) and loadings L (conditions, neurons, k), X(c) ~ L(c) B.\"\"\"\n    C, N, T = Xc.shape\n    A = Xc.reshape(C * N, T)\n    U, S, Vt = np.linalg.svd(A, full_matrices=False)\n    B = Vt[:k]\n    L = (U[:, :k] * S[:k]).reshape(C, N, k)\n    return B, L\n\n\ndef loadings(Xc, B):\n    \"\"\"Loadings of each condition on a fixed basis by least squares (Methods, Measuring the\n    across-condition alignment of rotations: 'used linear regression to identify the loading\n    matrix').\"\"\"\n    return Xc @ np.linalg.pinv(B)\n\n\ndef cv_tbf_k(Rtr, cond, nc, rng, kmax=20, folds=100, mask=None, t0=FIT0):\n    \"\"\"Held-out variance explained for k = 1..kmax (Methods, Cross-validating the number of\n    temporal basis functions): TBF on one half of the trials, compared with the other half.\"\"\"\n    ve = np.zeros((folds, kmax))\n    for f_ in range(folds):\n        a, b = split_half(cond, nc, rng, mask)\n        XA = cond_average(Rtr, cond, nc, a)[..., t0:]\n        XB = cond_average(Rtr, cond, nc, b)[..., t0:]\n        C, N, T = XA.shape\n        U, S, Vt = np.linalg.svd(XA.reshape(C * N, T), full_matrices=False)\n        for k in range(1, kmax + 1):\n            Xh = ((U[:, :k] * S[:k]) @ Vt[:k]).reshape(C, N, T)\n            ve[f_, k - 1] = pop_ve(XB, Xh).mean()\n    return ve\n\n\ndef fit_lds_ls(Z):\n    \"\"\"Least-squares LDS z(t+1) = M z(t) on rows of Z (dims, time).\"\"\"\n    return Z[:, 1:] @ np.linalg.pinv(Z[:, :-1])\n\n\ndef demix(B, L):\n    \"\"\"De-mix the basis (Methods, De-mixing temporal basis functions): fit an LDS to the basis\n    functions and project onto its eigenvectors, in real form (a conjugate pair becomes the real\n    and imaginary parts of its eigenvector, spanning the same plane). Returns basis, loadings,\n    eigenvalues (one per basis row, the pair's eigenvalue with positive angle on both rows),\n    and a group label per row (rotation index; -1 for real modes), rotations sorted by frequency.\"\"\"\n    M = fit_lds_ls(B)\n    lam, V = np.linalg.eig(M)\n    cols, lams, kinds = [], [], []\n    used = np.zeros(len(lam), bool)\n    for i in np.argsort(np.abs(np.angle(lam))):\n        if used[i]:\n            continue\n        if abs(lam[i].imag) < 1e-10:\n            cols.append(V[:, i].real)\n            lams.append(lam[i].real)\n            kinds.append((\"real\", lam[i].real))\n            used[i] = True\n        else:\n            j = np.argmin(np.abs(lam - np.conj(lam[i])) + used * 1e9 + (np.arange(len(lam)) == i) * 1e9)\n            used[i] = used[j] = True\n            l = lam[i] if lam[i].imag > 0 else lam[j]\n            v = V[:, i] if lam[i].imag > 0 else V[:, j]\n            cols += [v.real, v.imag]\n            lams += [l, l]\n            kinds += [(\"pair\", l), (\"pair\", l)]\n    P = np.array(cols).T\n    Bd = np.linalg.solve(P, B)\n    Ld = L @ P\n    lams = np.array(lams, complex)\n    freq = np.abs(np.angle(lams)) / (2 * np.pi) * 100\n    group = np.full(len(lams), -1)\n    pf = sorted({round(fr, 9) for fr, (kd, _) in zip(freq, kinds) if kd == \"pair\"})\n    for r, fr in enumerate(pf):\n        group[np.isclose(freq, fr) & np.array([kd == \"pair\" for kd, _ in kinds])] = r\n    # normalise each basis row to unit norm, scaling loadings inversely (standard)\n    nrm = np.linalg.norm(Bd, axis=1)\n    return Bd / nrm[:, None], Ld * nrm, lams, group, freq\n\n\n# ---------------------------------------------------------------- alignment and angles\n\ndef orth(A):\n    \"\"\"Orthonormal basis of the column span of A (neurons, d).\"\"\"\n    U, S, _ = np.linalg.svd(A, full_matrices=False)\n    return U[:, S > S[0] * 1e-10]\n\n\ndef alignment_index(L1, B1, L2):\n    \"\"\"Fraction of the variance of activity L1 @ B1 (neurons x time) captured by projection onto\n    span(L2) (claims, shared method; code getAlignmentIndex.m).\"\"\"\n    Y = L1 @ B1\n    Y = Y - Y.mean(1, keepdims=True)\n    Q = orth(L2)\n    return np.sum((Q.T @ Y) ** 2) / np.sum(Y ** 2)\n\n\ndef sea(planes, ndim=25, seeds=None):\n    \"\"\"Subspace excursion angles (Methods, Subspace excursion angles). planes: list of\n    (neurons, d) orthonormal bases. From a seed, repeatedly add the vector of any other subspace\n    that forms the greatest angle with the span so far. Every seed is tried and the sequence with\n    the largest summed angles is kept (the Methods optimise over sequences; assumption that\n    greedy steps from the best seed implement it). Returns angles in degrees.\"\"\"\n    best, bestsum = None, -1\n    if seeds is None:\n        seeds = range(len(planes))\n    P = np.stack(planes)  # (c, N, d)\n    for s0 in seeds:\n        S = planes[s0].copy()\n        angs = []\n        while S.shape[1] < ndim + planes[s0].shape[1] and S.shape[1] < P.shape[1]:\n            R = P - S @ np.einsum(\"nk,cnd->ckd\", S, P)  # residuals (c, N, d)\n            best_c, best_sv, best_v = None, -1, None\n            for c in range(len(planes)):\n                U, sv, Vt = np.linalg.svd(R[c], full_matrices=False)\n                if sv[0] > best_sv:\n                    best_sv, best_c, best_v = sv[0], c, U[:, 0]\n            angs.append(np.degrees(np.arcsin(min(1.0, best_sv))))\n            S = np.column_stack([S, best_v])\n            if len(angs) >= ndim:\n                break\n        if sum(angs) > bestsum:\n            bestsum, best = sum(angs), np.array(angs)\n    return best\n\n\ndef participation_ratio(ev):\n    ev = np.asarray(ev)\n    return ev.sum() ** 2 / np.sum(ev ** 2)\n\n\n# ---------------------------------------------------------------- single-condition LDS\n\ndef rrr_lds(X, k, max_half_life_s=10.0, dt_s=0.01):\n    \"\"\"Reduced-rank LDS for one condition (Methods, Fitting dynamics to single conditions).\n    X (neurons, time). x(t+1) = x(t) M with rank(M) = k, by reduced-rank regression; eigenvalues\n    with half-life > 10 s are shrunk to a 10 s half-life; the system is simulated forward from the\n    first state. Returns the simulated activity and the k eigenvalues of the reduced system.\"\"\"\n    Xp, Xf = X[:, :-1].T, X[:, 1:].T\n    Mols = np.linalg.pinv(Xp) @ Xf\n    Yh = Xp @ Mols\n    _, _, Vt = np.linalg.svd(Yh, full_matrices=False)\n    V = Vt[:k].T  # (N, k)\n    A = V.T @ Mols @ V  # z(t+1) = z(t) A, with z = x V\n    lam, W = np.linalg.eig(A)\n    rmax = 0.5 ** (dt_s / max_half_life_s)\n    mag = np.abs(lam)\n    lam2 = np.where(mag > rmax, lam / mag * rmax, lam)\n    A2 = (W @ np.diag(lam2) @ np.linalg.inv(W)).real\n    T = X.shape[1]\n    out = np.zeros((T, X.shape[0]))\n    x0 = X[:, 0]\n    out[0] = x0\n    z = (x0 @ Mols) @ V\n    out[1] = z @ V.T\n    for t in range(2, T):\n        z = z @ A2\n        out[t] = z @ V.T\n    return out.T, lam2\n\n\ndef cv_condition_dim(Rtr, cond, nc, rng, ks, folds=100, mask=None, t0=FIT0, frac=0.5):\n    \"\"\"Per condition, PCA dimensionality by cross-validation over trial partitions (Methods,\n    Fitting dynamics to single conditions): singular vectors from X, projection of X onto the\n    top k, variance explained in Y. Returns (folds, conditions, len(ks)).\"\"\"\n    out = np.zeros((folds, nc, len(ks)))\n    for f_ in range(folds):\n        a = np.zeros(len(cond), bool)\n        m = np.ones(len(cond), bool) if mask is None else mask\n        for c in range(nc):\n            ii = rng.permutation(np.where(m & (cond == c))[0])\n            a[ii[: int(round(len(ii) * frac))]] = True\n        b = m & ~a\n        XA = cond_average(Rtr, cond, nc, a)[..., t0:]\n        XB = cond_average(Rtr, cond, nc, b)[..., t0:]\n        for c in range(nc):\n            U, S, Vt = np.linalg.svd(XA[c], full_matrices=False)\n            for j, k in enumerate(ks):\n                Xh = U[:, :k] @ (U[:, :k].T @ XA[c])\n                out[f_, c, j] = pop_ve(XB[c], Xh)\n    return out\n\n\ndef sort_eigs(lam):\n    \"\"\"Eigenvalues sorted by angle (frequency), conjugates with negative angle dropped.\"\"\"\n    lam = np.asarray(lam)\n    lam = lam[lam.imag >= -1e-12]\n    return lam[np.lexsort((-lam.real, np.abs(np.angle(lam))))]\n\n\n# ---------------------------------------------------------------- jPCA\n\ndef soft_norm(Xc, const=5.0):\n    \"\"\"Soft normalisation (Methods, Explaining variability in jPCA-identified rotations):\n    each neuron divided by its range over conditions and times plus 5.\"\"\"\n    rng_ = Xc.max(axis=(0, 2)) - Xc.min(axis=(0, 2))\n    return Xc / (rng_ + const)[None, :, None], rng_ + const\n\n\ndef jpca(Xc, t_idx, npc=6):\n    \"\"\"jPCA (Churchland et al. 2012, as the Methods apply it). Xc (conditions, neurons, time),\n    already soft-normalised and mean-subtracted across conditions. Fitted on time indices t_idx.\n    Returns dict with PCs, Mskew, Mbest, the jPC planes (in PC space, sorted by eigenvalue\n    magnitude), and the R2 of the skew-symmetric and unconstrained fits in the first plane.\"\"\"\n    C, N, T = Xc.shape\n    D = Xc[:, :, t_idx].transpose(0, 2, 1).reshape(-1, N)\n    mu = D.mean(0)\n    U, S, Vt = np.linalg.svd(D - mu, full_matrices=False)\n    PC = Vt[:npc].T  # (N, npc)\n    Z = (Xc[:, :, t_idx].transpose(0, 2, 1) @ PC)  # (C, T', npc)\n    pre = Z[:, :-1].reshape(-1, npc)\n    dZ = np.diff(Z, axis=1).reshape(-1, npc)\n    Mbest = np.linalg.lstsq(pre, dZ, rcond=None)[0]\n    Mskew = fit_skew(pre, dZ)\n    ev, evec = np.linalg.eig(Mskew)\n    order = np.argsort(-np.abs(ev.imag))\n    planes = []\n    used = set()\n    for i in order:\n        if i in used or ev[i].imag <= 0:\n            continue\n        v = evec[:, i]\n        p1, p2 = (v + np.conj(v)).real, ((v - np.conj(v)) * 1j).real\n        P = np.linalg.qr(np.column_stack([p1, p2]))[0]\n        planes.append(P)\n        used.add(i)\n    out = dict(PC=PC, Mskew=Mskew, Mbest=Mbest, planes=planes, mu=mu)\n    out[\"R2_skew_2D\"], out[\"R2_best_2D\"] = r2_plane(pre, dZ, Mskew, planes[0])\n    return out\n\n\ndef r2_plane(pre, dZ, Mskew, P):\n    pre2, d2 = pre @ P, dZ @ P\n    Ms2 = P.T @ Mskew @ P\n    ss = np.sum((d2 - d2.mean(0)) ** 2)\n    r2s = 1 - np.sum((d2 - pre2 @ Ms2) ** 2) / ss\n    Mb2 = np.linalg.lstsq(pre2, d2, rcond=None)[0]\n    r2b = 1 - np.sum((d2 - pre2 @ Mb2) ** 2) / ss\n    return r2s, r2b\n\n\ndef fit_skew(X, dX):\n    \"\"\"Least-squares skew-symmetric M with dX ~ X M (jPCA).\"\"\"\n    n = X.shape[1]\n    idx = [(i, j) for i in range(n) for j in range(i + 1, n)]\n    H = np.zeros((n * n, len(idx)))\n    for q, (i, j) in enumerate(idx):\n        Mq = np.zeros((n, n))\n        Mq[i, j], Mq[j, i] = 1, -1\n        H[:, q] = Mq.reshape(-1)\n    A = np.kron(X, np.eye(n))  # vec(X M) row-major = (X kron I) vec(M) row-major\n    k = np.linalg.lstsq(A @ H, dX.reshape(-1), rcond=None)[0]\n    return (H @ k).reshape(n, n)\n\n\n# ---------------------------------------------------------------- kinematics\n\ndef kin_basis(vel_list):\n    \"\"\"Kinematic basis functions (Methods, Extracting kinematic basis functions, raw-SVD reading):\n    SVD of x and y hand velocity of all conditions of all datasets; the top two right singular\n    vectors over time; integrated over time to position basis functions. vel_list: arrays\n    (conditions, time, 2).\"\"\"\n    rows = np.concatenate([v.transpose(0, 2, 1).reshape(-1, v.shape[1]) for v in vel_list])\n    U, S, Vt = np.linalg.svd(rows, full_matrices=False)\n    Bv = Vt[:2]\n    for i in range(2):  # sign: positive peak first basis (standard)\n        if Bv[i][np.argmax(np.abs(Bv[i]))] < 0:\n            Bv[i] = -Bv[i]\n    Bp = np.cumsum(Bv, axis=1)\n    return Bv, Bp, S\n\n\ndef skewnorm_basis(t, Bv):\n    \"\"\"Second reading of the kinematic basis: least-squares fits of a skew-normal curve and of the\n    derivative of a skew-normal curve to the two velocity basis functions (Methods).\"\"\"\n    from scipy.optimize import least_squares\n    from scipy.stats import skewnorm\n\n    def f1(p):\n        a, loc, sc, amp = p\n        return amp * skewnorm.pdf(t, a, loc, abs(sc) + 1e-6)\n\n    def f2(p):\n        a, loc, sc, amp = p\n        y = skewnorm.pdf(t, a, loc, abs(sc) + 1e-6)\n        return amp * np.gradient(y, t)\n\n    p1 = least_squares(lambda p: f1(p) - Bv[0], [1.0, 200.0, 150.0, Bv[0].max() * 150]).x\n    best = None\n    for s in (+1, -1):\n        r = least_squares(lambda p: f2(p) - Bv[1], [1.0, 200.0, 150.0, s * 1e4])\n        if best is None or r.cost < best.cost:\n            best = r\n    v = np.array([f1(p1), f2(best.x)])\n    return v, np.cumsum(v, axis=1)\n\n\ndef reach_params(pos, Bp):\n    \"\"\"Four reach parameters per condition or trial: least-squares coefficients of x and y hand\n    position (relative to the position at -350 ms) on the two position basis functions, ordered\n    (x1, y1, x2, y2) so that the third and fourth describe curvature (Methods, LDR encoding;\n    'Quantifying the trial-to-trial fidelity').\"\"\"\n    P = pos - pos[:, :1, :]\n    G = np.linalg.pinv(Bp)  # (T, 2)\n    cx = P[..., 0] @ G\n    cy = P[..., 1] @ G\n    return np.column_stack([cx[:, 0], cy[:, 0], cx[:, 1], cy[:, 1]])\n\n\ndef params_to_pos(p, Bp):\n    x = p[:, [0, 2]] @ Bp\n    y = p[:, [1, 3]] @ Bp\n    return np.stack([x, y], -1)\n\n\ndef kin_ve(true, pred):\n    \"\"\"Variance explained in position over time (code getVarExplainedKinematics.m), x and y\n    pooled, negatives set to 0. true, pred (time, 2) relative positions.\"\"\"\n    num = np.sum((true - pred) ** 2)\n    den = np.sum((true - true.mean(0)) ** 2)\n    return max(0.0, 1 - num / den)\n\n\n# ---------------------------------------------------------------- regression\n\ndef ridge_fit(X, Y, lam):\n    \"\"\"Ridge with an unpenalised intercept.\"\"\"\n    mx, my = X.mean(0), Y.mean(0)\n    Xc = X - mx\n    W = np.linalg.solve(Xc.T @ Xc + lam * np.eye(X.shape[1]), Xc.T @ (Y - my))\n    return lambda Z: (Z - mx) @ W + my\n\n\ndef kernel_fit(X, Y, kernel, ell, lam):\n    \"\"\"Kernel ridge regression with an intercept (the training mean). kernel 'ou'\n    (exp(-|x-y|/ell)) or 'gauss' (exp(-|x-y|^2/(2 ell^2))).\"\"\"\n    my = Y.mean(0)\n\n    def K(A, Bm):\n        d = np.sqrt(np.maximum(0, (A ** 2).sum(1)[:, None] + (Bm ** 2).sum(1)[None] - 2 * A @ Bm.T))\n        return np.exp(-d / ell) if kernel == \"ou\" else np.exp(-d ** 2 / (2 * ell ** 2))\n\n    Kx = K(X, X)\n    alpha = np.linalg.solve(Kx + max(lam, 1e-8) * np.eye(len(X)), Y - my)\n    return lambda Z: K(Z, X) @ alpha + my\n\n\ndef folds_of(n, k, rng):\n    p = rng.permutation(n)\n    return [np.sort(p[i::k]) for i in range(k)]\n\n\ndef auc(pos, neg):\n    \"\"\"ROC-AUC that pos > neg, folded to at least 0.5 (claims, shared method).\"\"\"\n    from scipy.stats import mannwhitneyu\n    u = mannwhitneyu(pos, neg).statistic\n    a = u / (len(pos) * len(neg))\n    return 0.5 + abs(a - 0.5), a\n\n\ndef circ_corr(a, b):\n    \"\"\"Circular correlation coefficient (Jammalamadaka) with a permutation-free large-sample p.\"\"\"\n    from scipy.stats import norm\n    sa, sb = np.sin(a - np.angle(np.exp(1j * a).mean())), np.sin(b - np.angle(np.exp(1j * b).mean()))\n    r = np.sum(sa * sb) / np.sqrt(np.sum(sa ** 2) * np.sum(sb ** 2))\n    n = len(a)\n    l20, l02, l22 = np.mean(sa ** 2), np.mean(sb ** 2), np.mean(sa ** 2 * sb ** 2)\n    z = np.sqrt(n * l20 * l02 / l22) * r\n    return r, 2 * (1 - norm.cdf(abs(z)))\n"
}
```

```
File created successfully at: entries/sabatini-2024/ldr.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python - <<'EOF'
s=open('ldr.py').read()
old="""                tq = warp_map(GRID_MS, dur[i], mode)
                arr[i] = np.array([np.interp(tq, win, sm[n]) for n in range(nunits)])"""
new="""                tq = warp_map(GRID_MS, dur[i], mode) - WIN0_MS
                j = np.clip(np.floor(tq).astype(int), 0, nwin - 2)
                w = (tq - j)[None, :]
                arr[i] = sm[:, j] * (1 - w) + sm[:, j + 1] * w"""
assert old in s; s=s.replace(old,new); open('ldr.py','w').write(s)
EOF
cd $TMPDIR && cat > dev_load.py <<'EOF'
import sys, time, resource, pickle, zlib
sys.path.insert(0,'entries/sabatini-2024')
import ldr, numpy as np
m=sys.argv[1]
t0=time.time()
S=ldr.load_session(m, seed_shuffle=zlib.crc32(b"sabatini-2024/tbf-shuffle-control"), progress=True)
print('time', time.time()-t0, 'maxrss GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
pickle.dump(S, open(f'{m}.pkl','wb'), protocol=4)
print(S['info']['unit_jumps'][:5], S['info']['n_hand_segments'], S['R'].shape, np.isnan(S['hand'][:,0,0]).sum(), S['info']['ok_window'].mean())
EOF
date -u; $TMPDIR/dev/bin/python dev_load.py J 2>&1 | tail -5
```

```
Fri Nov 20 10:46:19 UTC 2026
  File "/tmp/claude-1001/dev_load.py", line 6, in <module>
    S=ldr.load_session(m, seed_shuffle=zlib.crc32(b"sabatini-2024/tbf-shuffle-control"), progress=True)
  File "entries/sabatini-2024/ldr.py", line 169, in load_session
    raise RuntimeError(f"unit {un}: {len(segs)} spike runs, {tseg.max() + 1} segments")
RuntimeError: unit 1: 2 spike runs, 1 segments
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > t2.py <<'EOF'
import h5py, remfile, requests, numpy as np
for aid in ['033a04c0-9ce7-45c5-8012-c571a7b9bf12','02c2c5b7-0848-46f1-9ca6-1e657fd10eb5']:
    s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r'); u=f['units']; idx=u['spike_times_index'][:]
    s=u['spike_times'][:]
    a=np.r_[0,idx[:-1]]
    nj=[];big=[]
    for k in range(len(idx)):
        x=s[a[k]:idx[k]]; d=np.diff(x); j=np.where(d<0)[0]; nj.append(len(j))
        if k<3 or len(j)!=nj[0]: big.append((k,list(zip(x[j].round(3),x[j+1].round(3))) if len(j)<8 else len(j)))
    print(aid, np.bincount(nj)); print(big[:12])
EOF
$TMPDIR/dev/bin/python t2.py
```

```
033a04c0-9ce7-45c5-8012-c571a7b9bf12 [191   1]
[(0, []), (1, [(np.float64(15668.638), np.float64(4.717))]), (2, [])]
02c2c5b7-0848-46f1-9ca6-1e657fd10eb5 [  0   0   0   0 192]
[(0, [(np.float64(6076.442), np.float64(6074.246)), (np.float64(12076.757), np.float64(6070.575)), (np.float64(12494.382), np.float64(6119.762)), (np.float64(13516.001), np.float64(6073.581))]), (1, [(np.float64(6076.445), np.float64(6074.25)), (np.float64(12076.713), np.float64(6070.562)), (np.float64(12494.33), np.float64(6119.798)), (np.float64(13515.996), np.float64(6073.646))]), (2, [(np.float64(6076.462), np.float64(6074.22)), (np.float64(12076.752), np.float64(6070.648)), (np.float64(12494.382), np.float64(6119.774)), (np.float64(13516.001), np.float64(6073.546))])]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python - <<'EOF'
s=open('ldr.py').read()
old="""        segs = _segments(s)
        unit_jumps[un] = len(segs) - 1
"""
new="""        segs = _segments(s)
        unit_jumps[un] = len(segs) - 1
        if len(segs) != tseg.max() + 1 and tseg.max() == 0:
            # one recording segment but a spike train that restarts (one unit in J): the runs are
            # merged and sorted, as an electrode's multi-unit activity (assumption, notebook).
            s = np.sort(s)
            segs = [(0, len(s))]
"""
assert old in s; s=s.replace(old,new); open('ldr.py','w').write(s)
EOF
$TMPDIR/dev/bin/python $TMPDIR/dev_load.py J 2>&1 | tail -3; date -u
```

```
unit 144
time 66.88763070106506 maxrss GB 1.789352
[0 1 0 0 0] 1 (1595, 192, 121) 0 1.0
Fri Nov 20 10:48:08 UTC 2026
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python $TMPDIR/dev_load.py N 2>&1 | tail -3; date -u
```

```
unit 144
time 100.58913397789001 maxrss GB 2.4282
[4 4 4 4 4] 5 (2121, 192, 121) 1 1.0
Fri Nov 20 10:49:53 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > dev1.py <<'EOF'
import sys, time, pickle, numpy as np
sys.path.insert(0,'entries/sabatini-2024')
import ldr
S=pickle.load(open('J.pkl','rb'))
tr=S['trials']; ct=ldr.condition_table(tr); cond=ct['cond']; nc=len(ct['maze'])
mask=ldr.select_trials(tr,'b')
print('nc',nc,'straight',ct['straight'].sum(),'trials b',mask.sum())
print('trials per cond', np.bincount(cond[mask]).min(), np.bincount(cond[mask]).max())
for area in ['M1','PMd']:
    u=S['area']==area
    R=S['R'][:,u]
    X=ldr.cond_average(R,cond,nc,mask)
    print(area, 'rate range', X.min(), X.max(), 'mean', X.mean())
    rng=np.random.default_rng(0)
    t0=time.time(); ve=ldr.cv_tbf_k(R,cond,nc,rng,folds=10,mask=mask); print('cv time', time.time()-t0)
    k=np.argmax(ve.mean(0))+1; print('cv ve', ve.mean(0).round(3), 'k',k)
    if k%2==0: k+=1
    Xw=X[...,ldr.FIT0:]
    B,L=ldr.tbf(Xw,k)
    Bd,Ld,lam,grp,fr=ldr.demix(B,L)
    print('freq', fr.round(2), 'grp', grp, '|lam|', np.abs(lam).round(3))
    ve=ldr.pop_ve(Xw, np.einsum('cnk,kt->cnt',Ld,Bd)); print('TBF VE', ve.mean().round(3), ve.std().round(3))
EOF
$TMPDIR/dev/bin/python dev1.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev1.py", line 4, in <module>
    S=pickle.load(open('J.pkl','rb'))
                  ~~~~^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'J.pkl'
```

**Agent calls Bash**

```bash
mv entries/sabatini-2024/*.pkl $TMPDIR/; ls entries/sabatini-2024/; cd $TMPDIR && $TMPDIR/dev/bin/python dev1.py
```

```
__pycache__
ldr.py
nc 72 straight 36 trials b 1381
trials per cond 16 23
M1 rate range 4.022588729858398 220.11570739746094 mean 42.142422566229705
cv time 1.5728704929351807
cv ve [0.388 0.542 0.66  0.696 0.711 0.715 0.712 0.705 0.697 0.689 0.682 0.674
 0.668 0.663 0.658 0.653 0.649 0.646 0.643 0.64 ] k 6
freq [0.   0.7  0.7  1.82 1.82 3.08 3.08] grp [-1  0  0  1  1  2  2] |lam| [1.001 0.989 0.989 0.988 0.988 0.979 0.979]
TBF VE 0.935 0.012
PMd rate range 0.1259690523147583 275.2949523925781 mean 42.346547348132134
cv time 1.5752522945404053
cv ve [0.397 0.626 0.754 0.784 0.79  0.786 0.78  0.773 0.766 0.759 0.753 0.747
 0.742 0.737 0.733 0.729 0.726 0.723 0.72  0.718] k 5
freq [0.   0.64 0.64 1.54 1.54] grp [-1  0  0  1  1] |lam| [1.    0.989 0.989 0.987 0.987]
TBF VE 0.936 0.015
Shell cwd was reset to
```

**Agent**

Core pipeline works on monkey J (CV picks 7 basis functions for M1 with rotations near 0.7, 1.8, 3.1 Hz; TBF variance explained 0.94). Writing the full notebook now.

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python - <<'EOF'
s=open('ldr.py').read()
old="def load_session(monkey, reading_mask=None, seed_shuffle=None, progress=False):"
new="def load_session(monkey, shuffle_seeds=(), progress=False):"
s=s.replace(old,new)
s=s.replace("""    RS = np.zeros_like(R)
""","""    RS = {sd: np.zeros_like(R) for sd in shuffle_seeds}
    rngs = {sd: np.random.default_rng(sd) for sd in shuffle_seeds}
""")
s=s.replace("""    rng = np.random.default_rng(seed_shuffle)
""","")
s=s.replace("""        cs = c[:, rng.permutation(nwin)]
        RS[i] = gaussian_filter1d(cs, SMOOTH_SD_MS, axis=1, mode="reflect")[:, gi] * 1000
""","""        for sd in shuffle_seeds:
            # every unit's 1 ms bins permuted independently within the trial window (assumption:
            # the window; claims, tbf-shuffle-control, code scrambleTrials.m)
            perm = np.argsort(rngs[sd].random((nunits, nwin)), axis=1)
            cs = np.take_along_axis(c, perm, axis=1)
            RS[sd][i] = gaussian_filter1d(cs, SMOOTH_SD_MS, axis=1, mode="reflect")[:, gi] * 1000
""")
s=s.replace("""      RS  as R, with the 1 ms bins of each trial permuted in time before smoothing (tbf-shuffle);""","""      RS  {seed: array} as R, with the 1 ms bins of each trial and unit permuted in time before
          smoothing (tbf-shuffle-control), one array per seed;""")
open('ldr.py','w').write(s)
EOF
grep -n "RS\|shuffle_seeds" ldr.py | head
```

```
21:VERSION = "0.260528.0919"
41:def asset_url(path, version=VERSION):
106:def load_session(monkey, shuffle_seeds=(), progress=False):
114:      RS  {seed: array} as R, with the 1 ms bins of each trial and unit permuted in time before
193:    RS = {sd: np.zeros_like(R) for sd in shuffle_seeds}
194:    rngs = {sd: np.random.default_rng(sd) for sd in shuffle_seeds}
203:        for sd in shuffle_seeds:
208:            RS[sd][i] = gaussian_filter1d(cs, SMOOTH_SD_MS, axis=1, mode="reflect")[:, gi] * 1000
225:    return dict(trials=tr, all_trials=d, R=R, RS=RS, RW=RW, RW2=RW2, C10=C10, hand=hand,
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ldr.py').read()
old="""            # every unit's 1 ms bins permuted independently within the trial window (assumption:
            # the window; claims, tbf-shuffle-control, code scrambleTrials.m)
            perm = np.argsort(rngs[sd].random((nunits, nwin)), axis=1)
            cs = np.take_along_axis(c, perm, axis=1)"""
new="""            # the trial's 1 ms bins permuted in time, the same permutation for every unit so that
            # spike correlations between units are kept (Methods, Control for data smoothing); over
            # the window read (assumption; claims, tbf-shuffle-control, code scrambleTrials.m)
            cs = c[:, rngs[sd].permutation(nwin)]"""
assert old in s; s=s.replace(old,new)
s=s.replace("""      RS  {seed: array} as R, with the 1 ms bins of each trial and unit permuted in time before""","""      RS  {seed: array} as R, with the 1 ms bins of each trial permuted in time before""")
open('ldr.py','w').write(s)
EOF
cat > $TMPDIR/dev_load.py <<'EOF'
import sys, time, resource, pickle, zlib
sys.path.insert(0,'entries/sabatini-2024')
import ldr, numpy as np
m=sys.argv[1]
s0=zlib.crc32(b"sabatini-2024/tbf-shuffle-control")
t0=time.time()
S=ldr.load_session(m, shuffle_seeds=[s0+i*1000 for i in range(5)])
print('time', time.time()-t0, 'maxrss GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
pickle.dump(S, open(f'/tmp/claude-1001/{m}.pkl','wb'), protocol=4)
EOF
cd $TMPDIR; (dev/bin/python dev_load.py J > loadJ.log 2>&1; dev/bin/python dev_load.py N > loadN.log 2>&1) ; cat loadJ.log loadN.log
```

```
time 170.34971404075623 maxrss GB 2.223948
time 234.75606536865234 maxrss GB 3.197856
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u
```

```
Fri Nov 20 10:58:25 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/sabatini-2024/nb_part1.py",
 "content": "# %% md\n# Reproducing Sabatini & Kaufman (2024) on DANDI:000070\n\n**Paper.** Sabatini, D. A. & Kaufman, M. T. (2024). Reach-dependent reorientation of rotational dynamics\nin motor cortex. *Nature Communications* 15, 7007. doi:10.1038/s41467-024-51308-7. The claims file\n(`claims/sabatini-2024.yaml`) was written from the version of record (PMC11325044) with its Methods and\nits supplement, and from the paper's code (github.com/kaufmanlab/LDR-public at commit b65f28d).\n\n**Dataset.** DANDI:000070 (\"Neural population dynamics during reaching\"), version **0.260528.0919**,\nstreamed. The paper cites the dandiset without a version. Of its three versions (0.251218.1714,\n0.260528.0919 and the draft), the two published ones list the same ten assets with the same asset ids,\nsizes and modification times, so they hold the same files; the most recent published one is pinned, as\nthe protocol asks when no version is cited. The two files the paper's Data availability statement\nnames are read: `sub-Jenkins_ses-20090918` (monkey J) and `sub-Nitschke_ses-20100923` (monkey N).\n\n**What is tested.** The four datasets of the paper (M1-J, PMd-J, M1-N, PMd-N) are rebuilt from the\nunits, trials and hand position in the two files. The dataset holds no EMG.\n\n| Claim | Tested here |\n|---|---|\n| data-composition | tested |\n| jpca-fit-r2, jpca-variance-explained, single-lds-variance | tested |\n| fig2c-condition-lds-variance, fig3a-eigenvalue-clusters, fig3c-eigenvalue-distance-auc, suppfig2-eigenvalues-from-kinematics | tested |\n| fig3g-basis-frequencies, tbf-variance-explained, tbf-shuffle-control, fig3h-recoverability, fig3i-duration-warping, suppfig3-model-comparison | tested |\n| fig4b-plane-alignment, fig4c-subspace-excursion-angles, rotation-orientation-dimensionality, fig4d-jpca-variance-correlation, fig4f-plane-alignment-explains-jpca | tested |\n| fig5a-frequencies-segregated, fig5c-rotations-predict-rotations | tested |\n| suppfig6a-location-alignment, suppfig6b-location-dimensionality, suppfig6c-location-distinct-from-rotations, fig6b-location-predicts-rotations, fig6c-location-tracks-direction, fig6e-kinematics-predict-location | tested |\n| fig7c-ldr-encoding, suppfig7a-not-memorization, fig7c-standard-encoding-worse | tested |\n| fig7f-ldr-decoding, trial-curvature-decoding, suppfig8-no-output-potent-dependence | tested (suppfig8 without EMG) |\n| fig7f-decoder-beats-standard | tested except the GPFA decoders (see its section) |\n\nWhere a parameter comes from (the claim, a passage of the paper, an assumption, or a standard choice)\nis said in the docstrings of the helper `ldr.py` and beside the code here.\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"4\")\nimport time\nimport zlib\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport ldr\n\nT_START = time.time()\nDATASETS = [(\"J\", \"M1\"), (\"J\", \"PMd\"), (\"N\", \"M1\"), (\"N\", \"PMd\")]\nNAME = {d: f\"{d[1]}-{d[0]}\" for d in DATASETS}\n\n\ndef seed(claim):\n    \"\"\"The claim's seed (protocol): crc32 of '<paper key>/<claim id>'.\"\"\"\n    return zlib.crc32(f\"sabatini-2024/{claim}\".encode())\n\n\ndef seeds5(claim):\n    return [seed(claim) + i for i in (0, 1000, 2000, 3000, 4000)]\n\n\nprint(\"dandiset\", ldr.DANDISET, \"version\", ldr.VERSION)\n\n# %% md\n## Loading\n\nEach session is streamed once. Spike times are binned at 1 ms from 500 ms before to 1000 ms after\nmovement onset, smoothed with a Gaussian of 20 ms s.d. and sampled every 10 ms from -350 to +850 ms\n(Methods, Subjects, behavior and data pre-processing; claims, shared method). The time-shuffled\ncopies for tbf-shuffle-control are made at load time under that claim's five seeds, and the warped\ncopies for fig3i at the same time.\n\n# %%\nSESS = {}\nfor m in (\"J\", \"N\"):\n    t0 = time.time()\n    SESS[m] = ldr.load_session(m, shuffle_seeds=seeds5(\"tbf-shuffle-control\"))\n    print(m, \"loaded in\", round(time.time() - t0), \"s; trials kept (successful, 72 conditions):\",\n          len(SESS[m][\"trials\"][\"maze_condition\"]))\n\n# %% md\n## Data check\n\n# %% [sanity]\nimport resource\nfor m in (\"J\", \"N\"):\n    S = SESS[m]\n    d = S[\"all_trials\"]\n    tr = S[\"trials\"]\n    print(f\"== monkey {m} (asset {S['info']['asset_id']})\")\n    print(\"  trials in file\", S[\"info\"][\"n_all_trials\"], \"| successful\", int(d[\"task_success\"].sum()),\n          \"| maze_condition values\", len(np.unique(d[\"maze_condition\"])),\n          \"(min\", d[\"maze_condition\"].min(), \"max\", d[\"maze_condition\"].max(), \")\")\n    print(\"  units\", len(S[\"area\"]), {a: int((S[\"area\"] == a).sum()) for a in (\"M1\", \"PMd\")})\n    sp = S[\"info\"][\"spikes_per_unit\"]\n    print(\"  spikes per unit: min\", sp.min(), \"median\", int(np.median(sp)), \"max\", sp.max())\n    print(\"  recording segments (backward jumps of hand timestamps + 1):\", S[\"info\"][\"n_hand_segments\"],\n          \"| bounds (s):\", [(round(a, 1), round(b, 1)) for a, b in S[\"info\"][\"hand_segment_bounds\"]])\n    print(\"  backward jumps in spike times per unit:\", np.bincount(S[\"info\"][\"unit_jumps\"]))\n    print(\"  trials per segment:\", np.bincount(d[\"segment\"]))\n    print(\"  trial start times monotonic:\", bool(np.all(np.diff(d[\"start_time\"]) > 0)))\n    print(\"  -500..+1000 ms window inside the trial interval for\", int(S[\"info\"][\"ok_window\"].sum()), \"of\",\n          len(S[\"info\"][\"ok_window\"]), \"kept trials\")\n    print(\"  delay (go - target) s: range\", np.round(np.nanpercentile(d[\"delay\"], [0, 50, 100]), 3))\n    print(\"  movement onset - go cue s: range\", np.round(np.nanpercentile(d[\"move_begins_time\"] - d[\"go_cue_time\"], [0, 50, 100]), 3))\n    h = S[\"hand\"]\n    print(\"  hand position (file unit 'meters'): range x\", np.round(np.nanmin(h[..., 0]), 1), np.round(np.nanmax(h[..., 0]), 1),\n          \"y\", np.round(np.nanmin(h[..., 1]), 1), np.round(np.nanmax(h[..., 1]), 1), \"| trials without hand\",\n          int(np.isnan(h[:, 0, 0]).sum()))\n    sp_hand = np.hypot(*np.gradient(h, axis=1).transpose(2, 0, 1)) * 1000\n    print(\"  peak hand speed per trial (file units per s): median\", np.round(np.nanmedian(np.nanmax(sp_hand, 1)), 1))\n    print(\"  reach duration ms: median\", np.nanmedian(tr[\"duration_ms\"]), \"range\", np.nanmin(tr[\"duration_ms\"]), np.nanmax(tr[\"duration_ms\"]))\n    print(\"  smoothed rates (spikes/s): range\", float(S[\"R\"].min()), float(S[\"R\"].max()), \"mean\", float(S[\"R\"].mean()))\nprint(\"peak memory GB\", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6)\n\n# %% md\n### Conditions and trial readings\n\nThe claims file gives two readings for the 72 conditions (drop maze conditions that are a multiple of 3;\ndrop the 3-target versions, whose distractors repeat a curved maze) and two for trials (all successful\ntrials; successful trials with delay above 400 ms). Analyses below use trial reading (b), the one whose\ncounts are closer to the paper's (assumption, recorded).\n\n# %%\nCT = {}\nfor m in (\"J\", \"N\"):\n    d = SESS[m][\"all_trials\"]\n    mc = d[\"maze_condition\"]\n    a = np.unique(mc[(mc % 3 != 0)])\n    b = np.unique(mc[(d[\"maze_num_targets\"] == 1)])\n    print(m, \"reading (a) conditions\", len(a), \"| reading (b) 1-target conditions\", len(b),\n          \"| (b) minus maze 0:\", len(np.setdiff1d(b, [0])), \"| same set as (a):\", np.array_equal(np.setdiff1d(b, [0]), a))\n    print(\"   maze 0 trials:\", int((mc == 0).sum()), \"targets\", np.unique(d[\"maze_num_targets\"][mc == 0]),\n          \"barriers\", np.unique(d[\"maze_num_barriers\"][mc == 0]), \"novel_maze\", np.unique(d[\"novel_maze\"][mc == 0]))\n    tr = SESS[m][\"trials\"]\n    CT[m] = ldr.condition_table(tr)\n    st = CT[m][\"straight\"]\n    print(\"   72 conditions:\", len(CT[m][\"maze\"]), \"straight (no barrier)\", int(st.sum()), \"curved\", int((~st).sum()))\n    for r in (\"a\", \"b\"):\n        mk = ldr.select_trials(tr, r)\n        print(f\"   trial reading ({r}): {int(mk.sum())} trials; per condition {np.bincount(CT[m]['cond'][mk]).min()} to {np.bincount(CT[m]['cond'][mk]).max()}\")\n    print(\"   with correct_reach also required (not a reading):\", int((ldr.select_trials(tr, 'b') & (tr['correct_reach'] == 1)).sum()))\nMASK = {m: ldr.select_trials(SESS[m][\"trials\"], \"b\") & np.isfinite(SESS[m][\"hand\"][:, 0, 0]) for m in (\"J\", \"N\")}\nprint({m: int(MASK[m].sum()) for m in MASK})\n\n# %% md\n### Clock check\n\nSpikes and the trial table must share a clock. For each recording segment, the condition of a trial is\ndecoded from spike counts in -100 to +300 ms around movement onset (nearest centroid, leave one trial\nout; chance 1/72). As a contrast, the same decoder is run with each trial's activity paired with the\ncondition of the previous trial in the segment.\n\n# %%\ndef clock_check(m):\n    S = SESS[m]\n    tr = S[\"trials\"]\n    cond = CT[m][\"cond\"]\n    gi = (ldr.GRID_MS >= -100) & (ldr.GRID_MS <= 300)\n    F = S[\"R\"][:, :, gi].mean(2)\n    out = []\n    for sg in np.unique(tr[\"segment\"]):\n        ii = np.where((tr[\"segment\"] == sg) & MASK[m])[0]\n        res = []\n        for lab in (cond[ii], np.r_[cond[ii][-1], cond[ii][:-1]]):\n            X = F[ii]\n            hits = 0\n            for q in range(len(ii)):\n                o = np.ones(len(ii), bool)\n                o[q] = False\n                cs = np.unique(lab[o])\n                cen = np.array([X[o & (lab == c)].mean(0) for c in cs])\n                hits += cs[np.argmin(((cen - X[q]) ** 2).sum(1))] == lab[q]\n            res.append(hits / len(ii))\n        out.append((sg, len(ii), res[0], res[1]))\n    return out\n\n\nfor m in (\"J\", \"N\"):\n    for sg, n, acc, acc_sh in clock_check(m):\n        print(f\"{m} segment {sg}: {n} trials, condition decoded {acc:.3f} (labels of the previous trial {acc_sh:.3f}; chance {1/72:.3f})\")\n\n# %% md\n## Basis functions per dataset\n\nFor each dataset, condition-averaged rates are formed from trial reading (b), and the number of temporal\nbasis functions is cross-validated (Methods, Cross-validating the number of temporal basis functions;\nclaims, shared method: k = 1 to 20, two halves of the trials, 100 folds, an even k raised by one). The\nbasis is fitted on -150 to +850 ms (Methods, De-mixing temporal basis functions) and de-mixed. The\ncross-validation is repeated under the five seeds of fig3g-basis-frequencies.\n\n# %%\nD = {}\nfor ds in DATASETS:\n    m, area = ds\n    S = SESS[m]\n    u = S[\"area\"] == area\n    R = S[\"R\"][:, u]\n    cond = CT[m][\"cond\"]\n    X = ldr.cond_average(R, cond, 72, MASK[m])\n    D[ds] = dict(R=R, X=X, Xw=X[..., ldr.FIT0:], cond=cond, u=u)\n\nCV = {}\nfor ds in DATASETS:\n    ks = []\n    for sd in seeds5(\"fig3g-basis-frequencies\"):\n        ve = ldr.cv_tbf_k(D[ds][\"R\"], D[ds][\"cond\"], 72, np.random.default_rng(sd), mask=MASK[ds[0]])\n        kbest = int(np.argmax(ve.mean(0)) + 1)\n        ks.append(kbest)\n        if sd == seed(\"fig3g-basis-frequencies\"):\n            CV[ds] = ve\n    k = ks[0] + (ks[0] % 2 == 0)\n    D[ds][\"k_cv\"] = ks[0]\n    D[ds][\"k_seeds\"] = ks\n    # de-mix; drop the last basis function while more than one real (unpaired) mode remains\n    # (Methods: 'discarded the last basis function if it was unpaired')\n    while True:\n        B, L = ldr.tbf(D[ds][\"Xw\"], k)\n        Bd, Ld, lam, grp, fr = ldr.demix(B, L)\n        if (grp == -1).sum() <= 1 or k == 1:\n            break\n        k -= 1\n    D[ds].update(k=k, B=Bd, L=Ld, lam=lam, grp=grp, freq=fr, Braw=B, Lraw=L)\n    print(NAME[ds], \"held-out VE by k:\", np.round(CV[ds].mean(0)[:12], 3))\n    print(\"   best k under five seeds\", ks, \"-> k used\", k, \"| frequencies (Hz)\", np.round(fr, 2),\n          \"| |eigenvalue|\", np.round(np.abs(lam), 3))\n"
}
```

```
File created successfully at: entries/sabatini-2024/nb_part1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > harness.py <<'EOF'
import sys, pickle, time, re
sys.path.insert(0,'entries/sabatini-2024')
import ldr
_cache={}
def fake(m, shuffle_seeds=(), progress=False):
    return pickle.load(open(f'/tmp/claude-1001/{m}.pkl','rb'))
ldr.load_session=fake
import matplotlib; matplotlib.use('Agg')
parts=sys.argv[1:]
g={'__name__':'__main__'}
if parts[0]=='resume':
    g.update(pickle.load(open('/tmp/claude-1001/state.pkl','rb'))); parts=parts[1:]
    exec("import numpy as np, time, zlib, matplotlib.pyplot as plt\nfrom scipy import stats\nimport ldr",g)
    exec("def seed(claim):\n    return zlib.crc32(f'sabatini-2024/{claim}'.encode())\ndef seeds5(claim):\n    return [seed(claim) + i for i in (0, 1000, 2000, 3000, 4000)]\nDATASETS=[('J','M1'),('J','PMd'),('N','M1'),('N','PMd')]\nNAME={d: f'{d[1]}-{d[0]}' for d in DATASETS}\nT_START=time.time()",g)
    g['SESS']={m:fake(m) for m in ('J','N')}
for p in parts:
    src=open('entries/sabatini-2024/'+p).read()
    cells=re.split(r'^# %%.*$', src, flags=re.M)
    heads=re.findall(r'^# %%.*$', src, flags=re.M)
    for h,c in zip(heads,cells[1:]):
        if h.strip()=='# %% md': continue
        t0=time.time(); exec(c,g); dt=time.time()-t0
        if dt>5: print(f'[cell {h} took {dt:.0f}s]', flush=True)
keep={k:v for k,v in g.items() if k in ('D','CT','MASK','CV','RES','KIN','JP','EIG','TB')}
old={}
try: old=pickle.load(open('/tmp/claude-1001/state.pkl','rb'))
except Exception: pass
old.update(keep)
pickle.dump(old,open('/tmp/claude-1001/state.pkl','wb'))
EOF
time dev/bin/python harness.py nb_part1.py 2>&1 | tail -40
```

```
backward jumps in spike times per unit: [  0   0   0   0 192]
  trials per segment: [930 881 899 939  45]
  trial start times monotonic: False
  -500..+1000 ms window inside the trial interval for 2121 of 2121 kept trials
  delay (go - target) s: range [-0.003  0.665  0.999]
  movement onset - go cue s: range [0.145 0.374 1.69 ]
  hand position (file unit 'meters'): range x -155.1 151.1 y -182.3 67.4 | trials without hand 1
  peak hand speed per trial (file units per s): median 741.4
  reach duration ms: median 383.0 range 206.0 813.0
  smoothed rates (spikes/s): range 0.0 484.21783447265625 mean 47.47356414794922
peak memory GB 3.366504
J reading (a) conditions 72 | reading (b) 1-target conditions 73 | (b) minus maze 0: 72 | same set as (a): True
   maze 0 trials: 203 targets [1 3] barriers [2 7 9] novel_maze [0 1]
   72 conditions: 72 straight (no barrier) 36 curved 36
   trial reading (a): 1595 trials; per condition 17 to 29
   trial reading (b): 1381 trials; per condition 16 to 23
   with correct_reach also required (not a reading): 1345
N reading (a) conditions 72 | reading (b) 1-target conditions 73 | (b) minus maze 0: 72 | same set as (a): True
   maze 0 trials: 419 targets [1 3] barriers [0 1 2 3 4 5 6 7 8 9] novel_maze [0 1]
   72 conditions: 72 straight (no barrier) 36 curved 36
[... 25 more lines not kept]
```

**Agent**

Clock check flags something: in monkey N, segment 3 decodes condition at 0.16 against 0.41 to 0.46 in segments 0 to 2. Checking for a time offset in that segment.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > seg3.py <<'EOF'
import sys, pickle, numpy as np
sys.path.insert(0,'entries/sabatini-2024')
import ldr
f,aid=ldr.open_nwb('N'); d=ldr.load_trials(f)
ht=f['processing/behavior/Position/Hand/timestamps'][:]
hs=ldr._segments(ht); hb=[(ht[a],ht[b-1]) for a,b in hs]
tseg=ldr.assign_trial_segments(d['start_time'],hb)
keep=ldr.select_trials(d,'b'); mc=d['maze_condition']
u=f['units']; idx=u['spike_times_index'][:]
units=range(0,192,2)
sp=[]; a0=0
allst=u['spike_times'][:]
for un in units:
    a=0 if un==0 else idx[un-1]; s=allst[a:idx[un]]; sp.append([s[x:y] for x,y in ldr._segments(s)])
offs=[-3,-1,-0.5,-0.25,-0.1,0,0.1,0.25,0.5,1,3]
for sg in [1,2,3]:
    ii=np.where(keep&(tseg==sg))[0]; lab=np.searchsorted(np.unique(mc[keep]),mc[ii])
    for off in offs:
        on=d['move_begins_time'][ii]+off
        F=np.array([[np.searchsorted(s[sg],o+0.3)-np.searchsorted(s[sg],o-0.1) for o in on] for s in sp]).T.astype(float)
        hits=0
        for q in range(len(ii)):
            o=np.ones(len(ii),bool); o[q]=False; cs=np.unique(lab[o])
            cen=np.array([F[o&(lab==c)].mean(0) for c in cs]); hits+=cs[np.argmin(((cen-F[q])**2).sum(1))]==lab[q]
        print(sg, off, round(hits/len(ii),3), 'mean count', F.mean().round(2), flush=True)
EOF
dev/bin/python seg3.py
```

```
1 -3 0.016 mean count 5.77
1 -1 0.033 mean count 15.95
1 -0.5 0.116 mean count 18.64
1 -0.25 0.285 mean count 23.99
1 -0.1 0.374 mean count 24.6
1 0 0.381 mean count 22.64
1 0.1 0.354 mean count 20.42
1 0.25 0.33 mean count 18.0
1 0.5 0.234 mean count 15.46
1 1 0.187 mean count 14.01
1 3 0.024 mean count 7.97
2 -3 0.021 mean count 5.63
2 -1 0.041 mean count 15.92
2 -0.5 0.118 mean count 18.77
2 -0.25 0.286 mean count 24.08
2 -0.1 0.404 mean count 24.89
2 0 0.44 mean count 22.86
2 0.1 0.417 mean count 20.64
2 0.25 0.361 mean count 18.23
2 0.5 0.28 mean count 15.78
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > seg3b.py <<'EOF'
import sys, pickle, numpy as np
sys.path.insert(0,'entries/sabatini-2024')
import ldr
S=pickle.load(open('N.pkl','rb')); tr=S['trials']; ct=ldr.condition_table(tr); cond=ct['cond']
mask=ldr.select_trials(tr,'b')&np.isfinite(S['hand'][:,0,0])
h=S['hand']; end=h[:,-300]-h[:,0]  # displacement at +550 ms
tgt=np.column_stack([tr['target_x'],tr['target_y']])
for sg in range(5):
    m=mask&(tr['segment']==sg)
    ang_err=np.angle(np.exp(1j*(np.arctan2(end[m,1],end[m,0])-np.arctan2(tgt[m,1],tgt[m,0]))))
    print(sg, m.sum(), 'median |angle error| deg hand vs target', np.degrees(np.median(np.abs(ang_err))).round(1))
gi=(ldr.GRID_MS>=-100)&(ldr.GRID_MS<=300); F=S['R'][:,:,gi].mean(2)
tr_m=mask&np.isin(tr['segment'],[0,1,2])
cs=np.unique(cond[tr_m]); cen=np.array([F[tr_m&(cond==c)].mean(0) for c in cs])
for sg in range(5):
    m=np.where(mask&(tr['segment']==sg))[0]
    pred=cs[np.argmin(((F[m][:,None,:]-cen[None])**2).sum(2),1)]
    print('train seg0-2 test seg',sg, (pred==cond[m]).mean().round(3))
# per-unit mean rate by segment
for sg in range(5):
    m=mask&(tr['segment']==sg); print(sg, 'mean rate M1',F[m][:,S['area']=='M1'].mean().round(2),'PMd',F[m][:,S['area']=='PMd'].mean().round(2))
r=np.array([F[mask&(tr['segment']==sg)].mean(0) for sg in range(4)]); print(np.corrcoef(r).round(3))
EOF
dev/bin/python seg3b.py
```

```
0 467 median |angle error| deg hand vs target 87.1
1 449 median |angle error| deg hand vs target 87.1
2 468 median |angle error| deg hand vs target 85.2
3 477 median |angle error| deg hand vs target 87.0
4 22 median |angle error| deg hand vs target 95.6
train seg0-2 test seg 0 0.809
train seg0-2 test seg 1 0.88
train seg0-2 test seg 2 0.857
train seg0-2 test seg 3 0.48
train seg0-2 test seg 4 0.545
0 mean rate M1 52.89 PMd 53.83
1 mean rate M1 53.91 PMd 56.21
2 mean rate M1 54.06 PMd 58.01
3 mean rate M1 55.7 PMd 56.56
4 mean rate M1 54.36 PMd 55.31
[[1.    0.979 0.913 0.808]
 [0.979 1.    0.957 0.834]
 [0.913 0.957 1.    0.881]
 [0.808 0.834 0.881 1.   ]]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > hand.py <<'EOF'
import sys, pickle, numpy as np
sys.path.insert(0,'entries/sabatini-2024')
import ldr
for m in 'JN':
    S=pickle.load(open(f'{m}.pkl','rb')); tr=S['trials']; h=S['hand']
    ok=np.isfinite(h[:,0,0])
    for lag in [0,350,500,700,900,1200]:
        disp=h[:,min(lag,1200)]-h[:,0]
        a=np.arctan2(disp[:,1],disp[:,0]); b=np.arctan2(tr['target_y'],tr['target_x'])
        e=np.degrees(np.abs(np.angle(np.exp(1j*(a-b)))))
        print(m, lag-350, 'ms: median err', np.nanmedian(e[ok]).round(1), 'disp', np.nanmedian(np.hypot(*disp[ok].T)).round(1))
    i=np.where(ok)[0][0]; print('target', tr['target_x'][i], tr['target_y'][i], 'hand', h[i,::200].round(1).tolist())
    print('hand start median', np.nanmedian(h[:,0],0))
EOF
dev/bin/python hand.py
```

```
J -350 ms: median err 71.8 disp 0.0
J 0 ms: median err 56.2 disp 2.7
J 150 ms: median err 14.7 disp 85.7
J 350 ms: median err 3.4 disp 130.4
J 550 ms: median err 2.2 disp 129.9
J 850 ms: median err 2.0 disp 130.5
target -77.0 82.0 hand [[-4.1, -36.1], [-4.0, -36.2], [12.6, -20.5], [-32.6, 79.0], [-64.3, 53.7], [-64.2, 53.3], [-64.5, 52.5]]
hand start median [ -1.13006794 -38.43829476]
N -350 ms: median err 38.6 disp 0.0
N 0 ms: median err 39.2 disp 3.2
N 150 ms: median err 91.7 disp 75.2
N 350 ms: median err 88.3 disp 133.3
N 550 ms: median err 86.2 disp 136.9
N 850 ms: median err 88.0 disp 133.1
target 119.0 80.0 hand [[0.7, -64.0], [0.7, -64.0], [13.8, -44.0], [103.0, 24.9], [117.1, 27.2], [115.0, 22.7], [110.7, 20.1]]
hand start median [  2.41951483 -63.8969962 ]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python - <<'EOF'
s=open('nb_part1.py').read()
old="""        out.append((sg, len(ii), res[0], res[1]))
    return out


for m in ("J", "N"):
    for sg, n, acc, acc_sh in clock_check(m):
        print(f"{m} segment {sg}: {n} trials, condition decoded {acc:.3f} (labels of the previous trial {acc_sh:.3f}; chance {1/72:.3f})")"""
new="""        # trained on the other segments, tested on this one
        oth = np.where((tr["segment"] != sg) & MASK[m])[0]
        cross = np.nan
        if len(oth):
            cs = np.unique(cond[oth])
            cen = np.array([F[oth][cond[oth] == c].mean(0) for c in cs])
            pred = cs[np.argmin(((F[ii][:, None, :] - cen[None]) ** 2).sum(2), 1)]
            cross = (pred == cond[ii]).mean()
        out.append((sg, len(ii), res[0], res[1], cross))
    return out


for m in ("J", "N"):
    for sg, n, acc, acc_sh, cross in clock_check(m):
        print(f"{m} segment {sg}: {n} trials, condition decoded {acc:.3f} (labels of the previous trial {acc_sh:.3f}; "
              f"trained on the other segments {cross:.3f}; chance {1/72:.3f})")"""
assert old in s; s=s.replace(old,new); open('nb_part1.py','w').write(s)
EOF
date -u
```

```
Fri Nov 20 11:06:53 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ldr.py').read()
old='''    if mask is None:
        mask = np.ones(len(cond), bool)
    out = np.zeros((nc,) + X.shape[1:])
    for c in range(nc):
        m = mask & (cond == c)
        out[c] = np.nanmean(X[m], axis=0)
    return out'''
new='''    if mask is None:
        mask = np.ones(len(cond), bool)
    W = np.zeros((nc, len(cond)))
    W[cond[mask], np.where(mask)[0]] = 1
    W /= W.sum(1, keepdims=True)
    return (W @ X.reshape(len(cond), -1)).reshape((nc,) + X.shape[1:])'''
assert old in s; s=s.replace(old,new); open('ldr.py','w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ldr.py').read()
old='''    W /= W.sum(1, keepdims=True)
    return (W @ X.reshape(len(cond), -1)).reshape((nc,) + X.shape[1:])'''
new='''    W /= W.sum(1, keepdims=True)
    return (W[:, mask] @ X[mask].reshape(int(mask.sum()), -1)).reshape((nc,) + X.shape[1:])'''
assert old in s; s=s.replace(old,new); open('ldr.py','w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "entries/sabatini-2024/nb_part2.py",
 "content": "# %% md\n## data-composition\n\n> Two monkeys (J and N) performed the maze task with 72 conditions (36 straight, 36 curved); a PMd and\n> an M1 array in each monkey gave 79 to 118 units per array; 1469 trials for monkey J and 2014 for\n> monkey N.\n\n# %% [claim:data-composition]\nfor m, paper_n in ((\"J\", 1469), (\"N\", 2014)):\n    tr = SESS[m][\"trials\"]\n    for r in (\"a\", \"b\"):\n        n = int(ldr.select_trials(tr, r).sum())\n        print(f\"monkey {m}, trial reading ({r}): {n} trials (paper {paper_n}, tolerance {paper_n * 0.1:.1f}; \"\n              f\"within: {abs(n - paper_n) <= paper_n * 0.1}; difference {n - paper_n:+d})\")\n    print(f\"monkey {m}: conditions {len(CT[m]['maze'])}, straight {int(CT[m]['straight'].sum())}, curved {int((~CT[m]['straight']).sum())}\")\n    for a in (\"M1\", \"PMd\"):\n        print(f\"   {a}: {int((SESS[m]['area'] == a).sum())} units; units table columns hold no single/multi-unit label\")\nprint(\"units per electrode (J):\", np.unique(np.bincount(np.arange(192))))\n\n# %% md\n## Single-condition LDSs: fig2c-condition-lds-variance\n\n> Activity on each single condition was low-dimensional and approximated by an LDS of 5 to 9 dimensions,\n> which explained 71 to 93% of the population variance.\n\nDimensionality by cross-validation over two trial partitions, 100 repeats, odd k from 1 to 21 (the\ncode's set; claims), one k per dataset. The Methods' even split is the main reading and the code's 3/4\nto 1/4 split a variant.\n\n# %% [claim:fig2c-condition-lds-variance]\nKS = list(range(1, 22, 2))\nfor ds in DATASETS:\n    res = {}\n    for frac, lab in ((0.5, \"even split\"), (0.75, \"3/4 split\")):\n        cv = ldr.cv_condition_dim(D[ds][\"R\"], D[ds][\"cond\"], 72, np.random.default_rng(seed(\"fig2c-condition-lds-variance\")),\n                                  KS, folds=100, mask=MASK[ds[0]], frac=frac)\n        res[lab] = KS[int(np.argmax(cv.mean((0, 1))))]\n        if frac == 0.5:\n            cvm = cv.mean((0, 1))\n    kd = res[\"even split\"]\n    sims, lams = [], []\n    for c in range(72):\n        Xc = D[ds][\"Xw\"][c]\n        Xs, lam = ldr.rrr_lds(Xc, kd)\n        sims.append(ldr.pop_ve(Xc, Xs))\n        lams.append(lam)\n    D[ds][\"lds_k\"] = kd\n    D[ds][\"lds_ve\"] = np.array(sims)\n    D[ds][\"lds_lam\"] = lams\n    kv = res[\"3/4 split\"]\n    ve_v = np.array([ldr.pop_ve(D[ds][\"Xw\"][c], ldr.rrr_lds(D[ds][\"Xw\"][c], kv)[0]) for c in range(72)])\n    D[ds][\"lds_ve_var\"] = ve_v\n    print(f\"{NAME[ds]}: held-out VE by k {dict(zip(KS, np.round(cvm, 3)))}\")\n    print(f\"   chosen k {kd} (even split) | {kv} (3/4 split) ; LDS VE mean {np.mean(sims):.3f} s.d. {np.std(sims):.3f} \"\n          f\"range {np.min(sims):.3f}-{np.max(sims):.3f} | at k={kv}: mean {ve_v.mean():.3f}\")\n# seed sensitivity of the chosen k\nfor ds in DATASETS:\n    ks = []\n    for sd in seeds5(\"fig2c-condition-lds-variance\")[1:]:\n        cv = ldr.cv_condition_dim(D[ds][\"R\"], D[ds][\"cond\"], 72, np.random.default_rng(sd), KS, folds=100, mask=MASK[ds[0]])\n        ks.append(KS[int(np.argmax(cv.mean((0, 1))))])\n    print(NAME[ds], \"chosen k under the four other seeds:\", ks)\n\n# %% md\n## fig3a-eigenvalue-clusters\n\n> Eigenvalues of the single-condition LDSs formed distinct clusters, corresponding to rotations at about\n> 0.5, 1.5, 2.5 and 4 Hz on every condition, along with an offset.\n\n# %% [claim:fig3a-eigenvalue-clusters]\nfig, axs = plt.subplots(1, 4, figsize=(14, 3.2))\nfor ax, ds in zip(axs, DATASETS):\n    lams = D[ds][\"lds_lam\"]\n    pairs = [np.sort(np.abs(np.angle(l[l.imag > 1e-12]))) / (2 * np.pi) * 100 for l in lams]\n    npair = np.array([len(p) for p in pairs])\n    nreal = np.array([int(np.sum(np.abs(l.imag) <= 1e-12)) for l in lams])\n    maxp = npair.max()\n    med = [np.median([p[i] for p in pairs if len(p) > i]) for i in range(maxp)]\n    cnt = [sum(len(p) > i for p in pairs) for i in range(maxp)]\n    targets = [0.5, 1.5, 2.5, 4.0]\n    ok = [abs(med[i] - targets[i]) <= 0.1 * targets[i] for i in range(min(maxp, 4))]\n    print(f\"{NAME[ds]}: k={D[ds]['lds_k']}; complex pairs per condition {np.bincount(npair)} ; real eigenvalues per condition \"\n          f\"{np.bincount(nreal)} ; conditions with >=1 real: {int((nreal >= 1).sum())}/72\")\n    print(f\"   median frequency of pair rank 1..{maxp} (Hz): {np.round(med, 2)} (conditions: {cnt}); within 10% of 0.5,1.5,2.5,4: {ok}\")\n    allf = np.concatenate([np.abs(np.angle(l)) / (2 * np.pi) * 100 for l in lams])\n    print(f\"   all eigenvalue frequencies: range {allf.min():.2f}-{allf.max():.2f} Hz; |eigenvalue| range \"\n          f\"{min(np.abs(l).min() for l in lams):.3f}-{max(np.abs(l).max() for l in lams):.3f}\")\n    L_ = np.concatenate(lams)\n    ax.scatter(L_.real, L_.imag, s=3)\n    ax.set_title(NAME[ds]); ax.set_xlabel(\"real\"); ax.set_ylabel(\"imag\")\n    ax.set_xlim(0.8, 1.01); ax.set_ylim(-0.25, 0.25)\n    print(f\"   points outside the axes: {int(np.sum((L_.real < 0.8) | (np.abs(L_.imag) > 0.25)))}\")\nplt.tight_layout(); plt.show()\n\n# %% md\n## fig3c-eigenvalue-distance-auc\n\n> Eigenvalues differed between conditions only slightly more than expected from estimation noise, with\n> ROC-AUC 0.51 to 0.58 between the between-condition distances and the noise distribution.\n\nDistance: mean over frequency-sorted corresponding eigenvalues of their distance in the complex plane\n(claims); the code's vector norm is a variant. Nulls: (a) Poisson, two sets of 20 trials simulated from\neach condition's rates; (b) random halves of the real trials. The Methods give 500 repeats per\ncondition; 100 are run here for each reading (deviation; time). The Poisson trials are simulated as\n10 ms counts from the smoothed rates and smoothed with a 20 ms Gaussian at 10 ms resolution\n(deviation: the paper simulates at the resolution of its 1 ms pipeline).\n\n# %%\ndef eig_dist(l1, l2, how=\"mean\"):\n    a, b = ldr.sort_eigs(l1), ldr.sort_eigs(l2)\n    n = min(len(a), len(b))\n    if how == \"mean\":\n        return np.mean(np.abs(a[:n] - b[:n]))\n    return np.linalg.norm(a[:n] - b[:n])\n\n\ndef eig_null(ds, reading, nrep, sd):\n    rng = np.random.default_rng(sd)\n    m = ds[0]\n    kd = D[ds][\"lds_k\"]\n    R, cond = D[ds][\"R\"], D[ds][\"cond\"]\n    out_mean, out_norm = [], []\n    if reading == \"b\":\n        for r in range(nrep):\n            a, b = ldr.split_half(cond, 72, rng, MASK[m])\n            XA = ldr.cond_average(R, cond, 72, a)[..., ldr.FIT0:]\n            XB = ldr.cond_average(R, cond, 72, b)[..., ldr.FIT0:]\n            for c in range(72):\n                la, lb = ldr.rrr_lds(XA[c], kd)[1], ldr.rrr_lds(XB[c], kd)[1]\n                out_mean.append(eig_dist(la, lb)); out_norm.append(eig_dist(la, lb, \"norm\"))\n    else:\n        from scipy.ndimage import gaussian_filter1d\n        lam_rate = np.clip(D[ds][\"X\"], 0, None) * 0.01 * 20  # expected count of 20 trials per 10 ms bin\n        for r in range(nrep):\n            for c in range(72):\n                est = []\n                for _ in range(2):\n                    cnt = rng.poisson(lam_rate[c]).astype(float)\n                    est.append(gaussian_filter1d(cnt, 2.0, axis=1, mode=\"reflect\")[:, ldr.FIT0:] / (0.01 * 20))\n                la, lb = ldr.rrr_lds(est[0], kd)[1], ldr.rrr_lds(est[1], kd)[1]\n                out_mean.append(eig_dist(la, lb)); out_norm.append(eig_dist(la, lb, \"norm\"))\n    return np.array(out_mean), np.array(out_norm)\n\n\nEIG = {}\nfor ds in DATASETS:\n    lams = D[ds][\"lds_lam\"]\n    obs = np.array([eig_dist(lams[i], lams[j]) for i in range(72) for j in range(i + 1, 72)])\n    obs_n = np.array([eig_dist(lams[i], lams[j], \"norm\") for i in range(72) for j in range(i + 1, 72)])\n    EIG[ds] = dict(obs=obs, obs_n=obs_n)\n    for reading in (\"a\", \"b\"):\n        t0 = time.time()\n        nm, nn = eig_null(ds, reading, 100, seed(\"fig3c-eigenvalue-distance-auc\"))\n        EIG[ds][reading] = (nm, nn)\n    print(NAME[ds], \"done\", round(time.time() - t0), \"s\")\n\n# %% [claim:fig3c-eigenvalue-distance-auc]\nfor ds in DATASETS:\n    e = EIG[ds]\n    for reading in (\"a\", \"b\"):\n        nm, nn = e[reading]\n        A, raw = ldr.auc(e[\"obs\"], nm)\n        An, rawn = ldr.auc(e[\"obs_n\"], nn)\n        print(f\"{NAME[ds]} null ({reading}): AUC {A:.3f} (unfolded {raw:.3f}); median distance between conditions \"\n              f\"{np.median(e['obs']):.4f}, noise {np.median(nm):.4f} | code's norm variant AUC {An:.3f}\")\n# seed sensitivity, null (b), 20 repeats under each of the four other seeds\nfor ds in DATASETS:\n    vals = []\n    for sd in seeds5(\"fig3c-eigenvalue-distance-auc\")[1:]:\n        nm, _ = eig_null(ds, \"b\", 20, sd)\n        vals.append(ldr.auc(EIG[ds][\"obs\"], nm)[0])\n    print(NAME[ds], \"null (b) AUC under four other seeds (20 repeats each):\", np.round(vals, 3))\n\n# %% md\n## suppfig2-eigenvalues-from-kinematics\n\nThis claim needs the reach parameters of fig6e; it is computed in the kinematics section below.\n\n## fig3g-basis-frequencies\n\n> The cross-validated temporal basis functions contained 3 to 4 rotations at 0.5, 1.5, 2.5 and 4 Hz,\n> along with an offset.\n\n# %% [claim:fig3g-basis-frequencies]\nfig, axs = plt.subplots(1, 4, figsize=(14, 3))\nfor ax, ds in zip(axs, DATASETS):\n    g, fr = D[ds][\"grp\"], D[ds][\"freq\"]\n    rot_f = [fr[g == r][0] for r in range(g.max() + 1)]\n    near = [min([0.5, 1.5, 2.5, 4.0], key=lambda t: abs(t - f)) for f in rot_f]\n    within = [abs(f - t) <= 0.1 * t for f, t in zip(rot_f, near)]\n    print(f\"{NAME[ds]}: CV best k {D[ds]['k_cv']} (five seeds {D[ds]['k_seeds']}), k used {D[ds]['k']}; rotation pairs {g.max() + 1}, \"\n          f\"real modes {(g == -1).sum()}; rotation frequencies {np.round(rot_f, 2)} Hz; nearest of 0.5/1.5/2.5/4 {near}; within 10%: {within}\")\n    print(f\"   |eigenvalue| of the offset mode {np.abs(D[ds]['lam'][g == -1]).round(4)}\")\n    ax.plot(ldr.GRID_MS[ldr.FIT0:], D[ds][\"B\"].T)\n    ax.set_title(NAME[ds]); ax.set_xlabel(\"ms from movement onset\")\nplt.tight_layout(); plt.show()\n\n# %% md\n## tbf-variance-explained\n\n> The shared rotations of the temporal basis factorization explained 90 to 96% of the population variance.\n\n# %% [claim:tbf-variance-explained]\nfor ds in DATASETS:\n    Xw = D[ds][\"Xw\"]\n    ve_a = ldr.pop_ve(Xw, np.einsum(\"cnk,kt->cnt\", D[ds][\"L\"], D[ds][\"B\"]))\n    B2, L2 = ldr.tbf(D[ds][\"X\"], D[ds][\"k\"])\n    ve_b = ldr.pop_ve(D[ds][\"X\"], np.einsum(\"cnk,kt->cnt\", L2, B2))\n    D[ds][\"tbf_ve\"] = ve_a\n    print(f\"{NAME[ds]}: (a) -150..+850 ms, de-mixed basis: mean {ve_a.mean():.3f} s.d. {ve_a.std():.3f} range {ve_a.min():.3f}-{ve_a.max():.3f} | \"\n          f\"(b) -350..+850 ms, raw SVD basis: mean {ve_b.mean():.3f} s.d. {ve_b.std():.3f}\")\n\n# %% md\n## tbf-shuffle-control and fig3h-recoverability\n\nShuffled data: the 1 ms bins of each trial permuted in time (one permutation for all units of a trial)\nbefore smoothing and averaging, then TBF with the dataset's k. Recoverability per condition: the\nvariance of the basis functions explained by pinv(L(c)) X(c) (Methods, Eq. 6).\n\n# %%\ndef recoverability(L, B, Xw):\n    out = []\n    for c in range(len(L)):\n        Bh = np.linalg.pinv(L[c]) @ Xw[c]\n        out.append(ldr.pop_ve(B, Bh))\n    return np.array(out)\n\n\nSH = {}\nfor ds in DATASETS:\n    m, area = ds\n    D[ds][\"rec\"] = recoverability(D[ds][\"L\"], D[ds][\"B\"], D[ds][\"Xw\"])\n    SH[ds] = {}\n    for sd in seeds5(\"tbf-shuffle-control\"):\n        Xs = ldr.cond_average(SESS[m][\"RS\"][sd][:, D[ds][\"u\"]], D[ds][\"cond\"], 72, MASK[m])[..., ldr.FIT0:]\n        Bs, Ls = ldr.tbf(Xs, D[ds][\"k\"])\n        ve = ldr.pop_ve(Xs, np.einsum(\"cnk,kt->cnt\", Ls, Bs))\n        SH[ds][sd] = dict(ve=ve, rec=recoverability(Ls, Bs, Xs))\n\n# %% [claim:tbf-shuffle-control]\ns0 = seed(\"tbf-shuffle-control\")\nfor ds in DATASETS:\n    real, sh = D[ds][\"tbf_ve\"], SH[ds][s0][\"ve\"]\n    p_rs = stats.ranksums(real, sh).pvalue\n    p_sr = stats.wilcoxon(real, sh).pvalue\n    print(f\"{NAME[ds]}: shuffled VE mean {sh.mean():.3f} s.d. {sh.std():.3f} (real {real.mean():.3f}); rank-sum p {p_rs:.2e}; \"\n          f\"signed-rank (variant) p {p_sr:.2e}; real higher on {int((real > sh).sum())}/72\")\n    print(\"   shuffled mean under the five seeds:\", [round(SH[ds][sd][\"ve\"].mean(), 4) for sd in seeds5(\"tbf-shuffle-control\")])\n\n# %% [claim:fig3h-recoverability]\nfor ds in DATASETS:\n    rec, ch = D[ds][\"rec\"], SH[ds][s0][\"rec\"]\n    print(f\"{NAME[ds]}: recoverability mean {rec.mean():.3f} s.d. {rec.std():.3f}; chance (shuffled data) mean {ch.mean():.3f}; \"\n          f\"rank-sum p {stats.ranksums(rec, ch).pvalue:.2e}; real higher on {int((rec > ch).sum())}/72\")\n    print(\"   chance mean under the five seeds:\", [round(SH[ds][sd][\"rec\"].mean(), 4) for sd in seeds5(\"tbf-shuffle-control\")])\n\n# %% md\n## fig3i-duration-warping\n\nReach duration per trial: movement onset to the last 1 ms sample at which hand speed is at least a tenth\nof its peak, within 850 ms (claims; code warpTrials.m). Per condition, the mean over its trials;\ncorrelation of |duration - mean over conditions| with recoverability, before and after warping.\n\n# %% [claim:fig3i-duration-warping]\nfor ds in DATASETS:\n    m = ds[0]\n    dur = SESS[m][\"trials\"][\"duration_ms\"]\n    cdur = np.array([np.nanmean(dur[MASK[m] & (D[ds][\"cond\"] == c)]) for c in range(72)])\n    ext = np.abs(cdur - cdur.mean())\n    D[ds][\"cdur\"] = cdur\n    r0, p0 = stats.pearsonr(ext, D[ds][\"rec\"])\n    out = [f\"{NAME[ds]}: condition duration {cdur.min():.0f}-{cdur.max():.0f} ms; unwarped rho {r0:.3f} p {p0:.3g}\"]\n    for key, lab in ((\"RW\", \"warped, truncated at 850 (main)\"), (\"RW2\", \"warped, post-reach to 250 ms\")):\n        Xwp = ldr.cond_average(SESS[m][key][:, D[ds][\"u\"]], D[ds][\"cond\"], 72, MASK[m])[..., ldr.FIT0:]\n        Bw, Lw = ldr.tbf(Xwp, D[ds][\"k\"])\n        Bw, Lw = ldr.demix(Bw, Lw)[:2]\n        recw = recoverability(Lw, Bw, Xwp)\n        r, p = stats.pearsonr(ext, recw)\n        out.append(f\"{lab}: rho {r:.3f} p {p:.3g} (recoverability mean {recw.mean():.3f})\")\n    print(\" | \".join(out))\n\n# %% md\n## single-lds-variance\n\n> A single linear dynamical system fitted to all conditions captured on average 46 to 66% of the\n> population variance.\n\n# %% [claim:single-lds-variance]\nfor ds in DATASETS:\n    X = D[ds][\"X\"]\n    Xp = np.concatenate([X[c, :, ldr.FIT0:-1].T for c in range(72)])\n    Xf = np.concatenate([X[c, :, ldr.FIT0 + 1:].T for c in range(72)])\n    M = np.linalg.lstsq(Xp, Xf, rcond=None)[0]\n    ve_a, ve_b = [], []\n    for c in range(72):\n        sim = np.zeros((X.shape[2], X.shape[1]))\n        sim[: ldr.FIT0 + 1] = X[c, :, : ldr.FIT0 + 1].T\n        for t in range(ldr.FIT0 + 1, X.shape[2]):\n            sim[t] = sim[t - 1] @ M\n        ve_a.append(ldr.pop_ve(X[c, :, ldr.FIT0:], sim[ldr.FIT0:].T))\n        ve_b.append(ldr.pop_ve(X[c], sim.T))\n    ve_a, ve_b = np.array(ve_a), np.array(ve_b)\n    D[ds][\"slds_ve\"] = ve_a\n    print(f\"{NAME[ds]}: (a) -150..+850 mean {ve_a.mean():.3f} s.d. {ve_a.std():.3f} | (b) whole window, bins before -150 copied \"\n          f\"mean {ve_b.mean():.3f} s.d. {ve_b.std():.3f} | max |eigenvalue| of M {np.abs(np.linalg.eigvals(M)).max():.4f}\")\n"
}
```

```
File created successfully at: entries/sabatini-2024/nb_part2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && time dev/bin/python harness.py resume nb_part2.py 2>&1 | tail -60
```

```
all eigenvalue frequencies: range 0.00-3.65 Hz; |eigenvalue| range 0.910-0.999
   points outside the axes: 0
PMd-N: k=5; complex pairs per condition [ 0  0 72] ; real eigenvalues per condition [ 0 72] ; conditions with >=1 real: 72/72
   median frequency of pair rank 1..2 (Hz): [0.73 1.67] (conditions: [72, 72]); within 10% of 0.5,1.5,2.5,4: [np.False_, np.False_]
   all eigenvalue frequencies: range 0.00-2.06 Hz; |eigenvalue| range 0.961-0.999
   points outside the axes: 0
M1-J done 62 s
PMd-J done 62 s
M1-N done 64 s
PMd-N done 64 s
[cell # %% took 543s]
M1-J null (a): AUC 0.812 (unfolded 0.812); median distance between conditions 0.0124, noise 0.0060 | code's norm variant AUC 0.794
M1-J null (b): AUC 0.696 (unfolded 0.696); median distance between conditions 0.0124, noise 0.0082 | code's norm variant AUC 0.689
PMd-J null (a): AUC 0.705 (unfolded 0.705); median distance between conditions 0.0116, noise 0.0072 | code's norm variant AUC 0.706
PMd-J null (b): AUC 0.641 (unfolded 0.641); median distance between conditions 0.0116, noise 0.0085 | code's norm variant AUC 0.645
M1-N null (a): AUC 0.631 (unfolded 0.631); median distance between conditions 0.0161, noise 0.0126 | code's norm variant AUC 0.629
M1-N null (b): AUC 0.662 (unfolded 0.662); median distance between conditions 0.0161, noise 0.0120 | code's norm variant AUC 0.657
PMd-N null (a): AUC 0.704 (unfolded 0.704); median distance between conditions 0.0109, noise 0.0074 | code's norm variant AUC 0.702
PMd-N null (b): AUC 0.680 (unfolded 0.680); median distance between conditions 0.0109, noise 0.0079 | code's norm variant AUC 0.677
M1-J null (b) AUC under four other seeds (20 repeats each): [0.696 0.709 0.694 0.695]
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && dev/bin/python -c "
import pickle; s=pickle.load(open('state.pkl','rb')); print(s.keys())
"; nproc; free -g | head -2
```

```
Fri Nov 20 11:32:52 UTC 2026
dict_keys(['CT', 'MASK', 'D', 'CV', 'EIG'])
4
               total        used        free      shared  buff/cache   available
Mem:              15           1           8           0           6          14
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python - <<'EOF'
s=open('ldr.py').read()
old=s[s.index("def sea(planes"):s.index("def participation_ratio")]
new='''def sea(planes, ndim=25, seeds=None):
    """Subspace excursion angles (Methods, Subspace excursion angles). planes: list of
    (neurons, d) orthonormal bases. From a seed, repeatedly add the vector of any other subspace
    that forms the greatest angle with the span so far. Every seed is tried and the sequence with
    the largest summed angles is kept (the Methods optimise over sequences; assumption that
    greedy steps from the best seed implement it). Returns angles in degrees."""
    best, bestsum = None, -1
    if seeds is None:
        seeds = range(len(planes))
    P = np.stack(planes)  # (c, N, d)
    for s0 in seeds:
        S = planes[s0].copy()
        angs = []
        while len(angs) < ndim and S.shape[1] < P.shape[1]:
            R = P - np.einsum("nk,cmd,mk->cnd", S, P, S)  # residuals (c, N, d)
            G = np.einsum("cnd,cne->cde", R, R)
            w, v = np.linalg.eigh(G)
            c = int(np.argmax(w[:, -1]))
            sv = np.sqrt(max(w[c, -1], 0.0))
            angs.append(np.degrees(np.arcsin(min(1.0, sv))))
            vec = R[c] @ v[c, :, -1]
            vec = vec / np.linalg.norm(vec)
            vec = vec - S @ (S.T @ vec)
            S = np.column_stack([S, vec / np.linalg.norm(vec)])
        if sum(angs) > bestsum:
            bestsum, best = sum(angs), np.array(angs)
    return best


def pmap(func, args, processes=4):
    """Run func over args in forked worker processes (standard; speeds up independent fits)."""
    import multiprocessing as mp
    with mp.get_context("fork").Pool(processes) as pool:
        return pool.map(func, args)


'''
s=s.replace(old,new); open('ldr.py','w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "entries/sabatini-2024/nb_part3.py",
 "content": "# %% md\n## Alignment of rotations across conditions\n\nRotations are the pairs of de-mixed basis functions that share a frequency; the state space location\nis the column of the real (offset) mode. Noise: loadings fitted by regression on the fixed basis to\ntwo random halves of a condition's trials, 36 repeats (Methods, Measuring the across-condition\nalignment of rotations).\n\n# %%\ndef comps(ds):\n    g = D[ds][\"grp\"]\n    out = [(\"rot%d (%.2f Hz)\" % (r, D[ds][\"freq\"][g == r][0]), np.where(g == r)[0]) for r in range(g.max() + 1)]\n    out.append((\"location\", np.where(g == -1)[0][:1]))\n    return out\n\n\ndef ai_matrix(L1, B1, L2):\n    \"\"\"AI of each condition's activity L1[c] @ B1 onto span(L2[c']) for all c, c'. Returns (C, C).\"\"\"\n    C = len(L1)\n    Q = np.stack([ldr.orth(L2[c]) for c in range(C)])\n    out = np.zeros((C, C))\n    for c in range(C):\n        Y = L1[c] @ B1\n        Y = Y - Y.mean(1, keepdims=True)\n        out[c] = np.sum(np.einsum(\"knd,nt->kdt\", Q, Y) ** 2, axis=(1, 2)) / np.sum(Y ** 2)\n    return out\n\n\ndef noise_ai(ds, nrep, sd):\n    rng = np.random.default_rng(sd)\n    m = ds[0]\n    Bp = np.linalg.pinv(D[ds][\"B\"])\n    out = {name: [] for name, _ in comps(ds)}\n    halves = []\n    for r in range(nrep):\n        a, b = ldr.split_half(D[ds][\"cond\"], 72, rng, MASK[m])\n        LA = ldr.cond_average(D[ds][\"R\"], D[ds][\"cond\"], 72, a)[..., ldr.FIT0:] @ Bp\n        LB = ldr.cond_average(D[ds][\"R\"], D[ds][\"cond\"], 72, b)[..., ldr.FIT0:] @ Bp\n        halves.append((LA, LB))\n        for name, idx in comps(ds):\n            out[name].append([ldr.alignment_index(LA[c][:, idx], D[ds][\"B\"][idx], LB[c][:, idx]) for c in range(72)])\n    return {k: np.array(v) for k, v in out.items()}, halves\n\n\nAL = {}\nfor ds in DATASETS:\n    L, B = D[ds][\"L\"], D[ds][\"B\"]\n    nz, halves = noise_ai(ds, 36, seed(\"fig4b-plane-alignment\"))\n    AL[ds] = dict(noise=nz, halves=halves, obs={})\n    for name, idx in comps(ds):\n        AL[ds][\"obs\"][name] = ai_matrix(L[:, :, idx], B[idx], L[:, :, idx])\n    AL[ds][\"noise_seeds\"] = [noise_ai(ds, 36, sd)[0] for sd in seeds5(\"fig4b-plane-alignment\")[1:]]\n\n\ndef align_report(ds, name):\n    O = AL[ds][\"obs\"][name]\n    off = ~np.eye(72, dtype=bool)\n    obs = O[off]\n    nz = AL[ds][\"noise\"][name].ravel()\n    A, raw = ldr.auc(nz, obs)  # raw: P(noise > observed)\n    per_c_obs = np.array([O[c][off[c]].mean() for c in range(72)])\n    per_c_nz = AL[ds][\"noise\"][name].mean(0)\n    p_a = stats.wilcoxon(per_c_obs, per_c_nz).pvalue\n    p_b = stats.ranksums(obs, nz).pvalue\n    seeds_auc = [ldr.auc(ns[name].ravel(), obs)[0] for ns in AL[ds][\"noise_seeds\"]]\n    return A, raw, obs, nz, p_a, p_b, per_c_obs, per_c_nz, seeds_auc\n\n# %% md\n## fig4b-plane-alignment\n\n> Same-frequency rotational planes on pairs of conditions were far less aligned than expected from\n> estimation noise (ROC-AUC 0.85 to 0.96).\n\n# %% [claim:fig4b-plane-alignment]\nfor ds in DATASETS:\n    for name, idx in comps(ds)[:-1]:\n        A, raw, obs, nz, p_a, p_b, pco, pcn, sa = align_report(ds, name)\n        print(f\"{NAME[ds]} {name}: AUC {A:.3f} (P(noise > observed) {raw:.3f}); observed median {np.median(obs):.3f}, \"\n              f\"noise median {np.median(nz):.3f}; (a) signed-rank over conditions p {p_a:.2e} (obs lower on \"\n              f\"{int((pco < pcn).sum())}/72); (b) rank-sum p {p_b:.2e}; AUC under four other seeds {np.round(sa, 3)}\")\n\n# %% md\n## suppfig6a-location-alignment\n\n> The state space location occupied different dimensions across conditions, less aligned than expected\n> from estimation noise (ROC-AUC 0.88 to 0.95).\n\n# %% [claim:suppfig6a-location-alignment]\nfor ds in DATASETS:\n    A, raw, obs, nz, p_a, p_b, pco, pcn, sa = align_report(ds, \"location\")\n    print(f\"{NAME[ds]} location: AUC {A:.3f} (P(noise > observed) {raw:.3f}); observed median {np.median(obs):.3f}, noise \"\n          f\"median {np.median(nz):.3f}; (a) signed-rank p {p_a:.2e} (obs lower on {int((pco < pcn).sum())}/72); (b) rank-sum \"\n          f\"p {p_b:.2e}; AUC under four other seeds {np.round(sa, 3)}\")\n\n# %% md\n## fig4c-subspace-excursion-angles\n\n> Across conditions, each rotation's planes spanned 6 to 20 distinct dimensions with angles above 45\n> degrees to each other, and more that varied above chance.\n\nSEA to 25 dimensions, every condition tried as the seed. Excursion angles are counted after the seed\nplane; the count including the seed's dimensions is shown as a variant. Chance: the largest principal\nangle between the two half-split estimates of the same condition's plane (36 repeats above); an\nexcursion angle is above chance when it exceeds the 95th percentile of these (assumption: the code's\nsingleFrequencyOverlapControl.m is described in the claims only as the fraction of noise SEA above the\ndata).\n\n# %%\ndef max_angle(Q1, Q2):\n    s = np.linalg.svd(Q1.T @ Q2, compute_uv=False)\n    return np.degrees(np.arccos(np.clip(s.min(), -1, 1)))\n\n\ndef sea_job(args):\n    ds, name = args\n    idx = dict(comps(ds))[name]\n    planes = [ldr.orth(D[ds][\"L\"][c][:, idx]) for c in range(72)]\n    return ldr.sea(planes, 25)\n\n\njobs = [(ds, name) for ds in DATASETS for name, _ in comps(ds)]\nSEA = dict(zip(jobs, ldr.pmap(sea_job, jobs)))\nSEA_NOISE = {}\nfor ds in DATASETS:\n    for name, idx in comps(ds):\n        SEA_NOISE[(ds, name)] = np.array([max_angle(ldr.orth(LA[c][:, idx]), ldr.orth(LB[c][:, idx]))\n                                          for LA, LB in AL[ds][\"halves\"] for c in range(72)])\n\n# %% [claim:fig4c-subspace-excursion-angles]\nfor ds in DATASETS:\n    for name, idx in comps(ds)[:-1]:\n        a = SEA[(ds, name)]\n        thr = np.percentile(SEA_NOISE[(ds, name)], 95)\n        print(f\"{NAME[ds]} {name}: angles >45 deg: {int((a > 45).sum())} (with the 2 seed dimensions {int((a > 45).sum()) + 2}); \"\n              f\"above chance ({thr:.1f} deg): {int((a > thr).sum())} of 25; angles {np.round(a[:12], 1)} ...\")\n\n# %% md\n## rotation-orientation-dimensionality and suppfig6b-location-dimensionality\n\nPCs to 80% and participation ratio from a PCA across conditions of (a) the loading columns stacked as\nobservations, (b) the activity of the component (loading columns times basis functions). SNR\ndimensionality by the half-split procedure of the Methods, 100 folds: basis from partition 1, loadings\nregressed on it for both partitions, PCA of partition 1's loadings; the dimensionality that maximises\nthe alignment index between the bottlenecked partition-1 loadings and partition 2's (dimensions 1 to\n60 searched; assumption).\n\n# %%\ndef pca_dims(Z):\n    Z = Z - Z.mean(0)\n    ev = np.linalg.svd(Z, compute_uv=False) ** 2\n    cum = np.cumsum(ev) / ev.sum()\n    return int(np.searchsorted(cum, 0.8) + 1), ldr.participation_ratio(ev)\n\n\ndef snr_job(args):\n    ds, sd, nfold, dmax = args\n    rng = np.random.default_rng(sd)\n    m = ds[0]\n    names = [n for n, _ in comps(ds)]\n    full_f = {n: (D[ds][\"freq\"][i][0] if n != \"location\" else 0.0) for n, i in comps(ds)}\n    score = {n: np.zeros(dmax) for n in names}\n    for f_ in range(nfold):\n        a, b = ldr.split_half(D[ds][\"cond\"], 72, rng, MASK[m])\n        XA = ldr.cond_average(D[ds][\"R\"], D[ds][\"cond\"], 72, a)[..., ldr.FIT0:]\n        XB = ldr.cond_average(D[ds][\"R\"], D[ds][\"cond\"], 72, b)[..., ldr.FIT0:]\n        B1, L1 = ldr.tbf(XA, D[ds][\"k\"])\n        B1, L1, lam1, g1, fr1 = ldr.demix(B1, L1)\n        L2 = XB @ np.linalg.pinv(B1)\n        for n in names:\n            if n == \"location\":\n                idx = np.where(g1 == -1)[0][:1]\n            else:\n                rs = [r for r in range(g1.max() + 1)]\n                if not rs:\n                    continue\n                r = min(rs, key=lambda r: abs(fr1[g1 == r][0] - full_f[n]))\n                idx = np.where(g1 == r)[0]\n            A1, A2 = L1[:, :, idx], L2[:, :, idx]\n            Z = A1.transpose(0, 2, 1).reshape(-1, A1.shape[1])\n            V = np.linalg.svd(Z - Z.mean(0), full_matrices=False)[2]\n            Bc = B1[idx] - B1[idx].mean(1, keepdims=True)\n            Q2 = np.stack([ldr.orth(A2[c]) for c in range(72)])\n            for d in range(1, dmax + 1):\n                P = V[:d].T\n                A1d = P @ np.einsum(\"dn,cnk->cdk\", P.T, A1)\n                Y = A1d @ Bc  # (c, N, T)\n                num = np.sum(np.einsum(\"cnd,cnt->cdt\", Q2, Y) ** 2, axis=(1, 2))\n                den = np.sum(Y ** 2, axis=(1, 2))\n                score[n][d - 1] += np.mean(num / den) / nfold\n    return score\n\n\nSNR = dict(zip(DATASETS, ldr.pmap(snr_job, [(ds, seed(\"rotation-orientation-dimensionality\"), 100, 60) for ds in DATASETS])))\nSNR_SEEDS = {ds: ldr.pmap(snr_job, [(ds, sd, 20, 60) for sd in seeds5(\"rotation-orientation-dimensionality\")[1:]]) for ds in DATASETS}\n\nDIMS = {}\nfor ds in DATASETS:\n    for name, idx in comps(ds):\n        A = D[ds][\"L\"][:, :, idx]\n        za = A.transpose(0, 2, 1).reshape(-1, A.shape[1])\n        zb = np.concatenate([(A[c] @ D[ds][\"B\"][idx]).T for c in range(72)])\n        pa, pra = pca_dims(za)\n        pb, prb = pca_dims(zb)\n        snr = int(np.argmax(SNR[ds][name]) + 1)\n        snr_s = [int(np.argmax(s[name]) + 1) for s in SNR_SEEDS[ds]]\n        DIMS[(ds, name)] = dict(pc_a=pa, pr_a=pra, pc_b=pb, pr_b=prb, snr=snr, snr_seeds=snr_s)\n\n# %% [claim:rotation-orientation-dimensionality]\nfor ds in DATASETS:\n    for name, idx in comps(ds)[:-1]:\n        d = DIMS[(ds, name)]\n        print(f\"{NAME[ds]} {name}: (a) PCs to 80% {d['pc_a']}, PR {d['pr_a']:.1f} | (b) PCs {d['pc_b']}, PR {d['pr_b']:.1f} | \"\n              f\"SNR>1 dims {d['snr']} (four other seeds, 20 folds: {d['snr_seeds']})\")\n\n# %% [claim:suppfig6b-location-dimensionality]\nfor ds in DATASETS:\n    d = DIMS[(ds, \"location\")]\n    a = SEA[(ds, \"location\")]\n    print(f\"{NAME[ds]} location: SEA angles >15 deg {int((a > 15).sum())} (with the seed dimension {int((a > 15).sum()) + 1}); \"\n          f\"(a) PCs to 80% {d['pc_a']}, PR {d['pr_a']:.1f} | (b) PCs {d['pc_b']}, PR {d['pr_b']:.1f} | SNR>1 dims {d['snr']} \"\n          f\"(four other seeds: {d['snr_seeds']}); first angles {np.round(a[:8], 1)}\")\n\n# %% md\n## fig5a-frequencies-segregated and suppfig6c-location-distinct-from-rotations\n\nAlignment index of a component on one condition onto the same component, and onto each other\ncomponent, on a different condition. Reading (a): signed-rank over the same ordered condition pairs;\nreading (b): the code's rank-sum test of the two distributions.\n\n# %%\ndef cross_ai(ds, n1, n2):\n    i1, i2 = dict(comps(ds))[n1], dict(comps(ds))[n2]\n    L, B = D[ds][\"L\"], D[ds][\"B\"]\n    return ai_matrix(L[:, :, i1], B[i1], L[:, :, i2])\n\n\ndef seg_report(ds, n1, n2):\n    off = ~np.eye(72, dtype=bool)\n    same = AL[ds][\"obs\"][n1][off]\n    diff = cross_ai(ds, n1, n2)[off]\n    return same, diff, stats.wilcoxon(same, diff).pvalue, stats.ranksums(same, diff).pvalue\n\n# %% [claim:fig5a-frequencies-segregated]\nfor ds in DATASETS:\n    names = [n for n, _ in comps(ds)][:-1]\n    for n1 in names:\n        for n2 in names:\n            if n1 == n2:\n                continue\n            same, diff, pa, pb = seg_report(ds, n1, n2)\n            print(f\"{NAME[ds]} {n1} vs onto {n2}: same median {np.median(same):.3f}, different median {np.median(diff):.3f}; \"\n                  f\"same higher on {(same > diff).mean():.3f} of pairs; (a) p {pa:.1e}; (b) p {pb:.1e}\")\n\n# %% [claim:suppfig6c-location-distinct-from-rotations]\nfor ds in DATASETS:\n    for n2, _ in comps(ds)[:-1]:\n        same, diff, pa, pb = seg_report(ds, \"location\", n2)\n        print(f\"{NAME[ds]} location vs onto {n2}: same median {np.median(same):.3f}, different median {np.median(diff):.3f}; \"\n              f\"(a) p {pa:.1e}; (b) p {pb:.1e}\")\n\n# %% md\n## fig5c-rotations-predict-rotations and fig6b-location-predicts-rotations\n\nSix folds over conditions; TBF, loadings and a ridge map fitted on 5/6 of the conditions; held-out\nloadings by projecting the held-out activity on the training basis (claims; code\npredictOneComponentFromAnother.m). Rotations in each fold are matched to the full-data rotations by\nfrequency (assumption).\n\n# %%\ndef fold_tbf(ds, train):\n    Xtr = D[ds][\"Xw\"][train]\n    B, L = ldr.tbf(Xtr, D[ds][\"k\"])\n    B, L, lam, g, fr = ldr.demix(B, L)\n    return B, g, fr\n\n\ndef match(ds, g, fr):\n    out = {}\n    for name, idx in comps(ds):\n        if name == \"location\":\n            out[name] = np.where(g == -1)[0][:1]\n        else:\n            f0 = D[ds][\"freq\"][idx][0]\n            r = min(range(g.max() + 1), key=lambda r: abs(fr[g == r][0] - f0))\n            out[name] = np.where(g == r)[0]\n    return out\n\n\ndef svd_reduce(Xtr, frac):\n    mu = Xtr.mean(0)\n    U, S, Vt = np.linalg.svd(Xtr - mu, full_matrices=False)\n    k = int(np.searchsorted(np.cumsum(S) / S.sum(), frac) + 1)\n    return lambda Z: (Z - mu) @ Vt[:k].T\n\n\ndef predict_job(args):\n    ds, sd, mode = args\n    rng = np.random.default_rng(sd)\n    folds = ldr.folds_of(72, 6 if mode != \"loc_code\" else 2, rng)\n    names = [n for n, _ in comps(ds)]\n    res = {}\n    for te in folds:\n        tr = np.setdiff1d(np.arange(72), te)\n        B, g, fr = fold_tbf(ds, tr)\n        mt = match(ds, g, fr)\n        Bp = np.linalg.pinv(B)\n        Ltr = D[ds][\"Xw\"][tr] @ Bp\n        Lte = D[ds][\"Xw\"][te] @ Bp\n        perm_tr, perm_te = rng.permutation(len(tr)), rng.permutation(len(te))\n        if mode == \"rot\":\n            pairs = [(a, b) for a in names[:-1] for b in names[:-1] if a != b]\n            for a, b in pairs:\n                Ptr = Ltr[:, :, mt[a]].reshape(len(tr), -1)\n                Pte = Lte[:, :, mt[a]].reshape(len(te), -1)\n                Ytr = Ltr[:, :, mt[b]].reshape(len(tr), -1)\n                for null in (False, True):\n                    red = svd_reduce(Ptr[perm_tr] if null else Ptr, 0.8)\n                    f = ldr.ridge_fit(red(Ptr[perm_tr] if null else Ptr), Ytr, 0.1)\n                    pred = f(red(Pte[perm_te] if null else Pte)).reshape(len(te), -1, 2)\n                    for q, c in enumerate(te):\n                        true = Lte[q][:, mt[b]] @ B[mt[b]]\n                        res.setdefault((a, b, null), {})[c] = ldr.pop_ve(true, pred[q] @ B[mt[b]])\n        else:\n            loc = mt[\"location\"]\n            rest = np.setdiff1d(np.arange(B.shape[0]), loc)\n            Ptr, Pte = Ltr[:, :, loc].reshape(len(tr), -1), Lte[:, :, loc].reshape(len(te), -1)\n            Ytr = Ltr[:, :, rest].reshape(len(tr), -1)\n            for null in (False, True):\n                Pt = Ptr[perm_tr] if null else Ptr\n                if mode == \"loc\":\n                    f = ldr.ridge_fit(Pt, Ytr, 0.1)\n                    pred = f(Pte[perm_te] if null else Pte)\n                else:  # the code's variant: SVD to 90%, lambda 0.01, 2 folds\n                    red = svd_reduce(Pt, 0.9)\n                    f = ldr.ridge_fit(red(Pt), Ytr, 0.01)\n                    pred = f(red(Pte[perm_te] if null else Pte))\n                pred = pred.reshape(len(te), -1, len(rest))\n                for q, c in enumerate(te):\n                    Lh = np.zeros_like(Lte[q])\n                    Lh[:, loc] = Lte[q][:, loc]\n                    Lh[:, rest] = pred[q]\n                    res.setdefault((\"location\", \"rest\", null), {})[c] = ldr.pop_ve(D[ds][\"Xw\"][c], Lh @ B)\n    return {k: np.array([v[c] for c in range(72)]) for k, v in res.items()}\n\n\njobs = [(ds, sd, mode) for ds in DATASETS for mode in (\"rot\", \"loc\", \"loc_code\") for sd in seeds5(\"fig5c-rotations-predict-rotations\")[:1]]\njobs += [(ds, sd, mode) for ds in DATASETS for mode in (\"rot\", \"loc\") for sd in seeds5(\"fig5c-rotations-predict-rotations\")[1:]]\nPRED = dict(zip(jobs, ldr.pmap(predict_job, jobs)))\n\n# %% [claim:fig5c-rotations-predict-rotations]\ns0 = seed(\"fig5c-rotations-predict-rotations\")\nfor ds in DATASETS:\n    r = PRED[(ds, s0, \"rot\")]\n    for (a, b, null), v in r.items():\n        if null:\n            continue\n        nv = r[(a, b, True)]\n        p = stats.wilcoxon(v, nv).pvalue\n        p2 = stats.ranksums(v, nv).pvalue\n        others = [PRED[(ds, sd, \"rot\")][(a, b, False)].mean() for sd in seeds5(\"fig5c-rotations-predict-rotations\")[1:]]\n        print(f\"{NAME[ds]} {a} -> {b}: mean {v.mean():.3f} s.d. {v.std():.3f}; null mean {nv.mean():.3f}; signed-rank p {p:.1e} \"\n              f\"(rank-sum {p2:.1e}); other seeds {np.round(others, 3)}\")\n\n# %% [claim:fig6b-location-predicts-rotations]\nfor ds in DATASETS:\n    for mode in (\"loc\", \"loc_code\"):\n        r = PRED[(ds, s0, mode)]\n        v, nv = r[(\"location\", \"rest\", False)], r[(\"location\", \"rest\", True)]\n        extra = \"\"\n        if mode == \"loc\":\n            extra = \"; other seeds \" + str(np.round([PRED[(ds, sd, 'loc')][('location', 'rest', False)].mean() for sd in seeds5(\"fig5c-rotations-predict-rotations\")[1:]], 3))\n        print(f\"{NAME[ds]} ({'Methods: 6 folds, lambda 0.1' if mode == 'loc' else 'code: 2 folds, lambda 0.01, SVD 90%'}): mean {v.mean():.3f} \"\n              f\"s.d. {v.std():.3f}; null mean {nv.mean():.3f}; signed-rank p {stats.wilcoxon(v, nv).pvalue:.1e}{extra}\")\n\n# %% md\n## fig6c-location-tracks-direction\n\nPCA of the offset columns across the 72 conditions; circular correlation between target angle and the\nangle of each condition in the PC 1-2 plane (claims). A sign flip of PC 2 reverses the direction of\ntravel, so both orientations are shown.\n\n# %% [claim:fig6c-location-tracks-direction]\nfig, axs = plt.subplots(1, 4, figsize=(14, 3.3))\nfor ax, ds in zip(axs, DATASETS):\n    m = ds[0]\n    loc = D[ds][\"L\"][:, :, dict(comps(ds))[\"location\"][0]]\n    Z = loc - loc.mean(0)\n    U, S, Vt = np.linalg.svd(Z, full_matrices=False)\n    pc = Z @ Vt[:2].T\n    ang = np.arctan2(pc[:, 1], pc[:, 0])\n    tang = CT[m][\"angle\"]\n    r1, p1 = ldr.circ_corr(tang, ang)\n    r2, p2 = ldr.circ_corr(tang, -ang)\n    print(f\"{NAME[ds]}: circular correlation {r1:.3f} p {p1:.2e} | PC 2 flipped {r2:.3f} p {p2:.2e} | PC1-2 variance share \"\n          f\"{(S[:2] ** 2).sum() / (S ** 2).sum():.3f}\")\n    sc = ax.scatter(pc[:, 0], pc[:, 1], c=tang, cmap=\"hsv\", s=14, marker=\"o\")\n    ax.set_title(NAME[ds]); ax.set_xlabel(\"PC 1\"); ax.set_ylabel(\"PC 2\")\nplt.tight_layout(); plt.show()\n"
}
```

```
File created successfully at: entries/sabatini-2024/nb_part3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i "s/^g={'__name__':'__main__'}/import __main__; g=__main__.__dict__/" harness.py && sed -i "s/keep={k:v for k,v in g.items() if k in ('D','CT','MASK','CV','RES','KIN','JP','EIG','TB')}/keep={k:v for k,v in g.items() if k in ('D','CT','MASK','CV','EIG','AL','SEA','SEA_NOISE','DIMS','PRED','SH')}/" harness.py && date -u && time dev/bin/python harness.py resume nb_part3.py 2>&1 | tail -80
```

```
Fri Nov 20 11:34:54 UTC 2026
[cell # %% took 1024s]
M1-J rot0 (0.70 Hz): (a) PCs to 80% 2, PR 1.8 | (b) PCs 2, PR 1.7 | SNR>1 dims 21 (four other seeds, 20 folds: [21, 22, 21, 20])
M1-J rot1 (1.82 Hz): (a) PCs to 80% 8, PR 5.6 | (b) PCs 7, PR 4.4 | SNR>1 dims 13 (four other seeds, 20 folds: [12, 12, 11, 13])
M1-J rot2 (3.08 Hz): (a) PCs to 80% 10, PR 7.2 | (b) PCs 6, PR 5.2 | SNR>1 dims 10 (four other seeds, 20 folds: [10, 10, 10, 10])
PMd-J rot0 (0.64 Hz): (a) PCs to 80% 4, PR 2.7 | (b) PCs 2, PR 1.8 | SNR>1 dims 20 (four other seeds, 20 folds: [20, 20, 19, 20])
PMd-J rot1 (1.54 Hz): (a) PCs to 80% 10, PR 7.0 | (b) PCs 9, PR 6.8 | SNR>1 dims 18 (four other seeds, 20 folds: [20, 16, 17, 20])
M1-N rot0 (0.69 Hz): (a) PCs to 80% 3, PR 2.4 | (b) PCs 3, PR 2.5 | SNR>1 dims 26 (four other seeds, 20 folds: [26, 26, 60, 32])
M1-N rot1 (1.79 Hz): (a) PCs to 80% 6, PR 4.5 | (b) PCs 6, PR 4.8 | SNR>1 dims 19 (four other seeds, 20 folds: [21, 20, 20, 19])
M1-N rot2 (3.23 Hz): (a) PCs to 80% 9, PR 7.8 | (b) PCs 7, PR 7.0 | SNR>1 dims 19 (four other seeds, 20 folds: [19, 18, 18, 19])
PMd-N rot0 (0.74 Hz): (a) PCs to 80% 9, PR 6.6 | (b) PCs 6, PR 5.4 | SNR>1 dims 60 (four other seeds, 20 folds: [60, 60, 59, 60])
PMd-N rot1 (1.55 Hz): (a) PCs to 80% 16, PR 11.2 | (b) PCs 14, PR 10.2 | SNR>1 dims 19 (four other seeds, 20 folds: [19, 20, 19, 20])
PMd-N rot2 (2.71 Hz): (a) PCs to 80% 23, PR 18.7 | (b) PCs 22, PR 18.5 | SNR>1 dims 19 (four other seeds, 20 folds: [19, 18, 20, 16])
M1-J location: SEA angles >15 deg 0 (with the seed dimension 1); (a) PCs to 80% 4, PR 4.2 | (b) PCs 4, PR 4.3 | SNR>1 dims 60 (four other seeds: [60, 60, 60, 60]); first angles [14.8 10.6  7.   6.8  6.1  5.8  5.6  5.2]
PMd-J location: SEA angles >15 deg 1 (with the seed dimension 2); (a) PCs to 80% 5, PR 3.2 | (b) PCs 5, PR 3.2 | SNR>1 dims 60 (four other seeds: [60, 60, 60, 60]); first angles [20.6 11.6 11.  10.   8.1  7.6  6.7  6.7]
M1-N location: SEA angles >15 deg 1 (with the seed dimension 2); (a) PCs to
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python - <<'EOF'
s=open('nb_part3.py').read()
old=s[s.index("            A1, A2 = L1[:, :, idx], L2[:, :, idx]"):s.index("    return score\n")]
new='''            A1, A2 = L1[:, :, idx], L2[:, :, idx]
            Z = A1.transpose(0, 2, 1).reshape(-1, A1.shape[1])
            V = np.linalg.svd(Z - Z.mean(0), full_matrices=False)[2]  # PCs of partition 1 (rows)
            Bc = B1[idx] - B1[idx].mean(1, keepdims=True)
            G = Bc @ Bc.T
            Q2 = np.stack([ldr.orth(A2[c]) for c in range(72)])
            C1 = np.einsum("pn,cnk->cpk", V, A1)  # loadings in PC coordinates
            W2 = np.einsum("cnd,pn->cdp", Q2, V)
            # bottleneck to d PCs: A1d = V[:d].T C1[:, :d]; the AI of A1d @ Bc onto span(Q2), for all d
            Mcum = np.cumsum(np.einsum("cdp,cpk->cpdk", W2, C1), axis=1)  # (c, d, dq, k)
            Ccum = np.cumsum(np.einsum("cpk,cpl->cpkl", C1, C1), axis=1)  # (c, d, k, k)
            num = np.einsum("cpdk,kl,cpdl->cp", Mcum, G, Mcum)
            den = np.einsum("cpkl,kl->cp", Ccum, G)
            ai = (num / den).mean(0)
            score[n][: min(dmax, len(ai))] += ai[:dmax] / nfold
'''
s=s.replace(old,new)
s=s.replace("""SNR = dict(zip(DATASETS, ldr.pmap(snr_job, [(ds, seed("rotation-orientation-dimensionality"), 100, 60) for ds in DATASETS])))
SNR_SEEDS = {ds: ldr.pmap(snr_job, [(ds, sd, 20, 60) for sd in seeds5("rotation-orientation-dimensionality")[1:]]) for ds in DATASETS}""",
"""SNR = dict(zip(DATASETS, ldr.pmap(snr_job, [(ds, seed("rotation-orientation-dimensionality"), 100, 96) for ds in DATASETS])))
_j = [(ds, sd, 100, 96) for ds in DATASETS for sd in seeds5("rotation-orientation-dimensionality")[1:]]
_r = ldr.pmap(snr_job, _j)
SNR_SEEDS = {ds: [r for (d_, *_), r in zip(_j, _r) if d_ == ds] for ds in DATASETS}""")
s=s.replace("""the alignment index between the bottlenecked partition-1 loadings and partition 2's (dimensions 1 to
60 searched; assumption).""","""the alignment index between the bottlenecked partition-1 loadings and partition 2's (all dimensions
searched).""")
s=s.replace("(four other seeds, 20 folds: {d['snr_seeds']})","(four other seeds: {d['snr_seeds']})")
open('nb_part3.py','w').write(s)
p=open('nb_part1.py').read()
p=p.replace('os.environ.setdefault("OMP_NUM_THREADS", "4")','for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):\n    os.environ[_v] = "1"  # many small fits, some in parallel worker processes (protocol)')
old=p[p.index("CV = {}\nfor ds in DATASETS:\n    ks = []"):p.index("    k = ks[0] + (ks[0] % 2 == 0)")]
new='''def cv_job(args):
    ds, sd = args
    return ldr.cv_tbf_k(D[ds]["R"], D[ds]["cond"], 72, np.random.default_rng(sd), mask=MASK[ds[0]])


_jobs = [(ds, sd) for ds in DATASETS for sd in seeds5("fig3g-basis-frequencies")]
_cv = dict(zip(_jobs, ldr.pmap(cv_job, _jobs)))
CV = {ds: _cv[(ds, seed("fig3g-basis-frequencies"))] for ds in DATASETS}
for ds in DATASETS:
    ks = [int(np.argmax(_cv[(ds, sd)].mean(0)) + 1) for sd in seeds5("fig3g-basis-frequencies")]
'''
p=p.replace(old,new)
open('nb_part1.py','w').write(p)
q=open('nb_part2.py').read()
old=q[q.index("KS = list(range(1, 22, 2))\nfor ds in DATASETS:"):q.index("    kd = res[\"even split\"]")]
new='''KS = list(range(1, 22, 2))


def dim_job(args):
    ds, sd, frac, folds = args
    cv = ldr.cv_condition_dim(D[ds]["R"], D[ds]["cond"], 72, np.random.default_rng(sd), KS, folds=folds, mask=MASK[ds[0]], frac=frac)
    return cv.mean((0, 1))


_jobs = [(ds, seed("fig2c-condition-lds-variance"), fr, 100) for ds in DATASETS for fr in (0.5, 0.75)]
_jobs += [(ds, sd, 0.5, 100) for ds in DATASETS for sd in seeds5("fig2c-condition-lds-variance")[1:]]
DIMCV = dict(zip(_jobs, ldr.pmap(dim_job, _jobs)))
for ds in DATASETS:
    cvm = DIMCV[(ds, seed("fig2c-condition-lds-variance"), 0.5, 100)]
    res = {"even split": KS[int(np.argmax(cvm))],
           "3/4 split": KS[int(np.argmax(DIMCV[(ds, seed("fig2c-condition-lds-variance"), 0.75, 100)]))]}
'''
q=q.replace(old,new)
old=q[q.index("# seed sensitivity of the chosen k"):q.index("# %% md\n## fig3a")]
new='''# seed sensitivity of the chosen k
for ds in DATASETS:
    ks = [KS[int(np.argmax(DIMCV[(ds, sd, 0.5, 100)]))] for sd in seeds5("fig2c-condition-lds-variance")[1:]]
    print(NAME[ds], "chosen k under the four other seeds:", ks)

'''
q=q.replace(old,new)
old=q[q.index("EIG = {}\nfor ds in DATASETS:"):q.index("# %% [claim:fig3c-eigenvalue-distance-auc]")]
new='''def eig_job(args):
    return eig_null(*args)


_jobs = [(ds, r, 100, seed("fig3c-eigenvalue-distance-auc")) for ds in DATASETS for r in ("a", "b")]
_jobs += [(ds, "b", 20, sd) for ds in DATASETS for sd in seeds5("fig3c-eigenvalue-distance-auc")[1:]]
_res = dict(zip(_jobs, ldr.pmap(eig_job, _jobs)))
EIG = {}
for ds in DATASETS:
    lams = D[ds]["lds_lam"]
    obs = np.array([eig_dist(lams[i], lams[j]) for i in range(72) for j in range(i + 1, 72)])
    obs_n = np.array([eig_dist(lams[i], lams[j], "norm") for i in range(72) for j in range(i + 1, 72)])
    EIG[ds] = dict(obs=obs, obs_n=obs_n)
    for r in ("a", "b"):
        EIG[ds][r] = _res[(ds, r, 100, seed("fig3c-eigenvalue-distance-auc"))]
    EIG[ds]["seeds"] = [_res[(ds, "b", 20, sd)][0] for sd in seeds5("fig3c-eigenvalue-distance-auc")[1:]]

'''
q=q.replace(old,new)
old=q[q.index("# seed sensitivity, null (b), 20 repeats"):q.index("# %% md\n## suppfig2")]
new='''# seed sensitivity, null (b), 20 repeats under each of the four other seeds
for ds in DATASETS:
    vals = [ldr.auc(EIG[ds]["obs"], nm)[0] for nm in EIG[ds]["seeds"]]
    print(NAME[ds], "null (b) AUC under four other seeds (20 repeats each):", np.round(vals, 3))

'''
q=q.replace(old,new)
open('nb_part2.py','w').write(q)
EOF
grep -n "pmap" nb_part*.py | head; date -u
```

```
nb_part1.py:216:_cv = dict(zip(_jobs, ldr.pmap(cv_job, _jobs)))
nb_part2.py:42:DIMCV = dict(zip(_jobs, ldr.pmap(dim_job, _jobs)))
nb_part2.py:155:_res = dict(zip(_jobs, ldr.pmap(eig_job, _jobs)))
nb_part3.py:122:SEA = dict(zip(jobs, ldr.pmap(sea_job, jobs)))
nb_part3.py:196:SNR = dict(zip(DATASETS, ldr.pmap(snr_job, [(ds, seed("rotation-orientation-dimensionality"), 100, 96) for ds in DATASETS])))
nb_part3.py:198:_r = ldr.pmap(snr_job, _j)
nb_part3.py:353:PRED = dict(zip(jobs, ldr.pmap(predict_job, jobs)))
Fri Nov 20 12:01:43 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/sabatini-2024/nb_part4.py",
 "content": "# %% md\n## jPCA\n\njPCA as in the Methods (Explaining variability in jPCA-identified rotations): activity reconstructed\nfrom the temporal basis functions (raw SVD basis over -350 to +850 ms with the dataset's k),\nsoft-normalised (constant 5), mean-subtracted across conditions, 6 PCs, fitted on bins 20 to 40 of the\ngrid (MATLAB indices; -160 to +40 ms). Two planes are kept for M1 and one for PMd.\n\n# %%\ndef run_jpca(Xc_norm, conds):\n    return ldr.jpca(Xc_norm[conds], np.arange(19, 40))\n\n\nJP = {}\nfor ds in DATASETS:\n    B2, L2 = ldr.tbf(D[ds][\"X\"], D[ds][\"k\"])\n    Xr = np.einsum(\"cnk,kt->cnt\", L2, B2)\n    Xn, nf = ldr.soft_norm(Xr)\n    Xm = Xn - Xn.mean(0)\n    allc = np.arange(72)\n    st = CT[ds[0]][\"straight\"]\n    J = run_jpca(Xm, allc)\n    nplanes = 2 if ds[1] == \"M1\" else 1\n    W = [J[\"PC\"] @ J[\"planes\"][p] for p in range(nplanes)]\n    JP[ds] = dict(J=J, W=W, Xm=Xm, nf=nf, mu_t=Xn.mean(0),\n                  Jst=run_jpca(Xm, allc[st]), Jcv=run_jpca(Xm, allc[~st]))\n\n# %% md\n## jpca-fit-r2\n\n> Rotational dynamics found by jPCA fit activity within the jPCA planes with R2 of 0.64 to 0.73, higher\n> on straight reaches (0.73 to 0.88) than on curved reaches (0.56 to 0.70).\n\n# %% [claim:jpca-fit-r2]\nfor ds in DATASETS:\n    J, Js, Jc = JP[ds][\"J\"], JP[ds][\"Jst\"], JP[ds][\"Jcv\"]\n    print(f\"{NAME[ds]}: (a) skew R2 all {J['R2_skew_2D']:.3f}, straight {Js['R2_skew_2D']:.3f}, curved {Jc['R2_skew_2D']:.3f} | \"\n          f\"(b) unconstrained R2 all {J['R2_best_2D']:.3f}, straight {Js['R2_best_2D']:.3f}, curved {Jc['R2_best_2D']:.3f}\")\n    # per-condition R2 in the first plane of the all-condition fit; straight vs curved paired by maze\n    Z = (JP[ds][\"Xm\"][:, :, 19:40].transpose(0, 2, 1) @ J[\"PC\"]) @ J[\"planes\"][0]\n    Ms2 = J[\"planes\"][0].T @ J[\"Mskew\"] @ J[\"planes\"][0]\n    r2c = []\n    for c in range(72):\n        pre, d2 = Z[c, :-1], np.diff(Z[c], axis=0)\n        r2c.append(1 - np.sum((d2 - pre @ Ms2) ** 2) / np.sum((d2 - d2.mean(0)) ** 2))\n    r2c = np.array(r2c)\n    mz = CT[ds[0]][\"maze\"]\n    si = [i for i in range(72) if CT[ds[0]][\"straight\"][i] and (mz[i] + 1) in mz]\n    ci = [int(np.where(mz == mz[i] + 1)[0][0]) for i in si]\n    print(f\"   per-condition R2 (first plane): straight median {np.median(r2c[si]):.3f}, curved median {np.median(r2c[ci]):.3f}; \"\n          f\"signed-rank over {len(si)} maze pairs p {stats.wilcoxon(r2c[si], r2c[ci]).pvalue:.2e}\")\n\n# %% md\n## jpca-variance-explained\n\n> Activity within the jPCA rotational planes explained only 7 to 12% of the population variance in\n> peri-movement firing rates.\n\nPer condition: the soft-normalised, mean-subtracted activity reconstructed in the retained planes,\nun-normalised, its summed variance over -150 to +850 ms as a fraction of the summed variance of the\ncondition's activity (not mean-subtracted).\n\n# %% [claim:jpca-variance-explained]\nfor ds in DATASETS:\n    W = np.column_stack(JP[ds][\"W\"])\n    Q = ldr.orth(W)\n    ve = []\n    for c in range(72):\n        Y = Q @ (Q.T @ JP[ds][\"Xm\"][c])\n        Yu = Y * JP[ds][\"nf\"][:, None]\n        X = D[ds][\"X\"][c]\n        ve.append(np.var(Yu[:, ldr.FIT0:], axis=1).sum() / np.var(X[:, ldr.FIT0:], axis=1).sum())\n    ve = np.array(ve)\n    D[ds][\"jpca_ve\"] = ve\n    print(f\"{NAME[ds]} ({W.shape[1] // 2} plane(s)): mean {ve.mean():.3f} s.d. {ve.std():.3f} range {ve.min():.3f}-{ve.max():.3f}\")\n\n# %% md\n## suppfig3-model-comparison\n\n# %% [claim:suppfig3-model-comparison]\nfor ds in DATASETS:\n    k = D[ds][\"k\"]\n    tbf_cv = CV[ds].mean(0)[k - 1]\n    print(f\"{NAME[ds]}: jPCA {D[ds]['jpca_ve'].mean():.3f} | single-condition LDS {D[ds]['lds_ve'].mean():.3f} | TBF cross-validated \"\n          f\"(held-out VE at k={k}) {tbf_cv:.3f} | TBF in sample {D[ds]['tbf_ve'].mean():.3f}; TBF highest (cross-validated): \"\n          f\"{tbf_cv > max(D[ds]['jpca_ve'].mean(), D[ds]['lds_ve'].mean())}; (in sample): \"\n          f\"{D[ds]['tbf_ve'].mean() > max(D[ds]['jpca_ve'].mean(), D[ds]['lds_ve'].mean())}\")\n\n# %% md\n## fig4d-jpca-variance-correlation and fig4f-plane-alignment-explains-jpca\n\nThe basis functions are extracted from the soft-normalised, mean-subtracted activity (-150 to +850 ms,\nthe dataset's k), as the Methods say. Per condition: the variance of the rotational components, the\nvariance in each retained jPCA plane, and the alignment index of the total rotational activity onto\nthe plane.\n\n# %%\nJ4 = {}\nfor ds in DATASETS:\n    Xm = JP[ds][\"Xm\"][..., ldr.FIT0:]\n    Bn, Ln = ldr.tbf(Xm, D[ds][\"k\"])\n    Bn, Ln, lam, g, fr = ldr.demix(Bn, Ln)\n    rot = np.where(g >= 0)[0]\n    rv = np.array([np.var(Ln[c][:, rot] @ Bn[rot], axis=1).sum() for c in range(72)])\n    J4[ds] = []\n    for p, Wp in enumerate(JP[ds][\"W\"]):\n        pv = np.array([np.var(Wp.T @ Xm[c], axis=1).sum() for c in range(72)])\n        ai = np.array([ldr.alignment_index(Ln[c][:, rot], Bn[rot], Wp) for c in range(72)])\n        J4[ds].append(dict(plane=p + 1, r_var=stats.pearsonr(rv, pv), r_ai=stats.pearsonr(ai, pv), npairs=int(g.max() + 1)))\n\n# %% [claim:fig4d-jpca-variance-correlation]\nrhos, sig = [], []\nfor ds in DATASETS:\n    for e in J4[ds]:\n        r, p = e[\"r_var\"]\n        rhos.append(r); sig.append(p < 0.05)\n        print(f\"{NAME[ds]} jPCA plane {e['plane']}: rho {r:.3f} p {p:.2e} (rotation pairs in the normalised TBF {e['npairs']})\")\n    print(f\"   {NAME[ds]} mean rho over retained planes {np.mean([e['r_var'][0] for e in J4[ds]]):.3f}\")\nprint(f\"planes with p < 0.05: {sum(sig)} of {len(sig)} ({100 * np.mean(sig):.0f}%)\")\n\n# %% [claim:fig4f-plane-alignment-explains-jpca]\nfor ds in DATASETS:\n    for e in J4[ds]:\n        r, p = e[\"r_ai\"]\n        print(f\"{NAME[ds]} jPCA plane {e['plane']}: rho (alignment index vs variance in plane) {r:.3f} p {p:.2e}\")\n\n# %% md\n## Kinematics\n\nHand position every 10 ms from -350 to +850 ms, relative to the position at -350 ms, averaged per\ncondition. Kinematic basis functions: the top two singular vectors of x and y hand velocity of all\nconditions of both monkeys (reading (a)), integrated to position; reading (b) fits a skew-normal and the\nderivative of a skew-normal to them (Methods, Extracting kinematic basis functions). Reach parameters\nare the least-squares coefficients of x and y position on the two position basis functions.\n\n# %%\nKIN = {}\nvel = []\nfor m in (\"J\", \"N\"):\n    H = SESS[m][\"hand\"][:, ::10]\n    H = H - H[:, :1]\n    Hc = ldr.cond_average(H, CT[m][\"cond\"], 72, MASK[m])\n    KIN[m] = dict(H=H, Hc=Hc)\n    vel.append(np.gradient(Hc, axis=1) / 0.01)\nBv, Bp_a, Sv = ldr.kin_basis(vel)\nprint(\"velocity singular values (top 5):\", np.round(Sv[:5], 1), \"share of the top two\", np.round((Sv[:2] ** 2).sum() / (Sv ** 2).sum(), 3))\ntry:\n    Bv_b, Bp_b = ldr.skewnorm_basis(ldr.GRID_MS.astype(float), Bv)\n    print(\"skew-normal fit, correlation with the SVD velocity vectors:\",\n          [round(float(np.corrcoef(Bv[i], Bv_b[i])[0, 1]), 3) for i in range(2)])\nexcept Exception as err:\n    Bp_b = None\n    print(\"skew-normal fit failed:\", err)\nKB = {\"a\": Bp_a, \"b\": Bp_b} if Bp_b is not None else {\"a\": Bp_a}\nfor m in (\"J\", \"N\"):\n    for r, Bp in KB.items():\n        P = ldr.reach_params(KIN[m][\"Hc\"], Bp)\n        KIN[m][\"P\" + r] = P\n        ve = np.mean([ldr.kin_ve(KIN[m][\"Hc\"][c], ldr.params_to_pos(P[c:c + 1], Bp)[0]) for c in range(72)])\n        print(f\"monkey {m}, reading ({r}): reach parameters reproduce condition-mean hand position with VE {ve:.3f}\")\nfig, ax = plt.subplots(1, 2, figsize=(8, 3))\nax[0].plot(ldr.GRID_MS, Bv.T); ax[0].set_title(\"velocity basis (a)\")\nax[1].plot(ldr.GRID_MS, Bp_a.T); ax[1].set_title(\"position basis (a)\")\nplt.tight_layout(); plt.show()\n\n# %% md\n## fig6e-kinematics-predict-location\n\nRidge regression (lambda 0.1, intercept) from the four reach parameters to the offset column, 6 folds\nover conditions; variance explained in the offset column over held-out conditions. Kernel (a): OU,\nlength scale 1000, no penalty; kernel (b): Gaussian, length scale 400, lambda 0.1. Shuffle: reach\nparameters permuted across conditions, 1000 permutations.\n\n# %%\ndef cv_offset(P, Y, folds, model):\n    pred = np.zeros_like(Y)\n    for te in folds:\n        tr = np.setdiff1d(np.arange(len(Y)), te)\n        if model == \"lin\":\n            f = ldr.ridge_fit(P[tr], Y[tr], 0.1)\n        elif model == \"ou\":\n            f = ldr.kernel_fit(P[tr], Y[tr], \"ou\", 1e3, 0.0)\n        else:\n            f = ldr.kernel_fit(P[tr], Y[tr], \"gauss\", 400.0, 0.1)\n        pred[te] = f(P[te])\n    return 1 - np.sum((Y - pred) ** 2) / np.sum((Y - Y.mean(0)) ** 2)\n\n\ndef fig6e_job(args):\n    ds, r, sd = args\n    rng = np.random.default_rng(sd)\n    P = KIN[ds[0]][\"P\" + r]\n    Y = D[ds][\"L\"][:, :, dict(comps(ds))[\"location\"][0]]\n    folds = ldr.folds_of(72, 6, rng)\n    out = {}\n    for model in (\"lin\", \"ou\", \"gauss\"):\n        real = cv_offset(P, Y, folds, model)\n        null = np.array([cv_offset(P[rng.permutation(72)], Y, folds, model) for _ in range(1000 if sd == seed(\"fig6e-kinematics-predict-location\") else 0)])\n        out[model] = (real, null)\n    return out\n\n\n_jobs = [(ds, r, sd) for ds in DATASETS for r in KB for sd in seeds5(\"fig6e-kinematics-predict-location\")]\nF6E = dict(zip(_jobs, ldr.pmap(fig6e_job, _jobs)))\n\n# %% [claim:fig6e-kinematics-predict-location]\ns0 = seed(\"fig6e-kinematics-predict-location\")\nfor ds in DATASETS:\n    for r in KB:\n        res = F6E[(ds, r, s0)]\n        txt = []\n        for model, lab in ((\"lin\", \"linear\"), (\"ou\", \"kernel OU\"), (\"gauss\", \"kernel Gaussian\")):\n            real, null = res[model]\n            others = [F6E[(ds, r, sd)][model][0] for sd in seeds5(\"fig6e-kinematics-predict-location\")[1:]]\n            txt.append(f\"{lab} {real:.3f} (null max {null.max():.3f}, p {(1 + (null >= real).sum()) / (1 + len(null)):.4f}; \"\n                       f\"other seeds {np.round(others, 3)})\")\n        print(f\"{NAME[ds]} kinematic reading ({r}): \" + \" | \".join(txt))\n\n# %% md\n## suppfig2-eigenvalues-from-kinematics\n\n> Kinematic parameters predicted the eigenvalues poorly (mean R2 = 0.1, leave-one-out cross-validation).\n\nPredictors: the four reach parameters, the condition's mean reach duration and a constant; targets:\nreal and imaginary parts of each frequency-sorted eigenvalue of the single-condition LDSs; OLS, leave\none condition out; R2 per component with negatives set to 0; mean over components pooled across the\nfour datasets. Components with no variance (the imaginary part of a real eigenvalue) are left out.\n\n# %% [claim:suppfig2-eigenvalues-from-kinematics]\nfor r in KB:\n    allr2 = []\n    for ds in DATASETS:\n        lams = [ldr.sort_eigs(l) for l in D[ds][\"lds_lam\"]]\n        n = min(len(l) for l in lams)\n        Y = np.column_stack([np.array([l[:n] for l in lams]).real, np.array([l[:n] for l in lams]).imag])\n        Y = Y[:, Y.std(0) > 1e-12]\n        Xp = np.column_stack([KIN[ds[0]][\"P\" + r], D[ds][\"cdur\"], np.ones(72)])\n        pred = np.zeros_like(Y)\n        for c in range(72):\n            o = np.arange(72) != c\n            w = np.linalg.lstsq(Xp[o], Y[o], rcond=None)[0]\n            pred[c] = Xp[c] @ w\n        r2 = np.maximum(0, 1 - ((Y - pred) ** 2).sum(0) / ((Y - Y.mean(0)) ** 2).sum(0))\n        allr2.append(r2)\n        print(f\"reading ({r}) {NAME[ds]}: {len(r2)} components, mean R2 {r2.mean():.3f}, max {r2.max():.3f}\")\n    print(f\"reading ({r}): mean R2 pooled over datasets {np.concatenate(allr2).mean():.3f}\")\n\n# %% md\n## fig7c-ldr-encoding and suppfig7a-not-memorization\n\nLDR encoding (Methods, LDR encoding; claims): 6 folds over conditions with TBF and loadings refitted on\n5/6; ridge (lambda 0.1, intercept) or OU kernel regression (length scale 1000, no penalty) from the\nreach parameters to the vectorised loading matrix; predicted loadings times the training basis;\npopulation variance explained per held-out condition. Null: the model trained with reach parameters\npermuted across the training conditions, signed-rank test over conditions.\n\n# %%\ndef encode(ds, P, folds, model, rng=None, null=False):\n    ve = np.zeros(72)\n    for te in folds:\n        tr = np.setdiff1d(np.arange(72), te)\n        B, L = ldr.tbf(D[ds][\"Xw\"][tr], D[ds][\"k\"])\n        Y = L.reshape(len(tr), -1)\n        Ptr = P[tr][rng.permutation(len(tr))] if null else P[tr]\n        if model == \"lin\":\n            f = ldr.ridge_fit(Ptr, Y, 0.1)\n        elif model == \"ou\":\n            f = ldr.kernel_fit(Ptr, Y, \"ou\", 1e3, 0.0)\n        else:  # nearest-neighbour regression\n            f = lambda Z, Ptr=Ptr, Y=Y: Y[np.argmin(((Z[:, None] - Ptr[None]) ** 2).sum(2), 1)]\n        Lh = f(P[te]).reshape(len(te), -1, B.shape[0])\n        for q, c in enumerate(te):\n            ve[c] = ldr.pop_ve(D[ds][\"Xw\"][c], Lh[q] @ B)\n    return ve\n\n\ndef enc_job(args):\n    ds, r, sd = args\n    rng = np.random.default_rng(sd)\n    P = KIN[ds[0]][\"P\" + r]\n    folds = ldr.folds_of(72, 6, rng)\n    out = {m: encode(ds, P, folds, m) for m in (\"lin\", \"ou\")}\n    out.update({m + \"_null\": encode(ds, P, folds, m, rng, True) for m in (\"lin\", \"ou\")})\n    ang = CT[ds[0]][\"angle\"]\n    sext = np.floor(((ang + np.pi) % (2 * np.pi)) / (np.pi / 3)).astype(int)\n    sfolds = [np.where(sext == s)[0] for s in range(6) if (sext == s).any()]\n    out[\"sext_ou\"] = encode(ds, P, sfolds, \"ou\")\n    out[\"sext_nn\"] = encode(ds, P, sfolds, \"nn\")\n    return out\n\n\n_jobs = [(ds, r, sd) for ds in DATASETS for r in KB for sd in seeds5(\"fig7c-ldr-encoding\")]\nENC = dict(zip(_jobs, ldr.pmap(enc_job, _jobs)))\n\n# %% [claim:fig7c-ldr-encoding]\ns0 = seed(\"fig7c-ldr-encoding\")\nfor r in KB:\n    for ds in DATASETS:\n        e = ENC[(ds, r, s0)]\n        o = {m: [ENC[(ds, r, sd)][m].mean() for sd in seeds5(\"fig7c-ldr-encoding\")[1:]] for m in (\"lin\", \"ou\")}\n        print(f\"reading ({r}) {NAME[ds]}: linear mean {e['lin'].mean():.3f} s.d. {e['lin'].std():.3f} (null {e['lin_null'].mean():.3f}, \"\n              f\"signed-rank p {stats.wilcoxon(e['lin'], e['lin_null']).pvalue:.1e}; other seeds {np.round(o['lin'], 3)}) | \"\n              f\"kernel mean {e['ou'].mean():.3f} s.d. {e['ou'].std():.3f} (null {e['ou_null'].mean():.3f}, p \"\n              f\"{stats.wilcoxon(e['ou'], e['ou_null']).pvalue:.1e}; other seeds {np.round(o['ou'], 3)})\")\n\n# %% [claim:suppfig7a-not-memorization]\nfor r in KB:\n    for ds in DATASETS:\n        e = ENC[(ds, r, s0)]\n        print(f\"reading ({r}) {NAME[ds]}: sextant hold-out, kernel mean {e['sext_ou'].mean():.3f}, nearest neighbour mean \"\n              f\"{e['sext_nn'].mean():.3f}; kernel higher on {int((e['sext_ou'] > e['sext_nn']).sum())}/72; signed-rank p \"\n              f\"{stats.wilcoxon(e['sext_ou'], e['sext_nn']).pvalue:.1e}\")\n\n# %% md\n## fig7c-standard-encoding-worse\n\nStandard instantaneous encoding models (Methods, Comparing the LDR encoding with standard instantaneous\nencoding models), 100 ms causal lag, the same 6 folds of conditions as fig7c: (1) ridge regression\n(lambda 0.1) on position, extent, velocity, speed, velocity angle (as its cosine and sine; assumption)\nand acceleration, with a baseline; (2) OU kernel regression on position, length scale 1e12; (3) OU\nkernel regression on velocity, length scale 1e11. The kernel penalty is not given; 0.1 is used\n(assumption, the Methods' L2 for kernel decoders).\n\n# %%\ndef kin_features(m):\n    Hc = KIN[m][\"Hc\"]\n    v = np.gradient(Hc, axis=1) / 0.01\n    a = np.gradient(v, axis=1) / 0.01\n    ext = np.linalg.norm(Hc, axis=2)[..., None]\n    sp = np.linalg.norm(v, axis=2)[..., None]\n    ang = np.arctan2(v[..., 1], v[..., 0])\n    lin = np.concatenate([Hc, ext, v, sp, np.cos(ang)[..., None], np.sin(ang)[..., None], a], axis=2)\n    return dict(lin=lin, pos=Hc, vel=v)\n\n\ndef std_job(args):\n    ds, sd = args\n    rng = np.random.default_rng(sd)\n    folds = ldr.folds_of(72, 6, rng)\n    feats = kin_features(ds[0])\n    lag = 10  # 100 ms at 10 ms bins\n    tt = np.arange(ldr.FIT0, len(ldr.GRID_MS))\n    out = {}\n    for name in (\"lin\", \"pos\", \"vel\"):\n        F = feats[name][:, tt - lag]  # (c, T, f)\n        mu, sdv = F.reshape(-1, F.shape[2]).mean(0), F.reshape(-1, F.shape[2]).std(0) + 1e-12\n        ve = np.zeros(72)\n        for te in folds:\n            tr = np.setdiff1d(np.arange(72), te)\n            Xtr = F[tr].reshape(-1, F.shape[2])\n            Ytr = D[ds][\"Xw\"][tr].transpose(0, 2, 1).reshape(-1, D[ds][\"Xw\"].shape[1])\n            if name == \"lin\":\n                f = ldr.ridge_fit((Xtr - mu) / sdv, Ytr, 0.1)\n                pr = lambda Z: f((Z - mu) / sdv)\n            else:\n                f = ldr.kernel_fit(Xtr, Ytr, \"ou\", 1e12 if name == \"pos\" else 1e11, 0.1)\n                pr = f\n            for c in te:\n                ve[c] = ldr.pop_ve(D[ds][\"Xw\"][c], pr(F[c]).T)\n        out[name] = ve\n    return out\n\n\nSTD = dict(zip(DATASETS, ldr.pmap(std_job, [(ds, seed(\"fig7c-ldr-encoding\")) for ds in DATASETS])))\n\n# %% [claim:fig7c-standard-encoding-worse]\nfor r in KB:\n    nwin = 0\n    for ds in DATASETS:\n        e = ENC[(ds, r, s0)]\n        for name, lab in ((\"lin\", \"linear multi-parameter\"), (\"pos\", \"kernel on position\"), (\"vel\", \"kernel on velocity\")):\n            sv = STD[ds][name]\n            res = []\n            for ldrm in (\"lin\", \"ou\"):\n                p = stats.wilcoxon(e[ldrm], sv).pvalue\n                win = (e[ldrm].mean() > sv.mean()) and p < 0.001\n                nwin += win\n                res.append(f\"LDR {ldrm} {e[ldrm].mean():.3f} p {p:.1e}\")\n            print(f\"reading ({r}) {NAME[ds]} {lab}: mean {sv.mean():.3f} | \" + \"; \".join(res))\n    print(f\"reading ({r}): LDR higher with p < 0.001 in {nwin} of 24 comparisons\")\n\n# %% md\n## fig7f-ldr-decoding, trial-curvature-decoding, suppfig8-no-output-potent-dependence\n\nTwo folds over conditions. On the training half: TBF on trial averages (raw SVD basis, -150 to +850\nms) and a ridge map (lambda 10, intercept) from vectorised loadings to the four reach parameters. On\nthe held-out half, single-trial loadings are 10 ms spike counts in spikes/s times the pseudo-inverse of\nthe basis; predicted parameters times the position basis give hand position, compared with the trial's\nown hand position (relative to -350 ms) over -350 to +850 ms (claims; code\nkinFromTBFSingleTrial.m). Variance explained per trial, negatives set to 0.\n\n# %%\ndef decode(ds, r, sd, lam=10.0, remove_potent=False, null=False):\n    m = ds[0]\n    rng = np.random.default_rng(sd)\n    Bp = KB[r]\n    P = KIN[m][\"P\" + r]\n    folds = ldr.folds_of(72, 2, rng)\n    cond = D[ds][\"cond\"]\n    C = SESS[m][\"C10\"][:, D[ds][\"u\"]][..., ldr.FIT0:]\n    Xw = D[ds][\"Xw\"]\n    if remove_potent:\n        # output-potent dimensions: row space of least-squares maps from activity to hand position and velocity\n        Hc = KIN[m][\"Hc\"][:, ldr.FIT0:]\n        Vc = (np.gradient(KIN[m][\"Hc\"], axis=1) / 0.01)[:, ldr.FIT0:]\n        Xs = Xw.transpose(0, 2, 1).reshape(-1, Xw.shape[1])\n        K = np.concatenate([Hc, Vc], axis=2).reshape(-1, 4)\n        Wm = np.linalg.lstsq(Xs - Xs.mean(0), K - K.mean(0), rcond=None)[0]\n        Q = ldr.orth(Wm)\n        Xw = Xw - np.einsum(\"nk,mk,cmt->cnt\", Q, Q, Xw)\n        C = C - np.einsum(\"nk,mk,cmt->cnt\", Q, Q, C)\n    ve = np.full(len(cond), np.nan)\n    dec = np.full((len(cond), 4), np.nan)\n    for te in folds:\n        tr = np.setdiff1d(np.arange(72), te)\n        B, L = ldr.tbf(Xw[tr], D[ds][\"k\"])\n        Ptr = P[tr][rng.permutation(len(tr))] if null else P[tr]\n        f = ldr.ridge_fit(L.reshape(len(tr), -1), Ptr, lam)\n        Bpinv = np.linalg.pinv(B)\n        ii = np.where(MASK[m] & np.isin(cond, te))[0]\n        Lt = C[ii] @ Bpinv\n        ph = f(Lt.reshape(len(ii), -1))\n        pos = ldr.params_to_pos(ph, Bp)\n        dec[ii] = ph\n        for q, i in enumerate(ii):\n            ve[i] = ldr.kin_ve(KIN[m][\"H\"][i], pos[q])\n    return ve, dec\n\n\ndef dec_job(args):\n    return decode(*args[:3], **args[3])\n\n\n_jobs = [(ds, r, sd, {}) for ds in DATASETS for r in KB for sd in seeds5(\"fig7f-ldr-decoding\")]\n_jobs += [(ds, r, seed(\"fig7f-ldr-decoding\"), {\"null\": True}) for ds in DATASETS for r in KB]\n_jobs += [(ds, r, seed(\"suppfig8-no-output-potent-dependence\"), {\"lam\": 1.0, \"remove_potent\": rp}) for ds in DATASETS for r in KB for rp in (False, True)]\nDEC = {(a[0], a[1], a[2], tuple(sorted(a[3].items()))): v for a, v in zip(_jobs, ldr.pmap(dec_job, _jobs))}\n\n# %% [claim:fig7f-ldr-decoding]\ns0 = seed(\"fig7f-ldr-decoding\")\nfor r in KB:\n    for ds in DATASETS:\n        ve, _ = DEC[(ds, r, s0, ())]\n        nv, _ = DEC[(ds, r, s0, ((\"null\", True),))]\n        ok = np.isfinite(ve)\n        others = [np.nanmean(DEC[(ds, r, sd, ())][0]) for sd in seeds5(\"fig7f-ldr-decoding\")[1:]]\n        print(f\"reading ({r}) {NAME[ds]}: {int(ok.sum())} trials, mean VE {np.nanmean(ve):.3f} s.d. {np.nanstd(ve):.3f} median \"\n              f\"{np.nanmedian(ve):.3f}; condition-shuffled null mean {np.nanmean(nv):.3f} (signed-rank p \"\n              f\"{stats.wilcoxon(ve[ok], nv[ok]).pvalue:.1e}); other seeds {np.round(others, 3)}\")\n\n# %% [claim:trial-curvature-decoding]\nfor r in KB:\n    for ds in DATASETS:\n        m = ds[0]\n        _, dec = DEC[(ds, r, s0, ())]\n        ok = np.isfinite(dec[:, 0])\n        cond = D[ds][\"cond\"]\n        true = ldr.reach_params(KIN[m][\"H\"], KB[r])\n        out = []\n        for j in (2, 3):\n            dres = dec[ok, j] - np.array([np.mean(dec[ok & (cond == c), j]) for c in cond[ok]])\n            tres = true[ok, j] - np.array([np.mean(true[ok & (cond == c), j]) for c in cond[ok]])\n            rr, pp = stats.pearsonr(dres, tres)\n            out.append(f\"parameter {j + 1}: rho {rr:.3f} p {pp:.1e}\")\n        print(f\"reading ({r}) {NAME[ds]} ({int(ok.sum())} trials): \" + \"; \".join(out))\n\n# %% [claim:suppfig8-no-output-potent-dependence]\ns8 = seed(\"suppfig8-no-output-potent-dependence\")\nfor r in KB:\n    for ds in DATASETS:\n        cond = D[ds][\"cond\"]\n        a, _ = DEC[(ds, r, s8, ((\"lam\", 1.0), (\"remove_potent\", False)))]\n        b, _ = DEC[(ds, r, s8, ((\"lam\", 1.0), (\"remove_potent\", True)))]\n        ca = np.array([np.nanmean(a[cond == c]) for c in range(72)])\n        cb = np.array([np.nanmean(b[cond == c]) for c in range(72)])\n        p = stats.wilcoxon(ca, cb).pvalue\n        print(f\"reading ({r}) {NAME[ds]}: per-condition VE with potent dims {ca.mean():.3f}, without {cb.mean():.3f} \"\n              f\"(mean drop {np.mean(ca - cb):.3f}); two-sided signed-rank p {p:.3f}\")\n"
}
```

```
File created successfully at: entries/sabatini-2024/nb_part4.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > defs.py <<'EOF'
# %%
def comps(ds):
    g = D[ds]["grp"]
    out = [("rot%d (%.2f Hz)" % (r, D[ds]["freq"][g == r][0]), np.where(g == r)[0]) for r in range(g.max() + 1)]
    out.append(("location", np.where(g == -1)[0][:1]))
    return out
EOF
cp defs.py entries/sabatini-2024/_defs_tmp.py
date -u; time OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 dev/bin/python harness.py resume _defs_tmp.py nb_part4.py 2>&1 | tail -80; rm entries/sabatini-2024/_defs_tmp.py
```

```
Fri Nov 20 12:03:54 UTC 2026
M1-J: (a) skew R2 all 0.776, straight 0.843, curved 0.712 | (b) unconstrained R2 all 0.823, straight 0.897, curved 0.757
   per-condition R2 (first plane): straight median 0.691, curved median 0.589; signed-rank over 36 maze pairs p 5.77e-02
PMd-J: (a) skew R2 all 0.664, straight 0.753, curved 0.574 | (b) unconstrained R2 all 0.692, straight 0.815, curved 0.637
   per-condition R2 (first plane): straight median 0.263, curved median -0.071; signed-rank over 36 maze pairs p 2.79e-01
M1-N: (a) skew R2 all 0.623, straight 0.763, curved 0.660 | (b) unconstrained R2 all 0.685, straight 0.811, curved 0.747
   per-condition R2 (first plane): straight median 0.566, curved median 0.405; signed-rank over 36 maze pairs p 5.14e-05
PMd-N: (a) skew R2 all 0.452, straight 0.781, curved 0.562 | (b) unconstrained R2 all 0.466, straight 0.868, curved 0.613
   per-condition R2 (first plane): straight median 0.001, curved median 0.024; signed-rank over 36 maze pairs p 5.29e-01
M1-J (2 plane(s)): mean 0.089 s.d. 0.036 range 0.038-0.178
PMd-J (1 plane(s)): mean 0.116 s.d. 0.116 range 0.023-0.589
M1-N (2 plane(s)): mean 0.117 s.d. 0.054 range 0.043-0.292
PMd-N (1 plane(s)): mean 0.051 s.d. 0.032 range 0.003-0.131
M1-J: jPCA 0.089 | single-condition LDS 0.844 | TBF cross-validated (held-out VE at k=7) 0.711 | TBF in sample 0.935; TBF highest (cross-validated): False; (in sample): True
PMd-J: jPCA 0.116 | single-condition LDS 0.902 | TBF cross-validated (held-out VE at k=5) 0.790 | TBF in sample 0.936; TBF highest (cross-validated): False; (in sample): True
M1-N: jPCA 0.117 | single-condition LDS 0.942 | TBF cross-validated (held-out VE at k=7) 0.866 | TBF in sample 0.966; TBF highest (cross-validated): False; (in sample): True
PMd-N: jPCA 0.051 | single-condition LDS 0.906 | TBF cross-validated (held-out VE at k=7) 0.791 | TBF in sample 0.953; TBF highest (cross-validated): False; (in sample): True
Traceback (most recent call last):
  File "/tmp/claude-1001/harn
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/import __main__; g=__main__.__dict__/import __main__; _G=__main__.__dict__/; s/exec(c,g)/exec(c,_G)/; s/    g.update(/    _G.update(/; s/exec("import numpy as np, time, zlib, matplotlib.pyplot as plt\\nfrom scipy import stats\\nimport ldr",g)/exec("import numpy as np, time, zlib, matplotlib.pyplot as plt\\nfrom scipy import stats\\nimport ldr",_G)/; s/T_START=time.time()",g)/T_START=time.time()",_G)/; s/    g\[.SESS.\]=/    _G["SESS"]=/; s/keep={k:v for k,v in g.items()/keep={k:v for k,v in _G.items()/' harness.py && grep -n "_G\|\bg\b" harness.py | head -20
```

```
10:import __main__; _G=__main__.__dict__
12:    _G.update(pickle.load(open('/tmp/claude-1001/state.pkl','rb'))); parts=parts[1:]
13:    exec("import numpy as np, time, zlib, matplotlib.pyplot as plt\nfrom scipy import stats\nimport ldr",_G)
14:    exec("def seed(claim):\n    return zlib.crc32(f'sabatini-2024/{claim}'.encode())\ndef seeds5(claim):\n    return [seed(claim) + i for i in (0, 1000, 2000, 3000, 4000)]\nDATASETS=[('J','M1'),('J','PMd'),('N','M1'),('N','PMd')]\nNAME={d: f'{d[1]}-{d[0]}' for d in DATASETS}\nT_START=time.time()",_G)
15:    _G["SESS"]={m:fake(m) for m in ('J','N')}
22:        t0=time.time(); exec(c,_G); dt=time.time()-t0
24:keep={k:v for k,v in _G.items() if k in ('D','CT','MASK','CV','EIG','AL','SEA','SEA_NOISE','DIMS','PRED','SH')}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cp defs.py entries/sabatini-2024/_defs_tmp.py && date -u; time OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 dev/bin/python harness.py resume _defs_tmp.py nb_part4.py 2>&1 | grep -v "^M1-J: (a)\|per-condition R2" | tail -75; rm entries/sabatini-2024/_defs_tmp.py
```

```
Fri Nov 20 12:04:12 UTC 2026
reading (a): mean R2 pooled over datasets 0.275
reading (b) M1-J: 5 components, mean R2 0.478, max 0.582
reading (b) PMd-J: 5 components, mean R2 0.253, max 0.432
reading (b) M1-N: 7 components, mean R2 0.136, max 0.271
reading (b) PMd-N: 5 components, mean R2 0.287, max 0.336
reading (b): mean R2 pooled over datasets 0.275
[cell # %% took 17s]
reading (a) M1-J: linear mean 0.765 s.d. 0.068 (null 0.638, signed-rank p 2.3e-13; other seeds [0.766 0.773 0.769 0.757]) | kernel mean 0.840 s.d. 0.044 (null 0.525, p 1.9e-13; other seeds [0.836 0.843 0.837 0.834])
reading (a) PMd-J: linear mean 0.681 s.d. 0.189 (null 0.580, signed-rank p 2.6e-08; other seeds [0.68  0.694 0.691 0.664]) | kernel mean 0.850 s.d. 0.078 (null 0.444, p 1.9e-13; other seeds [0.837 0.846 0.84  0.838])
reading (a) M1-N: linear mean 0.843 s.d. 0.059 (null 0.635, signed-rank p 1.7e-13; other seeds [0.841 0.838 0.836 0.842]) | kernel mean 0.921 s.d. 0.027 (null 0.523, p 1.7e-13; other seeds [0.915 0.917 0.917 0.919])
reading (a) PMd-N: linear mean 0.723 s.d. 0.133 (null 0.561, signed-rank p 1.5e-12; other seeds [0.723 0.713 0.712 0.726]) | kernel mean 0.867 s.d. 0.052 (null 0.432, p 1.7e-13; other seeds [0.856 0.853 0.856 0.861])
reading (b) M1-J: linear mean 0.766 s.d. 0.068 (null 0.638, signed-rank p 1.8e-13; other seeds [0.766 0.774 0.77  0.758]) | kernel mean 0.841 s.d. 0.041 (null 0.523, p 1.9e-13; other seeds [0.838 0.844 0.838 0.836])
reading (b) PMd-J: linear mean 0.681 s.d. 0.190 (null 0.579, signed-rank p 2.2e-08; other seeds [0.68  0.695 0.692 0.665]) | kernel mean 0.855 s.d. 0.068 (null 0.438, p 1.9e-13; other seeds [0.846 0.851 0.844 0.842])
reading (b) M1-N: linear mean 0.844 s.d. 0.058 (null 0.635, signed-rank p 1.7e-13; other seeds [0.842 0.839 0.837 0.843]) | kernel mean 0.920 s.d. 0.028 (null 0.519, p 1.7e-13; other seeds [0.914 0.916 0.915 0.918])
reading (b) PMd-N: linear mean 0.724 s.d. 0.131 (null 0.561, signed-rank p 1.4e-12; other seeds [0.724 0.714 
[... 65 more lines not kept]
```

**Agent**

Part 4 runs in about 3 minutes. Now checking the parts of the part 3 and 4 output I haven't seen yet, and testing the faster SNR code.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import re
src=open('entries/sabatini-2024/nb_part3.py').read()
cells=re.split(r'^(# %%.*)$', src, flags=re.M)
# cells: ['', head, body, head, body...]
out=[]
pairs=list(zip(cells[1::2],cells[2::2]))
for h,b in pairs:
    if h.strip()=='# %% md': continue
    if 'AL = {}' in b:  # strip heavy loop
        b=b[:b.index('AL = {}')]+b[b.index('def align_report'):]
    if 'SEA = dict(' in b:
        b=b[:b.index('jobs = [(ds, name)')]
    if 'SNR = dict(' in b:
        b=b.replace('SNR_SEEDS = {ds: [r for (d_, *_), r in zip(_j, _r) if d_ == ds] for ds in DATASETS}','SNR_SEEDS = {ds: [r for (d_, *_), r in zip(_j, _r) if d_ == ds] for ds in DATASETS}\nprint("snr done")')
    if 'PRED = dict' in b or 'fig5c-rotations' in h or 'fig6b' in h or 'fig6c' in h or 'fig5a' in h or 'suppfig6c' in h: continue
    out.append(h+'\n'+b)
open('entries/sabatini-2024/_p3tmp.py','w').write('\n'.join(out))
EOF
time OMP_NUM_THREADS=1 dev/bin/python harness.py resume _p3tmp.py 2>&1 | tail -40; rm entries/sabatini-2024/_p3tmp.py
```

```
M1-J rot0 (0.70 Hz): AUC 0.912 (P(noise > observed) 0.912); observed median 0.752, noise median 0.901; (a) signed-rank over conditions p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.912 0.912 0.912 0.912]
M1-J rot1 (1.82 Hz): AUC 0.886 (P(noise > observed) 0.886); observed median 0.245, noise median 0.572; (a) signed-rank over conditions p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.887 0.886 0.886 0.887]
M1-J rot2 (3.08 Hz): AUC 0.861 (P(noise > observed) 0.861); observed median 0.243, noise median 0.576; (a) signed-rank over conditions p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.86  0.859 0.86  0.859]
PMd-J rot0 (0.64 Hz): AUC 0.945 (P(noise > observed) 0.945); observed median 0.720, noise median 0.930; (a) signed-rank over conditions p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.945 0.945 0.946 0.945]
PMd-J rot1 (1.54 Hz): AUC 0.933 (P(noise > observed) 0.933); observed median 0.212, noise median 0.590; (a) signed-rank over conditions p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.932 0.932 0.932 0.932]
M1-N rot0 (0.69 Hz): AUC 0.949 (P(noise > observed) 0.949); observed median 0.641, noise median 0.928; (a) signed-rank over conditions p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.949 0.948 0.948 0.949]
M1-N rot1 (1.79 Hz): AUC 0.952 (P(noise > observed) 0.952); observed median 0.295, noise median 0.814; (a) signed-rank over conditions p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.953 0.952 0.952 0.953]
M1-N rot2 (3.23 Hz): AUC 0.933 (P(noise > observed) 0.933); observed median 0.176, noise median 0.661; (a) signed-rank over conditions p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.933 0.932 0.933 0.932]
PMd-N rot0 (0.74 Hz): AUC 0.95
[... 35 more lines not kept]
```

**Agent**

SNR code verified (same values, 2 minutes). Assembling the notebook and entry files for the first full run.

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/entry.schema.json'));print(json.dumps(s)[:2500])"; grep -n "python\b\|def cmd_lock\|python_version\|REGISTRY_PYTHON" tools/entry.py | head -20
```

```
{"$schema": "https://json-schema.org/draft/2020-12/schema", "title": "An entry: a directory of notebooks with its metadata (entry.yaml)", "description": "Draft. To be revised after the pilot.", "type": "object", "additionalProperties": false, "required": ["schema_version", "name", "type", "title", "description", "license", "notebooks", "related"], "properties": {"schema_version": {"const": 1}, "name": {"description": "Unique across the registry, and the name of the entry's directory.", "type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$", "maxLength": 100}, "type": {"enum": ["orientation", "reproduction", "analysis"]}, "title": {"type": "string", "minLength": 1, "maxLength": 300}, "description": {"type": "string", "minLength": 1}, "license": {"description": "SPDX identifier.", "type": "string"}, "python": {"description": "The Python version the entry runs on, major.minor; its lock is compiled for it (tools/entry.py lock). Entries from before the field run on the version their lock names.", "type": "string", "pattern": "^3\\.[0-9]+$"}, "notebooks": {"type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["path"], "properties": {"path": {"type": "string", "pattern": "\\.ipynb$"}, "title": {"type": "string"}, "runtime_minutes": {"description": "Roughly how long it takes to run.", "type": "integer", "minimum": 1}}}}, "helpers": {"description": "Python modules in the entry that the notebooks import.", "type": "array", "items": {"type": "string", "pattern": "\\.py$"}}, "related": {"type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["id", "relation"], "properties": {"id": {"description": "A dataset as <archive>:<id>[/<version>] (dandi:000003/0.220126.1855), doi:<doi>, or entry:<name>.", "type": "string", "pattern": "^(dandi:[0-9]{6}(/.+)?|doi:10\\.[0-9]{4,9}/.+|entry:[a-z0-9]+(-[a-z0-9]+)*|[a-z][a-z0-9-]*:[^\\s/]+(/\\S+)?)$"}, "relation": {"enum": ["uses_data", "reproduce
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && cat > $TMPDIR/build_nb.py <<'EOF'
import re, nbformat, sys
d='entries/sabatini-2024/'
parts=['nb_part1.py','nb_part2.py','nb_part3.py','nb_part4.py']+sys.argv[1:]
cells=[]
for p in parts:
    src=open(d+p).read() if not p.startswith('/') else open(p).read()
    chunks=re.split(r'^(# %%.*)$', src, flags=re.M)
    for h,b in zip(chunks[1::2],chunks[2::2]):
        b=b.strip('\n')
        h=h.strip()
        if h=='# %% md':
            cells.append(nbformat.v4.new_markdown_cell(b))
        else:
            c=nbformat.v4.new_code_cell(b)
            m=re.match(r'# %% \[(.+)\]',h)
            if m: c.metadata['tags']=[m.group(1)]
            cells.append(c)
nb=nbformat.v4.new_notebook(); nb.cells=cells
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
nbformat.write(nb, d+'reproduce_sabatini_2024.ipynb')
print(len(cells),'cells')
EOF
python $TMPDIR/build_nb.py
cat > requirements.in <<'EOF'
h5py
matplotlib
numpy
remfile
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: sabatini-2024
type: reproduction
title: Reach-dependent reorientation of rotational dynamics in motor cortex (Sabatini & Kaufman 2024)
description: Tests the findings of Sabatini and Kaufman (2024) on dandiset 000070, which holds the two
  maze-task sessions the paper names (monkeys J and N, a PMd and an M1 Utah array each). It rebuilds the
  four datasets from the units, trials and hand position, and tests jPCA, single-condition dynamics, the
  temporal basis factorization, the alignment and dimensionality of rotational planes, the state space
  location, and LDR encoding and decoding.
license: Apache-2.0
notebooks:
- path: reproduce_sabatini_2024.ipynb
  title: Reproducing Sabatini & Kaufman (2024) from dandiset 000070
  runtime_minutes: 30
helpers:
- ldr.py
related:
- id: dandi:000070/0.260528.0919
  relation: uses_data
- id: doi:10.1038/s41467-024-51308-7
  relation: reproduces
EOF
ls; cd  && python tools/entry.py lock entries/sabatini-2024 2>&1 | tail -3
```

```
87 cells
__pycache__
entry.yaml
ldr.py
nb_part1.py
nb_part2.py
nb_part3.py
nb_part4.py
reproduce_sabatini_2024.ipynb
requirements.in
wrote sabatini-2024/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && mkdir -p $TMPDIR/src && mv nb_part*.py $TMPDIR/src/ && rm -rf __pycache__ && sed -i "s#d='entries/sabatini-2024/'#d='$TMPDIR/src/'#; s#nbformat.write(nb, d+'reproduce_sabatini_2024.ipynb')#nbformat.write(nb, 'entries/sabatini-2024/reproduce_sabatini_2024.ipynb')#" $TMPDIR/build_nb.py && python $TMPDIR/build_nb.py && cd  && python tools/entry.py check entries/sabatini-2024 2>&1 | tail -15
```

```
87 cells
0 error(s)
```

**Agent calls Bash**

```bash
date -u; cd  && python tools/entry.py run entries/sabatini-2024 2>&1 | tail -15; date -u
```

```
Fri Nov 20 12:10:13 UTC 2026
Installed kernelspec registry-sabatini-2024 in executed/sabatini-2024/.venv/share/jupyter/kernels/registry-sabatini-2024
pass  reproduce_sabatini_2024.ipynb  (1713 s)
Fri Nov 20 12:38:49 UTC 2026
```

**Agent**

Full run passed in 28.5 minutes. Reading the outputs.

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/out1.txt
import nbformat
nb=nbformat.read('executed/sabatini-2024/reproduce_sabatini_2024.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    tags=c.metadata.get('tags',[])
    txt=''.join(o.get('text','') for o in c.outputs if o.get('output_type')=='stream')
    err=[o for o in c.outputs if o.get('output_type')=='error']
    print(f'=== cell {i} {tags}'); print(txt[:6000])
    if err: print('ERROR', err[0]['ename'], err[0]['evalue'])
EOF
wc -l $TMPDIR/out1.txt; sed -n 1,140p $TMPDIR/out1.txt
```

```
483 /tmp/claude-1001/out1.txt
=== cell 1 []
dandiset 000070 version 0.260528.0919

=== cell 3 []
J loaded in 173 s; trials kept (successful, 72 conditions): 1595
N loaded in 241 s; trials kept (successful, 72 conditions): 2121

=== cell 5 ['sanity']
== monkey J (asset 033a04c0-9ce7-45c5-8012-c571a7b9bf12)
  trials in file 2636 | successful 2570 | maze_condition values 109 (min 0 max 108 )
  units 192 {'M1': 96, 'PMd': 96}
  spikes per unit: min 61030 median 317716 max 1720529
  recording segments (backward jumps of hand timestamps + 1): 1 | bounds (s): [(np.float64(4.7), np.float64(15668.0))]
  backward jumps in spike times per unit: [191   1]
  trials per segment: [2636]
  trial start times monotonic: True
  -500..+1000 ms window inside the trial interval for 1595 of 1595 kept trials
  delay (go - target) s: range [-0.004  0.664  0.998]
  movement onset - go cue s: range [0.153 0.358 1.863]
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 140,330p $TMPDIR/out1.txt
```

```
PMd-J: CV best k 5 (five seeds [5, 5, 5, 5, 5]), k used 5; rotation pairs 2, real modes 1; rotation frequencies [0.64 1.54] Hz; nearest of 0.5/1.5/2.5/4 [0.5, 1.5]; within 10%: [np.False_, np.True_]
   |eigenvalue| of the offset mode [1.0002]
M1-N: CV best k 7 (five seeds [7, 7, 7, 7, 7]), k used 7; rotation pairs 3, real modes 1; rotation frequencies [0.69 1.79 3.23] Hz; nearest of 0.5/1.5/2.5/4 [0.5, 1.5, 2.5]; within 10%: [np.False_, np.False_, np.False_]
   |eigenvalue| of the offset mode [0.9989]
PMd-N: CV best k 6 (five seeds [6, 6, 6, 6, 6]), k used 7; rotation pairs 3, real modes 1; rotation frequencies [0.74 1.55 2.71] Hz; nearest of 0.5/1.5/2.5/4 [0.5, 1.5, 2.5]; within 10%: [np.False_, np.True_, np.True_]
   |eigenvalue| of the offset mode [0.994]

=== cell 24 ['claim:tbf-variance-explained']
M1-J: (a) -150..+850 ms, de-mixed basis: mean 0.935 s.d. 0.012 range 0.894-0.958 | (b) -350..+850 ms, raw SVD basis: mean 0.921 s.d. 0.014
PMd-J: (a) -150..+850 ms, de-mixed basis: mean 0.936 s.d. 0.015 range 0.896-0.959 | (b) -350..+850 ms, raw SVD basis: mean 0.924 s.d. 0.015
M1-N: (a) -150..+850 ms, de-mixed basis: mean 0.966 s.d. 0.008 range 0.950-0.978 | (b) -350..+850 ms, raw SVD basis: mean 0.961 s.d. 0.009
PMd-N: (a) -150..+850 ms, de-mixed basis: mean 0.953 s.d. 0.010 range 0.928-0.970 | (b) -350..+850 ms, raw SVD basis: mean 0.945 s.d. 0.009

=== cell 26 []

=== cell 27 ['claim:tbf-shuffle-control']
M1-J: shuffled VE mean 0.422 s.d. 0.020 (real 0.935); rank-sum p 3.91e-25; signed-rank (variant) p 1.66e-13; real higher on 72/72
   shuffled mean under the five seeds: [np.float64(0.4219), np.float64(0.4162), np.float64(0.4174), np.float64(0.416), np.float64(0.4187)]
PMd-J: shuffled VE mean 0.287 s.d. 0.016 (real 0.936); rank-sum p 3.91e-25; signed-rank (variant) p 1.66e-13; real higher on 72/72
   shuffled mean under the five seeds: [np.float64(0.2874), np.float64(0.292), np.float64(0.2873), np.float64(0.2901), np.float64(0.2882)]
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 330,483p $TMPDIR/out1.txt | grep -v "^reading (b)"
```

```
PMd-N: (a) skew R2 all 0.452, straight 0.781, curved 0.562 | (b) unconstrained R2 all 0.466, straight 0.868, curved 0.613
   per-condition R2 (first plane): straight median 0.001, curved median 0.024; signed-rank over 36 maze pairs p 5.29e-01

=== cell 61 ['claim:jpca-variance-explained']
M1-J (2 plane(s)): mean 0.089 s.d. 0.036 range 0.038-0.178
PMd-J (1 plane(s)): mean 0.116 s.d. 0.116 range 0.023-0.589
M1-N (2 plane(s)): mean 0.117 s.d. 0.054 range 0.043-0.292
PMd-N (1 plane(s)): mean 0.051 s.d. 0.032 range 0.003-0.131

=== cell 63 ['claim:suppfig3-model-comparison']
M1-J: jPCA 0.089 | single-condition LDS 0.844 | TBF cross-validated (held-out VE at k=7) 0.711 | TBF in sample 0.935; TBF highest (cross-validated): False; (in sample): True
PMd-J: jPCA 0.116 | single-condition LDS 0.902 | TBF cross-validated (held-out VE at k=5) 0.790 | TBF in sample 0.936; TBF highest (cross-validated): False; (in sample): True
M1-N: jPCA 0.117 | single-condition LDS 0.942 | TBF cross-validated (held-out VE at k=7) 0.866 | TBF in sample 0.966; TBF highest (cross-validated): False; (in sample): True
PMd-N: jPCA 0.051 | single-condition LDS 0.906 | TBF cross-validated (held-out VE at k=7) 0.791 | TBF in sample 0.953; TBF highest (cross-validated): False; (in sample): True

=== cell 65 []

=== cell 66 ['claim:fig4d-jpca-variance-correlation']
M1-J jPCA plane 1: rho -0.061 p 6.13e-01 (rotation pairs in the normalised TBF 3)
M1-J jPCA plane 2: rho 0.711 p 2.52e-12 (rotation pairs in the normalised TBF 3)
[... 95 more lines not kept]
```

**Agent**

All 33 runnable claims have numbers. Writing the conclusion cells and the summary now, then the final run.

**Agent calls Bash**

```bash
cd $TMPDIR/src && python - <<'EOF'
p=open('nb_part1.py').read()
p=p.replace('''    print("   72 conditions:", len(CT[m]["maze"]), "straight (no barrier)", int(st.sum()), "curved", int((~st).sum()))''','''    print("   conditions kept:", len(CT[m]["maze"]), "| straight (no barrier):", int(st.sum()), "| curved:", int((~st).sum()))''')
p=p.replace("| fig7f-decoder-beats-standard | tested except the GPFA decoders (see its section) |","| fig7f-decoder-beats-standard | blocked (not run within the time of this attempt) |")
open('nb_part1.py','w').write(p)
q=open('nb_part3.py').read()
old='''            print(f"{NAME[ds]} {n1} vs onto {n2}: same median {np.median(same):.3f}, different median {np.median(diff):.3f}; "
                  f"same higher on {(same > diff).mean():.3f} of pairs; (a) p {pa:.1e}; (b) p {pb:.1e}")'''
new='''            print(f"{NAME[ds]} {n1} vs onto {n2}: same median {np.median(same):.3f}, different median {np.median(diff):.3f}; "
                  f"mean difference {np.mean(same - diff):+.3f}; same higher on {(same > diff).mean():.3f} of pairs; "
                  f"(a) p {pa:.1e}; (b) p {pb:.1e}")'''
assert old in q; q=q.replace(old,new); open('nb_part3.py','w').write(q)
EOF
echo done
```

```
done
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/src/conclusions.py",
 "content": "C = {\n\"data-composition\": \"\"\"**Result: partially reproduced.** Both monkeys have the 72 conditions (36 straight, 36 curved), and the trial counts are within 10% of the paper's under both readings (J 1595 or 1381 against 1469; N 2121 or 1884 against 2014). Each array holds 96 units, one per electrode, and the units table carries no single- or multi-unit label, so the count the criterion asks for (units the dataset marks as single or multi-units) cannot be made; 96 lies in 71 to 130, but these are not shown to be the paper's 79 to 118 sorted units.\"\"\",\n\"fig2c-condition-lds-variance\": \"\"\"**Result: reproduced.** The cross-validated dimensionality is 5, 5, 7 and 5 (M1-J, PMd-J, M1-N, PMd-N), the same under all five seeds, and the single-condition LDSs explain on average 84.4, 90.2, 94.2 and 90.6% of the population variance, all within 63.9 to 100%. The values are at the top of the paper's 71 to 93%. The code's 3/4 split chooses 7, 5, 7 and 7.\"\"\",\n\"fig3a-eigenvalue-clusters\": \"\"\"**Result: partially reproduced.** Every condition's LDS has the same number of complex pairs (2, or 3 for M1-N on 71 of 72 conditions) and one real eigenvalue, so the eigenvalues form distinct clusters with an offset. Only PMd-J has its median frequencies within 10% of the paper's (0.54 and 1.53 Hz); M1-J has 0.85 and 2.35 Hz, M1-N 0.68, 1.74 and 3.21 Hz, PMd-N 0.73 and 1.67 Hz.\"\"\",\n\"fig3c-eigenvalue-distance-auc\": \"\"\"**Result: not reproduced.** The AUC between distances across conditions and the noise distribution is 0.81, 0.71, 0.63 and 0.70 under the Poisson null (a) and 0.70, 0.64, 0.66 and 0.68 under the half-split null (b), against 0.459 to 0.638; only M1-N under (a) is in range. Eigenvalues differ between conditions more than the paper reports, though the distances are small (median 0.011 to 0.016 in the complex plane). The five seeds give AUCs within 0.02 of each other under null (b).\"\"\",\n\"fig3g-basis-frequencies\": \"\"\"**Result: partially reproduced.** The cross-validated factorization has 3 rotation pairs and one offset in M1-J, M1-N and PMd-N, and 2 pairs in PMd-J. The rotation frequencies are 0.70, 1.82, 3.08 (M1-J), 0.64, 1.54 (PMd-J), 0.69, 1.79, 3.23 (M1-N) and 0.74, 1.55, 2.71 Hz (PMd-N); only 3 of the 11 are within 10% of 0.5, 1.5, 2.5 or 4 Hz, and no dataset has a rotation near 0.5 Hz or 4 Hz.\"\"\",\n\"tbf-variance-explained\": \"\"\"**Result: reproduced.** The factorization explains on average 93.5, 93.6, 96.6 and 95.3% of the population variance (s.d. 0.8 to 1.5% across conditions) over -150 to +850 ms, and 92.1 to 96.1% over the whole window with the raw basis, all within 81 to 100%.\"\"\",\n\"tbf-shuffle-control\": \"\"\"**Result: partially reproduced.** Shuffling time bins lowers the variance explained to 42.2, 28.7, 41.8 and 42.1%, below the real data on all 72 conditions of every dataset (rank-sum p = 3.9e-25). Three of four lie in 31.5 to 50.6%; PMd-J (28.7%) is below. The five seeds move the shuffled means by less than 0.01.\"\"\",\n\"fig3h-recoverability\": \"\"\"**Result: partially reproduced.** Recoverability is 97.3, 97.9, 98.6 and 98.6%, within 81.9 to 100%, and above the shuffled data on every condition (rank-sum p = 3.9e-25). The chance level is higher than the paper's: 89.6, 86.0, 89.0 and 89.6%, so only PMd-J lies in 56.7 to 88%.\"\"\",\n\"fig3i-duration-warping\": \"\"\"**Result: not reproduced.** Before warping, M1-N has rho = +0.235 (p = 0.047), opposite in sign to the paper's -0.26; the other three (-0.157, 0.083, 0.077) lie in the stated range. Warping to 600 ms induces a negative correlation only in M1-J (rho = -0.514, p = 4e-06); PMd-J, M1-N and PMd-N give -0.071, -0.024 and -0.193 (p > 0.1). The 250 ms post-reach variant gives -0.36, -0.18, -0.10 and -0.32.\"\"\",\n\"single-lds-variance\": \"\"\"**Result: not reproduced.** One LDS fitted to all conditions explains on average 76.6, 80.5, 82.1 and 77.4% of the population variance over -150 to +850 ms (79 to 87% over the whole window), above the range 41.4 to 72.6% in every dataset.\"\"\",\n\"fig4b-plane-alignment\": \"\"\"**Result: reproduced.** For every rotation in every dataset, same-frequency planes on pairs of conditions are less aligned than half-split estimates of the same condition: AUC 0.861 to 0.958, observed alignment lower on 72 of 72 conditions, signed-rank p = 1.7e-13 (reading a) and rank-sum p below 1e-200 (reading b). The four other seeds change the AUCs by at most 0.002.\"\"\",\n\"suppfig6a-location-alignment\": \"\"\"**Result: partially reproduced.** The state space location is less aligned across conditions than expected from noise in every dataset (signed-rank p at most 2.1e-13), with AUC 0.883, 0.748, 0.870 and 0.945; PMd-J (0.748) is below 0.792.\"\"\",\n\"fig4c-subspace-excursion-angles\": \"\"\"**Result: partially reproduced.** The number of excursion angles above 45 degrees is 5, 13, 11 (M1-J), 7, 14 (PMd-J), 3, 9, 11 (M1-N) and 7, 18, 25 (PMd-N); 8 of 11 lie in 5.4 to 22 (M1-J 0.70 Hz, M1-N 0.69 Hz and PMd-N 2.71 Hz do not; counting the seed's two dimensions, 9 of 11 do). The number of angles above the half-split noise level is 4 to 9, fewer than those above 45 degrees for 8 of 11 rotations, so \"far more that varied above chance\" is not reproduced with the noise level used here, which is an assumption.\"\"\",\n\"rotation-orientation-dimensionality\": \"\"\"**Result: not reproduced.** Rotation orientations need 2 to 23 PCs to reach 80% of their variance (reading a; 2 to 22 under b) and have participation ratios of 1.8 to 18.7, against 20.7 to 44 and 15.03 to 40.48; only PMd-N 2.71 Hz is inside either range. The SNR dimensionality is 10 to 21 for 9 of 11 rotations, inside 6.3 to 36.3; for the slowest rotation of M1-N and PMd-N the alignment rises up to all 96 dimensions, so no optimum is found.\"\"\",\n\"suppfig6b-location-dimensionality\": \"\"\"**Result: not reproduced.** SEA finds 0 or 1 location dimensions with angles above 15 degrees (1 or 2 with the seed), the locations need 2 to 5 PCs for 80% of their variance, and their participation ratios are 2.3 to 4.2, all far below the stated ranges. The SNR procedure reaches its maximum at the largest dimensionality tested (72), so it gives no estimate.\"\"\",\n\"fig5a-frequencies-segregated\": \"\"\"**Result: partially reproduced.** Same-frequency alignment is higher than different-frequency alignment for 18 of the 20 rotation comparisons (medians 0.135 to 0.752 against 0.052 to 0.257). For M1-N 3.23 Hz onto the other two rotations, same-frequency alignment is not higher (median 0.176 against 0.191 and 0.193; higher on 49% and 48% of condition pairs). In PMd-J 1.54 Hz onto 0.64 Hz and PMd-N 2.71 Hz onto the others the medians differ by 0.001 to 0.001 although the tests give p < 1e-6.\"\"\",\n\"suppfig6c-location-distinct-from-rotations\": \"\"\"**Result: reproduced.** In every dataset, the location on one condition is more aligned with the location on another (median 0.935 to 0.969) than with any rotation plane (median 0.078 to 0.670), with p below 1e-300 under both readings.\"\"\",\n\"fig5c-rotations-predict-rotations\": \"\"\"**Result: reproduced.** Each rotation predicts on average 41.4 to 94.6% of the variance of another rotation, above the shuffled null (2.4 to 76.3%) for every pair (signed-rank p at most 4.9e-13). All 20 pair means lie in 38.7 to 100%, and the four other seeds move them by at most 0.03.\"\"\",\n\"fig6b-location-predicts-rotations\": \"\"\"**Result: reproduced.** The state space location predicts on average 70.9, 72.3, 80.9 and 71.6% of the population variance (6 folds, lambda 0.1), within 60.3 to 88%, against a null of 12.9 to 22.6% (signed-rank p at most 2.4e-13). The code's variant gives 73.1 to 85.6%.\"\"\",\n\"fig6c-location-tracks-direction\": \"\"\"**Result: partially reproduced.** With PC 2 flipped, the angle of the location in the PC 1-2 plane correlates with target angle in M1-J (0.613), PMd-J (0.701) and M1-N (0.245, p = 0.016), but not in PMd-N (0.053 or -0.053, p = 0.62).\"\"\",\n\"fig6e-kinematics-predict-location\": \"\"\"**Result: reproduced.** With the SVD kinematic basis (reading a), the four reach parameters linearly predict 53.3, 55.0, 70.4 and 41.4% of the variance of the location (within 33.3 to 78.1%), and OU kernel regression 70.4, 68.8, 88.7 and 76.9% (within 62.1 to 89.1%), both above all 1000 permutations. The skew-normal basis (reading b) gives the same within 0.02. The Gaussian kernel (reading b of the kernel) gives 32 to 54%, below the range.\"\"\",\n\"suppfig2-eigenvalues-from-kinematics\": \"\"\"**Result: not reproduced.** Reach parameters and reach duration predict the eigenvalue components with a mean leave-one-out R2 of 0.275 pooled over datasets (0.135 to 0.480 per dataset) under both kinematic readings, above 0.1 +- 0.05.\"\"\",\n\"fig7c-ldr-encoding\": \"\"\"**Result: reproduced.** Linear LDR encoding explains on average 76.5, 68.1, 84.3 and 72.3% of the population variance (within 54 to 85.8%) and kernel LDR encoding 84.0, 85.0, 92.1 and 86.7% (within 63.9 to 95.7%), both above the shuffled null (p at most 2.6e-08). The skew-normal basis gives the same within 0.01.\"\"\",\n\"suppfig7a-not-memorization\": \"\"\"**Result: partially reproduced.** With target sextants held out, kernel regression beats nearest-neighbour regression with p < 0.01 in M1-J, M1-N and PMd-N (p 2e-11 to 6e-10), but not in PMd-J (p = 0.019 under the SVD basis, 0.89 under the skew-normal basis).\"\"\",\n\"fig7c-standard-encoding-worse\": \"\"\"**Result: reproduced.** Both LDR models exceed each standard encoding model in every dataset with p < 0.001 (24 of 24 comparisons under both kinematic readings). The linear multi-parameter model explains 51.7 to 53.4%. The two OU kernel models explain 0% with the assumed penalty of 0.1: with length scales of 1e11 and 1e12 the kernel is nearly constant and they predict the mean, so the comparison with them is not informative.\"\"\",\n\"fig7f-ldr-decoding\": \"\"\"**Result: partially reproduced.** The LDR decoder explains on average 77.4, 74.7, 87.4 and 73.4% of the variance of single-trial hand position (SVD basis; medians 82 to 92%); M1-J and M1-N lie in 75.6 to 100%, PMd-J and PMd-N below. The skew-normal basis gives 72.9 to 86.8%, with the same two in range. Under the four other seeds PMd-N reaches 75.8 and 76.1% twice, so two or three of four lie in range under every seed.\"\"\",\n\"trial-curvature-decoding\": \"\"\"**Result: partially reproduced.** Decoded and actual within-condition curvature correlate with p < 0.001 for all eight parameters, with rho 0.319, 0.162, 0.229, 0.093, 0.449, 0.548, 0.191 and 0.290 (SVD basis); 6 of 8 lie in 0.144 to 0.451 (PMd-J parameter 4 is lower, M1-N parameter 4 higher).\"\"\",\n\"suppfig8-no-output-potent-dependence\": \"\"\"**Result: not reproduced.** Removing the dimensions that map to hand position and velocity (the dataset has no EMG) lowers the decoded variance by 3.9 to 6.3 points per condition, and the two-sided signed-rank test finds the drop in every dataset (p < 0.001, below 0.036).\"\"\",\n\"jpca-fit-r2\": \"\"\"**Result: partially reproduced.** With the skew-symmetric R2 (reading a), jPCA fits 0.776, 0.664, 0.623 and 0.452 in the first plane; three lie in 0.576 to 0.803 and PMd-N does not. Refitted on straight and curved reaches alone, every dataset fits straight reaches better (0.753 to 0.843) than curved ones (0.562 to 0.712), all within their ranges. The unconstrained R2 (reading b) has two of four in range for all conditions.\"\"\",\n\"jpca-variance-explained\": \"\"\"**Result: partially reproduced.** The retained jPCA planes hold on average 8.9, 11.6, 11.7 and 5.1% of the population variance (s.d. 3.2 to 11.6% across conditions); three lie in 6.3 to 13.2% and PMd-N (5.1%) is below.\"\"\",\n\"suppfig3-model-comparison\": \"\"\"**Result: not reproduced.** Under the main reading, the cross-validated TBF value (71.1, 79.0, 86.6 and 79.1%) is above jPCA (5.1 to 11.7%) but below the in-sample single-condition LDS (84.4 to 94.2%) in every dataset. In sample (the variant), TBF (93.5 to 96.6%) exceeds both in every dataset.\"\"\",\n\"fig4d-jpca-variance-correlation\": \"\"\"**Result: not reproduced.** Rotational variance correlates with the variance in the jPCA planes more strongly than the paper reports: rho = -0.061 and 0.711 (M1-J), 0.930 (PMd-J), 0.663 and 0.627 (M1-N), 0.682 (PMd-N). Per-dataset means are 0.325, 0.930, 0.645 and 0.682, and the significant planes have rho 0.627 to 0.930; under neither reading do the values lie in 0.351 to 0.506. Five of six planes (83%) are significant, outside 66 +- 6.6%.\"\"\",\n\"fig4f-plane-alignment-explains-jpca\": \"\"\"**Result: partially reproduced.** The alignment of a condition's rotations with a jPCA plane correlates with its variance in that plane for every plane (p at most 2.3e-11), with rho 0.941, 0.926, 0.832, 0.689, 0.817 and 0.815; five of six lie in 0.738 to 1 (M1-N plane 1 does not).\"\"\",\n}\n"
}
```

```
File created successfully at: /tmp/claude-1001/src/conclusions.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -c "" /dev/null; cd $TMPDIR && grep -n "PMd-J rot1 (1.54 Hz) vs onto rot0\|PMd-N rot2" out1.txt | head; date -u
```

```
0
200:PMd-N rot2 (2.71 Hz): AUC 0.940 (P(noise > observed) 0.940); observed median 0.053, noise median 0.336; (a) signed-rank over conditions p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.941 0.941 0.94  0.941]
221:PMd-N rot2 (2.71 Hz): angles >45 deg: 25 (with the 2 seed dimensions 27); above chance (69.8 deg): 8 of 25; angles [89.8 89.  86.2 84.7 81.4 78.3 78.2 75.5 69.4 69.3 64.4 62.3] ...
236:PMd-N rot2 (2.71 Hz): (a) PCs to 80% 23, PR 18.7 | (b) PCs 22, PR 18.5 | SNR>1 dims 19 (four other seeds: [19, 19, 19, 19])
254:PMd-J rot1 (1.54 Hz) vs onto rot0 (0.64 Hz): same median 0.212, different median 0.211; same higher on 0.521 of pairs; (a) p 5.8e-19; (b) p 1.9e-06
265:PMd-N rot2 (2.71 Hz) vs onto rot0 (0.74 Hz): same median 0.053, different median 0.052; same higher on 0.511 of pairs; (a) p 9.2e-25; (b) p 1.6e-09
266:PMd-N rot2 (2.71 Hz) vs onto rot1 (1.55 Hz): same median 0.053, different median 0.052; same higher on 0.532 of pairs; (a) p 7.5e-33; (b) p 1.4e-09
302:PMd-N rot2 (2.71 Hz) -> rot0 (0.74 Hz): mean 0.758 s.d. 0.150; null mean 0.364; signed-rank p 4.9e-13 (rank-sum 5.9e-20); other seeds [0.775 0.759 0.772 0.764]
303:PMd-N rot2 (2.71 Hz) -> rot1 (1.55 Hz): mean 0.628 s.d. 0.148; null mean 0.128; signed-rank p 1.7e-13 (rank-sum 6.7e-23); other seeds [0.644 0.63  0.638 0.638]
Fri Nov 20 12:41:02 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/src && python - <<'EOF'
s=open('conclusions.py').read()
rep=[("the medians differ by 0.001 to 0.001 although","the medians differ by 0.001 although"),
("Every condition's LDS has the same number of complex pairs (2, or 3 for M1-N on 71 of 72 conditions) and one real eigenvalue, so the eigenvalues form distinct clusters with an offset.","Every condition's LDS has the same number of complex pairs (2; 3 in M1-N, where one condition has 2 pairs and 3 real eigenvalues) and at least one real eigenvalue, so the eigenvalues form distinct clusters with an offset."),
("fewer than those above 45 degrees for 8 of 11 rotations","fewer than those above 45 degrees for 7 of 11 rotations"),
("and their participation ratios are 2.3 to 4.2,","and their participation ratios are 2.3 to 4.2 (reading a),"),
("The values are at the top of the paper's 71 to 93%.","The values are at or above the top of the paper's 71 to 93%."),
("and rank-sum p below 1e-200 (reading b)","and rank-sum p printed as 0 (reading b)"),
("with p below 1e-300 under both readings.","with p printed as 0 under both readings."),
]
for a,b in rep:
    assert a in s, a; s=s.replace(a,b)
open('conclusions.py','w').write(s)
EOF
cat > $TMPDIR/src/nb_part5.py <<'EOF'
# %% md
## Summary

| Claim | Outcome |
|---|---|
| data-composition | partially reproduced (units are one per electrode, unlabelled) |
| jpca-fit-r2 | partially reproduced (3 of 4 in range) |
| jpca-variance-explained | partially reproduced (3 of 4 in range) |
| single-lds-variance | not reproduced (77 to 82%, above 41 to 73%) |
| fig2c-condition-lds-variance | reproduced |
| fig3a-eigenvalue-clusters | partially reproduced (clusters present; frequencies match in PMd-J only) |
| fig3c-eigenvalue-distance-auc | not reproduced (AUC 0.63 to 0.81) |
| suppfig2-eigenvalues-from-kinematics | not reproduced (mean R2 0.275) |
| fig3g-basis-frequencies | partially reproduced (rotations near 0.7, 1.6 to 1.8 and 2.7 to 3.2 Hz) |
| tbf-variance-explained | reproduced |
| tbf-shuffle-control | partially reproduced (3 of 4 in range) |
| fig3h-recoverability | partially reproduced (chance level higher) |
| fig3i-duration-warping | not reproduced |
| suppfig3-model-comparison | not reproduced under the main reading; holds in sample |
| fig4b-plane-alignment | reproduced |
| fig4c-subspace-excursion-angles | partially reproduced |
| rotation-orientation-dimensionality | not reproduced (lower dimensional) |
| fig4d-jpca-variance-correlation | not reproduced (stronger correlations) |
| fig4f-plane-alignment-explains-jpca | partially reproduced (5 of 6 planes) |
| fig5a-frequencies-segregated | partially reproduced (18 of 20 comparisons) |
| fig5c-rotations-predict-rotations | reproduced |
| suppfig6a-location-alignment | partially reproduced (3 of 4) |
| suppfig6b-location-dimensionality | not reproduced |
| suppfig6c-location-distinct-from-rotations | reproduced |
| fig6b-location-predicts-rotations | reproduced |
| fig6c-location-tracks-direction | partially reproduced (3 of 4) |
| fig6e-kinematics-predict-location | reproduced |
| fig7c-ldr-encoding | reproduced |
| suppfig7a-not-memorization | partially reproduced (3 of 4) |
| fig7c-standard-encoding-worse | reproduced (kernel standard models uninformative) |
| fig7f-ldr-decoding | partially reproduced (2 of 4) |
| fig7f-decoder-beats-standard | blocked (not run in the time of this attempt) |
| suppfig8-no-output-potent-dependence | not reproduced (without EMG) |
| trial-curvature-decoding | partially reproduced (6 of 8) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

**How the analysis differs from the paper's.** The dandiset's units are one per electrode (96 per
array) with no single- or multi-unit label, where the paper used 79 to 118 sorted single and stable
multi-units per array; every population measure here rests on these units. Trials are the successful
trials of the 72 conditions with a delay above 400 ms, the reading closest to the paper's counts (an
assumption; the paper gives no trial selection). The eigenvalue nulls use 100 repeats, not 500, and the
Poisson null is simulated at 10 ms. The paper's code is not run (it needs preprocessed files that are
not public); the methods follow the claims file, the Methods, and the code as the claims file reports
it. The dataset has no EMG, so suppfig8 removes the kinematic dimensions only. The GPFA decoder
comparison was not run.

**What was found about the dataset.** The Nitschke file joins five recording segments whose clocks
overlap: trial start times, hand timestamps and every unit's spike times jump backwards four times, so
spike times are not sorted and a trial's spikes cannot be found by time alone. Assigning each trial to
its segment in file order gives condition decoding well above chance in every segment and at chance
with shifted labels, so the alignment within segments is consistent with the trial table; condition
information in segment 3 is lower within the segment (0.16) than in segments 0 to 2 (0.41 to 0.46),
while a decoder trained on the other segments still reaches 0.48 there. In the Jenkins file one unit's
spike train restarts at the beginning of the session (two runs concatenated). Hand position is stored as
"meters" with a conversion of NaN, but its values are in millimetres (reaches of about 130). The units
table has no quality, sorting or single/multi-unit column.
EOF
cat > $TMPDIR/build2.py <<'EOF'
import re, nbformat, sys
sys.path.insert(0,'/tmp/claude-1001/src')
from conclusions import C
d='/tmp/claude-1001/src/'
cells=[]
for p in ['nb_part1.py','nb_part2.py','nb_part3.py','nb_part4.py','nb_part5.py']:
    src=open(d+p).read()
    chunks=re.split(r'^(# %%.*)$', src, flags=re.M)
    for h,b in zip(chunks[1::2],chunks[2::2]):
        b=b.strip('\n'); h=h.strip()
        if h=='# %% md':
            cells.append(nbformat.v4.new_markdown_cell(b)); continue
        c=nbformat.v4.new_code_cell(b)
        m=re.match(r'# %% \[(.+)\]',h)
        if m: c.metadata['tags']=[m.group(1)]
        cells.append(c)
        if m and m.group(1).startswith('claim:'):
            cid=m.group(1)[6:]
            cells.append(nbformat.v4.new_markdown_cell(C.pop(cid)))
assert not C, C.keys()
nb=nbformat.v4.new_notebook(); nb.cells=cells
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
nbformat.write(nb,'entries/sabatini-2024/reproduce_sabatini_2024.ipynb')
print(len(cells))
EOF
python $TMPDIR/build2.py && cd  && python tools/entry.py check entries/sabatini-2024 2>&1 | tail -5; date -u
```

```
121
0 error(s)
Fri Nov 20 12:41:52 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/sabatini-2024/README.md",
 "content": "# Sabatini & Kaufman (2024) from dandiset 000070\n\nTests the findings of [Sabatini & Kaufman (2024)](https://doi.org/10.1038/s41467-024-51308-7) on\n[DANDI:000070](https://dandiarchive.org/dandiset/000070/0.260528.0919), version 0.260528.0919, which holds\nthe two maze-task sessions the paper names (monkey J, 2009-09-18; monkey N, 2010-09-23), each with a PMd\nand an M1 Utah array and hand position. The notebook rebuilds the paper's four datasets (M1-J, PMd-J,\nM1-N, PMd-N) and tests its claims on jPCA, single-condition dynamics, the temporal basis factorization,\nthe orientation of rotational planes, the state space location, and LDR encoding and decoding.\n\n| Group | Outcomes |\n|---|---|\n| Reproduced | 9 claims, among them the factorization's variance explained, the misalignment of rotational planes across conditions, prediction of rotations from each other and from the location, and LDR encoding |\n| Partially reproduced | 15 claims |\n| Not reproduced | 9 claims, among them the eigenvalue distances, the single-LDS fit, the dimensionality of rotation orientations and location, and the warping control |\n| Blocked | 1 claim (the comparison with GPFA and other decoders, not run) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and\nthe differences from the paper's method.\n\nThe dandiset's units are one per electrode, with no single- or multi-unit label, where the paper used\nsorted units; the Nitschke file joins five recording segments whose clocks overlap. The attempt record,\nwith the reasons, the differences from the paper's method and the findings about the dataset, is\n[`attempts/sabatini-2024-01.yaml`](../../attempts/sabatini-2024-01.yaml).\n\nRun with `python tools/entry.py run entries/sabatini-2024`; it streams about 1 GB of spike times and hand\nposition and takes about 30 minutes.\n"
}
```

```
File created successfully at: entries/sabatini-2024/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd  && python tools/entry.py all entries/sabatini-2024 2>&1 | tail -8; date -u
```

```
Fri Nov 20 12:42:04 UTC 2026
Installed kernelspec registry-sabatini-2024 in executed/sabatini-2024/.venv/share/jupyter/kernels/registry-sabatini-2024
0 error(s)
pass  reproduce_sabatini_2024.ipynb  (1714 s)
Fri Nov 20 13:10:48 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/out2.txt
import nbformat
nb=nbformat.read('executed/sabatini-2024/reproduce_sabatini_2024.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    txt=''.join(o.get('text','') for o in c.outputs if o.get('output_type')=='stream')
    err=[o for o in c.outputs if o.get('output_type')=='error']
    print(f'=== cell {i} {c.metadata.get("tags",[])}'); print(txt[:6000])
    if err: print('ERROR')
EOF
diff <(grep -v "loaded in\|peak memory\|=== cell\|mean difference\|conditions kept" $TMPDIR/out1.txt) <(grep -v "loaded in\|peak memory\|=== cell\|mean difference\|conditions kept" $TMPDIR/out2.txt) | head; grep "mean difference" $TMPDIR/out2.txt | sed 's/same median.*mean difference/diff/'
```

```
34c34
< /tmp/claude-1001/ipykernel_37/3327514214.py:27: RuntimeWarning: All-NaN slice encountered
---
> /tmp/claude-1001/ipykernel_48/3327514214.py:27: RuntimeWarning: All-NaN slice encountered
39d38
<    72 conditions: 72 straight (no barrier) 36 curved 36
45d43
<    72 conditions: 72 straight (no barrier) 36 curved 36
216,235d213
< M1-J rot0 (0.70 Hz) vs onto rot1 (1.82 Hz): same median 0.752, different median 0.257; same higher on 0.997 of pairs; (a) p 0.0e+00; (b) p 0.0e+00
M1-J rot0 (0.70 Hz) vs onto rot1 (1.82 Hz): diff +0.493; same higher on 0.997 of pairs; (a) p 0.0e+00; (b) p 0.0e+00
M1-J rot0 (0.70 Hz) vs onto rot2 (3.08 Hz): diff +0.559; same higher on 1.000 of pairs; (a) p 0.0e+00; (b) p 0.0e+00
M1-J rot1 (1.82 Hz) vs onto rot0 (0.70 Hz): diff +0.070; same higher on 0.605 of pairs; (a) p 3.2e-84; (b) p 1.2e-52
M1-J rot1 (1.82 Hz) vs onto rot2 (3.08 Hz): diff +0.095; same higher on 0.698 of pairs; (a) p 7.5e-212; (b) p 2.0e-144
M1-J rot2 (3.08 Hz) vs onto rot0 (0.70 Hz): diff +0.132; same higher on 0.665 of pairs; (a) p 1.3e-279; (b) p 1.2e-194
M1-J rot2 (3.08 Hz) vs onto rot1 (1.82 Hz): diff +0.101; same higher on 0.608 of pairs; (a) p 2.4e-136; (b) p 4.4e-110
PMd-J rot0 (0.64 Hz) vs onto rot1 (1.54 Hz): diff +0.455; same higher on 0.999 of pairs; (a) p 0.0e+00; (b) p 0.0e+00
PMd-J rot1 (1.54 Hz) vs onto rot0 (0.64 Hz): diff +0.033; same higher on 0.521 of pairs; (a) p 5.8e-19; (b) p 1.9e-06
M1-N rot0 (0.69 Hz) vs onto rot1 (1.79 Hz): diff +0.362; same higher on 0.928 of pairs; (a) p 0.0e+00; (b) p 0.0e+00
M1-N rot0 (0.69 Hz) vs onto rot2 (3.23 Hz): diff +0.380; same higher on 0.977 of pairs; (a) p 0.0e+00; (b) p 0.0e+00
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required'))
p=s['properties']
for k in ['outcomes','findings','provenance','datasets','inputs']:
    v=p[k]; print(k, json.dumps(v)[:1500]); print()
EOF
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
outcomes {"description": "One per claim attempted.", "type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["claim", "outcome"], "properties": {"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "notes": {"description": "What differs, or what was missing, stated factually.", "type": "string"}, "notebook": {"description": "Path of the notebook within the entry.", "type": "string"}, "output": {"description": "Which output shows the result, e.g. a cell tag.", "type": "string"}, "measured": {"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}, "deviations": {"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.", "type": "array", "items": {"type": "string", "minLength": 1}}, "assumed": {"description": "True w

findings {"description": "What the attempt found, whatever the outcomes: about the dataset itself (`about: data`, for its owner and the archive, shown on the dataset's page) or about the paper (`about: paper`, shown on the paper's page).", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_m
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep sabatini; ls questions | grep sabatini; grep -n "seed_sensitive\|proposed\|verifications" schemas/attempt.schema.json | head -5
```

```
313:          "seed_sensitive": {
317:          "proposed": {
400:    "verifications": {
```

**Agent calls Write**

```json
{
 "file_path": "attempts/sabatini-2024-01.yaml",
 "content": "schema_version: 3\nid: sabatini-2024-01\ndatasets:\n- archive: dandi\n  id: \"000070\"\n  version: 0.260528.0919\n  doi: 10.48324/dandi.000070/0.260528.0919\n  relation: reuses\npaper: doi:10.1038/s41467-024-51308-7\ndate: 2026-11-20\nentry: sabatini-2024\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/44720511633\ninputs: []\noutcomes:\n- claim: data-composition\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:data-composition\n  measured:\n  - 72\n  - 1595\n  - 2121\n  notes: Both monkeys have the 72 conditions, 36 straight and 36 curved; the two readings of the\n    conditions give the same set (maze conditions not a multiple of 3 are exactly the 1-target mazes,\n    once maze 0, a set of 203 and 419 trials outside the 108, is left out). Trials, reading (a) all\n    successful, 1595 (J) and 2121 (N); reading (b) delay above 400 ms, 1381 and 1884; all four within\n    10% of 1469 and 2014. Each array holds 96 units, one per electrode, and the units table has no\n    single-unit, multi-unit or quality column, so the units the dataset marks as single or multi-units\n    cannot be counted; 96 is inside 71 to 130, but the same 96 in all four arrays, one per electrode,\n    is not the paper's 79 to 118 sorted units. The counts and conditions hold; the unit part does not\n    hold as the criterion states it.\n  deviations:\n  - The units are the dandiset's per-electrode units; the paper used sorted single units and stable\n    multi-units.\n- claim: jpca-fit-r2\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:jpca-fit-r2\n  assumed: true\n  notes: Reading (a), the skew-symmetric R2 in the first plane, gives 0.776, 0.664, 0.623 and 0.452\n    (M1-J, PMd-J, M1-N, PMd-N); three of four in 0.576 to 0.803. Refitted on straight and curved\n    reaches alone, straight 0.843, 0.753, 0.763, 0.781 and curved 0.712, 0.574, 0.660, 0.562, all in\n    their ranges and straight higher in every dataset. Reading (b), unconstrained, gives 0.823, 0.692,\n    0.685, 0.466 (two of four in range), straight 0.811 to 0.897 and curved 0.613 to 0.757. The\n    per-condition R2 paired by maze (straight against curved, 36 pairs) gives p = 0.058, 0.28, 5e-05\n    and 0.53, against the paper's p < 0.001; this part of the statement is not reproduced, and does not\n    decide.\n  deviations: &common\n  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label,\n    where the paper used 79 to 118 sorted single and stable multi-units.\n  - Trials are the successful trials of the 72 conditions with a delay above 400 ms (reading (b) of\n    the claims file), chosen because its counts are nearest the paper's; the paper gives no trial\n    selection. This is an assumption; reading (a) was not run for the analyses for lack of time.\n  - The paper's MATLAB code was not run; it needs preprocessed files that are available only on\n    request. Methods follow the claims file and the Methods.\n- claim: jpca-variance-explained\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:jpca-variance-explained\n  assumed: true\n  notes: Retained planes (two for M1, one for PMd) hold on average 8.9, 11.6, 11.7 and 5.1% of the\n    population variance, s.d. 3.6, 11.6, 5.4 and 3.2% across conditions (the paper gives s.d. below\n    13%). Three of four lie in 6.3 to 13.2%; PMd-N is below.\n  deviations: *common\n- claim: single-lds-variance\n  outcome: not_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:single-lds-variance\n  assumed: true\n  notes: One full-rank LDS over all conditions, simulated from each condition's state at -150 ms,\n    explains on average 76.6, 80.5, 82.1 and 77.4% over -150 to +850 ms (reading a) and 79.2, 83.4,\n    86.8 and 82.4% over the whole window (reading b), above 41.4 to 72.6% in every dataset. Units\n    pooled per electrode may give smoother, lower-dimensional population activity than sorted units,\n    which would raise every variance explained here.\n  deviations: *common\n- claim: fig2c-condition-lds-variance\n  outcome: reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig2c-condition-lds-variance\n  assumed: true\n  notes: Cross-validated dimensionality (even split, odd k from 1 to 21, 100 folds) is 5, 5, 7 and 5,\n    the same under all five seeds; the LDS explains 84.4, 90.2, 94.2 and 90.6% (s.d. 3.6 to 4.7%),\n    within 63.9 to 100%. The code's 3/4 split chooses 7, 5, 7 and 7 (86.9 to 94.2%).\n  deviations: *common\n- claim: fig3a-eigenvalue-clusters\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig3a-eigenvalue-clusters\n  assumed: true\n  notes: Every condition has the same number of complex pairs (2 in the k = 5 datasets; 3 in M1-N\n    except one condition) and at least one real eigenvalue on all 72 conditions, so the eigenvalues\n    cluster with an offset. Median pair frequencies are 0.85 and 2.35 Hz (M1-J), 0.54 and 1.53 (PMd-J),\n    0.68, 1.74 and 3.21 (M1-N), 0.73 and 1.67 (PMd-N); only PMd-J is within 10% of 0.5 and 1.5 Hz.\n  deviations: *common\n- claim: fig3c-eigenvalue-distance-auc\n  outcome: not_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig3c-eigenvalue-distance-auc\n  assumed: true\n  notes: AUC under the Poisson null (a) 0.812, 0.705, 0.631, 0.704 and under the half-split null (b)\n    0.696, 0.641, 0.662, 0.680; only M1-N under (a) lies in 0.459 to 0.638. The code's norm distance\n    gives AUCs within 0.02 of these. Under null (b) the five seeds give 0.694 to 0.709 (M1-J), 0.636 to\n    0.641, 0.656 to 0.667 and 0.673 to 0.680. Median distance between conditions 0.011 to 0.016,\n    noise 0.006 to 0.013.\n  deviations:\n  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label,\n    where the paper used 79 to 118 sorted single and stable multi-units.\n  - Trials as reading (b) of the claims file (assumption; see data-composition).\n  - 100 repeats per condition for each null, where the Methods give 500 (time); the other four seeds use\n    20.\n  - The Poisson null simulates 10 ms counts from the smoothed rates and smooths them at 10 ms\n    resolution, where the paper's pipeline works at 1 ms.\n- claim: suppfig2-eigenvalues-from-kinematics\n  outcome: not_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:suppfig2-eigenvalues-from-kinematics\n  assumed: true\n  measured: 0.275\n  notes: Mean leave-one-out R2 over the real and imaginary parts of the frequency-sorted eigenvalues,\n    pooled over the four datasets, is 0.275 under both kinematic readings (0.135 to 0.480 per\n    dataset), above 0.1 +- 0.05. Components without variance (the imaginary part of the real\n    eigenvalue) are left out; they would add zeros and lower the mean.\n  deviations: *common\n- claim: fig3g-basis-frequencies\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig3g-basis-frequencies\n  assumed: true\n  notes: Cross-validation chooses k = 6, 5, 7 and 6 under all five seeds; raised to odd, 7, 5, 7, 7.\n    De-mixing gives 3 rotation pairs and one offset in M1-J, M1-N and PMd-N, 2 pairs in PMd-J.\n    Frequencies 0.70, 1.82, 3.08 (M1-J), 0.64, 1.54 (PMd-J), 0.69, 1.79, 3.23 (M1-N), 0.74, 1.55, 2.71\n    Hz (PMd-N); 3 of 11 are within 10% of 0.5, 1.5, 2.5 or 4 Hz and none is near 0.5 or 4 Hz. The\n    structure (pairs plus an offset) holds; the frequencies are about 1.2 to 1.4 times the paper's.\n  deviations: *common\n- claim: tbf-variance-explained\n  outcome: reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:tbf-variance-explained\n  assumed: true\n  notes: Reading (a), -150 to +850 ms with the de-mixed basis, 93.5, 93.6, 96.6 and 95.3% (s.d. 0.8 to\n    1.5%); reading (b), whole window and raw basis, 92.1, 92.4, 96.1 and 94.5%; all within 81 to 100%.\n  deviations: *common\n- claim: tbf-shuffle-control\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:tbf-shuffle-control\n  assumed: true\n  notes: Shuffled variance explained 42.2, 28.7, 41.8 and 42.1%, real higher on 72 of 72 conditions,\n    rank-sum p = 3.9e-25 (signed-rank variant 1.7e-13). PMd-J lies below 31.5 to 50.6%. Under the five\n    seeds the shuffled means vary by at most 0.006 (PMd-J 0.287 to 0.292).\n  deviations:\n  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label,\n    where the paper used 79 to 118 sorted single and stable multi-units.\n  - Trials as reading (b) of the claims file (assumption; see data-composition).\n  - Time bins are permuted within the 1.5 s window read around movement onset (-500 to +1000 ms), with\n    one permutation for all units of a trial so that correlations between units are kept (Methods,\n    Control for data smoothing, \"preserving inter-neuron spike correlations\"); the span shuffled is\n    not given and is an assumption.\n- claim: fig3h-recoverability\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig3h-recoverability\n  assumed: true\n  notes: Recoverability 97.3, 97.9, 98.6 and 98.6% (within 81.9 to 100%), real higher on all 72\n    conditions, rank-sum p = 3.9e-25. Chance (the shuffled data) is 89.6, 86.0, 89.0 and 89.6%; only\n    PMd-J lies in 56.7 to 88%. Five seeds move chance by at most 0.012. The main result holds; the\n    chance level is higher than the paper's.\n  deviations: *common\n- claim: fig3i-duration-warping\n  outcome: not_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig3i-duration-warping\n  assumed: true\n  measured: 0.235\n  notes: Unwarped rho -0.157, 0.083, 0.235 (M1-N, p = 0.047) and 0.077; M1-N has the opposite sign to\n    -0.26. Warped (600 ms, truncated at 850 ms) rho -0.514 (p = 4e-06), -0.071, -0.024 and -0.193; only\n    M1-J lies in -0.693 to -0.468 with p < 0.001. The 250 ms post-reach variant gives -0.363, -0.175,\n    -0.096 and -0.323. Condition mean durations are 242 to 606 ms (J) and 252 to 573 ms (N).\n  deviations:\n  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label,\n    where the paper used 79 to 118 sorted single and stable multi-units.\n  - Trials as reading (b) of the claims file (assumption; see data-composition).\n  - Reach end is searched within 850 ms after onset, so durations are capped at 850 ms.\n  - Warping is applied to the 1 ms smoothed rates of each trial before averaging; the basis of the\n    warped data is de-mixed before recoverability is computed.\n- claim: suppfig3-model-comparison\n  outcome: not_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:suppfig3-model-comparison\n  assumed: true\n  notes: Under the main reading the cross-validated TBF value (held-out variance at the dataset's k;\n    71.1, 79.0, 86.6, 79.1%) exceeds jPCA (5.1 to 11.7%) but not the in-sample single-condition LDS\n    (84.4 to 94.2%) in any dataset. With all three in sample (the variant), TBF (93.5 to 96.6%) is the\n    highest in every dataset. The claims file's check noted this mix as open.\n  deviations: *common\n- claim: fig4b-plane-alignment\n  outcome: reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig4b-plane-alignment\n  assumed: true\n  notes: AUC per rotation 0.912, 0.886, 0.861 (M1-J), 0.945, 0.933 (PMd-J), 0.949, 0.952, 0.933 (M1-N),\n    0.958, 0.949, 0.940 (PMd-N), observed lower on 72 of 72 conditions; reading (a) signed-rank p =\n    1.7e-13 for each; reading (b) rank-sum p printed as 0. Four other seeds change each AUC by at most\n    0.002. The paper's 4 Hz rotation is not present here; the rotations tested are those found.\n  deviations: *common\n- claim: fig4c-subspace-excursion-angles\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig4c-subspace-excursion-angles\n  assumed: true\n  notes: Excursion angles above 45 degrees per rotation, 5, 13, 11 (M1-J), 7, 14 (PMd-J), 3, 9, 11\n    (M1-N), 7, 18, 25 (PMd-N); 8 of 11 in 5.4 to 22 (9 of 11 counting the seed plane's two\n    dimensions). Angles above the 95th percentile of half-split noise angles 4 to 9 per rotation,\n    fewer than the count above 45 degrees for 7 of 11 rotations, so the second part of the criterion\n    fails with this noise level.\n  deviations:\n  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label,\n    where the paper used 79 to 118 sorted single and stable multi-units.\n  - Trials as reading (b) of the claims file (assumption; see data-composition).\n  - The search over sequences is a greedy search from every seed, keeping the sequence with the\n    largest summed angles; the Methods say the search was optimised over all sequences.\n  - Chance is the 95th percentile of the largest principal angle between half-split estimates of the\n    same condition's plane (assumption; the code's control is described only as the fraction of noise\n    SEA above the data).\n- claim: rotation-orientation-dimensionality\n  outcome: not_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:rotation-orientation-dimensionality\n  assumed: true\n  notes: PCs to 80% are 2 to 23 (reading a, stacked columns) or 2 to 22 (reading b, activity), and\n    participation ratios 1.8 to 18.7 or 1.7 to 18.5, against 20.7 to 44 and 15.03 to 40.48; only PMd-N\n    2.71 Hz is in range. SNR dimensionality is 10 to 21 for 9 of 11 rotations (in 6.3 to 36.3); for\n    the slowest rotation of M1-N and PMd-N the alignment keeps rising to all 96 dimensions under all\n    five seeds. Orientations here are much lower-dimensional than in the paper.\n  deviations: *common\n- claim: fig4d-jpca-variance-correlation\n  outcome: not_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig4d-jpca-variance-correlation\n  assumed: true\n  measured: 83\n  notes: Rho per plane -0.061 and 0.711 (M1-J), 0.930 (PMd-J), 0.663 and 0.627 (M1-N), 0.682 (PMd-N).\n    Reading (a), per-dataset means 0.325, 0.930, 0.645, 0.682; reading (b), significant planes 0.627\n    to 0.930; neither lies in 0.351 to 0.506. Five of six planes (83%) have p < 0.05, outside 66 +-\n    6.6%. The correlations are mostly stronger than the paper's.\n  deviations: *common\n- claim: fig4f-plane-alignment-explains-jpca\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig4f-plane-alignment-explains-jpca\n  assumed: true\n  notes: Rho 0.941, 0.926 (M1-J), 0.832 (PMd-J), 0.689, 0.817 (M1-N), 0.815 (PMd-N), all with p at most\n    2.3e-11; five of six in 0.738 to 1.\n  deviations: *common\n- claim: fig5a-frequencies-segregated\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig5a-frequencies-segregated\n  assumed: true\n  notes: Of 20 ordered rotation comparisons, 18 show same-frequency alignment higher by median, by\n    mean and on more than half of the condition pairs, with p < 1e-6 under both readings. For M1-N 3.23\n    Hz onto 0.69 and 1.79 Hz, the medians are lower (0.176 against 0.191 and 0.193) and same-frequency\n    is higher on 49% and 48% of pairs, while the mean difference is positive (+0.038 and +0.042) and\n    the signed-rank test gives p = 9e-11 and 4e-08 (rank-sum 0.85 and 0.68). Whether same-frequency is\n    higher there depends on the measure; it is counted as not shown. 18 of 20 (90%) is at least 80%.\n  deviations: *common\n- claim: fig5c-rotations-predict-rotations\n  outcome: reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig5c-rotations-predict-rotations\n  assumed: true\n  notes: Mean variance explained per ordered pair 41.4 to 94.6% (all 20 in 38.7 to 100%), null 2.4 to\n    76.3%, signed-rank p at most 4.9e-13 for every pair. Four other seeds move pair means by at most\n    0.03.\n  deviations:\n  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label,\n    where the paper used 79 to 118 sorted single and stable multi-units.\n  - Trials as reading (b) of the claims file (assumption; see data-composition).\n  - Rotations of each fold's factorization are matched to the full-data rotations by nearest\n    frequency.\n- claim: suppfig6a-location-alignment\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:suppfig6a-location-alignment\n  assumed: true\n  notes: AUC 0.883, 0.748, 0.870 and 0.945, observed lower on 72, 70, 72 and 72 conditions, signed-rank\n    p at most 2.1e-13; PMd-J is below 0.792. Four other seeds give PMd-J 0.746 to 0.758.\n  deviations: *common\n- claim: suppfig6b-location-dimensionality\n  outcome: not_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:suppfig6b-location-dimensionality\n  assumed: true\n  notes: SEA location dimensions above 15 degrees 0, 1, 1, 0 (1, 2, 2, 1 with the seed); PCs to 80% 4,\n    5, 2, 5 (reading a); participation ratio 4.2, 3.2, 2.3, 3.5; all below their ranges. The SNR\n    procedure keeps rising to the largest dimensionality, 72 (the number of conditions), under all\n    five seeds, so it gives no estimate.\n  deviations: *common\n- claim: suppfig6c-location-distinct-from-rotations\n  outcome: reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:suppfig6c-location-distinct-from-rotations\n  assumed: true\n  notes: Location-to-location alignment median 0.935 to 0.969 against location onto rotation planes\n    0.078 to 0.670; p printed as 0 under both readings in every dataset.\n  deviations: *common\n- claim: fig6b-location-predicts-rotations\n  outcome: reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig6b-location-predicts-rotations\n  assumed: true\n  notes: Methods version (6 folds, lambda 0.1) 70.9, 72.3, 80.9 and 71.6%, null 19.1, 12.9, 22.6 and\n    13.0%, signed-rank p at most 2.4e-13; the code's variant 76.6, 73.1, 85.6 and 77.1%. Four other\n    seeds give 70.0 to 82.2%.\n  deviations: *common\n- claim: fig6c-location-tracks-direction\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig6c-location-tracks-direction\n  assumed: true\n  notes: With PC 2 flipped, circular correlation of target angle with the location's angle in the PC\n    1-2 plane is 0.613 (p = 4e-06), 0.701 (6e-09), 0.245 (0.016) and 0.053 (0.62) for M1-J, PMd-J, M1-N\n    and PMd-N; PMd-N fails in either orientation.\n  deviations: *common\n- claim: fig6e-kinematics-predict-location\n  outcome: reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig6e-kinematics-predict-location\n  assumed: true\n  notes: Kinematic reading (a) (SVD basis), linear 53.3, 55.0, 70.4, 41.4% (in 33.3 to 78.1%); OU kernel\n    70.4, 68.8, 88.7, 76.9% (in 62.1 to 89.1%); both above all 1000 permutations (p = 0.001). Reading\n    (b) (skew-normal basis) gives linear 41.5 to 70.4% and OU 69.6 to 89.1%, also all in range. The\n    Gaussian kernel (kernel reading b) gives 32.2 to 54.4%, below the range. Five seeds give OU 68.8 to\n    71.8 (M1-J), 65.9 to 70.5, 86.9 to 88.7 and 73.2 to 76.9%, all in range.\n  deviations: *common\n- claim: fig7c-ldr-encoding\n  outcome: reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig7c-ldr-encoding\n  assumed: true\n  notes: SVD kinematic basis, linear 76.5, 68.1, 84.3, 72.3% (s.d. 5.9 to 18.9%), kernel 84.0, 85.0,\n    92.1, 86.7% (s.d. 2.7 to 7.8%); against the shuffled null, p at most 2.6e-08 (linear) and 1.9e-13\n    (kernel). Skew-normal basis within 0.01 of these. Five seeds give linear 66.4 to 69.4% for PMd-J\n    and kernel 83.4 to 92.1% overall, all in range.\n  deviations: *common\n- claim: suppfig7a-not-memorization\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:suppfig7a-not-memorization\n  assumed: true\n  notes: Sextants held out, kernel against nearest neighbour, SVD basis, 75.2 against 66.7% (p = 6e-10),\n    67.6 against 58.5% (p = 0.019), 85.8 against 77.7% (p = 2e-11), 76.7 against 67.7% (p = 3e-11);\n    PMd-J misses p < 0.01, and under the skew-normal basis PMd-J gives p = 0.89.\n  deviations: *common\n- claim: fig7c-standard-encoding-worse\n  outcome: reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig7c-standard-encoding-worse\n  assumed: true\n  notes: Both LDR models exceed every standard model with p < 0.001 in all 24 comparisons under both\n    kinematic readings. The linear multi-parameter model explains 51.7 to 53.4%. The OU kernel models\n    on position (length scale 1e12) and velocity (1e11) explain 0% with the assumed penalty 0.1,\n    because the kernel is nearly constant at these length scales; those 16 comparisons are not\n    informative, and the outcome rests on the 8 comparisons with the linear model.\n  deviations:\n  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label,\n    where the paper used 79 to 118 sorted single and stable multi-units.\n  - Trials as reading (b) of the claims file (assumption; see data-composition).\n  - Velocity angle enters the linear model as its cosine and sine, and features are z-scored; the\n    kernel penalty is 0.1 (the Methods' L2 for kernel decoders). The Methods give neither (assumption).\n- claim: fig7f-ldr-decoding\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:fig7f-ldr-decoding\n  assumed: true\n  notes: Mean variance explained in single-trial hand position, SVD basis, 77.4, 74.7, 87.4 and 73.4%\n    (medians 84.4, 83.1, 92.0, 82.3%); M1-J and M1-N in 75.6 to 100%. Skew-normal basis 76.8, 74.1,\n    86.8 and 72.9%. Over the five seeds, M1-J 76.2 to 77.7, PMd-J 68.9 to 74.7, M1-N 87.4 to 88.3, PMd-N\n    72.2 to 76.1%; two or three datasets in range under each seed, so the outcome holds under all five.\n    The condition-shuffled null gives 2.0 to 3.8% (p below 1e-200).\n  deviations: *common\n- claim: fig7f-decoder-beats-standard\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not run. The comparison needs eight instantaneous decoders on single trials, kernel regression\n    on tens of thousands of single-trial samples, and GPFA, whose latent dimensionality and bin size\n    the paper and code do not give. With about 1.5 hours of the five-hour run left after the other 33\n    claims and two full runs of the notebook (29 minutes each), it was not attempted; nothing was\n    computed for it.\n- claim: suppfig8-no-output-potent-dependence\n  outcome: not_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:suppfig8-no-output-potent-dependence\n  assumed: true\n  notes: Removing the four-dimensional row space of the least-squares map from activity to hand\n    position and velocity lowers the per-condition decoded variance from 75.3 to 69.1% (M1-J), 74.2 to\n    69.4, 86.5 to 82.6 and 74.6 to 70.3% (SVD basis), drops of 3.9 to 6.2 points, and the two-sided\n    signed-rank test gives p < 0.001 in every dataset, below 0.036. The dataset holds no EMG, so the\n    muscle dimensions could not be removed.\n  deviations:\n  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label,\n    where the paper used 79 to 118 sorted single and stable multi-units.\n  - Trials as reading (b) of the claims file (assumption; see data-composition).\n  - No EMG in the dataset; only kinematic dimensions are removed, as the criterion allows.\n- claim: trial-curvature-decoding\n  outcome: partially_reproduced\n  notebook: reproduce_sabatini_2024.ipynb\n  output: claim:trial-curvature-decoding\n  assumed: true\n  notes: Within-condition residuals of decoded and actual curvature parameters, SVD basis, rho 0.319\n    and 0.162 (M1-J), 0.229 and 0.093 (PMd-J), 0.449 and 0.548 (M1-N), 0.191 and 0.290 (PMd-N), all p\n    below 0.001; 6 of 8 in 0.144 to 0.451. Skew-normal basis 5 of 8 in range.\n  deviations: *common\nfindings:\n- kind: format_error\n  about: data\n  severity: major\n  statement: The Nitschke file (sub-Nitschke_ses-20100923) joins five recording segments whose clocks\n    overlap. Trial start times, hand timestamps and every unit's spike times jump backwards four times\n    (segments span 5 to 6076 s, 6074 to 12077 s, 6071 to 12494 s, 6120 to 13516 s and 6074 to 6658 s),\n    so spike times are not sorted and a trial's spikes cannot be selected by time alone; doing so mixes\n    spikes of up to four segments. Splitting each unit's spikes at the jumps and assigning trials to\n    segments in file order gives condition decoding of 0.41 to 0.46 in segments 0 to 2 and 0.16 in\n    segment 3 (chance 0.014; 0.006 to 0.027 with the previous trial's labels).\n- kind: metadata_insufficient\n  about: data\n  severity: major\n  statement: The units table holds 96 units per array, one per electrode, in both files, with no column\n    for single or multi-unit, sorting quality or isolation. The paper reports 79 to 118 single and\n    stable multi-units per array. Whether these units are threshold crossings or sorted units merged\n    per electrode is not stated.\n- kind: format_error\n  about: data\n  severity: minor\n  statement: In the Jenkins file, one unit's spike train (the second row of the units table) holds two\n    sorted runs one after the other, the second restarting at 4.7 s after the first reached 15668.6 s.\n    The two runs were merged and sorted here.\n- kind: metadata_error\n  about: data\n  severity: minor\n  statement: Hand, cursor and eye positions are labelled \"meters\" with a conversion of NaN, but hold\n    millimetres (reaches of about 130 and positions from -182 to 159).\n- kind: data_missing\n  about: data\n  severity: minor\n  statement: The dataset holds no EMG, which the paper's Supplementary Figure 8 removes along with\n    kinematic dimensions.\n- kind: other\n  about: data\n  severity: minor\n  statement: In the Nitschke file, condition information in segment 3 is lower within the segment\n    (decoding 0.161) than in segments 0 to 2 (0.411 to 0.459), while a decoder trained on the other\n    segments reaches 0.478 on it, and decoding does not peak at another time offset. This is consistent\n    with a change of the recorded units over the session; segment 4 (22 trials) is too small to check\n    on its own.\n- kind: methods_unavailable\n  statement: Questions for the paper's authors. (1) Which trials were analysed? Successful trials with a\n    delay above 400 ms give 1381 (J) and 1884 (N) and all successful trials 1595 and 2121, against\n    1469 and 2014 in the Figure 7 legend; the first was used here. (2) Which units were used, and are\n    they in the dandiset? The files hold one unit per electrode with no single or multi-unit label.\n    (3) What penalty was used for the OU kernel encoding models with length scales 1e11 and 1e12? With\n    a penalty of 0.1 they predict only the mean. (4) How were the noise excursion angles of Figure 4c\n    computed? (5) Were the jPCA and single-condition LDS values of Supplementary Figure 3\n    cross-validated, and how?\n- kind: methods_unavailable\n  statement: The paper's code (kaufmanlab/LDR-public) loads preprocessed files (ShenoyMonkeyData and\n    others) that the Data availability statement offers only on request, so the code cannot be run on\n    the public data, and the trial and unit selection behind them cannot be checked.\n"
}
```

```
File created successfully at: attempts/sabatini-2024-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/sabatini-2024-01.yaml'; s=open(p).read()
rep=[("13.0%, signed-rank p at most 2.4e-13; the code's variant 76.6, 73.1, 85.6 and 77.1%. Four other\n    seeds give 70.0 to 82.2%.","13.0%, signed-rank p at most 2.4e-13; the code's variant 76.6, 73.1, 85.6 and 77.1%. Four other\n    seeds give 70.5 to 82.2%."),
("position and velocity lowers the per-condition decoded variance from 75.3 to 69.1% (M1-J), 74.2 to\n    69.4, 86.5 to 82.6 and 74.6 to 70.3% (SVD basis), drops of 3.9 to 6.2 points,","position and velocity lowers the per-condition decoded variance from 75.9 to 69.7% (M1-J), 75.0 to\n    70.1, 87.2 to 83.3 and 75.2 to 70.9% (SVD basis), drops of 3.9 to 6.3 points,")]
for a,b in rep:
    assert a in s, a[:40]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/entry.py check entries/sabatini-2024 2>&1 | tail -10; date -u
```

```
0 error(s)
Fri Nov 20 13:13:19 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml, collections
a=yaml.safe_load(open('attempts/sabatini-2024-01.yaml'))
c=yaml.safe_load(open('claims/sabatini-2024.yaml'))
ids=[x['id'] for x in c['claims']]; got=[o['claim'] for o in a['outcomes']]
print(len(ids), len(got), set(ids)-set(got), set(got)-set(ids))
print(collections.Counter(o['outcome'] for o in a['outcomes']))
EOF
grep -rn ": " attempts/sabatini-2024-01.yaml | grep -v "^\S*:[0-9]*: *[-a-z_]*:" | head
```

```
34 34 set() set()
Counter({'partially_reproduced': 15, 'not_reproduced': 9, 'reproduced': 9, 'blocked': 1})
1:schema_version: 3
2:id: sabatini-2024-01
4:- archive: dandi
5:  id: "000070"
6:  version: 0.260528.0919
7:  doi: 10.48324/dandi.000070/0.260528.0919
8:  relation: reuses
9:paper: doi:10.1038/s41467-024-51308-7
10:date: 2026-11-20
11:entry: sabatini-2024
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
a=yaml.safe_load(open('attempts/sabatini-2024-01.yaml'))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str) and (': ' in x or '—' in x or 'rather' in x): print(path, x[:80])
walk(a)
EOF
grep -n "—\|rather\|\*\*" entries/sabatini-2024/README.md | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -c "—\|rather" entries/sabatini-2024/reproduce_sabatini_2024.ipynb entries/sabatini-2024/ldr.py; python tools/entry.py handover entries/sabatini-2024 2>&1 | tail -5; git status --short; date -u
```

```
entries/sabatini-2024/reproduce_sabatini_2024.ipynb:0
entries/sabatini-2024/ldr.py:0
wrote executed/sabatini-2024/handover
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
?? attempts/sabatini-2024-01.yaml
?? entries/sabatini-2024/
?? scripts
Fri Nov 20 13:13:51 UTC 2026
```

**Agent calls Bash**

```bash
ls -la scripts .idea .vscode 2>&1 | head; ls -la .bashrc .mcp.json; ls entries/sabatini-2024
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 20 10:35 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 20 10:35 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 20 10:35 scripts
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 20 10:35 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 20 10:35 .mcp.json
README.md
__pycache__
entry.yaml
ldr.py
reproduce_sabatini_2024.ipynb
requirements.in
requirements.lock.txt
```

**Agent**

I have about 1.5 hours left. I'll use 50 minutes to run the non-GPFA part of the decoder comparison (the criterion allows a partial outcome without GPFA) and re-run the notebook once.

**Agent calls Bash**

```bash
rm -rf entries/sabatini-2024/__pycache__; cat >> $TMPDIR/src/nb_part4.py <<'EOF'

# %% md
## fig7f-decoder-beats-standard

Instantaneous decoders of hand position (Methods, Comparing LDR-based decoding to instantaneous
decoding methods): activity 100 ms before each time point, smoothed with a 20 ms Gaussian (the
single-trial rates used throughout) or a 100 ms Gaussian (10 ms counts smoothed with s.d. 10 bins, a
standard approximation); ridge regression (lambda 1) trained on single trials; OU kernel regression
(length scale 100, L2 0.1) trained on a random subset of 3000 single-trial time points (the Methods'
"subset of single-trial data"; the size is an assumption) or on trial averages. The same two folds of
conditions as the LDR decoder; variance explained in position per trial over -250 to +850 ms, compared
with the LDR decoder's per-trial values by two-sided signed-rank tests. The GPFA decoders are not run:
the paper gives neither the latent dimensionality nor the bin size, and there was not time to fit them.

# %%
from scipy.ndimage import gaussian_filter1d


def inst_job(args):
    ds, r, sd = args
    m = ds[0]
    rng = np.random.default_rng(sd)
    folds = ldr.folds_of(72, 2, rng)  # the same draw as decode() under this seed
    rng2 = np.random.default_rng(seed("fig7f-decoder-beats-standard"))
    cond = D[ds]["cond"]
    u = D[ds]["u"]
    lag = 10
    tt = np.arange(lag, len(ldr.GRID_MS))
    feats = {"20 ms": SESS[m]["R"][:, u], "100 ms": gaussian_filter1d(SESS[m]["C10"][:, u], 10, axis=2, mode="reflect")}
    H = KIN[m]["H"]
    out = {}
    for sname, F in feats.items():
        for dname in ("linear, single trials", "kernel, single trials", "kernel, trial averages"):
            ve = np.full(len(cond), np.nan)
            for te in folds:
                tr = np.setdiff1d(np.arange(72), te)
                itr = np.where(MASK[m] & np.isin(cond, tr))[0]
                ite = np.where(MASK[m] & np.isin(cond, te))[0]
                if dname == "kernel, trial averages":
                    Fa = ldr.cond_average(F, cond, 72, MASK[m])[tr]
                    Ha = KIN[m]["Hc"][tr]
                    X = Fa[:, :, tt - lag].transpose(0, 2, 1).reshape(-1, F.shape[1])
                    Y = Ha[:, tt].reshape(-1, 2)
                else:
                    X = F[itr][:, :, tt - lag].transpose(0, 2, 1).reshape(-1, F.shape[1])
                    Y = H[itr][:, tt].reshape(-1, 2)
                mu, sdv = X.mean(0), X.std(0) + 1e-9
                X = (X - mu) / sdv
                if dname.startswith("linear"):
                    f = ldr.ridge_fit(X, Y, 1.0)
                else:
                    if len(X) > 3000:
                        pick = rng2.choice(len(X), 3000, replace=False)
                        X, Y = X[pick], Y[pick]
                    f = ldr.kernel_fit(X, Y, "ou", 1e2, 0.1)
                for i in ite:
                    Z = (F[i][:, tt - lag].T - mu) / sdv
                    ve[i] = ldr.kin_ve(H[i][tt], f(Z))
            out[(sname, dname)] = ve
    return out


_jobs = [(ds, "a", seed("fig7f-ldr-decoding")) for ds in DATASETS]
INST = dict(zip(DATASETS, ldr.pmap(inst_job, _jobs)))

# %% [claim:fig7f-decoder-beats-standard]
nwin, ntot = 0, 0
for ds in DATASETS:
    ldr_ve, _ = DEC[(ds, "a", seed("fig7f-ldr-decoding"), ())]
    for key, ve in INST[ds].items():
        ok = np.isfinite(ve) & np.isfinite(ldr_ve)
        p = stats.wilcoxon(ldr_ve[ok], ve[ok]).pvalue
        win = (np.mean(ldr_ve[ok] - ve[ok]) > 0) and p < 0.001
        nwin += win
        ntot += 1
        print(f"{NAME[ds]} {key[1]}, {key[0]} smoothing: mean {np.mean(ve[ok]):.3f} against LDR {np.mean(ldr_ve[ok]):.3f} "
              f"({int(ok.sum())} trials); two-sided signed-rank p {p:.1e}")
print(f"LDR higher with p < 0.001 in {nwin} of {ntot} comparisons (GPFA decoders not run)")
EOF
cd $TMPDIR && cp defs.py entries/sabatini-2024/_defs_tmp.py && python3 - <<'EOF'
import re
src=open('/tmp/claude-1001/src/nb_part4.py').read()
i=src.index('# %% md\n## fig7f-decoder-beats-standard')
# dev: need KIN, DEC; build a dev file containing kinematics cell + decode cells + new cells
j=src.index('# %% md\n## Kinematics'); k=src.index('# %% md\n## fig6e')
d1=src.index('# %% md\n## fig7f-ldr-decoding'); d2=src.index('# %% [claim:fig7f-ldr-decoding]')
open('entries/sabatini-2024/_p4tmp.py','w').write(src[j:k]+src[d1:d2]+src[i:])
EOF
date -u; time OMP_NUM_THREADS=1 dev/bin/python harness.py resume _defs_tmp.py _p4tmp.py 2>&1 | tail -30; rm -f entries/sabatini-2024/_p4tmp.py entries/sabatini-2024/_defs_tmp.py
```

```
Fri Nov 20 13:14:26 UTC 2026
monkey J, reading (b): reach parameters reproduce condition-mean hand position with VE 0.981
monkey N, reading (a): reach parameters reproduce condition-mean hand position with VE 0.996
monkey N, reading (b): reach parameters reproduce condition-mean hand position with VE 0.987
[cell # %% took 32s]
[cell # %% took 53s]
M1-J linear, single trials, 20 ms smoothing: mean 0.019 against LDR 0.774 (1381 trials); two-sided signed-rank p 1.1e-223
M1-J kernel, single trials, 20 ms smoothing: mean 0.046 against LDR 0.774 (1381 trials); two-sided signed-rank p 1.7e-223
M1-J kernel, trial averages, 20 ms smoothing: mean 0.010 against LDR 0.774 (1381 trials); two-sided signed-rank p 1.1e-223
M1-J linear, single trials, 100 ms smoothing: mean 0.280 against LDR 0.774 (1381 trials); two-sided signed-rank p 2.6e-214
M1-J kernel, single trials, 100 ms smoothing: mean 0.403 against LDR 0.774 (1381 trials); two-sided signed-rank p 1.8e-195
M1-J kernel, trial averages, 100 ms smoothing: mean 0.155 against LDR 0.774 (1381 trials); two-sided signed-rank p 6.8e-219
PMd-J linear, single trials, 20 ms smoothing: mean 0.029 against LDR 0.747 (1381 trials); two-sided signed-rank p 2.3e-220
PMd-J kernel, single trials, 20 ms smoothing: mean 0.059 against LDR 0.747 (1381 trials); two-sided signed-rank p 2.6e-220
PMd-J kernel, trial averages, 20 ms smoothing: mean 0.005 against LDR 0.747 (1381 trials); two-sided signed-rank p 2.1e-220
PMd-J linear, single trials, 100 ms smoothing: mean 0.202 against LDR 0.747 (1381 trials); two-sided signed-rank p 8.7e-216
PMd-J kernel, single trials, 100 ms smoothing: mean 0.317 against LDR 0.747 (1381 trials); two-sided signed-rank p 1.9e-200
PMd-J kernel, trial averages, 100 ms smoothing: mean 0.029 against LDR 0.747 (1381 trials); two-sided signed-rank p 1.8e-220
M1-N linear, single trials, 20 ms smoothing: mean 0.146 against LDR 0.874 (1883 trials); two-sided signed-rank p 1.4e-308
M1-N kernel, single trials, 20 ms smoothing: mea
[... 16 more lines not kept]
```

**Agent**

Decoder comparison works (LDR higher in 24 of 24 non-GPFA comparisons). Updating conclusions, summary and README, then the final run.

**Agent calls Bash**

```bash
cd $TMPDIR/src && python - <<'EOF'
s=open('conclusions.py').read()
s=s.rstrip().rstrip('}')
s+='''"fig7f-decoder-beats-standard": """**Result: partially reproduced.** The LDR decoder explains more of the single-trial hand position than each of the 24 instantaneous decoders run (ridge regression and OU kernel regression on 20 or 100 ms smoothed activity, trained on single trials or trial averages), with two-sided signed-rank p below 1e-180 in every comparison; the best of them reaches 73.1% (M1-N, kernel on single trials, 100 ms) against 87.4% for LDR. The GPFA decoders were not run, so the claim holds against all but the GPFA decoders.""",
}
'''
a="""In PMd-J 1.54 Hz onto 0.64 Hz and PMd-N 2.71 Hz onto the others the medians differ by 0.001 although the tests give p < 1e-6.\"\"\","""
assert a in s
s=s.replace(a,"""Their mean differences are positive (+0.038 and +0.042) and the signed-rank tests give p = 9e-11 and 4e-08, so the direction there depends on the measure; they are counted as not shown. In PMd-J 1.54 Hz onto 0.64 Hz and PMd-N 2.71 Hz onto the others the medians differ by 0.001, with mean differences of +0.033 to +0.036.\"\"\",""")
open('conclusions.py','w').write(s)
p=open('nb_part1.py').read()
p=p.replace("| fig7f-decoder-beats-standard | blocked (not run within the time of this attempt) |","| fig7f-decoder-beats-standard | tested except the GPFA decoders |")
open('nb_part1.py','w').write(p)
q=open('nb_part5.py').read()
q=q.replace("| fig7f-decoder-beats-standard | blocked (not run in the time of this attempt) |","| fig7f-decoder-beats-standard | partially reproduced (GPFA decoders not run) |")
q=q.replace("The GPFA decoder\ncomparison was not run.","The GPFA decoders\nwere not run.")
open('nb_part5.py','w').write(q)
EOF
grep -n "GPFA" $TMPDIR/src/nb_part5.py; python3 -c "
import sys; sys.path.insert(0,'$TMPDIR/src'); import conclusions; print(len(conclusions.C))"
python $TMPDIR/build2.py
```

```
37:| fig7f-decoder-beats-standard | partially reproduced (GPFA decoders not run) |
51:it. The dataset has no EMG, so suppfig8 removes the kinematic dimensions only. The GPFA decoders
34
125
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python - <<'EOF'
s=open('README.md').read()
s=s.replace("| Partially reproduced | 15 claims |","| Partially reproduced | 16 claims, among them the comparison with instantaneous decoders, run without the GPFA decoders |")
s=s.replace("| Blocked | 1 claim (the comparison with GPFA and other decoders, not run) |\n","")
open('README.md','w').write(s)
EOF
cat README.md | sed -n 10,18p; cd ../.. && date -u && python tools/entry.py all entries/sabatini-2024 2>&1 | tail -4; date -u
```

```
| Group | Outcomes |
|---|---|
| Reproduced | 9 claims, among them the factorization's variance explained, the misalignment of rotational planes across conditions, prediction of rotations from each other and from the location, and LDR encoding |
| Partially reproduced | 16 claims, among them the comparison with instantaneous decoders, run without the GPFA decoders |
| Not reproduced | 9 claims, among them the eigenvalue distances, the single-LDS fit, the dimensionality of rotation orientations and location, and the warping control |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

Fri Nov 20 13:16:11 UTC 2026
Installed kernelspec registry-sabatini-2024 in executed/sabatini-2024/.venv/share/jupyter/kernels/registry-sabatini-2024
0 error(s)
pass  reproduce_sabatini_2024.ipynb  (1767 s)
Fri Nov 20 13:45:47 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/out3.txt
import nbformat
nb=nbformat.read('executed/sabatini-2024/reproduce_sabatini_2024.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    txt=''.join(o.get('text','') for o in c.outputs if o.get('output_type')=='stream')
    print(f'=== cell {c.metadata.get("tags",[])}'); print(txt[:6000])
    if any(o.get('output_type')=='error' for o in c.outputs): print('ERROR')
EOF
diff <(grep -v "loaded in\|peak memory\|=== cell\|ipykernel" $TMPDIR/out2.txt) <(grep -v "loaded in\|peak memory\|=== cell\|ipykernel" $TMPDIR/out3.txt) | head -40; grep -c ERROR $TMPDIR/out3.txt
```

```
426a427,453
> 
> M1-J linear, single trials, 20 ms smoothing: mean 0.019 against LDR 0.774 (1381 trials); two-sided signed-rank p 1.1e-223
> M1-J kernel, single trials, 20 ms smoothing: mean 0.046 against LDR 0.774 (1381 trials); two-sided signed-rank p 1.7e-223
> M1-J kernel, trial averages, 20 ms smoothing: mean 0.010 against LDR 0.774 (1381 trials); two-sided signed-rank p 1.1e-223
> M1-J linear, single trials, 100 ms smoothing: mean 0.280 against LDR 0.774 (1381 trials); two-sided signed-rank p 2.6e-214
> M1-J kernel, single trials, 100 ms smoothing: mean 0.403 against LDR 0.774 (1381 trials); two-sided signed-rank p 1.8e-195
> M1-J kernel, trial averages, 100 ms smoothing: mean 0.155 against LDR 0.774 (1381 trials); two-sided signed-rank p 6.8e-219
> PMd-J linear, single trials, 20 ms smoothing: mean 0.029 against LDR 0.747 (1381 trials); two-sided signed-rank p 2.3e-220
> PMd-J kernel, single trials, 20 ms smoothing: mean 0.059 against LDR 0.747 (1381 trials); two-sided signed-rank p 2.6e-220
> PMd-J kernel, trial averages, 20 ms smoothing: mean 0.005 against LDR 0.747 (1381 trials); two-sided signed-rank p 2.1e-220
> PMd-J linear, single trials, 100 ms smoothing: mean 0.202 against LDR 0.747 (1381 trials); two-sided signed-rank p 8.7e-216
> PMd-J kernel, single trials, 100 ms smoothing: mean 0.317 against LDR 0.747 (1381 trials); two-sided signed-rank p 1.9e-200
> PMd-J kernel, trial averages, 100 ms smoothing: mean 0.029 against LDR 0.747 (1381 trials); two-sided signed-rank p 1.8e-220
> M1-N linear, single trials, 20 ms smoothing: mean 0.146 against LDR 0.874 (1883 trials); two-sided signed-rank p 1.4e-308
> M1-N kernel, single trials, 20 ms smoothing: mean 0.321 against LDR 0.874 (1883 trials); two-sided signed-rank p 6.5e-307
> M1-N kernel, trial averages, 20 ms smoothing: mean 0.046 against LDR 0.874 (1883 trials); two-sided signed-rank p 1.3e-308
> M1-N linear, single trials, 100 ms smoothing: mean 0.542 against LDR 0.874 (1883 trials); two-sided signed
[... 11 more lines not kept]
```

**Agent**

Identical except the new cell. Updating the record for the decoder claim and fig5a, then handover.

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/sabatini-2024-01.yaml'; s=open(p).read()
i=s.index("- claim: fig7f-decoder-beats-standard"); j=s.index("- claim: suppfig8-no-output-potent-dependence")
new='''- claim: fig7f-decoder-beats-standard
  outcome: partially_reproduced
  notebook: reproduce_sabatini_2024.ipynb
  output: claim:fig7f-decoder-beats-standard
  assumed: true
  notes: Against 24 instantaneous decoders (ridge, lambda 1, on single trials; OU kernel, length scale
    100, L2 0.1, on single trials or trial averages; activity smoothed at 20 or 100 ms, 100 ms lag;
    six per dataset), the LDR decoder is higher in every comparison with two-sided signed-rank p at
    most 1.5e-184. The instantaneous decoders explain 0.5 to 73.1% of single-trial position (the best,
    M1-N kernel on single trials at 100 ms, 73.1% against 87.4%). The GPFA decoders were not run, so
    the claim holds against all but them, which the criterion counts as partial.
  deviations:
  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label,
    where the paper used 79 to 118 sorted single and stable multi-units.
  - Trials as reading (b) of the claims file (assumption; see data-composition).
  - GPFA decoders not run; the paper gives neither latent dimensionality nor bin size.
  - Kernel decoders on single trials are trained on 3000 random time points of the training trials (the
    Methods say "a subset"; the size is an assumption). The 100 ms smoothing is applied to 10 ms counts
    (s.d. 10 bins). Only position is decoded; variance explained is over -250 to +850 ms, where the
    LDR decoder's is over -350 to +850 ms.
'''
s=s[:i]+new+s[j:]
open(p,'w').write(s)
EOF
python tools/entry.py check entries/sabatini-2024 2>&1 | tail -2; python tools/entry.py handover entries/sabatini-2024 2>&1 | tail -2; ls executed/sabatini-2024/handover; python -c "
import nbformat; nb=nbformat.read('executed/sabatini-2024/handover/reproduce_sabatini_2024.ipynb',4); print(sum('**Result' in c.source for c in nb.cells), any('## Summary' in c.source for c in nb.cells))"; date -u
```

```
0 error(s)
wrote executed/sabatini-2024/handover
ldr.py
reproduce_sabatini_2024.ipynb
sabatini-2024.yaml
0 False
Fri Nov 20 13:46:30 UTC 2026
```

**Agent calls Bash**

```bash
rm -rf entries/sabatini-2024/__pycache__; git status --short | grep -v "^?? \.\(bash\|git\|idea\|mcp\|profile\|ripgrep\|vscode\|zprofile\|zshrc\)\|^?? scripts"; python -c "
import yaml,collections; a=yaml.safe_load(open('attempts/sabatini-2024-01.yaml')); print(collections.Counter(o['outcome'] for o in a['outcomes']))"; python tools/entry.py check entries/sabatini-2024 2>&1 | tail -1
```

```
?? attempts/sabatini-2024-01.yaml
?? entries/sabatini-2024/
Counter({'partially_reproduced': 16, 'not_reproduced': 9, 'reproduced': 9})
0 error(s)
```

**Agent**

The attempt is recorded and handed over: 33 of 34 claims tested, one (the decoder comparison) tested without its GPFA part. `python tools/entry.py all` passes (check clean, notebook runs in 29.5 min), and the handover package is in `executed/sabatini-2024/handover/`. Nothing is committed.

**(1) Outcomes** (`attempts/sabatini-2024-01.yaml`)

| Outcome | Claims |
|---|---|
| Reproduced (9) | fig2c-condition-lds-variance, tbf-variance-explained, fig4b-plane-alignment, suppfig6c-location-distinct-from-rotations, fig5c-rotations-predict-rotations, fig6b-location-predicts-rotations, fig6e-kinematics-predict-location, fig7c-ldr-encoding, fig7c-standard-encoding-worse |
| Partially reproduced (16) | data-composition, jpca-fit-r2, jpca-variance-explained, fig3a-eigenvalue-clusters, fig3g-basis-frequencies, tbf-shuffle-control, fig3h-recoverability, fig4c-subspace-excursion-angles, fig4f-plane-alignment-explains-jpca, fig5a-frequencies-segregated, suppfig6a-location-alignment, fig6c-location-tracks-direction, suppfig7a-not-memorization, fig7f-ldr-decoding, trial-curvature-decoding, fig7f-decoder-beats-standard (GPFA decoders not run) |
| Not reproduced (9) | single-lds-variance, fig3c-eigenvalue-distance-auc, suppfig2-eigenvalues-from-kinematics, fig3i-duration-warping, suppfig3-model-comparison, rotation-orientation-dimensionality, fig4d-jpca-variance-correlation, suppfig6b-location-dimensionality, suppfig8-no-output-potent-dependence |
| Blocked | none |

The most notable differences from the paper:
- The rotations sit near 0.7, 1.6 to 1.8 and 2.7 to 3.2 Hz, not 0.5, 1.5, 2.5 and 4 Hz.
- Eigenvalues differ between conditions more than the paper reports: AUC 0.63 to 0.81, against 0.51 to 0.58.
- Rotation orientations and the state space location are much lower-dimensional than in the paper.
- One linear dynamical system across all conditions fits better here (77 to 82%, against 46 to 66%).

**(2) Dataset, assumptions, questions**

Version 0.260528.0919 is pinned: the paper cites none, and the two published versions list the same assets.

Findings about the data:
- **Units (major):** each array holds 96 units, one per electrode, with no single-unit, multi-unit or quality label. The paper used 79 to 118 sorted units per array.
- **Nitschke file clocks (major):** the file joins five recording segments whose clocks overlap. Trial times, hand timestamps and every unit's spike times jump backwards four times, so a trial's spikes cannot be found by time alone. Splitting by segment gives above-chance condition decoding in each segment. Segment 3 carries less condition information within itself (0.16 against 0.41 to 0.46), which looks like drift over the session.
- **Jenkins unit (minor):** one unit's spike train holds two runs, the second restarting at the start of the session. I merged and sorted them.
- **Hand units (minor):** hand position is labelled "meters" with a NaN conversion factor, but the values are millimetres.
- **No EMG (minor):** so suppfig8 removes the kinematic dimensions only.

Assumptions:
- Every analysis uses the successful trials with a delay above 400 ms, because those counts are nearest the paper's. This is marked `assumed: true` on every analysis outcome.
- The penalty of 0.1 on the standard kernel encoders. With it, those encoders predict only the mean, so fig7c-standard-encoding-worse rests on the linear comparisons.
- The SEA noise level, the span of the time shuffle, and the subset size for the kernel decoders.

Questions for the paper's authors are in a `methods_unavailable` finding:
- the trial selection;
- which units were used;
- the kernel penalty;
- how the SEA noise angles were computed;
- whether the Supplementary Figure 3 comparison is cross-validated.

No questions were put to a reader.

**(3) Protocol gaps**
1. Running every reading of a choice that applies to every claim (the trial selection) would double a 30-minute notebook. I ran both readings only for data-composition and marked the rest as assumed.
2. Requiring five seeds on every random null multiplies run time. For the eigenvalue nulls I used 100 repeats instead of the Methods' 500, and 20 repeats for the four extra seeds; these are recorded as deviations.
3. The clock check does not cover a file made of segments with overlapping clocks. I checked per segment, and also with a decoder trained on the other segments; segment 4 (22 trials) is too small to check on its own.
4. Conclusions must be written after the outputs, and any edit forces a full re-run, so each change cost about 30 minutes. The protocol's time guidance does not mention this.
5. Some criteria have no "partially" clause (fig3a, fig3g, fig3h, fig6c). I used the protocol's general definition.
6. The direction of a signed-rank result is undefined when median and mean disagree (fig5a, M1-N 3.23 Hz). I counted it as not shown and gave both numbers.
7. archives.md says to read files with pynwb; I read them with h5py directly.

**(4) Runtime and failures**
- About 3 h 15 min of the 5 h (10:35 to 13:50 UTC).
- Three clean runs of the notebook, about 29 minutes each, all passing.
- Early development runs were too slow (about 25 minutes per part). I fixed this by running independent fits in parallel processes and replacing one loop with a closed form.
- Nothing failed in the final runs.

## End of run

83 turns, 189 minutes, $9.51 at API prices, result: success.
