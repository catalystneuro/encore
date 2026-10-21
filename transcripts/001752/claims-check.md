# 001752 · claims-check · run 39563704986

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001752/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; python tools/claims_check.py claims/001752/*.yaml paper/*.txt; cat claims/001752/*.yaml; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/055cb364-b207-4f34-950e-e08464b32005/tool-results/by1t7cldf.txt"
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
[... 681 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41556-026-02009-4.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
t=open('paper/10.1038-s41556-026-02009-4.txt').read()
print(t[51900:100000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/055cb364-b207-4f34-950e-e08464b32005/tool-results/bv1h79bl2.txt"
}
```

```
1	btypes. Due to the lack of axonal information from staining, the number of data points is 36, 20 and 74 for VEN-L, VEN-S and PC, respectively. f , UMAP representation of projection neurons with Patch-seq neurons mapped onto the UMAP. Expert-defined Patch-seq neurons including VEN-L and VEN-S are labelled. g , UMAP visualization of neuron subpopulations obtained by re-clustering Exc FEZF2 COL24A1. Patch-seq neurons are mapped to these subpopulations and presented on the UMAP. h , Stacked violin plot showing the expression of marker genes across subpopulations identified in g and Exc FEZF2 DSG2. Vertical rectangles indicate the expression of marker genes of both VEN subtypes. The maximum log-normalized expression value for each gene is shown on the right. The colour bar denotes the median expression in the neuron groups. i , j , Fluorescent staining confirming the gene markers HAPLN4 and POC5 for VEN-L and VEN-S, respectively. Biocytin was co-stained with HAPLN4 and POC5 antibodies. The somata (indicated by yellow arrows) are zoomed-in as indicated by dashed contours. Independent replications ( n = 5) yielded consistent results. Box plots in d and e show median (centre line), 25th–75th percentiles (box bounds) and whiskers extending to the minimum and maximum values within 1.5× interquartile range. Source data To determine whether these two morphological subtypes were also transcriptomically and physiologically distinguishable, we leveraged our combined Patch-seq and scRNA-seq data. By cross-referencing the molecular assignment with their morphology, we found the morphologically defined VENs mapped to L5 ET (Exc FEZF2 DSG2) were VEN-Ls ( n = 10), while those VENs mapped to L5/6 CT (Exc FEZF2 COL24A1) were VEN-Ss ( n = 11) (Fig. 6f ). To definitively distinguish VEN-S from canonical L5/6 CT neurons, we performed subclustering of the Exc FEZF2 COL24A1 population, revealing five transcriptomic subclusters (Fig. 6g ). VEN-Ss were specifically assigned to the subcluster 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41556-026-02009-4.txt').read()
i=t.find('References',100000)
print(len(t)); print(t[100000:140000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/055cb364-b207-4f34-950e-e08464b32005/tool-results/b10cgnlmc.txt"
}
```

```
1	204890
2	n their mapped cell types and each individual neuron was positioned at the median embedding location of its ten nearest neighbours using Pearson correlation distance in the high-dimensional spaces. The embedding was computed based on the log-transformed counts across the same genes used in the transcriptomic mapping above. Finally, the UMAP embedding of Patch-seq cells in the reference atlas UMAP was calculated and presented (Fig. 1e ). We used the 500 most-variable genes to calculate the correlation between the Patch-seq cells and the reference neuron clusters. The highly variable genes used here were selected using the same method as that in the previous publication 51 . Specifically, the genes that had counts of at least 32 ( C min = 32) in fewer than 10 cells were excluded first. The counts of remaining genes were log-transformed (log 2 ( x + 1)) and calculated the mean value (nonzero expression, µ ) across all counts, and the fraction of counts that were smaller than or equal to 32 (probability of near-zero expression, τ ). Here, μ and τ show a clear inverse relationship, approximately following an exponential law of the form τ ≈ exp(−1.5 × μ + a ), where a denotes a horizontal offset. Using a binary search, the value b of this offset was determined to produce the desired number of genes satisfying τ > exp(−1.5 × μ + b ) + 0.002. Extraction of electrophysiological features We developed a custom-made software kit (PatchElectroLab) for offline analysis of electrophysiology data using MATLAB (Mathworks). Neuronal electrophysiological properties were automatically extracted employing a methodology similar to previous studies 2 , 12 , 13 , 52 , 98 , 99 (Supplementary Fig. 10 ). AP-related properties were calculated based on the first AP elicited by current injection in our step stimulation protocol. The minimum current injection required to elicit an AP (or APs) was defined as the rheobase. To calculate the AP threshold, the 20-ms potential trace precedin
[... 1 more lines not kept]
```

**Agent**

Checker passes (32 claims, 0 problems). I've read the paper in full; now reviewing claims and making corrections.

**Agent calls Read**

```json
{
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "offset": 70,
 "limit": 5
}
```

```
70	- id: fig5b-sepsc-frequency
71	  statement: The frequency of spontaneous EPSCs is lower in VENs than in neighbouring PCs.
72	  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 1; Figure 5b
73	  quote: The frequencies of both excitatory and inhibitory events were significantly lower in VENs
74	    than in PCs (Fig. 5b )
```

**Agent**

Now the edits. First, the sEPSC criterion: add the Methods' stability and 200-event conditions and say plainly that the duration analysed is open.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    RMS noise level. The duration analysed follows the Methods, the whole stable recording (at\n    least 5 min); the code's 30 s per cell (its mIPSC table) is shown as a variant. Cell types are",
 "new_string": "    RMS noise level. The peak detector itself is a standard choice, not the paper's (miniAnalysis\n    is not reproduced). The Methods say each trace was recorded for at least 5 min after the\n    signal had stabilized (no shift beyond 4 s.d. of the baseline) and that at least 200 events\n    were included for analysis, but not how long a stretch was analysed; the analysis uses the\n    whole stable recording, and the code's 30 s per cell (its mIPSC table) is shown as a variant.\n    Cell types are"
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  where: GEO GSE319557 (10x scRNA-seq, FASTQ and processed h5ad)",
 "new_string": "  where: GEO GSE319557 (10x scRNA-seq, FASTQ, per the Data availability statement); processed\n    data in Zenodo doi:10.5281/zenodo.18814764"
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  - quantity: inhibitory Patch-seq neurons\n    value: 34\n    tolerance: 3\n",
 "new_string": "  - quantity: inhibitory Patch-seq neurons\n    value: 34\n    tolerance: 3.4\n  - quantity: excitatory types with mapped Patch-seq neurons\n    value: 18\n    tolerance: 1.8\n  - quantity: inhibitory types with mapped Patch-seq neurons\n    value: 17\n    tolerance: 1.7\n"
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    RORB 17, L5 IT FEZF2 119, VEN 22, L5 ET 16, L6 PC 13). Reproduced when L2/3 IT HPCAL1 has the\n    lowest median tau and AP width and differs from most other subclasses at FDR < 0.05; the\n    paper's adjusted p-values are in Supplementary Table 2, not read.",
 "new_string": "    RORB 17, L5 IT FEZF2 119, VEN 22, L5 ET 16, L6 PC 13; the Results give L6 PC n = 14). The\n    paper says only that the subclass \"stood out\", and its adjusted p-values are in\n    Supplementary Table 2, not read, so how many pairwise differences must be significant is\n    open. Readings, (a) the lowest median tau and the lowest median AP width of the six\n    subclasses, each lower than every other subclass at FDR-adjusted p < 0.05 (conventional), and\n    (b) the lowest median of each of the two, without a requirement on the pairwise tests.\n    Reproduced when both readings hold; blocked as methods_underspecified when they disagree."
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  criterion: Peak Na+ current per patch over the -80 to 0 mV steps (Methods). Two-tailed Wilcoxon\n    rank-sum (Fig. 4d legend). Reproduced when the VEN median is lower with p < 0.05\n    (conventional).",
 "new_string": "  criterion: Na+ currents evoked by 25 ms steps from -80 to 0 mV in 5 mV increments, leak\n    subtracted (Methods). The Methods do not name the measure compared; readings, (a) the largest\n    peak inward current over the steps, per patch, and (b) the same divided by the patch area\n    estimated from its capacitance at 1 uF/cm2 (Methods). Two-tailed Wilcoxon rank-sum (Fig. 4d\n    legend). Reproduced when, under both readings, the VEN median is lower with p < 0.05\n    (conventional); blocked as methods_underspecified when they disagree."
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  statement: The phase peak index decreases linearly with AIS distance from the soma, in the VEN\n    model and in real neurons, with slopes that do not differ.",
 "new_string": "  statement: The phase peak index decreases linearly with AIS distance from the soma in the VEN\n    model, and this relation closely matches the one in real neurons."
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    ephysio/data_ephy/NeuronPeakIdx_summary.mat); simulated traces in Zenodo\n    doi:10.5281/zenodo.18814764\n",
 "new_string": "    ephysio/data_ephy/NeuronPeakIdx_summary.mat); simulated traces in Zenodo\n    doi:10.5281/zenodo.18814764\n  criterion: Phase peak index as in the Methods (Calculation of the phase peak index), against\n    AIS distance; real neurons binned by AIS distance as in the Fig. 4i legend (n = 62, each point\n    a mean of 2 to 30 neurons; the bins are not given, a standard choice). Reproduced when the\n    slope is negative with two-tailed t-test p < 0.05 in the model and in real neurons, and the\n    ANCOVA term for intercept (model against real neurons) gives p >= 0.05. The paper does not say\n    what its ANCOVA \"slope\" P (0.0031) tests; readings, (a) the common slope against zero, which\n    fits \"closely matched\", and (b) the difference of slopes between model and data, under which\n    the printed P would mean the slopes differ. The slope term is reported under both and does not\n    decide the outcome. The printed F(1, 93) = 1.07 gives p near 0.30, not 0.5729, and the 93\n    degrees of freedom do not follow from the n stated.\n"
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    more than 20 trials (Fig. 5f legend); the paper gives no amplitude criterion for a connection,\n    so the deposit's own connection annotations, if present, are used.",
 "new_string": "    more than 20 trials (Fig. 5f legend), with uEPSPs measured at -70 mV and uIPSPs at -60 mV\n    (Methods); cell types as identified by firing pattern and post hoc morphology (Methods), taken\n    from the deposit's labels. The paper gives no amplitude or latency criterion for a\n    connection, so the deposit's own connection annotations are used; if it has none, the claim is\n    blocked as methods_underspecified."
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  criterion: Differential expression with SCANPY's Wilcoxon test, log fold change > 1 and\n    FDR < 0.05, among VEN-L, VEN-S and L5/6 CT (Methods, Enrichment marker genes). Reproduced when\n    each named gene passes for its subtype.",
 "new_string": "  criterion: Groups as in the Fig. 6h legend, the scRNA-seq cluster Exc FEZF2 DSG2 (VEN-L) and the\n    subclusters of Exc FEZF2 COL24A1 from Fig. 6g (COL24A1 POC5 for VEN-S, the others L5/6 CT).\n    Differential expression with SCANPY's Wilcoxon test (Methods, Enrichment marker genes). The\n    Methods give two levels, (a) significant marker genes, log fold change > 1 and FDR < 0.05, and\n    (b) enriched marker genes, among the top 50 ranked and meeting the four expression criteria\n    listed there; the text does not say which the named genes meet. Reproduced when each named\n    gene passes for its subtype under both; blocked as methods_underspecified when they disagree."
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    quantity: Pearson r, tau distance against RNA distance\n    value: 0.53\n    tolerance: 0.053\n",
 "new_string": "    quantity: Pearson r, tau distance against RNA distance\n    value: 0.53\n    tolerance: 0.053\n  criterion: Per pair of projection neuron types, the transcriptomic distance from the Pearson\n    correlation of mean log2(x + 1) counts over the 500 most-variable genes of the 10x data, and\n    the tau distance as the Euclidean distance between type means (Methods, Variability analysis\n    of transcriptomic neuron types); Pearson r over all pairs (Fig. 7c legend). The Results call\n    the transcriptomic distance \"RNA difference and correlation distance\", so whether it is 1 - r\n    or r is a sign convention that does not change the size of the correlation.\n"
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "    of transcriptomic neuron types); Pearson r over all pairs (Fig. 7c legend). The Results call\n    the transcriptomic distance \"RNA difference and correlation distance\", so whether it is 1 - r\n    or r is a sign convention that does not change the size of the correlation.",
 "new_string": "    of transcriptomic neuron types); Pearson r over all pairs (Fig. 7c legend). The Methods call\n    the transcriptomic distance \"the Pearson correlation\" and the Results \"correlation distance\";\n    it is taken as 1 - r, the reading under which a positive r between distances is possible, and\n    the notebook says so."
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -o "Crucially, simulating.\{0,330\}" paper/*.txt; grep -n "id: fig4j-eepsp-latency" claims/001752/*.yaml; tail -5 claims/001752/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001752/10.1038-s41556-026-02009-4.yaml",
 "old_string": "- id: fig4j-eepsp-latency\n",
 "new_string": "- id: fig4g-model-ais-distance-ap-shape\n  statement: In the VEN model, moving the AIS farther from the soma makes APs wider and smaller and\n    the phase-plane plot more saddle-like; this effect is not replicated in the PC model.\n  source: Results, The AIC evolved a neural signal-processing strategy, paragraph 4; Figure 4g,h;\n    Extended Data Figure 7b\n  quote: Crucially, simulating an increase in the distance of the AIS from the soma in the VEN\n    model led to APs being wider and smaller in amplitude, and the phase–plane plot becoming more\n    ‘saddle-like’, (Fig. 4g and Extended Data Fig. 7b ). This effect was not replicated in the PC\n    model (Fig. 4h ).\n  statistics:\n  - about: VEN model, AP amplitude against AIS distance\n    test: two-tailed Student's t-test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: VEN model, AP width against AIS distance\n    test: two-tailed Student's t-test\n    p: 0.0001\n    p_relation: \"<\"\n  data: elsewhere\n  where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6 (VEN_modeling); Zenodo\n    doi:10.5281/zenodo.18814764 (simulated traces)\n  criterion: Simulations as in the Methods (Computational model), AIS distance varied 0 to 170 um\n    along the thick basal dendrite in the VEN model and hillock length 0 to 70 um in the PC model.\n    Reproduced when, in the VEN model, AP amplitude falls and AP width rises with AIS distance,\n    each slope with two-tailed t-test p < 0.05 (Extended Data Fig. 7b legend), and the phase peak\n    index falls. In the PC model the legend reports small but significant changes (amplitude\n    slightly larger, p < 0.0001; width slightly wider, p = 0.0013), so \"not replicated\" is read\n    as no fall in amplitude and no saddle-like phase-plane plot, not as the absence of any\n    significant change.\n- id: fig4j-eepsp-latency\n"
}
```

```
The file claims/001752/10.1038-s41556-026-02009-4.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -l "^checks:" claims/*/*.yaml | head -2 | xargs -I{} sh -c 'sed -n "/^checks:/,\$p" {} | head -20'
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
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/001752/10.1038-s41556-026-02009-4.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig5b-sepsc-frequency (and the Fig. 5 claims that refer to it). The criterion said the Methods fix the analysed duration as the whole stable recording; they give only a minimum recording of 5 min after stabilization (no baseline shift beyond 4 s.d.) and at least 200 events. Added both conditions, named the duration as open, and said the peak detector is a standard choice, not the paper's.
  - scrna-classes. The where field named a processed h5ad on GEO; the paper says the GEO deposit is FASTQ. Replaced with FASTQ and the Zenodo processed data the paper names.
  - patchseq-mapping. The tolerance on 34 was 3, not 10% (3.4); corrected. Added the 18 and 17 type counts the statement rests on as expected values with 10% tolerance.
  - fig2d-f-l23-it-tau-width. The criterion required differences from "most other subclasses", which the paper does not say. Replaced with two readings of "stood out" (lowest median with every pairwise test significant, and lowest median alone), and noted the Results give L6 PC n = 14 where the legend gives 13.
  - fig4d-sodium-current. The criterion took the peak current as the measure; the Methods do not name it and also estimate patch area. Named peak current and current density as readings.
  - fig4i-peak-index-ais-distance. The statement said model and real slopes do not differ; the paper says the relation "closely matched", and its ANCOVA slope P is 0.0031. Restated as the paper says and added a criterion that judges on the slope t-tests and the intercept term, with the two readings of the slope term named. The claim had no criterion.
  - fig5-connectivity-by-type. The criterion did not say what happens when the deposit has no connection annotations. It now says the claim is blocked as methods_underspecified then, and adds the holding potentials and cell-type identification from the Methods.
  - fig6h-subtype-markers. The criterion gave only the significant-marker thresholds; the Methods also define enriched markers (top 50 and four expression criteria). Named both as readings, and fixed the groups from the Fig. 6h legend (scRNA-seq clusters, not Patch-seq cells).
  - fig7c-tau-rna-distance. Added a criterion with the Methods' distance definitions; the Methods call the transcriptomic distance a Pearson correlation, so it is taken as 1 - r, the reading under which the positive r reported is possible.
  - Added claim fig4g-model-ais-distance-ap-shape (Fig. 4g,h and Extended Data Fig. 7b), the modelling result that AIS distance shapes VEN APs, a main finding with no claim.
  - Open. The Fig. 5b,c p-values are printed only in the figure, not in the text read, so whether each of the four frequency comparisons (sEPSC, sIPSC, mEPSC, mIPSC) was significant on its own, as the four frequency claims read the pooled sentence, cannot be settled from the text.
  - Open. The Fig. 4i ANCOVA prints F(1, 93) = 1.07 with P = 0.5729; that F gives p near 0.30, and what the slope P tests is not said.
  - Open. The code details in the opening comment (the mEPSC label swap, the duplicated PC trace, the "+20mV" sIPSC files, the 30 s window) were not checked against the repository in this run; the criteria treat them as variants that do not decide the outcome.
EOF
python tools/claims_check.py claims/001752/10.1038-s41556-026-02009-4.yaml paper/10.1038-s41556-026-02009-4.txt; grep -n "[^ ]: [^ ]" claims/001752/*.yaml | grep -v "^\S*:\s*[-a-z_]*:" | head; grep -c "—\|rather" claims/001752/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import yaml,re
d=yaml.safe_load(open('claims/001752/10.1038-s41556-026-02009-4.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and ': ' in x and not p.endswith('quote'): print(p, x[:80])
walk(d)
EOF
```

```
(Bash completed with no output)
```

**Agent**

I checked the claims file for DANDI:001752 against the paper. After my changes the file is ready for an attempt.

**Checker:** `33 claims, 33 quotes, 10 statistical values, 0 problems`. Before my changes it was 32 claims, 8 statistical values and 0 problems.

**Changes, by claim** (each is also logged under `checks`):
- **fig5b-sepsc-frequency** (the other Fig. 5 claims refer to it): the criterion said the Methods fix the analysed duration as the whole stable recording. They don't. They give only a minimum 5 min recording after the baseline is stable (no shift beyond 4 s.d.) and at least 200 events. I added both conditions and marked the duration as open. I also wrote that the peak detector is a standard choice, not the paper's own method.
- **scrna-classes:** the "where" field named a processed h5ad on GEO, which the paper doesn't mention; the paper says the GEO deposit is FASTQ. I changed it to FASTQ, plus the Zenodo processed data the paper does name.
- **patchseq-mapping:** the tolerance on 34 was 3; 10% is 3.4, so I corrected it. I also added the 18 and 17 type counts as expected values.
- **fig2d-f-l23-it-tau-width:** the criterion required differences from "most other subclasses", which the paper doesn't say. I replaced it with two readings of "stood out". I also noted that the text gives L6 PC as n = 14 while the legend gives 13.
- **fig4d-sodium-current:** the Methods don't say what is compared. I named two readings: peak current, and current density using the patch area the Methods estimate.
- **fig4i-peak-index-ais-distance:** the statement said the model and real-neuron slopes don't differ. The paper only says the relation "closely matched", and its ANCOVA prints P = 0.0031 for slope. I restated the claim as the paper puts it and added the missing criterion: it is judged on the two slope t-tests and the intercept term, and both readings of the slope term are named.
- **fig5-connectivity-by-type:** the criterion said nothing about what happens if the deposit has no connection labels. It now says the claim is blocked as methods_underspecified in that case. I also added the holding potentials and how cell types were identified, from the Methods.
- **fig6h-subtype-markers:** the criterion gave only one of the Methods' two marker definitions. I added the second (top 50 genes plus four expression criteria) as a reading, and set the groups from the Fig. 6h legend (scRNA-seq clusters, not Patch-seq cells).
- **fig7c-tau-rna-distance:** I added a criterion with the Methods' distance definitions. The transcriptomic distance is taken as 1 − r, since a positive r is only possible under that reading.
- **New claim, fig4g-model-ais-distance-ap-shape** (Fig. 4g,h and Extended Data Fig. 7b): a main finding with no claim. Moving the AIS away from the soma in the VEN model makes APs wider and smaller, and the PC model doesn't show this.

**Still open:**
- The Fig. 5b,c p-values appear only in the figure, not in the text. So I can't confirm that each of the four frequency comparisons was significant on its own; the four claims assume it from one sentence that pools them.
- Fig. 4i prints F(1, 93) = 1.07 with P = 0.5729, but that F gives p ≈ 0.30. The paper also doesn't say what the slope P tests.
- I didn't check the opening comment's code details against the repository (the swapped mEPSC labels, the PC trace counted twice, the "+20mV" sIPSC files, the 30 s window). The criteria use them only as variants, so they don't decide any outcome.

Nothing was committed.

## End of run

26 turns, 3 minutes, result: success.
