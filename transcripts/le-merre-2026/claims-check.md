# 001260 · claims-check · run 39801393968

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001260/ paper/; grep -n "Reader" -A40 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 76,200p docs/protocol.md
```

```
finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
     states it (numbers only in a table, a result spread over several
     legends), a short note under `inferred` saying so. The statement is
     then a reading of the paper, and the note says what it was
     read from.
   - `statistics`: the statistical support the paper reports for the
     finding, one entry per test or interval: what it compares (`about`,
     when there is more than one), the `test` and `statistic` as named, the
     `p`-value as a number (a bound such as "p < 0.05" is `p: 0.05` with
     `p_relation: "<"`; a printed "P = 0" is recorded as 0), any `corrected`
     for multiple comparisons, a confidence interval (`ci`), and `n` in
     words. It records the paper; the
     numbers the attempt must match, with tolerances, stay in `expected`.
     Record only tests whose result is the finding. A significance threshold
     used to select or count units, cells or pairs ("238 of 288 neurons were
     better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
     finding.
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001260/10.1038-s41593-025-02190-z.yaml paper/10.1038-s41593-025-02190-z.txt; cat claims/001260/10.1038-s41593-025-02190-z.yaml; wc paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml"
}
```

```
1	# Claims for Le Merre, Heining et al. (2026), "A prefrontal cortex map based on single-neuron
2	# activity", Nature Neuroscience, doi:10.1038/s41593-025-02190-z, on dandiset 001260.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
5	# protocol pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read. The version of record (publisher HTML, open access, stored as
8	# paper/10.1038-s41593-025-02190-z.txt) in full: main text, figure legends, Methods, Data and
9	# Code availability, and the legends of Extended Data Figs. 1 to 9. No PDF was stored, so the
10	# figures themselves (values shown only in panels, such as correlation coefficients of Fig. 3
11	# and Fig. 4g) were not seen. Missing from the text read is the Supplementary Information file
12	# (Supplementary Methods, which describe the behavioral settings, Supplementary Figs. 1 and 2,
13	# and Supplementary Tables 1 to 7, which give the E-score p-values and the within-PFC
14	# hierarchy correlations of Supplementary Table 5), and the Source Data files. The main
15	# findings rest on the main and Extended Data figures, whose legends are in the text; the
16	# claims that cite a supplementary table say so. The bioRxiv preprint (10.1101/2024.11.06.622308
17	# v1, also under paper/) was read only to compare; it reports an earlier unit count (23,386)
18	# and no IBL task analysis, and no claim is taken from it.
19	#
20	# Code read. https://github.com/hejDMC/pfcmap at commit 9ae52eddc47fbb590ef4e1b1949507334707a0f1
[... 772 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n "" paper/10.1038-s41593-025-02190-z.txt | awk -F: 'length($0)>0' | cut -c1-200 | head -400
```

Result: not kept, because it reads the paper's text.

**Agent**

Running the checker gave 38 claims, 0 problems. Next I'm reading the paper body to check the claims against it.

**Agent calls Bash**

```bash
sed -n '220,$p' paper/10.1038-s41593-025-02190-z.txt | fold -s -w 200 > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt"
}
```

```
1	Download PDF Subjects Neural circuits Neuronal physiology Neurophysiology Abstract The intrinsic organization underlying the central cognitive role of the prefrontal cortex (PFC) is poorly 
2	understood. We approached organization by profiling the activity and spatial location of >24,000 neurons recorded in awake mice. High-resolution activity maps of the PFC did not align with 
3	cytoarchitecturally defined subregions. Instead, spontaneous activity and tuning to choice during a behavioral task were both related to intra-PFC hierarchy, suggesting that connectivity, rather than 
4	cytoarchitecture, shapes the PFC’s activity landscape. Low-rate, regular spontaneous firing was a hallmark of both the PFC and high hierarchy. Surprisingly, choice tuning was overrepresented in units 
5	displaying high spontaneous firing rates, linking connectivity-based hierarchy to distinct functional properties in separate neuronal populations. Our data-driven approach provides a scalable roadmap 
6	to explore functional organizations in diverse brain regions and species, opening avenues to obtain an integrated view of activity, structure and function in the brain. Similar content being viewed 
7	by others Single-neuron projectome of mouse prefrontal cortex Article 31 March 2022 Timescales of learning in prefrontal cortex Article 27 June 2024 Spatial transcriptomics reveals the distinct 
8	organization of mouse prefrontal cortex and neuronal subtypes regulating chronic pain Article Open access 16 October 2023 Main The PFC integrates information from all over the brain and is crucial 
9	for emotional and cognitive functions 1 , 2 . While mapping of gene expression 3 , 4 , 5 , cytoarchitecture 6 , 7 , 8 and connectivity 9 , 10 , 11 , 12 , 13 provides insights into the PFC’s 
10	infrastructure, a functional description of the PFC remains elusive 14 . It is unclear to what extent subregions of the PFC hold functional specializations 14 , 15 , and the existing structural 
11	descriptions of
[... 276 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 288,
 "limit": 200
}
```

```
288	Data were not anonymized for analysis. Recording sessions were excluded from any further analysis if (1) the presence of slow waves in the LFP and up-and-down states in cortical activity indicated 
289	that the session was dominated by sleep-like states, (2) the abundance of artifacts in the LFP made such assessment impossible, or (3) experiments involved licking and it was not possible to reliably 
290	detect licking from LFP artifacts or the piezo element. Following these criteria, 24 recordings were excluded in total. Data analysis Unless stated otherwise, continuous variables are reported as the 
291	median and interquartile range (IQR, 25th–75th percentiles) in the following. Detection and exclusion of licking periods In 18 of the 99 recording sessions in the dataset KI, mice could lick to 
292	obtain water rewards following the tone stimuli. Licking requires motor action, which could influence firing patterns. Licking also occurred outside the reward window and could thus affect not only 
293	tone response epochs but also spontaneous epochs. To improve comparability of patterns across sessions, licking periods were detected and both spontaneous and tone response epochs overlapping with 
294	licking periods were excluded. If available, licking was detected using a piezoelectric sensor. Otherwise, licking was detected as artifacts in LFPs (LFPs downsampled to 500 Hz with a polyphase 
295	filter) using independent component analysis. Lick periods invariably presented as a single independent component displaying a characteristic, rhythmic, saw-tooth like pattern with close to uniform 
296	weight contribution across the electrodes of a probe, that is, the lick artifacts were similarly strong across electrodes. Periods of lick artifacts in the lick component were detected using a 
297	semiautomatic procedure, which involved manually setting an amplitude threshold for each recording, detecting threshold crossings and manual curation that allowed deletion of false
[... 190 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 488,
 "limit": 170
}
```

```
488	behaviour. Nature 645 , 177–191 (2025). Article CAS Google Scholar Montijn, J. S. et al. A parameter-free statistical test for neuronal responsiveness. eLife 10 , e71969 (2021). Article PubMed PubMed 
489	Central Google Scholar Steinmetz, N. A., Zatka-Haas, P., Carandini, M. & Harris, K. D. Distributed coding of choice, action and engagement across the mouse brain. Nature 576 , 266–273 (2019). Article 
490	PubMed PubMed Central CAS Google Scholar Gallero-Salas, Y. et al. Sensory and behavioral components of neocortical signal flow in discrimination tasks with short-term memory. Neuron 109 , 135–148 
491	(2021). Article PubMed CAS Google Scholar Esmaeili, V. et al. Rapid suppression and sustained activation of distinct cortical regions for a delayed sensory-triggered motor response. Neuron 109 , 
492	2183–2201 (2021). Article PubMed PubMed Central CAS Google Scholar Oryshchuk, A. et al. Distributed and specific encoding of sensory, motor, and decision information in the mouse neocortex during 
493	goal-directed behavior. Cell Rep. 43 , 113618 (2024). Article PubMed CAS Google Scholar Chen, S. et al. Brain-wide neural activity underlying memory-guided movement. Cell 187 , 676–691 (2024). 
494	Article PubMed PubMed Central CAS Google Scholar Schomburg, E. W. et al. Theta phase segregation of input-specific gamma patterns in entorhinal-Hippocampal networks. Neuron 84 , 470–485 (2014). 
495	Article PubMed PubMed Central CAS Google Scholar Osanai, H., Yamamoto, J. & Kitamura, T. Extracting electromyographic signals from multi-channel LFPs using independent component analysis without 
496	direct muscular recording. Cell Rep. Methods 3 , 100482 (2023). Article PubMed PubMed Central CAS Google Scholar Shinomoto, S. et al. Relating neuronal firing patterns to functional differentiation 
497	of cerebral cortex. PLOS Comput. Biol. 5 , e1000433 (2009). Article PubMed PubMed Central Google Scholar Harris, K. D. Nonsense correlations in neuroscience. Preprint at bioRxiv 
498	h
[... 156 more lines not kept]
```

**Agent**

Checker passed. I've read the full paper text and have a list of suspected problems. Next I'm checking the preprint count, the protocol's `data` labels, and whether the code is reachable.

**Agent calls Bash**

```bash
grep -o "23,[0-9]\{3\}[^.]\{0,80\}" paper/10.1101-2024.11.06.622308.txt | head; grep -n "with_inputs\|with_labels\|elsewhere" docs/*.md | head -20; timeout 60 git clone -q https://github.com/hejDMC/pfcmap $TMPDIR/pfcmap 2>&1 | tail -2; cd $TMPDIR/pfcmap 2>/dev/null && git checkout -q 9ae52eddc47fbb590ef4e1b1949507334707a0f1 && grep -rn "Nmin_maps" --include=*.py . | head -20
```

Result: not kept, because it reads the paper's text.

**Agent**

The code is reachable. Checking the thresholds and shuffle settings that the claims attribute to it.

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap; grep -rn "Nmin_maps\s*=" . | head; grep -rln "gao" python | head -20; grep -rn "nshuff\|n_shuff\|Nshuff\|nrep" python/goalDirectedBehavior_IBL/*.py | head -20
```

```
./python/goalDirectedBehavior_IBL/plot_tuning_flatmaps.py:60:Nmin_maps = int(S.Nmin_maps)
./python/goalDirectedBehavior_IBL/gao_vs_enrichment_tuning.py:84:Nmin_maps = int(S.Nmin_maps)
./python/settings.py:32:Nmin_maps = 20
python/SOM/plot_SOMhits_resolved.py
python/connectivity_correlations/plot_gao.py
python/connectivity_correlations/gao_vs_enrichment.py
python/connectivity_correlations/gao_module_hierarchy.py
python/goalDirectedBehavior_IBL/README_goalDirectedBehavior.rst
python/goalDirectedBehavior_IBL/calc_statsdict_gaoRois_tuning.py
python/goalDirectedBehavior_IBL/gao_vs_enrichment_tuning.py
python/PATHS/filepaths_carlen.yml
python/PATHS/filepaths_IBLTuning.yml
python/PATHS/filepaths_IBL.yml
python/callers/call_flatmap_counts.py
python/callers/call_flatmap_enrichment_calc_and_plot.py
python/callers/call_flat_zeta_enrichment_and_hier.py
python/callers/call_connectivity_correlations.py
python/callers/call_flatmap_enrichment_ds_compare.py
python/callers/call_dataset_description.py
python/flatmaps/plot_flatmap_enrichments.py
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap; grep -n "Nmin\|>=\|> 20\|const_attr" python/connectivity_correlations/gao_vs_enrichment.py | head; grep -n "const_attr\s*=\|nshuff" python/goalDirectedBehavior_IBL/calc_statsdict_tuning.py python/goalDirectedBehavior_IBL/calc_statsdict_gaoRois_tuning.py | head; sed -n 100,150p python/goalDirectedBehavior_IBL/calc_statsdict_tuning.py
```

```
python/goalDirectedBehavior_IBL/calc_statsdict_tuning.py:16:nshuff = 2000
python/goalDirectedBehavior_IBL/calc_statsdict_tuning.py:120:const_attr = ['task','area']
python/goalDirectedBehavior_IBL/calc_statsdict_tuning.py:124:    statsdict_spont[attr1] = matchfns.get_all_shuffs(Usubsel,attr1,attr2,const_attr=const_attr,nshuff=nshuff,signif_levels=signif_levels)
python/goalDirectedBehavior_IBL/calc_statsdict_tuning.py:141:const_attr = 'task'
python/goalDirectedBehavior_IBL/calc_statsdict_tuning.py:146:    statsdict_rois[attr2] = matchfns.get_all_shuffs(Usubsel,attr1,attr2,const_attr=const_attr,nshuff=nshuff,signif_levels=signif_levels)
python/goalDirectedBehavior_IBL/calc_statsdict_gaoRois_tuning.py:12:nshuff = 2000
python/goalDirectedBehavior_IBL/calc_statsdict_gaoRois_tuning.py:95:const_attr = 'task'
python/goalDirectedBehavior_IBL/calc_statsdict_gaoRois_tuning.py:100:    statsdict_rois[attr2] = matchfns.get_all_shuffs(Usubsel,attr1,attr2,const_attr=const_attr,nshuff=nshuff,signif_levels=signif_levels)
        return 'signif'
    elif mybool==False:
        return 'ns'
    else:
        assert 0, 'unknown booltype'

for U in Usel:
    for attrname,featname in zip(['stimTuned','choiceTuned','feedbTuned'],['stimulus','choice','feedback']):

        setattr(U,attrname,signifbool_to_tag(U.tsignif[featname][blk_condition]))
#now task engagement
taskresp_dict = iblfns.load_taskresp_data(recids,outdir,myrun)
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap; grep -n "20\|Nmin\|count" python/connectivity_correlations/gao_vs_enrichment.py | head -20; grep -rn "Nmin\|nmin" python/flatmaps/*.py | head
```

```
99:Units,somfeats,weightvec =  uloader.load_all_units_for_som(metricsfiles,rundict,check_pfc= (not myrun.count('_brain')),rois_from_path=False)#rois from path = False  gets us the Gao rois
335:        if not myrun.count('resp'):
python/flatmaps/compare_flatmap_enrichments.py:62:        #presel_inds = np.array([aa for aa, aval in enumerate(mystats['avals1']) if countvec[aa]  > S.Nmin_maps and not aval.count('|sup') and not aval=='na' \
python/flatmaps/compare_flatmap_enrichments.py:64:        presel_inds = np.array([aa for aa, aval in enumerate(mystats['avals1']) if countvec[aa]  > S.Nmin_maps])
python/flatmaps/compare_flatmap_enrichments.py:228:x_bounds = np.array([np.nanmin(allX),np.nanmax(allX)])
python/flatmaps/compare_flatmaps_spont_resp_task.py:76:    presel_inds = np.array([aa for aa, aval in enumerate(mystats['avals1']) if countvec[aa]  > S.Nmin_maps and aval.count('|deep')])
python/flatmaps/compare_flatmaps_spont_resp_task.py:92:presel_inds = np.array([aa for aa, aval in enumerate(mystats['avals1']) if countvec[aa]  > S.Nmin_maps and aval.count('|deep')])
python/flatmaps/compare_flatmaps_spont_resp_task.py:113:cond_avail = (minnperroi>=S.Nmin_maps)&(deep_cond)
python/flatmaps/compare_flatmaps_spont_resp_task.py:383:    presel_inds = np.array([aa for aa, aval in enumerate(mystats['avals1']) if countvec[aa]  > S.Nmin_maps and aval.count('|deep')])
python/flatmaps/compare_flatmaps_spont_resp_task.py:395:presel_inds = np.array([aa for aa, aval in enumerate(mystats['avals1']) if countvec[aa]  > S.Nmin_maps and aval.count('|deep')])
python/flatmaps/compare_flatmaps_spont_resp_task.py:415:cond_avail = (minnperroi>=S.Nmin_maps)&(deep_cond)
python/flatmaps/plot_flat_zeta_responder_and_hierarchy.py:195:        presel_inds = np.array([aa for aa, aval in enumerate(mystats['avals1']) if countvec[aa]  > S.Nmin_maps and aval.count('|deep')])
Shell cwd was reset to
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "# percentile of the shuffles, with no correction, and that is followed (P < 0.05). Regions and\n# ROIs need more than 20 units (code, settings.py Nmin_maps = 20; the Fig. 4f legend says fewer\n# than 20 were not analyzed). Random seeds",
 "new_string": "# percentile of the shuffles, with no correction, and that is followed (P < 0.05). ROIs need at\n# least 20 deep-layer units (Fig. 4f legend, fewer than 20 not analyzed; Extended Data Figs. 7i\n# and 9d, n >= 20). The code's settings.py has Nmin_maps = 20 but most dataset KI scripts keep\n# counts > 20 while the IBL scripts keep >= 20; the legends' >= 20 is followed, > 20 is a variant.\n# For brain (sub)regions the text gives no minimum; the code's Nmin_maps is used. Random seeds"
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "v1, also under paper/) was read only to compare; it reports an earlier unit count (23,386)\n# and no IBL task analysis",
 "new_string": "v1, also under paper/) was read only to compare; it reports earlier unit counts (23,386 in the\n# Results, 23,667 in the figure legends) and no IBL task analysis"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "  - quantity: recordings (probes)\n    value: 99\n    tolerance: 0\n  criterion: Units counted",
 "new_string": "  - quantity: recordings (probes)\n    value: 99\n    tolerance: 0\n  - quantity: units in the PFC subregions (Extended Data Fig. 1b legend)\n    value: 12674\n    tolerance: 1267\n  criterion: Units counted"
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "    (Methods, equation 6), with the unit-type effect tested by an F test with\n    Kenward-Roger degrees of freedom (Methods; code Fig1i__MixModel_Statistics.jl, emmeans\n    pairwise contrast).",
 "new_string": "    (Methods, equation 6), with the unit-type effect tested by a post hoc F test with\n    Kenward-Roger degrees of freedom and Tukey's correction for multiple comparisons (Methods;\n    Fig. 1i legend; code Fig1i__MixModel_Statistics.jl, emmeans pairwise contrast)."
}
```

```
<tool_use_error>String to replace not found in file.
String:     (Methods, equation 6), with the unit-type effect tested by an F test with
    Kenward-Roger degrees of freedom (Methods; code Fig1i__MixModel_Statistics.jl, emmeans
    pairwise contrast).</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "    padded by 1 s or 0.3 s). Sleep-like epochs overlap such a period. Per unit, metrics computed\n    over active and over sleep-like epochs, units with enough of each (12 epochs of at least 6\n    spikes). A mixed model Metric ~ 1 + EpochType + (1|Mouse) (Methods, equation 7) per metric\n    and unit type. Reproduced when the epoch-type effect has p < 0.05 for at least two of the\n    three metrics in ww units; the direction of each is reported. The legend gives no direction\n    and no p-value in the text.",
 "new_string": "    padded by 1 s or 0.3 s). Sleep-like epochs overlap such a period. Per unit, metrics computed\n    over active epochs (all ww units with enough active epochs, n = 19,186) and over sleep-like\n    epochs (ww units with at least 12 sleep-like epochs of at least 6 spikes, n = 11,599), as the\n    Extended Data Fig. 1 legend gives the two samples. A mixed model Metric ~ 1 + EpochType +\n    (1|Mouse) (Methods, equation 7) per metric and unit type, post hoc F test with Kenward-Roger\n    degrees of freedom and Tukey's correction (Methods). The legend's per-metric marks and any\n    direction are in the figure only, so the count of metrics required is this file's rule.\n    Reproduced when the epoch-type effect has p < 0.05 for all three metrics in ww units;\n    partially reproduced for one or two; the direction of each is reported."
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "  criterion: Sleep-like detection and epoch rules as in extfig1d-sleep-like-differ. Whether a",
 "new_string": "  - quantity: ww units with enough sleep-like epochs (Extended Data Fig. 1 legend)\n    value: 11599\n    tolerance: 1160\n  criterion: Sleep-like detection and epoch rules as in extfig1d-sleep-like-differ. Whether a"
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "    (1|Mouse) (Methods, equation 6), with the unit-type effect tested by an F test with\n    Kenward-Roger degrees of freedom (Methods; code",
 "new_string": "    (1|Mouse) (Methods, equation 6), with the unit-type effect tested by a post hoc F test with\n    Kenward-Roger degrees of freedom and Tukey's correction for multiple comparisons (Methods;\n    Fig. 1i legend; code"
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "    Stability is the trace over the total of the summed transition matrix; chance is the same\n    for the matrix expected from its marginals. The paper does not say whether 57% pools all\n    transitions or averages per transition; both readings are shown and the value holds under\n    either.",
 "new_string": "    Stability per transition t is the trace of the summed transition matrix M_t over its total,\n    and chance is the same for the matrix expected from the marginals of M_t (Methods,\n    Assessment of overall stability per transition; Fig. 2e plots it per transition). The\n    paper does not say how \"around 57%\" summarizes the transitions; readings (a) the mean over\n    transitions, (b) the pooled matrix summed over transitions. Both are shown with the\n    per-transition values, and the value holds under either."
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "    shuffles. Supplementary Tables 1 and 2 (the p-values) were not read. Reproduced when L2/3 has\n    a significant positive E-score for at least one of the bursty categories 6 to 8 and none for\n    categories 1 to 3, and L5 and L6 each",
 "new_string": "    shuffles. Supplementary Tables 1 and 2 (the p-values) were not read. Reproduced when L2/3 has\n    a significant positive E-score for at least one of the bursty categories 6 to 8, and L5 and\n    L6 each"
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "  criterion: Pearson correlation across the n = 9 regions with sufficient nw units (Fig. 2j legend;\n    regions with more than 20 nw units), between ww and nw category E-scores.",
 "new_string": "  criterion: Pearson correlation across the n = 9 regions with sufficient nw units (Fig. 2j legend),\n    between ww and nw category E-scores. The text does not define \"sufficient\"; the code's\n    Nmin_maps (more than 20 nw units) is used and the number of regions it keeps is reported\n    against 9."
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "    ORBl have a significant positive E-score in category 7 or 8. Disagreeing readings block it.",
 "new_string": "    ORBl have a significant positive E-score in category 7 or 8. Disagreeing readings block it.\n    The ORBl part of the statement (most ventral dataROI) is not tested, as the flatmap's\n    dorsoventral axis is not given in the text; the ORBl dataROI with the highest category 7\n    and 8 E-scores is reported."
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "    flatmap_PFCrois.h5); E-scores per GaoROI as for dataROIs; GaoROIs with more than 20 deep ww\n    units and a hierarchy score",
 "new_string": "    flatmap_PFCrois.h5); E-scores per GaoROI as for dataROIs; GaoROIs with at least 20 deep ww\n    units (Extended Data Fig. 7i; > 20 as in the code is a variant) and a hierarchy score"
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap; ls config 2>/dev/null | head; find . -name "somsettings_carlenResp*" | xargs cat 2>/dev/null | head -40
```

```
runCrespZP_brain:
    state: 'active'
    tsel: 'response'
    layerlist: 'all'
    reftag: 'all'
    spec: 'zscore'
    datasets: ['Carlen']
    tasks: ['Passive','Aversion','Opto','Detection','Context','Attention']#
    imetrics:
      features: []
      weights: []
    wmetrics:
      features: []#['peak2Trough','abRatio','p2tRatio']
      weights: []#[1,1,1]
    rmetrics:
      features: 'all'#'all' or int, if  int the pcs up to int are considered
      weights: []
    utypes: ['ww']
    nnodes: 400
    clustering:
[... 21 more lines not kept]
```

**Agent**

The code trains the tone-response SOM on all ww units in every region and layer. The Results instead say deep-layer ww units (n = 15,352), so I'm recording that as an open choice in fig5b.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "    pooled, 8 components; SOM of 400 nodes on ww units (code somsettings_carlenResp.yml), Ward into\n    8 categories numbered by mean peak delay, the flat or negative category last (Methods).",
 "new_string": "    pooled, 8 components; SOM of 400 nodes on ww units (code somsettings_carlenResp.yml), Ward into\n    8 categories numbered by mean peak delay, the flat or negative category last (Methods). The\n    units the SOM is trained on are open; readings (a) deep-layer ww units of all regions, n =\n    15,352 (Results, Tone response maps, paragraph 1); (b) all ww units of all regions and layers,\n    as the code's runCresp*_brain settings (layerlist all). The claim is judged on the PFC\n    deep-layer ww units with tone responses, n = 7,184 (Fig. 5 legend), under both readings."
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "  criterion: Tuned units as in fig5g; E-scores per GaoROI with more than 20 units and a hierarchy\n    score (n = 39), shuffling as in Methods, Enrichment statistics (the grouping for dataset IBL is\n    not stated; no grouping is one reading and grouping by recording a second; both shown).",
 "new_string": "  criterion: Tuned units as in fig5g; E-scores per GaoROI with at least 20 units (Extended Data\n    Fig. 9d) and a hierarchy score (n = 39), 1,000 shuffles as in Methods, Enrichment statistics\n    (the grouping for dataset IBL is not stated; no grouping is one reading and grouping by\n    recording a second; both shown). The code (calc_statsdict_gaoRois_tuning.py) uses 2,000\n    shuffles grouped by its 'task' label; shown as a variant."
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "  criterion: Mutual enrichment of spontaneous category (IBL Passive units on dataset KI's ww SOM)\n    against tuning (Methods); the code shuffles within recording setting and region with 2,000\n    shuffles, followed. Reproduced",
 "new_string": "  criterion: Mutual enrichment of spontaneous category (IBL Passive units on dataset KI's ww SOM)\n    as population against tuning as attribute (Methods, Mutual enrichment), 1,000 shuffles\n    (Methods, Enrichment statistics). The Methods name no grouping for Fig. 5k; readings (a) no\n    grouping, (b) the code's grouping by its 'task' label and region (calc_statsdict_tuning.py).\n    The code's 2,000 shuffles are a variant, as the Methods give 1,000. Reproduced"
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "    significant positive E-score in spontaneous category 4.",
 "new_string": "    significant positive E-score in spontaneous category 4, under both readings; readings that\n    disagree block the claim as methods_underspecified."
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -n 975,990p docs/pilot-notes.md; grep -n "with_inputs" docs/protocol.md docs/pipeline.md | head
```

```
001933 showed that a blocked claim can mean two different things. Eight of
its claims rest on imaging, proteomics and blots that the paper deposited
in the BioImage Archive, PRIDE and Zenodo; they were blocked with
`data_missing`, the same reason as data that are public nowhere. pilot-7
adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
does not hold because the paper put them in another public archive. The
claim names the archive and a pinned identifier under `where`, is tested on
those data like any other claim, and is counted on its own, apart from the
dandiset's claims and from `with_inputs` claims. It is never blocked with
`data_missing`; if it cannot be tested here, the reason is the one that
applies, such as `too_large` or `not_runnable`. `data_missing` now means
public nowhere. The README table leaves these claims out, and each
dandiset's page shows them in a line of their own.

Attempts recorded under pilot-6 keep their claims as they are.

docs/protocol.md:137:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:206:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:207:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:240:   - The notes of a `with_inputs` claim say which side a difference comes
```

**Agent**

`data` labels are consistent: IBL-only tests are `elsewhere`, and KI tests that use outside data are `with_inputs`. Adding a claim for the Fig. 5g tuning maps, a reported finding with no claim yet.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "- id: fig5h-choice-gao-hierarchy",
 "new_string": "- id: fig5g-tuning-maps\n  statement: Across 73 IBL ROIs, choice-tuned units are enriched in a territory spanning central\n    MOs, FRP and anterior ACAd, ORBvl and PL, and consistently depleted in ILA, ORBm, ORBl and\n    ACAv; feedback-tuned units are enriched in AId, FRP and anterior MOs, ORBvl and PL, and\n    depleted in ILA, ORBm and ACAd/ACAv; visual stimulus tuning is strongly enriched in a single\n    IBL ROI in MOs.\n  source: Figure 5g; Extended Data Fig. 9c; Results, Mapping task variables during goal-directed\n    behavior, paragraphs 2 and 3\n  quote: Choice-tuned units ( n = 1,109 units) were enriched in a spatially cohesive territory\n    spanning central MOs, the FRP and the anterior parts of ACAd, ORBvl and PL; ILA, ORBm, ORBl and\n    ACAv were consistently depleted in choice-tuned units (Fig. 5g ). Feedback-tuned units ( n =\n    2,868 units) were enriched in AId, FRP and anterior parts of MOs, ORBvl and PL, while they were\n    depleted in ILA, ORBm and ACAd/ACAv\n  data: elsewhere\n  where: IBL Brain Wide Map, https://registry.opendata.aws/ibl-brain-wide-map/ (release accessed\n    February 2024; no release tag is given)\n  expected:\n  - quantity: IBL ROIs\n    value: 73\n    tolerance: 7\n  depends_on:\n  - fig5g-tuned-unit-counts\n  criterion: IBL ROIs from the dataset IBL deep-layer PFC ww units, parcellated as in\n    fig4b-dataroi-parcellation (Methods, Parcellation into ROIs of similar unit count). E-scores of\n    tuned against untuned units per IBL ROI with at least 20 units, 1,000 shuffles (Methods); the\n    grouping is not stated (readings as in fig5h-choice-gao-hierarchy; the code's 2,000 shuffles\n    grouped by 'task', calc_statsdict_tuning.py, a variant). The text gives no rule for\n    \"enriched\" or \"depleted\" in a territory; readings (a) a significant E-score of that sign, (b)\n    an E-score of that sign. Enriched is judged per subregion as at least one IBL ROI of the\n    subregion enriched; \"consistently depleted\" and \"depleted\" as every IBL ROI of the subregion\n    with a negative E-score (under (a), none significantly positive and at least one significantly\n    negative). Reproduced when every named subregion meets its part for choice and for feedback,\n    and exactly one IBL ROI, in MOs, has a significant positive E-score for visual tuning, under\n    both readings; partially reproduced when choice or feedback holds alone. \"Anterior\" and\n    \"central\" are not tested, as the flatmap axes are not given in the text.\n- id: fig5h-choice-gao-hierarchy"
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "  quote: Choice-tuned units ( n = 1,109 units) were enriched in a spatially cohesive territory\n    spanning central",
 "new_string": "  quote: with a single IBL ROI in the MOs showing strong enrichment (Fig. 5g ). Choice-tuned units (\n    n = 1,109 units) were enriched in a spatially cohesive territory spanning central"
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001260/10.1038-s41593-025-02190-z.yaml",
 "old_string": "  source: Methods, Detection of sleep-like periods and Epoch selection\n",
 "new_string": "  source: Methods, Detection of sleep-like periods and Epoch selection; Extended Data Fig. 1 legend,\n    Data (unit count)\n"
}
```

```
The file claims/001260/10.1038-s41593-025-02190-z.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
tail -5 claims/001260/10.1038-s41593-025-02190-z.yaml; grep -n "^checks" claims/001260/*.yaml
```

```
distributions were not significantly different across behavioral settings
  criterion: A claim of absence, but the paper names no test in the text read; the Supplementary
    Methods, which may give it, were not read. The claim is blocked as methods_underspecified
    unless a reader answers with the paper's test. As a variant only, a mixed model Metric ~ 1 +
    Setting + (1|Mouse) per metric for ww units, with the size of the setting effects.
```

**Agent calls Bash**

```bash
grep -l "^checks:" claims/*/*.yaml | head -1 | xargs -I{} sh -c "sed -n '/^checks:/,\$p' {} | head -25"
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
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/001260/10.1038-s41593-025-02190-z.yaml <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header. The ROI minimum was "more than 20 units"; Fig. 4f and Extended Data Figs. 7i and 9d say ROIs with at least 20 units were analyzed. Now at least 20, with the code's > 20 (most dataset KI scripts, while its IBL scripts use >= 20) as a variant; for brain regions the text gives no minimum and the code's value is used.
  - Header. The preprint gives 23,386 units in its Results and 23,667 in its legends; the header named only the first while fig1h-waveform-classes cites the second. Both are now named.
  - dataset-ki-counts. Added the PFC unit count of the Extended Data Fig. 1b legend (12,674), the number behind the 52%.
  - fig1i-nw-higher-metrics. The Methods and the Fig. 1i legend correct the post hoc F tests for multiple comparisons (Tukey); the criterion left this out.
  - extfig1d-sleep-like-differ. The criterion compared only units with enough active and sleep-like epochs; the Extended Data Fig. 1 legend gives two samples, 19,186 ww units for active epochs and 11,599 for sleep-like epochs. Now uses them, adds the Tukey correction, and says that the count of metrics required is the file's rule (all three for reproduced, one or two for partial), as the per-metric marks are in the figure only.
  - extfig1-epoch-counts. Added the 11,599 ww units with enough sleep-like epochs as an expected value, and the legend to the source.
  - fig2e-category-stability. The criterion defined stability on the matrix summed over transitions; the Methods define it per transition (M_t) and Fig. 2e plots it per transition. Now per transition, with the mean over transitions and the pooled value as the two readings of "around 57%".
  - extfig3f-layer-enrichment. Removed the requirement that L2/3 have no significant enrichment in categories 1 to 3, which the paper does not state.
  - fig2j-nw-ww-correspondence. "Regions with more than 20 nw units" was given as the Fig. 2j legend's; the legend says only "sufficient nw units". Now named as the code's threshold, with the region count reported against 9.
  - fig4cd-dataroi-enrichment. The statement's ORBl part (most ventral dataROI) was not in the criterion. Now said to be untested, as the flatmap axes are not in the text, and the ORBl dataROI with the highest category 7 and 8 E-scores is reported.
  - fig4g-gao-category1. ROI minimum set to at least 20 units (Extended Data Fig. 7i), > 20 as a variant.
  - fig5b-tone-categories. Which units the tone SOM is trained on was not stated. The Results give deep-layer ww units (n = 15,352); the code's runCresp*_brain settings use all ww units of all layers. Both are now named as readings, judged on the 7,184 PFC deep ww units of the Fig. 5 legend.
  - fig5h-choice-gao-hierarchy. ROI minimum set to at least 20 (Extended Data Fig. 9d); 1,000 shuffles from the Methods stated; the code's 2,000 shuffles grouped by 'task' added as a variant.
  - fig5k-task-tuning-category4. The criterion followed the code's 2,000 shuffles grouped by setting and region, against the Methods' 1,000 shuffles; the Methods name no grouping for Fig. 5k. Now 1,000 shuffles, with no grouping and the code's grouping as two readings, 2,000 shuffles as a variant, and disagreeing readings blocking the claim.
  - Added claim fig5g-tuning-maps (Fig. 5g enrichment maps of choice, feedback and visual tuning across 73 IBL ROIs), a Results finding with no claim. The paper gives no rule for enriched or depleted territories, so the criterion names two readings.
  - Open, not settled. Several criteria judge figure-only findings by rules this file chose, as the paper gives no measure or test. These are fig2a-som-memory-burstiness (angle 60 to 120 degrees, top 10% or 25% of memory nodes), fig2b-pfc-regular-territory (Mann-Whitney and chi-square on unit metrics), fig2f-low-rate-less-stable (part 2 group rule), fig4e-activity-modules, fig5b-tone-categories (IQR of ZETA onsets), fig5e-tone-responsive-patches (three subregions), fig5j-tone-responsive-high-rate (summed E-scores, four of five categories) and fig5g-tuning-maps. Each says so; an outcome that rests on them is weaker than one on the paper's own test.
  - Open, not settled. The Supplementary Information (Supplementary Methods, Tables 1 to 7) and the figures themselves were not available. The groups of the behavioral-setting control (G1), the test behind methods-settings-no-difference, and the p-values of the E-scores and of the within-PFC hierarchy correlations remain unread.
  - Open, not settled. Secondary findings without a claim are the corroboration of the dataROI profiles and modules with GaoROIs (Extended Data Fig. 7e to h, Supplementary Table 7), the occupancy differences across PFC subregions on the SOM (Extended Data Fig. 2f), the nw stability (Extended Data Fig. 5e,f) and the match of block-wise and full-data categories (Extended Data Fig. 3c).
EOF
python tools/claims_check.py claims/001260/10.1038-s41593-025-02190-z.yaml paper/10.1038-s41593-025-02190-z.txt; grep -n "—\|rather" claims/001260/*.yaml | grep -v "quote\|^.*rather than cytoarchitecture" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import re
for i,l in enumerate(open('claims/001260/10.1038-s41593-025-02190-z.yaml'),1):
    if l.startswith('#'): continue
    s=l.strip()
    s=re.sub(r'^(- )?[a-z_]+: ','',s)
    s=re.sub(r'^- ','',s)
    if ': ' in s: print(i,l.rstrip()[:120])
EOF
git status --short
```

```
M claims/001260/10.1038-s41593-025-02190-z.yaml
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

The claims file is ready for an attempt. I changed 13 claims, added one, and recorded the changes under `checks` with `ready: true`.

**Checker:** before my edits it reported `38 claims, 38 quotes, 1 statistical values, 0 problems`; after them, `39 claims, 39 quotes, 1 statistical values, 0 problems`.

**Changes, by claim**
- **Header:**
  - ROIs need at least 20 units, as the Fig. 4f and Extended Data Fig. 7i and 9d legends say; the file said "more than 20". I checked the paper's code at the pinned commit: most dataset KI scripts keep counts above 20 and the IBL scripts keep 20 or more, so "more than 20" is now a variant.
  - It now gives both preprint unit counts (23,386 and 23,667).
- **dataset-ki-counts:** added the PFC unit count from the Extended Data Fig. 1b legend (12,674) as an expected value.
- **fig1i-nw-higher-metrics:** added Tukey's correction for multiple comparisons, which the Methods and the legend state.
- **extfig1d-sleep-like-differ:**
  - The comparison now uses the legend's two separate samples: 19,186 ww units for active epochs and 11,599 for sleep-like epochs.
  - Added Tukey's correction.
  - The criterion now says the number of metrics required is the file's own rule.
- **extfig1-epoch-counts:** added 11,599 as an expected value and the legend to the source.
- **fig2e-category-stability:** stability is now computed per transition, as the Methods define it, and "around 57%" has two readings: the mean over transitions or the pooled value.
- **extfig3f-layer-enrichment:** removed a condition the paper doesn't state (L2/3 not enriched in categories 1 to 3).
- **fig2j-nw-ww-correspondence:** the "more than 20 nw units" threshold came from the code, not the legend, which says only "sufficient". It is now labelled as the code's.
- **fig4cd-dataroi-enrichment:** the "most ventral ORBl dataROI" part is marked untested, because the text doesn't give the flatmap's axes.
- **fig4g-gao-category1 and fig5h-choice-gao-hierarchy:** minimum set to at least 20 units. fig5h now states the Methods' 1,000 shuffles, with the code's 2,000 shuffles grouped by `task` as a variant.
- **fig5b-tone-categories:** which units train the tone SOM is now open, with two readings. The Results say deep-layer ww units (n = 15,352); the code uses all ww units in every layer.
- **fig5k-task-tuning-category4:** the main test followed the code's 2,000 shuffles over the Methods' 1,000. It now uses 1,000. Grouping, which the Methods don't give for this figure, has two readings, and disagreeing readings block the claim.
- **Added fig5g-tuning-maps:** the Fig. 5g maps of choice, feedback and visual tuning across 73 IBL ROIs, a Results finding that had no claim.

**Still open**
- Several criteria for findings shown only in figures rest on rules this file chose, because the paper gives no measure or test: fig2a, fig2b, fig2f part 2, fig4e, fig5b, fig5e, fig5j and fig5g-tuning-maps.
- The Supplementary Information was not available, nor the figures themselves. So the grouping by behavioral setting (G1), the test behind methods-settings-no-difference, and the E-score p-values (Supplementary Tables 1 to 7) are unread.
- Some minor findings have no claim: the GaoROI corroboration (Extended Data Fig. 7e–h), SOM occupancy by PFC subregion (Extended Data Fig. 2f), nw-unit category stability (Extended Data Fig. 5e,f) and Extended Data Fig. 3c.

Nothing was committed.

## End of run

39 turns, 4 minutes, result: success.
