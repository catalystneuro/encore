# 001347 · claims-check · run 41394225953

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001347/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 100,200p docs/protocol.md; cat claims/001347/*.yaml; python tools/claims_check.py claims/001347/10.1126-science.adt3971.yaml paper/10.1126-science.adt3971.txt
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; cat paper/10.1126-science.adt3971.txt
```

Result: not kept, because it reads the paper's text.

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001347/10.1126-science.adt3971.yaml paper/10.1126-science.adt3971.txt 2>&1 | tail -40; wc -l claims/001347/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001347/10.1126-science.adt3971.yaml"
}
```

```
1	# Claims for Kauvar, Richman, Liu et al. (2025), Science 388, eadt3971, on dandiset 001347.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-02,
3	# protocol pilot-13 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (Science, 29 May 2025), main text with Materials and Methods,
6	# figure legends and references, and both supplement PDFs (the MDAR checklist, and the
7	# Supplementary Materials with Supplemental Note 1, the legends of figs. S1 to S38 and Tables S1
8	# to S3), all as extracted in paper/10.1126-science.adt3971.txt. No figure image could be
9	# rendered in this run, so every claim rests on the text and on Table S3. The body of Table S1
10	# (contacts with significant changes per HCP area) is garbled in the extraction and is not used.
11	# The variance-explained labels of Fig. 5G to 5I (0.954, 0.870, 0.927) are read from the
12	# extracted figure text; their assignment to panels is named as open in that claim.
13	#
14	# Code read:
15	# - Human electrophysiology and behaviour, and mouse behaviour (ref. 101): Zenodo record
16	#   14920570, kauvar-richman-liu-2025_zenodo.zip (md5 bd1fb567121aaf0291337783df57bcfc), a git
17	#   repository with one commit, b873ca5 ("First commit."). It loads its data from dandiset 001347.
18	#   Key scripts: human_ieeg/scripts/analyze_airpuff_p50.py (Fig. 1, fig. S1),
19	#   analyze_airpuff_ieeg_behavior_across_subjects.py (Fig. 2C and 2D, figs. S8 and S14G),
20	#   analyze_airpuff_ieeg_cd.py (Fig. 6C, 6E, 6G), analyze_airpuff_ieeg_sgram_load_allpt.py (Figs.
[... 687 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "offset": 708,
 "limit": 770
}
```

```
File content (26442 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent**

Checker reports one problem so far (a p-value 1.8e-09 not found for fig2i). Reading the rest of the claims file.

**Agent calls Read**

```json
{
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "offset": 708,
 "limit": 390
}
```

```
708	  source: Figure 3C and 3D; figs. S22 to S25; Table S1; Results, Brain-wide activity screen during
709	    emergence of affect in human beings, paragraph 8
710	  quote: These analyses consistently identified distinctive ketamine-elicited spectrotemporal
711	    pattern changes in the insular cortex (INS), cingulate cortex (ACC, MCC), orbitofrontal cortex
712	    (ORB), posteromedial cortex (PMC), supramarginal gyrus (SMG), motor cortex (MOT), and
713	    subcortical structures including the hippocampus (HIPP), basal ganglia (BG, primarily
714	    caudate), and thalamus (THAL)
715	  criterion: The method of fig3b applied to the 21 regions sampled in at least two participants,
716	    with the trial counts of Fig. 3C (ORB 151, IFG 175, MFG 61, INS 183, ACC 61, MCC 70, PMC 175,
717	    MOT 61, SS 61, SMG 153, PHG 102, STG 114, STS 102, MTG 214, ITG 120, TP 108, HIPP 214, BG
718	    151, AMY 105, THAL ANT 171, THAL POS 184). The listed set is drawn from several analyses
719	    (regions, Yeo17 networks, single channels). Readings, (a) each of INS, ACC, MCC, ORB, PMC,
720	    SMG, MOT, HIPP, BG and THAL (ANT or POS) is significant in the region test; (b) each is
721	    significant in the region test or has a channel significant in the single-channel test (the
722	    same test per channel, lowest cluster p Benjamini-Hochberg corrected across channels,
723	    significant below 0.05; Table S3, fig. S24). Reproduced when one reading holds for all ten
724	    and at least five of the other eleven regions are not significant; partially reproduced when
725	    it holds for seven to nine.
726	- id: figs27-slow-oscillations-with-strong-dissociation
727	  statement: All participants with strong dissociation (CADSS above 10) show ketamine-induced
[... 370 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "offset": 1097,
 "limit": 380
}
```

```
1097	  statement: In mice, late eye closure accumulates across a sequence of eight puffs and persists
1098	    after the last puff, with a Kaplan-Meier median survival of 15.16 s.
1099	  source: Figure 1M; fig. S2E and S2F; Table S3, fig. S2 E; Results, Precisely timed affective
1100	    behavior in mice and humans, paragraph 4
1101	  quote: late-phase eye closure in mice accumulated across a sequence of eyepuffs and decayed
1102	    slowly after the final eyepuff in the sequence (Fig. 1M), demonstrating persistence (fig.
1103	    S2E) and scalability (fig. S2, F and G)
1104	  expected:
1105	  - quantity: Kaplan-Meier median survival of eye closure after the final puff
1106	    value: 15.16
1107	    tolerance: 1.52
1108	    unit: s
1109	  criterion: From the code (fig1_persistence.py, lifelines KaplanMeierFitter) on the saline
1110	    sessions (5 mice, 20 trials each, 100 trials), raw eye closure; the eye is closed while above
1111	    1.2 times the trial's mean over its first 5 s; the time is from the start frame to the first
1112	    open frame, trials never reopening censored at 50 s. The code's start frame is 24.3 s into
1113	    the trial, 3.3 s after the eighth puff, while the figure axis reads "time from final puff";
1114	    readings, (a) the code's start, (b) 0.3 s after the eighth puff. Reproduced when, under one
1115	    reading, the pooled median is within tolerance and mean late eye closure (M-EYE) is higher on
1116	    the eighth puff than on the first.
[... 360 more lines not kept]
```

**Agent**

The file has 54 claims and is detailed. Now I'll check it against the paper text, starting with Table S3 entries, since most numbers come from there.

**Agent calls Bash**

```bash
cd paper; grep -n "Table S3\|=== page" 10.1126-science.adt3971.txt | grep -n "Table S3" | head; grep -n "Fig. 2I\|2I " 10.1126-science.adt3971.txt | head -30
```

```
25:3070:See Table S3 
26:3074:See Table S3 
28:3142:See Table S3 
93:7150:Table S3. 
814:followed by post infusion recovery (Fig. 2I). We analyzed changes in 
7436:Fig. 2I
```

**Agent calls Bash**

```bash
cd paper; wc -l 10.1126-science.adt3971.txt; sed -n 7150,7700p 10.1126-science.adt3971.txt
```

```
11601 10.1126-science.adt3971.txt
Table S3. 
Summary of statistical analyses 
Fig. 1D 
Analysis: Puff-triggered eye closure of an example human subject, averaged across trials, comparing saline and 
ketamine (0.5 mg/kg) conditions.  
5 
Condition 
# trials 
Plot 
Saline 
38 
Mean ± s.e.m. 
Ketamine 
38 
Mean ± s.e.m. 
Fig. 1E 
Analysis: Normalized late eye closure (late divided by early) in humans, saline vs. ketamine. Point estimates for 
each subject are mean ± s.e.m. across trials, excluding the first two trials. 
Null hypothesis: No difference between ketamine and saline conditions.  
[... 532 more lines not kept]
```

**Agent**

Checker's one flag (fig2i 1.8e-09) is a formatting mismatch: Table S3 prints "1.80e-09" for factor 1 post hoc. Now reading the Results sections.

**Agent calls Bash**

```bash
cd paper; grep -n "^RESULTS\|^Results\|Precisely timed\|Brain-wide activity screen during\|Conserved emotion-related\|^Discussion\|^DISCUSSION\|Materials and Methods\|^References" 10.1126-science.adt3971.txt | head -40
```

```
44:RESULTS: We determined that sequences of air puffs, directed at the 
198:Precisely timed affective behavior in mice and humans
541:Brain-wide activity screen during emergence of affect  
996:Brain-wide activity screen during emergence of affect in mice
1470:Conserved emotion-related population dynamics across 
1550:Discussion
1801:Materials and Methods
2880:References (60–104); MDAR Reproducibility Checklist
3276:References (60-104) 
3330:References: 
3358:References: 
3397:References: 
3421:References: 
3453:References: 
3488:References: 
3515:References: 
3539:References: 
11445:References
```

**Agent calls Bash**

```bash
cd paper; sed -n 198,1000p 10.1126-science.adt3971.txt | grep -v "^$"
```

```
<persisted-output>
Output too large (32.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/54866b92-7f59-4058-b368-9a7c4aeee639/tool-results/br1lh8u4t.txt

Preview (first 2KB):
Precisely timed affective behavior in mice and humans
We first sought to define a precise and quantifiable behavioral assay 
that would capture the fast-timescale onset of an emotional state, and 
that would be comparably controllable across species from humans to 
mice. We identified a puff of air directed at the cornea (eyepuff) as a 
candidate stimulus with critical features including clinical safety, temporal precision, and repeatability. Eyepuffs are innately aversive stimuli across species (18–21) and evoke broad cortical neural responses 
in mice (11); moreover, these stimuli are temporally delimited, precisely targeted, compatible with head-fixed neural recording, and safe 
to administer to human beings (forming part of standard ophthalmological assessment). Finally, the mammalian behavioral response to 
an eyepuff (eye closure) is fast, scalable, repeatable, easily scored in 
an automated manner, and similar between mice and humans; moreover, the neural circuitry governing eyepuff-triggered reflexive eyeblinks is well-mapped (22–25). We hypothesized that eyepuff stimuli of 
sufficient intensity and duration would evoke a behavioral response 
with fast reflexive but also persistent affective features, and that these 
features could manifest in temporally separable neural activity patterns. To test these hypotheses, we developed a protocol for administering eyepuffs to human participants or mice (Fig. 1) under conditions 
that would allow measurements of behavioral responses and brain-wide screens for neural responses, as well as intervention with medications, in both cases (figs. S1A, S2A, and S3).
Under control conditions (during intravenous saline administration) in human participants (Fig. 1A), we observed a multiphasic 
response to the eyepuf
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/54866b92-7f59-4058-b368-9a7c4aeee639/tool-results/br1lh8u4t.txt"
}
```

```
1	Precisely timed affective behavior in mice and humans
2	We first sought to define a precise and quantifiable behavioral assay 
3	that would capture the fast-timescale onset of an emotional state, and 
4	that would be comparably controllable across species from humans to 
5	mice. We identified a puff of air directed at the cornea (eyepuff) as a 
6	candidate stimulus with critical features including clinical safety, temporal precision, and repeatability. Eyepuffs are innately aversive stimuli across species (18–21) and evoke broad cortical neural responses 
7	in mice (11); moreover, these stimuli are temporally delimited, precisely targeted, compatible with head-fixed neural recording, and safe 
8	to administer to human beings (forming part of standard ophthalmological assessment). Finally, the mammalian behavioral response to 
9	an eyepuff (eye closure) is fast, scalable, repeatable, easily scored in 
10	an automated manner, and similar between mice and humans; moreover, the neural circuitry governing eyepuff-triggered reflexive eyeblinks is well-mapped (22–25). We hypothesized that eyepuff stimuli of 
11	sufficient intensity and duration would evoke a behavioral response 
12	with fast reflexive but also persistent affective features, and that these 
13	features could manifest in temporally separable neural activity patterns. To test these hypotheses, we developed a protocol for administering eyepuffs to human participants or mice (Fig. 1) under conditions 
14	that would allow measurements of behavioral responses and brain-wide screens for neural responses, as well as intervention with medications, in both cases (figs. S1A, S2A, and S3).
15	Under control conditions (during intravenous saline administration) in human participants (Fig. 1A), we observed a multiphasic 
16	response to the eyepuff (Fig. 1B), composed of a consistent and fast 
17	1Human Neural Circuitry program, Stanford University, Stanford, CA, USA. 2Department of Bioengineering, Stanford University, S
[... 782 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 996,1560p 10.1126-science.adt3971.txt | awk 'length($0)>40'
```

```
Brain-wide activity screen during emergence of affect in mice
To more deeply explore how neural dynamics immediately following eyepuffs may accumulate into longer-timescale emotional state 
changes, we took advantage of the species-spanning nature of the assay 
system to provide key complementary information through mouse 
experiments. In particular, although our work in human participants 
offers verbal reports of subjective experience during emotional states 
as well as direct observation of human neural dynamics, neural recordings in mice would further offer single-neuron spiking activity across 
the brain, as well as greater numbers and dynamic range of experimental trials of aversive stimuli. In the mouse eyepuff assay, we showed 
that trials of eight puffs in close succession pushed the animal into a 
persistent negative emotional state in a scalable manner (Fig. 1, J to 
L). We therefore sought to characterize in mice the brain-wide, single-neuron spiking activity in response to single eyepuffs, across a series 
of eyepuffs, and during decay of the affective behavior following an 
We performed acute high density extracellular electrophysiology 
with three to four simultaneously inserted Neuropixels probes in mice 
undergoing the eyepuff assay (Fig. 4A), in the presence or absence of 
ketamine administration by remote injection (fig. S2A). In response 
to eyepuffs, mice showed affective eye closure that was reduced by 
ketamine (Fig. 4B and fig. S28A) (as had occurred in our human participants that were likewise undergoing intracranial recording). We 
obtained recordings from many thousands of single units throughout 
the brain, with simultaneous recording of dozens of regions (Fig. 4C, 
[... 216 more lines not kept]
```

**Agent**

Results paragraph sources check out so far. Reading the remainder of Table S3.

**Agent calls Bash**

```bash
cd paper; sed -n 7700,11601p 10.1126-science.adt3971.txt | grep -n "^Fig\. \|^fig\. \|^Table\|^References" | head -80
```

```
13:Fig. 4E 
85:fig. S31 additionally shows post-infusion condition. Averages are baseline subtracted by average cluster activity 
237:Fig. 4H, I 
250:Fig. 5B 
268:Fig. 5D 
285:Fig. 5E 
336:Fig. 5G 
356:Fig. 5H, I 
393:Fig. 6C 
428:Fig. 6D 
472:Fig. 6E 
502:Fig. 6F 
547:Fig. 6G 
575:Fig. 6H 
604:Fig. 6I 
627:Fig. 6J 
658:fig. S1 B 
681:fig. S1 C 
710:fig. S1 D 
728:fig. S1 E 
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 7700,8370p 10.1126-science.adt3971.txt | grep -v "^Submitted Manuscript\|^Template revised\|^ $" | tr '\n' '|' | fold -w 4000
```

```
20 |10 |Ketamine |13 |10 |10 ||=== page 68 ===|68 |Fig. 4E |Analysis: Average cluster per-puff firing rate. Averages are baseline subtracted by average cluster activity 1s |prior to airpuff onset. Cluster labels obtained in Fig. 3D. Mean cluster activity is z-scored across the peri-puff |time window within cluster. Mean across all cells assigned to cluster, pooled across all datasets.  |Condition |# cells |# airpuffs |# sessions |# subjects |Cluster 0 |1070 |160 |13 |10 |Cluster 1 |832 |160 |13 |10 |Cluster 2 |803 |160 |13 |10 |Cluster 3 |663 |160 |13 |10 |Cluster 4 |639 |160 |13 |10 |Cluster 5 |597 |160 |13 |10 |Cluster 6 |547 |160 |13 |10 |Cluster 7 |508 |160 |13 |10 |Cluster 8 |473 |160 |13 |10 |Cluster 9 |344 |160 |13 |10 |Cluster 10 |317 |160 |13 |10 |Cluster 11 |176 |160 |13 |10 |Fig 4G, fig. S31 A |5 |Analysis: Average cluster per-puff firing rate compared between pre-infusion and ketamine infusion conditions. |fig. S31 additionally shows post-infusion condition. Averages are baseline subtracted by average cluster activity |1s prior to airpuff onset. Cluster labels obtained in Fig. 4D. Mean cluster activity is z-scored across the peri-puff |time window within cluster and condition. Mean across all cells assigned to cluster, pooled across all datasets. |Mean ± 95% confidence interval (1.96 * s.e.m.), with variability measured across all cells within cluster. |0 |Condition |# cells |# airpuffs |# sessions |# subjects |Cluster 0 - Pre |1070 |160 |13 |10 |Cluster 0 - Ketamine |64 |Cluster 0 - Post |64 |Cluster 1 - Pre |832 |160 |13 |10 |Cluster 1 - Ketamine |64 |Cluster 1 - Post |64 |Cluster 2 - Pre |803 |160 |13 |10 |Cluster 2 - Ketamine |64 |Cluster 2 - Post |64 |Cluster 3 - Pre |663 |160 |13 |10 |Cluster 3 - Ketamine |64 |Cluster 3 - Post |64 |Cluster 4 - Pre |639 |160 |13 |10 |Cluster 4 - Ketamine |64 |Cluster 4 - Post |64 |Cluster 5 - Pre |597 |160 |13 |10 |Cluster 5 - Ketamine |64 |Cluster 5 - Post |64 |Cluster 6 - Pre |547 |160 |13 |10 |Cluster 6 - Ketamin
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 8355,9250p 10.1126-science.adt3971.txt | grep -v "^Submitted Manuscript\|^Template revised\|^ $" | tr '\n' '|' | fold -w 4000
```

```
0.49 ± 0.07 |fig. S1 B |Analysis: Reflexive eye closure (sum of eye closure during 0.1 to 0.2 s after puff initiation), ketamine vs. saline. |Point estimates for each subject are mean ± s.e.m. across trials, excluding the first two trials. |0 |Null hypothesis: No difference between ketamine and saline conditions.  |Condition |# human participants |# trials per subject |Mean ± s.e.m. |Statistical test |Test statistic |p-Value |Saline |4 |38 |0.84 ± 0.01 |Paired t-test |1.622 |0.2032 |Ketamine |4 |38 |0.78 ± 0.04 |fig. S1 C |Analysis:  Affective eye closure (sum of eye closure during 0.3 to 0.8 s after puff initiation), ketamine vs. |saline. Point estimates for each subject are mean ± s.e.m. across trials, excluding the first two trials. ||=== page 73 ===|73 |Null hypothesis: No difference between ketamine and saline conditions.  |Condition |# human participants |# trials per subject |Mean ± s.e.m. |Statistical test |Test |statistic |p-Value |Saline |4 |38 |0.59 ± 0.07 |Paired t-test |3.653 |0.0354 |Ketamine |4 |38 |0.34 ± 0.10 |fig. S1 D |Analysis: Clinician administered dissociative states scale (CADSS), saline vs. ketamine.  |Null hypothesis: No difference between ketamine and saline conditions.  |Condition |# human participants |Mean ± s.e.m. |Statistical test |Test statistic |p-Value |Saline |4 |0.50 ± 0.29 |Paired t-test |7.034 |0.006 |Ketamine |4 |9.75 ± 1.25 |fig. S1 E |5 |Analysis: Puff-triggered eye closure of each human subject, averaged across trials excluding the first two trials, |comparing saline and ketamine conditions.  |Human subject |Condition |# trials |Plot |1 |Saline |38 |Mean ± s.e.m. |1 |Ketamine |38 |Mean ± s.e.m. |2 |Saline |38 |Mean ± s.e.m. |2 |Ketamine |38 |Mean ± s.e.m. |3 |Saline |38 |Mean ± s.e.m. |3 |Ketamine |38 |Mean ± s.e.m. |4 |Saline |38 |Mean ± s.e.m. |4 |Ketamine |38 |Mean ± s.e.m. |fig. S2 B |Analysis: Reflexive eye closure in mice during for first puff of each trial, saline vs. ketamine. |Null hypothesis: No difference between
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 9245,10100p 10.1126-science.adt3971.txt | grep -v "^Submitted Manuscript\|^Template revised\|^ $" | tr '\n' '|' | fold -w 4000
```

```
0.7475 |fig. S2 M |5 |Analysis: Average eye closure across trials (trials consist of 8 closely-spaced puffs),  averaged across mice, |comparing preinfusion conditions for three different airpuff pressures.  |Condition |# mice |# trials per mouse |Plot |8 PSI |8 |15 |mean ± s.e.m. |18 PSI |8 |15 |mean ± s.e.m. |28 PSI |8 |15 |mean ± s.e.m. |fig. S2 N |Analysis: Left, average eye closure across trials (trials consist of 8 closely-spaced puffs),  averaged across mice, |comparing preinfusion condition for male and female mice. |0 |Condition |# mice |# trials per mouse |Plot |Female |5 |15 |mean ± s.e.m. |Male |5 |15 |mean ± s.e.m. ||=== page 78 ===|78 |Analysis: Right, normalized affective eye closure for male and female mice for the eighth puff of each trial. |Paired t-test for within-subject comparisons, and independent t-test for across subject. |Null hypothesis: No difference between male and female mice.  |Condition |# |mice |# trials per |mouse |Mean ± |s.e.m. |Statistical test |Comparison |Test |statistic |Corrected p|Value |Male Pre-saline |5 |15 |0.44 ± 0.08 |T-test with fdr-bh |correction |Male Pre vs. Saline |1.080 |0.3827 |Male  |saline |5 |15 |0.57 ± 0.11 |Female Pre vs. Saline |0.980 |0.3827 |Female Pre|saline |5 |15 |0.66 ± 0.07 |Pre Male vs. Female |2.079 |0.2851 |Female saline |5 |15 |0.70 ± 0.09 |Saline Male vs. |Female |0.983 |0.3827 |fig. S2 O |Analysis: Average eye closure across trials (trials consist of 8 closely-spaced puffs),  averaged across mice, on |5 |trials in which either the 6th or 7th puff was skipped.  |Condition |# mice |# trials per mouse |Plot |Preinfusion skip 6th puff |5 |10 |mean ± s.e.m. |Infusion  |skip 6th puff |5 |10 |mean ± s.e.m. |Preinfusion skip 7th puff |5 |10 |mean ± s.e.m. |Infusion  |skip 7th puff |5 |10 |mean ± s.e.m. |fig. S5 A |Analysis: Average eye closure across trials (trials consist of 8 closely-spaced puffs),  averaged across mice, |comparing preinfusion and drug infusion conditions. |Condition |# mice |# trial
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 10100,10500p 10.1126-science.adt3971.txt | grep -v "^Submitted Manuscript\|^Template revised\|^ $" | tr '\n' '|' | fold -w 4000
```

```
Paired t-test with fdr-bh correction |Pre vs. Ketamine |10.5245 |4.09e-11 |Ketamine |0.21 ± 0.04 |Post vs. Ketamine |5.8804 |2.21e-06 |Postinfusion |0.53 ± 0.04 |SD185 |Preinfusion |31 |0.60 ± 0.03 |Paired t-test with fdr-bh correction |Pre vs. Ketamine |4.7462 |4.77e-05 |Ketamine |0.45 ± 0.03 |Post vs. Ketamine |6.8624 |2.58e-07 |Postinfusion |0.67 ± 0.02 |SD186 |Preinfusion |12 |0.54 ± 0.05 |Paired t-test with fdr-bh correction |Pre vs. Ketamine |2.7912 |0.0236 |Ketamine |0.35 ± 0.04 |Post vs. Ketamine |2.6265 |0.0236 |Postinfusion |0.55 ± 0.06 ||=== page 83 ===|83 |SD211 |Preinfusion |39 |0.31 ± 0.02 |Paired t-test with fdr-bh correction |Pre vs. Ketamine |7.1858 |1.38e-08 |Ketamine |0.15 ± 0.02 |Post vs. Ketamine |10.4531 |1.96e-12 |Postinfusion |0.36 ± 0.01 |SD245 |Preinfusion |39 |0.56 ± 0.02 |Paired t-test with fdr-bh correction |Pre vs. Ketamine |5.2553 |1.19e-05 |Ketamine |0.40 ± 0.02 |Post vs. Ketamine |2.9258 |0.0058 |Postinfusion |0.50 ± 0.02 |fig. S8 B |Analysis: Comparison of normalized affective eye closure during preinfusion, ketamine infusion, and |postinfusion for each human subject that did not meet the behavioral inclusion criteria. Affective eye closure is |normalized by the reflexive eye closure on each trial.  |Null hypothesis: No difference between infusion and preinfusion or postinfusion.  |5 |Subject |ID |Condition |# |trials |Mean ± |s.e.m. |Statistical test |Comparison |Test |statistic |Corrected p|Value |SD163 |Preinfusion |39 |0.67 ± 0.03 |Paired t-test with fdr-bh |correction |Pre vs. Ketamine |0.3794 |0.7065 |Ketamine |0.68 ± 0.03 |Post vs. |Ketamine |1.7575 |0.1738 |Postinfusion |0.78 ± 0.05 |SD170 |Preinfusion |39 |0.13 ± 0.03 |Paired t-test with fdr-bh |correction |Pre vs. Ketamine |0.1429 |0.8871 |Ketamine |0.12 ± 0.05 |Post vs. |Ketamine |1.1008 |0.5558 |Postinfusion |0.05 ± 0.03 |SD178 |Preinfusion |27 |0.93 ± 0.02 |Paired t-test with fdr-bh |correction |Pre vs. Ketamine |1.7376 |0.0941 |Ketamine |0.98 ± 0.02 |Post vs. |Ketamine
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 10500,11000p 10.1126-science.adt3971.txt | grep -v "^Submitted Manuscript\|^Template revised\|^ $" | tr '\n' '|' | fold -w 4000
```

```
Paired t-test with fdr-bh |correction |Pre. vs. Ket. |1.088 |0.318 |Ketamine |7 |7 |5 |1.83 ± 0.399 |Postinfusion |7 |7 |3 |1.56 ± 0.275 |Post vs. Ket. |1.438 |0.318 |fig. S34 E |Analysis: Left, peri-tone population activity along tone persistent dimension (difference between average |activity in the window [150 ms, 350 ms] and baseline). Mean ± 95% confidence interval (1.96 x s.e.m.). Right, |average tone persistent population activity during 350 ms to 500 ms after tone onset, comparing preinfusion, |5 |infusion, and postinfusion. Variation quantified across sessions, trials averaged per session per condition. |Null hypothesis: No difference between infusion and preinfusion or postinfusion. |Condition |# |subjects |# |sessions |# |trials |Mean ± |s.e.m. |Statistical test |Comparison |Test |statistic |Corrected p|Value |Preinfusion |7 |7 |10 |1.531 ± 0.081 |Paired t-test with fdr-bh |correction |Pre. vs. Ket. |6.942 |0.0009 |Ketamine |7 |7 |5 |0.392 ± 0.177 |Postinfusion |7 |7 |3 |1.385 ± 0.338 |Post vs. Ket. |–3.753 |0.009 |fig. S34 F |Analysis: Comparison of timecourse of detectability of activity along the persistent dimension for eyepuff vs. |0 |tone. Detectability is calculated as d-prime. Mean ± 95% CI.  |fig. S34 G |Analysis: Intrinsic timescale of tone persistent population activity during 30s preceding each tone series, during |preinfusion and infusion conditions. Statistics across session replicates. Values averaged within session across |trials for each condition. |5 |Null hypothesis: No difference between preinfusion and infusion conditions. |Condition |# subjects |# sessions |# trials |Mean ± s.e.m. |Statistical test |Comparison |Test statistic |p-Value |Preinfusion |7 |7 |10 |0.268 ± 0.037 |Paired t-test |Preinfusion vs. ketamine |5.479 |0.0015 |Ketamine |7 |7 |5 |0.089 ± 0.012 |fig. S34 H |Analysis: Pairwise correlation between tone persistent neurons (selected as neurons with greater than 90th |percentile weight in tone persistent population dimensio
[... 2 more lines not kept]
```

**Agent**

Found so far: figs37b omits the post-against-ketamine tests its criterion uses; fig6f lacks Table S3's means. Continuing with S38 and the Methods.

**Agent calls Bash**

```bash
cd paper; sed -n 11000,11445p 10.1126-science.adt3971.txt | grep -v "^Submitted Manuscript\|^Template revised\|^ $" | tr '\n' '|' | fold -w 4000
```

```
1.32 ± 0.08 |Paired t-test with fdr-bh |correction |Pre. vs. Ket. |6.252 |0.002 |Ketamine |7 |0.49 ± 0.17 |Postinfusion |7 |0.52 ± 0.14 |Post vs. Ket. |0.383 |0.715 |High Gamma  |(65-95 Hz) |Preinfusion |7 |0.90 ± 0.11 |Paired t-test with fdr-bh |correction |Pre. vs. Ket. |6.870 |0.001 |Ketamine |7 |0.27 ± 0.13 |Postinfusion |7 |0.39 ± 0.08 |Post vs. Ket. |1.189 |0.279 |Broadband LFP |Preinfusion |7 |1.66 ± 0.05 |Paired t-test with fdr-bh |correction |Pre. vs. Ket. |2.625 |0.079 |Ketamine |7 |1.37 ± 0.14 |Postinfusion |7 |1.49 ± 0.08 |Post vs. Ket. |0.790 |0.460 |fig. S38 A |Analysis: Mixed effects linear model, grouped by subject, of preinfusion phase locking ~ high vs. low CD edge |identity (categorical).   |Null hypothesis: No correlation between preinfusion phase locking and an edge’s identity as being between |high vs. low CD channels.  |5 |Frequency |band |# human |participants |# interchannel |edges |Statistical |test |Comparison |Coefficient |Confidence |interval 95% |R2 |Corrected |p-value |Delta  |(1-4 Hz) |7 |716 |Mixed-effects |linear model |with fdr-bh |correction |Low vs. High |0.0017 |[-0.005, 0.008] |1.3e-4 |0.76 |Theta  |(4-8 Hz) |7 |716 |Low vs. High |0.0026 |[-0.004, 0.009] |-7.4e-4 |0.76 |Alpha  |(8-12 Hz) |7 |716 |Low vs. High |0.0017 |[-0.006, 0.009] |-7.6e-4 |0.76 |Beta  |(12-30 Hz) |7 |716 |Low vs. High |0.0016 |[-0.005, 0.008] |-3.7e-4 |0.76 |Gamma  |(30-50 Hz) |7 |716 |Low vs. High |0.0018 |[-0.004, 0.007] |3.7e-4 |0.76 |High Gamma  |(65-95 Hz) |7 |716 |Low vs. High |-0.00060 |[-0.006, 0.005] |4.6e-5 |0.83 |fig. S38 B |Analysis: Mixed effects linear model, grouped by subject, of phase locking change on ketamine ~ high vs. low |CD edge identity (categorical).   |Null hypothesis: No correlation between ketamine-induced change in an edge’s phase locking and an edge’s |identity as being either high or low CD channels.  |0 |Frequency |band |# human |participants |# interchannel |edges |Statistical test |Comparison |Coefficient |Confidence |inter
[... 1 more lines not kept]
```

**Agent**

S38 entries match. Now spot-checking Methods details the criteria cite.

**Agent calls Bash**

```bash
cd paper; grep -n -i "first trial\|permutation\|n_permutations\|seed\|8 min\|eight min\|tenth percentile\|25 min\|1\.3\b\|d' \|d’ of\|threshold of\|0\.05 s immediately\|22 to 32\|34 to 40\|3 min\|FOOOF\|half-bandwidth\|80%\|40%\|10,000\|white matter" 10.1126-science.adt3971.txt | sed -n 1,80p
```

```
830:we performed an independent and complementary analysis: permutation cluster testing (Fig. 3A and Methods). Permutation cluster 
887:Permutation
923:Fig. 3. Selective disruption of human regional eyepuff-triggered dynamics by ketamine. (A) Schematic of permutation cluster test for identification of eyepuff-evoked 
949:neural dynamics, we performed permutation clustering both by region 
988:permutation cluster analysis, with similar outcomes using both methods) included fast-onset transient increases in separate bands of 
1835:the first trial of each session was excluded from analyses.
1984:gray and white matter surrounding a stereotactic electrode that has its 
1985:centroid either in neocortical gray or white matter. Voxel labels are 
1988:and white matter voxels in the cube are counted. If an electrode has 1 
2078:Permutation cluster test. Within each patient, channels were aggregated by each labeled region, and the mean spectrogram across 
2084:for each eyepuff session (preinfusion, infusion, post infusion). To identify changes in response during the infusion, a permutation clustered 
2085:one-sample t-test [mne.stats.permutation_cluster_1samp_test from 
2091:cluster forming threshold of 0.01 was used. The lowest (most significant) P-value in each region was further corrected for multiple comparisons across regions, using Benjamini-Hochberg False Discovery 
2111:preceding each puff and either an early (0.05 s immediately after each 
2133:section), for an eight minute time period immediately preceding onset 
2161:the top and bottom tenth percentile of sites per patient were classified 
2162:as high or low persistence, respectively, and white matter contacts 
2164:Preinfusion time windows of 25 minutes prior to the start of ketamine 
2168:be the final 25 minutes of the ketamine infusion, excluding periods of 
2201:spectral power outputs [time-half-bandwidth of 30, 59 tapers, window 
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 2060,2240p 10.1126-science.adt3971.txt
```

```
post  infusion), loadings were	 computed for each session based on test 
trials, using the factorization derived from pre- and post  infusion 
training trials. Infusion loadings were compared with the average of 
preinfusion and post  infusion loadings, using a mixed-effects linear 
model, grouped by patient, to identify significant changes in infusion 
loading. The anatomical distribution of each factor was computed 
by averaging the loadings of all channels within a region or Yeo7 
Downloaded from https://www.science.org at St Petersburg State University on May 31, 2025

=== page 15 ===
Research Article
Science 
29 May 2025
14 of 20
resting state network. For visualization, loadings within a region 
were normalized across the six factors. Regional change in loading was 
similarly computed using the average change in loading (infusion 
minus preinfusion) for all channels in a region.
Permutation cluster test. Within each patient, channels were aggregated by each labeled region, and the mean spectrogram across 
channels within a region was used as a regional spectrogram. Only 
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 2325,2345p 10.1126-science.adt3971.txt; echo ----; sed -n 2405,2600p 10.1126-science.adt3971.txt
```

```
Eyepuff assay with liquid reward available. In an alternative behavioral assay, mice were trained to freely collect a liquid caloric 
reward (Vanilla Ensure) from a lick spout. A small amount of Ensure 
was dispensed onto the tip of a spout approximately every 4.75 s (min 
4.5 s, average 4.75 s, max 5 s, with an exponential distribution of times 
between 4.5 s and 5 s). A small amount of Ensure was additionally 
delivered if mice licked the spout at any time, subject to a 0.5 s refractory period. Mice received two sequences of 8 eyepuffs (each 3 s 
apart) spaced by approximately 90 s. Licking was measured across 
the eyepuff sequence and lick probability per time bin was measured 
combining both trials within animal and averaging across animals (n = 6).
Drug infusion. Mice were C57BL/6J (Jackson Laboratory #664), between 8 to 20 weeks old, and predominantly female. For behavioral 
experiments without neural recording, intraperitoneal (IP) infusion was 
used. After 20 preinfusion trials had completed, the mouse was removed 
from head restraint, manually infused IP with a 32G needle, and head 
restrained again, at which point the post infusion trials commenced. 
Only trials occurring at least 3 minutes after the time of infusion were 
considered post infusion. The head restraint device was designed such 
that the animal’s location was identical with each head restraint. In 
many cases, the same mice were used for experiments with different 
drugs, with at least one full day of separation between experiments. For 
the baseline saline, ketamine (50 mg/kg), and PCP (20 mg/kg) experiments of Fig. 1, the same five mice were used for all conditions, with at 
[... 198 more lines not kept]
```

**Agent**

Mouse Methods match the criteria (Methods 1.3 vs Table S3 2 for d', epochs 22 to 32 and 34 to 40). Checking the supplementary legends next.

**Agent calls Bash**

```bash
cd paper; for f in "Fig. S1\." "Fig. S2\." "Fig. S4\." "Fig. S12\." "Fig. S13\." "Fig. S14\." "Fig. S15\." "Fig. S17\." "Fig. S19\." "Fig. S27\." "Fig. S33\." "Fig. S37\." "Fig. S38\." "Fig. S8\." "Fig. S6\." "Fig. S34\." "Fig. S35\."; do n=$(grep -n "^$f" 10.1126-science.adt3971.txt | head -1 | cut -d: -f1); echo "=== $f at $n"; sed -n "${n},$((n+22))p" 10.1126-science.adt3971.txt | awk 'length($0)>30' ; done
```

```
=== Fig. S1\. at 3560
Fig. S1. Additional details about eyepuff assay in humans. (A) Eyepuff protocol during infusion of ketamine or saline. 
During each session, a total of 40 air puffs are directed at the subject’s left cornea, with an inter-puff interval that varies 
Submitted Manuscript: Confidential 
Template revised November 2023 
between 3 to 8 s to prevent subjects from predicting the timing of each air puff. To reduce stress for the subject, there is a 
35 s interval after every eighth puff. To allow for direct comparison, the same inter-puff interval timing sequence was used 
in saline and infusion sessions and across subjects. For analysis, we do not include the first two trials in order to exclude an 
initial response that can differ from subsequent trials.  (B) Early eye closure (during 0.1 to 0.2 s after puff onset) does not 
change between saline and ketamine sessions (n=38 trials per subject, median ± 95% confidence interval). (C) Late eye 
closure (during 0.3 to 0.8 s after puff onset) decreases with ketamine relative to saline (n=38 trials per subject, median ± 
95% confidence interval). (D) Dissociation increases during ketamine, as measured using the Clinician-Administered 
Dissociative States Scale (CADSS). (E) Puff-triggered eye closure for each subject. top: summary, mean ± s.e.m across 
trials. middle: saline individual puffs, bottom: ketamine individual puffs. (F) Self-reported descriptions of subjective 
experience of eyepuffs during saline or ketamine. ns, P-value ≥ 0.05. *, P-value < 0.05. **, P-value < 0.01. ***, P-value < 
0.001. ****, P-value < 0.0001. See Supplementary table 3 for information on statistical analyses and sample sizes. 
=== Fig. S2\. at 3590
Fig. S2. Additional characterization of eyepuff assay in mice. (A) Eyepuff protocol with bolus drug infusion. Each trial 
consists of 8 air puffs with an inter-puff interval of 3 s. The inter-trial interval ranges from 50 to 70 s. Twenty trials are 
presented before infusion, and tw
[... 238 more lines not kept]
```

**Agent**

Legends agree with the criteria. Now checking the Fig. 5G to 5I labels and the Fig. 4G and 5D findings, which have no claims yet.

**Agent calls Bash**

```bash
cd paper; grep -n "0\.954\|0\.870\|0\.927\|Var\. exp\|variance explained\|R2 =" 10.1126-science.adt3971.txt | head; n=$(grep -n "0.954" 10.1126-science.adt3971.txt | head -1 | cut -d: -f1); sed -n "$((n-60)),$((n+40))p" 10.1126-science.adt3971.txt | tr '\n' '|'
```

```
1371:0.954
1406:0.870
1417:0.927
2622:Model variance explained. Variance explained was quantified as 
In summary, we have identified, measured, localized, and perturbed |mouse neural population activity that accumulates in response to |repeated aversive stimuli, scales with and persists with affective behavior corresponding to a negative emotional state, and closely corresponds in all these properties to a similar neurally and behaviorally |defined state in human participants. We also found that a two-phase |first order model robustly explains the neural dynamics of emotional |state in this assay. We demonstrated that a single variable modulating |timescale of state persistence substantially captures neural effects of |intervention in this system. This model is consistent with the per-puff |regional results of Fig. 4H, in which activity of most regions decays |more rapidly during ketamine. Quantitatively longer per-puff decay |timing in frontal and limbic regions suggests that these regions may |play a special role in the establishment and maintenance of the persistent-population affective-state evoked activity across puffs, which is widely |broadcast across most regions.|Neuron 1|Firing rate|Neuron 2|Activity|after series|Activity|before|series|Emotion-like|neural|dimension|Neuron n|+|+|Pre|Ketamine|ns|**|0–0.25s 2–3s|Time after first puff|0|1|2|3|Emotion-like|dimension activity|10 mg/kg|5 mg/kg|1 mg/kg|Model|PCP|35 mg/kg|25 mg/kg|13 mg/kg|Model|Ketamine|6 mg/kg|Model|0|20|40|60|Time (s)|0|1|2|Theoretical model|0.954|0|1|2|Emotion-like|dimension activity|Broadcast|Saturating input|Persistence|Time|State|Time|State|Time|Signal|Broadcast:|Persistence:|Remote ketamine injection|40 mins |-40 mins|~90 s|3 s|8 puffs|0|10|20|30|40|Time (s)|0.0|0.1|0.2|0.3|0.4|Affective eye closure|0.870|0|10|20|30|40|
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "old_string": "  statement: Factors 1 and 2 are reduced during ketamine and recover after infusion; factors 0, 4\n    and 5 are not significantly changed.",
 "new_string": "  statement: Factors 1 and 2 are reduced during ketamine and recover after infusion; in the\n    comparison of infusion with the mean of preinfusion and postinfusion, factors 0, 4 and 5 show\n    no significant change."
}
```

```
The file claims/001347/10.1126-science.adt3971.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "old_string": "    within tolerance, and factors 0, 4 and 5 are not significant; partially reproduced when\n    factors 1 and 2 hold but the means or the other factors do not.",
 "new_string": "    within tolerance, and factors 0, 4 and 5 are not significant in that infusion against mean of\n    preinfusion and postinfusion test; partially reproduced when factors 1 and 2 hold but the\n    means or the other factors do not. The post-hoc tests of Table S3 are significant for factors\n    0, 4 and 5 in some comparisons (factor 0 pre against infusion p = 0.036; factor 4 pre against\n    infusion p = 2.99e-04 and post against infusion p = 0.046; factor 5 pre against infusion\n    p = 0.010), so their absence is judged on the main test alone; the post-hoc results are\n    reported as well."
}
```

```
The file claims/001347/10.1126-science.adt3971.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "old_string": "  - {about: \"broadband pre against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 0.816\", p: 0.761, corrected: \"Benjamini-Hochberg\"}\n  criterion: A claim of absence",
 "new_string": "  - {about: \"broadband pre against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 0.816\", p: 0.761, corrected: \"Benjamini-Hochberg\"}\n  - {about: \"delta post against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 0.183\", p: 0.859, corrected: \"Benjamini-Hochberg\"}\n  - {about: \"theta post against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 0.428\", p: 0.793, corrected: \"Benjamini-Hochberg\"}\n  - {about: \"alpha post against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 0.703\", p: 0.508, corrected: \"Benjamini-Hochberg\"}\n  - {about: \"beta post against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 1.063\", p: 0.657, corrected: \"Benjamini-Hochberg\"}\n  - {about: \"gamma post against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 1.207\", p: 0.273, corrected: \"Benjamini-Hochberg\"}\n  - {about: \"high gamma post against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 0.371\", p: 0.960, corrected: \"Benjamini-Hochberg\"}\n  - {about: \"broadband post against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 0.319\", p: 0.761, corrected: \"Benjamini-Hochberg\"}\n  criterion: A claim of absence"
}
```

```
The file claims/001347/10.1126-science.adt3971.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "old_string": "  - {about: \"post against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 2.468\", p: 0.066, corrected: \"Benjamini-Hochberg\", n: \"11 sessions, 9 mice\"}\n  criterion: A claim of absence, judged on the paper's test, the fast dimension of the Methods\n    (target and quantification 0 to 70 ms) with the epochs of fig6d. Reproduced when both\n    corrected p >= 0.05.",
 "new_string": "  - {about: \"post against ketamine\", test: \"Paired t-test with fdr-bh correction\", statistic: \"t = 2.468\", p: 0.066, corrected: \"Benjamini-Hochberg\", n: \"11 sessions, 9 mice\"}\n  expected:\n  - {quantity: \"fast projection preinfusion\", value: 4.48, tolerance: 0.129}\n  - {quantity: \"fast projection ketamine\", value: 4.59, tolerance: 0.185}\n  - {quantity: \"fast projection postinfusion\", value: 4.32, tolerance: 0.184}\n  criterion: A claim of absence, judged on the paper's test, the fast dimension of the Methods\n    (target and quantification 0 to 70 ms) with the epochs of fig6d. Reproduced when both\n    corrected p >= 0.05; the means (tolerance the reported s.e.m.) and effect sizes are reported."
}
```

```
The file claims/001347/10.1126-science.adt3971.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "old_string": "5 s after the last puff against 750 ms ending 250 ms before the first puff; orthogonalised by\n    QR against the fast dimension from puffs 5 to 8); per-trial baseline",
 "new_string": "5 s after the last puff against 750 ms ending 250 ms before the first puff; orthogonalised by\n    QR against a fast dimension built from the 200 ms after against the 200 ms before each puff\n    onset in the saturation phase of the series, which the Methods call the \"last 4 trials\" and\n    which is read as puffs 5 to 8 of each series; open, the reading of the last 4 puff series\n    of the preinfusion epoch is shown as a variant); per-trial baseline"
}
```

```
The file claims/001347/10.1126-science.adt3971.yaml has been updated successfully.
```

**Agent**

Now adding the two missing claims after fig4hi.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "old_string": "    median rise-time change has an interval that includes zero.\n",
 "new_string": "    median rise-time change has an interval that includes zero.\n- id: fig4g-mouse-slow-clusters-altered\n  statement: Ketamine leaves neuron clusters with rapid preinfusion puff responses little changed\n    and substantially alters clusters with slower, more persistent responses.\n  source: Figure 4G; fig. S31A and S31C; Table S3, Fig 4G, fig. S31 A; Results, Brain-wide\n    activity screen during emergence of affect in mice, paragraph 5\n  quote: Clusters with more rapid preinfusion dynamics were minimally altered or unaltered by\n    ketamine, whereas clusters with slower and more persistent preinfusion dynamics were\n    substantially altered (Fig. 4G)\n  data: elsewhere\n  where: DANDI 001326\n  criterion: Clusters of puff-modulated neurons as in the Methods (Significant modulation;\n    Unsupervised clustering of peri-puff firing rates, Scanpy, 30 neighbours, 20 PCs, UMAP,\n    Leiden; 12 clusters from 13 sessions and 10 mice, Table S3, Fig. 4E). Per cluster, the\n    average per-puff firing rate before and during ketamine (trials as in fig6d), baseline\n    subtracted by the 1 s before the puff and z-scored within cluster and condition, mean and 95%\n    interval over cells (Table S3, Fig 4G). Clusters are ordered by the time of their preinfusion\n    average to decay to 25% of its peak (Methods, Cumulative fraction of cells in cluster by\n    region). The paper reports no test and no measure of change; a reading fixed here is the\n    fraction of the 0 to 2 s post-puff window in which the ketamine and preinfusion 95% intervals\n    do not overlap. Reproduced when this fraction has a positive Spearman correlation with the\n    preinfusion decay time across clusters and the mean fraction of the three slowest clusters\n    exceeds that of the three fastest. Cluster identities from a refit may differ from the\n    paper's numbering; the claim does not depend on the numbering.\n- id: fig5d-mouse-emotion-dimension-accumulates\n  statement: In mice, activity along the emotion-like dimension rises and saturates across the\n    eight-puff series and decays over tens of seconds after it; on ketamine it does not\n    accumulate.\n  source: Figure 5D; Table S3, Fig. 5D; Results, Brain-wide activity screen during emergence of\n    affect in mice, paragraph 6\n  quote: Measuring neural activity along this dimension revealed emotion-like properties of\n    scalability through a saturating rise across the series of eyepuffs and of persistence\n    through a decay lasting tens of seconds following each eyepuff series before returning to\n    baseline (Fig. 5D)\n  data: elsewhere\n  where: DANDI 001326\n  criterion: Emotion-like dimension as in fig5e (Methods, Emotion-like neural dimension), each\n    session projected on its own dimension, per-trial baseline the 250 ms before the first puff,\n    trials averaged within session, mean and 95% interval (1.96 s.e.m.) across 11 sessions from\n    9 mice, 20 preinfusion and 10 ketamine trials (Table S3, Fig. 5D; epochs as in fig6d). The\n    window used to build the dimension (5 to 6 s after the last puff onset) is left out, as in\n    the figure. The paper gives no test; a reading fixed here. Reproduced when, in preinfusion,\n    the mean activity in the 1 s before the eighth puff exceeds that in the 1 s before the second\n    puff, the activity 10 to 20 s after the last puff is above zero with its 95% interval\n    excluding zero, and, on ketamine, the activity in the 1 s before the eighth puff is not above\n    that before the second puff by more than its 95% interval.\n  depends_on:\n  - fig5e-mouse-emotion-dimension-late-reduced\n"
}
```

```
The file claims/001347/10.1126-science.adt3971.yaml has been updated successfully.
```

**Agent**

Adding two smaller notes: Table S3 labels fig. S2E's trials "Preinfusion", and the fig. S2B/C legend gives 18 trials where Table S3 gives 15.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "old_string": "  criterion: From the code (fig1_persistence.py, lifelines KaplanMeierFitter) on the saline\n    sessions (5 mice, 20 trials each, 100 trials), raw eye closure;",
 "new_string": "  criterion: From the code (fig1_persistence.py, lifelines KaplanMeierFitter) on the saline\n    sessions (5 mice, 20 trials each, 100 trials; Table S3, fig. S2 E, labels them\n    \"Preinfusion\", so the 20 trials before the injection are used), raw eye closure;"
}
```

```
The file claims/001347/10.1126-science.adt3971.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001347/10.1126-science.adt3971.yaml",
 "old_string": "  criterion: As fig1k, for early and for late eye closure separately. Reproduced when both tests",
 "new_string": "  criterion: As fig1k, for early and for late eye closure separately (Table S3 gives 15 trials\n    per mouse; the fig. S2B and S2C legends say 18, which is shown as a variant under Open I\n    reading b). Reproduced when both tests"
}
```

```
The file claims/001347/10.1126-science.adt3971.yaml has been updated successfully.
```

**Agent**

Checking how other claims files format the `checks` entry.

**Agent calls Bash**

```bash
cd  grep -rn -A8 "^checks:" claims/*/*.yaml | head -30
```

```
claims/000005/10.1038-nn.4412.yaml:1092:checks:
claims/000005/10.1038-nn.4412.yaml-1093-- date: 2026-10-20
claims/000005/10.1038-nn.4412.yaml-1094-  kind: agent
claims/000005/10.1038-nn.4412.yaml-1095-  model: claude-opus-5-5
claims/000005/10.1038-nn.4412.yaml-1096-  ready: true
claims/000005/10.1038-nn.4412.yaml-1097-  changes:
claims/000005/10.1038-nn.4412.yaml-1098-  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
claims/000005/10.1038-nn.4412.yaml-1099-  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
claims/000005/10.1038-nn.4412.yaml-1100-  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
--
claims/000006/10.1038-s41586-018-0642-9.yaml:841:checks:
claims/000006/10.1038-s41586-018-0642-9.yaml-842-- date: "2026-10-20"
claims/000006/10.1038-s41586-018-0642-9.yaml-843-  kind: agent
claims/000006/10.1038-s41586-018-0642-9.yaml-844-  model: claude-opus-5-5
claims/000006/10.1038-s41586-018-0642-9.yaml-845-  ready: true
claims/000006/10.1038-s41586-018-0642-9.yaml-846-  changes:
claims/000006/10.1038-s41586-018-0642-9.yaml-847-  - Opening comment. Added two code details read in Ephys.zip Code/ (Figshare doi:10.25378/janelia.7007846 v1),
claims/000006/10.1038-s41586-018-0642-9.yaml-848-    the zero weight of a neuron with rank-sum p of 1 in DirectionVector, and the epoch means taking time > start
claims/000006/10.1038-s41586-018-0642-9.yaml-849-    and <= end, unlike the CD windows.
--
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> claims/001347/10.1126-science.adt3971.yaml <<'EOF'
checks:
- date: 2026-11-02
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2i-ketamine-reduces-factors-1-2. The statement and criterion said factors 0, 4 and 5 are not significantly changed; Table S3's post-hoc tests are significant for all three in some comparison (factor 0 pre against infusion p = 0.036, factor 4 p = 2.99e-04 and 0.046, factor 5 p = 0.010). Limited the absence to the main test (infusion against the mean of pre and post) and had the post-hoc results reported.
  - fig2i-ketamine-reduces-factors-1-2. The checker flags p 1.8e-09 as not found; Table S3 prints it as 1.80e-09 (factor 1, pre against infusion). No change.
  - figs37b-fast-unchanged-across-bands. Added the seven post against ketamine tests of Table S3, fig. S37 B; the criterion judges the absence on both tests per band but only the pre against ketamine tests were recorded.
  - fig6f-mouse-fast-activity-unchanged. Added the three means of Table S3, Fig. 6F (4.48, 4.59, 4.32) as expected values with their s.e.m. as tolerance; they were missing.
  - fig5e-mouse-emotion-dimension-late-reduced. The criterion gave the orthogonalising fast dimension as built from puffs 5 to 8; the Methods say "saturation phase of the puff-series (last 4 trials)" with 200 ms windows. Added the windows and named the reading of "last 4 trials" as open, with the last four puff series shown as a variant.
  - fig4g-mouse-slow-clusters-altered. New claim. Fig. 4G and its Results sentence (slow clusters altered by ketamine, fast ones not) are a main finding with no claim. The paper gives no test or measure of change, so the measure is named as a reading fixed here.
  - fig5d-mouse-emotion-dimension-accumulates. New claim. The accumulation and tens-of-seconds persistence of the emotion-like dimension, absent on ketamine (Fig. 5D, Results), had no claim; fig5e covers the first puff only. The paper gives no test, so the windows compared are a reading fixed here.
  - fig1m-mouse-late-closure-accumulates-and-persists. Noted that Table S3, fig. S2 E, labels the 100 trials as preinfusion.
  - figs2bc-mouse-ketamine-early-present-late-abolished. Noted that the fig. S2B and S2C legends say 18 trials per mouse where Table S3 says 15.
  - Open, not settled. Fig. 5H and 5I variance explained (0.870, 0.927) cannot be assigned to ketamine and PCP from the text; fig5g keeps both assignments.
  - Open, not settled. Minor findings with no claim, left out as secondary - ketamine raising within-region correlations at rest (fig. S29, S30), the shorter persistence for the tone than the eyepuff (fig. S34F), and the regional cluster over-representation (fig. S31B).
  - Open, not settled. The code details cited (Zenodo 14920570 and 14876694) could not be checked in this run; they were taken as written.
EOF
python tools/claims_check.py claims/001347/10.1126-science.adt3971.yaml paper/10.1126-science.adt3971.txt 2>&1 | tail -8
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker's result line is: `claims/001347/10.1126-science.adt3971.yaml: 56 claims, 55 quotes, 195 statistical values, 1 problems`. That one problem is not a real error. It is fig2i's p-value 1.8e-09, which Table S3 prints as "1.80e-09" (factor 1, pre against infusion), so the value is in the paper.

**Changes, by claim**
- **fig2i-ketamine-reduces-factors-1-2:** the claim said factors 0, 4 and 5 are not significantly changed. That is true only for the main test (infusion against the mean of pre and post). Table S3's post-hoc tests are significant for all three (factor 0 p = 0.036; factor 4 p = 2.99e-04 and 0.046; factor 5 p = 0.010). I limited the statement and criterion to the main test, and the post-hoc results are now reported too.
- **figs37b-fast-unchanged-across-bands:** added the seven post-against-ketamine tests from Table S3. The criterion judges each band on both tests, but only the pre-against-ketamine tests had been recorded.
- **fig6f-mouse-fast-activity-unchanged:** added Table S3's means (4.48, 4.59, 4.32) as expected values, with the reported s.e.m. as tolerance.
- **fig5e-mouse-emotion-dimension-late-reduced:** the criterion said the fast dimension was built from "puffs 5 to 8". The Methods say "last 4 trials" with 200 ms windows. I added the windows, named the reading of "last 4 trials" as open, and added the other reading as a variant.
- **fig1m-mouse-late-closure-accumulates-and-persists:** noted that Table S3 labels the 100 trials "Preinfusion".
- **figs2bc-mouse-ketamine-early-present-late-abolished:** noted that the fig. S2B and S2C legends say 18 trials per mouse where Table S3 says 15.
- **New claim fig4g-mouse-slow-clusters-altered:** ketamine changes the slow neuron clusters but not the fast ones (Fig. 4G and its Results sentence). This main finding had no claim. The paper gives no test, so the measure of change is named as a reading fixed here.
- **New claim fig5d-mouse-emotion-dimension-accumulates:** activity along the emotion-like dimension builds up over the eight puffs, lasts tens of seconds, and does not build up on ketamine (Fig. 5D). This had no claim. The comparison windows are named as a reading fixed here.

Everything else matched the paper: the other Table S3 values, the Methods details I spot-checked (cluster test, coding dimension, timescale, phase locking, oscillation detection, mouse epochs, coding dimensions and d′ thresholds), the legends, the sources and the quotes.

**Still open**
- The Fig. 5H and 5I variance-explained values (0.870 and 0.927) can't be assigned to ketamine and PCP from the text, so fig5g keeps both assignments.
- I could not read the code the criteria cite (Zenodo 14920570 and 14876694) in this run, so those details are taken as the first reader wrote them.
- I left three minor findings without claims: ketamine raising within-region correlations at rest (figs. S29 and S30), shorter persistence for the tone than for the eyepuff (fig. S34F), and regional over-representation of clusters (fig. S31B).

**Ready:** yes. The `checks` entry at the end of the file records all of the above with `ready: true`. Only the claims file was changed, and nothing was committed.

## End of run

37 turns, 3 minutes, $2.39 at API prices, result: success.
