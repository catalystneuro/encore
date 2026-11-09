# 001603 · claims-check · run 39605601685

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001603/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; cat claims/001603/*.yaml
```

```
<persisted-output>
Output too large (73.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0fbcea67-7262-4758-917f-864669094595/tool-results/bhazmis8a.txt

Preview (first 2KB):
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; wc -l claims/001603/*.yaml paper/10.1038-s41593-025-02111-0.txt
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001603/10.1038-s41593-025-02111-0.yaml paper/10.1038-s41593-025-02111-0.txt
```

Result: not kept, because it reads the paper's text.

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml"
}
```

```
1	# Claims for van der Molen, Spaeth, Chini et al. (2025), "Preconfigured neuronal firing sequences in
2	# human brain organoids", Nature Neuroscience, doi:10.1038/s41593-025-02111-0, on dandiset 001603.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
4	# version pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read. The NIH author manuscript in PubMed Central (PMC12912721.1, NIHMS2139360), as served by
7	# NCBI PMC on 2026-10-20: main text, Methods, figure legends and Extended Data legends (Figs. 1 to 8),
8	# with the publisher's Supplementary Information PDF (41593_2025_2111_MOESM1_ESM.pdf; Supplementary
9	# Figures 1 to 27 and Supplementary Methods). Not the typeset version of record. Figures were not
10	# opened; every number below is from the text.
11	#
12	# Code read. https://github.com/braingeneers/Protosequences at commit e9a79c4 (2025-05-19), the
13	# repository named under Code Availability. It holds MATLAB scripts for the spike matrices, bursts,
14	# backbone units, firing rates, burst-to-burst and pairwise correlations, burst similarity and PCA
15	# (Main_analyses_matlab, process_data_backbone.m above all), the Python spike shuffling
16	# (shuffle_spike_mats.py), the HMM analysis in Python with SSM (HMM_analysis_python, with lmem.R for
17	# the HMM statistics), the burst clustering in Python (burst_clustering_analysis_python), the d2
18	# results and plotting (Criticality_analysis; the d2 code itself is downloaded from figshare article
19	# 25927081, Sooter et al.), plotting notebooks, and processed per-figure tables (Processed_data). The
20	# R scripts for the linear mixed-effects models of Figs. 2, 3, 6 and 7 are not in it.
[... 865 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "offset": 885
}
```

```
885	    test: two-sided linear mixed-effect model with sample as grouping variable
886	    p: 1.0e-20
887	    p_relation: "<"
888	    n: 31 samples
889	  - about: murine slices
890	    test: two-sided linear mixed-effect model with sample as grouping variable
891	    p: 7.0e-13
892	    n: 31 samples
893	  - about: primary cultures
894	    test: two-sided linear mixed-effect model with sample as grouping variable
895	    p: 1.0e-20
896	    p_relation: "<"
897	    n: 31 samples
898	  criterion: CV2 per unit as in Holt et al. (mean over consecutive interval pairs of 2|I2 - I1|/(I2 +
899	    I1)), units with at least 30 spikes. The panel does not say whether raw or shuffle z-scored CV2
900	    (Methods) is tested; readings (a) raw, (b) z-scored to the 100 shuffles. Model, CV2 on unit type,
901	    model type and their interaction with a random intercept per recording. Reproduced when non-rigid
902	    exceeds backbone with p < 0.05 in all four model types under both readings. (The paper prints
903	    "P ≤ 10-20"; p_relation "<" stands for it.)
904	- id: supp10b-rank-order-by-model
[... 180 more lines not kept]
```

**Agent**

The checker reports 0 problems across 48 claims. Next I'm reading the paper to check each claim against it.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-025-02111-0.txt",
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-025-02111-0.txt",
 "limit": 150
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Long lines; I'll view it via fold.

**Agent calls Bash**

```bash
fold -s -w 200 paper/10.1038-s41593-025-02111-0.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; grep -n -i "^results\|^methods\|^discussion\|Temporal dynamics of neuronal\|Backbone units are a highly\|Population firing rate timing\|Revealing temporal\|Endogenous sequences\|Comparing sequences\|Firing pattern stability" $TMPDIR/p.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 63,
 "limit": 110
}
```

```
63	that underlie the neural code 34 . Results Temporal dynamics of neuronal firing sequences in brain organoids Using high-density CMOS-based microelectrode arrays 22 , we investigated the temporal 
64	dynamics of spontaneous neuronal activity across guided and unguided human and mouse brain organoids. Single-unit spike events revealed population bursts lasting several hundred milliseconds, 
65	followed by quiescent periods up to several seconds ( Fig. 1A ). Moreover, we observed that the distribution of firing rates follows a heavy-tailed, right-skewed lognormal distribution ( n = 8, R 2 = 
66	0.97 ± 0.04, Extended Data Fig. 1A – C ). This represents one facet of functional activity conserved across brain regions and states in vivo 3 . Reordering single-units by the timing of their peak 
67	firing rate revealed sequential activation patterns during bursts ( Fig. 1B ). Bursts exhibited consistent rate profiles within organoids ( Fig. 1C ), with durations spanning timescales on the order 
68	of ≈ 10 2 milliseconds ( Fig. 1D , Supplementary Fig. 1 C ). A majority of units firing rates peaked in close proximity to the population burst maxima ( Fig. 1E ). These timescales align with 
69	spontaneous and evoked sequences in the murine 4 and reptile cortex 5 , as well as during memory retrieval in the human cortex 13 , 14 . Moreover, the dominant neuronal response time of sensory 
70	cortices peaks with similar constants across regions and species 30 , 35 , 36 , suggesting a conserved temporal motif in cortical computation. To assess stereotypy, we separated units into two 
71	classes. Backbone units were defined as those spiking in every burst ( Fig. 2A , above dashed line), all other units were defined as non-rigid (below dashed line). Backbone units, residing in the 
72	high-firing tail of the lognormal distribution ( Extended Data Fig. 1D ), displayed stable temporal delays across bursts ( Fig. 2B - C , Extended Data Fig. 2 ). Clustering bursts by their pairwise 
73	co
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -o -i "Burst detection\|Backbone units\b.\{0,40\}\|Comparing data from different sources\|Burst-to-burst\|Pairwise firing rate correlations\|Burst similarity score\|Statistical analysis\|Figure [0-9] \|Extended Data Fig. [0-9] \|Supplementary Fig. [0-9]* \|Code availability\|Data availability" $TMPDIR/p.txt | awk -F: '$1>172' | head -120
```

```
185:Extended Data Fig. 5 
192:backbone units increase in burst-to-burst correlation 
192:Supplementary Fig. 2 
194:Extended Data Fig. 4 
249:Comparing data from different sources
270:backbone units. For murine organoids and cortical slic
272:backbone units based on their median firing rate peak 
274:Burst-to-burst
278:burst-to-burst
279:burst-to-burst
280:burst-to-burst
281:Pairwise firing rate correlations
284:backbone units, pairs of one backbone and one non-rigi
286:backbone units, the lag time corresponding to the maxi
287:Burst similarity score
289:burst similarity score
291:burst similarity score
291:burst similarity score
291:backbone units and all 
292:burst similarity score
[... 87 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 173,
 "limit": 240
}
```

```
173	but were absent in two-dimensional murine cortical cultures where intrinsic anatomical organization is disrupted. Our results support the hypothesis that neuronal sequences are ‘preconfigured’ as an 
174	innate three-dimensional architecture established during neurodevelopment, arising independent of experience. To address the open questions above, we leveraged state-of-the-art high density 
175	extracellular recordings from three-dimensional stem cell derived models of the human and murine brain, known as brain organoids, which represent an intrinsically self-organized neuronal system that 
176	recapitulates key facets of early brain development 17 – 20 and the establishment of functional circuits 21 , 22 , 26 . Our results demonstrate that temporally rigid sequences represent a 
177	subpopulation that projects back onto a minority of strong functional connections with a lognormal distribution ( Fig. 3 ). In a seminal paper, Hopfield demonstrated that emergent computational 
178	properties from simple properties of many cells, rather than complex circuits, are capable of generalization and time sequence retention 44 . Therefore, it’s not surprising that the temporal 
179	structure of spontaneous and evoked patterns of cortical circuits are similar 45 , 46 , since such representations are drawn from a functionally connected neuronal pool with right-skewed, lognormal 
180	scaling rules 2 . Units that fire within neuronal sequences exhibit varying temporal precision. Neurons firing at the beginning of population bursts are most constrained, whereas later-firing units 
181	are more flexible ( Fig. 2F , G ). An analogous organization is present in rat somatosensory and auditory cortex 4 and the three-layered turtle cortex 5 . In the hippocampus, experience-dependent 
182	replay emerges from spontaneous, experience-independent preconfigured sequences 11 . The balance between temporally correlated and irregular spiking populations is essential for information 
183	pro
[... 229 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 480,
 "limit": 80
}
```

```
480	interval in which the population rate remains above 10% of its peak value in the burst. ( B ) Top, the instantaneous firing rate of single-unit activity from panel A . Bottom, zoomed in view of the 
481	neuronal firing during population bursts reveals temporal segregation and contiguous tiling of the peak firing rate of single-unit activity. Here the subset of units that fire at least two times 
482	during the burst are shown, re-ordered for each burst individually based on the time at which the unit has its maximum firing rate during the burst period. ( C ) The population firing rate (gray 
483	lines) is plotted relative to the burst peak for 46 burst events measured across a three-minute interval for the same organoid. The mean value is shown by the solid line and the dotted lines 
484	represent 1 STD. ( D ) Burst durations are plotted from four different organoids. ( E ) The distribution of single-unit firing rate peak times relative to population burst peaks for the same 
485	organoids as in D . Box plots (panels D–E): boxes span the 25th–75th percentiles; the center line marks the median (50th). Whiskers extend to the most extreme values within 1.5× the interquartile 
486	range from quartile 1 and quartile 3. In violin plots, minima and maxima equal the lowest and highest observations; the shaded area shows the variable’s probability density. Figure 2. Sequential 
487	activation patterns in human brain organoids generate a stereotyped temporal backbone. ( A ) Single-units were divided into backbone and non-rigid units. Backbone units, defined as spiking at least 
488	twice in every burst, are plotted above the dashed line; non-rigid units are below. Within each group, units are ordered by their median firing peak time relative to the burst peak across all bursts. 
489	( B ) Zoomed view of the backbone units across four bursts with the same unit order. (C) Average burst peak–centered firing rates from 46 burst events. Units maintain the same order A,B. Note 
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '560,760p' $TMPDIR/p.txt | cut -c1-200 | grep -n -i "supplementary fig\|figure [0-9]" | head -40
```

```
184:Supplementary Figures 1 to 27
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 743,
 "limit": 170
}
```

```
743	Supplementary Figures 1 to 27 
744	 
745	Supplementary Methods 
746	  
747	 
748	 
749	 
750	 
751	 
752	 
753	 
754	 
755	 
756	 
757	 
758	 
759	 
760	 
761	 
762	 
[... 150 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 912,
 "limit": 250
}
```

```
912	Sharf et al. (HO1), human organoids from Alam El Din et al. (HO5), murine organoids (MO1) 
913	and murine brain slices (M1S1) but not in murine primary cultures (Pr1). (B) Normalized 
914	Spearman rank order correlations comparing the sequential order of backbone sequences for all 
915	burst pairs over the recordings for the 4 different model types. Correlation scores are normalized 
916	relative to shuffled spike matrices such that values above 0 indicate a more consistent backbone 
917	sequence than the shuffled data (Main effect of sample type P = 0.004, Human organoids vs 
918	Murine Organoids P = 0.066, Human organoids vs Murine slices P = 0.061, Human organoids vs 
919	Murine primary cultures P = 0.0004, Murine organoids vs Murine slices P = 0.99, Murine 
920	organoids vs Murine primary culture P = 0.38, Murine slices vs Murine primary cultures P = 0.65, 
921	two-sided linear mixed-effect model with sample as grouping variable, n = 31 total samples). Box 
922	plots: boxes span the 25th–75th percentiles; the center line marks the median (50th). Whiskers 
923	extend to the most extreme values within 1.5× the interquartile range from quartile 1 and quartile 
924	3. In violin plots, minima and maxima equal the lowest and highest observations; the shaded area 
925	shows the variable’s probability density. 
926	 
927	 
928	
929	=== page 14 ===
930	 
931	Supplementary Figure 11. Correlation lag times. Lag times corresponding to the maximum 
[... 230 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 1161,
 "limit": 480
}
```

```
1161	Supplementary Figure 26. State traversal rate differs significantly between models. For each 
1162	hidden Markov model fitted to a given experiment, we averaged across bursts the number of 
1163	distinct hidden states traversed during the backbone interval (see Methods) divided by its duration. 
1164	The distributions appear substantially different, but not all are significant according to a linear 
1165	mixed-effects model given the large inter-sample effects. In particular, human and murine 
1166	organoid cannot be distinguished (P = 0.93), whereas the higher state traversal rate of murine 
1167	primary cultures is significantly different from that of human organoids (P = .021) and murine 
1168	acute slices (P < 0.0001) but not significant relative to murine organoids (P = 0.064). 
1169	 
1170	 
1171	 
1172	
1173	=== page 30 ===
1174	 
1175	Supplementary Figure 27. All preparations are capable of generating scale invariant 
1176	dynamics consistent with a near-critical regime. (A) The distance metric d2 quantifies how close 
1177	a system is to temporal criticality. Values of d2 between ~0.0-0.1 indicate near-critical dynamics 
1178	with temporal structure spanning multiple timescales. Random (shuffled) data typically yield d2 
1179	≥0.2. A subset of preparations from each model system generated activity well-described by the 
1180	autoregressive model underlying d2 calculation and exhibited near-critical dynamics (teal box 
[... 455 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "  statement: Lags of maximum cross-correlation between backbone units are longer in human and murine\n    organoids than in primary cultures, and longer in human organoids than in murine organoids or\n    slices.",
 "new_string": "  statement: Lags of maximum cross-correlation between backbone units are longer in human and murine\n    organoids than in primary cultures, and lags in human organoids differ from those in murine\n    organoids and in slices."
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "    contrasts. Reproduced when the four contrasts have the paper's direction with p < 0.05 under both\n    readings; partially reproduced when the two contrasts against primary cultures do.",
 "new_string": "    contrasts. The text gives the direction only for the contrasts against primary cultures (larger\n    in organoids); for human organoids against murine organoids and against slices it says only that\n    they differ, so either direction counts and the direction found is reported. Reproduced when the\n    two contrasts against primary cultures are larger in organoids and all four have p < 0.05, under\n    both readings; partially reproduced when the two contrasts against primary cultures hold."
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -o "In contrast, backbone units in organoids and neonatal.\{0,200\}" paper/10.1038-s41593-025-02111-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "  quote: After normalization relative to randomized data, backbone units remained significantly more\n    correlated than non-rigid units in organoids and slices ( P < 10 −10 and P = 7×10 −4 , linear\n    mixed-effects model)",
 "new_string": "  quote: backbone units in organoids and neonatal slices showed significantly stronger normalized\n    burst-to-burst single-unit firing correlations compared to primary cultures ( Fig. 7B ,\n    Supplementary Fig. 9 ). After normalization relative to randomized data, backbone units remained\n    significantly more correlated than non-rigid units in organoids and slices ( P < 10 −10 and P =\n    7×10 −4 , linear mixed-effects model)"
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "    reproduced when only the within-type contrasts hold. The Results and the legend print different\n    p-values for the same panel; both are recorded.",
 "new_string": "    reproduced when only the within-type contrasts hold. The Results and the legend print different\n    p-values for the same panel; both are recorded. Supplementary Fig. 9B describes the normalization\n    as subtracting the shuffle mean (A - B); that is shown as a variant, as for fig7e-pca-backbone-variance."
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "    are higher with p < 0.05 in both human and murine organoids. Pair-level values with a random\n    intercept per recording are a variant.",
 "new_string": "    are higher with p < 0.05 in both human and murine organoids. Pair-level values with a random\n    intercept per recording are a variant. Supplementary Fig. 12B describes the normalization as\n    subtracting the shuffle mean (A - B); that is shown as a variant."
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent**

Now fig7e (which comparison the legend's "differences" refers to) and supp8 (the non-rigid half of the finding).

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "    pca table; Supplementary Fig. 15 says the shuffle mean was subtracted, a variant). Model, value\n    on unit type (backbone, non-rigid), model type and their interaction with a random intercept per\n    recording. Reproduced when backbone exceeds non-rigid with p < 0.05 in human and murine organoids",
 "new_string": "    pca table; Supplementary Fig. 15 says the shuffle mean was subtracted, a variant). Model, value\n    on unit type, model type and their interaction with a random intercept per recording. The legend\n    plots all units, backbone and non-rigid and says only \"Differences were significant\", and the\n    Methods compare \"the three selections\", so which contrast is meant is open; readings (a)\n    backbone against non-rigid (unit types backbone and non-rigid), (b) backbone against all units\n    (all three selections in the model). Reproduced when backbone exceeds the comparison group with\n    p < 0.05 in human and murine organoids"
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "    the same test); partially reproduced when only the organoid contrasts hold. The Results also say",
 "new_string": "    the same test), under both readings; partially reproduced when only the organoid contrasts hold.\n    The Results also say"
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "    later, and backbone units keep more consistent firing patterns across the two recordings than\n    non-rigid units.",
 "new_string": "    later, units classed as non-rigid are mostly classed as non-rigid again, and backbone units keep\n    more consistent firing patterns across the two recordings than non-rigid units."
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "    example by joint sorting). Reproduced when more than half of the 0 h backbone units are backbone\n    at 4 h in both organoids, and the mean",
 "new_string": "    example by joint sorting). Reproduced when more than half of the 0 h backbone units are backbone\n    at 4 h and more than half of the 0 h non-rigid units are non-rigid at 4 h in both organoids, and\n    the mean"
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "    detected as backbone unit at time point 4-hour (top left) for both organoids\n  criterion: HO2",
 "new_string": "    detected as backbone unit at time point 4-hour (top left) for both organoids. Meanwhile, the\n    majority of units that were detected as non-rigid units at time point 0-hour were also detected\n    as non-rigid units at time point 4-hour (bottom right) for both organoids\n  criterion: HO2"
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "- id: fig4d-burst-similarity\n",
 "new_string": "- id: fig4c-similarity-variance\n  statement: The spread of burst similarity across pairs of bursts is high outside bursts, drops at\n    burst onset and stays low until the bursts end.\n  source: Results, Population firing rate timing across burst epochs, paragraph 1; Figure 4C\n  quote: \"Variance in similarity showed the opposite trend: it was high during non-bursting periods,\n    rapidly declining at burst onset, and remaining low until bursts ended ( Fig. 4C )\"\n  depends_on:\n  - fig1c-example-burst-count\n  criterion: Burst similarity over all units as in fig4d-burst-similarity, for every pair of bursts at\n    each frame from the earliest burst start to the latest burst end relative to the peak (Methods,\n    Burst similarity score); at each frame, the standard deviation over burst pairs (Fig. 4C legend).\n    Example organoid from fig1c-example-burst-count. No test is reported, and the paper does not say\n    which frames count as inside a burst; readings, inside is (a) from the median burst start to the\n    median burst end relative to the peak, (b) the backbone window. Reproduced when the mean standard\n    deviation over frames inside is lower than over the frames outside, under both readings. HO1 to\n    HO8 are reported.\n- id: fig4d-burst-similarity\n"
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "- id: supp10b-rank-order-by-model\n",
 "new_string": "- id: supp24d-backbone-non-poisson\n  statement: Given the HMM hidden state, non-rigid units fire mostly like Poisson units, while\n    backbone units fire less variably than Poisson in a sizable fraction of states.\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 4; Supplementary\n    Fig. 24D; Supplementary Methods, Non-Poisson Units\n  quote: Across models, non-rigid units were predominantly Poisson, while backbone units were\n    non-Poisson ( Supplementary Fig. 24 )\n  depends_on:\n  - fig7f-hmm-dimensionality\n  criterion: As the Supplementary Methods, Non-Poisson Units. HMMs as in fig7f-hmm-dimensionality (all\n    31 recordings, K from 10 to 30). For each unit, model and state, the spike counts of the unit in\n    the realizations of the state (bins where it is most probable); a one-sided chi-square test of\n    variance below the Poisson variance (the mean count) at the 1% level, using the standard statistic\n    (n - 1) s² / mean against chi-square with n - 1 degrees of freedom (the paper does not give the\n    statistic; a standard choice). Per unit, the fraction of states passing, weighted by realizations,\n    over all its fitted HMMs. No test of the group difference is reported. \"Sizable\" and \"almost all\n    states\" are not fixed; reproduced when, in every model type, the median fraction of backbone units\n    exceeds that of non-rigid units and the median fraction of non-rigid units is at most 0.1 (read\n    as at least 90% of states Poisson). The medians and a linear mixed-effects model of the fraction\n    on unit type with a random intercept per recording are reported.\n- id: supp10b-rank-order-by-model\n"
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent**

Now the `checks` entry. First I'm checking how other claims files format it.

**Agent calls Bash**

```bash
grep -l "^checks:" claims/*/*.yaml | head -1 | xargs -I{} sh -c 'sed -n "/^checks:/,\$p" {} | head -20'
```

```
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumption.
  - ion-cut-exc-no-touch. The post-touch Vm (Vm at the peak of the average PSP) is undefined without a PSP and biased upward on a flat average. The test now uses the paper's touch epoch (4 to 50 ms) against the 0 to 5 ms pre-touch mean, with the peak-based amplitude as a variant.
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion now says the test is reported and does not enter the outcome.
  - auc-weak-strong. The criterion compared groups on the Fig. 
[... 4 more lines not kept]
```

**Agent**

Before I write the checks entry, I'm trying the paper's code repository so I can verify the criteria that cite it.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/braingeneers/Protosequences && cd Protosequences && git log -1 --format='%h %ad' && ls
```

```
e9a79c4 Mon May 19 08:31:56 2025 +0200
Criticality_analysis
HMM_analysis_python
Main_analyses_matlab
Plotting_notebooks_python
Processed_data
README.md
burst_clustering_analysis_python
Shell cwd was reset to
```

**Agent**

The clone worked (commit e9a79c4). Spot-checking the code details the criteria cite.

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences; grep -rn "MinPeakDistance\|smoothdata\|0\.7\b\|>= *0\.3\|bonf\|alpha" Main_analyses_matlab/process_data_backbone.m | head -30; grep -rn "KEEP_DURATION" --include=*.py . | head -5; grep -rn "SGDClassifier\|LeaveOneOut" --include=*.py . | head; ls HMM_analysis_python
```

```
44:square_smooth_summed_spike = smoothdata(sum(t_spk_mat, 2),'movmean',SQUARE_WIDTH);
47:pop_rate = smoothdata(square_smooth_summed_spike,'gaussian',GAUSS_SIGMA);
53:[peak_amp, peaks] = findpeaks(pop_rate, 'MinPeakHeight', pop_rms*THR_BURST, 'MinPeakDistance', MIN_BURST_DIFF);
62:square_smooth_summed_spike_acc = smoothdata(sum(t_spk_mat, 2),'movmean',SQUARE_WIDTH_ACC);
65:pop_rate_acc = smoothdata(square_smooth_summed_spike_acc,'gaussian',GAUSS_SIGMA_ACC);
424:            rate_mat(:,unit,c) = 1000*smoothdata(isi_rate_temp_result,'gaussian',GAUSS_SIGMA);
./HMM_analysis_python/hmmsupport.py:362:        if duration := KEEP_DURATION.get(experiment):
./HMM_analysis_python/hmmsupport.py:773:KEEP_DURATION = {exp: 600e3 if exp in _long_exps else 180e3 for exp in ALL_EXPERIMENTS}
./HMM_analysis_python/Fig5.py:11:from sklearn.linear_model import SGDClassifier
./HMM_analysis_python/Fig5.py:12:from sklearn.model_selection import LeaveOneOut, cross_validate
./HMM_analysis_python/Fig5.py:71:    cv = LeaveOneOut()
./HMM_analysis_python/Fig5.py:72:    clf = make_pipeline(StandardScaler(), SGDClassifier())
Dockerfile
Fig5.py
Supplements.py
cv_worker.py
do_cv.py
fit_hmms.py
hmm_worker.py
hmmsupport.py
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences; grep -n "MIN_BURST_DIFF\s*=\|THR_BURST\s*=\|GAUSS_SIGMA\s*=\|SQUARE_WIDTH\s*=\|0\.7\|0\.8\|0\.9\|ttest\|0\.05" Main_analyses_matlab/process_data_backbone.m | head -30; cat HMM_analysis_python/lmem.R | head -80
```

```
34:THR_BURST = 4; % threshold for population peak detection
35:MIN_BURST_DIFF = 800; % minimum time between bursts (ms)
36:SQUARE_WIDTH = 20; % square window size for coarse population rate
37:GAUSS_SIGMA = 100; % gaussian window size for coarse population rate
library('dplyr')
library('lme4')
library('lmerTest')
library('emmeans')

dimensions <- read.csv("dimensions.csv")
dsub = dimensions[dimensions$theta == 0.75, ]
# Make a LMEM of this current subset of the data.
sample_type <- factor(dsub$sample_type)
sample_id <- factor(dsub$sample_id)
model <- glmer(dsub$dims ~ sample_type + (1 | sample_id), family=poisson(link="log"))
emmeans(model, pairwise ~ sample_type)

df <- do.call(rbind, lapply(split(dimensions, dimensions$theta), function(dsub) {
		# Make a LMEM of this current subset of the data.
		sample_type <- factor(dsub$sample_type)
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences; grep -rn -i "bonferroni\|0\.05/\|/ *size\|ttest" Main_analyses_matlab/*.m | head -10; grep -rn "0\.7\b\|0\.3\b\|>= *0\.[0-9]\|BACKBONE\|backbone_thr\|bb_thr" Main_analyses_matlab/process_data_backbone.m | head -20; grep -n "chi2\|def .*poisson\|n_components\|theta\|range(1, *1" HMM_analysis_python/Supplements.py HMM_analysis_python/hmmsupport.py | head -30
```

```
Main_analyses_matlab/plot_single_rec_figs_backbone.m:721:        [sig_scores(frame), pval] = ttest(frame_data_comp1(logical(tril(ones(size(frame_data_comp1)),-1))), ...
Main_analyses_matlab/plot_single_rec_figs_backbone.m:722:            frame_data_comp2(logical(tril(ones(size(frame_data_comp2)),-1))), "Alpha", 0.05/length(above_thresh_i));        
Main_analyses_matlab/plot_single_rec_figs_backbone.m:988:    [~,p] = ttest(reshape(thresh_cos_sim(1,:,:,frame),1,[]), reshape(thresh_cos_sim(end,:,:,frame),1,[]));
Main_analyses_matlab/process_data_backbone.m:139:frac_per_unit = sum(above_thresh, 2)/size(edges,1);
Main_analyses_matlab/process_data_backbone.m:140:frac_per_burst = sum(above_thresh, 1)/size(t_spk_mat,2);
228:MIN_BURST_FRAC = 0.3;
HMM_analysis_python/Supplements.py:115:def poisson_test(data):
HMM_analysis_python/Supplements.py:133:    return stats.chi2(dof).cdf(statistic)
HMM_analysis_python/Supplements.py:200:            theta=theta,
HMM_analysis_python/Supplements.py:207:        for theta in np.linspace(0.5, 1, num=51)
HMM_analysis_python/Supplements.py:210:            components_required(exp, theta),
HMM_analysis_python/Supplements.py:211:            components_required(exp, theta, rsm=True),
HMM_analysis_python/Supplements.py:218:dreq_df[dreq_df.theta == 0.75].to_csv("dimensions_0.75.csv", index=False)
HMM_analysis_python/Supplements.py:387:    sns.lineplot(data=pval_df, x="theta", y="p.value", hue="contrast", ax=B)
HMM_analysis_python/Supplements.py:391:    B.set_xlabel(r"Threshold $\theta$ (Percent Explained Variance)")
Shell cwd was reset to
```

**Agent**

The code has `MIN_BURST_FRAC = 0.3`, but fig2e says the code uses 70%. Checking that and the non-Poisson test.

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences; sed -n 215,275p Main_analyses_matlab/process_data_backbone.m; grep -n "MIN_BURST_FRAC\|frac_per_unit\|backbone_units\s*=\|bb_units\|== *1\b" Main_analyses_matlab/process_data_backbone.m | head -20; sed -n 110,175p HMM_analysis_python/Supplements.py
```

```
[~,sort_i_mean_scaf] = sort(max_i_mean_scaf);
[~,sort_i_mean_non_scaf] = sort(max_i_mean_non_scaf);

% store results
mean_rate_ordering = fliplr([sort_i_mean_scaf(1:length(scaf_units)), sort_i_mean_non_scaf(1:length(non_scaf_units))]);
   

%% compute correlation scores burst to burst

% set parameters
MAXLAG_BTB = 10;
WINDOW = [250,500];
MIN_SPIKES = 2;
MIN_BURST_FRAC = 0.3;

% compute burst to burst correlations for normal data
[all_btb_corr_scores, av_btb_corr_scores] = compute_burst_to_burst_corr(rate_mat_burst_only, ...
    t_spk_mat_burst_only, tburst, MAXLAG_BTB, WINDOW, MIN_SPIKES, MIN_BURST_FRAC);
 
% compute burst to burst correlations for randomized data
[... 119 more lines not kept]
```

**Agent**

The code uses 0.3, matching the Methods, so I'm checking whether 0.7 appears anywhere. I'm also reading the rest of the non-Poisson code, which limits states to bins inside bursts.

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences; grep -rn "0\.7\b\|= *0\.7\|70" Main_analyses_matlab/compute_burst_to_burst_corr.m Main_analyses_matlab/*.m 2>/dev/null | grep -v "^.*%.*70" | head; ls Main_analyses_matlab; sed -n 175,195p HMM_analysis_python/Supplements.py
```

```
Main_analyses_matlab/plot_multi_rec_figs_backbone.m:500:set(fig, 'Position', [100 100 800 700])
Main_analyses_matlab/plot_multi_rec_rand_figs_backbone.m:127:set(fig, 'Position', [100 100 1400 700])
Main_analyses_matlab/plot_multi_rec_rand_figs_backbone.m:479:set(fig, 'Position', [100 100 1800 700])
Main_analyses_matlab/plot_single_rec_figs_backbone.m:22:PLOT_RANGE = [197000,207000];%[48000, 63500]; % select range for example plot in ms 
Main_analyses_matlab/plot_single_rec_figs_backbone.m:466:set(fig, 'Position', [0 20 700 300])
plot_develomental_analysis.m
plot_multi_rec_figs_backbone.m
plot_multi_rec_rand_figs_backbone.m
plot_single_rec_figs_backbone.m
plot_time_diff_analysis.m
preprocess_ks.m
process_data_backbone.m
shuffle_spike_mats.py
    # consistent", i.e. potentially Poisson, then invert.
    return np.ma.average(scores < 0.01, axis=0, weights=nobs)


consistency_df = pd.DataFrame(
    [
        dict(
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences; n=$(grep -n "function \[all_btb_corr_scores" Main_analyses_matlab/process_data_backbone.m | cut -d: -f1); sed -n "${n},$((n+45))p" Main_analyses_matlab/process_data_backbone.m; grep -n "FRAC_THRESH\s*=" -A3 Main_analyses_matlab/process_data_backbone.m
```

```
sed: -e expression #1, char 1: unknown command: `,'
112:FRAC_THRESH = 1; % define minimum fraction of bursts
113-
114-% initiate result cell array
115-spikes_per_burst = zeros(size(t_spk_mat,2), size(edges,1));
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences; grep -rn "compute_burst_to_burst_corr" . | grep function; grep -rn "min_burst_frac\|MIN_BURST_FRAC" -i . | head
```

```
./Main_analyses_matlab/process_data_backbone.m:487:function [all_burst_corr_scores, av_burst_corr_scores] = compute_burst_to_burst_corr(rate_mat, ...
./Main_analyses_matlab/process_data_backbone.m:228:MIN_BURST_FRAC = 0.3;
./Main_analyses_matlab/process_data_backbone.m:232:    t_spk_mat_burst_only, tburst, MAXLAG_BTB, WINDOW, MIN_SPIKES, MIN_BURST_FRAC);
./Main_analyses_matlab/process_data_backbone.m:236:    t_spk_mat_burst_only_all_shuf, tburst, MAXLAG_BTB, WINDOW, MIN_SPIKES, MIN_BURST_FRAC);
./Main_analyses_matlab/plot_time_diff_analysis.m:68:MIN_BURST_FRAC = 0.3;
./Main_analyses_matlab/plot_time_diff_analysis.m:83:    % set values with frac_per_unit smaller than MIN_BURST_FRAC to NaN
./Main_analyses_matlab/plot_time_diff_analysis.m:84:    unit_mask = frac_per_unit{array,1} < MIN_BURST_FRAC | frac_per_unit{array,2} < MIN_BURST_FRAC;
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences; sed -n 487,540p Main_analyses_matlab/process_data_backbone.m
```

```
function [all_burst_corr_scores, av_burst_corr_scores] = compute_burst_to_burst_corr(rate_mat, ...
    t_spk_mat, tburst, MAXLAG, WINDOW, MIN_SPIKES, MIN_FRAC)
 
% make empty result matrices
av_burst_corr_scores = NaN(1,size(rate_mat,2), size(rate_mat,3));
all_burst_corr_scores = NaN(size(rate_mat,2), length(tburst),length(tburst),size(rate_mat,3));

% for each copy
for c = 1:size(rate_mat,3)
    
    % for each unit
    for unit = 1:size(rate_mat,2)

        % make list of comparison bursts
        comp_bursts = 1:length(tburst);

        % set counter to 0
        counter = 0;

        % for each reference burst
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences; sed -n 540,575p Main_analyses_matlab/process_data_backbone.m
```

```
% cut out firing rate for burst
                comp_rate = rate_mat(tburst(comp_bursts(comp_b))-WINDOW(1):tburst(comp_bursts(comp_b))+WINDOW(2), unit, c);

                % compute cross correlation
                [r, ~] = xcorr(ref_rate, comp_rate, MAXLAG, 'coeff');

                % obtain maximum correlation
                [max_corr, ~] = max(r);

                % store results
                all_burst_corr_scores(unit, comp_bursts(comp_b), ref_b, c) = max_corr;

            end % comp_b
        end % ref_b

        % if more than MIN_FRAC bursts had at least 2 spikes
        if counter/length(tburst) <= MIN_FRAC

            % select pairs
            to_average = all_burst_corr_scores(unit,:,:, c);
[... 17 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "old_string": "  criterion: As the Supplementary Methods, Non-Poisson Units. HMMs as in fig7f-hmm-dimensionality (all\n    31 recordings, K from 10 to 30). For each unit, model and state, the spike counts of the unit in\n    the realizations of the state (bins where it is most probable); a one-sided chi-square test of\n    variance below the Poisson variance (the mean count) at the 1% level, using the standard statistic\n    (n - 1) s² / mean against chi-square with n - 1 degrees of freedom (the paper does not give the\n    statistic; a standard choice). Per unit, the fraction of states passing, weighted by realizations,\n    over all its fitted HMMs. No test of the group difference is reported.",
 "new_string": "  criterion: As the Supplementary Methods, Non-Poisson Units, and Supplements.py (poisson_test,\n    unit_consistency, mean_consistency). HMMs as in fig7f-hmm-dimensionality (all 31 recordings, K\n    from 10 to 30). For each unit, model and state, the spike counts of the unit in the realizations\n    of the state (bins where it is the most likely state; the code keeps only bins inside burst\n    windows); a one-sided chi-square test of variance below the Poisson variance (the mean count) at\n    the 1% level, statistic (n - 1) s² / mean against the lower tail of chi-square with n - 1 degrees\n    of freedom (code). A unit that never fires in a state counts as Poisson there (code). Per unit,\n    the fraction of states passing, weighted by their numbers of realizations, over all its fitted\n    HMMs. No test of the group difference is reported."
}
```

```
The file claims/001603/10.1038-s41593-025-02111-0.yaml has been updated successfully.
```

**Agent**

Spot-checks of the code agree with the file. Now adding the checks entry and rerunning the checker.

**Agent calls Bash**

```bash
cat >> claims/001603/10.1038-s41593-025-02111-0.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig7d-lag-times. The statement said human organoid lags are longer than those of murine organoids and slices; the Fig. 7D legend says only that they differ, and the Results give a direction only against primary cultures. The statement now says "differ", and the criterion accepts either direction for those two contrasts and reports it.
  - fig7b-normalized-b2b. The quote did not hold the Results sentence for the second half of the statement (organoid and slice backbone units above primary cultures); added it. Named the shuffle-mean subtraction of Supplementary Fig. 9B as a variant, as fig7e-pca-backbone-variance does for Supplementary Fig. 15.
  - fig7c-normalized-pairwise. Named the shuffle-mean subtraction of Supplementary Fig. 12B as a variant, for the same reason.
  - fig7e-pca-backbone-variance. The criterion compared backbone with non-rigid units only; the legend plots all units, backbone and non-rigid and says only "Differences were significant", and the Methods compare "the three selections". Named readings (a) backbone against non-rigid and (b) backbone against all units.
  - supp8-backbone-stable-4h. Added the legend's second finding (most 0 h non-rigid units are non-rigid at 4 h) to the statement, quote and criterion, so the statement says no less than the panel.
  - Added claim fig4c-similarity-variance (Fig. 4C, the spread of burst similarity drops during bursts), a Results finding with no claim. No test or bound for "inside a burst" is given; the criterion names two readings.
  - Added claim supp24d-backbone-non-poisson (non-rigid units Poisson and backbone units non-Poisson given the HMM state, Results paragraph 4 of the model comparison and Supplementary Fig. 24D), a Results finding with no claim. Method from the Supplementary Methods and Supplements.py; the bounds for "sizable" and "almost all states" are not given, and the criterion names the reading it uses.
  - Checked against the code at e9a79c4 (cloned for this check). The 800 ms peak distance, the 0.3 burst fraction of compute_burst_to_burst_corr (units with at least 2 spikes in at least 70% of bursts), the Bonferroni alpha of the burst similarity t-tests, KEEP_DURATION, the SGDClassifier with leave-one-out, and the glmer and traversal models of lmem.R are as the file states.
  - Open. ed4b-nbqx-cpp-abolish-bursts reads "bursting disappears" as at most one burst per treated recording; the paper gives no count, and zero bursts is the stricter reading.
  - Open. fig5d-backbone-more-states. The paper reports no test and does not define the "pool" of states; the 0.5 consistency bound and the mixed-effects model with a random intercept for K are the reader's readings, not the paper's.
  - Open. fig7a-backbone-higher-rate. The Fig. 7A legend gives 1048 units for both human organoids and primary cultures, possibly a typo; it cannot be settled from the paper.
EOF
python tools/claims_check.py claims/001603/10.1038-s41593-025-02111-0.yaml paper/10.1038-s41593-025-02111-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes. Last, I'm checking that no plain scalar contains ": " and that there are no em dashes or "rather".

**Agent calls Bash**

```bash
f=claims/001603/10.1038-s41593-025-02111-0.yaml; python -c "import yaml;d=yaml.safe_load(open('$f'));print(len(d['claims']), d['checks'][-1]['ready'])"; grep -n "—\|rather" $f; grep -nE "^\s+[^#\"].*[^:]: " $f | grep -vE "^\s*[0-9]+:\s+(- )?[a-z_]+: " | head; git status --short
```

```
50 True
780:    cultures (human organoid vs primary: P = 1 × 10 −8 ; murine organoids vs primary: P = 0.011),
 M claims/001603/10.1038-s41593-025-02111-0.yaml
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

**Agent**

The claims file for DANDI:001603 is ready for an attempt (`ready: true`). Nothing was committed or pushed.

**Checker:** `50 claims, 50 quotes, 71 statistical values, 0 problems` (it was 48 claims before I added two).

I read the whole paper, including the Methods, all figure legends and the supplement. I also cloned the paper's code (Protosequences at e9a79c4) to check the details the file says come from the code. Those checks all agree with the file, including the 70% unit rule in fig2e, which I first thought was wrong.

**Changes, by claim:**
- **fig7d-lag-times:** the statement said human organoid lags are *longer* than in murine organoids and slices. The paper only says they *differ*, so the statement now says "differ" and the criterion accepts either direction for those two contrasts.
- **fig7b-normalized-b2b:** the quote now includes the Results sentence behind the "organoids and slices above primary cultures" half of the statement. Supplementary Fig. 9B describes the normalization differently from the Methods (subtracting the shuffle mean); that is now a variant.
- **fig7c-normalized-pairwise:** the same subtraction variant, from Supplementary Fig. 12B.
- **fig7e-pca-backbone-variance:** the legend's "Differences were significant" does not say which groups are compared. The criterion now has two readings: backbone against non-rigid units, and backbone against all units.
- **supp8-backbone-stable-4h:** added the legend's second finding (most non-rigid units are still non-rigid 4 h later) to the statement, quote and criterion.
- **New claim fig4c-similarity-variance:** a finding stated in the Results that had no claim. The paper does not say which frames count as inside a burst, so the criterion names two readings.
- **New claim supp24d-backbone-non-poisson:** a finding stated in the Results that had no claim. The method comes from the Supplementary Methods and the code.

**Still open (recorded under `checks`):**
- **ed4b-nbqx-cpp-abolish-bursts:** "bursting disappears" is read as at most one burst per recording; zero would be the stricter reading.
- **fig5d-backbone-more-states:** the paper reports no test and does not define the "pool" of states. The 0.5 bound and the random effect for the number of states are the claims writer's choices, not the paper's.
- **fig7a-backbone-higher-rate:** the legend gives 1048 units for both human organoids and primary cultures, possibly a typo that the paper cannot settle.

## End of run

45 turns, 4 minutes, result: success.
