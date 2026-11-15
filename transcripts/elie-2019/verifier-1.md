# elie-2019 · verifier-1 · run 43520417989

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; find . -maxdepth 2 -type f | head -50
```

```
total 136
drwxr-xr-x 6 runner runner   4096 Nov 13 22:52 .
drwxr-xr-x 8 runner runner   4096 Nov 13 22:52 ..
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 13 22:34 .bash_profile
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 13 22:34 .bashrc
drwxr-xr-x 5 runner runner   4096 Nov 13 22:52 .claude
-rw-r--r-- 1 runner runner      0 Nov 13 22:52 .env
-rw-r--r-- 1 runner runner      0 Nov 13 22:52 .env.development
-rw-r--r-- 1 runner runner      0 Nov 13 22:52 .env.development.local
-rw-r--r-- 1 runner runner      0 Nov 13 22:52 .env.local
-rw-r--r-- 1 runner runner      0 Nov 13 22:52 .env.production
-rw-r--r-- 1 runner runner      0 Nov 13 22:52 .env.production.local
-rw-r--r-- 1 runner runner      0 Nov 13 22:52 .env.test
-rw-r--r-- 1 runner runner      0 Nov 13 22:52 .env.test.local
drwx------ 2 runner runner   4096 Nov 13 22:52 .git
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 13 22:34 .gitconfig
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 13 22:34 .github
-rw-r--r-- 1 runner runner      0 Nov 13 22:52 .gitmodules
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 13 22:34 .idea
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 13 22:34 .mcp.json
[... 56 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "elie-2019.yaml"
}
```

```
1	# Claims for Elie & Theunissen (2019), PLoS Computational Biology 15(9):e1006698, "Invariant neural
2	# responses for sensory categories revealed by the time-varying information for communication calls",
3	# doi:10.1371/journal.pcbi.1006698, on CRCNS data set aa-4 (doi:10.6080/K00C4T06).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record (PMC6762074, open access), as JATS XML flattened to text under
8	# paper/: main text, Methods, Table 1, and the legends of Figures 1 to 10 and of S1 to S7 Fig. The
9	# supplement is the seven figures whose legends are in the text; it has no other file. No PDF was
10	# supplied. The extraction drops every displayed equation: the information formulas, the
11	# coherence-based information (Methods, Time-varying spike rate estimation), the exponential model
12	# of the cumulative information (Results, Time-varying Information for 3 example neurons), the
13	# definition of the CII (Methods, Calculation of the expected value of categorical information) and
14	# the confusion-matrix information. Where the words around an equation or the code fix it, the
15	# criteria say so; where not, the equation is named as open and the reading the text allows is given.
16	# The author may read those equations in the published article (they are not figures). The data
17	# set's description (paper/aa-4.data-description.txt) was read only to know what it holds; no claim
18	# comes from it.
19	#
20	# Code read: https://github.com/julieelie/PoissonTimeVaryingInfo, commit 97802032 (2019-04-01), the
[... 770 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_elie_2019.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain']))
            else: print('--OUT--', list(d.keys()))
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
"
```

```
<persisted-output>
Output too large (32KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/625489a7-8ac1-41f6-b584-d31cd84e4319/tool-results/b7dv2gz4e.txt

Preview (first 2KB):
==================== 0 markdown
# Elie & Theunissen (2019) on CRCNS aa-4

Paper: Elie JE, Theunissen FE (2019). Invariant neural responses for sensory categories revealed by the
time-varying information for communication calls. PLoS Comput Biol 15(9):e1006698,
doi:10.1371/journal.pcbi.1006698.

Dataset: CRCNS aa-4, "Simultaneous extracellular recordings of avian auditory neurons in zebra finches presented
with all the repertoire of vocalizations used by this species for vocal communication", doi:10.6080/K00C4T06,
data description version 0.6 (July 15, 2019). CRCNS data sets are not versioned, so the version is recorded as
`unversioned`; the only published state is the one in `aa-4/live/`, and it is the one read here. The files are
streamed from the public S3 bucket `crcnsarchive`; their MD5 sums in `aa-4/live/checksums.md5`, read on
2026-11-13, are:

| file | md5 |
|---|---|
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/625489a7-8ac1-41f6-b584-d31cd84e4319/tool-results/b7dv2gz4e.txt"
}
```

```
1	==================== 0 markdown
2	# Elie & Theunissen (2019) on CRCNS aa-4
3	
4	Paper: Elie JE, Theunissen FE (2019). Invariant neural responses for sensory categories revealed by the
5	time-varying information for communication calls. PLoS Comput Biol 15(9):e1006698,
6	doi:10.1371/journal.pcbi.1006698.
7	
8	Dataset: CRCNS aa-4, "Simultaneous extracellular recordings of avian auditory neurons in zebra finches presented
9	with all the repertoire of vocalizations used by this species for vocal communication", doi:10.6080/K00C4T06,
10	data description version 0.6 (July 15, 2019). CRCNS data sets are not versioned, so the version is recorded as
11	`unversioned`; the only published state is the one in `aa-4/live/`, and it is the one read here. The files are
12	streamed from the public S3 bucket `crcnsarchive`; their MD5 sums in `aa-4/live/checksums.md5`, read on
13	2026-11-13, are:
14	
15	| file | md5 |
16	|---|---|
17	| data/BlaBro09xxF.tar.gz | ee387cc051e5fa5ee66a5f4db5d8bae6 |
18	| data/GreBlu9508M.tar.gz | 16f1bb223946288f8b426d6382f06510 |
19	| data/LblBlu2028M.tar.gz | 80c181eb8bd70ddbbd9b3aa46587dfb5 |
20	| data/WhiBlu5396M.tar.gz | 2ba7776cd4130d0090b13e5f5c0359fd |
[... 507 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "elie.py"
}
```

```
1	"""Loading and measures for Elie & Theunissen (2019) on CRCNS aa-4.
2	
3	Data. CRCNS aa-4 is unversioned; the files are read from the public S3 bucket
4	crcnsarchive under aa-4/live/data/, one tar.gz per bird. Each tar.gz is read as
5	a stream (tarfile mode "r|gz" over fsspec), each h5 member is opened in memory
6	with h5py, reduced to what the analysis needs, and dropped. Nothing is written
7	to disk.
8	
9	Parameters and where they come from (claims file header, Methods R, B, P):
10	- Window 0 to 600 ms after stimulus onset, 60 bins of 10 ms (Methods B; paper,
11	  Methods, "Here, we analyzed the neural response in the first 600ms").
12	- Call stimuli: in the unit's Call group, stim_type "call" with call types Ag
13	  (Wsst, Ws), Be, DC, Di, LT, Ne, Te, Th, and the songs of the vocalization bank
14	  (So). Whines (Wh), noise and the search songs are dropped (claims header,
15	  selVoc.m; paper, S4 Fig legend).
16	"""
17	from __future__ import annotations
18	
19	import io
20	import tarfile
[... 320 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -l *; grep -n -i -E "914|404|single|snr|anatom|histolog|coordinat|region|ncm|cmm|L2|depth|f32|selected|decod|class_info|extra_info|sortType" aa-4.data-description.txt | head -80
```

```
638 10.1371-journal.pcbi.1006698.txt
   128 aa-4.data-description.txt
   766 total
26:maximum number of stimuli that could be selected in that procedure was therefore 3x7x3 (adult males x 
28:renditions) +10 +20 = 171. The average number of stimuli played for each single unit was 144 (sd = 22, 
36:following avian auditory cortical regions: Field L (including the thalamo recipient L2, the primary 
37:auditory regions L1 and L3), caudolateral and caudomedial mesopallium (CLM and CMM) and 
38:caudomedial nidopallium (NCM). Spike arrival times and spike shapes of multiple units were obtained by 
44:were randomly selected by progressively deepening the penetration of the electrodes and ensuring at 
47:hemisphere at a depth ranging from 400 μm to 2550 μm. 
52:These units were sorted into single units based on spike shape (spike sorting) and twice sorted for the 
53:quality of their neural responses to sounds: before and after spike sorting. This process yielded 914 
54:single auditory units. 
57:single spike train and the actual time-varying mean response, IAR . The thresholds used on IAR to 
60:Single unit isolation was performed off-line using custom software that used a combination of 
64:single units based on spike shape reliability across snippets. The spike shape reliability measure was a 
65:signal to noise ratio (SNR) where the signal was the difference between the maximum and the minimum 
67:used a threshold of 5 SNR to classify units as single units. Using this approach, we extracted 914 single 
69:The data of spike arrival times and stimuli played are saved for each single-unit as an h5 file 
71:site number, “L750”and “R1100” give respectively the depth of the arrays in the left  and right 
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 20,128p aa-4.data-description.txt
```

```
in a sound-attenuated chamber and neural recording were performed while the bird was presented with 
sound stimuli. At each electrophysiological recording site a set of sounds was presented to the subject. 
This set was made from 10 ripple noise stimuli of 2 sec., 20 songs of zebra finches and the vocalizations 
from the repertoire of 10 individuals: three adult females, three adult males, two female chicks and two 
male chicks. From each of these 10 individual caller, we randomly chose 3 call bouts from each category 
or fewer if fewer than 3 call bouts were obtained for that particular call-type and individual. The 
maximum number of stimuli that could be selected in that procedure was therefore 3x7x3 (adult males x 
repertoire x renditions) + 3x6x3 (adult females x repertoire x renditions) + 4x2x3 (juveniles x repertoire x 
renditions) +10 +20 = 171. The average number of stimuli played for each single unit was 144 (sd = 22, 
min = 64, max = 153). Ten trials were acquired for each stimulus with a few exceptions (min=9, max = 
11).  Sounds were broadcasted in a random order. 
 
Neural responses were recorded using the signal of two (5 subjects) or one (1 subject) electrode 
arrays, band-pass filtered between 300Hz and 5kHz (sample frequency 24414.0625 Hz). The electrode 
arrays consisted of two rows of 8 tungsten electrodes with row separation of 500 μm and interelectrode separation within row of 250 μm.  Electrode impedances were approximately 2 MOhms. 
When two electrode arrays were used, they were placed each in one hemisphere, targeting the 
following avian auditory cortical regions: Field L (including the thalamo recipient L2, the primary 
auditory regions L1 and L3), caudolateral and caudomedial mesopallium (CLM and CMM) and 
caudomedial nidopallium (NCM). Spike arrival times and spike shapes of multiple units were obtained by 
voltage threshold. The level of the threshold was set automatically by the software using the variance of 
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=aa-4/" -o list.xml; python3 -c "
import re
x=open('list.xml').read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',x): print(s,k)
print(re.findall(r'<IsTruncated>(.*?)<',x))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live/filelist.txt; echo; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live/data/CRCNSCode.tar.gz | tar tzvf -
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live/data/CRCNSCode.tar.gz | tar xzf - CRCNSCode/h5_plot_one_spike.m CRCNSCode/Zeebee_VocRepertoire_AudNeuron_Tutorial.pdf; cat CRCNSCode/h5_plot_one_spike.m; pdftotext CRCNSCode/Zeebee_VocRepertoire_AudNeuron_Tutorial.pdf - 2>/dev/null | grep -n -i -E "f32|snr|404|914|single|anatom|region|select" | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "S4 Fig|S5 Fig|S6 Fig|Table 1|anatomical|coordinates|histolog" 10.1371-journal.pcbi.1006698.txt | head -40
```

```
25:In this study, we developed a new approach for estimating time-varying information and cumulative information for sensory object identification task. Our approach assumes that time-varying neural responses can be modeled as inhomogeneous Poisson processes and generalizes well to large number of stimulus categories and to long integration times relative to the dynamics of the time-varying response. Our motivation for developing this methodology was to gain additional understanding on the neural representation of communication signals in high level auditory areas. Animal communication calls, just as speech sounds in humans, are categorized into behaviorally meaningful units. Significant progress has been made in identifying brain regions involved in categorizing sounds, in particular in the primate brain, where neural responses that are correlated with progressively more abstracts concepts are found in primary auditory cortex, the lateral belt of the auditory cortex and the prefrontal cortex [ 30 ]. However, the neural computations involved in generating categorical responses remain poorly described [ 31 ] and only a small number of studies have examined the neural categorization of natural communication calls in non-human species [ 32 – 36 ]. We and others have been developing an avian model system to study the neural processing of relatively large and complex vocal repertoires [ 37 , 38 ]. Our prior studies include a detailed bioacoustical analysis of the features that define each call-type of the complete vocal repertoire of the zebra finch [ 39 ] and the first characterization of neural responses to the calls from that large repertoire in primary and secondary avian auditory cortical areas [ 40 ]. In that study, we found that approximately 45% of auditory neurons encode information about call-type categories. Among those, a minority show strong selectivity for single call-type categories and invariance for calls within that category. Here, we investigated the p
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, elie, itertools
from scipy.stats import poisson
rng=np.random.default_rng(0)
mu=rng.uniform(0.05,2,(5,3))
g=np.array([0,0,0,1,2])
# exact cumulative info by enumeration up to y=8
def exact(mu,groups=None,ymax=8):
    S,T=mu.shape
    if groups is None: groups=np.arange(S)
    cats=np.unique(groups)
    out=[]
    for t in range(1,T+1):
        ys=np.array(list(itertools.product(range(ymax+1),repeat=t)))
        ps=np.array([np.prod(poisson.pmf(ys,mu[s,:t]),1) for s in range(S)])
        pc=np.array([ps[groups==c].mean(0) for c in cats])
        py=pc.mean(0)
        H=lambda p:-(p[p>0]*np.log2(p[p>0])).sum()
        out.append(H(py)-np.mean([H(p) for p in pc]))
    return np.array(out)
print('stim exact',exact(mu)); print('stim mc',elie.cum_info_mc(mu,200000,1)); print('stim inst',elie.inst_info(mu))
print('cat exact',exact(mu,g)); print('cat mc',elie.cum_info_mc(mu,200000,1,g)); print('cat inst',elie.inst_info(mu,g))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, elie, itertools
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  (pip install --quiet numpy scipy fsspec h5py 2>&1 || uv pip install --system numpy scipy 2>&1) | tail -3; python3 -c "import numpy, scipy; print(numpy.__version__, scipy.__version__)"
```

```
Exit code 1
error: Failed to install: numpy-2.5.4-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (numpy==2.5.4)
  cause: Failed to create directory `/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/numpy`
  cause: failed to create directory `/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/numpy`: Read-only file system (os error 30)
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy; print(numpy.__version__, scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v && v/bin/pip install --quiet numpy scipy fsspec h5py 2>&1 | tail -2; v/bin/python -c "import numpy, scipy; print(numpy.__version__, scipy.__version__)"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
2.5.4 1.18.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np, elie, itertools
from scipy.stats import poisson
rng=np.random.default_rng(0)
mu=rng.uniform(0.05,2,(5,3))
g=np.array([0,0,0,1,2])
def exact(mu,groups=None,ymax=10):
    S,T=mu.shape
    if groups is None: groups=np.arange(S)
    cats=np.unique(groups)
    out=[]
    H=lambda p:-(p[p>0]*np.log2(p[p>0])).sum()
    for t in range(1,T+1):
        ys=np.array(list(itertools.product(range(ymax+1),repeat=t)))
        ps=np.array([np.prod(poisson.pmf(ys,mu[s,:t]),1) for s in range(S)])
        pc=np.array([ps[groups==c].mean(0) for c in cats])
        py=pc.mean(0)
        out.append(H(py)-np.mean([H(p) for p in pc]))
    return np.array(out)
np.set_printoptions(precision=4)
print('stim exact',exact(mu)); print('stim mc  ',elie.cum_info_mc(mu,200000,1)); print('stim inst',elie.inst_info(mu))
print('cat exact',exact(mu,g)); print('cat mc   ',elie.cum_info_mc(mu,200000,1,g)); print('cat inst ',elie.inst_info(mu,g))
"
```

```
stim exact [0.2946 0.569  0.9185]
stim mc   [0.2949 0.5692 0.9199]
stim inst [0.2946 0.2902 0.4108]
cat exact [0.1006 0.4237 0.6855]
cat mc    [-0.036   0.3496  0.7173]
cat inst  [0.1006 0.3253 0.3207]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" elie-2019.yaml; grep -n "Mask\|Sel\|STRF\|group" elie.py | head
```

```
26
12:- Call stimuli: in the unit's Call group, stim_type "call" with call types Ag
59:    u["groups"] = list(h.keys())
69:            st = {"group": g, "number": sn, **{k: a.get(k) for k in (
144:    caller) are So; the songs of the search set (files STRFxx..._So_*.wav) and the
150:        return None if w.startswith("STRF") else "So"
207:def inst_info(mu: np.ndarray, groups: np.ndarray | None = None) -> np.ndarray:
210:    With groups (a category per stimulus), p(y|c) is the mean of p(y|s) over the
214:    if groups is not None:
215:        cats = np.unique(groups)
216:        p = np.stack([p[groups == c].mean(0) for c in cats])
```

**Agent**

**Verifier report, round 1: Elie & Theunissen 2019 on CRCNS aa-4**

The claims file has 26 claims. The notebook tests one, fig1-model-neurons, and blocks the other 25.

### A. Outcomes

| claim id | my outcome | reason |
|---|---|---|
| units-404 | blocked (methods_underspecified) | Cell 12: 1281 files are labelled single units, 1246 of them with I_AR ≥ 2.3. No file, the data description or the CRCNSCode folder lists the 914 or the 404 units. The criterion's reading (b), redoing the 2015 decoding, was not attempted, and the 914 count was not even approached (B1). |
| units-337 | blocked (methods_underspecified; too_large also applies) | Depends on units-404. Cell 15 estimates about 124 h on one core for the KDE rates alone. |
| s1-temporal-resolution | blocked (methods_underspecified) | Depends on units-404. The variant on 1246 units (cell 18: 65.8 ± 19.0% below 50 Hz, 1245 units losing more than 5%) decides nothing. The power part was not computed at all. |
| fig1-model-neurons | partially_reproduced | Cell 21, temporal neuron: mean \|KDE − model\| is 0.009 spikes/ms (< 0.02); bias-corrected peak instantaneous information is 0.519 bits (0.500 uncorrected; within 0.5 ± 0.05); cumulative information reaches 1.928 bits (≥ 1.8). The MATLAB tutorial's saved results agree (0.502; 1.894). The rate and onset neurons are not in the repository, so "each model neuron" holds for one of three. |
| fig2a-poisson-test | blocked (methods_underspecified) | Depends on units-404. No variant was run. |
| fig2cd-fano-factor | blocked (methods_underspecified) | Depends on units-404. The variant on 1246 units gives 1.027 (SEM 0.002), significantly different from 1; it decides nothing. |
| fig2b-noise-correlations | blocked (methods_underspecified) | Depends on units-404. The variant gives a noise-correlation median of 0.152, outside the ±0.05 band, and a stimulus-correlation median of 0.29 (over stimuli) or 0.24 (within stimulus); it decides nothing. |
| fig3-5-example-neurons | blocked (methods_underspecified) | The paper does not name the units. The S4 to S6 raster images are not in the materials, and the notebook shows no attempt to match them, which the criterion allows. |
| fig6a-onset-sustained-information, fig6c-new-information, fig6b-fixed-rate-fraction, fig7a-time-constants, fig7b-k300, k300-rate-regression, fig9a-mean-cii, fig9a-top-quartile, s7-invariant-information, fig9b-cii-tau-ratio, fig9c-cii-k300, cii-unimodal | blocked (methods_underspecified; too_large also applies) | Each depends on units-337, directly or through fig7a or fig9a-top-quartile, and units-337 is blocked. |
| table1-anatomy-counts, fig10-cii-distance, fig10-cii-area-anova, fig10-tau-k300-distance, fig10-no-anatomy-categorical | blocked (methods_underspecified) | All depend on units-337. The notebook's own reason ("no anatomical location in the data set") is not shown: the `extra_info` group was never opened (B3). |
| s2-spike-counts | blocked (methods_underspecified) | Depends on units-404. The variant on 1246 units gives max 9, 442 bins at 8, and a mean of 0.132; it decides nothing. |

No claim states a chance level for a selection, so there was no chance level to compare.

### B. Problems

1. **[does not affect a conclusion] Cell 13 says the `.f32` snippet files are undocumented. They are documented.** `CRCNSCode/h5_plot_one_spike.m`, inside the archive's `CRCNSCode.tar.gz`, reads them: 18 float32 samples per snippet, indexed by the `spike_ids` that `read_unit` already loads. That makes the 2015 SNR > 5 criterion, and so the 914 count, computable at least for the sites that have snippets. The notebook also never shows which sites have `.f32` files. The outcome stays blocked because the 404 still needs the 2015 decoding.

2. **[does not affect a conclusion] Cell 12 skips a check against the data description.** The description gives 1401 spike-sorted auditory units at I_AR ≥ 2.3. The notebook never counts the `_ss` files (any `sortType`) at that threshold, which would test whether its I_AR reading matches the authors'.

3. **[does not affect a conclusion] `read_unit` does not support the anatomy blocking reason.** It records only that `extra_info` exists (`has_extra_info`) and never reads its contents. "No anatomical location in the data set" is therefore unverified. The anatomy claims are blocked anyway through units-337.

4. **[does not affect a conclusion] `read_unit` contradicts the module docstring on stimulus selection.** The docstring says call stimuli come from "the unit's Call group", but the code takes stimuli of type call or song from every group, including Sel1–7, Mask1 and STRF1. This may explain why cell 4 finds 95.4 call stimuli per unit against the paper's 114, and 1874 unit-stimulus pairs with 12 trials against the description's maximum of 11. It affects only the non-deciding variants of cell 18.

5. **[does not affect a conclusion] `cum_info_mc` with `groups` is wrong when categories have unequal sizes.** It mixes a stimulus-weighted p(y) with category-weighted conditional entropies. I checked it against exact enumeration on a synthetic case (5 stimuli in groups {0,0,0,1,2}, 3 bins):

   | | bin 1 | bin 2 | bin 3 |
   |---|---|---|---|
   | exact | 0.101 | 0.424 | 0.686 |
   | `cum_info_mc` | −0.036 | 0.350 | 0.717 |

   It also disagrees with `inst_info` at bin 1. The stimulus version matches exact to about 0.001 bits. Category cumulative information is not used for any outcome here, but it would bias every category claim if those were run.

6. **[does not affect a conclusion] Cell 21 departs from Method I in three ways:**
   - It uses a fixed 200,000 samples instead of the code's adaptive chunks targeting 0.2 bits.
   - It uses jackknife SE instead of 20 bootstraps of the jackknife.
   - It never applies the 0.6-bit stopping rule.

   Its common-random-numbers assumption decides the curve: with independent draws the curve goes to 2.206 bits, above the 2-bit maximum, and ends at 0.803. The fig1 conclusion still stands because the MATLAB tutorial's saved results (peak 0.502, last 1.894) agree with the common-random-numbers run.

7. **[does not affect a conclusion] Cell 18: the coherence variant uses the stored `class_info` curve, which runs from 4 to 496 Hz.** That may not be the S1 Fig computation, so the 65.8% says nothing about the paper. The power part of s1 is not computed.

8. **[does not affect a conclusion] Cell 15: the cost argument is a valid second reason (too_large) for the 337-dependent claims, but the notebook does not name it as a blocking reason.**

I found no place where the claims file misreads the paper for the claims at issue.

### C. What I could not check, and the output that would have let me

- **Anatomy in the files:** a dump of the keys and attributes of one `extra_info` group, and of one `class_info` group beyond coherence.
- **Stimulus selection:** per-group counts of stimuli with type call or song (Call, Call1–3, Sel*, Mask1, STRF1), and whether the same `stim_md5` appears in more than one group for a unit.
- **The 914 route:** a count of `.f32` files per bird and site, and the SNR distribution for the units that have them.
- **The 1401 check:** the count of `_ss` files of any `sortType` with I_AR ≥ 2.3.
- **fig3-5:** a comparison against the S4 to S6 Fig images, or a statement that they were inspected and could not be matched.
- **fig1 under the paper's procedure:** the cumulative information with the code's adaptive sample size, its bootstrap error and the 0.6-bit stop. That would settle whether the 1.8-bit result depends on the common-random-numbers assumption.

The other 25 claims were not run by the notebook, so I could form no outcome on them beyond blocked. To check the archive I listed the S3 bucket and opened only the 389 KB `CRCNSCode.tar.gz`; no bird data was downloaded.

## End of run

17 turns, 3 minutes, $1.16 at API prices, result: success.
