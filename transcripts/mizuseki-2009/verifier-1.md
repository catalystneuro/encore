# mizuseki-2009 · verifier-1 · run 42714134449

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; find . -maxdepth 2 -type f | head -50
```

```
total 328
drwxr-xr-x 6 runner runner    4096 Nov  9 22:54 .
drwxr-xr-x 7 runner runner    4096 Nov  9 22:54 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  9 22:41 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  9 22:41 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  9 22:54 .claude
-rw-r--r-- 1 runner runner       0 Nov  9 22:54 .env
-rw-r--r-- 1 runner runner       0 Nov  9 22:54 .env.development
-rw-r--r-- 1 runner runner       0 Nov  9 22:54 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  9 22:54 .env.local
-rw-r--r-- 1 runner runner       0 Nov  9 22:54 .env.production
-rw-r--r-- 1 runner runner       0 Nov  9 22:54 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  9 22:54 .env.test
-rw-r--r-- 1 runner runner       0 Nov  9 22:54 .env.test.local
drwx------ 2 runner runner    4096 Nov  9 22:54 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  9 22:41 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  9 22:41 .github
-rw-r--r-- 1 runner runner       0 Nov  9 22:54 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  9 22:41 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  9 22:41 .mcp.json
[... 60 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "mizuseki-2009.yaml"
}
```

```
1	# Claims for Mizuseki, Sirota, Pastalkova & Buzsaki (2009), Neuron 64, 267-280, "Theta Oscillations
2	# Provide Temporal Windows for Local Circuit Computation in the Entorhinal-Hippocampal Loop",
3	# doi:10.1016/j.neuron.2009.08.037, on CRCNS data set hc-2.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
5	# protocol as stated in docs/protocol.md (Reader).
6	#
7	# Text read: the version of record with its supplement (Supplemental Data, 678d1873-mmc1_1.pdf),
8	# as supplied under paper/ (PyMuPDF text): main text, figure legends, the short Experimental
9	# Procedures, the Supplemental Experimental Procedures, Table S1 and the legends of Figures S1 to
10	# S19. The text prints degree signs, minus signs and "approximately" as a replacement character;
11	# those values were read from the PDF. Table S1 is an image in the supplement and was read from
12	# the rendered page. Figure 3D and 3H (significance marks), Figure 4 (arrows) and Figure 7 (the
13	# percentages and n above each panel) were read from the rendered pages. The CRCNS data
14	# description (paper/hc-2.data-description.txt) was read for the layout of the deposit only; no
15	# claim comes from it.
16	#
17	# Code: the paper links no code. Its analyses were "carried out by custom-written MATLAB-based
18	# software" (Supplemental Experimental Procedures), not published with it. Every method below
19	# comes from the paper and its supplement alone.
20	#
[... 875 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('mizuseki-2009.yaml'));print(len(d['claims']));[print(c['id']) for c in d['claims']]"
python3 - <<'EOF'
import json
nb=json.load(open('reproduce_mizuseki_2009.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"===== CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain'])[:6000])
            else: print('--OUT-- ',list(d.keys()))
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
EOF
```

```
<persisted-output>
Output too large (71.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/a08ed2ae-0cb7-4301-a6b8-aa94b7c592c6/tool-results/b40ij87x6.txt

Preview (first 2KB):
37
tables1-cell-counts
fig2c-ec-cell-classes
figs4-ec2-bursting
fig1-ec3-ca1-theta-coherence
fig1-layer-reversals
fig3-interneurons-min-ascending
fig3-dg-ca3-precede-ca1
fig3-ec-opposite-to-targets
fig3c-ec3-subset-locked
fig3-ec5-weakest
fig3d-ec2-strongest-modulation
fig3d-hippocampal-modulation
figs8-task-invariance
figs9-phase-method
figs10-ca1-reference
[... 39 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/a08ed2ae-0cb7-4301-a6b8-aa94b7c592c6/tool-results/b40ij87x6.txt"
}
```

```
1	37
2	tables1-cell-counts
3	fig2c-ec-cell-classes
4	figs4-ec2-bursting
5	fig1-ec3-ca1-theta-coherence
6	fig1-layer-reversals
7	fig3-interneurons-min-ascending
8	fig3-dg-ca3-precede-ca1
9	fig3-ec-opposite-to-targets
10	fig3c-ec3-subset-locked
11	fig3-ec5-weakest
12	fig3d-ec2-strongest-modulation
13	fig3d-hippocampal-modulation
14	figs8-task-invariance
15	figs9-phase-method
16	figs10-ca1-reference
17	fig4a-ec-hippocampus-offsets
18	fig4a-pair-offset-ranges
19	fig4a-ec5-ca1-flat
20	fig4-ec2-ec3-opposite-lags
[... 759 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/a08ed2ae-0cb7-4301-a6b8-aa94b7c592c6/tool-results/b40ij87x6.txt",
 "offset": 780,
 "limit": 520
}
```

```
780	6         7  28    143       142.97    0.25              -12.95
781	7         8  32    128       131.51    0.28              -11.45
782	8         9  36    104       127.73    0.30               -3.78
783	9        10  40    148       117.86    0.31               -9.87
784	  shift 4 Hz -> >=40 Hz: circular -130.2 deg, summed path -130.2 deg (negative = advance to earlier phase)
785	  Spearman of mean R with category: rho 0.28
786	
787	--OUT--
788	int
789	   category  Hz  cells  group_phase  mean_R  step_from_previous
790	0         1   4     97       213.31    0.40                 NaN
791	1         2   8     92       199.62    0.39              -13.69
792	2         3  12     87       189.38    0.38              -10.25
793	3         4  16     78       174.77    0.35              -14.61
794	4         5  20     76       166.50    0.34               -8.27
795	5         6  24     73       164.84    0.33               -1.66
796	6         7  28     70       164.61    0.32               -0.23
797	7         8  32     65       162.65    0.31               -1.95
798	8         9  36     62       162.84    0.32                0.18
799	9        10  40     64       153.68    0.29               -9.16
[... 496 more lines not kept]
```

**Agent**

Notebook read (38 cells, 12 claims tested on CA1). Now the helper module.

**Agent calls Read**

```json
{
 "file_path": "hc2.py"
}
```

```
1	"""Loading and theta measures for CRCNS hc-2 (Mizuseki, Sirota, Pastalkova & Buzsaki 2009).
2	
3	The data set hc-2 (doi:10.6080/K0Z60KZ9) holds 21 open-field sessions of three rats (ec13, ec14,
4	ec16) with a silicon probe in CA1. It is not versioned on CRCNS; the files read are pinned by the
5	MD5 sums of the data set's ``checksums.md5`` (``session_md5``).
6	
7	Each session is one ``<session>.tar.gz`` in the public bucket ``crcnsarchive`` (all files but the
8	wideband ``.dat`` and the video). The tarball is streamed once over HTTP with ``fsspec`` and
9	``tarfile`` in stream mode, nothing written to disk, and reduced as it is read
10	(``load_session``): spike times and cluster ids of isolated units (cluster 2 and above, data
11	descriptor 2b), each unit's mean waveform from the ``.spk`` files, the head position from the
12	``.whl`` file, and one LFP channel (the CA1 pyramidal layer channel, below).
13	
14	Where each parameter comes from:
15	
16	- Theta band 5-11 Hz, maxima method for the phase (peak 0 and 360 degrees, trough 180), Hilbert
17	  and minima methods: Supplemental Experimental Procedures (SEP), paragraph "Theta periods were
18	  detected ...". The filter is not named (claims file, O3); a zero-phase 4th-order Butterworth
19	  band-pass is a standard choice.
20	- Theta epochs: SEP, ratio of 5-11 Hz power to the 1-4 and 12-14 Hz bands, with a manual
[... 481 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat paper/hc-2.data-description.txt | head -150; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Notebook and helper read. Next: check Table S1, Figure S6/S11 legends, and the archive file list.

**Agent calls Bash**

```bash
cd  python3 -c "import fitz;print(fitz.__doc__)"; grep -n -i "S6\|S11\|Table S1\|square\|identified" paper/10.1016-j.neuron.2009.08.037.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1120,1135p paper/10.1016-j.neuron.2009.08.037.txt; sed -n 1415,1440p paper/10.1016-j.neuron.2009.08.037.txt; sed -n 1595,1615p paper/10.1016-j.neuron.2009.08.037.txt; sed -n 1700,1725p paper/10.1016-j.neuron.2009.08.037.txt; sed -n 1520,1560p paper/10.1016-j.neuron.2009.08.037.txt; grep -n -i "Hilbert" paper/10.1016-j.neuron.2009.08.037.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm pdfimages mutool; python3 -c "import pypdf" 2>&1; python3 -c "import pdfplumber" 2>&1; pip list 2>/dev/null | grep -i -E "pdf|mupdf|pillow"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2009.08.037.supp.pdf",
 "pages": "9"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Can't render Table S1 here, so I'll go by the claims file. Next, the archive file list.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -m 60 https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-2/checksums.md5 -o hc2md5.txt; wc -l hc2md5.txt; awk '{print $2}' hc2md5.txt | cut -d/ -f1 | sort | uniq -c | head -40; grep -v "tar.gz" hc2md5.txt | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -E "ec01" hc2md5.txt | awk '{print $2}' | head -80; curl -s -m 60 https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-2/filelist.txt | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -m 60 -O https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-2/docs/crcns-hc2-shank_maps.doc; curl -s -m 60 -O https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-2/crcns-hc2-scripts.zip; strings -n 4 crcns-hc2-shank_maps.doc | head -60; unzip -l crcns-hc2-scripts.zip
```

Result: the fetched text is not kept.

**Agent**

Archive confirms only CA1 open-field data (plus shank maps and loader scripts). Now testing the helpers on synthetic inputs.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import sys, types
try:
    import fsspec
except ImportError:
    sys.modules['fsspec']=types.ModuleType('fsspec')
import numpy as np, hc2
from scipy import stats
fs=hc2.FS_LFP; t=np.arange(0,20,1/fs)
y=np.cos(2*np.pi*8*t)
yf=hc2.theta_filter(y)
for w in ['max','min']:
    ph,_=hc2.phase_extrema(yf,w)
    un=hc2.unwrap_phase(ph)
    # spikes at troughs
    tt=np.arange(1,19,1/8)+1/16
    print(w, np.round(hc2.circ_stats(hc2.spike_phase(tt,un))[:2],2))
un=hc2.unwrap_phase(hc2.phase_hilbert(yf)); print('hil',np.round(hc2.circ_stats(hc2.spike_phase(np.arange(1,19,1/8)+1/16,un))[:2],2))
# Rayleigh vs scipy-like exact via simulation
rng=np.random.default_rng(0)
ps=[hc2.circ_stats(rng.uniform(0,360,100))[2] for _ in range(4000)]
print('uniform false pos rate p<0.01', np.mean(np.array(ps)<0.01), 'p<0.05',np.mean(np.array(ps)<0.05))
# inst rate
s=np.array([0,0.1,0.2,0.3, 1.0]); print(hc2.inst_rate_count(s))
b,si=hc2.isi_groups(np.array([0,0.003,0.1,0.13,0.2])); print(b,si)
# waveform
w=np.zeros((32,2)); w[15,0]=-100; w[22,0]=30; w[10,0]=10
print(hc2.waveform_features(w))
# theta ratio on pure 8 Hz + noise
r=hc2.theta_ratio(y+0.1*rng.standard_normal(len(y)))[1]; print('ratio',np.median(r))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /usr/bin/python3* /usr/local/bin/python* 2>/dev/null; which -a python python3 uv pip3; python3 -c "import yaml; print('yaml ok')"
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip3
/usr/bin/pip3
/bin/pip3
yaml ok
```

**Agent calls Bash**

```bash
cd  for p in /usr/bin/python3 /usr/bin/python3.14; do $p -c "import numpy,scipy;print('$p ok')" 2>&1 | tail -1; done; uv --version; uv venv $TMPDIR/v -q 2>&1 | tail -1 && uv pip install -q --python $TMPDIR/v/bin/python numpy scipy 2>&1 | tail -2
```

```
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
uv 0.13.7 (x86_64-unknown-linux-gnu)
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import sys, types
sys.modules['fsspec']=types.ModuleType('fsspec')
import numpy as np, hc2
fs=hc2.FS_LFP; t=np.arange(0,20,1/fs)
y=np.cos(2*np.pi*8*t)
yf=hc2.theta_filter(y)
tt=np.arange(1,19,1/8)+1/16
for w in ['max','min']:
    ph,_=hc2.phase_extrema(yf,w)
    print(w, np.round(hc2.circ_stats(hc2.spike_phase(tt,hc2.unwrap_phase(ph)))[:2],2))
print('hil',np.round(hc2.circ_stats(hc2.spike_phase(tt,hc2.unwrap_phase(hc2.phase_hilbert(yf))))[:2],2))
rng=np.random.default_rng(0)
ps=np.array([hc2.circ_stats(rng.uniform(0,360,60))[2] for _ in range(5000)])
print('uniform FP p<0.01', np.mean(ps<0.01), 'p<0.05',np.mean(ps<0.05))
print(hc2.inst_rate_count(np.array([0,0.1,0.2,0.3,1.0])))
print(hc2.isi_groups(np.array([0,0.003,0.1,0.13,0.2])))
w=np.zeros((32,2)); w[15,0]=-100; w[22,0]=30; w[10,0]=10
print(hc2.waveform_features(w))
print('ratio',np.median(hc2.theta_ratio(y+0.1*rng.standard_normal(len(y)))[1]), np.median(hc2.theta_ratio(rng.standard_normal(len(y)))[1]))
# pink noise ratio
x=np.cumsum(rng.standard_normal(len(y))); x=x-np.convolve(x,np.ones(1250)/1250,'same')
print('brown noise ratio', np.median(hc2.theta_ratio(x)[1]))
ev=np.array([[1.0,2.5],[4,5]]); print(hc2.in_epochs(np.array([0.5,1,2.49,2.5,4.5,6]),ev))
EOF
```

```
max [180.05   1.  ]
min [180.   1.]
hil [180.   1.]
uniform FP p<0.01 0.0094 p<0.05 0.0512
[2 3 3 2 1]
(array([ True,  True, False, False, False]), array([False, False,  True,  True,  True]))
(0.35, np.float64(0.5), 0)
ratio 3941.999134898603 1.02118678201072
brown noise ratio 0.16264705816265165
[False  True  True False  True False]
```

**Agent**

I checked all 37 claims in the claims file. The notebook tests 11 of them on CA1 alone. It treats `tables1-cell-counts` and the other 25 claims as blocked. The archive's own file list (`checksums.md5`, `filelist.txt`, shank maps) confirms that hc-2 holds only 21 open-field sessions with CA1 probes, from rats ec13, ec14 and ec16.

My outcomes: 5 reproduced, 2 partially reproduced, 4 not reproduced and 26 blocked. One of the blocked claims, `figs6-identified-cells`, could be partly tested on CA1 but was not attempted.

## A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| tables1-cell-counts | blocked (metadata_insufficient) | The per-rat counts cover all tasks, and hc-2 holds only the open field. For the open-field totals (paper 1083 principal cells / 188 interneurons; hc-2 739 / 181 counted session by session, cell 14), the notebook asserts the paper's figure "includes i01" but shows nothing to support it. Whether hc-2 holds all of the paper's open-field sessions is also unknown. |
| fig3d-hippocampal-modulation | partially_reproduced | Mean R 0.193 is inside 0.19±0.019. Percent modulated is 93.0% against 84±8.4 (limit 92.4), so just outside (cell 16). Two of the four theta-epoch variants fall inside (91.1%, 92.0%; cell 17). The CA1-vs-CA3/DG comparisons cannot be tested. |
| fig3-interneurons-min-ascending | reproduced (CA1 only) | Minimum bin is 335° for principal cells and 315° for interneurons. Both stay inside reading (a), 180–360°, after converting to EC3 phase with the 0–80° shift (255–335° and 235–315°). The result is stable across rats, cell-type rules and epoch variants (cell 19). |
| figs9-phase-method | reproduced | Maxima, minima and Hilbert methods differ by at most 0.7° (cell 21). |
| fig5-rate-phase-shift | not_reproduced | CA1 principal cells advance by 130.2° from 4 Hz to ≥40 Hz; the criterion needs more than 135° (cell 23). Every variant gives 129–131°. Only the single-cell variant (−137°, which the criterion reports but does not judge on) and rat ec14 (−147°) exceed 135°. The EC2 part cannot be tested. |
| fig5b-burst-double-peak | not_reproduced | Burst spikes and ≥40 Hz spikes differ by 154°; the criterion requires under 90° (cell 25). The two-peak part does hold under both readings (peaks at 235° and 25°; the two-component BIC is lower). |
| figs13-interneuron-rate | not_reproduced | The largest pairwise difference is 59.6°, above the 33° limit (cell 27). It stays above 33° under every cell-type and epoch variant (minimum 43.2°). |
| figs12b-burst-single-phase | reproduced (CA1) | 64 of 226 cells (28%) under reading (a) and 177 of 226 (78%) under reading (b), each against 5% chance, binomial p ≤ 3e-30 (cell 29). |
| figs19-fast-firing-minority | reproduced (CA1) | Low against high rates: 0.546 vs 0.049 under reading (a), 0.662 vs 0.338 under (b); this holds in every rat (cell 31). The EC part cannot be tested. |
| figs7-individual-rats | reproduced (CA1) | Largest difference between rats is 8.5° for principal cells and 31.9° for interneurons, inside both 45° and 90° (cell 33). |
| figs11-phase-time-agreement | partially_reproduced | After wrapping the lag to one cycle, principal–interneuron pairs give r = 0.614 (circular 0.659), which passes. Principal–principal pairs give r = 0.146 (circular 0.205), which fails. All pairs pooled give r = 0.361, which also fails (cell 35). |
| figs2-ripple-sequence | not_reproduced | Firing increase during ripples, principal cells: 10.05× under baseline (a), 7.41× under (b), against 6±0.6. Interneurons: 4.41× and 2.12× against 3±0.3. No baseline reading puts either group inside tolerance (cell 37). The onset/peak delays need EC data and cannot be tested. |
| figs6-identified-cells | blocked (other: not attempted) | Figure S6 includes hippocampal neurons. The jitter test for monosynaptic pairs can be run on hc-2's CA1 spike times (20 kHz), so the CA1 part could be tested. "data_missing" is wrong for that part. |
| figs16-open-field-smallest-shift | blocked (data_missing) | Open field is the only task, so the comparison between tasks cannot be tested. The criterion still asks for the open-field median shift to be reported, and the notebook does not report it. |
| fig2c-ec-cell-classes, figs4-ec2-bursting, fig1-ec3-ca1-theta-coherence, fig1-layer-reversals, fig3-dg-ca3-precede-ca1, fig3-ec-opposite-to-targets, fig3c-ec3-subset-locked, fig3-ec5-weakest, fig3d-ec2-strongest-modulation, figs10-ca1-reference, fig4a-ec-hippocampus-offsets, fig4a-pair-offset-ranges, fig4a-ec5-ca1-flat, fig4-ec2-ec3-opposite-lags, discussion-ec-interneurons-with-ec2 | blocked (data_missing) | Each needs EC units or EC LFP, or CA3/DG units. The archive has none: no EC probe, and only CA1 shanks in the shank maps. Every bursting ordering in `figs4-ec2-bursting` involves EC, CA3 or DG. |
| figs8-task-invariance, fig6-hippocampal-precession, fig7a-precession-strength, figs15-ec3-no-precession, fig7b-frequency-shift, figs18-spike-phase-spectrum, fig7-ca1-highest-precession | blocked (data_missing) | Each needs several tasks, linear-track sessions, EC groups, or results that depend on those. The archive holds only open-field sessions. |
| fig8-ec-population-predicts-sinks | blocked (data_missing) | Needs the CSD data of Montgomery et al. and EC populations; neither is in hc-2. |

## B. Problems

1. **[affects a conclusion]** `hc2.classify` (cells 12 and 14). The main rule (trough-to-peak below 0.4 ms or rate above 10 Hz) labels 104 units firing at or below 1 Hz as interneurons. The "int" group's median rate is 0.24 Hz, which is implausible for CA1 interneurons under the methods the paper cites. The stricter variant `type_v3` (77 interneurons) was run for cells 19, 27 and 33 but not for `figs2-ripple-sequence` (interneuron fold, cell 37) or `figs11-phase-time-agreement` (principal–interneuron pairs, cell 35). It also decides whether hc-2's interneuron count matches Table S1's 188 (181 vs 77).
2. **[affects a conclusion]** `figs6-identified-cells` is blocked as data_missing, but its CA1 part is testable on hc-2 (Figure S6 covers hippocampal cells; the jitter test needs only spike times).
3. **[affects a conclusion]** `figs2-ripple-sequence`, cell 37. Firing increase is computed only as peak over baseline of the cell-averaged rate, which high-rate cells dominate. A per-cell fold (median of each cell's ratio) is another reading of the paper's open "fold increase" and was not run. Ripples also come only from pauses in the open field; the paper's Figure S2 ripple set is not stated. Either could move the result into or out of tolerance.
4. **[affects a conclusion]** `tables1-cell-counts`, cells 13 and 14. The claim that the open-field 1083/188 includes rat i01 is unsupported. If i01 had no open-field sessions, the open-field totals are testable (739 principal cells, outside 1083±108; 181 interneurons, inside 188±19), unless hc-2 holds only some of those sessions.
5. **[does not affect a conclusion]** Cell 35, `figs11-phase-time-agreement`. The pooled "all" correlation includes interneuron–interneuron pairs, which Figure S11 does not show (it has only principal–principal and principal–interneuron pairs). The per-category results are what decide the outcome.
6. **[does not affect a conclusion]** Cell 29, `watson_williams`. The test treats spikes as independent, which inflates significance (78% of cells). The formula itself is correct (Zar), and reading (a) passes anyway.
7. **[does not affect a conclusion]** Cell 6, `_pick_pyramidal_channel`. In ec013.808 (channel 0, r = 0.893) and ec013.844 the session-mean principal-cell phase is 248–265°, against about 200–220° in other sessions (cell 33). This may mean the reference channel is off the pyramidal layer. Results by rat are robust to it.
8. **[does not affect a conclusion]** `figs16-open-field-smallest-shift`. The open-field unit–LFP frequency shift for CA1 that the criterion asks to be reported is missing.
9. **[does not affect a conclusion]** Cell 0, summary table. It says "fig3 EC and CA3/DG claims (5)"; there are 4 besides `fig3d-ec2-strongest-modulation`, which is listed separately. All 37 claims are still covered.
10. **[does not affect a conclusion]** Theta reference and epochs use the CA1 pyramidal-layer LFP instead of EC3, with the ratio threshold, speed threshold and pixel scale as assumptions. These are stated and varied, and outcomes are stable across the variants. For `figs7-individual-rats`, a single CA1 reference may make rats look more alike than the paper's EC3 reference would.

The helper functions behave correctly on synthetic inputs:
- **Phase methods:** a spike at the trough reads 180° under the maxima, minima and Hilbert methods.
- **Rayleigh test:** on uniform data it gives false positives at 0.94% for p < 0.01 and 5.1% for p < 0.05.
- **Rate, ISI and epoch helpers:** `inst_rate_count`, `isi_groups` and `in_epochs` give the expected outputs.
- **`waveform_features`:** returns a trough-to-peak latency of 0.35 ms for a 7-sample gap at 20 kHz.

## C. What I could not check

- **Table S1:** it is an image, and no PDF renderer is available here, so I could not see whether its "square" column is broken down by rat or includes i01. A per-rat Table S1 printout next to hc-2's per-rat counts would settle `tables1-cell-counts`.
- **Session coverage:** whether hc-2's 21 sessions are all of the paper's open-field sessions for these rats. A list of the paper's sessions is needed and is not public.
- **Data loading:** I could not check it against the raw files without downloading them. Printing the `.clu` header counts against the unique cluster ids would have helped.
- **Outputs that would have let me settle more** if added to the notebook:
  - `figs2-ripple-sequence` and `figs11-phase-time-agreement` rerun under `type_v3`;
  - per-cell fold-increase distributions for ripples;
  - mean rate against trough-to-peak latency for the "int" units;
  - the jitter test for monosynaptic pairs on CA1 (for `figs6-identified-cells`);
  - the CA1 open-field unit–LFP frequency shift (for `figs16-open-field-smallest-shift`);
  - the depth of the reference channel against the shank maps in hc-2's docs.

## End of run

19 turns, 5 minutes, $1.77 at API prices, result: success.
