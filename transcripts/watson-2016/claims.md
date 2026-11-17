# watson-2016 · claims · run 43677861926

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/Reader/,$p' | head -300; ls paper/ claims/ claims/watson-2016
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -40 paper/10.1016-j.neuron.2016.03.036.txt; grep -n -i "supplement\|^=\+\|^#" paper/10.1016-j.neuron.2016.03.036.txt | head -60; cat papers/datasets/watson-2016.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/watson-2016.yaml; cat claims/watson-2016/000041.yaml; echo ======; cat claims/watson-2016/crcns-fcx-1.yaml
```

```
<persisted-output>
Output too large (112.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8ad07bb3-73f4-48b6-949b-4741f0637a95/tool-results/bg5iw9g2i.txt

Preview (first 2KB):
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1016/j.neuron.2016.03.036
datasets:
- archive: dandi
  id: '000041'
  relation: primary
- archive: crcns
  id: fcx-1
  relation: primary
# Claims for Watson, Levenstein, Greene, Gelinas and Buzsaki (2016) on dandiset 000041.
# Source: the NIH author manuscript in PubMed Central (PMC4873379), full text of the main
# article, read from its Results, Experimental Procedures and figure legends. The Supplemental
# Experimental Procedures and the supplementary figures (NIHMS776601-supplement-1 and -2) could
# not be retrieved (PMC and the publisher answer with a browser check), and Table 1 is not in
# the manuscript text. Where the main text leaves a method open, the choice is fixed below.
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
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
grep -l "^  datasets:" claims/*.yaml | head; f=$(grep -l "^  datasets:" claims/*.yaml | head -1); sed -n 1,80p $f
```

```
claims/gao-2018.yaml
claims/kim-2022.yaml
claims/pakhomov-2023.yaml
claims/silkuniene-2025.yaml
claims/wirth-2017.yaml
# Claims for Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li (2018), "A
# cortico-cerebellar loop for motor planning", Nature 563, 113-116, doi:10.1038/s41586-018-0633-x,
# tested on DANDI:000007 and CRCNS:alm-4.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-14,
# protocol pilot-15 as stated in docs/protocol.md. It updates the file written 2026-11-10 under
# pilot-14 (and checked that day) for DANDI:000007 alone; ids are kept where the finding is the
# same, and the changes of that check are carried over.
#
# Text read: the version of record (PMC6212318, open access), Europe PMC JATS XML flattened, in
# paper/10.1038-s41586-018-0633-x.txt: main text, Methods, the legends of Extended Data Figs. 1 to
# 10, and the Supplementary Information (41586_2018_633_MOESM1_ESM.pdf, from the publisher; also
# paper/...supp1.pdf), whose text is appended: the Extended Data Fig. 10 discussion, the cerebellar
# circuitry discussion and Supplemental Table 1 (mice and hemispheres per experiment). supp2.pdf is
# the Nature reporting summary. The legends of the main Figs. 1 to 4 are not in the stored text,
# and there is no PDF of the main paper; values, significance marks and neuron counts given only in
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -v "^#" claims/gao-2018.yaml | sed -n 1,60p
```

```
127:schema_version: 2
128:paper: doi:10.1038/s41586-018-0633-x
129:claims:
130:- id: fig1d-fastigial-lesion-contra-choice
131:  statement: Fastigial nucleus lesions impair contralesional licking choices, measured as lower
132:    performance on trials instructing contralesional licking after the lesion than before.
133:  source: Main text, paragraph 4; Figure 1d
134:  quote: Fastigial lesions impaired initiation of contralesional licking ( Fig 1d )
135:  datasets:
136:  - "000007"
137:  - crcns-alm-4
138:  criterion: Performance as in B1 for contralesional and ipsilesional trials, before against
139:    after the lesion, in the 4 fastigial lesion mice (Supplemental Table 1). The main text gives
140:    no test and the Fig. 1 legend is not in the text read, so the one-sided bootstrap of B1 at p <
141:    0.05 is used (B1). Whether mice are pooled or tested one by one is open (readings (a) the
142:    hierarchical bootstrap of B1 over the 4 mice; (b) per mouse, the bootstrap over that mouse's
143:    sessions and trials). Reproduced when, under one reading, contralesional performance drops
144:    after the lesion at p < 0.05 (in every fastigial mouse, under reading (b)). The per-mouse
145:    drops are reported under both readings.
146:- id: fig1e-fastigial-lesion-slow-initiation
[... 40 more lines not kept]
```

**Agent**

Now the paper text. I'll read it in full.

**Agent calls Bash**

```bash
cd paper; fold -s -w 200 10.1016-j.neuron.2016.03.036.txt > $TMPDIR/w.txt; wc -l $TMPDIR/w.txt
```

```
1845 /tmp/claude-1001/w.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/w.txt",
 "limit": 700
}
```

```
File content (35127 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/w.txt",
 "limit": 450
}
```

```
File content (31507 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/w.txt",
 "limit": 200
}
```

```
1	DOI: 10.1016/j.neuron.2016.03.036
2	Version: as served by ncbi_pmc
3	Source: ncbi_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 2 supplement file(s) from PubMed Central, downloaded in a browser (PMC4873379), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	Neuron Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC4873379 PMC4873379.1 4873379 4873379 NIHMS776601 27133462 
8	10.1016/j.neuron.2016.03.036 NIHMS776601 NIHPA776601 1 Article Network homeostasis and state dynamics of neocortical sleep Watson Brendon O. 1 3 Levenstein Daniel 1 2 Greene J. Palmer 1 Gelinas 
9	Jennifer N. 1 Buzsáki György 1 2 1 New York University Neuroscience Institute, New York University, New York, NY 10016, USA 2 Center for Neural Science, New York University, New York, NY 10016, USA 3 
10	Department of Psychiatry, Weill Cornell Medical College, New York, NY 10065, USA Correspondence: [removed: an e-mail address] 28 4 2016 18 5 2016 90 4 269747 839 852 15 04 2016 18 05 2017 18 05 2017 30 
11	07 2016 05 06 2024 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Sleep exerts many effects on mammalian forebrain 
12	networks, including homeostatic effects on both synaptic strengths and firing rates. We used large-scale recordings to examine the activity of neurons in the frontal cortex of rats and firstly 
13	observed that the distribution of pyramidal cell firing rates was wide and strongly skewed towards high firing rates. Moreover, neurons from different parts of that distribution were differentially 
14	modulated by sleep sub-states. Periods of nonREM sleep reduced the activity of high firing rate neurons and tended to upregulate firing of slow firing neurons. By contrast, the effect of REM was to 

[... 186 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/w.txt",
 "offset": 200,
 "limit": 200
}
```

```
200	This suggests that the shifting levels of norepinephrine abd other subcortical neuromodulators that occurs across sleep substates can shift STDP rules from depression to potentiation. It should be 
201	emphasized that the rate decrease of fast firing neurons within nonREM packets is not a simple consequence of the increased incidence and duration of DOWN states. First, UP state incidence also 
202	increased. Second, slow firing rate neurons showed an opposite change in firing rate. Third, when firing rates were considered only in UP states, rate decrease of fast firing neurons from early to 
203	late nonREM packets was still present. In contrast, firing rates of putative interneurons during UP states increased from the early to the late nonREM packets of sleep ( Figure 4E ). This latter 
204	finding is a strong argument against the possibility that the pattern changes of faster firing putative excitatory neurons was due to any contamination by interneurons, which may be regulated by 
205	different mechanisms (Cohen et al.). REM sleep Despite within-REM firing rate increases, REM had a net persisting effect of downshifting firing rates of all neuron groups, a reflection of a mechanism 
206	involving proportional changes (i.e. division or multiplication) ( Figure 6 ). Longer REM episodes exerted proportionally larger downscaling effects. Similar to previous observations in the 
207	hippocampus ( Grosmark et al., 2012 ; Miyawaki and Diba, 2016 ), we found that WAKE and REM episodes exerted opposite effects on firing rates. Furthermore, whereas many minutes of waking activity is 
208	necessary for inducing lasting changes in firing rates during and after WAKE ( Tononi and Cirelli, 2003 , 2014 ), approximately a minute of REM had the same magnitude but opposite direction effect. 
209	This is of particular interest since WAKE and REM sleep are associated with seemingly similar network states. Whereas WAKE is strongly linked to elevated activity of cholinergic, seroton
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "supplement\|SUPPLEMENTAL\|Table 1\|^=\+\|---" $TMPDIR/w.txt | sed -n 1,80p | cut -c1-200
```

```
5:Extracted: as fetched; with 2 supplement file(s) from PubMed Central, downloaded in a browser (PMC4873379), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6:------------------------------------------------------------------------
19:pmc-prop-legally-suppressed no pmc-prop-has-pdf yes pmc-prop-has-supplement yes pmc-prop-pdf-only no pmc-prop-suppress-copyright no pmc-prop-is-real-version no pmc-prop-is-scanned-article no 
47:Table 1 ). Brain state segregation was performed by a heuristic automated approach and verified by independent visual classification ( Figure 1 A–D ; Figure S1C ). First, LFPs were converted into 
59:nonREM epochs are referred to here as nonREM ‘packets’, whereas a stream of nonREM packets and MAs without REM are called ‘nonREM episodes’ ( Figure 1A ; definitions in Table 1 ). We found that the
65:(details of detection algorithm in Supplemental Materials ). Within UP states, we were able to characterize the evolution of LFP ( Figure 1E , upper part) as well as spiking metrics, including rate
68:clustering of single units and separation of principal neurons from interneurons have been described in detail previously ( Supplementary Material ). Neurons that did not meet the strict criteria f
69:clean clusters and recording stability ( Schmitzer-Torbert et al., 2005 ) were discarded. Sessions without full WAKE-SLEEP cycles ( Supplementary Materials ) were also discarded. This resulted in 9
130:ratio negative correlation versus time p < 0.05). The fraction of epochs identified as neither UP nor DOWN (see Supplementary Methods ) increased over packets (R = – 0.04, p < 10 −3 ). The inciden
255:interneurons ( Supplemental Methods ). Sleep scoring was performed by an automated algorithm and supervised manually, using LFP derivatives and EMG signals to segregate WAKE, nonREM, REM and 
259:analyses are available in Supplemental Experimental Procedures . Supplementary Material 1 2 This is a PDF file of an unedited manuscript tha
[... 37 more lines not kept]
```

**Agent**

The full text includes both supplements (Supplemental Experimental Procedures, Table 1, Figures S1 to S5). Reading them now.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/w.txt",
 "offset": 535,
 "limit": 330
}
```

```
535	[71] Sleep drives metabolite clearance from the adult brain. Science. 2013. 10.1126/science.1241224
536	
537	##### Supplement: NIHMS776601-supplement-1.pdf
538	
539	=== page 1 ===
540	 
541	1 
542	SUPPLEMENTAL INFORMATION 
543	Network homeostasis and state dynamics of neocortical sleep 
544	 
545	Brendon O. Watson1, 3, Daniel Levenstein1,2, J. Palmer Greene1, Jennifer N. Gelinas1 and 
546	György Buzsáki1, 2 
547	 
548	 
549	 
550	 
551	 
552	 
553	 
554	 
[... 310 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/w.txt",
 "offset": 865,
 "limit": 500
}
```

```
865	120
866	-50
867	-30
868	-10
869	10
870	30
871	50
872	0
873	0.2
874	0.4
875	0.6
876	0.8
877	1
878	Autocorrelograms
879	Normalized amplitude
880	ms
881	0.5 0.25
882	0
883	0.25 0.5 0.75
884	-1
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/w.txt",
 "offset": 1365,
 "limit": 480
}
```

```
1365	for the separation of MA and WAKE is justified by a plateau in the proportion of 
1366	movement in epochs > 40-s.  Shorter epochs (with less movement) are defined as 
1367	microarousal. 
1368	 
1369	
1370	=== page 9 ===
1371	 
1372	3 
1373	Figure S2, related to Figure 2. Units: classification and firing patterns 
1374	(A) Separation of putative excitatory cells (pE) and putative inhibitory ccells (pI) by 
1375	waveform features and physiological interactions. Neurons were clustered according to 
1376	trough-to-peak time and spike width of the wide band-recorded waveforms (20 kHz 
1377	sampled, detrended waveforms; Sirota et al., 2008; Stark et al., 2014). Also shown are the 
1378	firing rates (although rate was not used for clustering). Each symbol corresponds to an 
1379	isolated unit. pE and pI neurons form separate clusters.  Separatrix (black) is based on 
1380	optogenetically tagged cells in hippocampal data (Stark et al., 2014). Additional support 
1381	for classification was based on monosynaptic timescale interactions between pairs of 
1382	units (right column).  Units preceding an increase in firing by another unit at 1-4 ms 
1383	delay (example upper right t0 = firing time of cell under examination) were considered 
1384	excitatory and therefore pE cells (dark green dots in 3-D plot).  Units preceding a drop in 
[... 460 more lines not kept]
```

**Agent**

Both supplements are present (supp2 is the graphical abstract). Now the prior claims files.

**Agent calls Bash**

```bash
cd ..; wc -l claims/watson-2016/*.yaml; grep -n "^- id:\|^  - id:" claims/watson-2016/*.yaml
```

```
791 claims/watson-2016/000041.yaml
  1182 claims/watson-2016/crcns-fcx-1.yaml
  1973 total
claims/watson-2016/000041.yaml:57:- id: dataset-composition
claims/watson-2016/000041.yaml:87:- id: fig2a-median-rates
claims/watson-2016/000041.yaml:123:- id: fig2a-skewed-wide-distribution
claims/watson-2016/000041.yaml:134:- id: fig2a-fraction-above-2hz
claims/watson-2016/000041.yaml:161:- id: fig2b-wake-nrem-slope
claims/watson-2016/000041.yaml:193:- id: fig2-burst-index-by-state
claims/watson-2016/000041.yaml:224:- id: fig2c-acg-peaks
claims/watson-2016/000041.yaml:238:- id: fig2c-acg-decay
claims/watson-2016/000041.yaml:249:- id: fig2f-rate-group-correlations
claims/watson-2016/000041.yaml:262:- id: ma-statistics
claims/watson-2016/000041.yaml:287:- id: ma-fraction-over-nrem-episodes
claims/watson-2016/000041.yaml:306:- id: packet-duration
claims/watson-2016/000041.yaml:319:- id: wake-sleep-cycles
claims/watson-2016/000041.yaml:336:- id: fig3b-population-decline
claims/watson-2016/000041.yaml:358:- id: fig3-first-last-packet
claims/watson-2016/000041.yaml:384:- id: fig3d-first-last-slope
claims/watson-2016/000041.yaml:410:- id: fig3e-wake-before-after
[... 63 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/watson-2016/crcns-fcx-1.yaml"
}
```

```
1	# Claims for Watson, Levenstein, Greene, Gelinas & Buzsaki (2016), Neuron 90, 839-852, "Network
2	# homeostasis and state dynamics of neocortical sleep", doi:10.1016/j.neuron.2016.03.036, on CRCNS
3	# data set fcx-1 (doi:10.6080/K02N506Q).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
6	#
7	# Text read: the accepted author manuscript in PubMed Central (PMC4873379, NIHMS776601), as supplied
8	# under paper/: Introduction, Results, Discussion, Experimental Procedures, and the legends of
9	# Figures 1 to 6; with its supplement 1 (Table S1, legends of Figures S1 to S5, Supplemental
10	# Experimental Procedures, and the figure pages as extracted text) and supplement 2 (the Figure 1
11	# artwork as extracted text). The version of record was not read. No PDF of the main paper was
12	# supplied and the supplement PDF could not be rendered in this run, so values printed only inside
13	# Figures 2 to 5 (the per-sextile R and p of Fig. 3B and 4A-B iv, the n of each triplet class and
14	# the asterisks of Fig. 5B) were not read; claims on those figures rest on the Results and legends.
15	# The per-sextile R and p of Figure S5A and S5B and the R and p of Figure S3C and S5C to S5G come
16	# from the extracted text of the supplement figure pages; the S5C to S5G values carry their panel
17	# titles; the assignment of the two S5A/S5B lists to WAKE and REM is read from the extraction order
18	# and agrees with the Results for REM only.
19	#
20	# Code. The paper links no analysis code. Its methods name MATLAB, KlustaKwik, Klusters, the
[... 862 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/watson-2016/crcns-fcx-1.yaml",
 "offset": 883,
 "limit": 300
}
```

```
883	    per session; R = - 0.29, p<10 −10 ). A positive correlation was observed between firing rate of
884	    the top sextile group and UP state duration (R = 0.14, p < 10 −3 ) and gamma power ( Figure 4D ;
885	    R = 0.44; p < 10 −10 ). Finally, a positive correlation was found between normalized firing rates
886	    per packet in the bottom sextile group and sigma power in the last 20 sec of the packet (R =
887	    0.25; p < 10 −10 ). Other tested relationship combinations were not significant
888	  statistics:
889	  - about: top sextile rate against delta power
890	    statistic: R = -0.28
891	    p: 1.0e-10
892	    p_relation: "<"
893	  - about: top sextile rate against DOWN duration
894	    statistic: R = -0.16
895	    p: 0.0001
896	    p_relation: "<"
897	  - about: top sextile rate against DOWN incidence
898	    statistic: R = -0.29
899	    p: 1.0e-10
900	    p_relation: "<"
901	  - about: top sextile rate against UP duration
902	    statistic: R = 0.14
[... 280 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/watson-2016/000041.yaml",
 "limit": 340
}
```

```
1	# Claims for Watson, Levenstein, Greene, Gelinas and Buzsaki (2016) on dandiset 000041.
2	# Source: the NIH author manuscript in PubMed Central (PMC4873379), full text of the main
3	# article, read from its Results, Experimental Procedures and figure legends. The Supplemental
4	# Experimental Procedures and the supplementary figures (NIHMS776601-supplement-1 and -2) could
5	# not be retrieved (PMC and the publisher answer with a browser check), and Table 1 is not in
6	# the manuscript text. Where the main text leaves a method open, the choice is fixed below.
7	# Quotes and statistics added 2026-10-19 from the full text (PMC4873379, NCBI PMC JATS XML via
8	# E-utilities; Europe PMC returned an error).
9	#
10	# When these criteria were written, the author had seen the data check only: the file list and
11	# dandiset metadata; for every file the subject, session, scalar metadata, unit counts by
12	# cell_type and region, spike-time ranges, the number and total duration of each state label,
13	# LFP shape, rate and chunking, electrode columns; the first 40 rows of the state table in two
14	# sessions; and the spike times of Dino-072114, which are whole seconds divided by 20000. No
15	# claim's analysis had been run. The paper links no analysis code; the NWB conversion code
16	# (catalystneuro/buzsaki-lab-to-nwb at commit 5f6a375) was read.
17	#
18	# Method choices fixed here, before the analysis:
19	# - Sessions. The 21 files whose spike times are usable; Dino-072114 is left out (see the data
20	#   check). Each session's units are treated as distinct cells, as the paper counts cells per
[... 320 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/watson-2016/000041.yaml",
 "offset": 340,
 "limit": 452
}
```

```
340	  quote: the arithmetic mean of the population firing rates of pE cells declined over the course of
341	    sleep using a test of correlation of spike rate versus time (Figure 3A–B; R = – 0.11
342	  statistics:
343	  - statistic: R = -0.11
344	    p: 0.001
345	    p_relation: "<"
346	  depends_on:
347	  - wake-sleep-cycles
348	  expected:
349	    quantity: Pearson R, population rate against normalized SLEEP time
350	    value: -0.11
351	    tolerance: 0.011
352	  criterion: Over the SLEEP periods of WAKE-SLEEP cycles. Readings (a) one point per nonREM
353	    packet at the normalized time of its midpoint, its population mean rate divided by the
354	    mean of these values over the period's packets; (b) 10 bins of normalized SLEEP time,
355	    Non-REM time only, bins with under 10 s of Non-REM dropped, normalized the same way.
356	    Reproduced when under one reading R is within tolerance and p < 1e-3; partially
357	    reproduced when R is negative with p < 1e-3 but outside tolerance.
358	- id: fig3-first-last-packet
359	  statement: The mean pE rate is lower in the last than in the first nonREM packet of SLEEP
[... 432 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rl "000041" --include=*.yaml --include=*.md --include=*.json . 2>/dev/null | grep -v "^./claims/watson-2016/" | head; sed -n 1,80p paper/fcx-1.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Text is complete (main, Methods, supplement). Fetching only the DANDI title and description for 000041.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000041/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['draft_version']['name']);print(d.get('most_recent_published_version'))"; curl -s https://api.dandiarchive.org/api/dandisets/000041/versions/draft/info/ | python3 -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m.get('description'));print(m.get('name'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2016.03.036.supp1.pdf')
print(len(d))
for i in [4,6]:
    d[i].get_pixmap(dpi=110).save(f'p{i+1}.png')
" && ls; python3 -c "
from scipy import stats
import numpy as np
def p(r,n): t=r*np.sqrt((n-2)/(1-r*r)); return 2*stats.t.sf(abs(t),n-2)
print(p(0.651633,50), p(0.267028,50), p(-0.19849,873), p(-0.14923,947), p(-0.39537,136))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm mutool; pdftoppm -f 7 -l 7 -r 100 -png paper/10.1016-j.neuron.2016.03.036.supp1.pdf s5 && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.03.036.supp1.pdf",
 "pages": "7"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --target $TMPDIR/py pymupdf scipy -q 2>&1 | tail -2; PYTHONPATH=$TMPDIR/py python3 -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2016.03.036.supp1.pdf')
for i in [4,6]:
    d[i].get_pixmap(dpi=110).save(f'p{i+1}.png')
from scipy import stats
import numpy as np
def p(r,n): t=r*np.sqrt((n-2)/(1-r*r)); return 2*stats.t.sf(abs(t),n-2)
print(p(0.651633,50), p(0.267028,50), p(-0.19849,873), p(-0.14923,947), p(-0.39537,136))
"; ls
```

Result: not kept, because it reads the paper's text.

**Agent**

The implied counts check out (50 bins; ~873 packets; ~947 and 136 cells). Looking at Figure S5 to settle which R list belongs to WAKE.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p7.png"
}
```

Result: no output.

**Agent**

I have everything needed. Writing the combined claims file now, built on the full-text reading (crcns file) with ids from both prior files, splitting combined claims where one file had them separate.

**Agent calls Write**

```json
{
 "file_path": "claims/watson-2016.yaml",
 "content": "# Claims for Watson, Levenstein, Greene, Gelinas & Buzsaki (2016), Neuron 90, 839-852, \"Network\n# homeostasis and state dynamics of neocortical sleep\", doi:10.1016/j.neuron.2016.03.036, tested on\n# DANDI:000041 and CRCNS:fcx-1.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-15,\n# protocol as stated in docs/protocol.md (Reader). It replaces the two per-dataset files\n# claims/watson-2016/000041.yaml and claims/watson-2016/crcns-fcx-1.yaml; ids are reused where the\n# finding is the same (see \"Ids\" below).\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC4873379, NIHMS776601), in\n# paper/10.1016-j.neuron.2016.03.036.txt: Introduction, Results, Discussion, Experimental Procedures,\n# the legends of Figures 1 to 6 and the Highlights; with supplement 1 (NIHMS776601-supplement-1:\n# Table S1, the legends of Figures S1 to S5, the Supplemental Experimental Procedures, and the figure\n# pages as extracted text) and supplement 2 (artwork of Figure 1 only, as extracted text). The version\n# of record was not read. There is no PDF of the main paper, so values printed only inside Figures 2\n# to 5 (the per-sextile R and p of Fig. 3B and 4A-B iv, the n of each triplet class and the asterisks\n# of Fig. 5B, the significance marks of Fig. 2F) were not read; claims on those figures rest on the\n# Results and legends. Page 7 of the supplement PDF (Figure S5) was rendered to read its panel titles\n# and printed R and p, which the text extraction separates from their panels.\n#\n# Code. The paper links no analysis code. Its methods name MATLAB, KlustaKwik, Klusters, the\n# process_multi_start shell script and a modification of FindRipples.m from FMAToolbox\n# (http://fmatoolbox.sourceforge.net/) for spindle detection. The CRCNS descriptor ships data readers\n# (LoadBinary_bw.m, TStoolbox.zip); these are not the paper's analysis code and were not read. Every\n# method below is from the paper's text, its legends or its supplement, or is named as open.\n#\n# The datasets, from their titles and descriptions on the archives.\n#  - 000041 (DANDI), titled as the paper. Its description: silicon probe recordings in the frontal\n#    cortices of male Long Evans rats, home cage, no task; LFP and spikes; 11 animals, 27 recording\n#    sessions, 1360 units, 1121 stable, 995 putative excitatory and 126 putative inhibitory; only\n#    recordings with a WAKE-SLEEP episode (7 min of wake followed by 20 min of sleep), about 2 per\n#    session.\n#  - crcns-fcx-1 (CRCNS, doi:10.6080/K02N506Q), \"Multi-unit spiking activity recorded from rat frontal\n#    cortex (brain regions mPFC, OFC, ACC, and M2) during wake-sleep episode ...\". Its descriptor\n#    (paper/fcx-1.data-description.txt, read for this alone) gives the same summary and names the\n#    paper as the source; one folder per session with LFP, spike trains and their classification,\n#    and the state intervals, as the paper's Table S1 defines them.\n#  Both describe the same 27 sessions, the paper's whole data set. Every claim on recorded data lists\n#  both; the author tests each claim on each dataset that holds what it needs.\n#\n# Data the paper used, as it reports them (Results; Experimental Procedures; Table S1; Supplemental\n# Experimental Procedures). Eleven male Long Evans rats, 3 to 7 months old, one or two 64-site\n# silicon probes in deep layers of frontal cortex (medial prefrontal, orbitofrontal, anterior\n# cingulate and secondary motor cortex; Table S1 gives the area, sessions and units per rat: BWRat17\n# to BWRat21, Dino, B22, Bogey, Splinter, Rizzo, Templeton), recorded in the home cage in the light\n# cycle; 27 sessions (294 +- 137 min). Wideband at 20 kHz; LFP at 1250 Hz; spikes sorted with\n# KlustaKwik and Klusters; 1360 clustered units, 1121 stable, 995 putative pyramidal (pE) and 126\n# putative interneurons (pI), classified by waveform and verified by monosynaptic interactions. EMG\n# from the correlation of 300 to 600 Hz signals across shanks; motion from video, accelerometer or\n# induction coil. States scored per second (Table S1, Supplemental Experimental Procedures, Brain\n# state scoring): nonREM (packets, 20+ s of uninterrupted nonREM), REM, microarousals (MA, < 40 s\n# between nonREM packets), nonREM episodes, REM episodes, WAKE (7+ min, interruptions < 2 min), SLEEP\n# (20+ min of nonREM, REM and MA with no interruption > 2 min), WAKE-SLEEP cycles (54). Detected\n# events, UP and DOWN states (43230 and 86839) and spindles (5203). LFP bands delta 0.5 to 4 Hz,\n# sigma 9 to 25 Hz, gamma 40 to 100 Hz; theta ratio 5-10 Hz over 2-16 Hz.\n#\n# Shared method details, used by the criteria below.\n# M1. Cells and sessions. Statistics are per cell on pE cells unless stated (Results, Assessment of\n#   firing patterns). Analyses are confined to WAKE-SLEEP cycles (Supplemental Experimental\n#   Procedures, Brain state scoring). A cell's rate in a state is its spike count over the summed\n#   duration of that state's intervals (a standard choice). The paper does not say whether a cell\n#   recorded across two WAKE-SLEEP cycles enters a per-episode comparison once per episode or once\n#   with its episodes averaged; readings (a) one entry per cell and episode, (b) one per cell,\n#   averaged over episodes.\n# M2. Sextiles. pE cells from the whole data set are split into six equal groups by WAKE firing\n#   rate (Results, Firing pattern and LFP changes across the course of sleep; Fig. 2A legend;\n#   Experimental Procedures), kept for all later analyses. \"General WAKE firing rate\" is read as the\n#   rate over all WAKE intervals of the cell's session; reading (b) is the rate over the WAKE of\n#   each cycle. The Fig. 2F groups are \"based on mean rate\"; readings the same WAKE sextiles, or\n#   sextiles of the nonREM rate. Sextile numbers differ between figures; Figure S2 numbers 1 as the\n#   lowest rate (1 pE Low FR, 6 pE High FR), the Figure S5 legend says sextile 1 is the highest.\n#   Criteria name sextiles by rate (top, bottom), or say which numbering they use.\n# M3. Time-normalized correlations. SLEEP, nonREM episodes and packets are time-normalized to 0 to 1\n#   and, for SLEEP, only nonREM time is used (Results, Firing pattern and LFP changes across the\n#   course of sleep; Fig. 3B legend). Correlations are Pearson (Fig. 3B legend). The unit of a sample\n#   in these correlations is not stated. Readings, (a) one point per nonREM packet (its mean value at\n#   its normalized mid-time); (b) one point per 10 s bin of nonREM (the bin the Supplemental\n#   Experimental Procedures use for the CV and burst ratio); (c) 50 equal bins of normalized time,\n#   values averaged over episodes per bin. Every R and p printed in Figure S5A and S5B equals a\n#   Pearson test on exactly 50 points (checked here, for example R = 0.651633 with n = 50 gives p =\n#   2.97e-07 as printed), so the paper used 50 bins there. The Figure S3C R and p (-0.19849,\n#   3.3168e-09) equal a Pearson test on about 873 points, about the number of nonREM packets in 54\n#   SLEEP periods, which agrees with reading (a) but does not settle it. Values are normalized by the\n#   recording's mean before pooling, as the Supplemental Experimental Procedures do for CV and burst\n#   ratio.\n# M4. Judging correlations and tests. Where the paper reports an R and a p bound, the claim is\n#   reproduced when R has the reported sign and p is below the reported bound under one reading,\n#   partially reproduced when the sign holds and p < 0.05 but not below the bound, and not\n#   reproduced otherwise; the R obtained is reported beside the paper's. Reported R values are test\n#   statistics whose size depends on the sampling unit the paper does not fix (M3), so they are not\n#   targets with a tolerance. Where the paper prints an exact p (Figures S3C, S5C to S5G), the bound\n#   is the next power of ten above it.\n# M5. Rate-rate slopes (Fig. 2B, 3D, S2D, S3A). The figures plot log rates and the S2D legend speaks\n#   of log firing rates, so the slope is an ordinary least-squares fit of log10 later (or nonREM)\n#   rate on log10 earlier (or WAKE) rate, with a 95% interval; cells with a zero rate in either\n#   state are left out (a standard choice the paper does not state). Reading (b) fits linear rates.\n#   The expected slope is the midpoint of the paper's interval, with half its width as tolerance,\n#   the paper's own uncertainty.\n# M6. Triplets (Results, Sleep sub-states induce differential lasting firing rate changes;\n#   Supplemental Experimental Procedures, Spiking metrics). State A n, state B, state A n+1, with the\n#   change from A n to A n+1 attributed to B; nonREM-REM-nonREM triplets are kept unless a WAKE (>\n#   120 s) follows the REM before the second packet. The change is per cell rate(A n+1) minus rate(A\n#   n) (Fig. 5B legend); the S5 correlations use log(rate n+1) minus log(rate n). The per-sextile\n#   test for Fig. 5B is not named; readings (a) Wilcoxon signed-rank against zero, the test the\n#   paper uses for paired rate comparisons elsewhere; (b) one-sample t-test against zero; at p <\n#   0.05 unless the claim gives a bound. The R and p printed in Figures S5C to S5G equal Pearson\n#   tests on about 947 (S5C), 136 (S5D), 576 (S5E), 952 (S5F) and 972 (S5G) points, counts of\n#   cells, so those correlations have one point per cell, its changes averaged over its triplets (M1\n#   reading b).\n# M7. Tolerances. 10% of the reported value unless a claim gives another. Where the paper gives a\n#   median or mean +- SD (Table S1, Results), the SD is the spread of values over cells, events or\n#   sessions, not an uncertainty of the median or mean, and is often larger than the value (pE WAKE\n#   median 0.76 +- 1.53 Hz), so it is not used as the tolerance.\n#\n# Ids. Where the two earlier files named the same finding differently, one id is kept and the other\n# is listed here (000041 id / crcns-fcx-1 id -> id kept).\n#   dataset-composition / table1-dataset-counts -> table1-dataset-counts\n#   wake-sleep-cycles (000041; crcns had it in table1-dataset-counts) -> wake-sleep-cycles\n#   ma-statistics and ma-fraction-over-nrem-episodes / ma-statistics -> both kept, split as in 000041\n#   fig2a-median-rates and fig2a-skewed-wide-distribution / fig2a-pe-rate-distribution -> the two\n#     000041 ids\n#   fig2-burst-index-by-state / burst-index-by-state -> burst-index-by-state\n#   fig2c-acg-peaks and fig2c-acg-decay / fig2c-autocorrelogram -> the two 000041 ids\n#   fig2de-up-state-sequences / fig2de-fast-before-slow -> fig2de-fast-before-slow\n#   fig3b-population-decline / fig3ab-population-rate-declines -> fig3ab-population-rate-declines\n#   fig3-first-last-packet / first-last-packet-mean-rate -> first-last-packet-mean-rate\n#   fig3d-first-last-slope / fig3d-first-last-packet-slope -> fig3d-first-last-packet-slope\n#   fig3e-wake-before-after / post-sleep-wake-lower and fig3e-wake-before-after-sextiles -> the two\n#     crcns-fcx-1 ids\n#   fig3b-sextiles-over-sleep / fig3b-sextile-changes -> fig3b-sextile-changes\n#   fig3b-cv-over-sleep / cv-decreases-over-sleep -> cv-decreases-over-sleep\n#   fig3c-slow-oscillation-spindles-over-sleep / fig3c-spindles-over-sleep and fig3c-updown-over-sleep\n#     -> the two crcns-fcx-1 ids\n#   fig3f-4e-within-up-rates / fig3f-within-up-changes and fig4e-within-up-sextiles -> the two\n#     crcns-fcx-1 ids\n#   fig4i-band-power-within-nrem and fig4-delta-packet-length / fig4-lfp-within-nrem -> the two\n#     000041 ids\n#   fig4ii-iii-updown-spindles-within-packets / fig4-updown-within-packets and\n#     fig4-spindles-within-nrem -> the two crcns-fcx-1 ids\n#   fig4iv-sextiles-within-nrem, fig4v-cv-within-nrem and fig4vi-burst-within-nrem /\n#     fig4-sextiles-within-nrem -> the three 000041 ids\n#   fig4cd-packet-rate-lfp / fig4cd-packet-rate-lfp-correlations -> fig4cd-packet-rate-lfp-correlations\n#   fig5b-nrem-between-ma / fig5b-ma-nrem-ma -> fig5b-ma-nrem-ma\n#   fig5c-sigma-ma / fig5c-sigma-ma-change -> fig5c-sigma-ma-change\n#   fig5c-wake-movement / part of fig5b-wake-between-packets -> fig5c-wake-movement split out\n#   fig5c-rem-duration / part of fig5b-rem-between-packets -> fig5c-rem-duration split out, with the\n#     REM theta part as fig5c-rem-theta\n#   fig5c-delta-change / fig5c-delta-change-slow-cells -> fig5c-delta-change-slow-cells\n#   New here, tables1-state-durations and fig4-late-packet-sigma-delta.\nschema_version: 2\npaper: doi:10.1016/j.neuron.2016.03.036\nclaims:\n- id: table1-dataset-counts\n  statement: The data comprise 11 rats and 27 sessions, with 1360 clustered units of which 1121 are\n    stable, 995 putative pyramidal cells (mean 36.9 per session, range 10 to 104) and 126 putative\n    interneurons (4.67 per session, range 0 to 13).\n  source: Results, Identification of brain states, sentence 1; Results, Assessment of firing patterns\n    in different brain states, paragraph 1; Table S1, top\n  quote: This resulted in 995 putative pyramidal (pE) cells (mean of 36.9 cells/session; range ...\n    10–104) and 126 putative interneurons (pI) (4.67 cells/session; range ... 0–13)\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n  - quantity: rats\n    value: 11\n    tolerance: 0\n  - quantity: sessions\n    value: 27\n    tolerance: 0\n  - quantity: putative pyramidal cells\n    value: 995\n    tolerance: 0\n  - quantity: putative interneurons\n    value: 126\n    tolerance: 0\n  - quantity: stable units\n    value: 1121\n    tolerance: 0\n  - quantity: mean pE cells per session\n    value: 36.9\n    tolerance: 0.1\n  criterion: Counts of the subjects, sessions and classified cells, which every later claim uses.\n    They are integers of a fixed selection, so the tolerance is zero (0.1 for the mean, its printed\n    precision). Reproduced when all counts match; partially reproduced when the pE and pI counts\n    are within 10% and the rest are not exact. The per-rat sessions and units of Table S1 are\n    compared and reported. The 1360 clustered units are reported if the dataset holds unstable\n    units too.\n- id: wake-sleep-cycles\n  statement: The data hold 54 WAKE-SLEEP episodes (WAKE of at least 7 min followed by SLEEP of at\n    least 20 min), an average of 2.0 per session, and sessions without one were discarded.\n  source: Results, Identification of brain states, paragraph 1; Results, Firing pattern and LFP\n    changes across the course of sleep, sentence 1; Table S1\n  quote: We identified 54 WAKE-SLEEP episodes in our dataset, or an average of 2.0 episodes per\n    neuron recorded (27 sessions)\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n  - quantity: WAKE-SLEEP episodes\n    value: 54\n    tolerance: 5.4\n  - quantity: WAKE-SLEEP episodes per session\n    value: 2.0\n    tolerance: 0.2\n  criterion: Cycles as Table S1 and the Supplemental Experimental Procedures define them, a WAKE\n    (7+ min of not REM and not nonREM, interruptions < 2 min) immediately followed by a SLEEP (20+\n    min of nonREM, REM and MA with no interruption > 2 min). Readings (a) deposited cycle\n    intervals where a dataset holds them; (b) cycles built from the deposited state intervals by\n    these rules. Reproduced when under one reading both values are within tolerance and every\n    session has at least one cycle.\n- id: tables1-state-durations\n  statement: Median durations are 1192 s for WAKE episodes, 2421 s for SLEEP episodes, 297 s for\n    nonREM episodes, 98 s for REM episodes, and REM latency from SLEEP start is 647 s.\n  source: Table S1, top\n  inferred: Values read from Table S1 (median +- SD); no sentence of the text states them.\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n  - quantity: WAKE episode duration\n    value: 1192\n    tolerance: 119.2\n    unit: s\n  - quantity: SLEEP episode duration\n    value: 2421\n    tolerance: 242.1\n    unit: s\n  - quantity: nonREM episode duration\n    value: 297\n    tolerance: 29.7\n    unit: s\n  - quantity: REM episode duration\n    value: 98\n    tolerance: 9.8\n    unit: s\n  - quantity: REM latency (start REM minus start SLEEP)\n    value: 647\n    tolerance: 64.7\n    unit: s\n  depends_on:\n  - wake-sleep-cycles\n  criterion: Medians over the intervals of WAKE-SLEEP cycles (Supplemental Experimental Procedures,\n    analyses confined to those cycles); REM latency per SLEEP, from its start to the start of its\n    first REM episode. Table S1 also gives a WAKE-SLEEP episode duration of 5918 +- 125 s, which is\n    not judged, as it cannot be the sum of the WAKE and SLEEP medians and its SD is implausibly\n    small; it is reported. Reproduced when all five are within tolerance; partially reproduced\n    when three or four are.\n- id: ma-statistics\n  statement: There are 790 microarousals, with median duration 15.9 s, 0.32 per minute, taking 9.1%\n    of SLEEP time.\n  source: Results, Identification of brain states, paragraph 2; Table S1\n  quote: There were a total of 790 MAs in our dataset (median duration = 15.9±3.3sec; frequency =\n    0.32±0.12 per minute; 9.1±3.5% of time in SLEEP)\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n  - quantity: number of MAs\n    value: 790\n    tolerance: 79\n  - quantity: median MA duration\n    value: 15.9\n    tolerance: 1.59\n    unit: s\n  - quantity: MA incidence\n    value: 0.32\n    tolerance: 0.032\n    unit: per minute\n  - quantity: MA percent of SLEEP time\n    value: 9.1\n    tolerance: 0.91\n    unit: percent\n  criterion: MAs are arousals < 40 s between nonREM packets (Results; Table S1; Supplemental\n    Experimental Procedures), within SLEEP. Table S1 gives median +- SD, with incidence and percent\n    \"on a per-session basis\"; readings for the duration, (a) median over all MAs, (b) median over\n    sessions of session medians; incidence and percent are per session, then the median over\n    sessions (Table S1 header \"Median ± SD\"). Reproduced when under one reading the four values\n    are within tolerance; partially reproduced when three are.\n- id: ma-fraction-over-nrem-episodes\n  statement: The fraction of time occupied by MAs decreases over the course of nonREM episodes (R =\n    -0.85), with no statistical change over the course of SLEEP.\n  source: Results, Identification of brain states, paragraph 2\n  quote: Over nonREM episodes the fraction of time occupied by MAs decreased (correlation versus\n    normalized nonREM episode time ... R = −0.85, p < 10 −10 ), with no statistical change over the\n    course of SLEEP\n  statistics:\n  - about: MA time fraction against normalized nonREM episode time\n    test: correlation\n    statistic: R = -0.85\n    p: 1.0e-10\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - ma-statistics\n  criterion: Per nonREM episode, the fraction of each normalized-time bin spent in MA, Pearson\n    against normalized time (M3). An R of -0.85 at p < 1e-10 implies few, averaged points, so the\n    readings are M3 (c), 50 bins averaged over episodes, and 10 bins averaged over episodes (the\n    bin count is not given); M3 (a) and (b) are shown as variants. Judged by M4. The absence over\n    SLEEP is judged by the same correlation over normalized SLEEP time at p < 0.05; reproduced\n    when the episode decrease holds and the SLEEP correlation is not significant.\n- id: packet-duration\n  statement: nonREM packet durations span two orders of magnitude with a median of 111 s.\n  source: Results, Identification of brain states, paragraph 3; Table S1\n  quote: We found that the duration of packets was distributed over two orders of magnitude, with a\n    median of 111 seconds\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n    quantity: median nonREM packet duration\n    value: 111\n    tolerance: 11.1\n    unit: s\n  criterion: Packets are the scored nonREM packets (20+ s of uninterrupted nonREM, Table S1) in\n    WAKE-SLEEP cycles; reading (b) all packets of the session. Reproduced when under one reading\n    the median is within tolerance; the ratio of the longest to the shortest packet is reported for\n    the two orders of magnitude, which Table S1's 20 s minimum bounds from below.\n- id: fig2a-median-rates\n  statement: Median firing rates of pE cells are 0.76 Hz in WAKE, 0.69 Hz in nonREM and 0.88 Hz in\n    REM; of pI cells 5.59, 4.69 and 4.25 Hz.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 2; Figure 2A;\n    Figure S2C\n  quote: \"Median rates (±SD) of putative pyramidal cells in each state were: WAKE: 0.76±1.53 Hz,\n    nonREM: 0.69±0.86 Hz, REM: 0.88±1.33 Hz; and for putative interneurons were: WAKE: 5.59±7.25 Hz,\n    nonREM: 4.69±5.62 Hz, REM 4.25±9.43 Hz\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n  - quantity: pE median rate, WAKE\n    value: 0.76\n    tolerance: 0.076\n    unit: Hz\n  - quantity: pE median rate, nonREM\n    value: 0.69\n    tolerance: 0.069\n    unit: Hz\n  - quantity: pE median rate, REM\n    value: 0.88\n    tolerance: 0.088\n    unit: Hz\n  - quantity: pI median rate, WAKE\n    value: 5.59\n    tolerance: 0.559\n    unit: Hz\n  - quantity: pI median rate, nonREM\n    value: 4.69\n    tolerance: 0.469\n    unit: Hz\n  - quantity: pI median rate, REM\n    value: 4.25\n    tolerance: 0.425\n    unit: Hz\n  criterion: Per-cell rates per state as in M1 (readings a or b for cells in two cycles; and,\n    as a further reading, over the whole session), median over cells. Reproduced when under one\n    reading the six medians are within tolerance; partially reproduced when at least four are.\n- id: fig2a-skewed-wide-distribution\n  statement: The distribution of pE firing rates is strongly positively skewed, with a lognormal\n    tail toward high rates, and spans three orders of magnitude, from 0.05 to 5 Hz.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 2; Figure 2A;\n    Figure S2C\n  quote: the distribution of per-cell mean firing rates for putative pyramidal neurons was strongly\n    positively skewed, with a lognormal tail toward higher frequencies, and a supra-lognormal tail\n    toward lower frequencies ( Figure S2C ), spanning three orders of magnitude range from 0.05 Hz to\n    5 Hz ( Figure 2A )\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig2a-median-rates\n  criterion: On the per-cell rates of fig2a-median-rates, in each state and over all states\n    (\"Across all states\", Results). The paper does not say what range \"spanning\" means, and 0.05 to\n    5 Hz is two orders of magnitude, not the three it states. The shape holds when the pE rate\n    distribution has positive skewness in linear rate (a standard measure); the range holds when\n    it covers 0.05 to 5 Hz, each bound within 10%; readings of the range (a) 5th to 95th\n    percentile, (b) 1st to 99th percentile, (c) 2.5th to 97.5th percentile. Reproduced when under\n    one reading the shape and range hold in WAKE; partially reproduced when the shape holds and\n    the range does not. Skewness of log10 rates is reported for the lognormal description.\n- id: fig2a-fraction-above-2hz\n  statement: The right tail of the rate distribution is longer in WAKE and REM than in nonREM; the\n    fraction of pE cells above 2 Hz is 19.2% in WAKE and in REM and 8.8% in nonREM.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 2; Figure 2A\n  quote: \"The right tail extended toward higher rates during WAKE and REM compared to nonREM ( Figure\n    2A ; fraction of >2 Hz neurons: WAKE= 19.2%; REM= 19.2%; nonREM= 8.8%; Chi-Square Test: all\n    comparisons p < 1 −10 )\"\n  statistics:\n  - test: Chi-Square Test\n    p: 1.0e-10\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig2a-median-rates\n  expected:\n  - quantity: fraction above 2 Hz, WAKE\n    value: 19.2\n    tolerance: 1.92\n    unit: percent\n  - quantity: fraction above 2 Hz, REM\n    value: 19.2\n    tolerance: 1.92\n    unit: percent\n  - quantity: fraction above 2 Hz, nonREM\n    value: 8.8\n    tolerance: 0.88\n    unit: percent\n  criterion: Per-cell rates as in fig2a-median-rates. The paper says \"all comparisons p < 1e-10\",\n    yet WAKE and REM have the same fraction, so the comparisons are read as nonREM against WAKE and\n    nonREM against REM, each a 2 x 2 chi-square of cells above and below 2 Hz. Reproduced when the\n    three fractions are within tolerance and both tests give p < 1e-10 with nonREM lower;\n    partially reproduced when the fractions are within tolerance and the tests give p < 0.05.\n- id: fig2b-wake-nrem-slope\n  statement: Per-cell nonREM and WAKE rates are highly correlated (R = 0.82), but the slope of\n    their relation is below 1 (95% interval 0.66 to 0.71); in nonREM fast cells decrease and slow\n    cells increase their rates relative to WAKE.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 2; Figure 2B\n    and legend\n  quote: Whereas nonREM and WAKE firing rates remained highly correlated on a per-cell basis (R =\n    0.82, p < 1 −10 ), the slope of this relationship significantly deviated from 1 ( Figure 2B ),\n    demonstrating that state transitions exert a differential effect across the firing rate spectrum\n    (95% confidence interval of slope ... 0.66 – 0.71)\n  statistics:\n  - about: correlation of nonREM and WAKE rates\n    test: correlation\n    statistic: R = 0.82\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: slope of nonREM rate on WAKE rate\n    ci:\n      level: 0.95\n      low: 0.66\n      high: 0.71\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig2a-median-rates\n  expected:\n  - quantity: slope of nonREM on WAKE rate\n    value: 0.685\n    tolerance: 0.025\n  - quantity: correlation R\n    value: 0.82\n    tolerance: 0.082\n  criterion: Slope by M5 over pE cells, rates per state as in fig2a-median-rates; R is the Pearson\n    correlation of the same values (log10 in reading a, linear in reading b). Reproduced when,\n    under one reading, the slope and R are within tolerance and p < 1e-10; partially reproduced\n    when the slope's 95% interval lies below 1 but the slope or R is outside tolerance. The reverse\n    regression (WAKE on nonREM) is shown as a check on regression to the mean.\n- id: burst-index-by-state\n  statement: The burst index (fraction of spikes with ISIs below 15 ms) is highest in nonREM (median\n    11.8%), lowest in WAKE (4.0%), with REM (5.5%) slightly above WAKE.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 3\n  quote: Burst index was highest during nonREM (median in nonREM = 11.8%) and lowest during WAKE (4.0\n    %), with REM (5.5 %) slightly higher than WAKE (p < 0.05; Kruskal-Wallis test)\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 0.05\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n  - quantity: median burst index, nonREM\n    value: 11.8\n    tolerance: 1.18\n    unit: percent\n  - quantity: median burst index, WAKE\n    value: 4.0\n    tolerance: 0.4\n    unit: percent\n  - quantity: median burst index, REM\n    value: 5.5\n    tolerance: 0.55\n    unit: percent\n  criterion: The Results define the index as the fraction of spikes with ISIs below 15 ms; the\n    Supplemental Experimental Procedures compute it per neuron in 10 s bins as the proportion of ISIs\n    of 15 ms or less. Readings, (a) per cell and state, the fraction of ISIs <= 15 ms over all the\n    state's time; (b) the mean over the cell's 10 s bins in that state; (c) the fraction of spikes\n    with an ISI under 15 ms to the previous or next spike. ISIs spanning two intervals of a state\n    are dropped (a standard choice). Median over pE cells. Kruskal-Wallis across the three states\n    on per-cell values; the post hoc test for REM against WAKE is not named (readings Dunn's test,\n    or a Wilcoxon rank-sum test, at p < 0.05). Reproduced when under one reading the medians are\n    within tolerance, the Kruskal-Wallis p < 0.05 and REM exceeds WAKE at p < 0.05; partially\n    reproduced when the order nonREM > REM > WAKE and the Kruskal-Wallis test hold but a median\n    misses.\n- id: fig2c-acg-peaks\n  statement: The average spike autocorrelogram of pE cells peaks near 8 ms in nonREM, with smaller\n    peaks near 125 ms (theta) in REM and WAKE.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 3; Figure 2C\n    and legend\n  quote: a large peak occurred at approximately 8ms inter-spike interval during nonREM, whereas\n    smaller peaks were present at ~125 ms (i.e., theta frequency) during REM and WAKE ( Figure 2C )\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n  - quantity: autocorrelogram peak lag, nonREM\n    value: 8\n    tolerance: 0.8\n    unit: ms\n  - quantity: autocorrelogram theta peak lag, REM and WAKE\n    value: 125\n    tolerance: 12.5\n    unit: ms\n  criterion: The paper does not give the autocorrelogram bin, range or normalization. Per pE cell\n    and state, spike-time differences within the same interval of the state, 1 ms bins to 300 ms,\n    normalized to the cell's peak, averaged over cells (standard choices; Figure S2B shows\n    autocorrelograms normalized in amplitude). The nonREM peak is the maximum of the mean; the\n    theta peak is the largest local maximum between 60 and 250 ms (a standard window around 8 Hz).\n    Reproduced when the nonREM peak lag is within tolerance (7 to 9 ms in whole bins) and REM and\n    WAKE each show a local maximum within tolerance of 125 ms; partially reproduced when one part\n    holds.\n- id: fig2c-acg-decay\n  statement: The autocorrelogram of pE cells decays faster in nonREM than in WAKE and REM (decay fit\n    exponent medians -1.35, -0.83 and -0.80).\n  source: Results, Assessment of firing patterns in different brain states, paragraph 3; Figure 2C\n  quote: Time decay of the autocorrelograms of pyramidal neurons was significantly faster during\n    nonREM compared to WAKE and REM ( Figure 2C ; decay fit exponent median nonREM = – 1.35, WAKE = –\n    0.83, REM = – 0.80; p < 0.05; Kruskal-Wallis test)\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 0.05\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig2c-acg-peaks\n  expected:\n  - quantity: median decay exponent, nonREM\n    value: -1.35\n    tolerance: 0.135\n  - quantity: median decay exponent, WAKE\n    value: -0.83\n    tolerance: 0.083\n  - quantity: median decay exponent, REM\n    value: -0.8\n    tolerance: 0.08\n  criterion: The paper does not define the decay model or its range. A negative \"exponent\" is read\n    as a fit to each cell's normalized autocorrelogram from its peak outward. Readings, (a)\n    power-law fit (log count on log lag) from the peak to 100 ms; (b) the same to 500 ms; (c)\n    exponential fit, count proportional to exp(k t) with t in seconds, from the peak to 500 ms.\n    Kruskal-Wallis across states on per-cell exponents. Reproduced when under one reading the three\n    medians are within tolerance and the test gives p < 0.05 with nonREM the most negative;\n    partially reproduced when the ordering and test hold but the medians are outside tolerance.\n- id: synchrony-skew\n  statement: Population synchrony (fraction of pE cells firing in 50 ms windows) has a skewed\n    distribution; more than 15% of pE cells rarely fire synchronously with others (in 4% of\n    windows) while fewer than 4.2% fire synchronously in at least half of the windows.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 4; Figure S2F\n  quote: The fraction of principal cells firing in 50 ms overlapping time windows (‘population\n    synchrony’) showed a skewed distribution. More than 15% of principal neurons rarely fired\n    synchronously with others (4% of windows), while less than 4.2% discharged synchronously in at\n    least half of the windows\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n  - quantity: percent of pE cells that rarely fire synchronously\n    value: 15\n    tolerance: 1.5\n    unit: percent\n  - quantity: percent of pE cells firing synchronously in at least half of windows\n    value: 4.2\n    tolerance: 0.42\n    unit: percent\n  criterion: Windows of 50 ms every 25 ms (Supplemental Experimental Procedures, Spiking metrics).\n    The per-cell measure is not defined. Readings, (a) for each cell, the fraction of windows in\n    which it fires together with at least one other pE cell, \"rarely\" being at most 4% of windows;\n    (b) the fraction of all windows in which the cell fires, with the same cutoffs. The state used\n    is not said; all time in WAKE-SLEEP cycles is used, and each state is shown as a variant.\n    Reproduced when under one reading more than 15% of cells fall at or below 4% and fewer than\n    4.2% at or above 50%, each within tolerance of the bound or beyond it in the stated direction.\n- id: updown-durations\n  statement: DOWN state durations are skewed with a median of 0.19 s and UP state durations with a\n    median of 0.47 s.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 4; Figure S4A;\n    Table S1\n  quote: The durations of DOWN states of ‘slow oscillations’ showed a skewed distribution (median =\n    0.19s) and so did the UP states (median = 0.47s; Figure S4A )\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n  - quantity: median DOWN duration\n    value: 0.19\n    tolerance: 0.019\n    unit: s\n  - quantity: median UP duration\n    value: 0.47\n    tolerance: 0.047\n    unit: s\n  - quantity: number of UP states\n    value: 43230\n    tolerance: 4323\n  - quantity: number of DOWN states\n    value: 86839\n    tolerance: 8684\n  criterion: From UP and DOWN states detected as in the Supplemental Experimental Procedures\n    (OFF periods of population silence of 75 to 1250 ms; ON periods of at least 10 spikes lasting\n    200 to 4000 ms; low power above 100 Hz, 0.5 SD below the mean, 75 to 1250 ms; DOWN as OFF\n    coinciding with low gamma, DOWN states separated by a single spike combined; UP as ON\n    immediately following DOWN, truncated by DOWN or OFF). Readings, (a) the deposited detections\n    where a dataset holds them; (b) a new detection by these rules on the deposited spikes and LFP.\n    Reproduced when under one reading both medians are within tolerance and both distributions are\n    right-skewed; counts are reported and judged with the same tolerance as a variant.\n- id: fig1e-up-state-dynamics\n  statement: Within UP states, firing rates of pyramidal cells and interneurons decrease over the\n    course of the UP state, with decreasing E/(E+I) ratio and decreasing pE population synchrony;\n    UP states begin with a surge of gamma power followed by increased sigma power.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 4; Figure 1E\n    and legend; Figure S4C\n  quote: UP states were characterized by an initial surge of gamma power, followed by increased sigma\n    power ( Figure 1E ), corresponding to UP state-related sleep spindles. Firing rates of both\n    pyramidal cells and interneurons decreased over the time course of the UP state, accompanied by\n    a decreasing gain of excitation (excitatory-inhibitory, E-I, ratio) and decreasing population\n    synchrony of pyramidal neurons\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - updown-durations\n  criterion: UP states normalized in time to 0 to 1 (Fig. 1E legend), 10 equal bins (a standard\n    choice); mean pE and pI rates, synchrony (fraction of pE cells spiking in 50 ms bins) and E/(E+I)\n    (fraction of pE cells over the fraction of pE and pI cells spiking in 50 ms bins) per bin,\n    averaged over all UP states (Fig. 1E legend). The paper reports no test; Pearson R against\n    normalized time over the 10 bin means is used (a standard choice). Reproduced when the pE rate,\n    pI rate, synchrony and E/(E+I) each have negative R and are lower in the last bin than in the\n    first, and in the UP-onset-triggered spectrogram (Fig. 1E top; Fig. S4C, UP states of at least\n    1 s) the gamma (40 to 100 Hz) power peak precedes the sigma (9 to 25 Hz) peak. Partially\n    reproduced when three of the four decrease, or the four decrease and the spectral order fails.\n- id: fig2de-fast-before-slow\n  statement: In the early UP state pE cells fire in sequences stable across the first and second\n    halves of SLEEP, and a cell's onset latency is negatively correlated with its firing rate.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 5; Figure 2D\n    and 2E and legends\n  quote: pyramidal neurons fired in reliable spatiotemporal sequences during the early part of the UP\n    state (<200 msec) and these stereotypical sequences remained stable across the entirety of sleep\n    ( Figure 2D ). Additionally, the spike onset times of individual neurons in the sequences were\n    negatively correlated with their firing rates\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - updown-durations\n  criterion: Per cell, the mean latency of its first spike after each DOWN-UP transition (Fig. 2D\n    and E legends), within 200 ms (Results), in the first and second halves of SLEEP. The Fig. 2D\n    legend and the Results say halves of SLEEP, the Fig. 2E legend halves of the recording session;\n    readings (a) halves of each SLEEP, (b) halves of the session. The rate used is not named;\n    readings the cell's WAKE rate (M2) or its nonREM rate. The paper names no test; Pearson at p <\n    0.05, with log10 rate, is a standard choice. Reproduced when under one reading the first-half\n    and second-half latencies are positively correlated and latency is negatively correlated with\n    rate; partially reproduced when one of the two holds.\n- id: fig2f-rate-group-correlations\n  statement: In nonREM, pairwise spike-count correlations depend on firing rate group; pairs within\n    the fastest group and within the slowest group are positively correlated, fast-firing pairs most\n    highly, and fast and slow cells are negatively correlated with each other.\n  source: Results, Assessment of firing patterns in different brain states, paragraph 5; Figure 2F\n    and legend\n  quote: the fastest and slowest firing neurons tended to be positively correlated within groups, but\n    were actually negatively correlated across groups ( Figure 2F )\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  criterion: Pearson correlation of 100 ms binned spike counts per simultaneously recorded pair in\n    nonREM (Supplemental Experimental Procedures, Spiking metrics; Fig. 2F legend), grouped by the\n    two cells' rate groups (M2 readings). The legend says all comparisons except (4,4) are\n    significant, with the test in the Supplementary Methods, which do not describe it. A Wilcoxon\n    signed-rank test of the pair correlations against zero, per group pair, at p < 0.05 is used (a\n    standard choice). Reproduced when under one reading the mean correlation of fastest with\n    fastest is positive and the largest of the 21 group pairs, fastest with slowest is negative,\n    and slowest with slowest is positive, each at p < 0.05; the full 6 x 6 matrix is reported.\n    Partially reproduced when the fastest-fastest and fastest-slowest parts hold and the\n    slowest-slowest part does not.\n- id: fig3ab-population-rate-declines\n  statement: The mean population firing rate of pE cells declines over SLEEP (nonREM time only).\n  source: Results, Firing pattern and LFP changes across the course of sleep, paragraph 1; Figure 3A\n    and 3B and legend\n  quote: we found that the arithmetic mean of the population firing rates of pE cells declined over\n    the course of sleep using a test of correlation of spike rate versus time ( Figure 3A–B ; R = –\n    0.11, p < 10 −3 )\n  statistics:\n  - test: correlation of spike rate versus time\n    statistic: R = -0.11\n    p: 0.001\n    p_relation: \"<\"\n    n: 995 cells, 54 sessions, 11 rats\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  criterion: M3 and M4, nonREM time of SLEEP only, rate as the arithmetic mean over pE cells,\n    Pearson (Fig. 3B legend).\n- id: first-last-packet-mean-rate\n  statement: The mean pE rate is lower in the last than in the first nonREM packet of SLEEP (1.04\n    against 0.88 Hz).\n  source: Results, Firing pattern and LFP changes across the course of sleep, paragraph 1\n  quote: Comparison of the population discharge rates in the first and last nonREM packets of SLEEP\n    episodes showed an overall mean rate decrease (1.04±1.20 Hz versus 0.88±0.91 Hz; p < 0.02;\n    Wilcoxon test)\n  statistics:\n  - test: Wilcoxon test\n    p: 0.02\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  expected:\n  - quantity: mean pE rate, first packet\n    value: 1.04\n    tolerance: 0.104\n    unit: Hz\n  - quantity: mean pE rate, last packet\n    value: 0.88\n    tolerance: 0.088\n    unit: Hz\n  criterion: Per cell, rate in the first and last nonREM packet of each SLEEP (M1 readings a and b),\n    mean +- SD over cells. The paper says \"Wilcoxon test\"; readings (a) signed-rank, paired by\n    cell, (b) rank-sum; two-sided. Reproduced when under one reading both means are within\n    tolerance and p < 0.02 with the last lower; partially reproduced when the decrease is\n    significant at p < 0.05 but a mean is outside tolerance.\n- id: post-sleep-wake-lower\n  statement: pE rates in the 5 min of WAKE after SLEEP are lower than in the 5 min of WAKE before.\n  source: Results, Firing pattern and LFP changes across the course of sleep, paragraph 1\n  quote: This effect was ‘carried over’ to subsequent WAKE as shown by the significantly decreased\n    discharge rate of pE neurons in a 5-min post-sleep WAKE compared to a 5-min pre-sleep WAKE epoch\n    (p < 10 −6 ; Wilcoxon test)\n  statistics:\n  - test: Wilcoxon test\n    p: 1.0e-6\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  criterion: Per cell, rate in the last 5 min of the WAKE that precedes SLEEP and the first 5 min of\n    WAKE after it (Fig. S3A legend; Results, \"immediately before\" and \"immediately after\"). What\n    counts as the WAKE after SLEEP is not defined; readings (i) the next scored WAKE interval (7+\n    min), (ii) the arousal of more than 120 s that ends SLEEP (Results, SLEEP \"terminated by\n    prolonged (> 120 sec) WAKE\"); cycles without a following WAKE are left out. The paper says\n    \"Wilcoxon test\"; readings (a) signed-rank, paired by cell, (b) rank-sum, each with M1\n    readings. Judged by M4.\n- id: fig3d-first-last-packet-slope\n  statement: Comparing the same cells in the first and last nonREM packets of SLEEP, the slope of\n    last on first rate is below 1 (95% interval 0.827 to 0.880); fast cells decrease and slow cells\n    increase their rates over sleep.\n  source: Results, Firing pattern and LFP changes across the course of sleep, paragraph 2; Figure 3D\n    and legend; Figure S3B\n  quote: we assessed spike rates of the same neurons in the first versus the last nonREM packets of\n    SLEEP and found the slope of this correlation significantly departed from unity (slope 95%\n    confidence interval 0.827–0.880)\n  statistics:\n  - ci:\n      level: 0.95\n      low: 0.827\n      high: 0.88\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  expected:\n    quantity: slope of last-packet on first-packet rate\n    value: 0.8535\n    tolerance: 0.0265\n  criterion: M5 on pE cells, one point per cell and SLEEP (M1 reading a) or per cell (reading b).\n    Reproduced when under one reading the slope is within tolerance; partially reproduced when its\n    95% interval lies below 1 but the slope is outside tolerance. The reverse regression is shown\n    as a check on regression to the mean.\n- id: fig3b-sextile-changes\n  statement: Over SLEEP (nonREM only), the mean rate of the highest-rate sextiles decreases while\n    the lowest sextile shows a marginal increase.\n  source: Results, Firing pattern and LFP changes across the course of sleep, paragraph 2; Figure 3B,\n    bottom, and legend\n  quote: The mean spike discharge rate of highest-firing rate sextile groups significantly decreased\n    over sleep whereas the activity of the lowest-firing rate sextile showed a marginal increase (\n    Figure 3B ; Pearson correlations versus normalized time)\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  criterion: Sextiles by M2; per sextile, mean rate against normalized SLEEP time by M3, Pearson.\n    The per-sextile R and p are printed only in the figure and were not read. Reproduced when under\n    one reading the top sextile has a negative R with p < 0.05 and the bottom sextile a positive R\n    (any p, as \"marginal\"); partially reproduced when only the top-sextile decrease holds.\n- id: cv-decreases-over-sleep\n  statement: The coefficient of variation of pE firing rates decreases over SLEEP.\n  source: Results, Firing pattern and LFP changes across the course of sleep, paragraph 2\n  quote: the coefficient of firing rate variation also showed a significantly decreasing slope over\n    the course of SLEEP (R = – 0.05; p < 0.01)\n  statistics:\n  - test: Pearson correlation versus normalized time\n    statistic: R = -0.05\n    p: 0.01\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  criterion: CV across simultaneously recorded pE cells of their rates in 10 s bins, normalized by\n    the recording's mean CV (Supplemental Experimental Procedures, Spiking metrics), against\n    normalized SLEEP time, nonREM bins only (M3 reading b); M3 reading a (CV per packet) as a\n    second reading. Judged by M4.\n- id: fig3c-spindles-over-sleep\n  statement: Over SLEEP spindle incidence (1.94/min) decreases while spindle duration (0.52 s),\n    frequency (13.93 Hz) and amplitude (203.3 uV) do not change.\n  source: Results, Firing pattern and LFP changes across the course of sleep, paragraph 3; Figure 3C,\n    bottom; Table S1\n  quote: Incidence of spindles (1.94±0.39/min) decreased (R = – 0. 093; p < 10 −5 ), while spindle\n    duration (0.52±0.32 sec), frequency (13.93±0.93 Hz) and amplitude (203.3±87.71 µV) did not change\n    over SLEEP\n  statistics:\n  - about: spindle incidence against normalized SLEEP time\n    test: correlation\n    statistic: R = -0.093\n    p: 1.0e-5\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  expected:\n  - quantity: spindle incidence\n    value: 1.94\n    tolerance: 0.194\n    unit: per minute\n  - quantity: spindle duration\n    value: 0.52\n    tolerance: 0.052\n    unit: s\n  - quantity: spindle frequency\n    value: 13.93\n    tolerance: 1.393\n    unit: Hz\n  - quantity: spindle amplitude\n    value: 203.3\n    tolerance: 20.33\n    unit: uV\n  criterion: Spindles detected as in the Supplemental Experimental Procedures (10 to 20 Hz band,\n    rectified half-cycles above 2 SD of the filtered signal, half-cycles more than 30 ms apart not\n    joined, 200 to 3000 ms, events within 300 ms merged, high-voltage spindles found at 6 to 9 Hz\n    and 7 SD removed); readings (a) the deposited detections where a dataset holds them, (b) a new\n    detection. Table S1 gives the incidence as 0.049 +- 0.008 Hz (2.94 per minute), which disagrees\n    with 1.94 per minute in the Results; both are compared and the discrepancy is recorded; the\n    claim is judged on the Results value. Incidence change by M3 and M4. For duration, frequency\n    and amplitude, claims of absence on the same correlation (the paper's test for this\n    paragraph), reproduced when p >= 0.05 for each. Reproduced when the incidence decrease, the\n    three absences and the four values hold; partially reproduced when the decrease holds and some\n    of the rest do not.\n- id: fig3c-updown-over-sleep\n  statement: Over SLEEP the incidence of UP and DOWN states decreases, DOWN state duration\n    increases, UP state duration does not change, and the fraction of time in neither UP nor DOWN\n    increases.\n  source: Results, Firing pattern and LFP changes across the course of sleep, paragraph 3; Figure 3C\n    and legend\n  quote: Incidence of both UP states (R = – 0.10; p <10 −6 ) and DOWN states (R = – 0.08; p < 10 −4 )\n    decreased significantly, while the duration of DOWN states increased (R slope = 0.09; p < 10 −4 ;\n    Figure 3B ) and duration of UP states did not change. In addition, the fraction of time that\n    could be identified as neither UP nor DOWN state (‘other’) increased significantly over the\n    course of sleep (R = 0.08; p < 10 −2 )\n  statistics:\n  - about: UP incidence\n    statistic: R = -0.10\n    p: 1.0e-6\n    p_relation: \"<\"\n  - about: DOWN incidence\n    statistic: R = -0.08\n    p: 1.0e-4\n    p_relation: \"<\"\n  - about: DOWN duration\n    statistic: R = 0.09\n    p: 1.0e-4\n    p_relation: \"<\"\n  - about: fraction neither UP nor DOWN\n    statistic: R = 0.08\n    p: 0.01\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - updown-durations\n  - wake-sleep-cycles\n  criterion: UP/DOWN detections as in updown-durations, nonREM time of SLEEP only, M3 and M4 for\n    each of the four changes; \"other\" is nonREM time in neither a detected UP nor a DOWN state. UP\n    duration is a claim of absence on the same correlation, reproduced when p >= 0.05. Reproduced\n    when all five hold under one reading; partially reproduced when at least three do.\n- id: fig3f-within-up-changes\n  statement: Within UP states, pE rates decrease over SLEEP, and from first to last packet the\n    fastest sextile and interneurons decrease while the slowest sextile increases.\n  source: Results, Firing pattern and LFP changes across the course of sleep, paragraph 3; Figure 3F\n    and legend; Figure S3C\n  quote: Comparison of firing rates within UP states showed a general decrease across the whole\n    population ( Figure S3C ) and subtraction of UP state firing activity in early sleep from that\n    in late sleep revealed that the firing rates of the fastest sextile group and putative\n    interneurons decreased later in sleep, whereas firing of the slowest sextile increased\n  statistics:\n  - about: within-UP pE rate against normalized SLEEP time (Figure S3C)\n    statistic: R = -0.19849\n    p: 3.3168e-09\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - updown-durations\n  - fig3b-sextile-changes\n  criterion: Rates counted only within UP states. The S3C correlation by M3 and M4 on the mean pE\n    within-UP rate (bound p < 1e-8). The sextile part, per cell, within-UP rate in the last packet\n    minus the first packet of SLEEP (Fig. 3F legend), mean per group; no test is named, so a\n    Wilcoxon signed-rank test against zero per group at p < 0.05 is used (a standard choice).\n    Reproduced when the S3C correlation holds and the fastest sextile and pI change is negative\n    and the slowest positive, each significant; partially reproduced when the correlation holds\n    and two of the three signs are right.\n- id: figs3a-first-last-rem-ma-slopes\n  statement: Rates change differentially across the spectrum also from the first to last REM and\n    first to last MA of SLEEP and from WAKE before to WAKE after sleep, with slopes below 1 (REM\n    0.76 to 0.83, MA 0.58 to 0.68, WAKE 0.80 to 0.86).\n  source: Results, Firing pattern and LFP changes across the course of sleep, last paragraph, and\n    Sleep sub-states induce differential lasting firing rate changes, paragraph 1; Figure S3A legend\n  quote: first versus last REM episode, also note significant deviation of slope from 1\n    (confidence interval ... 0.76-0.83). Right first versus last MA episode per sleep session,\n    confidence interval of slope does not include 1 (0.58- 0.68)\n  statistics:\n  - about: first against last REM\n    ci:\n      level: 0.95\n      low: 0.76\n      high: 0.83\n  - about: first against last MA\n    ci:\n      level: 0.95\n      low: 0.58\n      high: 0.68\n  - about: WAKE before against WAKE after SLEEP\n    ci:\n      level: 0.95\n      low: 0.8\n      high: 0.86\n  - about: correlation of WAKE before and WAKE after SLEEP rates (Figure S3A legend)\n    test: Pearson\n    p: 1.0e-10\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - post-sleep-wake-lower\n  expected:\n  - quantity: slope, last REM on first REM\n    value: 0.795\n    tolerance: 0.035\n  - quantity: slope, last MA on first MA\n    value: 0.63\n    tolerance: 0.05\n  - quantity: slope, WAKE after on WAKE before\n    value: 0.83\n    tolerance: 0.03\n  criterion: M5 for each pair. The Results print the WAKE interval as \"0.801 - 0.0856\" and the\n    S3A legend as 0.80 to 0.86; the legend is used. The WAKE windows are the last 5 min before and\n    the first 5 min after SLEEP (S3A legend; readings of post-sleep-wake-lower). The S3A legend's\n    confidence level is not stated; 95% is used, as in the Results. Reproduced when under one\n    reading all three slopes are within tolerance; partially reproduced when all three intervals\n    lie below 1.\n- id: fig3e-wake-before-after-sextiles\n  statement: From 5 min of WAKE before to 5 min of WAKE after SLEEP, the top three sextiles\n    decrease their rates and the lowest sextile increases.\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 1;\n    Figure 3E and legend\n  quote: Comparison of firing rates during 5 minutes of WAKE immediately before SLEEP versus 5\n    minutes of WAKE immediately after SLEEP showed a significant decrease firing in the top three\n    sextile groups and an increase in the lowest sextile group (all ps < 0.05; stars in Figure 3E )\n  statistics:\n  - test: one-tailed Wilcoxon\n    p: 0.05\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - post-sleep-wake-lower\n  criterion: Sextiles by M2; windows as in post-sleep-wake-lower; one-tailed Wilcoxon per sextile\n    in the reported direction (Fig. 3E legend), read as signed-rank paired by cell. Reproduced when\n    the top three sextiles decrease and the lowest increases, each at p < 0.05; partially\n    reproduced when at least three of the four do.\n- id: fig4i-band-power-within-nrem\n  statement: Within nonREM episodes and packets delta and sigma power increase, while gamma power\n    decreases over episodes but not over packets.\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraph 2;\n    Figure 4A-B i and legend\n  quote: Over nonREM episodes and packets, delta and sigma band power steadily increased ( Trachsel et\n    al., 1988 ), whereas gamma power decreased over episodes but not packets ( Figure 4 A–B i )\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  criterion: Band power (delta 0.5 to 4 Hz, Results and Fig. 1B legend; the Fig. 4 legend gives 1\n    to 4 Hz, a variant; sigma 9 to 25 Hz, gamma 40 to 100 Hz) from a spectrogram of 10 s windows\n    every 1 s (Supplemental Experimental Procedures, Brain state scoring; that this is the\n    spectrogram used here is a choice the paper does not state), z-scored per session (a standard\n    choice), on one cortical channel. M3 and M4 for each band, within episodes and packets; the\n    paper reports no R or p for these, so the bound is p < 0.05. The gamma change over packets is a\n    claim of absence on the same correlation, reproduced when p >= 0.05. Reproduced when all six\n    hold; partially reproduced when the delta and sigma increases hold.\n- id: fig4-delta-packet-length\n  statement: Mean delta power within whole packets, normalized by nonREM delta power, is positively\n    correlated with packet length (R = 0.31).\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraph 2\n  quote: Mean delta power within whole packets (normalized by nonREM delta power) was positively\n    correlated with packet length (R = 0.31; p < 0.05)\n  statistics:\n  - statistic: R = 0.31\n    p: 0.05\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig4i-band-power-within-nrem\n  criterion: One point per packet, its mean delta power divided by the session's mean nonREM delta\n    power (Results), against packet duration, Pearson (the test is not named; a standard choice).\n    Judged by M4.\n- id: fig4-late-packet-sigma-delta\n  statement: In the final portion of nonREM packets, the positive correlation between delta and\n    sigma power gives way to a sudden increase of sigma power with a concurrent decrease of delta\n    power.\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraph 3;\n    Figure 4A-B i\n  quote: During the final portion of packets, the generally positive correlation between delta and\n    sigma power was replaced by a sudden increase of sigma power and concurrent decrease of delta\n    power\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig4i-band-power-within-nrem\n  criterion: Band power as in fig4i-band-power-within-nrem, packets time-normalized (M3). The\n    paper gives no test and does not define the final portion; readings (a) the last 20 s of each\n    packet (the window the paper uses for packet-end sigma power), (b) the last tenth of normalized\n    packet time. Per packet, mean sigma and delta power in the final portion against the\n    preceding portion of equal length; Wilcoxon signed-rank over packets at p < 0.05 (a standard\n    choice). The correlation between delta and sigma power over 1 s spectrogram steps is computed\n    in the final portion and in the rest of each packet and its mean over packets compared. Reproduced\n    when under one reading sigma rises and delta falls at p < 0.05 and the delta-sigma correlation is\n    positive in the rest of the packet and lower in the final portion; partially reproduced when the\n    sigma rise and delta fall hold and the correlation part does not.\n- id: fig4-updown-within-packets\n  statement: Within packets UP and DOWN incidence increase, UP duration decreases and DOWN duration\n    increases, so the UP/DOWN ratio falls.\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraph 2;\n    Figure 4A-B ii\n  quote: The incidence of both UP states (R = 0.05, p < 10 −3 ) and DOWN states (R = 0.08; p < 10 −10\n    ) increased significantly within packets, whereas the duration of UP states decreased (R = –\n    0.02; p < 0.01) and DOWN states increased (R = 0.07; p < 10 −10 ), changing the UP-DOWN balance\n    (UP/DOWN ratio negative correlation versus time p < 0.05)\n  statistics:\n  - about: UP incidence\n    statistic: R = 0.05\n    p: 0.001\n    p_relation: \"<\"\n  - about: DOWN incidence\n    statistic: R = 0.08\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: UP duration\n    statistic: R = -0.02\n    p: 0.01\n    p_relation: \"<\"\n  - about: DOWN duration\n    statistic: R = 0.07\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: UP/DOWN ratio\n    p: 0.05\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - updown-durations\n  criterion: As fig3c-updown-over-sleep, over time-normalized packets. The UP/DOWN ratio is not\n    defined; readings (a) UP duration over DOWN duration, (b) time in UP over time in DOWN, per\n    time bin. Reproduced when all five hold under one reading; partially reproduced when at least\n    three do. The paper also reports the fraction of time neither UP nor DOWN as increasing with R =\n    -0.04, a sign that contradicts the word; it is reported and not judged.\n- id: fig4-spindles-within-nrem\n  statement: Spindle incidence and duration increase within nonREM episodes and packets (duration\n    0.61 to 0.67 s in episodes, 0.58 to 0.67 s in packets), while spindle frequency and amplitude do\n    not change.\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraph 2;\n    Figure 4A-B iii\n  quote: The incidence of spindles significantly increased both within nonREM episodes ( Figure 4A–B\n    iii ; R = 0.08; p < 10 −10 ) and packets (R = 0.7; p < 10 −10 ). Spindle duration also increased\n    (nonREM episode increase from 0.61 ± 0.33 s to 0.67 ± 0.30 s, R = 0.08; p < 10 −3 ; nonREM packet\n    increase from 0.58 ± 0.25 s to 0.67 ± 0.27 s, R = 0.07, p < 10 −4 ), whereas spindle frequency and\n    amplitude remained unchanged\n  statistics:\n  - about: spindle incidence within episodes\n    statistic: R = 0.08\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: spindle incidence within packets\n    statistic: R = 0.7\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: spindle duration within episodes\n    statistic: R = 0.08\n    p: 0.001\n    p_relation: \"<\"\n  - about: spindle duration within packets\n    statistic: R = 0.07\n    p: 0.0001\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig3c-spindles-over-sleep\n  expected:\n  - quantity: spindle duration, early episode\n    value: 0.61\n    tolerance: 0.061\n    unit: s\n  - quantity: spindle duration, late episode\n    value: 0.67\n    tolerance: 0.067\n    unit: s\n  - quantity: spindle duration, early packet\n    value: 0.58\n    tolerance: 0.058\n    unit: s\n  - quantity: spindle duration, late packet\n    value: 0.67\n    tolerance: 0.067\n    unit: s\n  criterion: Spindles as in fig3c-spindles-over-sleep. M3 and M4 for incidence and duration. The\n    packet incidence R of 0.7 is read as a likely misprint for 0.07 beside the other values; the\n    sign and p are judged, not the size. \"From ... to\" is not defined; readings (a) first and last\n    tenth of normalized time, (b) first and last third. Frequency and amplitude are claims of\n    absence on the same correlation, reproduced when p >= 0.05. Reproduced when the four increases\n    hold, the two absences hold and the four durations are within tolerance under one reading;\n    partially reproduced when the increases hold.\n- id: fig4e-late-packet-sigma\n  statement: UP states late in nonREM packets have more sigma power than UP states early in packets.\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraphs 3 and\n    6; Figure 4E; Figure S4B and S4D and legends\n  quote: Spectral comparison of UP states in first third versus last third of packets showed\n    increased sigma power ( Figure 4E ; p < 10 −10 ; Wilcoxon rank-sum test and per-pixel\n    significance; Figure S4B )\n  statistics:\n  - about: UP state sigma power, first against last third of packets\n    test: Wilcoxon rank-sum test\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: DOWN-UP transition-triggered sigma power, late against early packet (Results, Figure S4B)\n    test: t-test\n    p: 1.0e-5\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - updown-durations\n  criterion: UP-state spectrograms for UP states in the first and last thirds of each packet;\n    readings (a) time-normalized to UP duration for UP states longer than 500 ms (S4B legend), (b)\n    UP-onset-triggered without normalization for UP states of at least 1 s (S4C legend). Per UP\n    state, mean 9 to 25 Hz power over the UP state; Wilcoxon rank-sum of late against early.\n    Reproduced when late exceeds early with p < 1e-10 under one reading; partially reproduced at p\n    < 1e-5. The per-pixel t-test map of S4B is shown.\n- id: fig4iv-sextiles-within-nrem\n  statement: Within both nonREM episodes and nonREM packets, the fastest sextiles decrease their\n    rates while the slowest increase.\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraph 4;\n    Figure 4A-B iv\n  quote: Firing rates of the fastest-firing sextile groups decreased, whereas those of the\n    slowest-firing sextile groups increased within both nonREM episodes and packets ( Figure 4A, B iv\n    ; R and p values in figure)\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  criterion: Sextiles by M2; mean rate per sextile against normalized episode or packet time, M3\n    readings and Pearson. The per-sextile R and p are only in the figure and were not read.\n    Reproduced when under one reading the top sextile has a negative and the bottom sextile a\n    positive R, each p < 0.05, in both episodes and packets; partially reproduced when this holds\n    in one of the two, or one sextile's direction holds in both.\n- id: fig4v-cv-within-nrem\n  statement: The coefficient of variation of binned population firing rates decreases within nonREM\n    episodes (R = -0.13) and packets (R = -0.12).\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraph 4;\n    Figure 4A-B v and legend\n  quote: resulting in a decreasing coefficient of variation of binned population firing rates (\n    Figure 4 A–B v ; R episode = −0.13, p < 10 −10 ; R packet = – 0.12, p < 10 −10 )\n  statistics:\n  - about: CV within episodes\n    statistic: R = -0.13\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: CV within packets\n    statistic: R = -0.12\n    p: 1.0e-10\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  criterion: CV across a session's simultaneously recorded pE cells of their rates in 10 s bins,\n    normalized by the recording's mean (Supplemental Experimental Procedures, Spiking metrics);\n    each bin placed at its normalized time in its episode or packet, M3 reading b, Pearson. Judged\n    by M4 for each.\n- id: fig4vi-burst-within-nrem\n  statement: The 15 ms burst index of pE cells increases within nonREM episodes (R = 0.09) and\n    packets (R = 0.08).\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraph 4;\n    Figure 4A-B vi and legend\n  quote: An additional metric, the 15ms spike burst index of pyramidal neurons, also showed a\n    positive slope within both nonREM episodes and packets ( Figure 4 A–B vi ; R episode = 0.09, p <\n    10 −10 ; R packet = 0.08, p < 10 −10 )\n  statistics:\n  - about: burst index within episodes\n    statistic: R = 0.09\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: burst index within packets\n    statistic: R = 0.08\n    p: 1.0e-10\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - burst-index-by-state\n  criterion: Burst ratio per neuron in 10 s bins, the proportion of ISIs of 15 ms or less,\n    normalized by the recording's mean (Supplemental Experimental Procedures, Spiking metrics);\n    readings (a) the mean over pE cells per bin, (b) each cell and bin a point; placed at\n    normalized time, M3 reading b, Pearson. Judged by M4 for each.\n- id: fig4cd-packet-rate-lfp-correlations\n  statement: Across packets, the top sextile's rate correlates negatively with delta power, DOWN\n    duration and DOWN incidence and positively with UP duration and gamma power, and the bottom\n    sextile's rate correlates positively with sigma power in the last 20 s of the packet; other\n    combinations are not significant.\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraph 5;\n    Figure 4C and 4D and legends\n  quote: Per-packet firing rate of the top sextile group was negatively correlated with per-packet\n    LFP metrics, including whole-packet delta power (Z-scored per session; Figure 4C ; R= – 0.28; p\n    < 10 −10 ), DOWN state duration (R = – 0.16, p < 10 −4 ), and DOWN state incidence rate (Z-scored\n    per session; R = – 0.29, p<10 −10 ). A positive correlation was observed between firing rate of\n    the top sextile group and UP state duration (R = 0.14, p < 10 −3 ) and gamma power ( Figure 4D ;\n    R = 0.44; p < 10 −10 ). Finally, a positive correlation was found between normalized firing rates\n    per packet in the bottom sextile group and sigma power in the last 20 sec of the packet (R =\n    0.25; p < 10 −10 ). Other tested relationship combinations were not significant\n  statistics:\n  - about: top sextile rate against delta power\n    statistic: R = -0.28\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: top sextile rate against DOWN duration\n    statistic: R = -0.16\n    p: 0.0001\n    p_relation: \"<\"\n  - about: top sextile rate against DOWN incidence\n    statistic: R = -0.29\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: top sextile rate against UP duration\n    statistic: R = 0.14\n    p: 0.001\n    p_relation: \"<\"\n  - about: top sextile rate against gamma power\n    statistic: R = 0.44\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: bottom sextile rate against sigma power in the last 20 s\n    statistic: R = 0.25\n    p: 1.0e-10\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - updown-durations\n  - fig4i-band-power-within-nrem\n  criterion: One point per packet; per packet the mean rate of the sextile's cells normalized per\n    sleep session (Results, \"normalized per sleep session\"; read as divided by the mean packet rate\n    of that SLEEP, a standard reading) and the packet's LFP metrics z-scored per session (Results),\n    Pearson. M4 for each of the six. The set of \"other tested\" combinations is not listed; the\n    bottom sextile against delta power, DOWN duration, DOWN incidence, UP duration and gamma, and\n    the top sextile against late sigma, are tested at p < 0.05 and reported. Reproduced when the\n    six hold; partially reproduced when at least four do.\n- id: fig4e-within-up-sextiles\n  statement: Within UP states, from early to later parts of packets, the fastest sextile's rate\n    drops, interneuron rate increases, and the slowest sextile decreases slightly.\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, paragraph 6;\n    Figure 4E, bottom, and legend\n  quote: Comparison of within-UP state activity in the first versus second third of packets showed a\n    drop in firing rate for the fastest sextile group (P < 10 −8 ; Wilcoxon rank-sum test), an\n    increase in firing rate of putative interneurons (P < 10 −3 ), and a small but significant\n    decrease for the slowest group (P < 0.003; Figure 4B, E )\n  statistics:\n  - about: fastest sextile\n    test: Wilcoxon rank-sum test\n    p: 1.0e-8\n    p_relation: \"<\"\n  - about: putative interneurons\n    test: Wilcoxon rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n  - about: slowest sextile\n    test: Wilcoxon rank-sum test\n    p: 0.003\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - updown-durations\n  criterion: The Results say first against second third, the Fig. 4E legend first against last\n    third; readings (a) first against second third, (b) first against last third. The unit of the\n    rank-sum test is not stated; readings (i) per UP state, the group's mean rate within the UP\n    state, rank-sum of the two sets of UP states; (ii) per cell, its within-UP rate in each third,\n    rank-sum of the two sets of cells. Judged by M4 per group; reproduced when all three hold under\n    one reading, partially when two do.\n- id: figs5-within-wake-rem\n  statement: Within WAKE the two highest sextiles increase and the two lowest decrease their rates,\n    opposite to nonREM; within REM all sextiles except the fourth increase.\n  source: Results, Firing rate and LFP changes within nonREM episodes and packets, last paragraph;\n    Figure S5A and S5B and legend\n  quote: We found that entry into WAKE corresponded with an increase in firing rate of the highest\n    sextile two groups and a drop in firing rate of the lowest two sextile groups ( Figure S5A ),\n    opposing the effects seen in SLEEP and nonREM. During REM, all sextile groups except the fourth\n    showed an increase in firing rate\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  criterion: Sextiles by M2, numbered as in the S5 legend (1 highest), so \"the fourth\" is the third\n    from the bottom. For REM, rate against normalized REM episode time, M3 reading c (50 bins, as\n    Figure S5B's printed R and p imply), Pearson; the REM part holds when the five sextiles other\n    than the fourth show positive R at p < 0.05. Figure S5B prints, for sextiles 1 to 6, R 0.652,\n    0.526, 0.422, 0.268, 0.437 and 0.410 with p 2.97e-07, 8.67e-05, 0.00226, 0.0600, 0.00151 and\n    0.00309, which agree with the Results. For WAKE, Figure S5A (panel title WAKE, read from the\n    rendered page) prints R 0.267, 0.302, 0.184, -0.049, 0.531 and -0.192 with p 0.061, 0.033,\n    0.200, 0.737, 7.2e-05 and 0.181, which do not support the Results sentence over the whole\n    episode; the legend says rates diverge \"especially towards the beginning of the state\", and\n    the Results speak of \"entry into WAKE\". Readings for WAKE, (a) Pearson over normalized WAKE\n    time in 50 bins, as printed; (b) the change at entry, per cell the rate in the first tenth of\n    normalized WAKE minus the rate in the period before WAKE (the figure plots from -0.25 of\n    normalized time), Wilcoxon signed-rank per sextile at p < 0.05 (a standard choice). The WAKE\n    part holds when under one reading the two highest sextiles increase and the two lowest\n    decrease, each at p < 0.05. Reproduced when both parts hold, partially when one does.\n- id: fig5b-ma-nrem-ma\n  statement: An intervening nonREM packet reduces the rates of the top two sextiles from one MA to\n    the next, with an inverse relation between rate and change across cells.\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 2;\n    Figure 5B, blue; Figure S5C\n  quote: Firing rates in the top two firing rate sextiles were significantly reduced by the\n    intervening nonREM packet (both p < 0.01; Figure 5B , blue)\n  statistics:\n  - about: top two sextiles, MA n+1 against MA n\n    p: 0.01\n    p_relation: \"<\"\n  - about: log rate change against WAKE rate (Figure S5C)\n    statistic: R = -0.14923\n    p: 3.9886e-06\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - ma-statistics\n  criterion: Triplets MA, packet, MA by M6; per-sextile test by M6 readings. The S5C correlation is\n    Pearson of log(MA n+1 rate) minus log(MA n rate) against WAKE rate, one point per cell (M6);\n    the WAKE rate is plotted on a log axis, readings (a) log10 WAKE rate, (b) linear WAKE rate;\n    cells with zero rate in either MA are left out. Reproduced when both top sextiles decrease at\n    p < 0.01 and the S5C correlation is negative at p < 1e-5; partially reproduced when one of the\n    two parts holds.\n- id: figs5d-rem-nrem-rem\n  statement: For REM, packet, REM triplets the rate change is inversely correlated with rate.\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 2;\n    Figure S5D\n  quote: Analysis of rate change versus firing rate for these triplets also showed an inverse\n    correlation between rate and change ( Figure S5C ), as did a similar analysis for REM n - packet\n    - REM n+1 triplets ( Figure S5D )\n  statistics:\n  - statistic: R = -0.39537\n    p: 1.9003e-06\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  criterion: As in fig5b-ma-nrem-ma, for REM, packet, REM triplets (M6), one point per cell. Judged\n    by M4 with the S5D p as bound (p < 1e-5).\n- id: fig5c-sigma-ma-change\n  statement: Higher sigma power in the last 20 s of a packet goes with a larger increase of the\n    lowest sextile from the MA before to the MA after it.\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 2;\n    Figure 5C, lower right, and legend\n  quote: we found that sigma power in the last 20 seconds of nonREM packets was correlated with a\n    greater increase in the lowest firing-rate sextile group in the MA n versus MA n+1 analysis (\n    Figure 5C ; R = 0.181, p < 0.01)\n  statistics:\n  - statistic: R = 0.181\n    p: 0.01\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig5b-ma-nrem-ma\n  criterion: One point per MA, packet, MA triplet; the mean change of the lowest sextile's cells\n    against the packet's sigma (9 to 25 Hz) power in its last 20 s, z-scored per session as the\n    packet LFP metrics of Fig. 4C are (Results; the paper does not say how this sigma power is\n    normalized, so this is a choice), Pearson (the test is not named). Judged by M4.\n- id: fig5b-wake-between-packets\n  statement: WAKE between nonREM packets increases the rate of the fastest sextile; its decrease of\n    slow cells is not significant (24 triplets).\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 3;\n    Figure 5B, black; Figure S5E\n  quote: WAKE episodes increased the activity of the fastest-firing sextile group of pyramidal cells\n    from nonREM packet n to packet n+1 ( Figure 5B , black). ... WAKE also appeared to exert a\n    rate-decreasing effect on slow firing neurons, although this effect was not significant;\n    similarly, a correlation of rate versus log percent change was also not significant ( Figure S5E\n    ), possibly due to the small number of uninterrupted nonREM-WAKE-nonREM triplets (n = 24)\n  statistics:\n  - about: log rate change against WAKE rate (Figure S5E)\n    statistic: R = 0.043591\n    p: 0.2963\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  expected:\n    quantity: nonREM-WAKE-nonREM triplets\n    value: 24\n    tolerance: 2.4\n  criterion: Triplets packet, WAKE, packet by M6. \"WAKE\" between packets is not defined further;\n    readings (a) a scored WAKE interval (7+ min), (b) any arousal over 40 s (including the 40 to 120\n    s WAKE interruptions within SLEEP). Reproduced when under one reading the fastest sextile\n    increases (M6 test, p < 0.05) and the number of triplets is within tolerance. The absence of a\n    significant slow-cell change is judged on the same test at p < 0.05, and the S5E correlation\n    (one point per cell, M6) at p < 0.05; both are reported, and the claim is partially reproduced\n    when the fastest-sextile increase holds and either absence fails or the count misses.\n- id: fig5c-wake-movement\n  statement: WAKE periods with more movement have a larger effect on the rate increase of the\n    fastest sextile from one packet to the next (R = 0.43).\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 3;\n    Figure 5C, upper left, and legend\n  quote: Furthermore, WAKE periods with more movement had a proportionally larger effect ( Figure 5C\n    ; R = 0.43; p < 0.05)\n  statistics:\n  - about: movement during WAKE against fastest sextile change\n    statistic: R = 0.43\n    p: 0.05\n    p_relation: \"<\"\n    n: 24 nonREM-WAKE-nonREM triplets\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig5b-wake-between-packets\n  criterion: One point per packet, WAKE, packet triplet (readings of fig5b-wake-between-packets);\n    the fastest sextile's mean rate change against the \"degree of movement\" in the WAKE period (Fig.\n    5C legend). The movement measure is not defined; readings (a) the mean of the session's motion\n    signal over the WAKE period, (b) the fraction of the WAKE period with movement above the 5 SD\n    of nonREM threshold the Results use for WAKE, (c) the mean EMG score where a dataset has no\n    motion signal. Pearson (the test is not named). Judged by M4.\n- id: fig5b-ma-between-packets\n  statement: MAs between packets do not change fast-firing cells but increase the rate of\n    slow-firing cells, with an inverse relation between rate and change across cells.\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 3;\n    Figure 5B, yellow; Figure S5G\n  quote: In contrast to WAKE, MA epochs between packets did not affect fast-firing neurons but\n    significantly increased the rate of slow-firing neurons from packet n to packet n+1 ( Figure 5B ,\n    yellow). Again, the differential effect across sextiles was confirmed by a correlation analysis\n  statistics:\n  - about: log rate change against WAKE rate (Figure S5G)\n    statistic: R = -0.20668\n    p: 7.7388e-11\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - ma-statistics\n  criterion: Triplets packet, MA, packet by M6. \"Slow-firing\" read as (a) the lowest sextile, (b)\n    the lowest two. The absence for fast cells is judged on the same M6 test of the top sextile at\n    p < 0.05 (the asterisks of Fig. 5B mark significance; their threshold was not read). Reproduced\n    when under one reading the slow group increases (M6 test, p < 0.05), the top sextile does not\n    change at p < 0.05, and the S5G correlation (one point per cell) is negative at p < 1e-10;\n    partially reproduced when the slow-group increase holds.\n- id: fig5b-rem-between-packets\n  statement: REM between packets decreases the rates of all sextiles, by about the same\n    proportion, without a rate-dependent effect across cells.\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 3;\n    Figure 5B, red; Figure S5F\n  quote: Finally, REM episodes decreased the spike rates from packet n to packet n+1 in all sextile\n    groups ( Figure 5B , red). ... Correlational analysis did not reveal differential effects of REM\n    on neurons across the rate spectrum ( Figure S5F )\n  statistics:\n  - about: log rate change against WAKE rate (Figure S5F)\n    statistic: R = -0.038346\n    p: 0.2372\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  criterion: Triplets packet, REM, packet by M6, with the REM-end tolerance of the Supplemental\n    Experimental Procedures. All six sextiles show a decrease, each by the M6 test at p < 0.05. The\n    absence of a rate-dependent effect is judged on the paper's test, the S5F Pearson correlation\n    of log rate change against WAKE rate, one point per cell, at p < 0.05. Reproduced when both\n    hold under one M6 reading; partially reproduced when at least four of the six sextiles decrease\n    significantly and none increases.\n- id: fig5c-rem-duration\n  statement: Longer REM episodes produce a proportionally larger decrease of rates from one packet\n    to the next, across all sextiles (R = -0.22).\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 3;\n    Figure 5C, upper right, and legend\n  quote: Longer REM episodes exerted a proportionally larger effect on rate changes from packet n to\n    packet n+1 for all sextile groups ( Figure 5C ; R = – 0.22; p < 10 −2 ; t-test)\n  statistics:\n  - about: REM duration against rate change\n    test: t-test\n    statistic: R = -0.22\n    p: 0.01\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig5b-rem-between-packets\n  criterion: Triplets packet, REM, packet; REM duration against the rate drop \"across all cells\"\n    (Fig. 5C legend), Pearson with its t-test. \"Proportionally\" suggests a relative change, which\n    is not defined; readings (a) per triplet, the change of the mean rate over all pE cells; (b)\n    per triplet, the mean over cells of (rate n+1 minus rate n) over rate n, cells with rate n of 0\n    left out; (c) per cell and triplet, the log rate change of the S5 panels. Judged by M4.\n- id: fig5c-rem-theta\n  statement: REM theta power correlates with the packet n to packet n+1 rate decrease of the slowest\n    sextile only.\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 3\n  quote: REM theta power was significantly correlated with the packet n to packet n+1 rate decrease\n    of the slowest sextile group only (R = – 0.15; p < 0.05)\n  statistics:\n  - about: REM theta power against slowest sextile change\n    statistic: R = -0.15\n    p: 0.05\n    p_relation: \"<\"\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig5b-rem-between-packets\n  criterion: One point per packet, REM, packet triplet; each sextile's mean rate change against\n    REM theta power, Pearson. \"REM theta power\" is not defined; readings (a) the 5-10 Hz over 2-16\n    Hz theta ratio used for scoring (Supplemental Experimental Procedures), averaged over the REM\n    episode, (b) 5 to 10 Hz power averaged over the episode, z-scored per session. Reproduced when\n    under one reading the slowest sextile has negative R at p < 0.05 and no other sextile is\n    significant at p < 0.05; partially reproduced when the slowest-sextile correlation holds and\n    another sextile is also significant.\n- id: fig5c-delta-change-slow-cells\n  statement: Regardless of the intervening state, the increase of the slowest sextile from packet n\n    to n+1 correlates positively with the change in delta power between the packets; the same is not\n    found for the fastest sextile.\n  source: Results, Sleep sub-states induce differential lasting firing rate changes, paragraph 4;\n    Figure 5C, lower left, and legend\n  quote: The increase of spike rate from packet n to packet n+1 in the slowest sextile group was\n    positively correlated with the delta power change from packet n to packet n+1 ( Figure 5C )\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig4i-band-power-within-nrem\n  criterion: All consecutive packet pairs in SLEEP, whatever the intervening state; delta power\n    normalized within session (Fig. 5C legend, \"within-session normalized delta power\"; read as the\n    packet mean divided by the session's mean nonREM delta power, as in fig4-delta-packet-length);\n    one point per pair, Pearson (no test or R is given in the text). Reproduced when the slowest\n    sextile shows R > 0 at p < 0.05 and the fastest sextile does not at p < 0.05.\n- id: figs2d-interneurons-unchanged\n  statement: Unlike pyramidal cells, interneuron rates in the first and last packets of SLEEP lie\n    on a line of slope 1 (95% interval 0.996 to 1.005).\n  source: Figure S2D legend\n  quote: Comparison of log firing rates of individual putative interneurons during the first and\n    last packets of SLEEP. Unlike for pE cells (Figure 2B) the regression line is not different from\n    unity (slope 95% confidence interval ... 0.996-1.005)\n  statistics:\n  - ci:\n      level: 0.95\n      low: 0.996\n      high: 1.005\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - wake-sleep-cycles\n  expected:\n    quantity: pI slope, last on first packet\n    value: 1.0005\n    tolerance: 0.0045\n  criterion: M5 on pI cells (log rates, as the legend says). A claim of absence on the paper's\n    measure, the 95% interval of the slope; reproduced when the interval includes 1, and the slope\n    within tolerance is reported beside it; not reproduced when the interval excludes 1.\n- id: sleep-homogenizes-rates\n  statement: The net effect of sleep is to homogenize the firing rate distribution, fast cells\n    decreasing and slow cells increasing, so the population rate dispersion falls.\n  source: Discussion, paragraph 1; Figure 6 and legend\n  quote: During nonREM, activity of high firing rate neurons decreased, whereas activity of slow\n    firing neurons increased. REM sleep reduced firing rates relatively uniformly of all firing rate\n    groups, whereas microarousals, interspersed between nonREM epochs, increased the discharge rates\n    of slow firing neurons. Accordingly, the net result of sleep is that the firing rate variation\n    of the population is decreased\n  datasets:\n  - \"000041\"\n  - crcns-fcx-1\n  depends_on:\n  - fig3d-first-last-packet-slope\n  - fig3e-wake-before-after-sextiles\n  - cv-decreases-over-sleep\n  - fig5b-rem-between-packets\n  - fig5b-ma-between-packets\n  criterion: A summary of the claims it depends on. Reproduced when fig3d-first-last-packet-slope,\n    fig3e-wake-before-after-sextiles and cv-decreases-over-sleep are reproduced, and partially\n    reproduced when one or two of them are; the sub-state claims are reported beside it.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/watson-2016.yaml paper/10.1016-j.neuron.2016.03.036.txt 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent**

No quote problems. Now the style checks (em dashes, "rather", ": " inside plain scalars) and any schema validator.

**Agent calls Bash**

```bash
grep -n "—" claims/watson-2016.yaml; grep -n -i "rather" claims/watson-2016.yaml; python3 -c "
import yaml
with open('claims/watson-2016.yaml') as f:
    for ev in yaml.parse(f):
        if isinstance(ev, yaml.ScalarEvent) and ev.style is None and ': ' in ev.value:
            print(ev.start_mark.line+1, ev.value[:80])
"; ls tools/ | head -30
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
contributors.py
conversion_issue.py
datasets.py
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
ls tools/ | sed -n 30,80p; ls schemas 2>/dev/null
```

```
papers_manifest.py
progress.py
readme_row.py
replicates.py
runner
site_assets
social_card.html
stage_files.py
targets_diff.py
transcript.py
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
```

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/py python3 -c "
import yaml,json
try:
    import jsonschema
except ImportError:
    print('no jsonschema'); raise SystemExit
s=json.load(open('schemas/claims.schema.json'))
d=yaml.safe_load(open('claims/watson-2016.yaml'))
errs=list(jsonschema.Draft202012Validator(s).iter_errors(d))
for e in errs[:20]: print(list(e.path), e.message[:200])
print(len(errs),'errors')
" || pip install --target $TMPDIR/py jsonschema -q
```

```
0 errors
```

**Agent calls Bash**

```bash
python3 -c "
import yaml
d=yaml.safe_load(open('claims/watson-2016.yaml'))['claims']
print(len(d), sum('quote' in c for c in d), sum('statistics' in c for c in d), sum(len(c.get('statistics',[])) for c in d), sum('criterion' in c for c in d), sum('expected' in c for c in d))
print([c['id'] for c in d if 'criterion' not in c])
"; git status --short
```

```
53 52 33 58 53 20
[]
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
?? claims/watson-2016.yaml
?? scripts
```

**Agent**

I wrote `claims/watson-2016.yaml`, one file covering both datasets. The quote checker reports 53 claims, 52 quotes, 64 statistical values and 0 problems, and the file passes `schemas/claims.schema.json`. It is not committed, as asked.

**Text read.** I read the accepted author manuscript (PMC4873379, NIHMS776601), not the version of record. That covers the main text, Experimental Procedures, legends of Figs. 1 to 6, and supplement 1: Table S1, legends of Figs. S1 to S5, and the Supplemental Experimental Procedures. Supplement 2 holds only the Figure 1 artwork. I rendered one page of the supplement PDF (Fig. S5) to tie its printed R and p values to the right panels. The paper links no analysis code. Every claim lists both `000041` and `crcns-fcx-1`, since both archive descriptions say they hold the paper's full 27 sessions.

**Counts.**
- 53 claims; 52 have a quote. `tables1-state-durations` has an `inferred` note instead, because its values appear only in Table S1.
- 33 claims carry statistics, 58 entries in all. The checker's count of 64 also includes p-values.
- All 53 have a criterion; 20 have expected values.
- Ids come from the two earlier files. Where those files named the same finding differently, a mapping in the header lists the id kept and the one dropped.
- Two claims are new: `tables1-state-durations` and `fig4-late-packet-sigma-delta`.

**Details the paper leaves open, and the readings named for each:**
- **Sampling unit for correlations against normalized time:** one point per packet, per 10 s bin, or 50 bins averaged. I checked that the R and p printed in Fig. S5A/B match exactly 50 points. Fig. S3C matches about 873 points, roughly one per packet.
- **Cells in two WAKE-SLEEP cycles:** one entry per cell and episode, or one per cell averaged over episodes.
- **"General WAKE rate" for sextiles:** session-wide WAKE or each cycle's WAKE. For the rate groups of Fig. 2F: WAKE or nonREM sextiles.
- **Sextile numbering** runs in opposite directions in Fig. S2 (1 lowest) and the Fig. S5 legend (1 highest), so criteria name sextiles by rate.
- **"Wilcoxon test":** signed-rank or rank-sum.
- **Fig. 5B per-sextile test:** Wilcoxon signed-rank or t-test.
- **Fig. 4E within-UP comparison:** first against second third, or first against last third. The rank-sum unit is UP states or cells.
- **WAKE after SLEEP:** the next scored WAKE, or the >120 s arousal that ends SLEEP. **"WAKE" between packets:** scored WAKE, or any arousal over 40 s.
- **Definitions the paper never gives:**
  - The UP/DOWN ratio (duration ratio or time ratio).
  - REM theta power (scoring ratio or 5 to 10 Hz power).
  - The WAKE movement measure (motion mean, fraction above threshold, or EMG).
  - "Proportionally larger" for REM duration (three readings).
  - The final portion of a packet (last 20 s or last tenth).
  - Spindle "from ... to" (first and last tenth or third).
- **Autocorrelogram decay model:** power law to 100 or 500 ms, or exponential.
- **Synchrony per-cell measure:** firing together with another cell, or the cell's own firing fraction.
- **Range for "spans 0.05 to 5 Hz":** three percentile ranges.
- **Within-WAKE sextile trends:** the Pearson trend printed in Fig. S5A, or the change at entry to WAKE. The printed Fig. S5A values contradict the Results sentence.
- **Absences with no named test** are judged on the paper's correlation at p ≥ 0.05. Several tests the paper doesn't name use a standard choice, labelled as one.

**Inconsistencies inside the paper** (recorded in the claims, not fixed):
- Spindle incidence is 1.94/min in the Results but 0.049 Hz (2.94/min) in Table S1. The claim is judged on the Results value.
- The packet spindle-incidence R is printed as 0.7, read as a likely misprint for 0.07.
- The WAKE slope interval is printed as "0.801 – 0.0856"; the S3A legend's 0.80 to 0.86 is used.
- "0.05 to 5 Hz" is called three orders of magnitude.
- The "other" fraction is said to increase with R = −0.04.

**Missing from what was supplied.** There is no PDF of the main paper. Values printed only inside Figs. 2 to 5 could not be read:
- per-sextile R and p of Figs. 3B and 4A-B iv;
- the triplet n per class and the asterisks of Fig. 5B;
- the significance marks of Fig. 2F.

Those claims rest on the Results and legends. The Supplementary Methods that Fig. 2F cites for its significance test do not describe it.

## End of run

34 turns, 7 minutes, $3.17 at API prices, result: success.
