# 001968 · claims · run 39546302341

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001968/ claims/001453/ paper/ 2>&1; grep -n "^#" docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 175
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
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
18	  claim, and it asks a reader for any method detail the file lacks.
19	- The **verifier** checks the author's work and must not be the author.
20	
[... 155 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -30 paper/*.txt; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02260-w.txt",
 "offset": 7,
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)}' *.txt | sort -t: -k2 -n -r | head; grep -n "SUPPLEMENT\|Supplementary\|=====" *.txt | head -30
```

```
<persisted-output>
Output too large (93.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/5c6aebdd-3285-48c7-aea6-c3547307c04e/tool-results/b3hfn711q.txt

Preview (first 2KB):
7: 53541
16: 37913
27: 879
29: 351
88: 259
98: 246
90: 219
92: 215
66: 212
52: 212
7:pmc Nat Neurosci Nat Neurosci 981 npgopen 9809671 Nature Neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC13246448 PMC13246448.1 13246448 13246448 42026254 10.1038/s41593-026-02260-w 2260 1 Article Early dopamine disruption in the entorhinal cortex of a knock-in model of Alzheimer’s disease http://orcid.org/0000-0002-1625-4334 Nakagawa Tatsuki [removed: an e-mail address] 1 2 Xie Jiayun L. 1 http://orcid.org/0009-0001-8721-7020 Park Kiwon 1 3 http://orcid.org/0009-0004-1491-0504 Cao Kai 1 Savadkohighodjanaki Marjan 1 Zhang Yutian J. 1 http://orcid.org/0000-0002-5905-2716 Jun Heechul 1 Ichii Ayana 1 http://orcid.org/0000-0002-5670-7211 Lee Jason Y. 1 http://orcid.org/0000-0002-7381-9477 Soma Shogo 1 8 Medhat Yasmeen K. 1 http://orcid.org/0000-0003-1970-6903 Saido Takaomi C. 4 http://orcid.org/0000-0002-5635-169X Igarashi Kei M. [removed: an e-mail address] 1 2 3 5 6 7 1 https://ror.org/04gyf1771 grid.266093.8 0000 0001 0668 7243 Department of Anatomy and Neurobiology, School of Medicine, University of California, Irvine, CA USA 2 https://ror.org/01dq60k83 grid.69566.3a 0000 0001 2248 6943 Cognitive Physiology Lab, Graduate School of Medicine, Tohoku University, Sendai, Japan 3 https://ror.org/04gyf1771 grid.266093.8 0000 0001 0668 7243 Department of Biomedical Engineering, Samueli School of Engineering, University of California, Irvine, CA USA 4 https://ror.org/04j1n1c04 grid.474690.8 Lab for Proteolytic Neuroscience, RIKEN Center for Brain Science, Wako, Japan 5 https://ror.org/04gyf1771 grid.266093.8 0000 0001 0668 7243 Center for Neural Circuit Mapping, School of Medicine, University of Cal
[... 2 more lines not kept]
```

**Agent**

Paper text is in two very long lines; I'll wrap it into a readable copy in $TMPDIR.

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/*.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; sed -n 8,15p paper/*.txt | cut -c1-300; sed -n 17,40p paper/*.txt | cut -c1-200
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 1,
 "limit": 140
}
```

```
1	DOI: 10.1038/s41593-026-02260-w
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement PDF(s), extracted with PyMuPDF (dehyphenated, NFKC)
6	------------------------------------------------------------------------
7	pmc Nat Neurosci Nat Neurosci 981 npgopen 9809671 Nature Neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC13246448 PMC13246448.1 13246448 
8	13246448 42026254 10.1038/s41593-026-02260-w 2260 1 Article Early dopamine disruption in the entorhinal cortex of a knock-in model of Alzheimer’s disease http://orcid.org/0000-0002-1625-4334 Nakagawa 
9	Tatsuki [removed: an e-mail address] 1 2 Xie Jiayun L. 1 http://orcid.org/0009-0001-8721-7020 Park Kiwon 1 3 http://orcid.org/0009-0004-1491-0504 Cao Kai 1 Savadkohighodjanaki Marjan 1 Zhang 
10	Yutian J. 1 http://orcid.org/0000-0002-5905-2716 Jun Heechul 1 Ichii Ayana 1 http://orcid.org/0000-0002-5670-7211 Lee Jason Y. 1 http://orcid.org/0000-0002-7381-9477 Soma Shogo 1 8 Medhat Yasmeen K. 
11	1 http://orcid.org/0000-0003-1970-6903 Saido Takaomi C. 4 http://orcid.org/0000-0002-5635-169X Igarashi Kei M. [removed: an e-mail address] 1 2 3 5 6 7 1 https://ror.org/04gyf1771 grid.266093.8 0000 0001 
12	0668 7243 Department of Anatomy and Neurobiology, School of Medicine, University of California, Irvine, CA USA 2 https://ror.org/01dq60k83 grid.69566.3a 0000 0001 2248 6943 Cognitive Physiology Lab, 
13	Graduate School of Medicine, Tohoku University, Sendai, Japan 3 https://ror.org/04gyf1771 grid.266093.8 0000 0001 0668 7243 Department of Biomedical Engineering, Samueli School of Engineering, 
14	University of California, Irvine, CA USA 4 https://ror.org/04j1n1c04 grid.474690.8 Lab for Proteolytic Neuroscience, RIKEN Center for Brain Science, Wako, Japan 5 https://ror.org/04gyf1771 
15	grid.266093.8 0000 0001 0668 7243 Center for Neural Circuit Mapping, School of Medicine, Unive
[... 125 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 140,
 "limit": 150
}
```

```
140	anti-TH and anti-Aβ immunostaining of young APP-KI mice. Left: LEC; right: VTA and SNc. b , Aβ density is higher in the SNc than VTA ( z = −3.2, ** P = 1.4 × 10 −3 , two-sided rank sum test; n = 12 
141	mice). c , Coronal section showing anti-TH immunostaining. Left: young WT mice; right: young APP-Ki mice. d , Quantification of TH + fiber density in the LEC of WT and APP-KI mice. P values for post 
142	hoc Tukey test are shown ( n = 8 young WT mice, n = 8 young APP-KI mice, n = 6 old WT mice, n = 6 old APP-KI mice). All post hoc P values, including those not shown, were above 0.05 ( F 1,24 = 0.22, 
143	P = 0.22, strain × age interaction, ANOVA; P > 0.05, two-sided Tukey post hoc test). All data are presented as mean ± s.e.m. Since LEC dopamine fibers did not show significant morphological 
144	degeneration in APP-KI mice, we examined functional activity of LEC dopamine axons using fiber photometry 16 . Adeno-associated virus (AAV) expressing calcium activity indicator GCaMP in a 
145	Cre-dependent manner (AAV-flex-GCaMP6m) was injected in the VTA or SNc of young APP-KI mice crossed with DAT-Cre (APP-KI × DAT-Cre), and photometry fibers were implanted in the LEC (Fig. 4a ). When 
146	control DAT-Cre mice successfully learned the association (correct sessions), LEC dopamine supplied reward expectation signals during rewarded trials, as observed previously 16 (Fig. 4b , top). At 
147	T1, dopamine was released primarily during delay periods of prelearned rewarded Odor-A (mean z -scored GCaMP signal, 1.1 ± 0.24; Z = −2.7, P = 6.9 × 10 −3 , rank sum test compared to precue period). 
148	The signal also emerged for novel Odor-1 (1.8 ± 0.2; Z = −2.8, P = 5.1 × 10 −3 ) and Odor-2 cues (0.76 ± 0.24; Z = −2.27, P = 0.028). As learning progressed, dopamine signals disappeared for Odor-2, 
149	while signals remained for rewarded Odor-A and Odor-1 through T5. These dopamine signals were absent in error sessions, where WT mice did not learn associations of novel odors (Fig. 4
[... 140 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 289,
 "limit": 80
}
```

```
289	\mathrm{--}}{{\rm{mean}}\,{\rm{distance}}}_{{\rm{shuffle}}})/{{\rm{mean}}\,{\rm{distance}}}_{{\rm{shuffle}}}$$\end{document} SI = ** ( mean distance real _ data ** mean distance shuffle ) / mean 
290	distance shuffle The numerator of SI was negatively flipped so that SI becomes positive if the distance obtained from a given odor pair was smaller than shuffle distance (similar representations of 
291	two odors), and negative if the distance was larger than shuffle distance (dissimilar representations of two odors). Bootstrapping analysis The change of SI during associative learning was compared 
292	using the bootstrapping method as previously described 16 . Briefly, PCA was performed from a resampled neuronal population, and this procedure was repeated 1,000 times to make 1,000 bootstraps. SI 
293	was calculated for each bootstrap, then SIs in T2–T5 were subtracted by that in T1, to test for a significant distribution above or below 0. Distribution of difference with P < 0.05 above or below 0 
294	was considered significant. The bootstraps were also compared between WT and APP-KI mice. Decoding analysis Mean firing rates in 50-ms bins during 1–4 s after odor onset for each odor type (A, B, 1 
295	and 2) were normalized and processed for decoding analysis using binary support vector machine learners. Mean firing rates for Odor-A and Odor-B were used to train the support vector machine. To test 
296	performance of prediction, mean firing rates for Odor-1 and Odor-2 were used. This procedure was repeated 10 times to make 10 bootstraps. For each bootstrap, the decoding performance rate predicting 
297	Odor-1 or Odor-2 during the 3-s period from 2–5 s after odor onset was calculated. Histology and reconstruction of recording positions Electrode positions Recording positions were confirmed by 
298	passing electrical current through tetrodes in anesthetized mice, followed by fixation in 4% paraformaldehyde and cryosectioning 16 , 39 . Only data from tetrodes in LEC wer
[... 70 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 369,
 "limit": 200
}
```

```
369	hoc test; n = 10). Extended Data Fig. 8 Detailed principal component analyses of LEC<sub>L2/3</sub> neurons of young WT and young APP-KI mice within first 10 trials. To test the dynamics of spike 
370	representations in the early phase of the learning, PCA analysis were performed for Trial 1-3 (T1a), Trial 4-6 (T1b) and Trial 7-9 (T1c) within T1. a . (Top) Spike firing rate of n = 423 LEC L2/3 
371	cells from young WT mice, shown in z-score during T1a, T1b and T1c. (Middle) Time-resolved principal component analysis (PCA) trajectory of LEC L2/3 cell activity for each odor type (⊳ cue-onset; ✩ 
372	cue-offset/delay-onset; ☐ delay-offset). (Bottom) Euclidean distance between odor types. b . Same as (a), but for young APP-KI mice ( n = 636 cells). Trajectories for Odor-A and Odor-1 kept far apart 
373	through T1a to T1c. c . Mean Euclidean distance between PCA trajectories during 0.5 – 1.5 s after cue onset in young WT (left) and young APP-KI mice (right). Ninety-fifth percentile distance obtained 
374	from shuffled data denotes significant distance (red line). d . Similarity index (SI) between Odor-A and -1 in young WT and young APP-KI mice across learning. Positive SI denotes similar 
375	representations between Odor-A and Odor-1, whereas negative SI denotes dissimilar representations. e . Similarity Index (SI) of young WT and young APP-KI mice was compared using bootstrapping method 
376	(see Method). SI was calculated for 1000 bootstraps, then SIs for WT were subtracted by SIs for APP-KI. The subtraction confirms higher similarity in the representations between Odor-A and Odor-1 in 
377	WT mice compared to that in APP-KI mice (* p < 0.05, *** p < 0.001, p T1a = 0.023, p T1c = 8.7e-4; n = 1000 two-sided bootstrapping test). Extended Data Fig. 9 Disrupted cue-reward association of 
378	LEC<sub>L2/3</sub> neurons in old APP-KI mice. a . An example LEC L2/3 cell from an old WT mouse showing constant firing for Odor-A and Odor-1. (mean ± s.e.m.; * p < 0.05, ** p < 0
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "SUPPLEMENT\|Supplementary Table 1\b\|^\[[0-9]*\]" $TMPDIR/p.txt | awk -F: '$1>560' | head -5; grep -n "^=\+\|^---\|^#\|Supplementary Information\|Supplementary Fig\. 1 \|Supplementary Figure 1" $TMPDIR/p.txt | awk -F: '$1>560' | head -30
```

```
561:[28] Takeuchi, T. et al. Locus coeruleus and dopaminergic consolidation of everyday memory. Nature 537, 357–362 (2016). 10.1038/nature19325
563:[29] Kempadoo, K. A., Mosharov, E. V., Choi, S. J., Sulzer, D. & Kandel, E. R. Dopamine release from the locus coeruleus to the dorsal hippocampus promotes spatial learning and memory. Proc. Natl 
566:[30] Hokfelt, T., Ljungdahl, A., Fuxe, K. & Johansson, O. Dopamine nerve terminals in the rat limbic cortex: aspects of the dopamine hypothesis of schizophrenia. Science 184, 177–179 (1974). 
569:[31] Fallon, J. H., Koziell, D. A. & Moore, R. Y. Catecholamine innervation of the basal forebrain. II. Amygdala, suprarhinal cortex and entorhinal cortex. J. Comp. Neurol. 180, 509–532 (1978). 
572:[32] Akil, M. & Lewis, D. A. The distribution of tyrosine hydroxylase-immunoreactive fibers in the human entorhinal cortex. Neuroscience 60, 857–874 (1994). 10.1016/0306-4522(94)90268-2
595:##### Supplement: supplementary information (41593_2026_2260_MOESM1_ESM.pdf)
597:=== page 1 ===
608:=== page 2 ===
738:Supplementary Figure 1 | Detailed behavior analysis of WT and 
756:=2.3e-4, podor2-WTvsodor1-APP = 4.4e-22, podorA-APPvsodor1-APP = 1.8e-25, 
776:=== page 3 ===
844:=== page 4 ===
868:=== page 5 ===
917:=== page 6 ===
978:=== page 7 ===
1004:=== page 8 ===
1030:=== page 9 ===
1096:=== page 10 ===
1206:= 1.7e-2, podor1-Salvsodor2-Sal = 4.5e-11, podor1-SalvsodorA-ldopa = 2.2e-11, 
1208:= 
[... 15 more lines not kept]
```

**Agent**

The main text, Methods, Extended Data legends and the supplement are all present. Reading the supplement now.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 595,
 "limit": 450
}
```

```
595	##### Supplement: supplementary information (41593_2026_2260_MOESM1_ESM.pdf)
596	
597	=== page 1 ===
598	nature neuroscience
599	https://doi.org/10.1038/s41593-026-02260-w
600	Article
601	Early dopamine disruption in the 
602	entorhinal cortex of a knock-in model 
603	of Alzheimer’s disease
604	In the format provided by the 
605	authors and unedited
606	Supplementary information
607	
608	=== page 2 ===
609	Correct rate (%)
610	100
611	2
612	1
613	A B
614	2
[... 430 more lines not kept]
```

**Agent calls Bash**

```bash
cd  awk 'NR>=1044 && NR<=1621 && length($0)>40' $TMPDIR/p.txt
```

```
Supplementary Figure 7 | Difference of LEC dopamine signals 
between WT and APP-KI mice across odor cues
a. Difference of dopamine activity between WT and APP-KI mice (WT 
minus KI) were compared across odor cues. All data (during correct and 
error sessions) were used. Decrease of dopamine for Odor-1 was signifi-
cantly larger than those for Odor-A or Odor-B (F3,28=3.98, p=0.017, 
group, ANOVA; podorAvsodor1=0.042, podorBvsodor1=0.041 in T1, two-sided 
b. Same as Supplementary Fig.7a, but for data during correct session. 
Decrease of dopamine for Odor-1 was again significantly larger than 
those for Odor-A or Odor-B (F3,28=4.41, p=0.011, group, ANOVA; 
podorAvsodor1=0.018, podorBvsodor1=0.036 in T1, two-sided Tukey post hoc 
c. Same as Supplementary Fig.7a, but for data during error session. No 
Data are presented as mean ± s.e.m. unless otherwise indicated.
Supplementary Figure 8 | Detailed behavior analysis for optogenetic 
LEC dopamine stimulation and L-DOPA treatment
a. Detailed behavioral performance for dopamine fiber optogenetic 
stimulation in young APP-KI x DAT-Cre mice in Fig. 5b-d, but plotted 
for each odor trial type. Learning curves during control (left) and stimu-
lation (middle) sessions. (Right) Performance of mice in the last 10 trials 
(F3,80=4.48, p=5.8e-3, odor x stim interaction, ANOVA; podorA-Ctrvsodo-
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "=== page\|Supplementary Table" $TMPDIR/p.txt | awk -F: '$1>1600'; sed -n 1621,1700p $TMPDIR/p.txt
```

```
1621:=== page 14 ===
1622:Supplementary Table 1. Statistics used in this study
1948:=== page 15 ===
1949:Supplementary Table 1. Statistics used in this study (continued)
2210:=== page 16 ===
2211:Supplementary Table 1. Statistics used in this study (continued)
2428:=== page 17 ===
2429:Supplementary Table 1. Statistics used in this study (continued)
2604:=== page 18 ===
2605:Supplementary Table 1. Statistics used in this study (continued)
2932:=== page 19 ===
2933:Supplementary Table 1. Statistics used in this study (continued)
3235:=== page 20 ===
3236:Supplementary Table 2. Animals used in this study
3372:=== page 21 ===
3373:Supplementary Table 2. Animals used in this study (continued)
3515:=== page 22 ===
3516:Supplementary Table 2. Animals used in this study (continued)
3612:=== page 23 ===
3613:Supplementary Table 3. Odors used in this study
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001968/ | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:3000])"; curl -s "https://api.dandiarchive.org/api/dandisets/001968/versions/draft/info/" | python -c "import json,sys; d=json.load(sys.stdin); m=d.get('metadata',{}); print(m.get('name')); print(m.get('description')); print(m.get('relatedResource')); print(m.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL https://www.igarashilab.org/resource | python -c "
import sys,re,html
t=sys.stdin.read()
links=set(re.findall(r'href=\"([^\"]+)\"',t))
for l in sorted(links): print(l)
txt=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
txt=html.unescape(re.sub(r'<[^>]+>','\n',txt))
print(re.sub(r'\n\s*\n+','\n',txt)[:4000])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for s in 022l19o8yprphemeydxbxcfhxvn31d2h 2u05p72kc18quwz3sw818pxs6dgmmd8k z1i55i3cwdfmsyrnvgf41kevd39dzj2v; do echo "== $s"; curl -sL "https://app.box.com/s/$s" -o box_$s.html; ls -la box_$s.html; python - "$s" <<'EOF'
import sys,re,json
t=open(f"box_{sys.argv[1]}.html",encoding="utf8",errors="ignore").read()
m=re.search(r'<title>(.*?)</title>',t); print(m.group(1) if m else None)
for k in ['"name":"[^"]+"','"typedID":"[^"]+"','"itemName":"[^"]+"']:
    print(set(re.findall(k,t))  and sorted(set(re.findall(k,t)))[:40])
EOF
done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import re
t=open("box_2u05p72kc18quwz3sw818pxs6dgmmd8k.html",encoding="utf8",errors="ignore").read()
for m in re.finditer(r'\{[^{}]*"name":"[^"]+\.m"[^{}]*\}',t): print(m.group(0)[:600]); print()
EOF
for id in 814057478415 814058719477 814059292441; do curl -sL "https://app.box.com/index.php?rm=box_download_shared_file&shared_name=2u05p72kc18quwz3sw818pxs6dgmmd8k&file_id=f_$id" -o f_$id.m; file f_$id.m; head -c 300 f_$id.m; echo; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; wc -l f_*.m; grep -n -i "width\|peak\|trough\|230\|100 spikes\|meanRate\|firing" f_814058719477.m | head -40
```

```
412 f_814057478415.m
 1288 f_814058719477.m
  794 f_814059292441.m
 2494 total
9:% calculates average rate, peak rate, perecentage of bursting,
36:% Bin width for the ratemap
37:param.binWidth = 2.5; %default: 2.5
47:% value when you change the bin width
49:% Bins with rate at 0.2 * peak rate and higher will be considered as part
148:    boxData.peakRate = 0;
239:    bins = ceil(obsLength2/param.binWidth);
240:    sLength = param.binWidth*bins;
241:    mapAxis = (-sLength/2+param.binWidth/2):param.binWidth:(sLength/2-param.binWidth/2);
258:    % Calculate the spike firing map
301:    % Peak rate of rate map
302:    peakRate = nanmax(nanmax(map));
315:    drawfield(map,mapAxis,'jet',max(max(map)),param.binWidth,spatial_info);
328:    xLength = maxX - xStart + param.binWidth*2;
329:    yLength = maxY - yStart + param.binWidth*2;
335:    drawfield(flipud(aMap),aColAxis,'jet',nanmax(nanmax(aMap)),param.binWidth,param.smoothing);
[... 25 more lines not kept]
```

**Agent**

The linked code is the 2021 place-cell protocol code (spatial rate maps), not this paper's task analyses, so it settles nothing here. Now reading Supplementary Tables 1 and 2.

**Agent calls Bash**

```bash
cd  sed -n 1700,2210p $TMPDIR/p.txt | paste -sd'|' | sed 's/|/ | /g' | fold -w 250
```

```
T5 | X 2=2.29, p=3.6e-9 | 1 odor: p=9.2e-8 | 2 odor: p=1.1e-3 | no responsive type: p=2.5e-10 | NS for other pairs | S4a | AB-only | 95th percentile value = 1.56 | 2g, S4a | T1 | 95th percentile value = 1.57 | S4a | T2 | 95th percentile value = 1.55 
| 2g, S4a | T3 | 95th percentile value = 1.51 | S4a | T4 | 95th percentile value = 1.56 | 2g, S4a | T5 | 95th percentile value = 1.59 | S4b | AB-only | 95th percentile value = 1.86 | 2g, S4b | T1 | 95th percentile value = 2.14 | S4b | T2 | 95th perce
ntile value = 2.15 | 2g, S4b | T3 | 95th percentile value = 2.04 | S4b | T4 | 95th percentile value = 2.07 | 2g, S4b | T5 | 95th percentile value = 2.08 | T1a: p=0.023 | T1b: p=0.072 | T1c: p=8.7e-4 | T2: p=6.6e-7 | T3: p=1.7e-5 | T4: p=8.7e-6 | T5: 
p=1.1e-3 | A beta density | VTA vsSNc | 3b | % Amyloid bata density in the VTA and SNc: | APP-KI mice | Young APP-KI mice: 12 mice | Wilcoxon signed-rank test | p=0.0014, Z=-3.2 | TH+ fiber density-LEC | 3b | % TH+ fiber density in the LEC: | WT mice
 vs APP-KI mice | young WT:8 mice | young APP-KI: 8 mice | old WT: 6mice | old APP-KI: 6 mice | 2-way ANOVA | (Strain [WT vs APP-KI] x Age | [young vs old]) | Strain: F(1,24)=0.79; p=0.38 | Age: F(1,24)=0.57; p=0.46 | Strain x Age: F(1,24)=0.22; p=0.
22 | Tukey test | NS for all pairs | Dopamine Photometry | (correct + error sessions) | 4d | Significance of Ca2+ singal in 2-4 s priod | young WT: 10 hemispheres | young APP-KI: 8 hemispheres | Wilcoxon signed-rank test | p<0.05 | For each strain | 
GCaMP signals at Odor A | Strain: F(1,80)=0.19; p=0.66 | Time: F(4,80)=0.33; p=0.85 | Strain x Time: F(4,80)=0.45; p=0.77 | NS for all pairs | GCaMP signals at Odor B | Strain: F(1,80)=0.41; p=0.52 | Time: F(4,80)=0.46; p=0.75 | Strain x Time: F(4,80
)=0.69; p=0.59 | NS for all pairs | GCaMP signals at Odor 1 | Strain: F(1,80)=9.3; p=3.1e-3 | Time: F(4,80)=0.67; p=0.61 | Strain x Time: F(4,80)=2.5; p=0.047 | T1 WT vs T5 WT: p=0.048 | T1 WT vs T1 APP: p=4.2e-3 | T1 WT vs T2 APP: p=0.0343 | 
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 2210,3235p $TMPDIR/p.txt | paste -sd'|' | sed 's/|/ | /g' | fold -w 250
```

```
=== page 16 === | Supplementary Table 1. Statistics used in this study (continued) | E3c | LEC cells: | Distribution of Spike Types | E4a | Distribution of FS, RS, WS cells | in young WT and young APP-KI mice | Young WT: 479 cells | Young APP-KI:846 
cells | Chi-Square test | p=1.2e-23, x2=105.51 | Benjamini-Hochberg post- | hoc test | NS: p=7.3e-9 | RS: p=1.0e-4 | WS: p<0.00001 | Spike width:Putative principal neurons | Young WT:423 cells | Young APP-KI: 636 cells | p = 1.7e-30, Z = 11.47 | Spik
e width: Putative interneurons | Young WT:56 cells | Young APP-KI: 210 cells | p = 0.76, Z = -0.29 | Wilcoxon rank sum test | p = 3.9e-15, Z = -7.85 | Kolmogorov–Smirnov test | p=3.3e-12 | Wilcoxon rank sum test | p = 4.7e-5, Z = -4.06 | Kolmogorov–S
mirnov test | p=4.4e-4 | Wilcoxon rank sum test | p = 0.0044, Z = -2.84 | Kolmogorov–Smirnov test | p=0.031 | Wilcoxon rank sum test | p = 0.75, Z = 0.31 | Kolmogorov–Smirnov test | p=0.81 | T1 | p=5.5e-4, x2=39.39 | A: p=0.032 | A-1: p=0.032 | null 
responsive type: p=1.4e-5 | NS for other pairs | T3 | p=4.5e-7, x2=58.49 | A: p=3.8e-3 | 1: p=0.014 | A-1: p=0.026 | B-1: p=0.026 | null responsive type: p=3.1e-8 | NS for other pairs | T5 | p=6.4e-6, x2=51.63 | A: p=1.8e-3 | 1: p=0.048 | A-1: p=0.04
8 | B-1: p=0.048 | null responsive type: p=8.2e-10 | NS for other pairs | LEC cells recording | E6a, E6b, E6c, E6d, E6e, | E6f, E6g, E6h | Significance of LEC cell firing in odor period | 10 trials | Wilcoxon signed-rank test | p<0.05 | For each LEC 
cell | AB-only | 95th percentile value = 1.33 | T1 | 95th percentile value = 1.42 | T2 | 95th percentile value = 1.35 | T3 | 95th percentile value = 1.36 | T4 | 95th percentile value = 1.41 | T5 | 95th percentile value = 1.43 | AB-only | 95th percent
ile value = 0.69 | T1 | 95th percentile value = 0.69 | T2 | 95th percentile value = 0.71 | T3 | 95th percentile value = 0.71 | T4 | 95th percentile value = 0.73 | T5 | 95th percentile value = 0.76 | Extended Data Fig. 3 (continuted) | Tukey te
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 3235,3612p $TMPDIR/p.txt | paste -sd'|' | sed 's/|/ | /g' | fold -w 250 | head -60
```

```
=== page 20 === | Supplementary Table 2. Animals used in this study | Figure # | Genotype | Experiment | Virus or Drug Injected | Animal ID | Sex | Implanted Device | 991 | M | 1293 | F | 1417 | M | 1638 | M | 1639 | M | 1640 | M | 1641 | F | 815 | M
 | 1191 | M | 1193 | F | 1425 | F | 1426 | F | 692 | F | 926 | F | 934 | F | 989 | M | 1247 | F | 1294 | M | 1421 | F | 1452 | F | 1479 | M | 364 | M | 375 | F | 390 | F | 1398 | F | 1431 | M | 247 | M | 690 | F | 703 | M | 925 | M | 941 | M | 163* |
 M | 164* | M | 263 | F | 264 | F | 265 | M | 266 | M | 1028 | F | 1029 | F | 1416 | F | 1451* | M | 1477* | M | Fig. 1, S1 | Old WT | Behavior test | None | Fig. 1, 4, | S1, S6, S7 | None | None | None | Optic fibers (400μm) | Tetrode drive | (64 ch
annels) | Fig.1, 2, E4-7, | S1,S4 | APP-KI | x | DAT-Cre | Dopamine photometry | (right hemisphere* or bilateral) | AAV-flex-GCaMP6 @ VTA/SNc | (0.75-1μL) | None | Young WT | LEC L2/3 cells recording | (right hemisphere) | None | None | Behavior test
 | Behavior test | Young APP-KI | Old APP-KI | Optic fibers (400μm) | AAV-flex-GCaMP6 @ VTA/SNc | (0.75-1μL) | Dopamine photometry | (left hemisphere* or bilateral) | DAT-Cre | None | Tetrode drive | (64 channels) | LEC L2/3 cells recording | (right 
hemisphere) | Young APP-KI |  | === page 21 === | Supplementary Table 2. Animals used in this study (continued) | 1167 | M | 1170 | M | 1183 | M | 1194 | F | 1195 | F | 1380 | F | 1414 | F | 1583 | M | 1585 | F | 1588 | F | 1601 | M | 2017 | M | 2018
 | M | 2019 | M | 2020 | F | 2021 | F | 2022 | F | 2023 | F | 2024 | F | 2178 | M | 2179 | M | 2180 | F | 2182 | F | 2243 | M | 2244 | M | 2246 | M | 2248 | F | 2250 | F | 2490 | M | 2491 | M | 2492 | F | 2493 | F | 2427 | M | 2474 | M | 2475 | F | 2
477 | F | 210 | M | 310 | F | 346 | M | 387 | M | 789 | F | 1199 | M | 1253 | M | 1254 | M | 1517 | M | Dopaminergic fiber stimulation | (bilateral) | AAV-DIO-ChR2-mCherry @ VTA/SNc | or AAV-DIO-ChR2-eYFP @ VTA/SNc | (1μL) | Optic fibers (400μ
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8744500/fullTextXML" -o lee.xml; ls -la lee.xml; python - <<'EOF'
import re,html
t=open("lee.xml",encoding="utf8").read()
t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(re.sub(r'\s+',' ',t))
i=t.find('Methods')
open("lee.txt","w").write(t)
for kw in ['Principal component','Similarity index','Shuffle','Behavioral performance','sliding window','Photometry','z-score','bootstrap']:
    for m in re.finditer(kw,t):
        print('==',kw,m.start()); print(t[max(0,m.start()-200):m.start()+1500]); break
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; cat lee.xml; echo; curl -sL "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC8744500/unicode" -o lee.json; ls -la lee.json; head -c 300 lee.json
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import json
d=json.load(open("lee.json"))
ps=d[0]["documents"][0]["passages"]
out=[]
for p in ps:
    sec=p["infons"].get("section_type","")
    if sec in ("METHODS",):
        out.append(p["text"])
t="\n".join(out)
open("lee_methods.txt","w").write(t)
print(len(t))
EOF
grep -n -i "principal component\|similarity\|shuffl\|behavioral performance\|photometry\|z-score\|bootstrap\|sliding\|PCA" lee_methods.txt | cut -c1-200
```

```
27692
9:For optogenetic inhibition experiment, optic fibers of 400 μm diameter (Thorlabs) were used. For photometry recording, optic fibers with 400 μm diameter (Doric lenses) were used.
20:For optogenetic inhibition experiments in Sim1-Cre, Wfs1-Cre and DAT-Cre animals, optic fibers with 400 μm diameter were bilaterally implanted at AP 3.5 mm, ML 3.5 mm, 4000 μm depth with an angle o
41:For inhibition experiments of fan cells, pyramidal cells, and DAT+ fibers, 635 nm red laser stimulation (20 mW mm−2 at the tip of implanted optic fiber) was delivered through the implanted optic fi
42:Photometry recording.
43:The photometry recording was performed using a custom-made photometry setup as described previously (Menegas et al., 2017). Briefly, two excitation lasers (473nm and 561nm, 0.1–0.2 mW) were deliver
47:Behavioral performance was calculated by counting the licking responses to Odor-A and 1 (hit) and the withholdings to Odor-B and 2 (correct rejection). Instantaneous behavioral performance (instant
53:Mean firing rates in 50-ms bins were obtained using a Gaussian filter with a sigma of 100 ms and transformed as z-score using the mean firing rate during a baseline pre-odor period (−1 – 0 s before
54:Principal component analysis (PCA).
55:Mean firing rates in 50-ms bins during −1 – 4 s after odor onset in each odor type (A, B, 1, 2) were normalized and processed for principal component analysis as described previously (Cunningham an
56:Shuffle analysis.
57:Shuffle analysis was used to statistically evaluate the mean distances between odor types (Igarashi et al., 2014). Shuffle data were obtained by randomly shuffling the assignment of odor type for e
58:Similarity index.
59:A mean shuffle distance was obtained by averaging the shuffle distance across T1 – T5. A similarity index (SI) was calculated as the difference between real and mean shuffled distance, normalized b
60:Bootstrapping analysis.
61:The change of SI during associative learning was compared using the b
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '44,64p' lee_methods.txt
```

```
Data Analysis
Unless indicated otherwise, analyses were performed using MATLAB codes written by the authors.
Behavioral analysis.
Behavioral performance was calculated by counting the licking responses to Odor-A and 1 (hit) and the withholdings to Odor-B and 2 (correct rejection). Instantaneous behavioral performance (instantaneous percent correct trials) for Odors-A/B and Odor-1/2 was calculated from a sum of hit and correct rejection trials within a sliding window of 20 trials, divided by a total trial number of 20. The mean behavioral performance for each session after the learning (percent correct trials in T5) was calculated from a sum of hit and correct rejection trials during trials 121–160, divided by a total trial number of 40. To evaluate the behavioral performance for each mouse, these two values were averaged for all sessions with the same condition (control or inhibition) for each mouse regardless of the performance and shown in the Figures. For percent correct sessions, sessions with (percent correct trials in T5) > 80% were counted from all sessions pooled from multiple animals.
Spike sorting.
Spike sorting was performed offline using graphical cluster-cutting software, MClust by Dr. David Redish. Putative excitatory cells were distinguished from putative interneurons by spike peak-valley width and average rate. All putative excitatory cells with spike peak-valley width of more than 230 μs and cells with more than 100 spikes in a session were included for further analysis. We compared spike clusters before and after turning tetrodes using the distribution of clusters in the 4-dimensional energy plots, spike autocorrelation, and mean firing frequency, as well as the coding property in the learning tasks. If there was any sign that clusters can be similar before and after the turning, they were considered as the same neuron, and the cluster after the turning was excluded from analyses. If new clusters appeared, they were included in the analyses.
Opt-ta
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import fitz
d=fitz.open('paper/10.1038-s41593-026-02260-w.supp.pdf'); print(d.page_count)
for i in [13,14,15,16,17]:
    d[i].get_pixmap(dpi=110).save('$TMPDIR/st_%d.png'%(i+1))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm mutool; pdftoppm -f 14 -l 18 -r 100 -png paper/10.1038-s41593-026-02260-w.supp.pdf $TMPDIR/st && ls $TMPDIR/st*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02260-w.supp.pdf",
 "pages": "14-15"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --quiet --target $TMPDIR/pylib pymupdf 2>&1 | tail -2; PYTHONPATH=$TMPDIR/pylib python -c "import fitz; print(fitz.__doc__)"
```

```
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
[0;93m2026-10-21 04:56:49.403610048 [W:onnxruntime:Default, device_discovery.cc:95 GetPciBusId] Skipping pci_bus_id for PCI path at "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/MSFT1000:00/5620e0c7-8062-4dce-aeb7-520c7ef76171" because filename "5620e0c7-8062-4dce-aeb7-520c7ef76171" did not match expected pattern of [0-9a-f]+:[0-9a-f]+:[0-9a-f]+[.][0-9a-f]+[m
/tmp/claude-1001/pylib/fitz/__init__.py:17: FutureWarning: The `fitz` API is deprecated and will be removed in future. Use `import pymupdf` instead.
  warnings.warn(
PyMuPDF 2.0: Python bindings for the MuPDF 1.28.5 library.
Python 3.13 running on linux (64-bit).
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/pylib python -c "
import pymupdf
d=pymupdf.open('paper/10.1038-s41593-026-02260-w.supp.pdf')
for i in [13,14,15,16,17]:
    d[i].get_pixmap(dpi=130).save('$TMPDIR/st_%d.png'%(i+1))
print('ok')
" 2>&1 | grep -v onnx
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/st_14.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/st_15.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/st_16.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/st_18.png"
}
```

Result: no output.

**Agent**

Table mapping confirmed (old WT thresholds 2.41 etc., old APP 2.09 etc.; the L-DOPA row says 132 cells, against 144 in the text). Now checking the quote checker and schema.

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; ls schema* docs/ 2>/dev/null; grep -rn "kind:" claims/*/*.yaml | awk '{print $2,$3}' | sort | uniq -c
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | head -250; ls claims/
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 291 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"; ls claims/002020; head -60 claims/002020/*.yaml
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o "Neurophysiological data are available[^.]*\.[^.]*\." paper/*.txt | head -2; grep -c "" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/001968/10.1038-s41593-026-02260-w.yaml",
 "content": "# Claims for Nakagawa et al. (2026), \"Early dopamine disruption in the entorhinal cortex of a\n# knock-in model of Alzheimer's disease\", Nature Neuroscience (doi:10.1038/s41593-026-02260-w),\n# on dandiset 001968.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (open access, CC BY), as served by Europe PMC (PMC13246448),\n# in paper/10.1038-s41593-026-02260-w.txt: main text, figure legends, Methods, Extended Data\n# Fig. 1 to 10 legends, and the supplement PDF (Supplementary Figs. 1 to 11 and Supplementary\n# Tables 1 to 4) extracted to text. Supplementary Table 1 (statistics) is garbled in the text and\n# its pages 14 to 18 were read from the supplement PDF. The main article PDF was not supplied, so\n# the figures themselves were not seen; numbers shown only in figure panels are not available\n# here. The reporting summary and source data were not supplied and were not read.\n#\n# Methods by reference. The Methods describe behavioral performance, spike sorting, PCA,\n# shuffle, similarity index, bootstrapping and photometry as \"previously described\" in their\n# ref. 16 (Lee et al. 2021, Nature 598, 321, doi:10.1038/s41586-021-03948-8). The Methods of\n# that paper (author manuscript, PMC8744500, read through the PMC BioC service) were read for\n# those steps only, and are cited below as \"ref. 16\".\n#\n# Code. The Code availability statement says \"standard functions in MATLAB\" were used and that\n# analytical codes are at https://www.igarashilab.org/resource. That page (read 2026-10-21) links\n# a Box folder \"matlabCodes\" with three files, analyze4LinearTracks.m, analyzePopulationVector.m\n# (header dated 05/20/2021) and boxSpikeInfo3.m, and a zip of 110 hippocampal neurons\n# (Igarashi_remapping_data.zip). These belong to the 2021 place cell remapping protocol (the\n# paper's ref. 39) and compute spatial rate maps and population vector correlations on linear\n# tracks. None of them covers the odor task, cue responses, PCA trajectories, similarity index,\n# bootstrap, decoding or photometry of this paper; Box gives no commit or version. So no method\n# detail below is settled by code.\n#\n# The dandiset. Its title is the paper's title; its description says only that it holds \"data\n# associated with\" the paper. Its archive summary lists mouse, an electrophysiological approach,\n# spike sorting, NWB, and 37 subjects. It is read here as meant to hold the tetrode recordings of\n# LEC L2/3 units (Fig. 2, Extended Data Figs. 3 to 9, Fig. 6d to i), possibly with the task\n# events of those sessions. Whether it also holds behavior of other mice, photometry or\n# histology is the author's to find; claims on those data are written all the same.\n#\n# Data the paper used, as it reports them.\n# - Mice. Homozygous APP NL-G-F knock-in mice (APP-KI) and APP WT/WT C57BL/6 controls (WT);\n#   young 3 to 6 months, old 7 to 11 months; 12 to 13 months for histology. Photometry and\n#   optogenetics used APP-KI x DAT-Cre mice and DAT-Cre controls; PS19 mice for one L-DOPA test.\n#   Animal IDs, sex and procedure per mouse are in Supplementary Table 2.\n# - Task. Head-fixed olfactory go/no-go task. Prelearned Odor-A (isoamyl acetate, lick for\n#   sucrose) and Odor-B (alpha-pinene, withhold licking to avoid quinine). Each day an AB-only\n#   session of about 20 trials, then an AB12 session of 160 trials with a novel rewarded Odor-1\n#   (C, E or G) and a novel punished Odor-2 (D, F or H), in random order every 18 to 22 s; A and\n#   B 20% each, 1 and 2 30% each. Delay of 2 s between odor and the response window; licking in\n#   the delay aborts the trial. Timepoints T1 to T5 within the session; T1 first 10 trials, T3\n#   middle 10, T5 last 10 (Fig. 2d legend); T1 also split into T1a (trials 1 to 3), T1b (4 to 6)\n#   and T1c (7 to 9). Behavioral T5 is trials 121 to 160. A session is correct when percent\n#   correct in T5 exceeds 80%, an error session otherwise.\n# - Units. Tetrode drives (64 channels) in right LEC, layer 2/3 (+-200 um of putative L2).\n#   Young: 479 neurons from 5 WT mice and 846 from 5 APP-KI mice; putative principal cells\n#   (peak-trough width > 230 us, > 100 spikes in a session) 423 and 636; putative interneurons\n#   56 and 210. Per mouse principal cells (Supplementary Fig. 2): WT #00364 95, #00375 48,\n#   #00390 130, #01398 112, #01431 38; APP-KI #00789 125, #01199 52, #01253 271, #01254 89,\n#   #01517 99 (97 in the Extended Data Fig. 3b legend). Correct and error sessions for young\n#   WT 352 and 71 cells, young APP-KI 411 and 225 cells (Supplementary Table 1). Old: 671 cells\n#   (WT) and 618 cells (APP-KI). L-DOPA: 144 cells from 4 L-DOPA mice and 132 from 4 saline\n#   mice, all APP-KI (Supplementary Table 1 prints 132 for both). Tetrodes were moved 40 to\n#   80 um between sessions, so each session holds new cells.\n# - Behavior. Young 11 WT and 16 APP-KI mice, old 11 WT and 14 APP-KI. Optogenetics 11 young\n#   APP-KI x DAT-Cre mice, stimulation on Odor-1 trials (473 nm, 5 s from Odor-1 onset then a\n#   10 s taper), against no-laser sessions in the same mice. L-DOPA (50 mg/kg i.p., 30 min before\n#   testing, 5 days) 9 mice, saline 8 mice; PS19 5 and 5; WT 4 and 4 (Supplementary Fig. 11\n#   also says 5 L-DOPA WT mice).\n# - Photometry. GCaMP6m in VTA/SNc dopamine neurons, fibers in LEC; 10 hemispheres from WT\n#   (DAT-Cre) and 8 from APP-KI x DAT-Cre mice.\n# - Histology. Abeta immunostaining by age (4 mice per group), TH+ fiber density in LEC and TH+\n#   cells in VTA/SNc (8 young WT, 8 young APP-KI, 6 old WT, 6 old APP-KI).\n#\n# Shared method, from the Methods, the legends, Supplementary Table 1 and ref. 16.\n# - Behavioral performance (Methods; ref. 16). Hits (licks to A or 1) plus correct rejections\n#   (no lick to B or 2), in a sliding window of 20 trials for the curves; percent correct in T5\n#   from trials 121 to 160; averaged over all sessions of a mouse; mice are the units. Open,\n#   with readings (B1) the trials of each odor pair that fall in session trials 121 to 160,\n#   (B2) the last 40 trials of each odor pair. Whether aborted trials count is open; the reading\n#   is that they count as trials of their odor, with their exclusion as a variant.\n# - Correct session. Methods say \"> 80%\", Results say \">= 80%\". Both are run; they differ only\n#   for sessions at exactly 80%.\n# - Timepoints for units. T1 is read as the first 10 trials of each odor type, T5 the last 10,\n#   T3 the middle 10, since T1a to T1c (trials 1 to 3, 4 to 6, 7 to 9) count trials within an odor\n#   type and cells from different sessions are pooled. T2 and T4 are not defined. Open, with\n#   readings (T-a) 10-trial blocks of each odor type centered midway between T1 and T3 and\n#   between T3 and T5, (T-b) each odor type's trials split into five equal blocks, with the\n#   first, middle and last 10 trials for T1, T3 and T5 and the whole second and fourth blocks\n#   for T2 and T4.\n# - Spike response (Methods). Firing rates in 50 ms bins, Gaussian filter sigma 100 ms, z-scored\n#   to the -1 to 0 s pre-odor baseline. A cell responds to an odor when its spike count 0.5 to\n#   1.5 s after odor onset differs from the 1 s pre-odor count over the timepoint's 10 trials\n#   (Wilcoxon signed-rank; Extended Data Fig. 5 says classification used 0.5 to 1.5 s). Open,\n#   with readings for the threshold (P05) p < 0.05 (Supplementary Table 1), (P01) p < 0.01\n#   (Results, Fig. 2b); for the direction (D+) increases only (\"fired to\"), (D+-) any change;\n#   for the period (W1) odor period only, (W3) any of odor (0.5 to 1.5 s), delay (2 to 3 s) and\n#   choice (3 to 4 s) periods (Methods list all three; Fig. 2b says \"cue-delay period\").\n# - PCA (Methods; ref. 16). For each timepoint separately (ref. 16 reports explained variance per\n#   timepoint), each cell's mean firing rate in 50 ms bins from -1 to 4 s after odor onset for\n#   each of the four odor types, concatenated; normalized per neuron by subtracting the minimum\n#   and dividing by the maximum; MATLAB pca with neurons as variables; PC1 and PC2 kept;\n#   Euclidean distance between the trajectories of two odor types, averaged over 0.5 to 1.5 s.\n#   Cells of all sessions and mice of a group are pooled. Open, with readings (N1) (x - min) /\n#   max, (N2) (x - min) / (max - min); and (F1) firing rates smoothed as in Spike response,\n#   (F2) unsmoothed binned rates.\n# - Shuffle (Methods; ref. 16). Odor labels shuffled across trials, keeping the count of each\n#   type; 1000 shuffles; the 95th percentile of the shuffle distances of each odor pair, averaged\n#   over pairs, is the significance threshold. Supplementary Table 1 calls it \"trial shift\".\n#   Open, with readings (S1) one permutation per session applied to all its cells, (S2) an\n#   independent permutation per cell.\n# - Similarity index (Methods). SI = -(real distance - mean shuffle distance) / mean shuffle\n#   distance, the mean shuffle distance averaged across T1 to T5. Open, with readings (M1) the\n#   mean shuffle distance of the odor pair itself (A-1), (M2) averaged over all six pairs.\n# - Bootstrap (Methods). Neurons resampled with replacement, PCA and SI recomputed, 1000 times;\n#   the difference of SIs between groups, bootstrap by bootstrap, is tested against 0, p < 0.05.\n#   The Results call the test \"maximum likelihood estimation\". Open, with readings (BS1) a normal\n#   distribution fitted to the differences by maximum likelihood, two-sided p of 0 under it,\n#   (BS2) the empirical two-sided fraction of differences on the other side of 0.\n# - Photometry (ref. 16). dF/F from the mean of the 1 s before cue, Gaussian filter sigma 200 ms,\n#   z-scored to the 1 s before cue; mean per odor type and timepoint per hemisphere. The window\n#   is open, with readings (G1) 1 to 4 s after cue onset (Fig. 4d legend), (G2) 2 to 4 s\n#   (Supplementary Table 1), (G3) 0.5 to 3 s (ref. 16).\n# - Statistics. The ANOVAs are ordinary (not repeated measures) on per mouse, per hemisphere or\n#   per session values, as their degrees of freedom show; Tukey post hoc; two-sided tests.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001968\"\npaper: doi:10.1038/s41593-026-02260-w\nclaims:\n- id: units-recorded\n  statement: In LEC layer 2/3 of young mice, 479 neurons were recorded from 5 WT mice and 846 from\n    5 APP-KI mice.\n  source: Results, Disrupted associative memory encoding in lateral entorhinal cortex layer 2/3\n    neurons, paragraph 1\n  quote: recorded 479 and 846 neurons from n = 5 young WT and n = 5 young APP-KI mice, respectively\n  expected:\n  - quantity: young WT neurons\n    value: 479\n    tolerance: 48\n  - quantity: young APP-KI neurons\n    value: 846\n    tolerance: 85\n  criterion: Counts of sorted units from young WT and young APP-KI tetrode sessions. The putative\n    principal cells (peak-trough width above 230 us and more than 100 spikes in the session,\n    Methods) are counted as well and compared with 423 and 636 (Fig. 2d legend) and with the\n    per mouse counts of Supplementary Fig. 2. Reproduced when both totals are within tolerance.\n- id: ed4a-spike-type-distribution\n  statement: The proportions of narrow, regular and wide spiking LEC L2/3 cells differ between\n    young WT and young APP-KI mice.\n  source: Extended Data Fig. 4a; Supplementary Table 1\n  quote: Bottom, percentage of NS, RS, and WS cells in young WT and young APP-KI mice. ( p =\n    1.2e-23, Chi-squared test for comparing distributions\n  statistics:\n  - test: Chi-squared test\n    statistic: chi2 = 105.51\n    p: 1.2e-23\n    n: 479 young WT and 846 young APP-KI cells\n  depends_on:\n  - units-recorded\n  criterion: All units classified by spike peak-trough width into NS (below 230 us), RS (230 to\n    390 us) and WS (above 390 us), the cut offs of Extended Data Fig. 4a; chi-squared test of the\n    3 by 2 table. The channel the width is read from is not given; readings (a) the channel with\n    the largest mean amplitude, (b) the mean over the four channels. Reproduced when p < 0.05.\n- id: ed4b-spike-width\n  statement: Putative principal cells of LEC L2/3 have narrower spikes in young APP-KI mice than\n    in young WT mice, while putative interneurons do not differ.\n  source: Results, Disrupted associative memory encoding in lateral entorhinal cortex layer 2/3\n    neurons, paragraph 1; Extended Data Fig. 4b; Supplementary Fig. 2b\n  quote: LEC L2/3 neurons in APP-KI mice showed decreasing spike widths compared to those of WT\n    mice, suggesting alterations in spike generation mechanisms\n  statistics:\n  - about: principal cells, cells as units\n    test: two-sided rank sum test\n    statistic: Z = 11.47\n    p: 3.9e-15\n    n: 423 young WT and 636 young APP-KI cells\n  - about: interneurons, cells as units\n    test: two-sided rank sum test\n    statistic: Z = -0.29\n    p: 0.76\n    n: 56 young WT and 210 young APP-KI cells\n  - about: principal cells, mice as units\n    test: two-sided unpaired t-test\n    statistic: t(8) = 2.49\n    p: 0.037\n    n: 5 and 5 mice\n  depends_on:\n  - units-recorded\n  criterion: Peak-trough width as in ed4a-spike-type-distribution; principal cells are RS plus WS,\n    interneurons NS (Supplementary Fig. 2b). Wilcoxon rank sum test on cells. Supplementary Table 1\n    gives p = 1.7e-30 for the principal cells where the legend gives 3.9e-15; either is\n    significant. Reproduced when the principal cells are narrower in APP-KI at p < 0.05 and the\n    interneurons do not differ at p < 0.05 (the paper's test, a claim of absence for that part).\n    The per mouse t-test is shown as well.\n- id: ed4c-higher-firing-rates\n  statement: Mean firing rates of putative principal neurons and interneurons in LEC L2/3 are\n    higher in young APP-KI mice than in young WT mice.\n  source: Results, Disrupted associative memory encoding in lateral entorhinal cortex layer 2/3\n    neurons, paragraph 1; Extended Data Fig. 4c and 4d\n  quote: the mean firing rates of putative LEC L2/3 principal neurons and interneurons were both\n    higher in APP-KI mice than those of WT mice\n  statistics:\n  - about: principal cells, mean rate\n    test: two-sided rank sum test\n    statistic: Z = -7.85\n    p: 3.9e-15\n    n: 423 young WT and 636 young APP-KI cells\n  - about: interneurons, mean rate\n    test: two-sided rank sum test\n    statistic: Z = -2.84\n    p: 0.0044\n    n: 56 young WT and 210 young APP-KI cells\n  - about: principal cells, peak rate\n    test: two-sided rank sum test\n    statistic: Z = -4.06\n    p: 4.7e-5\n  depends_on:\n  - units-recorded\n  criterion: Mean firing rate of each cell over the associative learning session (Extended Data\n    Fig. 4c), Wilcoxon rank sum test on cells, principal (RS and WS) and interneurons (NS)\n    separately. The rate's definition is not given; readings (a) spike count over the whole\n    recording of the session, (b) over the AB12 session's trial periods only. Reproduced when\n    both cell classes have higher rates in APP-KI at p < 0.05; partially when one class does.\n    The peak rate (not defined; read as the maximum of the 50 ms, sigma 100 ms smoothed rate) and\n    the per mouse t-tests of Supplementary Fig. 2c, 2d are shown.\n- id: fig2d-more-cue-responsive\n  statement: At the end of the session (T5), 16% of LEC L2/3 principal neurons respond to at\n    least one odor cue in young WT mice and 34% in young APP-KI mice; the distribution of\n    response classes differs at T1, T3 and T5.\n  source: Results, Disrupted associative memory encoding in lateral entorhinal cortex layer 2/3\n    neurons, paragraph 2; Fig. 2d\n  quote: While 16% of LEC L2/3 neurons fired to at least one odor cue at T5 in WT mice, an\n    excessive 34% of neurons exhibited cue responses in APP-KI mice\n  statistics:\n  - about: T5 distribution\n    test: chi-squared test\n    statistic: chi2 = 2.29\n    p: 3.6e-9\n    n: 423 young WT and 636 young APP-KI cells\n  - about: T1 distribution\n    test: chi-squared test\n    p: 7.1e-5\n  - about: T3 distribution\n    test: chi-squared test\n    p: 1.5e-7\n  expected:\n  - quantity: WT cells responsive to at least one odor at T5\n    value: 16\n    tolerance: 1.6\n    unit: percent\n  - quantity: APP-KI cells responsive to at least one odor at T5\n    value: 34\n    tolerance: 3.4\n    unit: percent\n  depends_on:\n  - units-recorded\n  criterion: Principal cells of all young sessions (correct and error). Each cell is classed at\n    T1, T3 and T5 by the number of odor types (0 to 4) it responds to, as in Shared method, Spike\n    response, under the eight readings P05 or P01, D+ or D+-, W1 or W3, each with timepoint\n    reading T-a (T1, T3, T5 do not depend on it). Chi-squared test of the class by strain table\n    at each timepoint, Benjamini-Hochberg post hoc per class. Reproduced when, under one reading,\n    both T5 percentages are within tolerance and the T5 chi-squared test has p < 0.05 with more\n    responsive cells in APP-KI. The printed chi2 of 2.29 cannot give p = 3.6e-9 on these counts\n    and is not used as a target.\n- id: ed5-more-odor-a-cells\n  statement: Among LEC L2/3 cells, young APP-KI mice have a higher percentage of Odor-A\n    responsive cells than young WT mice through T1 to T5.\n  source: Results, Disrupted associative memory encoding in lateral entorhinal cortex layer 2/3\n    neurons, paragraph 2; Extended Data Fig. 5; Supplementary Table 1\n  quote: Among these cue-responsive neurons in APP-KI mice, the percentage of Odor-A responsive\n    cells was higher in APP-KI mice compared to those in WT mice\n  statistics:\n  - about: overall distribution at T1, T3, T5\n    test: chi-squared test\n    p: 5.5e-4\n    n: 423 young WT and 636 young APP-KI cells\n  - about: Odor-A class at T5\n    test: Benjamini-Hochberg post hoc test\n    p: 1.8e-3\n  - about: Odor-A class, mice as units, T5\n    test: two-sided unpaired t-test followed by FDR correction\n    p: 0.031\n    corrected: FDR (Benjamini-Hochberg)\n    n: 5 and 5 mice\n  depends_on:\n  - fig2d-more-cue-responsive\n  criterion: Response classes by odor combination (A, B, 1, 2, A-1, and so on, and none) from the\n    responses of fig2d-more-cue-responsive, under the same readings, as a percentage of all\n    principal cells. Chi-squared test of the class by strain table at T1, T3, T5, with\n    Benjamini-Hochberg post hoc tests per class. Whether \"Odor-A cells\" means cells responding\n    to A only or to A among others is open; both are run. Reproduced when, under one reading, the\n    Odor-A class is larger in APP-KI at T1, T3 and T5 with a post hoc p < 0.05 at each;\n    partially when that holds at one or two timepoints.\n- id: fig2j-per-mouse-response-types\n  statement: Analysed per mouse, the response type distribution of LEC L2/3 cells differs between\n    young WT and young APP-KI mice at T5, with fewer non-responsive cells and more 1-odor cells in\n    APP-KI mice.\n  source: Fig. 2j; Extended Data Fig. 3c\n  quote: Similar results were obtained when data were separated and analyzed per animal\n  statistics:\n  - about: responsive type x strain at T5\n    test: two-way ANOVA\n    statistic: F(4,40) = 8.0\n    p: 7.7e-5\n    n: 5 mice per strain\n  - about: 1-odor cells at T5\n    test: two-sided Tukey post hoc test\n    p: 0.021\n  - about: non-responsive cells at T5\n    test: two-sided Tukey post hoc test\n    p: 4.3e-3\n  depends_on:\n  - fig2d-more-cue-responsive\n  criterion: Per mouse percentages of principal cells responding to 1, 2, 3 or 4 odors or none\n    at T5, under the readings of fig2d-more-cue-responsive; two-way ANOVA type by strain on the\n    50 mouse-by-type values, Tukey post hoc. Reproduced when, under one reading, the interaction\n    has p < 0.05 and the non-responsive percentage is lower in APP-KI with a Tukey p < 0.05.\n- id: fig2g-wt-a1-generalized\n  statement: In young WT mice, the PCA distance between Odor-A and Odor-1 population trajectories\n    is slightly above the shuffle at T1 and below it from T2 to T5, so the two rewarded cues\n    become similarly represented.\n  source: Results, Disrupted associative memory encoding in lateral entorhinal cortex layer 2/3\n    neurons, paragraph 3; Fig. 2e, 2g, 2h; Supplementary Fig. 4a\n  quote: In WT mice, A-1 distance was slightly larger than the shuffle at T1, but became smaller\n    than the shuffle through T2–T5, indicating generalized representations of rewarded cues\n    during learning\n  expected:\n  - quantity: young WT shuffle 95th percentile, T1\n    value: 1.57\n    tolerance: 0.157\n  - quantity: young WT shuffle 95th percentile, T3\n    value: 1.51\n    tolerance: 0.151\n  - quantity: young WT shuffle 95th percentile, T5\n    value: 1.59\n    tolerance: 0.159\n  depends_on:\n  - units-recorded\n  criterion: PCA, shuffle and SI as in Shared method on the 423 young WT principal cells, correct\n    and error sessions pooled, under readings N1 or N2, F1 or F2, S1 or S2, M1 or M2, T-a or\n    T-b. \"Smaller than the shuffle\" is open, with readings (a) below the mean shuffle distance\n    (SI above 0), (b) below the 95th percentile threshold. Reproduced when, under one\n    combination of readings, the A-1 distance is above the shuffle at T1 and below it at each\n    of T2 to T5; partially when below at three of the four. The shuffle thresholds (from\n    Supplementary Table 1) are a check of the pipeline and are reported, not judged alone.\n- id: fig2f-app-a1-separated\n  statement: In young APP-KI mice, the Odor-A and Odor-1 trajectories stay far apart throughout\n    the session, the A-1 distance remaining above the shuffle from T1 to T5.\n  source: Results, Disrupted associative memory encoding in lateral entorhinal cortex layer 2/3\n    neurons, paragraph 3; Fig. 2f, 2g, 2h; Supplementary Fig. 4b\n  quote: However, A-1 distance in APP-KI mice remained above shuffle, indicating that Odors-A and\n    -1 representations were not generalized together in APP-KI mice\n  expected:\n  - quantity: young APP-KI shuffle 95th percentile, T1\n    value: 2.14\n    tolerance: 0.214\n  - quantity: young APP-KI shuffle 95th percentile, T3\n    value: 2.04\n    tolerance: 0.204\n  - quantity: young APP-KI shuffle 95th percentile, T5\n    value: 2.08\n    tolerance: 0.208\n  depends_on:\n  - units-recorded\n  criterion: As fig2g-wt-a1-generalized on the 636 young APP-KI principal cells. \"Above shuffle\"\n    is read as (a) above the mean shuffle distance (SI below 0), (b) above the 95th percentile\n    threshold. Reproduced when, under one combination of readings, the A-1 distance is above\n    the shuffle at each of T1 to T5; partially when at four of the five.\n- id: fig2i-si-wt-above-app\n  statement: Bootstrapped similarity between Odor-A and Odor-1 representations is higher in young\n    WT than in young APP-KI mice across the session, significantly at T1a and T1c to T5.\n  source: Results, Disrupted associative memory encoding in lateral entorhinal cortex layer 2/3\n    neurons, paragraph 3; Fig. 2i; Extended Data Fig. 8e\n  quote: A bootstrapping analysis confirmed the decreased A-1 similarity in APP-KI mice compared\n    to WT mice throughout the session\n  statistics:\n  - about: T1a\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 0.023\n  - about: T1b\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 0.072\n  - about: T1c\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 8.7e-4\n  - about: T2\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 6.6e-7\n  - about: T3\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 1.7e-5\n  - about: T4\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 8.7e-6\n  - about: T5\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 1.1e-3\n  depends_on:\n  - fig2g-wt-a1-generalized\n  - fig2f-app-a1-separated\n  criterion: Bootstrap as in Shared method (readings BS1 and BS2) on the SI of fig2g and fig2f,\n    with the same PCA readings. Reproduced when, under one combination of readings, WT minus\n    APP-KI SI is positive with p < 0.05 at each of T2 to T5 and at T1a or T1c; partially when it\n    is at two or three of T2 to T5. Bootstrap p values below 0.001 cannot be matched exactly\n    under BS2 and are compared as bounds.\n- id: fig2k-per-mouse-distance\n  statement: Analysed per mouse, the A-1 PCA distance at T5 is larger in young APP-KI mice than\n    in young WT mice.\n  source: Fig. 2k; Extended Data Fig. 3d\n  inferred: The finding is read from the Fig. 2k legend, which gives the test but no sentence of\n    the paper states its direction; Fig. 2f and the Results give it as larger in APP-KI.\n  statistics:\n  - test: two-sided unpaired t-test followed by FDR correction\n    p: 0.048\n    corrected: FDR\n    n: 5 young WT and 5 young APP-KI mice\n  depends_on:\n  - fig2g-wt-a1-generalized\n  criterion: PCA as in Shared method on each mouse's principal cells, per timepoint; A-1 mean\n    distance per mouse; unpaired t-test WT against APP-KI at each timepoint, Benjamini-Hochberg\n    FDR across timepoints. The family of the correction is open, with readings (a) T1, T3 and T5\n    (the timepoints of Fig. 2d), (b) T1 to T5, (c) T1a to T5. Reproduced when, under one\n    reading, the T5 A-1 distance is larger in APP-KI with corrected p < 0.05.\n- id: fig2l-per-mouse-si\n  statement: Analysed per mouse, the A-1 similarity index is lower in young APP-KI mice than in\n    young WT mice across learning.\n  source: Fig. 2l; Extended Data Fig. 3e\n  inferred: The finding is read from the Fig. 2l legend, which gives the strain effect; no\n    sentence of the Results states it apart from the general \"similar results\" per animal.\n  statistics:\n  - about: strain effect\n    test: two-way ANOVA (strain x timepoint)\n    statistic: F(1,56) = 14.8\n    p: 3.1e-4\n    n: 5 young WT and 5 young APP-KI mice\n  depends_on:\n  - fig2k-per-mouse-distance\n  criterion: Per mouse SI from fig2k-per-mouse-distance at T1a, T1b, T1c, T2, T3, T4, T5; two-way\n    ANOVA strain by timepoint on the 70 values. Reproduced when the strain effect has p < 0.05\n    with WT higher.\n- id: ed8-t1-a1-decrease\n  statement: Within the first 10 trials, the A-1 distance of young WT mice decreases clearly from\n    trials 1 to 3 (T1a) to trials 7 to 9 (T1c), while in young APP-KI mice the trajectories stay\n    far apart.\n  source: Results, Disrupted associative memory encoding in lateral entorhinal cortex layer 2/3\n    neurons, paragraph 3; Extended Data Fig. 8\n  quote: We further subdivided T1 into trials 1–3 (T1a), 4–6 (T1b) and 7–9 (T1c) and observed\n    clear decrease of A-1 distance from T1a to T1c\n  expected:\n  - quantity: young WT shuffle 95th percentile, T1a\n    value: 1.16\n    tolerance: 0.116\n  - quantity: young WT shuffle 95th percentile, T1c\n    value: 1.11\n    tolerance: 0.111\n  - quantity: young APP-KI shuffle 95th percentile, T1a\n    value: 1.67\n    tolerance: 0.167\n  - quantity: young APP-KI shuffle 95th percentile, T1c\n    value: 1.64\n    tolerance: 0.164\n  depends_on:\n  - fig2g-wt-a1-generalized\n  criterion: PCA as in fig2g-wt-a1-generalized on trials 1 to 3, 4 to 6 and 7 to 9 of each odor\n    type. Reproduced when, under one combination of readings, the WT A-1 distance at T1c is\n    below that at T1a and the WT minus APP-KI SI at T1c is positive in the bootstrap with\n    p < 0.05.\n- id: ed9-old-a1-separated\n  statement: In old mice, Odor-A and Odor-1 representations generalize from T2 to T5 in WT mice\n    but stay separated throughout the session in APP-KI mice.\n  source: Results, Disrupted associative memory encoding in lateral entorhinal cortex layer 2/3\n    neurons, paragraph 3; Extended Data Fig. 9; Supplementary Fig. 5\n  quote: In old age, generalization of Odors-A and -1 was observed through T2–T5 in WT mice,\n    whereas representations for these two cues were again kept separated throughout the session\n    in APP-KI mice\n  statistics:\n  - about: WT minus APP-KI SI, T1c\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 7.1e-6\n    n: 671 old WT and 618 old APP-KI cells\n  - about: T2\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 0.015\n  - about: T4\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 0.017\n  - about: T5\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 6.9e-3\n  expected:\n  - quantity: old WT cells\n    value: 671\n    tolerance: 67\n  - quantity: old APP-KI cells\n    value: 618\n    tolerance: 62\n  - quantity: old WT shuffle 95th percentile, T1\n    value: 2.41\n    tolerance: 0.241\n  - quantity: old APP-KI shuffle 95th percentile, T1\n    value: 2.09\n    tolerance: 0.209\n  criterion: As fig2g-wt-a1-generalized, fig2f-app-a1-separated and fig2i-si-wt-above-app on old\n    principal cells. Supplementary Table 1 gives T3 p = 0.089 and T1a p = 0.17, so T3 is not\n    required. Reproduced when, under one combination of readings, the old WT A-1 distance is\n    below the shuffle at T2 to T5 (at least three of four), the old APP-KI distance is above it\n    at T1 to T5 (at least four of five), and the bootstrap difference is positive with p < 0.05\n    at T2, T4 and T5.\n- id: ed7-decoding-correct-error\n  statement: In both young WT and young APP-KI mice, a decoder trained on Odor-A against Odor-B\n    activity discriminates Odor-1 from Odor-2 in correct sessions but not in error sessions.\n  source: Extended Data Fig. 7b and 7d\n  quote: The decoding analysis showed that neural activity in correct sessions discriminated\n    between Odor-1 vs. Odor-2, whereas activity in error session could not discriminate them in\n    WT mice\n  statistics:\n  - about: young WT, session x time\n    test: two-way ANOVA\n    statistic: F(6,126) = 37.83\n    p: 5.7e-26\n  - about: young APP-KI, session x time\n    test: two-way ANOVA\n    statistic: F(6,126) = 21.59\n    p: 2.4e-17\n  depends_on:\n  - units-recorded\n  criterion: Methods, Decoding analysis. Mean firing rates in 50 ms bins, 1 to 4 s after odor\n    onset, normalized; binary SVM (MATLAB, linear) trained on Odor-A against Odor-B, tested on\n    Odor-1 (as A) and Odor-2 (as B); 10 bootstraps of resampled cells; correct and error sessions\n    apart (young WT 352 and 71 cells, APP-KI 411 and 225). The test window is given as 2 to 5 s\n    in the same paragraph; readings (a) 1 to 4 s, (b) 2 to 5 s. What a sample is is open, with\n    readings (c) each 50 ms bin's population vector, (d) each odor type's mean over the window.\n    Normalization is read as in PCA (N1). Reproduced when, under one combination, decoding\n    performance is higher in correct than in error sessions at T2 to T5 in both strains by the\n    two-way ANOVA session by time with Tukey p < 0.05, and error-session performance stays near\n    chance (within 10 points of 50%).\n- id: fig3b-abeta-snc-above-vta\n  statement: In young APP-KI mice, Abeta plaque density is higher in the SNc than in the VTA.\n  source: Results, Dysfunction of lateral entorhinal cortex dopamine activity, paragraph 1;\n    Fig. 3b\n  quote: The density of Aβ plaques was higher in the SNc than that in the VTA\n  statistics:\n  - test: two-sided rank sum test (Wilcoxon signed-rank in Supplementary Table 1)\n    statistic: Z = -3.2\n    p: 1.4e-3\n    n: 12 young APP-KI mice\n  criterion: Histology. Abeta-positive area above three standard deviations of background as a\n    percentage of image area (Methods), per region and mouse. The test is named as rank sum in\n    the text and signed-rank in Supplementary Table 1; both are run. Reproduced when SNc exceeds\n    VTA with p < 0.05 under either.\n- id: fig3d-th-fibers-spared\n  statement: TH-positive axon density in the LEC does not differ significantly between APP-KI and\n    WT mice, nor between ages.\n  source: Results, Dysfunction of lateral entorhinal cortex dopamine activity, paragraph 1;\n    Fig. 3d\n  quote: Although there was a trend of decrease in the density of TH + axons of APP-KI mice, the\n    effect was not significant across strain nor age\n  statistics:\n  - about: strain\n    test: two-way ANOVA\n    statistic: F(1,24) = 0.79\n    p: 0.38\n    n: 8 young WT, 8 young APP-KI, 6 old WT, 6 old APP-KI mice\n  - about: age\n    test: two-way ANOVA\n    statistic: F(1,24) = 0.57\n    p: 0.46\n  criterion: A claim of absence, on the paper's test. TH-positive area in LEC images (3.4 to 3.8\n    mm AP) above three standard deviations of background, as a percentage of image area, per\n    mouse; two-way ANOVA strain by age. Reproduced when neither the strain nor the age effect has\n    p < 0.05; the effect sizes are reported.\n- id: ed10-th-cells-spared\n  statement: The density of TH-positive dopamine neurons in the VTA and SNc does not differ\n    between APP-KI and WT mice.\n  source: Results, Dysfunction of lateral entorhinal cortex dopamine activity, paragraph 1;\n    Extended Data Fig. 10\n  quote: We also measured the density of dopaminergic neurons in the VTA and SNc, finding no\n    significant alteration between APP-KI and WT mice\n  statistics:\n  - about: VTA, strain x age\n    test: two-way ANOVA\n    statistic: F(1,22) = 0.08\n    p: 0.78\n  - about: SNc, strain x age\n    test: two-way ANOVA\n    statistic: F(1,22) = 0.20\n    p: 0.65\n  criterion: A claim of absence, on the paper's test. TH-positive cell counts per image area in\n    VTA and SNc (3.4 to 3.6 mm AP), per hemisphere or mouse; two-way ANOVA strain by age with\n    Tukey post hoc. Reproduced when no strain effect, interaction or WT against APP-KI Tukey\n    comparison at the same age has p < 0.05 (Supplementary Table 1 reports one significant pair,\n    young WT against old APP-KI in SNc, which is across ages).\n- id: ed1-abeta-onset\n  statement: In APP-KI mice, Abeta accumulates with age, starting in the LEC at 2 months and in\n    the VTA and SNc from 4 months.\n  source: Results, Impaired associative memory formation in amyloid precursor protein knock-in\n    mice, paragraph 1; Results, Dysfunction of lateral entorhinal cortex dopamine activity,\n    paragraph 1; Extended Data Fig. 1\n  quote: age-dependent accumulation of amyloid-ß (Aβ) starts widely in cortical regions,\n    including the LEC, at 2 months of age\n  statistics:\n  - about: LEC, group\n    test: one-way ANOVA\n    statistic: F(7,24) = 15.34\n    p: 1.8e-7\n    n: 4 mice per group\n  - about: VTA, group\n    test: one-way ANOVA\n    statistic: F(7,24) = 13.18\n    p: 7.4e-7\n  criterion: Abeta-positive area per region and age group (12 month WT, APP-KI at 1, 2, 3, 4, 6,\n    9 and 12 months); one-way ANOVA with Tukey. Reproduced when density rises with age in all\n    three regions (Spearman correlation with age above 0 at p < 0.05) and the ANOVA has\n    p < 0.05 in each.\n- id: fig4b-wt-dopamine-t1\n  statement: In correct sessions of control mice, LEC dopamine fibers respond at T1 to prelearned\n    Odor-A, to novel Odor-1 and to novel Odor-2; with learning the Odor-2 signal disappears while\n    the Odor-A and Odor-1 signals remain to T5.\n  source: Results, Dysfunction of lateral entorhinal cortex dopamine activity, paragraph 2;\n    Fig. 4b\n  quote: At T1, dopamine was released primarily during delay periods of prelearned rewarded\n    Odor-A (mean z -scored GCaMP signal, 1.1 ± 0.24\n  statistics:\n  - about: Odor-A at T1 against precue\n    test: rank sum test\n    statistic: Z = -2.7\n    p: 6.9e-3\n  - about: Odor-1 at T1 against precue\n    test: rank sum test\n    statistic: Z = -2.8\n    p: 5.1e-3\n  - about: Odor-2 at T1 against precue\n    test: rank sum test\n    statistic: Z = -2.27\n    p: 0.028\n  expected:\n  - quantity: Odor-A mean z-scored GCaMP signal at T1\n    value: 1.1\n    tolerance: 0.24\n  - quantity: Odor-1 mean z-scored GCaMP signal at T1\n    value: 1.8\n    tolerance: 0.2\n  - quantity: Odor-2 mean z-scored GCaMP signal at T1\n    value: 0.76\n    tolerance: 0.24\n  criterion: Photometry as in Shared method, correct sessions of the 10 control hemispheres, mean\n    over hemispheres. The window is \"delay periods\"; readings G1, G2, G3 and (G4) 2 to 3 s, the\n    delay period of the spike analysis. The test against the precue period is named rank sum in\n    the text and Wilcoxon signed-rank in Supplementary Table 1; both are run. Reproduced when,\n    under one window, all three T1 means are within tolerance and above precue at p < 0.05, and\n    the Odor-2 signal at T5 is not significant while Odor-A and Odor-1 are.\n- id: fig4c-app-dopamine-delayed\n  statement: In APP-KI mice, Odor-1 dopamine signals emerge late, from T3, in correct sessions and\n    are absent in error sessions (39% of sessions), while Odor-A signals stay intact.\n  source: Results, Dysfunction of lateral entorhinal cortex dopamine activity, paragraph 2;\n    Fig. 4c; Supplementary Fig. 6b\n  quote: In APP-KI mice, in contrast, signals for Odor-1 emerged in a delayed manner from T3 (Fig.\n    4c , top), while dopamine signals for Odor-A remained intact when mice learned the association\n  expected:\n  - quantity: error sessions among APP-KI photometry sessions\n    value: 39\n    tolerance: 3.9\n    unit: percent\n  criterion: Photometry as in Shared method, APP-KI hemispheres, correct and error sessions apart\n    (correct when T5 performance exceeds 80%). Signal significance per timepoint against the\n    1 s precue by Wilcoxon signed-rank at p < 0.05 (Supplementary Table 1), windows G1 to G3.\n    Reproduced when, under one window, the error-session share is within tolerance, Odor-1 is not\n    significant at T1 and T2 and significant at T3 in correct sessions, not significant at any\n    timepoint in error sessions, and Odor-A is significant at T1 and T5 in both.\n- id: fig4d-app-odor1-dopamine-decreased\n  statement: Across all sessions, LEC dopamine activity during Odor-1 trials is significantly\n    lower in APP-KI mice than in WT mice at T1.\n  source: Results, Dysfunction of lateral entorhinal cortex dopamine activity, paragraph 2;\n    Fig. 4d\n  quote: dopamine activity was significantly decreased in APP-KI mice during Odor-1 trials at T1\n  statistics:\n  - about: strain x time, Odor-1\n    test: two-way ANOVA\n    statistic: F(4,80) = 2.5\n    p: 0.047\n    n: 10 WT and 8 APP-KI hemispheres\n  - about: WT against APP-KI at T1, Odor-1\n    test: two-sided Tukey post hoc test\n    p: 4.2e-3\n  criterion: Per hemisphere mean z-scored GCaMP signal for Odor-1 at T1 to T5, correct and error\n    sessions together, windows G1 (the legend's 1 to 4 s, main), G2, G3; two-way ANOVA strain by\n    timepoint on the 90 values, Tukey post hoc. Reproduced when, under G1, the interaction has\n    p < 0.05 and WT exceeds APP-KI at T1 with Tukey p < 0.05; partially when only the T1 Tukey\n    comparison holds; the other windows are shown.\n- id: fig4e-correct-sessions-odor1-decreased\n  statement: In correct sessions, Odor-1 dopamine activity at T1 is also lower in APP-KI mice\n    than in WT mice, with no significant interaction for Odor-2.\n  source: Results, Dysfunction of lateral entorhinal cortex dopamine activity, paragraph 2;\n    Fig. 4e; Supplementary Fig. 6c\n  quote: Dopamine was also decreased in APP-KI mice during Odor-1 at T1 in correct sessions\n  statistics:\n  - about: Odor-1, strain x time\n    test: two-way ANOVA\n    statistic: F(4,80) = 3.72\n    p: 7.8e-3\n    n: 10 WT and 8 APP-KI hemispheres\n  - about: Odor-1, T1\n    test: two-sided Tukey post hoc test\n    p: 4.8e-3\n  - about: Odor-2, strain x time\n    test: two-way ANOVA\n    statistic: F(4,80) = 2.1\n    p: 0.093\n  criterion: As fig4d-app-odor1-dopamine-decreased on correct sessions only. Reproduced when,\n    under G1, the Odor-1 interaction and the T1 Tukey comparison have p < 0.05 with WT higher.\n- id: fig4f-error-sessions-no-difference\n  statement: In error sessions, dopamine activity does not differ between young WT and young\n    APP-KI mice.\n  source: Results, Dysfunction of lateral entorhinal cortex dopamine activity, paragraph 2;\n    Fig. 4f\n  quote: No difference was observed in error sessions\n  statistics:\n  - test: two-way ANOVA\n    p: 0.05\n    p_relation: \">\"\n    n: 10 WT and 8 APP-KI hemispheres\n  criterion: A claim of absence, on the paper's test. As fig4d-app-odor1-dopamine-decreased on\n    error sessions, window G1, for each odor type. Reproduced when no strain effect or strain by\n    time interaction has p < 0.05. Supplementary Table 1 reports strain effects at p = 0.047\n    (Odor-1) and 0.0061 (Odor-2) for these data, against the legend's \"NS\"; the result is\n    reported against both.\n- id: figs7-odor1-specific-decrease\n  statement: The WT minus APP-KI dopamine difference at T1 is larger for Odor-1 than for Odor-A or\n    Odor-B.\n  source: Results, Dysfunction of lateral entorhinal cortex dopamine activity, paragraph 2;\n    Supplementary Fig. 7a\n  quote: The difference for Odor-1 was significantly larger than that for Odor-A or Odor-B,\n    suggesting specific decrease of dopamine for Odor-1\n  statistics:\n  - about: group effect at T1, all sessions\n    test: one-way ANOVA\n    statistic: F(3,28) = 3.98\n    p: 0.017\n    n: 8 young WT and 8 young APP-KI mice\n  - about: Odor-A against Odor-1\n    test: two-sided Tukey post hoc test\n    p: 0.042\n  - about: Odor-B against Odor-1\n    test: two-sided Tukey post hoc test\n    p: 0.041\n  criterion: How a WT minus APP-KI difference is formed per unit is not given (F(3,28) implies 8\n    values per odor). Readings (a) the 8 APP-KI hemispheres each subtracted from the WT mean,\n    (b) WT and APP-KI units paired by rank order. Window G1. One-way ANOVA over the four odors at\n    T1, Tukey post hoc. Reproduced when, under one reading, Odor-1 exceeds Odor-A and Odor-B with\n    Tukey p < 0.05.\n- id: figs6d-dopamine-behavior-correlation\n  statement: In APP-KI mice, the trial at which Odor-1 dopamine signals emerge correlates with the\n    trial at which licking to Odor-1 is learned.\n  source: Results, Dysfunction of lateral entorhinal cortex dopamine activity, paragraph 2;\n    Supplementary Fig. 6d\n  quote: The delayed emergence of Odor-1 dopamine signals correlated well with slow learning of\n    licking to Odor-1 in APP-KI mice\n  statistics:\n  - test: two-sided Pearson correlation\n    statistic: r(19) = 0.7810\n    p: 2.5e-5\n    n: 21 sessions from 8 young APP-KI mice\n  expected:\n    quantity: Pearson r\n    value: 0.78\n    tolerance: 0.078\n  criterion: Per session (Supplementary Fig. 6d), the trial after which five consecutive Odor-1\n    hits start, against the trial after which five consecutive Odor-1 trials have GCaMP signal\n    above 3 SD; sessions without such a run are dropped. What the 3 SD is taken from is open,\n    with readings (a) the SD of the precue baseline, (b) the SD of the session's signal; the\n    window is G1. Reproduced when, under one reading, r is within tolerance and p < 0.05.\n- id: fig1d-young-new-association-impaired\n  statement: Young APP-KI mice perform worse than young WT mice on novel odor associations at T5\n    (78.6% against 90.6% correct).\n  source: Results, Impaired associative memory formation in amyloid precursor protein knock-in\n    mice, paragraph 2; Fig. 1c, 1d\n  quote: Young WT mice performed at 90.6 ± 0.9% in T5, whereas young APP-KI performed at 78.6 ±\n    2.1%\n  statistics:\n  - about: odor x strain\n    test: two-way ANOVA\n    statistic: F(1,50) = 20.2\n    p: 4.1e-5\n    n: 11 young WT and 16 young APP-KI mice\n  - about: odor 1/2, WT against APP-KI\n    test: two-sided Tukey post hoc test\n    p: 3.1e-8\n  expected:\n  - quantity: young WT percent correct, Odor-1/2, T5\n    value: 90.6\n    tolerance: 0.9\n    unit: percent\n  - quantity: young APP-KI percent correct, Odor-1/2, T5\n    value: 78.6\n    tolerance: 2.1\n    unit: percent\n  criterion: Behavioral performance as in Shared method (readings B1, B2), per mouse means over\n    all sessions; two-way ANOVA odor pair (A/B, 1/2) by strain on the 54 values, Tukey post hoc.\n    Reproduced when, under one reading, both means are within tolerance (the s.e.m.), the\n    interaction has p < 0.05 and the 1/2 Tukey comparison has p < 0.05; partially when the tests\n    hold and the means do not.\n- id: fig1d-prelearned-retrieval-intact\n  statement: Young and old APP-KI mice retrieve the prelearned Odor-A/B association as well as WT\n    mice.\n  source: Results, Impaired associative memory formation in amyloid precursor protein knock-in\n    mice, paragraph 2; Fig. 1d, 1g\n  quote: both young and old APP-KI mice showed intact performance for retrieving prelearned\n    associative memories\n  statistics:\n  - about: young, A/B, WT against APP-KI\n    test: post hoc Tukey test\n    p: 0.92\n  - about: old, A/B, WT against APP-KI\n    test: post hoc Tukey test\n    p: 0.61\n  depends_on:\n  - fig1d-young-new-association-impaired\n  criterion: A claim of absence, on the paper's test. The Tukey comparison of A/B WT against A/B\n    APP-KI in the ANOVAs of fig1d-young-new-association-impaired and fig1g-old-new-association-impaired.\n    Reproduced when p >= 0.05 at both ages; the differences are reported.\n- id: fig1e-young-correct-sessions\n  statement: Young WT mice learn the new association in 77.5% of sessions, young APP-KI mice in\n    59.1%.\n  source: Results, Impaired associative memory formation in amyloid precursor protein knock-in\n    mice, paragraph 2; Fig. 1e\n  quote: Young WT mice had correct sessions at 77.5 ± 6.1% among all tested sessions, whereas\n    young APP-KI mice had correct sessions at 59.1 ± 5.5%\n  statistics:\n  - test: two-sided unpaired t-test\n    statistic: t(25) = 2.19\n    p: 0.037\n    n: 11 young WT and 16 young APP-KI mice\n  expected:\n  - quantity: young WT correct sessions\n    value: 77.5\n    tolerance: 6.1\n    unit: percent\n  - quantity: young APP-KI correct sessions\n    value: 59.1\n    tolerance: 5.5\n    unit: percent\n  criterion: Per mouse percentage of correct sessions (Odor-1/2 T5 performance above 80%, and\n    at or above 80% as the variant, readings B1 and B2); unpaired t-test across mice. Reproduced\n    when, under one reading, both means are within tolerance and p < 0.05.\n- id: fig1g-old-new-association-impaired\n  statement: Old APP-KI mice are further impaired on novel associations compared with old WT mice\n    (67.9% against 84.9% correct at T5).\n  source: Results, Impaired associative memory formation in amyloid precursor protein knock-in\n    mice, paragraph 3; Fig. 1f, 1g\n  quote: 84.9 ± 1.8% correct trials for old WT mice versus 67.9 ± 2.0% for old APP-KI mice\n  statistics:\n  - about: odor x strain\n    test: two-way ANOVA\n    statistic: F(1,46) = 41.4\n    p: 6.4e-8\n    n: 11 old WT and 14 old APP-KI mice\n  - about: odor 1/2, WT against APP-KI\n    test: post hoc Tukey test\n    p: 2.7e-9\n  expected:\n  - quantity: old WT percent correct, Odor-1/2, T5\n    value: 84.9\n    tolerance: 1.8\n    unit: percent\n  - quantity: old APP-KI percent correct, Odor-1/2, T5\n    value: 67.9\n    tolerance: 2.0\n    unit: percent\n  criterion: As fig1d-young-new-association-impaired, for old mice.\n- id: fig1h-old-correct-sessions\n  statement: Old WT mice learn the new association in 81.3% of sessions, old APP-KI mice in 47.3%.\n  source: Results, Impaired associative memory formation in amyloid precursor protein knock-in\n    mice, paragraph 3; Fig. 1h\n  quote: Old WT mice correctly learned 81.3 ± 6.4% of all sessions, whereas APP-KI correctly\n    learned 47.3 ± 6.5%\n  statistics:\n  - test: two-sided unpaired t-test\n    statistic: t(23) = 3.65\n    p: 1.3e-3\n    n: 11 old WT and 14 old APP-KI mice\n  expected:\n  - quantity: old WT correct sessions\n    value: 81.3\n    tolerance: 6.4\n    unit: percent\n  - quantity: old APP-KI correct sessions\n    value: 47.3\n    tolerance: 6.5\n    unit: percent\n  criterion: As fig1e-young-correct-sessions, for old mice.\n- id: figs1c-old-wt-decline\n  statement: Old WT mice show a slight decline of novel association performance compared with\n    young WT mice.\n  source: Results, Impaired associative memory formation in amyloid precursor protein knock-in\n    mice, paragraph 3; Supplementary Fig. 1c\n  quote: Notably, old WT mice showed a slight decline of associative memory compared to young WT\n    mice\n  statistics:\n  - about: odor x age\n    test: two-way ANOVA\n    statistic: F(1,40) = 5.04 (the Results print 30.1)\n    p: 0.031\n    n: 11 young WT and 11 old WT mice\n  - about: odor 1/2, young against old\n    test: post hoc Tukey test\n    p: 0.038\n  criterion: As fig1d-young-new-association-impaired with age in place of strain, WT mice only.\n    Reproduced when the 1/2 performance is lower in old WT with Tukey p < 0.05.\n- id: figs1f-prelearning-duration-similar\n  statement: APP-KI and WT mice need comparable numbers of days to reach criterion in the\n    prelearning (Odor-A/B) sessions.\n  source: Results, Impaired associative memory formation in amyloid precursor protein knock-in\n    mice, paragraph 3; Supplementary Fig. 1f\n  quote: APP-KI and WT mice showed comparable duration for the training with prelearning sessions\n    using Odor-A and Odor-B\n  statistics:\n  - about: strain x age\n    test: two-way ANOVA\n    statistic: F(1,48) = 2.2e-3\n    p: 0.96\n    n: 11 young WT, 16 young APP-KI, 11 old WT, 14 old APP-KI mice\n  - about: young APP-KI against young WT\n    test: post hoc Tukey test\n    p: 0.93\n  - about: old APP-KI against old WT\n    test: post hoc Tukey test\n    p: 0.99\n  criterion: A claim of absence, on the paper's test. Days of prelearning to reach 80% per\n    mouse; two-way ANOVA strain by age, Tukey post hoc. Reproduced when neither Tukey comparison\n    within age has p < 0.05 and the interaction has p >= 0.05.\n- id: fig5c-optogenetic-rescue\n  statement: Optogenetic stimulation of LEC dopamine fibers during Odor-1 trials improves young\n    APP-KI mice's novel association performance at T5 (95.2% against 77.9% in control\n    sessions).\n  source: Results, Rescued memory by dopamine reactivation, paragraph 1; Fig. 5b, 5c\n  quote: 'stimulation: 95.2 ± 1.6% versus control: 77.9 ± 4.9% at T5'\n  statistics:\n  - about: odor x stimulation\n    test: two-way ANOVA\n    statistic: F(1,40) = 4.17\n    p: 0.045\n    n: 11 young APP-KI mice\n  - about: odor 1/2, control against stimulation\n    test: post hoc Tukey test\n    p: 0.024\n  expected:\n  - quantity: percent correct, Odor-1/2, T5, stimulation sessions\n    value: 95.2\n    tolerance: 1.6\n    unit: percent\n  - quantity: percent correct, Odor-1/2, T5, control sessions\n    value: 77.9\n    tolerance: 4.9\n    unit: percent\n  criterion: As fig1d-young-new-association-impaired with session type (control, stimulation) in\n    place of strain, per mouse means over sessions of each type. The interaction p is 0.045 in\n    the text and 0.047 in the legend and Supplementary Table 1. Reproduced when, under one\n    reading, both means are within tolerance and the 1/2 Tukey comparison has p < 0.05.\n- id: fig5d-optogenetic-correct-sessions\n  statement: The percentage of correct sessions rises with stimulation (86.9% against 50.1%).\n  source: Results, Rescued memory by dopamine reactivation, paragraph 1; Fig. 5d\n  quote: The percentage of total correct sessions significantly increased with stimulation\n  statistics:\n  - test: two-sided unpaired t-test\n    statistic: t(20) = -2.55\n    p: 0.019\n    n: 11 young APP-KI mice\n  expected:\n  - quantity: correct sessions with stimulation\n    value: 86.9\n    tolerance: 8.2\n    unit: percent\n  - quantity: correct sessions in control\n    value: 50.1\n    tolerance: 11.4\n    unit: percent\n  criterion: As fig1e-young-correct-sessions, stimulation against control sessions per mouse, with\n    the paper's unpaired t-test (a paired test is shown as a variant).\n- id: figs9a-all-odor-stimulation-no-rescue\n  statement: Stimulating LEC dopamine fibers during all four odor types does not rescue\n    associative learning in young APP-KI mice.\n  source: Results, Rescued memory by dopamine reactivation, paragraph 1; Supplementary Fig. 9a\n  quote: No rescuing effect was observed when dopamine axons were stimulated during all four odor\n    types\n  statistics:\n  - test: two-way ANOVA (odor x stimulation)\n    statistic: F(1,16) = 0.55\n    p: 0.47\n    n: 5 young APP-KI mice\n  criterion: A claim of absence, on the paper's test. As fig5c-optogenetic-rescue for the\n    all-odor stimulation mice. Reproduced when the interaction has p >= 0.05.\n- id: fig6b-ldopa-rescue\n  statement: L-DOPA restores young APP-KI mice's novel association performance at T5 (82.6%\n    against 67.1% with saline).\n  source: Results, Rescued memory by dopamine reactivation, paragraph 2; Fig. 6a, 6b\n  quote: L- DOPA groups 82.6 ± 1.7% versus saline group 67.1 ± 4.2% at T5\n  statistics:\n  - about: odor x drug\n    test: two-way ANOVA\n    statistic: F(1,30) = 5.2 (3.6 in the legend and Supplementary Table 1)\n    p: 0.029\n    n: 9 L-DOPA and 8 saline mice\n  - about: odor 1/2, saline against L-DOPA\n    test: post hoc Tukey test\n    p: 1.1e-3\n  expected:\n  - quantity: percent correct, Odor-1/2, T5, L-DOPA\n    value: 82.6\n    tolerance: 1.7\n    unit: percent\n  - quantity: percent correct, Odor-1/2, T5, saline\n    value: 67.1\n    tolerance: 4.2\n    unit: percent\n  criterion: As fig1d-young-new-association-impaired with drug in place of strain, over the 5\n    injection days. Reproduced when, under one reading, both means are within tolerance and the\n    1/2 Tukey comparison has p < 0.05.\n- id: fig6c-ldopa-correct-sessions\n  statement: L-DOPA raises the percentage of correct sessions in young APP-KI mice (78.5% against\n    33.1%).\n  source: Results, Rescued memory by dopamine reactivation, paragraph 2; Fig. 6c\n  quote: The percentage of total correct sessions significantly increased with L- DOPA treatment\n  statistics:\n  - test: two-sided unpaired t-test\n    statistic: t(15) = -4.25\n    p: 7.0e-4\n    n: 9 L-DOPA and 8 saline mice\n  expected:\n  - quantity: correct sessions, L-DOPA\n    value: 78.5\n    tolerance: 5.6\n    unit: percent\n  - quantity: correct sessions, saline\n    value: 33.1\n    tolerance: 9.4\n    unit: percent\n  criterion: As fig1e-young-correct-sessions, L-DOPA against saline mice.\n- id: fig6h-ldopa-restores-a1-similarity\n  statement: In L-DOPA treated APP-KI mice, Odor-A and Odor-1 trajectories become close and the\n    SI is above 0 from T1c to T5, while saline-treated APP-KI mice keep them separated with\n    negative SI.\n  source: Results, Rescued memory by dopamine reactivation, paragraph 3; Fig. 6e to 6h\n  quote: Saline-injected APP-KI mice showed separated trajectories for prelearned rewarded Odor-A\n    and novel rewarded Odor-1 (Fig. 6e,g ), resulting in negative SI values ... As a result, SI\n    values were above 0 from trials 7–9 (T1c) to T5\n  expected:\n  - quantity: L-DOPA cells\n    value: 144\n    tolerance: 14\n  - quantity: saline cells\n    value: 132\n    tolerance: 13\n  - quantity: saline shuffle 95th percentile, T1\n    value: 0.73\n    tolerance: 0.073\n  - quantity: L-DOPA shuffle 95th percentile, T1\n    value: 0.98\n    tolerance: 0.098\n  criterion: PCA, shuffle and SI as in fig2g-wt-a1-generalized on the L-DOPA and saline principal\n    cells. Reproduced when, under one combination of readings, the L-DOPA A-1 SI is above 0 at\n    T1c, T2, T3, T4 and T5 (at least four of five) and the saline SI is below 0 at T2 to T5 (at\n    least three of four).\n- id: fig6i-ldopa-si-bootstrap\n  statement: Bootstrapped A-1 similarity is higher with L-DOPA than with saline from T1c to T4.\n  source: Fig. 6i; Supplementary Table 1\n  quote: The subtraction confirms higher similarity in the representations between Odor-A and\n    Odor-1 in L -dopa treatment compared to that in saline control\n  statistics:\n  - about: T1c\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 9.1e-5\n  - about: T2\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 4.8e-3\n  - about: T3\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 0.011\n  - about: T4\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 0.041\n  - about: T5\n    test: two-sided bootstrapping test, 1000 bootstraps\n    p: 0.12\n  depends_on:\n  - fig6h-ldopa-restores-a1-similarity\n  criterion: As fig2i-si-wt-above-app, L-DOPA minus saline. Reproduced when, under one\n    combination of readings, the difference is positive with p < 0.05 at T1c, T2, T3 and T4\n    (at least three of the four).\n- id: fig6k-ps19-ldopa-rescue\n  statement: L-DOPA also rescues novel association performance in young PS19 tau model mice\n    (84.8% against 64.8% with saline).\n  source: Results, Rescued memory by dopamine reactivation, paragraph 3; Fig. 6j to 6l;\n    Supplementary Fig. 10\n  quote: L -DOPA groups 84.8 ± 3.8% versus saline group 64.8 ± 4.6% at T5\n  statistics:\n  - about: odor x drug\n    test: two-way ANOVA\n    statistic: F(1,16) = 10.99 (printed F2,16 = 10.9 in the Results)\n    p: 4.4e-3\n    n: 5 L-DOPA and 5 saline PS19 mice\n  - about: odor 1/2, saline against L-DOPA\n    test: post hoc Tukey test\n    p: 4.7e-3\n  expected:\n  - quantity: percent correct, Odor-1/2, T5, L-DOPA PS19\n    value: 84.8\n    tolerance: 3.8\n    unit: percent\n  - quantity: percent correct, Odor-1/2, T5, saline PS19\n    value: 64.8\n    tolerance: 4.6\n    unit: percent\n  criterion: As fig6b-ldopa-rescue for PS19 mice.\n- id: figs11-wt-ldopa-no-effect\n  statement: L-DOPA has no effect on the associative learning of control WT mice.\n  source: Results, Rescued memory by dopamine reactivation, paragraph 3; Supplementary Fig. 11\n  quote: No effect was observed in L -DOPA-treated control WT mice\n  statistics:\n  - test: two-way ANOVA (odor x drug)\n    statistic: F(1,4) = 0.011\n    p: 0.91\n    n: 4 L-DOPA and 4 saline WT mice\n  criterion: A claim of absence, on the paper's test. As fig6b-ldopa-rescue for WT mice.\n    Reproduced when the interaction has p >= 0.05.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001968/10.1038-s41593-026-02260-w.yaml paper/10.1038-s41593-026-02260-w.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes: 42 claims, 40 quotes, 79 statistical values, 0 problems. Last check is for style rules (em dashes, "rather").

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/001968/*.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/001968/10.1038-s41593-026-02260-w.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
42 40 36 42 19
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
?? claims/001968/
?? scripts
```

**Agent**

I wrote `claims/001968/10.1038-s41593-026-02260-w.yaml`. The quote checker passes on it with 0 problems, and nothing is committed.

**Text read**
- **Paper:** the version of record (open access) as served by Europe PMC (PMC13246448), including the main text, figure legends, Methods and the Extended Data Fig. 1–10 legends.
- **Supplement:** Supplementary Figs. 1–11 and Tables 1–4. Table 1 (the statistics) is garbled in the text, so I read its pages 14–18 from the supplement PDF.
- **Not available:** the main article PDF wasn't supplied, so I never saw the figures, and numbers shown only in figure panels aren't in the file. The reporting summary and source data weren't supplied either.
- **Ref. 16:** the Methods describe behavior scoring, PCA, the shuffle, the similarity index (SI), the bootstrap and photometry as "previously described" in their ref. 16 (Lee et al. 2021, Nature). I read that paper's Methods for those steps only. It settles the PCA bins (50 ms over −1 to 4 s), the per-neuron min-max scaling, a separate PCA per timepoint, the photometry normalization and the T5 trial range.
- **Code:** the lab page the paper links holds only the 2021 place-cell protocol code (`analyze4LinearTracks.m`, `analyzePopulationVector.m`, `boxSpikeInfo3.m`) and has no version or commit. None of it covers this paper's analyses, so the code settles no method detail.

**Claims**
- 42 claims; 40 have quotes. The two without are the per-mouse Fig. 2k and Fig. 2l results, which carry an `inferred` note because no sentence states them.
- 36 have statistics (79 values checked against the text), all 42 have criteria, and 19 have expected values.
- They cover recorded unit counts, spike width and firing rates, cue-responsive cells, PCA distance, SI and bootstrap (young, early trials, old, L-DOPA), decoding, histology, photometry, behavior, optogenetics and L-DOPA (including the PS19 and WT controls).
- All use `data: dataset`. The dandiset's archive metadata points to tetrode electrophysiology only, so photometry, histology and behavior from other mice may be absent; that is for the author to find.

**Details the paper leaves open, with the readings named in the file**
- **Behavioral T5 (trials 121–160):** (B1) the trials of each odor pair that fall in session trials 121–160, or (B2) the last 40 trials of each pair.
- **Correct session:** above 80% (Methods) or at or above 80% (Results).
- **T2 and T4 for units:** never defined. Read as (T-a) 10-trial blocks midway between T1, T3 and T5, or (T-b) the whole second and fourth fifths of each odor's trials.
- **Cue response:** threshold p < 0.05 (Supplementary Table 1) or p < 0.01 (Results); increases only or any change; odor period only or odor, delay and choice periods. That gives eight combinations.
- **PCA scaling and smoothing:** (x − min)/max or (x − min)/(max − min); smoothed or raw binned rates.
- **Shuffle:** one permutation per session or one per cell.
- **SI's mean shuffle distance:** from the A-1 pair itself or averaged over all six pairs.
- **Bootstrap test:** a normal fit (the Results call it "maximum likelihood estimation") or an empirical fraction.
- **"Smaller or larger than the shuffle":** relative to the mean shuffle distance or to the 95th-percentile threshold.
- **Photometry window:** 1–4 s (Fig. 4d legend), 2–4 s (Supplementary Table 1), 0.5–3 s (ref. 16), or 2–3 s for "delay periods".
- **Decoding:** test window 1–4 s or 2–5 s; a sample is each 50 ms bin or the window mean.
- **Smaller ones:** the channel used for spike width, the definition of mean and peak firing rate, how the Supplementary Fig. 7 difference is formed, the baseline for the 3 SD rule, the family for the FDR correction in Fig. 2k, and whether "Odor-A cells" means A only or A among others.

**Where the paper contradicts itself (recorded in the claims)**
- **Statistics:** the Results print χ² = 2.29 for p = 3.6e-9, and F = 30.1 against 5.04 in the table for Supplementary Fig. 1c. The Fig. 6b ANOVA is F = 5.2 against 3.6. The PS19 test is printed as F(2,16) against F(1,16). The Fig. 5c interaction is p = 0.045 in the text and 0.047 in the legend and table.
- **Fig. 3b test:** rank sum in the text, signed-rank in the table.
- **Fig. 4f:** the legend says no significant difference, but the table shows strain effects of p = 0.047 and 0.0061.
- **Counts:** the L-DOPA group has 144 cells in the text but 132 in the table. Mouse #01517 has 97 or 99 cells. The WT L-DOPA group has 4 or 5 mice.

**Missing from the paper:** nothing the claims needed is absent apart from the figure panels themselves and task analysis code. The shuffle thresholds and bootstrap p-values come from Supplementary Table 1.

## End of run

44 turns, 10 minutes, result: success.
