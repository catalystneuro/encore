# fujisawa-2008 · verifier-1 · run 43785776344

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 308
drwxr-xr-x 6 runner runner    4096 Nov 16 01:51 .
drwxr-xr-x 8 runner runner    4096 Nov 16 01:51 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 01:21 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 01:21 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 16 01:51 .claude
-rw-r--r-- 1 runner runner       0 Nov 16 01:51 .env
-rw-r--r-- 1 runner runner       0 Nov 16 01:51 .env.development
-rw-r--r-- 1 runner runner       0 Nov 16 01:51 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 16 01:51 .env.local
-rw-r--r-- 1 runner runner       0 Nov 16 01:51 .env.production
-rw-r--r-- 1 runner runner       0 Nov 16 01:51 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 16 01:51 .env.test
-rw-r--r-- 1 runner runner       0 Nov 16 01:51 .env.test.local
drwx------ 2 runner runner    4096 Nov 16 01:51 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 01:21 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 01:21 .github
-rw-r--r-- 1 runner runner       0 Nov 16 01:51 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 01:21 .idea
[... 39 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "fujisawa-2008.yaml"
}
```

```
1	# Claims for Fujisawa, Amarasingham, Harrison & Buzsaki (2008), Nature Neuroscience 11:823-833,
2	# doi:10.1038/nn.2134, tested on DANDI:000067 and CRCNS pfc-2 (doi:10.6080/K01V5BWK).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-15,
4	# protocol as stated in docs/protocol.md (version pilot-15, Reader). It replaces the two files
5	# read per dataset, claims/fujisawa-2008/000067.yaml and claims/fujisawa-2008/crcns-pfc-2.yaml;
6	# their ids are kept where the finding is the same (map below).
7	#
8	# Text read. The version of record (PDF supplied by a person; text by PyMuPDF in
9	# paper/10.1038-nn.2134.txt): main text, figure legends, Methods, and the supplement (Supplementary
10	# Note; legends of Supplementary Figures 1 to 16; references). PDF pages were opened only for
11	# figures the text garbles: Figure 2 (the counts and t-test marks of panels d and e), Figure 3
12	# (legend of 3b, the matrix size printed as 117 squared), Supplementary Figures 1 to 3, and the
13	# legend of Supplementary Figure 11 (142 squared). Where the extracted text prints "1172" and
14	# "1422" the PDF has 117^2 and 142^2 (a lost superscript); quotes keep the extracted text. The
15	# paper links no analysis code; its only link is to the KlustaKwik spike sorter, which was not
16	# read, as it is not analysis code of the paper.
17	#
18	# The datasets. DANDI:000067 is titled with the paper's title and carries its abstract as
19	# description. The CRCNS pfc-2 description says it holds simultaneous PFC (64 channels) and CA1
20	# (32 channels) recordings in three rats (EE, FF, GG) during the working memory task of this
[... 995 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "fujisawa.py"
}
```

```
1	"""Loading and measures for Fujisawa, Amarasingham, Harrison & Buzsaki (2008), Nat Neurosci 11:823.
2	
3	Data come from two archives, both streamed (nothing is written to disk):
4	
5	- DANDI:000067, pinned at DANDI_VERSION. Spike times, shank and cluster of every unit, the raw
6	  wideband signal (for the channel map check) and the head LED positions are read from the NWB
7	  files with remfile and h5py.
8	- CRCNS pfc-2 (doi:10.6080/K01V5BWK, unversioned; MD5 sums in CRCNS_MD5). The lab's summary
9	  files: SessionNP (correct trials: first poke start, last poke end = trial start, reward start =
10	  trial end, side R=1 L=2), the extended whl file (linearised position d in 1..2 at 39.0625 Hz),
11	  spikeph (unit -> shank, cluster), CellsInfo (the units of each session and the lab's cell
12	  type), and EE188_example.mat (the 117 cells of the paper's Figure 2a / 3 session and the lab's
13	  list of connections, pairs_all). The example file is read from inside EE.188.tar.gz by
14	  streaming the archive (about 80 s).
15	
16	Where each parameter comes from is said where it is defined:
17	  [claims]   the claim's criterion or the claims file's shared method, which cite the paper;
18	  [paper]    a passage of the paper, cited (author step 1.6);
19	  [assumed]  an assumption, with the reason;
20	  [standard] a standard choice for a detail that cannot change a result.
[... 543 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_fujisawa_2008.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--');print(''.join(o['data']['text/plain']))
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1979 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 code
2	# # Reproducing Fujisawa, Amarasingham, Harrison & Buzsaki (2008) from DANDI:000067 and CRCNS pfc-2
3	#
4	# **Paper.** Fujisawa S, Amarasingham A, Harrison MT, Buzsaki G. Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex. *Nat Neurosci* 11:823-833 (2008), doi:10.1038/nn.2134. The claims file (`claims/fujisawa-2008.yaml`) was written from the version of record with its supplement.
5	#
6	# **Datasets.**
7	# - DANDI:000067, version 0.261106.2004 (doi:10.48324/dandi.000067/0.261106.2004). The paper cites no version of either dataset, so the most recent published version is pinned; its release notes say it changes only metadata from 0.261106.0244, and the two earlier versions (0.210812.1457, 0.250624.0419) hold 28 assets against 31, so the latest is the fullest. Read: the units table (spike times, shank, cluster), the trials tables, the head LED positions and the wideband signal of the 13 working memory sessions.
8	# - CRCNS pfc-2 (doi:10.6080/K01V5BWK), unversioned (description version 0.7, July 2021); MD5 sums of the files read are printed in the data check. Read, streamed from the public bucket: `behaviors.zip` (the lab's summary of 12 working memory sessions), `EE0708/EE188_Behavior.mat` and `EE188_Behavior_PFC.mat` (session EE.188, not in the zip), `EE0711/EE210_Behavior_PFC.mat` (compared with the zip's copy), and `EE188_example.mat` from inside `EE0708/EE.188.tar.gz` (the paper's Figure 2a / 3 session: 117 cells and the lab's connection list).
9	#
10	# Spike times come from the NWB files, matched to the lab's cell numbers by shank and cluster (identical to the lab's spike times, data check); trials, positions and cell lists come from CRCNS, as the NWB files lack them for some sessions and give no lab cell numbers for most.
11	#
12	# **Claims.** All 33 claims of the claims file are tested except `task-performance`, blocked (data_missing): the datasets list correct trials only.
13	#
14	# | Claim | Tested 
[... 526 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 541,
 "limit": 500
}
```

```
541	
542	> Of 62,408 directed pairs of simultaneously recorded neurons, 495 (0.79%) show a short-latency narrow peak or trough in the cross-correlogram by the jitter test, 0.55% excitatory and 0.24% inhibitory, and 0.17% of pairs are reciprocally connected.
543	
544	Reciprocal: a pair connected in both directions (any type), over (a) directed pairs and (b) unordered pairs.
545	==================== 21 code
546	RATES = {}
547	for c in COMBOS:
548	    v = CONN[c]
549	    dirs = {(s, a, b) for s, a, b, k in v}
550	    nE = sum(k == "E" for *_, k in v)
551	    nI = sum(k == "I" for *_, k in v)
552	    recip = {(s, min(a, b), max(a, b)) for s, a, b in dirs if (s, b, a) in dirs}
553	    tot = pct(len(dirs), NPAIRS)
554	    RATES[c] = (tot, pct(nE, NPAIRS), pct(nI, NPAIRS), pct(len(recip), NPAIRS), pct(len(recip), NPAIRS / 2))
555	    r = RATES[c]
556	    print(f"{c}: directed pairs {NPAIRS} (paper 62,408); connected {len(dirs)} = {r[0]:.3f}% (0.79 +/- 0.079: {abs(r[0]-0.79)<=0.079}); "
557	          f"excitatory {nE} = {r[1]:.3f}% (0.55 +/- 0.055: {abs(r[1]-0.55)<=0.055}); inhibitory {nI} = {r[2]:.3f}% (0.24 +/- 0.024: {abs(r[2]-0.24)<=0.024}); "
558	          f"reciprocal pairs {len(recip)} = {r[3]:.3f}% of directed (a), {r[4]:.3f}% of unordered (b) (0.17 +/- 0.017: {abs(r[3]-0.17)<=0.017} / {abs(r[4]-0.17)<=0.017})")
559	print("per session (B-a, W-a), % of directed pairs connected:",
560	      {s: round(pct(sum(1 for r in CONN[MAIN] if r[0] == s), len(x.cells) * (len(x.cells) - 1)), 2) for s, x in S.items()})
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1041,
 "limit": 480
}
```

```
1041	    if which == "a":
1042	        return [rate(allm)]
1043	    l, r = rate(lab), rate(~lab)
1044	    if which == "b":
1045	        return [l, r]
1046	    return [l if l.max() >= r.max() else r]
1047	def width(v, how):
1048	    if v.max() <= 0:
1049	        return np.nan
1050	    above = v >= 0.5 * v.max()
1051	    if how == "ii":
1052	        return above.sum() * dx
1053	    p = int(np.argmax(v)); a = b = p
1054	    while a > 0 and above[a - 1]:
1055	        a -= 1
1056	    while b < len(v) - 1 and above[b + 1]:
1057	        b += 1
1058	    return (b - a + 1) * dx
1059	FS_RES = []
1060	for pr in ("P-a", "P-b"):
[... 460 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1521,
 "limit": 460
}
```

```
1521	--OUT--
1522	(a) EE188: previous-trial labels 4.3% (5/117), current 60.7% (71/117); less than half: True
1523	(a) FF130 stand-in: previous-trial labels 12.5% (8/64), current 79.7% (51/64); less than half: True
1524	(b) R-a (FF layer 5): L2/3: previous 6.9% (33/481), current 62.8%, less than half True; L5: previous 8.9% (13/146), current 66.4%, less than half True
1525	(b) R-b1 (EE layer 5): L2/3: previous 8.3% (15/181), current 63.5%, less than half True; L5: previous 7.0% (31/446), current 63.7%, less than half True
1526	(b) R-b2 (GG layer 5): L2/3: previous 7.4% (44/592), current 64.4%, less than half True; L5: previous 5.7% (2/35), current 51.4%, less than half True
1527	null relabelling, all neurons: 4.8%
1528	
1529	==================== 58 markdown
1530	## Claim speed-not-correlated
1531	
1532	> Firing rates show no net positive relationship with running speed; the distribution of rate-speed correlations is symmetric around zero.
1533	
1534	Supplementary Figure 3C: trials divided into 0.5 s bins; per bin the neuron's rate and the running speed (path length of the head position, the LED midpoint where two LEDs exist, in pixels per second); Pearson correlation per neuron over its session's bins. Two-sided Wilcoxon signed-rank test of the correlations against 0, over all neurons and within putative pyramidal cells and interneurons (B-a, W-a). Reproduced when the median over all neurons is not significantly above 0 at p < 0.05.
1535	==================== 59 code
1536	SPD = {}
1537	for s, x in S.items():
1538	    l1 = x.leds[0]
1539	    mid = (l1 + x.leds[1]) / 2 if len(x.leds) > 1 else l1
1540	    edges = np.concatenate([np.arange(a, b - 0.5 + 1e-9, 0.5) for a, b in zip(x.start, x.stop)])
[... 440 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; grep -n -i -E "cells|CellsInfo|1 ?Hz|spikeph|SessionNP|correct|whl|pairs_all|example|GG|interneuron|cell type" pfc-2.data-description.txt | head -80
```

```
2368 10.1038-nn.2134.txt
   433 pfc-2.data-description.txt
  2801 total
18:intermediate area CA1 of the hippocampus (32 channels) in three rats (EE, FF, GG). In one rat 
46:Rat FF and GG contains 101 channels. 
63:(1) SessionNP : Time information of each trial. Only correct trials are listed. 
72:(2) whlrl : Extended whl file.  
73:     Each row: video frame of 39.0625Hz (=20kHz/512), as normal whl file. 
74:     1st~4th column: [x1, y1, x2, y2], as normal whl file. 
86:(6) spikeph: 
92:(7) Cells: the neuron # whose max firing rates are more than 1 Hz in the trials. 
97:or GG) followed by four digits corresponding to the day the recordings were made. For animals 
98:FF and GG, there is only one recording session per day (made during the working memory 
99:task), except on one day (folder GG0330) in which both the spontaneous alternation task and 
104:task. Due to some instability in the recording, some neurons might not have been correctly 
344:GG0330 
345:GG.063 
349:GG.069 
352:GG0401 
353:GG.097 
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 55,130p pfc-2.data-description.txt; sed -n 370,433p pfc-2.data-description.txt
```

```
Page 2 of 6 
Behavior and data processing 
In each folder containing the recording session during the working memory task, a matlab file 
called ‘XXX_Behavior.mat’ (where XXX is the session name) contains basic parameters for 
behavior. File 'behaviors.zip' includes Matlab files that summarize the behavioral and neuronal 
data in all sessions. 
 
(1) SessionNP : Time information of each trial. Only correct trials are listed. 
     Each row: Each trial. 
     1st column: Time when rat started the first nose-poking in each trial. (the unit is seconds.) 
     2st column: Time when rat ended the last nose-poking in each trial. This time is defined as 
the "trial start time" in my paper.  
     3rd column: Time when rat stared the reward consumption (i.e., chewing nose). This time is 
defined as the "trial end time" in my paper.  
     4th column: Left or Right trials. R = 1 and L = 2. 
 
(2) whlrl : Extended whl file.  
     Each row: video frame of 39.0625Hz (=20kHz/512), as normal whl file. 
     1st~4th column: [x1, y1, x2, y2], as normal whl file. 
     5th column: Left or Right trials. R = 1 and L = 2. 
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000067/versions/0.261106.2004/assets/?page_size=200" -o assets.json; python3 -c "
import json;d=json.load(open('assets.json'));print(d['count'])
for a in d['results']: print(a['path'],a['size'])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "jitter|global band|pointwise|99%|stepping" 10.1038-nn.2134.txt | head -60
```

```
235:P < 0.05 (pointwise)
265:the rat spends at each position. Red, right turns; blue, left turns, in this and subsequent figures. Two types of statistical assessment are shown: pointwise
267:once a segment was established as significant, we used pointwise criteria to determine the segment’s (spatial) extent; see Methods; Supplementary Fig. 4).
634:the reference cell as an inhibitory interneuron. Blue line, mean of time-jittered spikes; red line, point wise comparison (P o 0.01); magenta line, global
665:To disambiguate multiple-timescale effects, we used jitter techniques26 to infer monosynaptic connections. Each spike in each neuron
667:‘jittered’) on a uniform interval of [–5,+5] ms to form a surrogate data
671:the jittered data sets (see Methods for quantitative details; Supplementary Fig. 9 online). Because the jittered data sets preserve firing rates on
672:timescales much broader than that of the jitter interval, the overall
757:P < 0.01 (pointwise)
758:Jittered mean
811:coincident (within 4 ms) spikes of the two neurons (crosses). Bottom panel, comparison of real and jittered surrogate (the ‘expected coincidence’) data. Maze
981:P < 0.01 (pointwise)
982:Jitter mean
985:P < 0.01 (pointwise)
986:Jitter mean
1026:of cell pairs from a. Real and jittered surrogates as in Figure 4. (See Methods; Supplementary Fig. 12.) Note that monosynaptic efficacy can vary despite little
1046:or greater, as quantified by the jitter technique (Fig. 4b; Supplementary Fig. 12 online). Across all sessions, out of 343 pairs with significant
1059:jittering technique to assess position dependence of monosynaptic
1444:pointwise bands. Firing rate differences were assayed by the relative frequency
1489:P-values for a fixed value of x (pointwise P-values) can be computed directly
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1425,1630p 10.1038-nn.2134.txt
```

```
probes in the prefrontal cortex, layer 2/3 (n 1⁄4 3) or layer 5 (n 1⁄4 1) (anteroposterior 1⁄4 3.0–4.4 mm, medio-lateral 1⁄4 0.5 mm). The recording silicon probe
was attached to a micromanipulator and moved gradually to its desired depth
position. The probe consisted of eight shanks (200-mm shank separation) and
each shank had eight recording sites (160 mm2 each site; 1–3 MO impedance),
staggered to provide a two-dimensional arrangement (20-mm vertical separation; Fig. 1a). All protocols were approved by the Institutional Animal Care and
Use Committee of Rutgers University. During the recording sessions, neurophysiological signals were acquired continuously at 20 kHz on a 128-channel
DataMax system (16-bit resolution; RC Electronics). For offline sorting, the
wideband signals were digitally high-pass filtered (0.8–5 kHz). For tracking the
position of the animals on the task track, two small light-emitting diodes (5-cm
separation), mounted above the headstage, were recorded by a digital video
camera and sampled (at 40 Hz). Spike sorting was performed semiautomatically, using KlustaKwik (available at http://osiris.rutgers.edu/frontmid/indexmid.html) followed by manual adjustment of the clusters.
Resampling methods. Resampling methods are the primarily statistical tool
used to identify (i) conditional differences in firing rates, (ii) monosynaptic
interactions and (iii) regions of excess monosynaptic interactions in the maze.
Resampling methods involve the randomized construction of surrogate data
sets that reproduce certain aspects of the original data, as specified by a null
hypothesis. Then, the original data set is compared to the surrogate data sets to
identify structures that do or do not exist in violation of the null hypothesis.
Identifying conditional differences in firing rates. Permutation tests and
pointwise bands. Firing rate differences were assayed by the relative frequency
[... 186 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 2110,2150p 10.1038-nn.2134.txt; grep -n -i -E "trajectory.selective|side arms|22%|40%|Fig. 2b|figure 2b" 10.1038-nn.2134.txt | head;
```

```
Fujisawa et al. 
 
13
 
 
 
Supplementary Fig 9. Identifying monosynaptic interactions. Spike jittering method. 
(see also, Experimental Procedures in the main text; Amarasingham et al., 2007) 
 
(A) To assess the statistical significance of bin fluctuations in the spike cross-correlograms, spikes of one 
of the neurons were time jittered by -5 to 5 msec to generate a jittered cross-correlogram (jittered). By 
repeating the procedure 1000 times, the 99% confidence intervals for each bin (p=0.01) is calculated. In 
addition, the global (band) significance is indicated and both sets of statistics are superimposed on the 
original cross-correlogram (lower right).  (B) Definition of the standardized peak height. Left, Different 
levels of pointwise significance values computed by the jittering method are shown, superimposed on the 
original cross-correlogram. Right, Relationship between the height of the significant peak (“synaptic 
strength”, normalized to the mean firing rate) and p values. The standardized peak height 
 is defined 
as: 
hˆ
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "import numba, h5py, remfile, fsspec, scipy; print('ok')" 2>&1 | tail -1
```

```
ModuleNotFoundError: No module named 'numba'
```

**Agent calls Bash**

```bash
cd  python3 -c "import numpy, scipy; print(numpy.__version__, scipy.__version__)"; for m in h5py remfile fsspec requests; do python3 -c "import $m" 2>&1 | tail -1; done; pip install numba 2>&1 | tail -1
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy; print(numpy.__version__, scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'h5py'
ModuleNotFoundError: No module named 'remfile'
ModuleNotFoundError: No module named 'fsspec'
ModuleNotFoundError: No module named 'requests'
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -m venv v 2>&1|tail -1; ./v/bin/pip install -q numpy scipy numba 2>&1 | tail -2; ./v/bin/python -c "import numba, scipy; print('ok')"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; mkdir -p stubs; for m in h5py remfile requests fsspec; do echo "" > stubs/$m.py; done; cp fujisawa.py .; cat > t1.py <<'EOF'
import sys; sys.path.insert(0,'stubs')
import numpy as np, fujisawa as fj
rng=np.random.default_rng(1)
# 1. bands_from_curves FWER under null: permutation test with null data
fp2=0; fp1=0; N=300
for i in range(N):
    P=rng.poisson(2,(40,101)).astype(float)
    from scipy.ndimage import gaussian_filter1d
    P=gaussian_filter1d(P,5,axis=1)
    lab=np.arange(40)<20
    r=fj.perm_bands(P,lab,M=500,alpha=0.05,rng=rng)
    fp2+=r['significant']
print('two-sided FWER (alpha .05):',fp2/N)
# one-sided global, iid null curves
c=0
for i in range(N):
    D=gaussian_filter1d(rng.normal(size=(1001,101)),5,axis=1)
    c+=fj.bands_from_curves(D,0.01,two_sided=False)['significant']
print('one-sided FWER (alpha .01, M=1000):',c/N)
c=0
for i in range(100):
    D=gaussian_filter1d(rng.normal(size=(5001,101)),5,axis=1)
    c+=fj.bands_from_curves(D,0.01,two_sided=False)['significant']
print('one-sided FWER (alpha .01, M=5000):',c/100)
EOF
./v/bin/python t1.py
```

```
two-sided FWER (alpha .05): 0.0
one-sided FWER (alpha .01, M=1000): 0.0
one-sided FWER (alpha .01, M=5000): 0.01
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > t2.py <<'EOF'
import sys; sys.path.insert(0,'stubs')
import numpy as np, fujisawa as fj
from scipy.ndimage import gaussian_filter1d
rng=np.random.default_rng(2)
for M in (500,1000,5000):
  for a,two in ((0.05,True),(0.01,False),(0.05,False)):
    c=0;ks=[];N=200
    for i in range(N):
        D=gaussian_filter1d(rng.normal(size=(M+1,101)),5,axis=1)
        r=fj.bands_from_curves(D,a,two_sided=two); c+=r['significant']; ks.append(r['kstar'])
    print(M,a,two,'FWER',c/N,'median kstar',np.median(ks))
EOF
./v/bin/python t2.py
```

```
500 0.05 True FWER 0.0 median kstar 0.0
500 0.01 False FWER 0.0 median kstar 0.0
500 0.05 False FWER 0.04 median kstar 1.0
1000 0.05 True FWER 0.04 median kstar 1.0
1000 0.01 False FWER 0.0 median kstar 0.0
1000 0.05 False FWER 0.03 median kstar 2.0
5000 0.05 True FWER 0.05 median kstar 6.0
5000 0.01 False FWER 0.0 median kstar 2.0
5000 0.05 False FWER 0.035 median kstar 13.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > t3.py <<'EOF'
import sys; sys.path.insert(0,'stubs')
import numpy as np, fujisawa as fj
rng=np.random.default_rng(3)
T=1800.
def pois(rate):
    n=rng.poisson(rate*T); return np.sort(rng.uniform(0,T,n))
cnt={('E',0):0,('I',0):0}; N=150
res=[]
for i in range(N):
    a=pois(3); b=pois(3)
    e,C=fj.jitter_pair(a,b,M=1000,binw=0.0005,seed=i)
    C1=C.reshape(C.shape[0],-1,2).sum(2)
    r=fj.classify_ccg(e[::2],C1)
    res.append([r['ab'][0],r['ab'][1],r['ba'][0],r['ba'][1]])
res=np.array(res); print('null independent Poisson: rate per direction exc %.4f inh %.4f'%(res[:,[0,2]].mean(),res[:,[1,3]].mean()))
# common slow-modulated (20-ms timescale) drive: no monosynaptic but shared fast-ish rate
res=[]
for i in range(N):
    base=pois(3)
    # common 'bursts': events with both cells firing within +-8 ms gaussian of event, symmetric
    ev=np.sort(rng.uniform(0,T,2000))
    a=np.sort(np.r_[pois(2),ev+rng.normal(0,0.008,len(ev))]); b=np.sort(np.r_[pois(2),ev+rng.normal(0,0.008,len(ev))])
    e,C=fj.jitter_pair(a,b,M=1000,binw=0.0005,seed=i)
    C1=C.reshape(C.shape[0],-1,2).sum(2)
    r=fj.classify_ccg(e[::2],C1)
    res.append([r['ab'][0],r['ab'][1],r['ba'][0],r['ba'][1]])
res=np.array(res); print('8ms-sd common input, no synapse: exc %.3f inh %.3f'%(res[:,[0,2]].mean(),res[:,[1,3]].mean()))
# injected connection a->b at 2 ms
a=pois(3); b=np.sort(np.r_[pois(3), a[rng.random(len(a))<0.05]+0.002])
e,C=fj.jitter_pair(a,b,M=1000,binw=0.0005,seed=1); C1=C.reshape(C.shape[0],-1,2).sum(2)
print('injected a->b:',fj.classify_ccg(e[::2],C1), 'real ccg 1ms',C1[0])
EOF
./v/bin/python t3.py
```

```
null independent Poisson: rate per direction exc 0.0000 inh 0.0000
8ms-sd common input, no synapse: exc 0.010 inh 0.000
injected a->b: {'ab': (True, True), 'ba': (False, True)} real ccg 1ms [ 12  11  16  16  19  13 222  78  12  13]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > t4.py <<'EOF'
import sys; sys.path.insert(0,'stubs')
import numpy as np, fujisawa as fj
rng=np.random.default_rng(4)
T=1800.
def pois(rate):
    n=rng.poisson(rate*T); return np.sort(rng.uniform(0,T,n))
for p in (0.005,0.01,0.02,0.05):
    out=[]
    for i in range(40):
        a=pois(3); b=np.sort(np.r_[pois(3), a[rng.random(len(a))<p]+0.002+rng.uniform(-0.0005,0.0005,len(a))[rng.random(len(a))<p][:0].sum()])
        e,C=fj.jitter_pair(a,b,M=1000,binw=0.0005,seed=i); C1=C.reshape(C.shape[0],-1,2).sum(2)
        r=fj.classify_ccg(e[::2],C1)
        out.append([r['ab'][0],r['ab'][1],r['ba'][1]])
    out=np.array(out).mean(0)
    print(f'transmission {p}: detect E a->b {out[0]:.2f}; spurious I a->b {out[1]:.2f}; spurious I b->a {out[2]:.2f}')
EOF
./v/bin/python t4.py
```

```
transmission 0.005: detect E a->b 0.72; spurious I a->b 0.00; spurious I b->a 0.00
transmission 0.01: detect E a->b 1.00; spurious I a->b 0.03; spurious I b->a 0.00
transmission 0.02: detect E a->b 1.00; spurious I a->b 0.03; spurious I b->a 0.20
transmission 0.05: detect E a->b 1.00; spurious I a->b 0.33; spurious I b->a 0.62
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json,urllib.request
d=json.load(open('assets.json'))
for a in d['results']:
    if 'FF-130' in a['path'] or 'EE-188' in a['path']:
        m=json.load(urllib.request.urlopen(f"https://api.dandiarchive.org/api/dandisets/000067/versions/0.261106.2004/assets/{a['asset_id']}/"))
        print(a['path']); print(json.dumps({k:m[k] for k in m if k not in ('digest','contentUrl')},indent=0)[:2500])
EOF
```

```
sub-EE/sub-EE_ses-EE-188_behavior+ecephys.nwb
{
"id": "dandiasset:dfcb05d9-049b-4479-9f53-e164a8ea9807",
"path": "sub-EE/sub-EE_ses-EE-188_behavior+ecephys.nwb",
"access": [
{
"schemaKey": "AccessRequirements",
"status": "dandi:OpenAccess"
}
],
"@context": "https://raw.githubusercontent.com/dandi/schema/master/releases/0.7.0/context.json",
"approach": [
{
"name": "electrophysiological approach",
"schemaKey": "ApproachType"
},
{
"name": "behavioral approach",
"schemaKey": "ApproachType"
}
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 15,54p pfc-2.data-description.txt
```

```
This dataset of multi single neuron recording was acquired in rats while performing a working 
memory task. Neuronal activity was monitored simultaneously in the PFC (64 channels) and the 
intermediate area CA1 of the hippocampus (32 channels) in three rats (EE, FF, GG). In one rat 
(EE), sleep was also recorded before and after the task.  Total duration of the recorded data 
from all three animals is approximately 23.37 hours.  Details of the task were described in the 
following paper:  
 
Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex. Fujisawa S, 
Amarasingham A, Harrison MT, Buzsáki G. Nature Neuroscience 2008 Jul;11(7):823-33.  
doi: 10.1038/nn.2134.  
 
Data structure 
Data structures and file name conventions are similar to those in the hc-2, hc-3 and hc-4 data 
sets at CRCNS.org.  See the documentation in those data sets for a description of the files.  
Sampling rate for raw data ‘.dat’ files is 20k hz.  Sampling rate of low-pass filtered files (.eeg) is 
1,250 hz (20k / 16). 
 
Channel structure of the ‘.dat’ (raw wideband binary) and ‘.eeg’ (low-pass filtered binary) files: 
Rat EE contains 104 channels. 
1-64 ch: PFC (Buzsaki64 probe) 
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "Fig(ure)?\.? ?16|first spike|depress|facilitat" 10.1038-nn.2134.txt | head -30
```

```
19:we found evidence for both firing pattern–dependent facilitation and depression, as well as for a supralinear effect of
27:of a number of biophysical phenomena, such as synaptic facilitation
28:and depression9–11. There has also been, correspondingly, a great deal
57:with synaptic facilitation and depression, as well as evidence for a
1089:activity. We hypothesized that the ‘depressing’ and ‘facilitating’ nature
1094:200 ms. We compared the impact of the first spike of the train on
1132:First spikes
1153:Depressing
1159:Facilitation
1160:Depression
1173:Facilitating
1177:(a) Illustration of depressing and facilitating
1182:trains. ‘First spikes’, spikes with long interspike
1189:depressing (12.7%) and facilitating (10.7%)
1193:permutation test (shuffling the first spike,
1195:one side corresponds ‘facilitation’, the other to
1196:‘depression’). See also Supplementary
1204:pyramidal cell 197 showing a depressing effect with spike repetition. In
1205:contrast, the first spike of spike trains of cell 186 was ineffective, but
1212:depressing (12.7%) and facilitating (10.7%) effects (Fig. 6c). These
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1085,1110p 10.1038-nn.2134.txt; sed -n 1175,1200p 10.1038-nn.2134.txt; sed -n 2266,2300p 10.1038-nn.2134.txt
```

```
neurons varies according to task needs. Next, we examined physiological mechanisms that might potentially explain such transient effects.
The ability of a presynaptic pyramidal cell to discharge a postsynaptic neuron depends on a variety of conditions. The specific pattern of
firing of the presynaptic cell is a particularly important factor because
the likelihood of transmitter release depends on previous spiking
activity. We hypothesized that the ‘depressing’ and ‘facilitating’ nature
of interactions, observed previously between neuron pairs in vitro5
(Fig. 6a), could be detected by estimating spike transmission probabilities, conditioning separately on the first and later spikes of a train
of the presynaptic neuron. Here we operationally defined a spike train
as a series of spikes occurring after a nonspiking period of at least
200 ms. We compared the impact of the first spike of the train on
postsynaptic discharge to the effects of second and subsequent
spikes that occurred within 40 ms of each other. Figure 6b shows a
putative layer 2/3 interneuron innervated by two pyramidal cells, with
–50
0
50
0
100
–50
0
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 2005,2032p 10.1038-nn.2134.txt; grep -n -i "chance" 10.1038-nn.2134.txt | head
```

```
Nevertheless, the procedure is analogous to the peri-stimulus time histogram (PSTH). For the shuffling 
procedure the fundamental idea is same in PSTH (time) and in post-start distance histogram. (If the 
histograms of the spike events are divided by the occupancy time, the units “1/cm” can be converted to 
“1/s”.) Because PSTH is used more generally, we use this notation. 
 
(B) PSTHs and their difference of shuffled data. 
We then randomly permute the Left/Right assignments to L1,L2,...,LN , and re-estimate the PSTH’s and 
compute the statistic D1(x) under the permuted labels. Repeat this process R times to obtain the statistic 
from the original data, D0(x), along with the statistic from resample data, D1(x),...,DR(x). 
 
(C) How to compute pointwise bands. 
Using resampled (shuffled) data set, we computed pointwise p-value at each point (equation (E3-5)).  
 
(D) How to compute global bands? 
Here the adjusted p-values are computed as following. First, create a family of pointwise acceptance 
band, one for each possible level of significance. Then, for each pointwise acceptance band see what 
fraction of the samples lie completely within the band. This fraction is that band’s simultaneous 
acceptance level. The adjusted p-value at an index x can be inferred from the smallest level simultaneous 
acceptance band that dose not contain the original measurement at index x. In the example of this figure, 
the global 5% bands correspond to pointwise 0.6% bands. Using the global assessment method, we can 
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1330,1345p 10.1038-nn.2134.txt; grep -n -i "satellite" 10.1038-nn.2134.txt | head
```

```
10
20
0
(%)
Figure 7 Coincident firing of more than one neuron facilitates spike transmission. (a) Left, representative ‘satellite’ network with eight putative pyramidal cells
converging on an interneuron. Center, spike transmission probability as a function of the number of coincident spikes among two or more neurons within
increasing time windows. Right, frequency of coincident events. Note supralinear facilitation at o5-ms intervals. Cells 32 and 72 were recorded from different
shanks than the interneuron (135). (b) Group data for all satellites using 5-ms time windows (mean ± s.d., n 1⁄4 14; inset, individual satellites).
830
VOLUME 11 [ NUMBER 7 [ JULY 2008 NATURE NEUROSCIENCE
A R T I C L E S
© 2008 Nature Publishing Group  http://www.nature.com/natureneuroscience

=== page 9 ===
physiological mechanisms underlying associative mechanisms, learning, memory or reward expectancy. In contrast, taking into account
physiological criteria to separate excitatory and inhibitory neurons,
1334:Figure 7 Coincident firing of more than one neuron facilitates spike transmission. (a) Left, representative ‘satellite’ network with eight putative pyramidal cells
1337:shanks than the interneuron (135). (b) Group data for all satellites using 5-ms time windows (mean ± s.d., n 1⁄4 14; inset, individual satellites).
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > t5.py <<'EOF'
import sys; sys.path.insert(0,'stubs')
import numpy as np, fujisawa as fj
rng=np.random.default_rng(5)
T=1800.
res=[]
for i in range(40):
    # presynaptic: bursts after silences, so first spikes numerous, later fewer
    starts=np.cumsum(rng.exponential(0.6,int(T/0.6)))
    a=[]
    for s in starts:
        a.append(s)
        if rng.random()<0.15: a.append(s+0.01)
    a=np.sort(np.array(a)); a=a[a<T]
    b=np.sort(np.r_[rng.uniform(0,T,int(5*T)), a[rng.random(len(a))<0.05]+0.002])  # same efficacy for all spikes
    first,later=fj.spike_labels(a,'x')
    r=fj.standardized_height_test(a,b,first,later,M_jit=100,R=300,seed=i)
    res.append((r['sum']['diff'],r['sum']['p'],r['n_first'],r['n_later']))
res=np.array(res)
print('n_first/n_later median',np.median(res[:,2]),np.median(res[:,3]))
print('mean diff (no true effect):',res[:,0].mean(),'; fraction diff>0:',(res[:,0]>0).mean(),'; p<0.10:',(res[:,1]<0.10).mean())
EOF
./v/bin/python t5.py
```

```
n_first/n_later median 2134.5 499.5
mean diff (no true effect): 5.7660059267340795 ; fraction diff>0: 1.0 ; p<0.10: 0.1
Shell cwd was reset to
```

**Agent**

**Verification report: Fujisawa et al. 2008, round 1**

Claim and outcome counts come from the claims file (33 claims) and from my own judgement of the notebook outputs. My outcomes: 5 reproduced, 11 partially reproduced, 16 not reproduced, 1 blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| channel-region-link | not_reproduced | Check (i) holds in the 12 sessions with raw signal; EE088 has none. Check (ii) fails in GG069, GG097 and GG149 (0.30, 0.42, 0.42), and even the best channels found by search reach only 0.68–0.78, below 90% (cell 6). |
| rats-and-units | partially_reproduced | The total is 627, within 633 ± 63.3. No rat has 222 ± 22.2 units (FF 146, EE 446, GG 35; cell 8). This rests on an unverified unit list (B1). |
| task-performance | blocked (data_missing) | SessionNP is documented as "Only correct trials are listed", and the NWB trials tables are identical (cells 3, 10). The criterion says to block in this case. |
| fig2-population-uniform | not_reproduced | In EE188, peaks per tenth are [24,0,1,2,14,5,3,8,1,59] against 11.7 expected. The population rate test passes (cell 39). Peaks were computed with the P-b rate only (B2). |
| fig2c-active-fraction | not_reproduced | No reading has both values in tolerance. Reading (a): EE188 11.8% (needs 10 ± 1). Reading (b), R-a: layer 2/3 12.6%, layer 5 20.3% (cell 41). |
| fig2-field-size | reproduced | 5 of 24 combinations have both mean and s.d. in tolerance, e.g. P-a (b)(i)(x) 0.241 ± 0.169 and P-b (a)(ii)(y) 0.286 ± 0.185 (cell 43). |
| population-vector-width | partially_reproduced | The claim's own method (raw PSTHs) gives about 1.0. Values fall in tolerance only after the author's z-scoring, which neither the paper nor the claims specify: EE188 0.19–0.22. With peak normalisation (as Figure 2a displays rates), layer 2/3 just misses: 0.268 against a limit of 0.267. The layer 5 value comes only from a stand-in session or the rat readings (cell 45). |
| fig2d-layer-rates | partially_reproduced | Under R-a, trial periods: pyramidal cells L5 > L2/3 at p = 0.0028. All neurons only reach p = 0.026 (Welch). No combination gets both below 0.01 (cell 47). |
| fig2e-layer-discrimination | not_reproduced | At most one group (pyramidal, R-a, p = 0.023) is higher at p < 0.05. The partial criterion needs two (cell 49). |
| traj-diverge | partially_reproduced | EE188 path diverges at 0.30 (in tolerance). Head direction diverges at 0.02 against 0.24 (cell 51); see B8. |
| side-arm-selectivity-by-layer | partially_reproduced | Values are far from tolerance (about 50–60% against 40% and 22%). Under R-a, L5 > L2/3 by one-sided Fisher test, p = 0.046 (reading a) and p = 0.017 (reading b) (cell 14). |
| central-arm-selectivity | partially_reproduced | Values are 23–31% against 16% and 18%. The pooled 30.1% is far above one random relabelling (1.4%, p = 6e-52) (cell 16). |
| odor-nosepoke | not_reproduced | 39–45% in EE188 and 31–33% over all neurons, against 26 ± 2.6 (cell 53). |
| odor-unrelated-to-stem | not_reproduced | Fisher tests are not significant, but the correlation with the stem is r = −0.38 (p = 2e-5) and with the side arms p = 0.03 in EE188 (cell 55). |
| retrospective-coding-rare | reproduced | Previous-trial labels give 4–13% of neurons against 51–80% for current labels, in every reading (cell 57). |
| speed-not-correlated | reproduced | Median r = −0.022, so not above 0 (cell 59). |
| fig3-connection-rates | not_reproduced | None of the three directed percentages is in tolerance in any of the 4 combinations (e.g. 1.45 / 1.17 / 0.28%) (cell 21). |
| fig3-cell-classes | not_reproduced | Interneurons are 2.6–4.4% against 12.5%, and the pyramidal-to-interneuron ratio is 9.9–14.8 against 2.82 (cell 23). |
| pyr-pyr-connections | partially_reproduced | No value is in tolerance. L5 > L2/3 under R-a, reading (a): 0.355% against 0.261% (cell 25). |
| nearby-pyr-int-probability | not_reproduced | 45–59% against 0.9–2.2% (cell 27). |
| fig3b-session-connections | not_reproduced | EE188 gives 119/22 directed connections and 67/16 distinct reference cells, against 48/30. The layer 5 session was not identified, which rests on B1 (cell 29). |
| fig3d-hub | not_reproduced | EE188's largest component is 65–86 cells, against 39. The lab's own `pairs_all` list gives exactly 39 (cell 31), so detection here is much more liberal than the lab's. |
| fig3f-distance | partially_reproduced | Same shank 384 against 200 on other shanks, and the confidence intervals separate. But the largest separation with a connection is 1400 µm, not 1200 µm (cell 33). |
| fig3-trajectory-by-class | partially_reproduced | Under R-a, reading (b), 2 of 4 values are in tolerance: layer 2/3 pyramidal 66.8% and layer 2/3 interneurons 52.6% (cell 35). |
| no-spatial-clustering | reproduced (layer 2/3 session only) | EE188: shank × class p = 0.27, shank × peak tenth p = 0.23. The layer 5 session was not tested (cell 37). |
| fig4-position-dependence | partially_reproduced | 6.4–7.2% against 19.5%, but well above the 1–2% null rate (binomial p ≤ 5e-8) (cell 63). |
| fig5a-session-selective-connections | not_reproduced | 8–9 of 119 connections found here, and 6–7 of the lab's 43 (cell 65). |
| fig4-pair-156-136 | not_reproduced | The region starts at 0.34 (needs 0.4 ± 0.04), and cell 136 varies by 61% between 0.2 and 0.5, so it is not steady (cell 67). |
| fig5b-example-pairs | not_reproduced | Only 197-201 holds. 49-52 has no region on left trials, and 186-201's region starts at 0.73, not beyond 0.75 (cell 69). |
| thinning-preserves-dependence | reproduced | Under region reading (a), 7 of 34 pairs keep their dependence in most repetitions (cell 71). |
| fig6-facilitation-depression | not_reproduced | No combination has both fractions above 5% at p < 0.05 (cell 73). The depression/facilitation split is flawed (B3). |
| fig6b-convergent-examples | partially_reproduced | By the literal criterion: 197 has first > later, but p ≥ 0.26. 186 has later > first with p = 0.064 or 0.034 (cell 75). The sign for 197 carries no information (B3). |
| fig7-supralinear | not_reproduced | S-b gives 14 satellites, but the excess over linear at 5 ms is negative in every reading (cell 77). |

### B. Problems

1. **[affects a conclusion]** `Session` and cells 2, 8, 29: the unit list is `CellsInfo` from the `Behavior_PFC` files, which the CRCNS description does not document.
   - For EE188 this list has 105 cells, while the paper's session has 117, so these lists are subsets. They may be the 1 Hz "Cells" list, which the claims file treats only as a variant.
   - The notebook never compares the list with `spikeph` or the NWB units tables.
   - The NWB variant promised in cell 7 was never computed: `nwb_by_rat` is defined and never used.
   - Affected claims: rats-and-units (FF could hold about 222 units); "no session of 142 cells", and with it fig3b, fig3d-hub and every layer 5 stand-in; fig2c (leaving out low-rate units inflates the active fraction); every fraction by layer.
2. **[affects a conclusion]** `peak_tenth` (cells 37, 39): peak positions use only the P-b PSTH. The claims header asks for both P-a and P-b wherever peaks matter. P-b peaks pile up at 0 and 1, where the rat lingers. This decides fig2-population-uniform and test (ii) of no-spatial-clustering.
3. **[affects a conclusion]** `standardized_height_test` and cell 73 label a pair depressing or facilitating by the sign of z_first − z_later.
   - Standardized height grows with √n, and first spikes far outnumber later ones (e.g. 2311 against 252).
   - On synthetic data with no true effect, the difference was positive in 40 of 40 pairs, so every significant pair would be called "depressing".
   - The Figure 6c legend assigns the label by which tail of the permutation distribution the result falls in.
   - Reassigning the 69 significant pairs of the (a,y) reading could put both fractions above 5% and turn fig6 into partially reproduced.
   - The claims file's literal "first-spike height above later" for fig6 and fig6b repeats this reading of the paper (reported, not corrected).
4. **[affects a conclusion]** `standardized_height_test`: for fig6 it jitters only the presynaptic spikes, with 200 jitters (the Supplementary Figure 9A variant). The claims file says to use the shared method: both cells, 1,000 jitters. Several binomial p-values sit near 0.05 (e.g. 0.044, 0.054), so this could matter.
5. **[affects a conclusion]** Cell 45: the outcome of population-vector-width depends on the author's normalisation (z-score or peak), which neither the paper nor the claims specify. The assumption is stated, but it decides the outcome.
6. **[affects a conclusion]** `head_curves` (cell 51): head direction is the angle from LED 1 to LED 2, averaged linearly after wrapping. LED order and orientation are never checked, and the 0.02 onset is never inspected. A wrap artefact or an LED axis perpendicular to the heading would change the head-direction result. Only 3 sessions have two LEDs.
7. **[does not affect a conclusion]** `classify_ccg`: with a strong excitatory peak, the jittered surrogates inflate the baseline, so the real baseline breaks the global minimum band. In my synthetic test with 5% transmission, spurious troughs appeared in 33% of cases in the same direction and 62% in the reverse direction. The notebook never inspects its 39 units classed as both, its 80 reciprocal pairs, or the inhibitory counts. Those claims fail by wide margins anyway.
8. **[does not affect a conclusion]** Cell 18: the one-cell jitter variant (Supplementary Figure 9A) named in the claims header was not run. It is the obvious candidate for why 141 EE188 connections are found here against the lab's 43.
9. **[does not affect a conclusion]** Cell 27: `dirs = {…: k}` overwrites an E connection with an I one in the same direction, so E connections are undercounted. The values (45%) are far from 2% anyway.
10. **[does not affect a conclusion]** Cell 6: the NWB files for FF label 8 channels from 97 on, while CRCNS gives FF 101 channels; GG's are labelled "neural". Neither is remarked on.
11. **[does not affect a conclusion]** Cell 4: the clock check is weak for EE049 (0.58 against 0.53 chance) and GG097 (0.55 true against 0.61 shifted).

Checks that passed:
- `bands_from_curves` / `perm_bands`: on synthetic null curves the familywise error was at or below α. This matches the notebook's 4.8% null rate and the paper's α = 0.05. Very conservative with M = 1,000 at α = 0.01, as the notebook notes.
- `jitter_pair`: detects injected 2 ms connections and gives no false positives on independent Poisson trains.

### C. Not checked, and what output would have allowed it

- **Unit lists:** per-session counts of NWB units and `spikeph` entries, their overlap with `CellsInfo`, and the `Behavior_PFC` variable names (is there a `Cells` list?). This would also show whether any session has 142 units.
- **task-performance (blocked):**
  - The DANDI asset list (31 NWB files) has no other behavioural files.
  - Archive contents can't be inspected through metadata alone.
  - The notebook printed only the number of unique whl trial numbers, not their range or gaps; gaps would reveal error trials.
  - Poke bouts on sensor channels 97/98 plus the LED path could count error trials in the EE and FF sessions (not GG, not EE088). The criterion as written still blocks the claim.
- **Positions:** d at each trial's start and stop, to confirm that positions run from 0 to 1 within each trial window.
- **Trial tables:** what the 18–67% of whl frames with d > 0 outside trials are.
- **P-a peaks:** peak-tenth counts under P-a.
- **Head direction:** mean head angle against position for left and right trials.
- **fig6 tails:** the null mean of the first-minus-later difference for each pair, so tails can be reassigned.
- **CCGs:** the CCGs of units classed as both and of the reciprocal pairs.
- **Global bands:** the distribution of `kstar` (pointwise-equivalent level) for the left-right tests, to compare with the paper's example of global 5% ≈ pointwise 0.6%.

## End of run

29 turns, 10 minutes, $3.04 at API prices, result: success.
