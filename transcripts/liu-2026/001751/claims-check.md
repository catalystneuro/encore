# 001751 · claims-check · run 39565351430

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001751/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md; python tools/claims_check.py claims/001751/*.yaml paper/*.txt; cat claims/001751/*.yaml; wc paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/8d6e7f04-f9ec-4096-a1e5-184e48cb2617/tool-results/bjyw16zba.txt"
}
```

```
1	## Reader
2	
3	### 1. Get the paper
4	
5	The workflow puts the paper's full text, and its PDF where there is one, under
6	`paper/`: the main text, the Methods, and the supplement. Read the text; open
7	the PDF only to read a figure or a table the text garbles. If the full text is
8	not there, or lacks the Methods or a supplement the results rest on, stop:
9	write no claims, and end with a report that names what is missing, so that it
10	can be supplied. Never write claims from the abstract. Do not copy figures.
11	Do not look at the dataset's data: its title and description on the archive
12	are enough to know which paper and which experiments it is meant to hold.
13	
14	### 2. Read the paper's code
15	
16	Read the code the paper links to before writing criteria. Say what it holds,
17	and record the repository and commit read. Where the Methods leave a choice
18	open and the code settles it, follow the code and say so. Where they disagree,
19	follow the Methods for the main result and name the code's choice as a
20	variant. When more sources disagree (the Methods, the analysis code, the
[... 832 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "connectivity profile\|1,292\|multi-patch\|Fig. 5\|Figure 5\|soma distance" *.txt | cut -c1-200
```

```
7:981 npgopen Nature Cell Biology Nat Cell Biol PMC13457102 13457102 13457102 42393360 10.1038/s41556-026-02009-4 An atlas of primate insular cortex reveals a signal-processing strategy in von Economo
446:                    The anterior insular cortex (AIC) is a critical hub integrating exteroceptive and interoceptive information into high-order cognition, yet its neural basis remains incompletely
```

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)}' *.txt | sort -t: -k2 -n -r | head; grep -o -i ".\{300\}1,292.\{2500\}" *.txt
```

```
7: 160162
446: 640
450: 544
593: 285
577: 285
565: 258
261: 253
290: 249
675: 247
641: 247
proach combining (1) scRNA-seq (122,663 cells) to recover transcriptomes from isolated whole cells; (2) Patch-seq (578 neurons) to simultaneously capture morphological, electrophysiological and transcriptomic profiles of individual neurons; and (3) eight-channel simultaneous patch-clamp recordings (1,292 potential local connectivity pairs among 377 neurons) (Fig. 1a ). Fig. 1 Cellular taxonomy of the macaque anterior insular cortex and transcriptomic mapping of Patch-seq neurons. a , Experimental paradigm of our scRNA-seq and Patch-seq approaches to study the macaque AIC. The crossed dashed lines label the ear bar zero (EBZ). The vertical black lines on the brain schematic indicate the anterior–posterior position (anterior 23–28 to EBZ) of sample collection and coronal slices from the insular cortex. b , UMAP visualization of all scRNA-seq cells. Excitatory (Exc) and inhibitory (Inh) neuron types are coloured greenish and reddish, respectively. Sequencing data were collected from seven animals ( n = 7), and this sample size applies to all whole-cell-sequencing datasets collected in this study. Endo, endothelial cells; Astro, astrocytes. c , Pie chart illustrating the percentages of transcriptomic cell types revealed by scRNA-seq. d , The expression level similarity within cell classes across primate species. See Extended Data Fig. 2d for detailed labelling of species names. e , UMAP visualization of neurons from the scRNA-seq dataset. Colours represent neuron types consistent with those in b . Patch-seq neurons are shown as bigger markers and are transcriptomically assigned to the neuronal atlas. f , Example morphologies coloured by cell types (top). Axons of excitatory and inhibitory neurons are depicted in grey and reddish colours, respectively. Dendrites of excitatory and inhibitory neurons are in greenish and black colours, respectively. Electrophysiological firing pattern
[... 1 more lines not kept]
```

**Agent**

Checker passes (33 claims, 0 problems). Now reading the paper text against each claim.

**Agent calls Bash**

```bash
cd paper; sed -n 7p *.txt | fold -w 4000 > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; grep -o -i "This analysis identified six.\{1500\}" *.txt
```

```
41 /tmp/claude-1001/p.txt
This analysis identified six synaptic connections between L5 PCs and INs (PC-to-IN, 2 of 65 and IN-to-PC, 4 of 65, 107.0 ± 60.1 μm). However, no synaptic connections were found between VENs and INs (VEN-to-IN, 0 of 55 and IN-to-VEN, 0 of 55, 97.4 ± 36.8 μm). These findings suggest that VENs follow a distinct connectivity pattern characterized by sparse synaptic interactions with local neuronal circuits compared with PCs (Fig. 5i ). This result aligns with fewer spines in VENs than in PCs 60 , suggesting that they act as specialized conduits for transferring specific, integrated information over long distance. Multimodal profiling of two VEN subtypes As a region-specific innovation, VEN depletion has been observed in psychiatric diseases, such as autism, callosal agenesis and schizophrenia, which are often characterized by severe impairments in empathy, social awareness, and self-control 30 , 61 – 64 . Leveraging Patch-seq recording, we multimodally profiled the late evolutionary-emergent neurons 39 , 53 . Our detailed morphological reconstructions revealed morphological diversity among VENs, notably in their prominent basal dendrites (Fig. 6a,b ). Some VENs are characterized by a long, prominent basal dendrite (VEN-L), which often exceeds 500 µm into the deep part of layer 6b, yielding a nearly symmetric morphology relative to the apical dendrite. Conversely, other VENs possess a short, prominent basal dendrite (VEN-S) that abruptly terminates into thin branches extending horizontally or laterally downw
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "seeman\|37349\|Multi-patch\|multipatch\|simultaneous whole-cell\|uEPSP\|unitary\|0.01" *.txt | cut -c1-300; grep -o -i ".\{200\}uIPSP.\{1500\}" *.txt
```

```
7:981 npgopen Nature Cell Biology Nat Cell Biol PMC13457102 13457102 13457102 42393360 10.1038/s41556-026-02009-4 An atlas of primate insular cortex reveals a signal-processing strategy in von Economo neurons Liu Rui-Feng 1 # Huang Mengyao 1 # Shen Yuhui 1 # Shao Mingting 1 # Jing Junzhan 2 3 # Xu N
121:10.1152/physiol.00019.2022
148:10.1007/s00401-018-1942-8
153:20801106
173:10.1016/j.pnpbp.2018.10.015
212:10.7554/eLife.37349
215:Seeman, S. C. et al. Sparse recurrent excitatory connectivity in the microcircuit of the adult mouse and human cortex. eLife7, e37349 (2018).
252:10.1097/WCO.0b013e3283168e2d
256:10.1007/s00401-010-0673-2
259:10.1007/s00401-009-0568-2
262:10.1007/s00401-008-0434-7
398:10.1084/jem.20030167
497:[23] Prilutski, Y. & Livneh, Y. Physiological needs: sensations and predictions in the insular cortex. Physiology 38, 73–81 (2023). 10.1152/physiol.00019.2022
513:[31] Nana, A. L. et al. Neurons selectively targeted in frontotemporal dementia reveal early stage TDP-43 pathobiology. Acta Neuropathol. 137, 27–46 (2019). 10.1007/s00401-018-1942-8
527:[38] Nomi, J. S., Molnar-Szakacs, I. & Uddin, L. Q. Insular function in autism: Update and future directions in neuroimaging and interventions. Prog. Neuropsychopharmacol. Biol. Psychiatry 89, 412–426 (2019). 10.1016/j.pnpbp.2018.10.015
551:[50] Seeman, S. C. et al. Sparse recurrent excitatory connectivity in the microcircuit of the adult mouse and human cortex. eLife 7, e37349 (2018). 10.7554/eLife.37349
573:[61] Seeley, W. W. Selective functional, regional, and neuronal vulnerability in frontotemporal dementia. Curr. Opin. Neurol. 21, 701–707 (2008). 10.1097/WCO.0b013e3283168e2d
575:[62] Brüne, M. et al. Von Economo neuron density in the anterior cingulate cortex is reduced in early onset schizophrenia. Acta Neuropathol. 119, 771–778 (2010). 10.1007/s00401-010-0673-2
577:[63] Simms, M. L., Kemper, T. L., Timbie, C. M., Bauman, M. L. & Blatt, G. J. The anterior cingulate cortex in autism: heterogeneity of q
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i ".\{1800\}ms at 0.01–0.1 Hz" *.txt; grep -o -i "monosynaptic.\{300\}" *.txt | head; grep -o -i "\(averaged\|average\) .\{200\}" *.txt | head -20
```

```
monosynaptic connections among AIC neurons (Fig. 5d ). In total, we tested 1,292 potential connections from an additional set of 377 neurons in layer 5b and confirmed 31 monosynaptic connections. Each recorded neuron was identified as VEN or PC by physiological properties and post hoc morphology staining (Fig. 
monosynaptic connections with other PCs in 24 out of 503 tested pairs (Supplementary Table 5 ), a connectivity rate comparable with previously reported for L5 PCs in the primate brain 50 . These connections spanned a wide range of soma distances (111.8 ± 61.2 μm, mean± s.d.). In contrast, VENs did not form syna
Monosynaptic eEPSPs were defined as those with amplitudes that monotonically increased with stimulation current and with constant response latencies. In this study, only monosynaptic eEPSPs recorded from paired VENs and PCs were analysed. The recorded polysynaptic responses and those with AP evoked were exclude
Average expression levels of cell-type marker genes across primate brain regions. The top left panel presents the current data and the other three panels reproduce the visualization of multiple primates’ data
average gene expression levels and were colour-coded. The gene expression within each cell classes/subclasses correlated well across brain regions, while the cross-species correlation patterns are different b
averaged of 2–30 neurons except for the rightmost one with n = 1). Data are shown as mean ± s.e.m. Two-tailed Student’s t -test, P < 0.0001 for slope. j , Comparison of eEPSPs in VENs and PCs to electrical sti
average response (>20 replications) from potential postsynaptic cells. The black arrows indicate the evoked EPSPs in cell 6. Scale bar, 10 nA for I inj , 100 mV for spikes and 1 mV for unitary EPSPs. g , Simi
average log counts) and the phenotypic distance (Euclidean distance between average feature vectors) for each pair of clusters 52 . Pooling the pairs across all clusters revealed a high correlation ( r = 0.53
average number 
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i ".\{1500\}(2 nA, 2" *.txt
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd paper; grep -o -i ".\{1500\}ms at 0.01" *.txt
```

```
s APV (100 µM). To isolate the mEPSCs and mIPSCs, tetrodotoxin (1 µM) was added to the ACSF to suppress AP-dependent release. Each trace was recorded for a minimum 5 min after the signal had stabilized (no significant shifting beyond ±4 s.d. of the baseline), and at least 200 synaptic events were included for analysis. The traces were imported into miniAnalysis (Synaptosoft) to identify EPSC and IPSC events. The event detection threshold was set at the maximus root mean squared noise level (5 pA) 95 , 96 . Recordings of synaptic events were assessed for frequency (Hz) and amplitude (pA) using Clampfit 10.6 (Molecular Devices). Then the results were plotted with custom-made MATLAB routines (MATLAB, Mathworks). To examine synaptic connections between neurons, simultaneous multichannel whole-cell recordings were obtained from cortical neurons 91 . Specifically, patch recording pipettes (5–7 MΩ) were filled with intracellular solution containing 120 mM potassium gluconate, 10 mM HEPES, 4 mM KCl, 4 mM MgATP, 0.3 mM Na 3 GTP, 10 mM sodium phosphocreatine and 0.5% biocytin (pH 7.25). Whole-cell recordings were made from up to eight neurons simultaneously using two Quadro EPC 10 amplifiers (HEKA Electronics). A built-in LIH 8 + 8 interface board (HEKA) was used to achieve simultaneous A/D and D/A conversion of current, voltage, command and triggering signal for up to eight amplifiers. To test synaptic connections, current pulses were injected into the presynaptic neurons (2 nA for 2 ms at 0.01
```

**Agent calls Bash**

```bash
cd paper; for q in "further subdivided into 78" "273 excitatory neurons mapped" "29 neurons that were morphologically" "lower firing rate and greater" "farther from the soma than in PCs" "lower phase peak indices" "broader and had a lower" "outside-out patch-clamp recording showed"; do echo "=== $q"; grep -o -i ".\{400\}$q.\{700\}" *.txt; done
```

```
=== further subdivided into 78
s from the VEN-enriched AIC (Supplementary Fig. 2 ). Using a hierarchical clustering approach combining the canonical markers, we categorized these cells into four main classes: excitatory neurons (21,733 cells, 17.8%), inhibitory neurons (17,007 cells, 13.9%), glial cells (83,283 cells, 67.8%) and vascular cells (640 cells, 0.5%) (Fig. 1b,c ). The four classes were divided into 20 subclasses and further subdivided into 78 molecularly defined transcriptomic cell types, including 34 inhibitory and 20 excitatory neuron types, and 24 non-neuronal cell types (Extended Data Fig. 1e,f ). No significant sex differences were observed in cell types (Supplementary Fig. 3 ). The non-neuronal cells contained six subclasses: MOG + oligodendrocytes (Oligo), AQP4 + astrocytes, C1QA + microglia, C1QL1 + oligodendrocyte progenitor cells (OPCs), FLT1 + endothelial cells and BGN + vascular leptomeningeal cells (VLMCs) 1 , 2 , 41 – 45 (Extended Data Fig. 2a–c and Supplementary Figs. 4 and 5 ). Spearman correlation analysis between our macaque dataset and neocortical data from four species 46 reveals high correlation in gene expr
=== 273 excitatory neurons mapped
 morphology reconstructed and 352 neurons that passed mRNA quality control were sequenced. Among them, 307 cells had their transcriptomes recovered and were used for downstream analysis (Supplementary Fig. 8 ). These Patch-seq cells were mapped onto our AIC transcriptomic atlas using an established cell assignment method 51 , 52 . The mapping covered the majority of the discovered cell diversity; 273 excitatory neurons mapped to 18 of the 20 excitatory types, while 34 inhibitory neurons mapped to 17 of the 33 inhibitory types (Fig. 1e , Extended Data Fig. 6a and Supplementary Fig. 9 ). The laminar distribution of somata was consistent with their assigned cell types 7 , 47 (Fig. 1f and Extended Data Fig. 6b,c ), validating our mapping strategy. The 273 Patch-seq excitatory neurons were assigned int
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "Data availability.\{2000\}" *.txt; for q in "Fig. 3 " "c , " ; do :; done; grep -o -i "two-way ANOVA.\{300\}" *.txt; grep -o -i ".\{300\}Kruskal.\{300\}" *.txt
```

```
Data availability Sequencing data that support the findings of this study, including 10x scRNA-seq data and Patch-seq data (both in FASTQ format), have been deposited in the Gene Expression Omnibus (GEO) under accession numbers GSE319557 and GSE319369 , respectively. Previously published sequencing data that were reanalysed here are available at EMBL-EBI under accession code E-MTAB- 10459 (ref. 2 ), Neuroscience Multi-omics Archive (NeMO, RRID: SCR_016152 ) 41 , and GEO under accession numbers GSE115746 (ref. 47 ), GSE127898 and GSE127774 (ref. 46 ). Metabolomics data that support the findings of this study have been deposited in MetaboLights under accession code MTBLS13927 . Electrophysiological data that supporting the findings have been deposited in the DANDI archive at https://dandiarchive.org/dandiset/001746 (main dataset, Patch-seq), https://dandiarchive.org/dandiset/001750 (sodium channel currents), https://dandiarchive.org/dandiset/001751 (multi-Patch recording) and https://dandiarchive.org/dandiset/001752 (postsynaptic currents). Neuronal morphology data supporting the findings have been deposited at NeuroMorpho.org ref. 111 in ASC format. All other data supporting the findings of this study are available from the corresponding authors on reasonable request. Source data are provided with this paper. Code availability The custom-made software PatchAnaLab was developed and deposited at Zenodo 112 . The code used for data analysis, computational modelling and figure generation is available on GitHub at https://github.com/RFLiu2021/AIC_proj , with direct links to the processed data and meta data deposited at Zenodo 113 . Competing interests The authors declare no competing interests. Footnotes Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. These authors contributed equally: Rui-Feng Liu, Mengyao Huang, Yuhui Shen, Mingting Shao, Junzhan Jing. Contributor Information Zhao-Zh
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i ".\{1500\}two-way ANOVA. d , Morphology" *.txt; grep -o -i ".\{800\}two-way ANOVA, n = 12 for pairwise VEN-L.\{300\}" *.txt
```

```
the relationship between AIS geometry and AP generation dynamics in VENs. Fig. 3 Morphoelectric distinction between VEN and PC. a , Micrographs show an example of PC and VEN. Their somata and apical dendrites are indicated as ‘s’ and ‘a’, respectively. Their axons are indicated by the black closed arrowheads, and black arrows point to their originating sites. Independent replications ( n = 20) yielded the consistent results. b , Co-staining with biocytin and Pan-Nav antibodies. Yellow arrowheads indicate co-stained axons. White arrows mark axon origins: from prominent basal dendrites in VEN (top row) and from the base of the soma in PC (bottom row). The apical dendrites (‘a’) and prominent basal dendrites (‘b’) of VEN are labelled accordingly. Independent replications ( n = 35) yielded the consistent results. c , Co-staining of fluorescent Nissl immunostaining with Pan-Nav and 4,6-diamidino-2-phenylindole (DAPI) in a 30-µm-thick brain slice (left). White and yellow arrows indicated the cell bodies of representative VENs and PCs, respectively. White and yellow arrowheads indicate the stained Nav channels clustered in AISs of VENs and PCs, respectively. Box plots showing the length (top) and distance (bottom) of AIS to the soma (right). Data were collected from 23 Nissl staining slices (30-μm thickness) from five animals, and n = 108 and 430 for VEN and PC, respectively. AIS L, the length of AIS; AIS D, the AIS distance to soma. Statistical significance was determined using a two-way ANOVA. d , Morphology
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "c , Comparisons of the first (solid.\{3500\}" *.txt
```

```
c , Comparisons of the first (solid lines) and the penultimate (dashed lines) APs in the supra-threshold spike trains in VENs and L5 PCs. d , Top: evoked somatic Na + currents of a VEN and a PC using outside-out patch-clamp recording. Bottom: comparison of Na + currents between VENs and PCs. Two-tailed Wilcoxon rank-sum test, n = 14 for VENs, n = 21 for PCs. Box plots show median (centre line), 25th–75th percentiles (box bounds) and whiskers extending to the minimum and maximum values within 1.5× interquartile range. e , Simulated first (solid lines) and penultimate (dashed lines) APs of VEN and PC models. f , The phase–plane trajectories of APs from simulated VEN and PC models. g , AP waveforms (top) and phase–plane plots (bottom) from the VEN model, showing the effect of varying the AIS distance from the soma. All traces are threshold-aligned. h , AP waveforms and the phase–plane plots from the PC model. The spectrum of blue colour encodes the length of axon hillock, denoting the AIS distance from the soma. i , Scatter-plot showing the peak index as a function of AIS distance. Top: simulated VEN model; two-tailed Student’s t -test, P = 0.0015 for slope. Bottom: real neurons ( n = 62, each data point was averaged of 2–30 neurons except for the rightmost one with n = 1). Data are shown as mean ± s.e.m. Two-tailed Student’s t -test, P < 0.0001 for slope. j , Comparison of eEPSPs in VENs and PCs to electrical stimulation in the cortical deep layers. Left: experiment paradigm. Right: example EPSPs to three stimulation current levels and population analysis between pairwise VENs and PCs ( n = 26). Data are shown as mean ± s.e.m. k , Simulated VEN and PC respond to a train of synaptic input on the basal dendrite. l , Responses of VEN models with somatic (left, AIS D = 0 μm) and dendritic (right, AIS D = 70 μm) axon initiation. The black line denotes the firing rates shown in k (left). Source data To support that AIS geometry gives rise to unique AP shape and dynamics in 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "b . Scatter plot showing simulated AP shapes.\{1500\}" *.txt; echo; grep -o -i "VENs respond robustly to deep-layer.\{2500\}" *.txt
```

```
b . Scatter plot showing simulated AP shapes as a function of AIS distance (AIS D, distance of AIS away from the soma; hillock length denotes the AIS D in PC model) in the VEN and PC models as in Fig. 4g-h . Top left: VEN AP amplitude becomes smaller with increasing AIS D (Two-tailed Student’s t -test, p < 0.0001). Top right: VEN AP becomes wider with increasing AIS D (Two-tailed Student’s t -test, p < 0.0001). Bottom left: PC AP amplitude slightly increases with increasing AIS D (Two-tailed Student’s t -test, p < 0.0001). Bottom right: PC AP width as a function of AIS D (hillock length). AP becomes slightly wider with increasing AIS D (Two-tailed Student’s t -test, p = 0.0013). We increased the axon initial segment (AIS) distance in the VEN model by relocating the connection site distally along the basal dendrite, and in the PC model by elongating the axon hillock while maintaining its somatic connection. c . The effect of somatodendritic (SD) sodium conductance on PC APs. The somatic sodium conductance is changed to mimic varying sodium channel density in the SD part of PC. Top left: the first APs in simulated AP trains evoked by supra-threshold current stimulation as a function of SD sodium conductance. Top right: phase-plane plots of APs shown on the top left. Bottom left and right: AP amplitudes and half-widths as a function of SD sodium conductance. AP becomes higher and narrower slightly but significantly with increasing SD sodium conductance (Two-tailed Student’s t -test for AP amplitude and width, each p < 0.0

VENs respond robustly to deep-layer synaptic input The prominent, axon-carrying basal dendrite and spindle-shaped soma are signature morphological features of VENs, suggesting their privileged role in processing information from deep-layer projections. We simultaneously recorded evoked excitatory postsynaptic potentials (eEPSPs) from paired neighbouring VENs and PCs ( n = 26) in response to electrical stimulation in the deep layers of the AIC (Fig. 4
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "Fig. 5 Altered.\{1200\}" *.txt; grep -o -i "and miniature EPSCs/IPSCs.\{700\}" *.txt
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "and miniature.\{2200\}" *.txt | head -c 2500
```

```
and miniature excitatory/inhibitory postsynaptic currents (mEPSCs/mIPSCs) from post hoc morphologically confirmed VENs and PCs in brain slices (Fig. 5a ). The frequencies of both excitatory and inhibitory events were significantly lower in VENs than in PCs (Fig. 5b ), whereas the amplitudes were not significantly different between VENs and PCs (Fig. 5c ). The findings indicate that VENs receive markedly fewer excitatory and inhibitory inputs compared with adjacent PCs, suggesting their reduced connection with local circuits. Fig. 5 VENs establish sparse synaptic interactions within the local circuits. a , Example traces of sEPSCs/sIPSCs as well as mEPSCs/mIPSCs from either PC or VEN. Scale bar in amplitude, 20 pA for sEPSC, 60 pA for sIPSC, 20 pA for mEPSC and 40 pA for mIPSC. Time scale, 500 ms for all traces. b , Frequency of postsynaptic currents in VENs and PCs. sEPSC: n = 8 for VEN, n = 11 for PC. sIPSC: n = 7 for VEN, n = 8 for PC. mEPSC: n = 8 for VEN, n = 8 for PC. mIPSC: n = 15 for VEN, n = 21 for PC. Two-tailed Wilcoxon rank-sum test for independent experiments. c , Amplitudes of postsynaptic currents in VENs and PCs. The same data in b . Two-tailed Wilcoxon rank-sum test for independent experiments. d , Left: microscopic image of six simultaneously recorded excitatory neurons in the macaque AIC layer 5. Right: morphological reconstruction of the neurons. A total of 1,292 potential connectivity pairs (from n = 377 neurons) were tested. e , Enlarged soma shapes and firing patterns of the six neurons shown in d . The colours of traces are the same as the reconstructed morphologies. f , Traces showing a PC-to-PC connection (from cell 2 to cell 6, bottom block). Testing of projections from a PC (cell 2) to other cells. Traces from top to bottom show injected currents ( I inj ), single spikes elicited in presynaptic cells and average response (>20 replications) from potential postsynaptic cells. The black arrows indicate the evoked EPSPs in cell 6. Scale bar, 1
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "downw.\{3500\}" *.txt | head -c 3600
```

```
downward. Quantitative analysis confirmed additional morphological differences: VEN-L had larger basal dendritic arborization than L5 PCs, whereas VEN-S had intermediate-sized basal dendrite arborization similar to PCs (Fig. 6c,d and Supplementary Tables 6 and 7 ). Despite these dendritic differences, the distance from the axon originating site to the soma was significantly greater in both VEN subtypes compared with PCs (Fig. 6e ), with no significant difference observed between VEN-L and VEN-S. Fig. 6 Multimodal characteristics revealed two VEN subtypes. a , Morphology gallery of VEN subtypes (VEN-L and VEN-S) and neighbouring L5 ET neurons. b , Comparison of the prominent basal dendritic diameters of VEN-L and VEN-S. The stem diameters of the prominent basal dendrites were normalized and plotted as a function of their distances from the somata. The grey rectangle indicates the significant difference between VEN-L and VEN-S (two-tailed Student’s t -test. Statistical length bin: 50 μm with 10-μm sliding window; n = 10 for VEN-L, n = 11 for VEN-S). The lines and shaded error bands represent mean ± s.e.m. c , Representative morphologies of VEN-L, VEN-S and PC. The basal dendritic fields of neurons are contoured with white lines. Unit of the dendritic length density, μm μm −2 . d , Box plot showing the comparisons of basal dendritic heights, field sizes and axon distances to soma among projection neuron types in layer 5 ( n = 38 for VEN-L, n = 34 for VEN-S, and n = 85 for PCs). Benjamini–Hochberg FDR-adjusted after two-tailed Wilcoxon rank-sum test for d and e . More comparisons are provided in Supplementary Tables 6 and 7 . e , Similar to d , but comparison of axon distances to soma among PCs and VEN subtypes. Due to the lack of axonal information from staining, the number of data points is 36, 20 and 74 for VEN-L, VEN-S and PC, respectively. f , UMAP representation of projection neurons with Patch-seq neurons mapped onto the UMAP. Expert-defined Patch-seq neurons inc
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "VEN-Ss ( n = 11) (Fig. 6f ).\{3000\}" *.txt
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "To definitive.\{4000\}" *.txt
```

```
To definitively distinguish VEN-S from canonical L5/6 CT neurons, we performed subclustering of the Exc FEZF2 COL24A1 population, revealing five transcriptomic subclusters (Fig. 6g ). VEN-Ss were specifically assigned to the subcluster COL24A1 POC5, whereas the canonical L5/6 CT neurons ( n = 10) mapped to the other subclusters. Both VEN subtypes are enriched for canonical VEN markers identified in molecular analyses of human tissues, including FEZF2 , GABRQ and ADRA1A (Supplementary Fig. 16 ); however, these genes are not specific to VENs or their homologue in other animals 49 , 53 , 65 – 70 . To identify more specific molecular signatures, we performed differentially expressed gene (DEG) analysis comparing VEN-L, VEN-S and L5/6 CT types (Fig. 6h ). This identified highly specific marker genes for each subtype; VEN-L expressed markers such as DSG2, HAPLN4, TOX2, TRPC4, CAMK1G and TAGLN2 , whereas VEN-S showed high expression of ATP8A2, POC5 and SEMA3E . These specific molecular markers were further validated using fluorescent staining ( HAPLN4 for VEN-L; COL24A1 and POC5 for VEN-S) (Fig. 6i,j and Extended Data Fig. 8 ). Despite their distinct morphological and transcriptomic profiles, both VEN subtypes exhibited similar physiological properties (Extended Data Fig. 9 and Supplementary Table 8 ). Mirroring the transcriptomic similarity between VEN-S and L5/6 CT, VEN-L shows greater physiological disparity from L5/6 CT than does VEN-S (Supplementary Table 9 ). In contrast, both VEN-L and VEN-S are significantly different from L5/6 CT in terms of morphology (Supplementary Table 10 ). Extended Data Fig. 8 Validation of highly expressed genes in VEN-L and VEN-S. a . Confirmation of HAPLN4 with RNAscope in AIC tissue. b . Higher magnification of the field indicated by the dashed rectangle in ( a ). The small vertical rectangles represent the positions of example VENs shown in ( c ) and ( d ). c-d . Confirmation of HAPLN4 in the example VENs indicated by the rectangles in 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "Transcriptomic distinctions underlie.\{2500\}" *.txt; echo; grep -o -i "Cortical metabolomics reveals.\{5000\}" *.txt | tail -c 5000
```

```
Transcriptomic distinctions underlie phenotypic variation Leveraging our multimodal dataset, we then investigated the correlation between phenotypic and transcriptomic diversity across projection neuron types. We computed the transcriptomic distance (RNA difference and correlation distance between average log counts) and the phenotypic distance (Euclidean distance between average feature vectors) for each pair of clusters 52 . Pooling the pairs across all clusters revealed a high correlation ( r = 0.53) between the membrane time constant (tau) distances and RNA distances (Fig. 7a–c ). Similar correlations extended to other morphoelectric properties (Fig. 7d–i and Supplementary Fig. 17 ), suggesting that transcriptomic diversity underlies the morphoelectric disparity of projection neurons in AIC. For three main subclasses of IT neurons, the expression of specific genes involved in neuronal development and morphogenesis 71 – 74 substantially correlated with soma location and volume (Fig. 7j,k ), reinforcing the causal link between transcriptomic diversity and phenotypic variability. Fig. 7 Correlations between the phenotypic traits and transcriptomic variation suggest fundamental differences in macaque AIC. a , Patch-seq neurons mapped to the reference scRNA-seq projection neuron atlas. The dots indicate mapped cells and were coloured by membrane time constant (tau). Four example transcriptomic type cells are labelled. b , Example firing patterns of neurons labelled in a with circled numbers. The four example neurons show different tau levels. c , Correlation between membrane time constant (tau) distances and transcriptomic distances across pairwise neuron types. Pearson correlation coefficient is labelled in the plot. d – f , Similar to a – c , showing correlation between neuronal maximal firing rate distances and their RNA expression distances. g – i , As in d – f , showing correlation between an example morphological feature, normalized soma depth and the transcrip
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "Variability analysis of transcriptomic.\{1500\}" *.txt; echo; grep -o -i "AIC cells displayed elevated.\{1200\}" *.txt; echo; grep -o -i ".\{300\}Calculation of the phase peak.\{600\}" *.txt
```

```
Variability analysis of transcriptomic neuron types Based on the mapping of Patch-seq neurons on the 10x projection neuron types, we studied the relationship between morphoelectric and transcriptomic properties (Fig. 7a–i and Supplementary Fig. 17 ). The algorithm we used is the same as that previously reported 52 . In brief, the transcriptomic distance of each pairwise cell type was defined as the Pearson correlation of the mean log 2 ( x + 1)-transformed unique molecular identifier counts in the 10x data, using the 500 most-variable genes. Electrophysiological and morphological property distances were calculated as the Euclidean distance between mean feature vectors. Untargeted metabolomics Untargeted metabolomics was conducted at LipidALL Technologies. Polar metabolites were extracted from approximately 50 mg of tissues using 500 μl of ice-cold methanol: H 2 O (4:1, v/v) containing 0.224 mM phenylhydrazine. Tissues were minced into small pieces in the extraction solvent and subsequently homogenized using a bead ruptor with an optimized program. Tissue homogenates were incubated at 1,500 rpm for 30 min at 4 °C. Following incubation, the samples were kept at −20 °C for 1 h for derivatization of α-keto acids 105 . Then, samples were centrifuged for 10 min at 12,000 rpm at 4 °C. Clean supernatant was transferred to a new tube. Extraction was repeated for another round by adding another 500 μl of ice-cold methanol containing 0.224 mM phenylhydrazine. Extracts from both rounds were pooled into a single tube and drie

AIC cells displayed elevated citrate and reduced 2-ketobutyrate levels, along with increased glutamate. These suggest that V1 cells may rely on glutaminolysis for energy, whereas AIC cells seem to maintain sufficient glucose-derived carbon, reducing their need for glutamine catabolism. These metabolic adaptations in AIC may reflect an evolutionary optimization for efficient information processing, supporting its role in integrating sensory, cognitive and e
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "UMAP) analysis confirmed this.\{1200\}" *.txt; echo; grep -o -i "The AIC evolved a neural signal-processing strategy.\{1800\}" *.txt; echo; grep -o -i "reorganized.\{300\}" *.txt | head -3; grep -o -i ".\{1200\}Notably, VENs exhibit lower" *.txt
```

```
UMAP) analysis confirmed this morphological distinction, particularly separating VENs and PCs into distinct clusters and underscoring VENs’ unique morphology (Fig. 2i ). The AIC evolved a neural signal-processing strategy One of the most notable morphological features that distinguish VENs from other PC types is that the axons of the VENs emanate from its basal dendrite (Fig. 3a ), consistent with the observation of Banovac et al. in the human ACC 54 . The axonal initial segment (AIS), a specialized region with highly concentrated clusters of sodium channels located at the axon base, is where APs are initiated 55 . This led us to investigate the relationship between AIS geometry and AP generation dynamics in VENs. Fig. 3 Morphoelectric distinction between VEN and PC. a , Micrographs show an example of PC and VEN. Their somata and apical dendrites are indicated as ‘s’ and ‘a’, respectively. Their axons are indicated by the black closed arrowheads, and black arrows point to their originating sites. Independent replications ( n = 20) yielded the consistent results. b , Co-staining with biocytin and Pan-Nav antibodies. Yellow arrowheads indicate co-stained axons. White arrows mark axon origins: from prominent basa

The AIC evolved a neural signal-processing strategy One of the most notable morphological features that distinguish VENs from other PC types is that the axons of the VENs emanate from its basal dendrite (Fig. 3a ), consistent with the observation of Banovac et al. in the human ACC 54 . The axonal initial segment (AIS), a specialized region with highly concentrated clusters of sodium channels located at the axon base, is where APs are initiated 55 . This led us to investigate the relationship between AIS geometry and AP generation dynamics in VENs. Fig. 3 Morphoelectric distinction between VEN and PC. a , Micrographs show an example of PC and VEN. Their somata and apical dendrites are indicated as ‘s’ and ‘a’, respectively. Their axons are indicated by the bla
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i "outside-out.\{600\}" *.txt | tail -2; grep -o -i "eEPSP.\{400\}" *.txt | grep -i "stimulat" | head -3
```

```
outside-out recordings at somatic membrane were made on HEKA setups using pipettes of similar resistance (2–3 MΩ) filled with Cs-based internal solution containing 145 mM CsCl, 2 mM MgCl 2 , 2 mM Na 2 ATP, 10 mM HEPES, 0.2 mM EGTA and 2 mM TEA (tetraethylammonium) (adjusting the pH to 7.2 with CsOH). No differences in the degree or time of suction applied to the back of pipettes were required to form high resistance (3–10 GΩ) seals at somatic sites, suggesting that similar membrane areas were sampled 55 . Furthermore, the surface area of outside-out patches was estimated using the similar method in the p
outside-out patches was calculated from the capacitance (~50 fF) assuming a specific membrane capacitance of 1 µF cm −2 . The membrane potentials were held initially at −80 mV and families of Na + currents in response to a series of depolarizing voltages ranging from −80 to 0 mV (25 ms) with 5-mV stepping were recorded under voltage-clamp recording mode. Currents were leak subtracted online with PatchMaster (HEKA) software and the data were collected at a 100-kHz sample frequency. In the electrical stimulation experiment, a concentric bipolar electrode (125 µm diameter; FHC) was placed at the border of t
eEPSPs in VENs and PCs to electrical stimulation in the cortical deep layers. Left: experiment paradigm. Right: example EPSPs to three stimulation current levels and population analysis between pairwise VENs and PCs ( n = 26). Data are shown as mean ± s.e.m. k , Simulated VEN and PC respond to a train of synaptic input on the basal dendrite. l , Responses of VEN models with somatic (left, AIS D = 0 μm)
eEPSPs) from paired neighbouring VENs and PCs ( n = 26) in response to electrical stimulation in the deep layers of the AIC (Fig. 4j left). The postsynaptic response latencies were similar between VENs and PCs (5.13 ± 0.29 ms for VENs and 5.02 ± 0.30 ms for PCs, two-tailed paired t -test: P = 0.8941), whereas the response amplitudes in VENs were significantly higher t
[... 1 more lines not kept]
```

**Agent**

Paper read. The Fig. 5 claims (this dataset) hold up. I found smaller gaps in several other claims and am editing now.

**Agent calls Read**

```json
{
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "offset": 220,
 "limit": 10
}
```

```
220	  - fig5d-connectivity-totals
221	  criterion: As fig5-pc-in. Reproduced when both values hold under every reading run.
222	- id: fig5-pair-distances
223	  statement: PC-PC connections span a wide range of soma distances, 111.8 ± 61.2 um (mean ± s.d.);
224	    the distances given for the other classes are 135.7 ± 60.0 um for VEN-VEN, 119.3 ± 63.1 um for
225	    VEN-PC, 107.0 ± 60.1 um for PC-IN and 97.4 ± 36.8 um for VEN-IN.
226	  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 2
227	  quote: These connections spanned a wide range of soma distances (111.8 ± 61.2 μm, mean± s.d.).
228	    In contrast, VENs did not form synaptic connections with adjacent VENs (VEN-to-VEN, 0 of 110,
229	    135.7 ± 60.0 μm) or with PCs (VEN-to-PC, 0 of 200, 119.3 ± 63.1 μm)
```

**Agent calls Bash**

```bash
cd  grep -rn "checks:" claims/*/*.yaml | head -3; f=$(grep -rln "^checks:" claims | head -1); sed -n '/^checks:/,$p' $f | head -30
```

```
claims/000005/10.1038-nn.4412.yaml:1092:checks:
claims/000006/10.1038-s41586-018-0642-9.yaml:746:checks:
claims/000008/10.1038-s41586-020-2907-3.yaml:964:checks:
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checker. The 29 values flagged as not found (28 before this check, plus the Supplementary Table 1 p-value added here) are all printed in the paper with "x 10^" garbled to "3 10" in the text; 25 were confirmed in the text, the table value on PDF page 49, and the three of figs7cd-number-of-words (and those of figs7e-downsampled-words) on PDF page 46, rendered for this check.
  - fig1c-object-tuned-fraction. The binomial test was one-sided; the Methods (Statistical tests) say all tests were two-sided. Made two-sided.
  - fig1h-cross-day-stability. Same change to a two-sided binomial test. Noted that the Figure 1H y axis runs to 62 cells while its legend says 35.
  - figs4-object-traces. Same change to a two-sided binomial test. Added that a cell counts when any field passes, since the Supplementary Figure 4A legend tests each field.
  - fig1g-no-experience-effect. The criterion pooled all cell-days; the legend says each of the 62 dots is a cell and does not say which day's score is used. Named this open, with three readings.
  - figs2d-traces-no-interference. The criterion said only one reading of trace removal was possible; the paper does not say how traces were removed. Added the reading that sets the trace bins to zero.
  - fig3b-decode-presence and figs5a-decode-no-from-no-prime. The 99th percentile of label shuffles was not in the paper, which gives chance as 50% from the shuffling procedure. Now judged against 0.5 and the mean of the session's shuffles.
  - fig3d-number-of-cells. The SD-based rule was not in the paper. Replaced with the paper's test for correlations (Pearson) of accuracy with the number of cells.
  - fig4c-each-session-decreasing. Made explicit that every session is judged under the same readin
[... 13 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    135.7 ± 60.0 μm) or with PCs (VEN-to-PC, 0 of 200, 119.3 ± 63.1 μm)\n  expected:\n  - quantity: PC-PC distance, mean",
 "new_string": "    135.7 ± 60.0 μm) or with PCs (VEN-to-PC, 0 of 200, 119.3 ± 63.1 μm) ... (PC-to-IN, 2 of 65 and\n    IN-to-PC, 4 of 65, 107.0 ± 60.1 μm) ... (VEN-to-IN, 0 of 55 and IN-to-VEN, 0 of 55, 97.4 ± 36.8\n    μm)\n  expected:\n  - quantity: PC-PC distance, mean"
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  statement: In the example slice of Fig. 5d-h (six cells, VEN, PC, PC, VEN, VEN, PC), PC cell 2\n    evokes uEPSPs in PC cell 6, and VEN cell 4 evokes no EPSP in any of the other cells.",
 "new_string": "  statement: In the example slice of Fig. 5d-h (six simultaneously recorded excitatory neurons),\n    PC cell 2 evokes EPSPs in cell 6, and VEN cell 4 evokes no EPSP in any of the other cells."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  criterion: The slice and channels come from the code (Fig5fg_plotConn.m and\n    Fig5e_plotConnexampleFPs.m), slice 20190315 s4 of subject Mfa190314, cells 1 to 6 on",
 "new_string": "  criterion: The slice and channels come from the code (Fig5fg_plotConn.m and\n    Fig5e_plotConnexampleFPs.m, which types cells 1 to 6 as VEN, PC, PC, VEN, VEN, PC; the paper\n    types only cell 2, a PC, cell 4, a VEN, and cell 6, a PC by its legend title \"PC-to-PC\n    connection\"), slice 20190315 s4 of subject Mfa190314, cells 1 to 6 on"
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  criterion: A claim of absence, judged on the paper's test, a two-tailed Wilcoxon rank-sum test\n    of per-cell mean amplitudes per event type (Fig. 5c legend), alpha 0.05 (conventional).\n    Reproduced when p >= 0.05 for each type, with the effect size reported.",
 "new_string": "  criterion: A claim of absence, judged on the paper's test, a two-tailed Wilcoxon rank-sum test\n    of per-cell amplitudes per event type (Fig. 5c legend; \"The same data in b\", so the cells of\n    Fig. 5b), alpha 0.05 (conventional). The paper does not say how a cell's amplitude summarizes\n    its events (Clampfit, Methods); readings, (a) the mean and (b) the median of the cell's event\n    amplitudes. Reproduced when p >= 0.05 for each type, with the effect size reported."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  statistics:\n  - test: two-tailed Wilcoxon rank-sum\n    p: 0.001\n    p_relation: \"<\"\n    n: 281 VENs and 306 PCs",
 "new_string": "  statistics:\n  - about: AP amplitude\n    test: two-tailed Wilcoxon rank-sum\n    p: 0.001\n    p_relation: \"<\"\n    n: 281 VENs and 306 PCs\n  - about: AP width\n    test: two-tailed Wilcoxon rank-sum\n    p: 0.001\n    p_relation: \"<\"\n    n: 281 VENs and 306 PCs"
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    and in real neurons, and the ANCOVA intercept term gives p >= 0.05. What the ANCOVA slope P\n    tests is not said (common slope against zero, or difference of slopes); it is reported under\n    both readings and does not decide.",
 "new_string": "    and in real neurons, and the ANCOVA intercept term gives p >= 0.05. What the ANCOVA slope P\n    tests is not said (common slope against zero, or difference of slopes); it is reported under\n    both readings and does not decide. The printed F(1, 93) = 1.07 is placed before both P values\n    and gives p of about 0.30, matching neither 0.5729 nor 0.0031, so which term it belongs to is\n    open; it is recorded under the intercept as the text's order suggests and does not decide."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python3 -c "from scipy.stats import f; print(f.sf(1.07,1,93))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    from scipy.stats import f; print(f.sf(1.07,1,93))
    ^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
python3 -c "
import math
# F(1,df)=t^2; two-sided t p via numeric integration of t density
t=math.sqrt(1.07); n=93
c=math.gamma((n+1)/2)/(math.sqrt(n*math.pi)*math.gamma(n/2))
N=200000; a=t; b=60; h=(b-a)/N
s=sum(c*(1+((a+i*h+h/2)**2)/n)**(-(n+1)/2) for i in range(N))*h
print(2*s)"
```

```
0.30362779493093983
```

**Agent**

Confirmed (p ≈ 0.30). Continuing with the model, eEPSP and Fig. 6/7 claims.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  quote: Crucially, simulating an increase in the distance of the AIS from the soma in the VEN\n    model led to APs being wider and smaller in amplitude\n  data: elsewhere",
 "new_string": "  quote: Crucially, simulating an increase in the distance of the AIS from the soma in the VEN\n    model led to APs being wider and smaller in amplitude\n  statistics:\n  - about: VEN model, AP amplitude against AIS distance, slope\n    test: two-tailed Student's t-test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: VEN model, AP width against AIS distance, slope\n    test: two-tailed Student's t-test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: PC model, AP amplitude against hillock length, slope (amplitude slightly increases)\n    test: two-tailed Student's t-test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: PC model, AP width against hillock length, slope (AP slightly wider)\n    test: two-tailed Student's t-test\n    p: 0.0013\n  data: elsewhere"
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    (Extended Data Fig. 7b legend), and in the PC model amplitude does not fall.",
 "new_string": "    (Extended Data Fig. 7b legend), and in the PC model amplitude does not fall (the legend\n    reports it slightly increasing; the PC AP also widens slightly, p = 0.0013, so width does not\n    separate the models and is reported only)."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  criterion: A claim of absence, judged on the paper's two-tailed paired t-test at alpha 0.05;\n    reproduced when p >= 0.05, with the mean difference reported. Tolerances are the stated s.e.m.",
 "new_string": "  criterion: Only monosynaptic eEPSPs, those whose amplitude increases monotonically with\n    stimulation current at a constant latency, with polysynaptic responses and those evoking APs\n    excluded (Methods, electrical stimulation). A claim of absence, judged on the paper's\n    two-tailed paired t-test at alpha 0.05; reproduced when p >= 0.05, with the mean difference\n    reported. Tolerances are the stated s.e.m."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  criterion: Two-way ANOVA of amplitude on cell type and stimulation level. Reproduced when VEN\n    amplitudes are higher and the cell-type effect has p < 0.05 (conventional).",
 "new_string": "  criterion: The monosynaptic eEPSPs of fig4j-eepsp-latency (Methods). ANOVA of amplitude on cell\n    type and stimulation level (the Results name the two factors; the legend of the same design in\n    Extended Data Fig. 9e,f says two-way ANOVA). Whether it treats the 26 VEN-PC pairs and the\n    stimulation levels as repeated measures is not said; readings, (a) ordinary two-way ANOVA and\n    (b) repeated-measures ANOVA with the pair as subject. Reproduced when, under both, VEN\n    amplitudes are higher and the cell-type effect has p < 0.05 (conventional)."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    distance. Reproduced when VEN-L basal field exceeds PCs at FDR < 0.05, VEN-S does not differ\n    from PCs, both subtypes exceed PCs in axon distance at FDR < 0.05, and VEN-L against VEN-S\n    gives FDR >= 0.05.",
 "new_string": "    distance. \"Basal dendritic arborization\" is measured in Fig. 6d by two features, basal\n    dendritic height and field size; the text does not say which carries the finding, so each is\n    a reading. Reproduced when, under each, VEN-L exceeds PCs at FDR < 0.05 and VEN-S does not\n    differ from PCs (FDR >= 0.05), both subtypes exceed PCs in axon distance at FDR < 0.05, and\n    VEN-L against VEN-S in axon distance gives FDR >= 0.05."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  criterion: SCANPY Wilcoxon differential expression (Methods, Enrichment marker genes). The",
 "new_string": "  criterion: SCANPY Wilcoxon differential expression (Methods, Enrichment marker genes),\n    comparing VEN-L, VEN-S and L5/6 CT types (Results; Fig. 6h shows the Exc FEZF2 COL24A1\n    subpopulations and Exc FEZF2 DSG2). The"
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  source: Results, Multimodal profiling of two VEN subtypes, paragraph 2; Extended Data Figure 9c,d;\n    Supplementary Table 8",
 "new_string": "  source: Results, Multimodal profiling of two VEN subtypes, paragraph 2; Extended Data Figure\n    9c-f; Supplementary Table 8"
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  criterion: A claim of absence, judged on the paper's test, two-tailed Wilcoxon rank-sum with\n    Benjamini-Hochberg FDR (Extended Data Fig. 9c,d), on AP width and amplitude of 85 VEN-L and\n    41 VEN-S. Reproduced when neither is significant at FDR 0.05. The other features are in\n    Supplementary Table 8, not read.",
 "new_string": "  statistics:\n  - about: eEPSP amplitude, VEN-L against VEN-S (pairs of Extended Data Fig. 9e,f)\n    test: two-way ANOVA\n    p: 0.9852\n  criterion: A claim of absence, judged on the paper's tests, two-tailed Wilcoxon rank-sum with\n    Benjamini-Hochberg FDR (Extended Data Fig. 9c,d), on AP width and amplitude of 85 VEN-L and\n    41 VEN-S, and the two-way ANOVA of eEPSP amplitudes between VEN-L and VEN-S (Extended Data\n    Fig. 9f legend, 12 VEN-L and 12 VEN-S paired with PCs, a subset of the Fig. 4j recordings).\n    Reproduced when none is significant at 0.05 (FDR for the first two). The other features are\n    in Supplementary Table 8, not read."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    (Methods, Variability analysis of transcriptomic neuron types); Pearson r over all pairs. The\n    transcriptomic distance is taken as 1 - r, the reading under which a positive r between\n    distances is possible.",
 "new_string": "    (Methods, Variability analysis of transcriptomic neuron types); Pearson r over all pairs. The\n    Methods define the distance as \"the Pearson correlation\"; the Results call it the\n    \"correlation distance between average log counts\", so it is taken as 1 - r, the reading\n    the Results give and the one under which a positive r between distances is possible."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  tail -5 claims/001751/*.yaml; grep -n "id: fig3c" claims/001751/*.yaml
```

```
increased glutamate
  data: elsewhere
  where: MetaboLights MTBLS13927
  criterion: Welch's ANOVA followed by Games-Howell test (Fig. 8 legend). Reproduced when citrate
    and glutamate are higher and 2-ketobutyrate lower in AIC than in V1 at P < 0.05.
468:- id: fig3c-ais-distance-length
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "- id: fig3c-ais-distance-length",
 "new_string": "- id: fig3ab-ven-axon-from-basal-dendrite\n  statement: The axons of VENs emanate from their basal dendrite, while those of PCs originate at\n    the base of the soma.\n  source: Results, The AIC evolved a neural signal-processing strategy, paragraph 1; Figure 3a,b\n  quote: One of the most notable morphological features that distinguish VENs from other PC types\n    is that the axons of the VENs emanate from its basal dendrite (Fig. 3a )\n  data: elsewhere\n  where: NeuroMorpho.org doi:10.13021/y4be-0p18 (morphologies, ASC)\n  criterion: The paper shows examples (Fig. 3a, 20 replications; Fig. 3b, biocytin and Pan-Nav\n    co-staining, 35 replications, axon origins \"from prominent basal dendrites in VEN\" and \"from\n    the base of the soma in PC\") and reports no count or test. Reproduced when, in the reconstructed\n    VENs with an axon, the axon leaves a basal dendrite and, in PCs, the soma; the fraction of each\n    is reported. The paper gives no fraction, so a VEN whose axon leaves the soma is reported and\n    does not by itself decide.\n- id: fig3c-ais-distance-length"
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    the base of the soma in PC\") and reports no count or test. Reproduced when, in the reconstructed\n    VENs with an axon, the axon leaves a basal dendrite and, in PCs, the soma; the fraction of each\n    is reported. The paper gives no fraction, so a VEN whose axon leaves the soma is reported and\n    does not by itself decide.",
 "new_string": "    the base of the soma in PC\") and reports no count or test. Measured on the reconstructed VENs\n    and PCs whose axon was recovered (Fig. 6e counts 36 VEN-L, 20 VEN-S and 74 PCs with axonal\n    information). The paper gives no fraction; readings, (a) every such VEN's axon leaves a basal\n    dendrite and every PC's the soma, and (b) most do in each type. Reproduced under the readings\n    that hold, with the fractions reported."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "dendrite and every PC's the soma, and (b) most do in each type. Reproduced under the readings\n    that hold, with the fractions reported.",
 "new_string": "dendrite and every PC's the soma, and (b) more than half do in each type, the number of the\n    reported count read as the paper's claim. Reproduced when either reading holds, with the\n    fractions reported and the reading that holds named."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "(b) more than half do in each type, the number of the\n    reported count read as the paper's claim. Reproduced",
 "new_string": "(b) more than half do in each type. Reproduced"
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  cat >> claims/001751/10.1038-s41556-026-02009-4.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checker. 33 claims, 33 quotes, 8 statistical values, 0 problems before this check; rerun after the changes below.
  - The Fig. 5d-i claims (this dataset) were checked against the Results paragraph, the Fig. 5 legend and the Methods on multi-patch recording; counts, rates, distances, the sum 24 + 1 + 2 + 4 = 31 and the reference 50 (Seeman et al. 2018) agree with the paper. The code details of the opening comment (metadata_multiPatch.xlsx tallies, Fig5fg_plotConn.m) could not be checked here, as the code was not opened in this check.
  - fig5-pair-distances. The quote lacked the sentences that give the PC-IN and VEN-IN distances the statement and expected values use; added them.
  - fig5fg-example-slice. The statement gave the types of all six cells, which come from the code, not the paper (the legend types only cells 2, 4 and 6); moved them to the criterion with their source.
  - fig5c-psc-amplitude. The criterion said per-cell mean amplitude; the paper does not say how a cell's events are summarized. Named mean and median as readings.
  - fig4ac-ap-width-amplitude. One statistics entry stood for two tests (the legend gives P < 0.001 for both amplitude and width); split into two.
  - fig4i-peak-index-ais-distance. Noted that F(1, 93) = 1.07 gives p of about 0.30, matching neither printed P, so the term it belongs to is open.
  - fig4g-model-ais-distance-ap-shape. Added the Extended Data Fig. 7b slope tests as statistics, and noted that the PC model's AP also widens slightly (p = 0.0013), so only amplitude separates the models.
  - fig4j-eepsp-latency and fig4j-eepsp-amplitude. Added the Methods' selection of monosynaptic eEPSPs (monotonic amplitude with current, constant latency, polysynaptic and AP-evoking responses excluded), which the criteria left out.
  - fig4j-eepsp-amplitude. The paper does not say whether the ANOVA treats the paired cells as repeated measures; named ordinary and repeated-measures two-way ANOVA as readings.
  - fig6-ven-subtype-morphology. The criterion said "basal field" while Fig. 6d measures height and field size; named each as a reading, and made the VEN-S against PC test explicit (FDR >= 0.05).
  - fig6h-subtype-markers. Added the comparison groups the Results give (VEN-L, VEN-S and L5/6 CT).
  - ven-subtypes-similar-physiology. Added the Extended Data Fig. 9f two-way ANOVA between VEN-L and VEN-S (p = 0.9852) as statistics and to the criterion; source widened to Extended Data Fig. 9c-f.
  - fig7c-tau-rna-distance. The 1 - r reading was justified only by the sign; added that the Results name the measure "correlation distance".
  - fig3ab-ven-axon-from-basal-dendrite. New claim, a main finding of the Results (axon origin from the basal dendrite, Fig. 3a,b) that had no claim.
  - Open. fig5d-connectivity-totals and the claims that depend on it. The paper gives no rule for calling a connection; the criterion rests on annotations (the dataset's or the code's table), and the claims are blocked as methods_underspecified when neither exists. This cannot be settled from the paper.
  - Open. fig5i-ven-sparse-local-connectivity. The pairing of each VEN rate with a PC rate of the same partner class is a reading of "compared with PCs"; the paper gives no test.
  - Open. fig3c-ais-distance-length. The two-way ANOVA's second factor is not named; the slice and animal readings are kept.
  - Open. Not covered by a claim, as secondary or resting on unread supplementary items, the Fig. 2d-f type differences (Supplementary Fig. 11), the model's basal dendrite thickness results (Extended Data Fig. 7g-j), the other Fig. 7d-k correlations and the Fig. 8b,c pathway enrichment.
EOF
python tools/claims_check.py claims/001751/10.1038-s41556-026-02009-4.yaml paper/10.1038-s41556-026-02009-4.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -nE "^\s+[^:]*\S: .*: |^\s{4,}[^'\"]*\S: " claims/001751/*.yaml | grep -v "^\S*:\s*-\? \?[a-z_]*: '" | head; git status --short
```

```
84:    value: 1292
85:    tolerance: 129
87:    value: 377
88:    tolerance: 38
90:    value: 31
91:    tolerance: 3.1
115:    value: 24
116:    tolerance: 2.4
118:    value: 503
119:    tolerance: 50
 M claims/001751/10.1038-s41556-026-02009-4.yaml
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -nE "^\s{4}[^-'\" ].*: " claims/001751/*.yaml | grep -vE "^\d+:\s{4}(value|tolerance|unit|quantity|test|p|p_relation|n|statistic|about): " | head
```

```
84:    value: 1292
85:    tolerance: 129
87:    value: 377
88:    tolerance: 38
90:    value: 31
91:    tolerance: 3.1
115:    value: 24
116:    tolerance: 2.4
118:    value: 503
119:    tolerance: 50
```

**Agent calls Bash**

```bash
cd  grep -nE "^ {4}.*: " claims/001751/*.yaml | grep -vE "^[0-9]+: {4}(value|tolerance|unit|quantity|test|p|p_relation|n|statistic|about): " | head
```

```
542:    VEN model closely matched the experimental data (Fig. 4i , ANCOVA: F(1, 93) = 1.07, P = 0.5729
606:    VENs and 5.02 ± 0.30 ms for PCs, two-tailed paired t -test: P = 0.8941)'
```

**Agent**

The checker now reports `34 claims, 34 quotes, 14 statistical values, 0 problems`. Before my changes it reported 33 claims, 33 quotes, 8 statistical values and 0 problems.

**Changes, by claim:**
- **The Fig. 5d–i claims (this dataset):** the counts, rates, distances and reference 50 (Seeman et al. 2018) match the Results, the Fig. 5 legend and the Methods, and the connection counts add up (24 + 1 + 2 + 4 = 31). Two claims needed fixes:
  - **fig5-pair-distances:** the quote now includes the sentences that give the PC-IN and VEN-IN distances, which the statement and expected values already used.
  - **fig5fg-example-slice:** the statement listed the types of all six cells, but those come from the code, not the paper. I moved them to the criterion and named their source; the paper's legend types only cells 2, 4 and 6.
- **fig5c-psc-amplitude:** the criterion said "per-cell mean", which the paper does not give. Mean and median are now named as readings.
- **fig4ac-ap-width-amplitude:** one statistics entry stood for two tests, so I split it into amplitude and width.
- **fig4i-peak-index-ais-distance:** the printed F(1, 93) = 1.07 gives p ≈ 0.30, which matches neither printed P. The criterion now says it is unclear which term it belongs to.
- **fig4g-model-ais-distance-ap-shape:** added the Extended Data Fig. 7b slope tests as statistics. The criterion now notes that the PC model's AP also widens a little (p = 0.0013), so only amplitude separates the two models.
- **fig4j-eepsp-latency / fig4j-eepsp-amplitude:** added the Methods' rule for selecting monosynaptic eEPSPs, which the criteria left out. For amplitude, ordinary and repeated-measures two-way ANOVA are now named as readings.
- **fig6-ven-subtype-morphology:** basal height and basal field size are now each a reading. The test that VEN-S does not differ from PCs is now stated explicitly.
- **fig6h-subtype-markers:** added the comparison groups the Results give (VEN-L, VEN-S and L5/6 CT).
- **ven-subtypes-similar-physiology:** added the Extended Data Fig. 9f ANOVA (p = 0.9852) to the statistics and the criterion, and widened the source to Extended Data Fig. 9c–f.
- **fig7c-tau-rna-distance:** the 1 − r reading is now backed by the Results' own term, "correlation distance".
- **New claim, fig3ab-ven-axon-from-basal-dendrite:** a main finding (Fig. 3a,b) that had no claim.

**Still open (recorded in `checks`):**
- The paper gives no rule for calling a connection. The Fig. 5 claims therefore depend on annotations, from the dataset or the code's table, and are blocked as `methods_underspecified` when neither is available.
- The Fig. 5i comparison of each VEN rate with a PC rate of the same partner class is one reading of "compared with PCs"; the paper reports no test.
- The second factor of the Fig. 3c two-way ANOVA is not named.
- I did not open the code, so the code details in the opening comment (the table tallies and the plotting script) are unverified.
- Some secondary findings have no claim: the Fig. 2 type differences, Extended Data Fig. 7g–j, Fig. 7d–k and Fig. 8b,c.

**Ready:** yes. I set `ready: true`. Nothing was committed.

## End of run

53 turns, 4 minutes, result: success.
