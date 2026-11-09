# 001893 · claims · run 41774898552

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/001453/ claims/001893/ 2>&1; head -c 3000 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8d3f0361-ab65-41aa-b007-727d7e0e525a/tool-results/bgynggsyl.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 650 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -c *; grep -n -i "^#\|^Methods\|^Supplementary\|Extended Data Fig. 1\b\|patch-seq\|dandi\|github\|code availability\|data availability" *.txt | head -120
```

```
<persisted-output>
Output too large (241.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8d3f0361-ab65-41aa-b007-727d7e0e525a/tool-results/b1p7mxxp6.txt

Preview (first 2KB):
249584 10.1038-s41586-026-11026-0.txt
212414 10.64898-2026.04.10.717727.txt
461998 total
10.1038-s41586-026-11026-0.txt:268:Download PDF Abstract Noradrenaline (also known as norepinephrine) is released throughout most of the central nervous system by neurons in the locus coeruleus 1 , 2 , 3 , 4 . Here we identified a relationship between the morphologies, gene expression and activity of noradrenergic neurons in locus coeruleus in mice. Axonal projections of individual neurons were extensive but largely confined to subsets of brain regions. Axonal projections and graded gene expression correlated with locations of cell bodies in locus coeruleus. In a behavioural task requiring continuous learning from actions, dorsal locus coeruleus neurons projecting to isocortex were activated when mice switched choices and by reward-prediction-error signals that drive learning. Background activity of neurons in ventral locus coeruleus was higher when mice ignored stimuli indicating potential reward availability. These observations reveal a topographically organized structure and function of a neurotransmitter system and show that it contains learning signals for flexible behaviour. Similar content being viewed by others Locus coeruleus α-synuclein overexpression induces prodromal Parkinsonian features in mice Article Open access 08 June 2026 Spatiotemporal dynamics of noradrenaline during learned behaviour Article 01 June 2022 Generation of locus coeruleus norepinephrine neurons from human pluripotent stem cells Article Open access 16 November 2023 Explore related subjects Discover the latest articles and news in related subjects. Cellular neuroscience Reward Sex Differences in Stress Response Mechanisms Main Monoamine neurotransmitters are released by small populati
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)}' 10.1038-s41586-026-11026-0.txt | sort -t: -k2 -n -r | head -5; grep -n "^## " 10.64898-2026.04.10.717727.txt
```

```
268: 221376
13: 909
126: 302
70: 286
76: 277
9:## Abstract
13:## Introduction
21:## Results
23:## LC-NE projections are spatially organized
29:## Spatial distribution of LC-NE neurons.
35:## Organization of LC-NE neurons and their brain-wide projections.
43:## Brain-wide projections of LC-NE neurons in the right hemisphere.
51:## Individual LC-NE morphologies.
57:## Spatial distribution of LC-NE axon innervation.
63:## LC-NE projections are spatially organized.
73:## LC-NE projections measured with MAPseq and BARseq.
81:## Somatodendritic morphologies of LC-NE neurons vary continuously.
87:## Retrograde tracing to quantify locations of somata with projections to olfactory bulb, frontal cortex, thalamus, periaqueductal gray, cerebellar cortex, or spinal cord.
91:## LC-NE neurons have graded gene expression in space
97:## LC-NE neurons have distinct gene expression from surrounding cells.
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 268p 10.1038-s41586-026-11026-0.txt | fold -w 3000 > $TMPDIR/vor.txt; wc -l $TMPDIR/vor.txt; grep -o -i "patch-seq[^.]*\." 10.1038-s41586-026-11026-0.txt | head -50; sed -n 1,267p 10.1038-s41586-026-11026-0.txt | grep -v "^\[" | grep -v "^$" | head -60
```

```
73 /tmp/claude-1001/vor.txt
Patch-seq Transgenic mice and labelling projection neurons Heterozygous Dbh -Cre mice crossed with homozygous Ai65 mice (P28–P30) were anaesthetized with 2.
Patch-seq experiments.
Patch-seq recordings Slices were bathed in warm (34 °C) recording ACSF (2 mM calcium chloride (dihydrate), 12.
Patch-seq experiments, we reverse transcribed the collected nuclear and cytosolic mRNA, and sequenced the resulting cDNA using a SMART-Seq v4 method 41 , 48 .
Patch-seq dataset.
Patch-seq experiments were mounted on slides and imaged on an upright AxioImager Z2 microscope (Zeiss, Germany) with an Axiocam 506 monochrome camera and 0.
DOI: 10.1038/s41586-026-11026-0
Version: as served by crossref
Source: crossref+publisher_html (paper-text-fetcher)
Stored: 2026-10-21
Extracted: as fetched
------------------------------------------------------------------------
Topographic structure and function of locus coeruleus noradrenaline neurons
Abstract
                    Noradrenaline (also known as norepinephrine) is released throughout most of the central nervous system by neurons in the locus coeruleus
                    1–4
                    . Here we identified a relationship between the morphologies, gene expression and activity of noradrenergic neurons in locus coeruleus in mice. Axonal projections of individual neurons were extensive but largely confined to subsets of brain regions. Axonal projections and graded gene expression correlated with locations of cell bodies in locus coeruleus. In a behavioural task requiring continuous learning from actions, dorsal locus coeruleus neurons projecting to isocortex were activated when mice switched choices and by reward-prediction-error signals that drive learning. Background activity of neurons in ventral locus coeruleus was higher when mice ignored stimuli indicating potential reward availability. These observations reveal a topographically organized structure and function of a neurotransmitter system and sho
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/vor.txt"
}
```

```
1	Download PDF Abstract Noradrenaline (also known as norepinephrine) is released throughout most of the central nervous system by neurons in the locus coeruleus 1 , 2 , 3 , 4 . Here we identified a relationship between the morphologies, gene expression and activity of noradrenergic neurons in locus coeruleus in mice. Axonal projections of individual neurons were extensive but largely confined to subsets of brain regions. Axonal projections and graded gene expression correlated with locations of cell bodies in locus coeruleus. In a behavioural task requiring continuous learning from actions, dorsal locus coeruleus neurons projecting to isocortex were activated when mice switched choices and by reward-prediction-error signals that drive learning. Background activity of neurons in ventral locus coeruleus was higher when mice ignored stimuli indicating potential reward availability. These observations reveal a topographically organized structure and function of a neurotransmitter system and show that it contains learning signals for flexible behaviour. Similar content being viewed by others Locus coeruleus α-synuclein overexpression induces prodromal Parkinsonian features in mice Article Open access 08 June 2026 Spatiotemporal dynamics of noradrenaline during learned behaviour Article 01 June 2022 Generation of locus coeruleus norepinephrine neurons from human pluripotent stem cells Article Open access 16 November 2023 Explore related subjects Discover the latest articles and news in related subjects. Cellular neuroscience Reward Sex Differences in Stress Response Mechanisms Main Monoamine neurotransmitters are released by small populations of neurons that project extensively throughout the central nervous system (CNS). The locus coeruleus (LC) in the pons supplies the monoamine noradrenaline to most of the CNS 1 , 2 , 3 , 4 . Noradrenaline binds G-protein-coupled receptors on neurons and glia, activating intracellular signalling pathways 5 and gating synaptic plasticit
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -o "Patch-seq Transgenic.\{0,9000\}" vor.txt | head -c 12000
```

```
Exit code 143
Command timed out after 1h 0m 0s
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1038-s41586-026-11026-0.txt').read()
i=t.find('Patch-seq Transgenic'); print(t[i:i+9000])"
```

```
Patch-seq Transgenic mice and labelling projection neurons Heterozygous Dbh -Cre mice crossed with homozygous Ai65 mice (P28–P30) were anaesthetized with 2.0% isoflurane in O 2 and maintained at 0.7–1.0% isoflurane throughout surgery. Mice were mounted in a stereotaxic frame (David Kopf Instruments) for injections of AAV pEF1a-DIO-FLPo-WPRE-hGHpA (Addgene 87306-AAVrg, lot v188462). Small craniotomies were made in the skull above the injection target for intracerebral injections 89 . Spinal cord injections were made between C4–C5 vertebrae without drilling 90 . Intracerebral injections were in the right hemisphere. Spinal cord injections were bilateral. Mice recovered in their home cage for approximately 21 days before Patch-seq experiments. Tissue processing For preparation of acute brain slices, adult male and female mice (50–74 days old) were first fully anaesthetized by 5% isoflurane inhalation. A transcardial perfusion was then performed with ~10 ml of ice-cold cutting artificial cerebrospinal fluid (ACSF; 0.5 mM calcium chloride (dihydrate), 25 mM d -glucose, 20 mM HEPES buffer, 10 mM magnesium sulfate, 1.25 mM sodium phosphate monobasic monohydrate, 3 mM myo-inositol, 12 mM N -acetyl- l -cysteine, 96 mM N -methyl- d -glucamine chloride (NMDG-Cl), 2.5 mM potassium chloride, 25 mM sodium bicarbonate, 5 mM sodium l -ascorbate, 3 mM sodium pyruvate, 0.01 mM taurine, and 2 mM thiourea (pH 7.3), which had been continuously bubbling with a mixture of 95% O 2 /5% CO 2 ). Coronal or sagittal sections (thickness 350 μm) containing the LC were sliced on a vibrating microtome (VT1200S Vibratome, Leica Biosystems). Immediately after slicing, brain slices were placed in warm (34 °C) oxygenated cutting ACSF for 10 min, then allowed to further recover in holding ACSF (2 mM calcium chloride (dihydrate), 25 mM d -glucose, 20 mM HEPES buffer, 2 mM magnesium sulfate, 1.25 mM sodium phosphate monobasic monohydrate, 3 mM myo-inositol, 12.3 mM N -acetyl- l -cysteine, 84 mM sodium ch
[... 1 more lines not kept]
```

**Agent**

Now the Extended Data legends, statistics, and data/code availability.

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1038-s41586-026-11026-0.txt').read()
import re
for k in ['Extended Data Fig. 11:','Extended Data Fig. 10:','Data availability','Code availability','Supplementary Information','Statistics','Reporting summary']:
  for m in re.finditer(re.escape(k),t):
    print('=====',k,m.start())
i=t.find('Data availability'); print(t[i:i+3000])
"
```

```
===== Data availability 191301
===== Code availability 191603
===== Statistics 231888
===== Reporting summary 191165
Data availability Data are available at https://github.com/AllenNeuralDynamics/locus_coeruleus_norepinephrine_neurons , https://assets.nemoarchive.org/col-p9d5w39 and https://codeocean.allenneuraldynamics.org/collections/9cf044ce-93c7−4c7e-bfa1-5d8c37aa42ec . Source data are provided with this paper. Code availability Code is available at https://github.com/AllenNeuralDynamics/locus_coeruleus_norepinephrine_neurons and https://codeocean.allenneuraldynamics.org/collections/9cf044ce-93c7−4c7e-bfa1−5d8c37aa42ec . References Swanson, L. W. The locus coeruleus: a cytoarchitectonic, Golgi and immunohistochemical study in the albino rat. Brain Res. 110 , 39–56 (1976). Article CAS PubMed Google Scholar Amaral, D. G. & Sinnamon, H. M. The locus coeruleus: neurobiology of a central noradrenergic nucleus. Prog. Neurobiol. 9 , 147–196 (1977). Article CAS PubMed Google Scholar Jones, B. E. & Moore, R. Y. Ascending projections of the locus coeruleus in the rat. II. Autoradiographic study. Brain Res. 127 , 25–53 (1977). Article CAS PubMed Google Scholar Foote, S. L., Bloom, F. E. & Aston-Jones, G. Nucleus locus ceruleus: new evidence of anatomical and physiological specificity. Physiol. Rev. 63 , 844–914 (1983). Article CAS PubMed Google Scholar Hein, L. Adrenoceptors and signal transduction in neurons. Cell Tissue Res. 326 , 541–551 (2006). Article CAS PubMed Google Scholar Seol, G. H. et al. Neuromodulators control the polarity of spike-timing-dependent synaptic plasticity. Neuron 55 , 919–929 (2007). Article CAS PubMed PubMed Central Google Scholar Tully, K. & Bolshakov, V. Y. Emotional enhancement of memory: how norepinephrine enables synaptic plasticity. Mol. Brain 3 , 15 (2010). Article PubMed PubMed Central Google Scholar Bergles, D. E., Doze, V. A., Madison, D. V. & Smith, S. J. Excitatory actions of norepinephrine on multiple classes of hippocampal CA1 inte
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1038-s41586-026-11026-0.txt').read()
i=t.find('Statistics',231000); print(t[231000-200:])
" | head -c 20000
```

```
scription. Source data Extended Data Fig. 7 MERFISH analysis. a , CCA analyses of population gene expression. b , CI around CCA analysis of population gene expression. c , Example genes with spatial gradients from MERFISH data. Source data Extended Data Fig. 8 Retro-seq. a , GradientBoosting classifiers were trained on the retro-seq dataset (raw counts) to predict projection targets. b , Retro-seq cells embedded by PCA using the scVI normalized counts. Projection target labels were restricted to frontal cortex, cerebellum, and spinal cord. c , Right: projection targets were imputed onto snRNA-seq cells by k-nearest neighbor matching (k = 10). Cells were assigned by majority vote among labeled neighbors with \(\ge \) 80% agreement; otherwise left unassigned. Left, inferred projection target; middle, imputation disagreement score (1 \(-\) nmax/nvalid,), where (nmax) is the count of the most frequent neighbor label and (nvalid) is the number of labelled neighbors (range 0–1). Only the first two subpanels of the three-panel display are shown. Source data Extended Data Fig. 9 Statistics of behavior. a , Distributions of behavioral performance statistics. b , Example lick raster aligned to start of choice. Blue: rewarded trials. Red: unrewarded trials. c , Example mean licking rate of sessions with reward latency of 200 ms and 300 ms. d , Top: distribution of lick latencies of stay and switch trials. Bottom: lick latency of switch vs. stay choices. Each dot is one session. e , Example in-trial licks (black) and spontaneous licks (gray). f , Example video frame. g , Licks detected by video aligned to go cue. Top: example rewarded and unrewarded trials. Bottom: example session’s lick time distribution. h , Lick preference (left/right) in spontaneous period vs. normalized reward ratios (left/right) in the task (Pearson’s \(r=0.39\) , \(p=1.54\times {10}^{-10}\) ). i , % of licks in task vs. deviation of lick preference from reward ratio shown in h (Spearman’s \(r=-0.17\) , \
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 155,175p 10.64898-2026.04.10.717727.txt; sed -n 505,530p 10.64898-2026.04.10.717727.txt; grep -n -i "supplementary table\|welch\|time constant\|IPFX\|upstroke\|patch clamp\|whole-cell" 10.64898-2026.04.10.717727.txt | cut -c1-400
```

```
## Identifying LC-NE neurons in vivo .

a , ChRmine, Chrimson, or ChR2 were injected into LC of Dbh -Cre animals for optical identification with Neuropixels probes or tetrodes. b , Expression of ChR2 in LC-NE neurons. Scale bar: 50 µm. c , Example raw trace of a tetrode recording with spikes following laser stimulation (blue ticks). d , Two example identified LC-NE neurons in response to multiple trains of light stimuli. e , Quality metrics of LC-NE neurons. Gray: single units. Black: identified as NE neurons. Top row: basic quality metrics of neurons; bottom row: waveform similarity between stimulated and spontaneous spikes. f , Distribution of laser-evoked response properties for identified NE neurons and unidentified neurons. g , Schema for antidromic stimulation: ChRmine was injected into LC of Dbh -Cre animals. To perform antidromic stimulation, light was delivered to the brain surface through the skull over frontal cortex. h , Expression of ChRmine in LC-NE neurons. Scale bar: 20 µm. i , Example antidromic stimulation. Top row: antidromic spikes; Bottom row: collision when a spontaneous spike preceded the antidromic spike. j , Example antidromic stimulation across trials. Top: Rows are sorted by the time of first spike. Bottom: mean spike rate aligned to the time of antidromic stimulation. a is antidromic latency, defined as the time of peak mean spike rate aligned to time of laser stimulation; b is jitter, defined as the half peak width of mean spike rate aligned to laser stimulation; c is antidromic window, during which if a spontaneous spike occurred, a collision occurred. k , Distribution of antidromic response properties of all identified LC-NE neurons, identified to project to cortex (black) or not (gray). t -statistics are log-scaled for ease of visualization. l , Distribution of light-evoked response jitter of LC-NE cells, identified to project to cortex versus not. m , Distribution of all identified NE neurons in space, highlighting cortex-projecting 
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 300 git clone -q https://github.com/AllenNeuralDynamics/locus_coeruleus_norepinephrine_neurons lcrepo 2>&1 | tail -3; cd lcrepo && git log -1 --format='%H %cd' && git ls-files | head -100 && git ls-files | wc -l
```

```
43f7083df17042afc23917edfa59183ef166a972 Wed Sep 16 13:04:55 2026 -0700
.github/ISSUE_TEMPLATE/bug_report.md
.github/ISSUE_TEMPLATE/feature_request.md
.github/ISSUE_TEMPLATE/user-story.md
.gitignore
CITATION.cff
CODE_OF_CONDUCT.md
LICENSE
README.md
8
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat $TMPDIR/lcrepo/README.md; cd $TMPDIR/lcrepo; git branch -a; git log --oneline | head
```

```
# Locus Coeruleus Norepinephrine Neurons

This repository is an index of the computational capsules associated with our publication on locus coeruleus norepinephrine (LC-NE) neurons. Each capsule contains the code, environment, and links to data needed to reproduce the corresponding analyses and figures.

The full collection is also available as a public Code Ocean collection:
[https://codeocean.allenneuraldynamics.org/collections/9cf044ce-93c7-4c7e-bfa1-5d8c37aa42ec](https://codeocean.allenneuraldynamics.org/collections/9cf044ce-93c7-4c7e-bfa1-5d8c37aa42ec)

## Capsules

| # | Capsule | Description | GitHub | Code Ocean |
|---|---------|-------------|--------|------------|
| 1 | trailmap_with_point_calls | Immunolabeling in cleared brains: LC-NE neuron definition and brain-wide projection imaging (data prep) | [GitHub](https://github.com/AllenNeuralDynamics/trailmap_with_point_calls) | [Code Ocean](https://codeocean.allenneuraldynamics.org/capsule/0999722/tree) |
| 2 | LC_H2B_points_to_mesh | Figure generation from LC-NE point data | [GitHub](https://github.com/AllenNeuralDynamics/LC_H2B_points_to_mesh) | [Code Ocean](https://codeocean.allenneuraldynamics.org/capsule/8736312/tree) |
| 3 | aind-LC-morphologies | ExA-SPIM single neuron reconstructions projection analysis | [GitHub](https://github.com/AllenNeuralDynamics/aind-LC-morphologies) | [Code Ocean](https://codeocean.allenneuraldynamics.org/capsule/5888750/tree) |
| 4 | LC somatodendritic morphology analysis | ExA-SPIM somatodendritic morphology analysis | [GitHub](https://github.com/AllenNeuralDynamics/LC-somatodendritic-morphology) | [Code Ocean](https://codeocean.allenneuraldynamics.org/capsule/7421970/tree) |
| 5 | aind-LC-morphologies_supplemental_figure | Supplemental analysis of LC reconstruction Markov models | [GitHub](https://github.com/AllenNeuralDynamics/aind-LC-morphologies_supplemental_figure) | [Code Ocean](https://codeocean.allenneuraldynamics.org/capsule/7470432/tree) |
| 6 | LC-NE_retrograde_
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 300 git clone -q https://github.com/AllenNeuralDynamics/LCNE-patchseq-figures pseq 2>&1|tail -3; cd pseq && git log -1 --format='%H %cd' && git ls-files | head -200
```

```
79fa20aff7f0195140fac6584962814562c33922 Wed Oct 7 22:05:26 2026 +0000
.codeocean/environment.json
.codeocean/resources.json
.gitignore
LICENSE
README.md
code/dandi_assets.py
code/data/LCNE_patchseq_S14_cell_table.csv
code/ephys.py
code/example_traces.py
code/generate_S14jk.py
code/run
code/spikes.py
environment/Dockerfile
environment/postInstall
metadata/metadata.yml
tests/test_dandi_assets.py
tests/test_example_traces.py
tests/test_generate_S14jk.py
tests/test_nwb_sweeps.py
[... 3 more lines not kept]
```

**Agent**

The linked index points to a Patch-seq capsule, `LCNE-patchseq-figures`, which builds Extended Data Fig. 11j,k from DANDI. Reading it now.

**Agent calls Bash**

```bash
cd $TMPDIR/pseq; cat README.md code/run metadata/metadata.yml; cat code/generate_S14jk.py; head -5 code/data/LCNE_patchseq_S14_cell_table.csv; wc -l code/data/LCNE_patchseq_S14_cell_table.csv
```

```
# LCNE patch-seq figures

This repository is the GitHub source for a Code Ocean capsule that creates
supplementary figure S14j/k from the publication
[Topographic structure and function of locus coeruleus norepinephrine neurons](https://doi.org/10.64898/2026.04.10.717727)
(Su et al., 2026). The analysis downloads intracellular electrophysiology
recordings from DANDI, computes the action-potential waveform PC1 and
the example current-clamp traces in panel j, and writes the figure and all
supporting data to `/results`.

## Resources

| Resource | Description |
| --- | --- |
| [Figures repository](https://github.com/AllenNeuralDynamics/LCNE-patchseq-figures) | This capsule's code, environment, metadata, and frozen inputs |
| [Code Ocean capsule](https://codeocean.allenneuraldynamics.org/capsule/9190472/tree) | Reproducible environment and run interface for figure S14j/k |
| [DANDIset 001893](https://dandiarchive.org/dandiset/001893/) | Raw intracellular current-clamp NWB recordings |
| [NeMO collection](https://assets.nemoarchive.org/col-p9d5w39) | Associated transcriptomic data collection (not used for manuscript figures) |
| [Analysis repository](https://github.com/AllenNeuralDynamics/LCNE-patchseq-analysis) | Full multimodal analysis code (for exploratio beyond manuscript figures)|

[... 525 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pseq; cat code/spikes.py; sed -n 1,200p code/dandi_assets.py
```

```
"""Recompute representative spike waveforms from raw patch-seq sweeps."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from ephys import (
    CurrentClampSweep,
    NwbSource,
    list_current_clamp_sweeps,
    load_current_clamp_sweep,
)

LONG_SQUARE_RHEO_LABELS = ("X3LP_Rheo_DA_0", "X5LP_Rheo_DA_0")
SPIKE_THRESHOLD_MV = -10.0
SPIKE_WINDOW_MS = (-5.0, 10.0)

[... 235 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 300 git clone -q https://github.com/AllenNeuralDynamics/LCNE-patchseq-analysis pana 2>&1|tail -3; cd pana && git log -1 --format='%H %cd' && git ls-files | grep -v -i "\.png$\|\.svg$" | head -150; grep -rn -i "tau" --include=*.py . | grep -v test | head -40
```

```
1190697203164593d0f82234f7320a08a8073097 Mon Jul 13 23:15:53 2026 +0000
.claude/settings.local.json
.codeocean/app-panel.json
.codeocean/datasets.json
.codeocean/resources.json
.flake8
.gitattributes
.github/ISSUE_TEMPLATE/bug_report.md
.github/ISSUE_TEMPLATE/feature_request.md
.github/ISSUE_TEMPLATE/user-story.md
.github/workflows/init.yml
.github/workflows/tag_and_publish.yml
.github/workflows/test_and_lint.yml
.gitignore
LICENSE
README.md
assets/fonts/Helvetica.ttf
code/export_S14_metadata.py
code/generate_S14jk.py
code/run
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pana; grep -n -i "ipfx\|tau" src/LCNE_patchseq_analysis/pipeline_util/*.py | head -30; sed -n 1,60p README.md
```

```
src/LCNE_patchseq_analysis/pipeline_util/metadata.py:37:    tab_ephys_fx = "ipfx_ephys_250709"
src/LCNE_patchseq_analysis/pipeline_util/metadata.py:40:    # Add "ipfx_" prefix to ephys_fx columns except for "cell_specimen_id"
src/LCNE_patchseq_analysis/pipeline_util/metadata.py:42:        columns=lambda x: f"ipfx_{x}" if x != "cell_specimen_id" else x
src/LCNE_patchseq_analysis/pipeline_util/metadata.py:119:    column_to_log = ["recording_date", "x", "ipfx_tau"]
src/LCNE_patchseq_analysis/pipeline_util/sequencing.py:32:    "imp_pseudoclusters_softmax_tau0p1_k100",
src/LCNE_patchseq_analysis/pipeline_util/sequencing.py:33:    "imp_pseudoclusters_softmax_tau0p5_k100",
src/LCNE_patchseq_analysis/pipeline_util/sequencing.py:180:                "pc_softmax_tau0p1": "imp_pseudoclusters_softmax_tau0p1_k100",
src/LCNE_patchseq_analysis/pipeline_util/sequencing.py:181:                "pc_softmax_tau0p5": "imp_pseudoclusters_softmax_tau0p5_k100",
src/LCNE_patchseq_analysis/pipeline_util/sequencing.py:190:            "imp_pseudoclusters_softmax_tau0p1_k100",
src/LCNE_patchseq_analysis/pipeline_util/sequencing.py:191:            "imp_pseudoclusters_softmax_tau0p5_k100",
# LCNE-patchseq-analysis

[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)
![Code Style](https://img.shields.io/badge/code%20style-black-black)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)
![Interrogate](https://img.shields.io/badge/interrogate-86.5%25-yellow)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?logo=codecov)
![Python](https://img.shields.io/badge/python->=3.9-blue?logo=python)

This repository is the **main entry point for reproducing the LCNE-patchseq analysis** associated with our paper. It contains the full pipeline for extracting electrophysiological features from patch-seq recordings in locus coeruleus norepinephrine (LC-NE)
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import re
t=open('paper/10.1038-s41586-026-11026-0.txt').read()
for m in re.finditer('Supplementary Table',t): print(t[max(0,m.start()-300):m.start()+100].replace('\n',' '));print('--')
"; sed -n 1,80p claims/001453/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 80,400p claims/001453/*.yaml | grep -n "^  [a-z_]*:\|^- \|^[a-z]" | awk -F: '{print $1":"$2}' | sort -t: -k2 -u | head -40; sed -n 1,60p tools/claims_check.py; ls schemas 2>/dev/null; ls
```

```
4:  criterion
18:  data
19:  depends_on
21:  expected
16:  quote
15:  source
13:  statement
47:  statistics
12:- id
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; ls targets | grep 1893; cat targets/*1893* 2>/dev/null | head -40
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
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000])"; grep -rl 001893 targets queue papers 2>/dev/null | head;
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
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items = d if isinstance(d,list) else d.get('dandisets', d)
it = [x for x in (items if isinstance(items,list) else items.values()) if '001893' in json.dumps(x)]
print(json.dumps(it,indent=1)[:3000])"; grep -n -B2 -A12 001893 papers/manifest.yaml | head -40
```

```
[
 [
  {
   "dandiset": "000003",
   "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
   "published_version": "0.260218.2052",
   "asset_count": 101,
   "size_gb": 2559.25,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "House mouse"
   ],
   "approaches": [
    "electrophysiological approach",
    "behavioral approach"
   ],
   "papers": [
    {
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
def walk(x):
  if isinstance(x,dict):
    if x.get('dandiset')=='001893': print(json.dumps(x,indent=1))
    for v in x.values(): walk(v)
  elif isinstance(x,list):
    for v in x: walk(v)
walk(d)"; grep -n -A8 001893 papers/triage.yaml
```

```
{
 "dandiset": "001893",
 "name": "Patch-seq profiling of mouse locus coeruleus norepinephrine neurons",
 "published_version": "0.260817.1647",
 "asset_count": 105,
 "size_gb": 5.67,
 "data_standards": [
  "Neurodata Without Borders (NWB)",
  "Brain Imaging Data Structure (BIDS)"
 ],
 "species": [
  "Mus musculus - House mouse"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.64898/2026.04.10.717727",
   "title": "Topographic structure and function of locus coeruleus norepinephrine neurons",
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/vor.txt",
 "offset": 19,
 "limit": 20
}
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/vor.txt",
 "offset": 39,
 "limit": 25
}
```

```
19	r temperature changes between cutting thick and thin slices. For MAPseq experiments, 3× 300-μm coronal sections were mounted in a row onto Superfrost Plus Gold slides. For BARseq experiments, 4× 20-μm sections were mounted onto Superfrost Plus Gold slides according to microfluidic chamber template. Once all cut sections were melted onto the slide, slides were rapidly frozen on dry ice and stored at –80 °C in slide boxes in vacuum sealed bags until microdissection (MAPseq) or library prep (BARseq). Regions of interest were dissected from each chilled brain slice with microscalpels pre-chilled (Fine Science Tools 10316-14). Glass slides were kept on dry ice and placed on a pre-chilled metal platform mounted above a dry ice/ethanol bath. Sections were first bisected down the midline. Then major anatomical regions (for example, isocortex, hippocampus or midbrain) were cut along their respective boundaries. Each cut was performed with a cleaned blade. Blades were rinsed in consecutive 4× 50 ml conical tubes containing ethanol stored on ice. To keep blade temperature consistently low, 3–4 scalpels were rotated and stored on the metal platform. After right hemisphere dissection was completed, a reference image for dissection boundaries was taken again for each of the 3 sections. After that, the left side was dissected along the same boundaries. Individual tissue pieces were then collected into pre-chilled microtubes (Qiagen 19560 tubes, 19566 caps) on dry ice, capped and stored at −80 °C. Left and right hemisphere samples were kept separate, and corresponding regions of interest were combined across 3 consecutive 300-μm sections mounted on the same slide. To assess cross-sample contamination, we collected tissue from uninjected brains as negative controls. After all regions of interest were collected, with samples kept on dry ice we added pre-chilled Qiagen bead (69989) to each tube. Spinal cord samples then received 800 μl Trizol, while the rest used 400 μl Trizol (The
[... 19 more lines not kept]
```

```
File content (30060 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent**

Methods for anatomy, BARseq, snRNA-seq, MERFISH, retro-seq and Patch-seq are read. One chunk is left: the in vivo physiology and spatial statistics.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/vor.txt",
 "offset": 44,
 "limit": 20
}
```

```
44	 short timescales, and post = 300 s for long timescale calculations. Abrupt drift events were detected at time t when both λ ′( t ) and \(|\hat{\lambda \text{'}}|\) exceeded 0.5, with either short or long timescale calculations. We also estimated slow drifts of the probe over long timescales. A neuron’s overall relative spike rate change over a whole session was calculated as the ratio of standard deviation of spike rate divided by mean spike rate, calculated by binning the session into non-overlapping 300-s bins. Noradrenergic neurons with this ratio higher than 0.3 (98th percentile) after being restricted to periods without abrupt drift events were excluded from analysis. To avoid potential effects of slow electrode motion on spike sorting, one drift regressor was added to all single-neuron analyses with linear regression. The drift regressor was the deviation of mean waveform amplitude on its peak channel for each trial from the mode of waveform amplitudes. Axonal calcium indicator measurements To express GCaMP6s, or jGCaMP8s 44 in LC-NE neurons, we pressure-injected within LC AAV-hSyn-FLEX-axon-GCaMP6s (1.0 × 10 13 GC ml −1 ) or AAV-hSyn-FLEX-Axon-jGCaMP8s (1.0 × 10 13 GC ml −1 ) into the LC of Dbh -Cre mice at a rate of 1 nl s −1 . pAAV-hSynapsin1-FLEx-axon-GCaMP6s was a gift from L. Tian (Addgene viral prep 112010-AAV5; RRID: Addgene_112010 ) 122 . For Axon-jGCaMP8s, based on the Axon-GCaMP6s sequence (Addgene: 112010), we PCR-amplified AvrII-Axon-jGCAMP8s-NheI. The construct was then ligated into the hSynapsin1-FLEX pAAV backbone cut from pAAV-Syn-FLEX-rc[ChrimsonR-tdTomato] (Addgene: 62723) with AvrII/NheI. Viruses were injected at following locations: from bregma, 5.4 mm posterior for male mice (400 nl), 5.2 mm posterior for female mice (300 nl); 0.85 mm bilateral; and (2.9, 3.1) mm from surface. Fibre implantation We implanted 200-μm-diameter optic fibres (0.39 NA) above prelimbic cortex (2.0 mm anterior to bregma, 0.5 mm lateral, 1.5 mm ventral from th
[... 19 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001893/10.1038-s41586-026-11026-0.yaml",
 "content": "# Claims for Su, Kosillo, Jung et al. (2026), \"Topographic structure and function of locus\n# coeruleus noradrenaline neurons\", Nature, doi:10.1038/s41586-026-11026-0, on dandiset 001893.\n#\n# Provenance. Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub\n# Actions\"), 2026-11-04, under docs/protocol.md version pilot-13 (Reader). The reader did not\n# look at the dataset's data or files; only its title and description on the archive.\n#\n# Text read. The version of record, as served by Crossref from the publisher's HTML (stored\n# 2026-10-21): main text, Methods, figure legends and Extended Data Fig. 1 to 15 legends. The\n# Supplementary Tables 1 to 3 (a PDF) are not in the text; the paper cites them only for\n# injection coordinates and volumes (Tables 1 and 2) and model priors (Table 3), and no result\n# rests on them. The bioRxiv preprint (doi:10.64898/2026.04.10.717727, version 1) was also\n# read, only to compare. It differs in places used here. Its Figure S14k legend names \"paired\n# t-tests\" where the version of record (Extended Data Fig. 11k) names two-sided Welch's\n# t-tests, and its Figure S15t p-values differ from Extended Data Fig. 12t. The version of\n# record is followed.\n#\n# Code read. (1) github.com/AllenNeuralDynamics/locus_coeruleus_norepinephrine_neurons at\n# 43f7083 (the index the paper's Code availability links), which lists one capsule per\n# analysis. (2) Capsule 13, github.com/AllenNeuralDynamics/LCNE-patchseq-figures at 79fa20a,\n# which builds Extended Data Fig. 11j,k (preprint Figure S14j,k) from dandiset 001893 version\n# 0.260817.1647. It reads 96 NWB files (sourcedata/raw/*/*_icephys.nwb, one per ephys_roi_id),\n# takes donor and projection target from the dandiset's participants.tsv (donor_local_id,\n# injection_target_region), recomputes an action-potential waveform PC1 from the raw sweeps,\n# reads the membrane time constant from a frozen table (code/data/LCNE_patchseq_S14_cell_table.csv,\n# the IPFX \"tau\" from the Allen pipeline, in ms, missing for 14 of 96 cells), and runs two-sided\n# Welch t-tests per cell. (3) github.com/AllenNeuralDynamics/LCNE-patchseq-analysis at 1190697,\n# the fuller Patch-seq pipeline; it takes ipfx_tau from an upstream IPFX table and does not\n# recompute it. The other capsules (anatomy, sequencing, in vivo physiology) were not read in\n# full, as the dataset holds none of those data.\n#\n# Data the paper used. The dataset's title (\"Patch-seq profiling of mouse locus coeruleus\n# norepinephrine neurons\") and approach (electrophysiology) say it holds the Patch-seq\n# experiment only. As the paper reports it, whole-cell current-clamp recordings in acute\n# coronal or sagittal slices of LC from Dbh-Cre;Ai65 mice (50 to 74 days old, male and female)\n# whose LC-NE neurons were retrogradely labelled with AAVrg-DIO-FLPo from frontal cortex,\n# cerebellar cortex or spinal cord, about 21 days before recording: 96 cells from 28 mice\n# (frontal cortex 27 cells, 8 mice; cerebellar cortex 15 cells, 7 mice; spinal cord 54 cells,\n# 13 mice). Signals were Bessel filtered at 10 kHz and digitized at 50 kHz, uncorrected for a\n# -14 mV liquid junction potential. Measured variables are membrane voltage and injected\n# current per sweep (long-square steps including rheobase protocols), from which the action\n# potential waveform and the membrane time constant are computed (IPFX). The nucleus was\n# extracted for SMART-Seq v4 RNA sequencing (gene counts as CPM); the paper's code points to\n# the NeMO collection col-p9d5w39 for the Patch-seq transcriptomes.\n#\n# The paper's other experiments are not in this dataset: whole-brain SPIM of Dbh+ nuclei (8\n# mice); dense LC-NE axon labelling; 132 reconstructed LC-NE neurons (4 mice); MAPseq/BARseq (2\n# mice); retrograde tracing (35 mice); snRNA-seq (40 mice, 4,743 LC-NE nuclei); retro-seq\n# (1,076 nuclei); MERFISH data reused from Nardone et al. 2024 (ref. 39); in vivo tetrode and\n# Neuropixels recordings of optotagged LC-NE neurons during a dynamic foraging task (241\n# cells, 19 mice); axonal GCaMP photometry in prelimbic cortex (7 mice); pupil and tongue\n# video. The paper's Data availability names the GitHub index, the NeMO collection\n# col-p9d5w39 and a Code Ocean collection, without saying which data each holds. Claims on\n# sequencing data are marked `elsewhere` with NeMO; the rest are `dataset` and their data are\n# for the author to look for.\n#\n# Paper inconsistency noted. Fig. 3e gives the difference between the projection and gene\n# expression axes as chi-squared(2) = 29.9, bootstrapped P = 10^-4; Extended Data Fig. 15c\n# gives the same chi-squared with p = 3.25 x 10^-7.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001893\"\npaper: doi:10.1038/s41586-026-11026-0\nclaims:\n# Patch-seq: the claims this dataset is meant to test.\n- id: patchseq-sample\n  statement: Whole-cell patch-clamp recordings were made from 96 LC-NE neurons in brain slices\n    from 28 mice, retrogradely labelled from frontal cortex (27 cells, 8 mice), cerebellar cortex\n    (15 cells, 7 mice) or spinal cord (54 cells, 13 mice).\n  source: Results, LC-NE activity during action-outcome learning, paragraph 3\n  quote: we made whole-cell patch clamp recordings from LC-NE neurons in brain slices (96 cells,\n    28 mice). We retrogradely labelled neurons from frontal cortex (27 cells, 8 mice), cerebellar\n    cortex (15 cells, 7 mice) or spinal cord (54 cells, 13 mice)\n  expected:\n  - quantity: Patch-seq cells\n    value: 96\n    tolerance: 0\n  - quantity: mice\n    value: 28\n    tolerance: 0\n  - quantity: cells labelled from frontal cortex\n    value: 27\n    tolerance: 0\n  - quantity: mice, frontal cortex\n    value: 8\n    tolerance: 0\n  - quantity: cells labelled from cerebellar cortex\n    value: 15\n    tolerance: 0\n  - quantity: mice, cerebellar cortex\n    value: 7\n    tolerance: 0\n  - quantity: cells labelled from spinal cord\n    value: 54\n    tolerance: 0\n  - quantity: mice, spinal cord\n    value: 13\n    tolerance: 0\n  criterion: A cell is one recorded neuron (one ephys_roi_id, one NWB file, as the paper's code\n    LCNE-patchseq-figures at 79fa20a reads them), a mouse is one donor, and the group is the\n    injection target. The tolerance is zero because these are counts of the deposited cells\n    themselves, and the paper's code reads exactly 96. Reproduced when every count matches;\n    partially reproduced when the total is within 10% (87 to 106 cells) but a count differs.\n    Recordings deposited twice are counted once (author, step 1.2). Cells that fail the\n    Methods' inclusion rule (seal above 1 GOhm before break-in, initial access resistance below\n    20 MOhm and below 15% of input resistance; Methods, Patch-seq recordings) are reported\n    where the files hold those values.\n- id: patchseq-ne-identity\n  statement: The RNA sequenced from each recorded cell's nucleus confirmed that every recorded\n    cell was a noradrenergic neuron.\n  source: Results, LC-NE activity during action-outcome learning, paragraph 3; Methods, cDNA and\n    sequencing\n  quote: At the end of the recording, we extracted the nucleus for RNA sequencing 41 and\n    confirmed the identity of each cell as a noradrenergic neuron.\n  data: elsewhere\n  where: NeMO collection col-p9d5w39 (https://assets.nemoarchive.org/col-p9d5w39), named in the\n    paper's Data availability; the README of LCNE-patchseq-figures (79fa20a) names it as the\n    Patch-seq transcriptomic data\n  depends_on:\n  - patchseq-sample\n  criterion: The paper does not say how identity was confirmed. Gene counts as CPM of exonic\n    plus intronic reads (Methods, cDNA and sequencing). The markers the paper uses for\n    noradrenergic identity elsewhere are Dbh, Th, Slc6a2 and Slc18a2 (Methods, Identification of\n    noradrenergic cells; Retro-seq). Open, with these readings named before the analysis (a)\n    Dbh detected (CPM above 0) in the cell; (b) all four markers detected; (c) the cell's\n    transcriptomic type mapped to the LC-NE (Dbh) type, as the LCNE-patchseq-analysis diagram\n    shows with MapMyCells. Reproduced when all cells with a transcriptome pass under a reading;\n    partially reproduced when at least 90% pass. The fraction of the 96 cells with a\n    transcriptome is reported.\n- id: patchseq-ap-waveform-spinal-vs-cortex\n  statement: The intracellular action potential waveforms of LC-NE neurons projecting to the\n    spinal cord differ significantly from those of neurons projecting to isocortex (two-sided\n    Welch's t-test, p < 0.01).\n  source: Extended Data Fig. 11k, left; Results, LC-NE activity during action-outcome learning,\n    paragraph 3\n  quote: Neurons projecting to spinal cord had significantly different action potential\n    waveforms than those projecting to isocortex or cerebellum.\n  statistics:\n  - test: two-sided Welch's t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: cells projecting to spinal cord against cells projecting to isocortex (54 and 27 cells)\n  depends_on:\n  - patchseq-sample\n  criterion: Method from the paper's code (LCNE-patchseq-figures at 79fa20a, code/spikes.py and\n    code/generate_S14jk.py), as the legend names no waveform measure. For each cell, take the\n    long-square rheobase sweeps (protocols X3LP_Rheo_DA_0 and X5LP_Rheo_DA_0) whose main pulse\n    lasts at least 0.8 s, and choose the one of lowest absolute amplitude that has at least one\n    spike during the pulse. Detect spike peaks as the voltage maximum between paired upward and\n    downward crossings of -10 mV (after eFEL-style resampling at the sampling step), and average\n    the raw voltage from -5 to 10 ms around every peak of that sweep. Min-max normalize each\n    average over -2 to 4 ms, keep -3 to 6 ms, mean-centre across all cells, and take PC1 by SVD\n    (its sign is arbitrary and does not affect the test). Compare PC1 between spinal cord and\n    cortex cells with a two-sided Welch t-test at the cell level (scipy ttest_ind,\n    equal_var=False). Reproduced when p < 0.01; partially reproduced when 0.01 <= p < 0.05.\n    The group means, t, degrees of freedom and p are reported. Open detail that could change\n    the outcome; the Methods give a sweep inclusion rule (bridge balance below 20 MOhm and 15%\n    of input resistance, bias current within 100 pA, RMS noise below 0.07 mV over 1.5 ms and\n    0.5 mV over 500 ms; Methods, Patch-seq recordings) that the code does not apply. Readings\n    (a) the code's, no further sweep rule; (b) the Methods' sweep rule applied before choosing\n    the rheobase sweep, where the files hold the values it needs. Results under both are shown.\n- id: patchseq-ap-waveform-spinal-vs-cerebellum\n  statement: The intracellular action potential waveforms of LC-NE neurons projecting to the\n    spinal cord differ significantly from those of neurons projecting to cerebellum (two-sided\n    Welch's t-test, p < 0.05).\n  source: Extended Data Fig. 11k, left; Results, LC-NE activity during action-outcome learning,\n    paragraph 3\n  quote: Intracellular action potential waveforms (left; two-sided Welch’s \\(t\\) -tests, spinal\n    cord vs. cortex, \\(p < 0.01\\) , spinal cord vs. cerebellum, \\(p < 0.05\\) )\n  statistics:\n  - test: two-sided Welch's t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: cells projecting to spinal cord against cells projecting to cerebellum (54 and 15 cells)\n  depends_on:\n  - patchseq-sample\n  criterion: The same waveform PC1 as in patchseq-ap-waveform-spinal-vs-cortex, from the paper's\n    code (LCNE-patchseq-figures at 79fa20a), with the same two readings of sweep inclusion.\n    Compare PC1 between spinal cord and cerebellum cells with a two-sided Welch t-test at the\n    cell level. Reproduced when p < 0.05; not reproduced otherwise. Group means, t, degrees of\n    freedom and p are reported.\n- id: patchseq-tau-cortex-vs-spinal\n  statement: LC-NE neurons projecting to isocortex have significantly longer membrane time\n    constants than neurons projecting to the spinal cord (two-sided Welch's t-test, p < 0.001).\n  source: Extended Data Fig. 11k, right; Results, LC-NE activity during action-outcome learning,\n    paragraph 3\n  quote: Neurons projecting to isocortex had significantly longer membrane time constants than\n    those projecting to cerebellum or spinal cord\n  statistics:\n  - test: two-sided Welch's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: cells projecting to spinal cord against cells projecting to isocortex with a time constant\n  depends_on:\n  - patchseq-sample\n  criterion: The Methods say the features were computed with the IPFX package (Methods,\n    Patch-seq recordings). The paper's code (LCNE-patchseq-figures at 79fa20a) does not compute\n    the time constant; it reads IPFX's tau from a frozen table, in ms, missing for 14 of 96\n    cells. Main reading, from the Methods and the dataset - compute tau per cell with IPFX's\n    long-square subthreshold analysis at its default settings (exponential fits to the\n    hyperpolarizing long-square responses, averaged over the qualifying sweeps), using the\n    Methods' sweep inclusion rule where the files hold its values. Variant, from the code - the\n    frozen values in code/data/LCNE_patchseq_S14_cell_table.csv at 79fa20a, keyed by\n    ephys_roi_id (an outside input). Compare cortex and spinal cord cells with a two-sided\n    Welch t-test at the cell level (code/generate_S14jk.py, scipy ttest_ind, equal_var=False).\n    Reproduced when p < 0.001 and the cortex mean exceeds the spinal cord mean; partially\n    reproduced when p < 0.05 with cortex longer. The number of cells with a time constant per\n    group, the group means, t and p are reported for each reading.\n- id: patchseq-tau-cortex-vs-cerebellum\n  statement: LC-NE neurons projecting to isocortex have significantly longer membrane time\n    constants than neurons projecting to cerebellum (two-sided Welch's t-test, p < 0.001).\n  source: Extended Data Fig. 11k, right; Results, LC-NE activity during action-outcome learning,\n    paragraph 3\n  quote: membrane time constants (right; two-sided Welch’s \\(t\\) -tests, spinal cord vs. cortex,\n    \\(p < 0.001\\) , cerebellum vs. cortex, \\(p < 0.001\\) ) showed differences by projection\n    target\n  statistics:\n  - test: two-sided Welch's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: cells projecting to cerebellum against cells projecting to isocortex with a time constant\n  depends_on:\n  - patchseq-sample\n  criterion: The time constant as in patchseq-tau-cortex-vs-spinal (IPFX on the dataset, main;\n    the code's frozen table, variant). Compare cortex and cerebellum cells with a two-sided\n    Welch t-test at the cell level. Reproduced when p < 0.001 and the cortex mean exceeds the\n    cerebellum mean; partially reproduced when p < 0.05 with cortex longer. Cells per group,\n    means, t and p are reported for each reading.\n# Anatomy: not in this dataset.\n- id: lc-definition\n  statement: LC, defined in the CCF as the region at the 67th density percentile of pontine Dbh+\n    nuclei (34,998 cells, 8 mice), is a small dorsal region of 0.13 mm3 holding 1,507 +- 55\n    noradrenergic neurons per mouse, with 367 +- 95 more in sub-coeruleus.\n  source: Results, LC-NE projections are spatially organized, paragraph 1; Fig. 1a,b\n  quote: We defined LC in the CCF as a small dorsal region (0.13 mm 3 in volume) containing\n    approximately two-thirds of all pontine noradrenergic neurons (67th density percentile,\n    1,507 ± 55, mean ± s.d.).\n  expected:\n  - quantity: LC volume\n    value: 0.13\n    tolerance: 0.013\n    unit: mm3\n  - quantity: LC-NE neurons per mouse in LC, mean (s.d. 55)\n    value: 1507\n    tolerance: 55\n  - quantity: noradrenergic neurons in sub-coeruleus per mouse, mean (s.d. 95)\n    value: 367\n    tolerance: 95\n  criterion: Method from Methods, Definition of LC-NE neurons - Dbh-Cre;H2B-GFP nuclei detected\n    in SmartSPIM volumes, registered to CCFv3, restricted to caudal midbrain and dorsal pons,\n    reflected into one hemisphere; local density by nearest neighbours; LC is the mesh at the\n    67th density percentile. Tolerances on counts are the paper's s.d.\n- id: axon-density\n  statement: LC-NE axons from one hemisphere reach a high density in all CNS regions except the\n    striatum, at varying densities; projections to the telencephalon are mainly ipsilateral and\n    those to other regions bilateral.\n  source: Results, LC-NE projections are spatially organized, paragraph 2; Fig. 1c-e\n  quote: We found a high density of LC-NE axons in all CNS regions other than the striatum, with\n    varying densities across regions (Fig. 1c–e and Extended Data Fig. 1 ). Projections to the\n    telencephalon were predominantly ipsilateral\n  criterion: From the unilateral dense labelling imaged by SPIM (Results, paragraph 2; Methods,\n    Single-neuron reconstructions for the imaging). The paper gives no measure of density or a\n    threshold. Reproduced when the striatum has the lowest axon density of the level-2 CCF\n    regions and the telencephalon's ipsilateral density exceeds its contralateral density.\n- id: axon-length-and-branching\n  statement: Reconstructed LC-NE neurons (132 cells, 4 mice) have long axons (34.20 +- 12.83 cm,\n    longest 70.32 cm) that branch little (17.7 branches per cm), significantly less than 1,549\n    other CNS neurons (32.6 branches per cm; ANCOVA).\n  source: Results, LC-NE projections are spatially organized, paragraph 3; Extended Data Fig. 2b\n  quote: Many neurons had long axons (34.20 ± 12.83 cm, mean ± s.d.; Extended Data Fig. 2b ),\n    with the largest neurons reaching 70.32 cm of total length ... LC-NE neurons branched\n    significantly less (ANCOVA (analysis of covariance), P = 3.9 × 10 −160 )\n  statistics:\n  - about: branches against axon length, LC-NE neurons\n    test: linear regression\n    statistic: R2 = 0.72\n    p: 3.6e-38\n    n: 132 neurons\n  - about: branches against axon length, MouseLight neurons\n    test: linear regression\n    statistic: R2 = 0.45\n    p: 3.6e-201\n    n: 1,549 neurons\n  - about: LC-NE against other CNS neurons, branches per length\n    test: ANCOVA\n    p: 3.9e-160\n  expected:\n  - quantity: mean total axon length (s.d. 12.83)\n    value: 34.20\n    tolerance: 12.83\n    unit: cm\n  - quantity: longest total axon length\n    value: 70.32\n    tolerance: 7.03\n    unit: cm\n  - quantity: LC-NE branches per cm (regression slope)\n    value: 17.7\n    tolerance: 1.77\n  - quantity: MouseLight branches per cm (regression slope)\n    value: 32.6\n    tolerance: 3.26\n  criterion: Reconstructions in CCF from ExA-SPIM and HortaCloud (Methods, Single-neuron\n    reconstructions); the comparison set is the MouseLight database. Reproduced when the values\n    are within tolerance and the ANCOVA finds fewer branches per length for LC-NE neurons at p\n    < 0.05.\n- id: single-neuron-primary-targets\n  statement: Individual LC-NE neurons tend to send their axons mainly to one region (cortex,\n    thalamus and midbrain, cerebellum, brainstem or spinal cord); neurons projecting to the\n    forebrain avoid the brainstem and spinal cord, and the reverse.\n  source: Results, LC-NE projections are spatially organized, paragraph 3; Fig. 2b,c\n  quote: Consistent with largely non-overlapping pathways, neurons with forebrain projections\n    tended to project to other regions in the forebrain but not the brainstem or spinal cord\n    (Fig. 2c ).\n  criterion: Fraction of each neuron's axon length in each coarse region and the rank\n    correlation across neurons between region pairs (Fig. 2c legend; Methods, Models of\n    single-neuron axonal distributions, for the regions). Reproduced when the rank correlations\n    are positive among forebrain regions and negative between forebrain regions and medulla or\n    spinal cord.\n- id: markov-renewal-model\n  statement: A model in which axons grow as a Markov random walk between brain regions with a\n    length-dependent Weibull renewal process captures the anterior-posterior block structure of\n    LC-NE projections, unlike random projections.\n  source: Results, LC-NE projections are spatially organized, paragraph 3; Extended Data Fig. 2d;\n    Methods, Models of single-neuron axonal distributions\n  quote: A simple model that assumes axons grow as a random walk with a renewal process that\n    depends on the length of the axons captured fundamental structural features of LC-NE\n    projections (Extended Data Fig. 2d ).\n  criterion: Model as in Methods, Models of single-neuron axonal distributions (10-um steps,\n    transitions counted after 2 mm in the new region, minimum length 10 mm, Weibull renewal fit\n    with incomplete spinal neurons censored). Reproduced when the model's region correlation\n    matrix shows the anterior-posterior block structure of the data and the shuffled model does\n    not.\n- id: mapseq-consistent\n  statement: MAPseq/BARseq barcoding finds LC-NE neurons projecting across the CNS, with soma and\n    axon distributions consistent with the single-neuron reconstructions.\n  source: Results, LC-NE projections are spatially organized, paragraph 4; Extended Data Fig. 3\n  quote: We found LC-NE neurons with projections across the CNS, with distributions of somata\n    and axons consistent with our single-neuron morphologies (Extended Data Fig. 3 ).\n  criterion: Methods, BARseq and MAPseq and the following sections (1-mismatch barcode matching,\n    12 coarse regions, row-normalized fractions). The paper gives no measure of consistency.\n    Reproduced when the share of neurons whose top region is forebrain against hindbrain\n    follows the same dorsal-ventral soma order as in dorsal-ventral-projection-targets.\n- id: dorsal-ventral-projection-targets\n  statement: LC-NE neurons in dorsal LC have primary projections to the forebrain (olfactory\n    bulb, isocortex, hippocampus) and neurons in ventral LC to the hindbrain (pons, medulla,\n    spinal cord).\n  source: Results, LC-NE projections are spatially organized, paragraph 5; Fig. 2d,e\n  quote: Neurons in more dorsal LC had primary projections to the forebrain (olfactory bulb,\n    isocortex and hippocampus), whereas neurons in more ventral LC had primary projections to\n    the hindbrain (pons, medulla and spinal cord).\n  criterion: Soma CCF dorsal-ventral position of each reconstructed neuron against its primary\n    target (region with the largest axon fraction). The paper reports no test. Reproduced when\n    the median soma depth of forebrain-primary neurons is dorsal to that of hindbrain-primary\n    neurons.\n- id: retrograde-dorsal-cortex-ventral-spinal\n  statement: Retrograde tracing confirms that noradrenergic neurons projecting to cortex lie\n    preferentially in dorsal LC and those projecting to the spinal cord in ventral LC.\n  source: Results, LC-NE projections are spatially organized, paragraph 5; Fig. 2f; Extended\n    Data Fig. 5\n  quote: somata of noradrenergic neurons with projections to cortex were preferentially in\n    dorsal LC and noradrenergic neurons with projections to the spinal cord were in ventral LC\n  criterion: AAVrg-DIO-FLPo in Dbh-Cre;Ai65 mice, labelled somata registered to CCF (Methods,\n    Retrograde tracing). The paper reports no test here. Reproduced when the median\n    dorsal-ventral CCF coordinate of cortex-labelled somata is dorsal to that of spinal\n    cord-labelled somata.\n# Gene expression: sequencing data not in this dataset.\n- id: snrnaseq-single-cluster\n  statement: LC-NE gene expression from snRNA-seq (4,743 Dbh+ neurons, 40 mice) is best\n    described by a single cluster with smooth, graded variation (a continuum).\n  source: Results, LC-NE neurons have graded gene expression in space, paragraph 1; Extended Data\n    Fig. 6e\n  quote: A single cluster best explained the data (Extended Data Fig. 6e ), although gene\n    expression varied smoothly across the LC-NE neuron population.\n  data: elsewhere\n  where: NeMO collection col-p9d5w39 (https://assets.nemoarchive.org/col-p9d5w39), the\n    sequencing archive named in the paper's Data availability\n  expected:\n  - quantity: LC-NE nuclei after QC\n    value: 4743\n    tolerance: 474\n  criterion: Methods, Cluster quality analysis - silhouette scores for K = 1 to 15 with Gaussian\n    mixture models in 10-dimensional PCA space (and MMIDAS), five seeds each. Reproduced when\n    the silhouette score is highest at K = 1 with a large drop from 1 to 2.\n- id: pseudospace-graded-genes\n  statement: Many genes vary smoothly along the pseudospace axis of LC-NE gene expression,\n    including axon guidance, adhesion, extracellular matrix, ion channel, receptor and\n    transcription genes, some in opposing gradients (Epha6 against Epha7, Col18a1 against\n    Col6a5).\n  source: Results, LC-NE neurons have graded gene expression in space, paragraph 1; Fig. 3a,b\n  quote: In some cases, two related genes were expressed in opposing gradients - for example,\n    Epha6 versus Epha7 and Col18a1 versus Col6a5 .\n  data: elsewhere\n  where: NeMO collection col-p9d5w39 (https://assets.nemoarchive.org/col-p9d5w39)\n  expected:\n  - quantity: variance explained by the first 10 PCs\n    value: 0.80\n    tolerance: 0.08\n  - quantity: variance explained by the pseudospace curve\n    value: 0.46\n    tolerance: 0.046\n  criterion: Pseudospace as in Methods, Pseudospace analysis (cubic polynomial in the first 10\n    PCs of 1,500 HVGs after scVI, cells projected to the nearest of 10,000 curve points, scaled\n    0 to 1). Reproduced when Epha6 and Epha7, and Col18a1 and Col6a5, have rank correlations\n    with pseudospace of opposite sign.\n- id: merfish-pseudospace-dorsal-ventral\n  statement: Pseudospace imputed onto 2,308 MERFISH LC-NE neurons registered to the CCF aligns\n    with the dorsal-ventral axis of LC.\n  source: Results, LC-NE neurons have graded gene expression in space, paragraph 2; Fig. 3c\n  quote: Gene expression pseudospace aligned with the dorsal–ventral axis of the LC (Fig. 3c and\n    Extended Data Fig. 7 )\n  data: elsewhere\n  where: MERFISH data of Nardone et al. 2024 (Nat. Commun. 15, 1966; ref. 39) and snRNA-seq in\n    NeMO collection col-p9d5w39\n  expected:\n  - quantity: MERFISH LC-NE neurons\n    value: 2308\n    tolerance: 231\n  criterion: Methods, Analysis of MERFISH data and Pseudospace score imputations (k = 50\n    nearest snRNA-seq neighbours on shared genes). Reproduced when imputed pseudospace\n    correlates with the CCF dorsal-ventral coordinate at p < 0.05 and more strongly than with\n    the other two axes.\n- id: retroseq-projection-gene-space\n  statement: Neurons projecting to isocortex, cerebellum or spinal cord occupy different parts\n    of gene expression space; cortex-projecting neurons resemble dorsal LC-NE neurons,\n    spinal cord-projecting neurons ventral ones, and cerebellum-projecting neurons lie between.\n  source: Results, LC-NE neurons have graded gene expression in space, paragraph 3; Fig. 3d\n  quote: Cortex-projecting neurons shared gene expression with dorsal LC-NE neurons, spinal\n    cord-projecting neurons with ventral neurons, and cerebellum-projecting neurons were in\n    between.\n  data: elsewhere\n  where: NeMO collection col-p9d5w39 (https://assets.nemoarchive.org/col-p9d5w39)\n  statistics:\n  - test: Kruskal-Wallis\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Projection targets imputed onto snRNA-seq cells by 10 nearest retro-seq\n    neighbours with at least 8 agreeing (Methods, Projection site imputations for snRNA-seq\n    data). Reproduced when pseudospace differs between imputed targets (Kruskal-Wallis p <\n    0.001) in the order cortex, cerebellum, spinal cord.\n- id: projection-and-expression-axes\n  statement: The primary spatial axes explaining axonal projections (retrograde tracing) and\n    gene expression (MERFISH) both run dorsal-ventral, about 20 degrees apart, and differ\n    significantly.\n  source: Results, LC-NE neurons have graded gene expression in space, paragraph 4; Fig. 3e\n  quote: Primary axes that explain axonal projections (black, from retrograde tracing) and gene\n    expression (grey, from MERFISH) were primarily dorsal–ventral but differed\n  statistics:\n  - test: bootstrapped Mahalanobis test of axis difference\n    statistic: chi-squared(2) = 29.9\n    p: 1.0e-4\n  expected:\n  - quantity: angle between the two axes\n    value: 20\n    tolerance: 2\n    unit: degrees\n  criterion: Methods, Global linear trend test for single features using LDA (retrograde\n    labels), CCA (MERFISH genes), Bootstrap estimation of spatial vector confidence intervals\n    and Comparison of two primary spatial axes. Reproduced when both axes are mainly\n    dorsal-ventral, the angle is within tolerance and the bootstrap p < 0.05. Extended Data\n    Fig. 15c prints p = 3.25 x 10^-7 for the same chi-squared; either p meets the criterion.\n# In vivo physiology and behaviour: not in this dataset.\n- id: behaviour-history-dependence\n  statement: Mice tracked changing reward probabilities, using reward and choice history to\n    guide choices; a logistic regression on outcome history fits choices with R2 = 0.60 and\n    predicts 0.88 of them (259 sessions, 32 mice).\n  source: Fig. 4c; Results, LC-NE activity during action-outcome learning, paragraph 2\n  quote: Mice tracked the changing reward probabilities, using reward and choice history to\n    influence future choices (Fig. 4c ).\n  expected:\n  - quantity: R2 of choice logistic regression\n    value: 0.60\n    tolerance: 0.06\n  - quantity: fraction of choices predicted\n    value: 0.88\n    tolerance: 0.088\n  criterion: Choice model in Methods, Analyses and models of behaviour (10 trials of reward and\n    choice history). Reproduced when both values are within tolerance and the reward history\n    coefficients are positive and decay with lag.\n- id: go-cue-response\n  statement: Nearly all LC-NE neurons (240 of 241, 19 mice) increase their spike rate in the 300\n    ms after the go cue, and the size of this increase relative to baseline is anticorrelated\n    with the correlation between go-cue and baseline rates.\n  source: Results, LC-NE activity during action-outcome learning, paragraph 4; Fig. 4g,h\n  quote: Nearly all LC-NE neurons showed an increase in spike rate in a 300 ms window following\n    the go cue (paired t -tests, 240 out of 241 cells, 19 mice; Fig. 4e–h ).\n  statistics:\n  - about: go-cue response against baseline-response correlation\n    test: correlation\n    statistic: r = -0.38\n    p: 8.3e-11\n    n: 241 cells\n  expected:\n  - quantity: cells with an increase after the go cue\n    value: 240\n    tolerance: 24\n  - quantity: correlation coefficient, Fig. 4h\n    value: -0.38\n    tolerance: 0.038\n  criterion: Per cell, a paired t-test of the spike rate in the 300 ms after go cues against the\n    2 s before (Fig. 4g legend). Open, the paper does not give the threshold for counting a cell;\n    readings (a) p < 0.05 with a higher rate after the cue; (b) a higher mean rate after the cue.\n- id: ventral-respond-ignore\n  statement: Spike rates in the 2 s before the go cue predict whether the mouse responds, higher\n    before ignored trials (46.5% of neurons significant), strongest in ventral LC.\n  source: Results, LC-NE activity during action-outcome learning, paragraph 5; Fig. 5b-d\n  quote: This effect was strongest in neurons in ventral LC (Fig. 5c ; P values from permutation\n    test of linear regression between t -statistics and spatial location - R 2 = 0.152, P = 1.4 × 10\n    −3 ).\n  statistics:\n  - about: t-statistics against CCF location, linear model\n    test: permutation test of linear regression\n    statistic: R2 = 0.152\n    p: 1.4e-3\n    n: 103 cells, 15 mice\n  - about: t-statistics against CCF location, kNN\n    test: kNN cross-validated permutation test\n    statistic: R2 = 5.57e-2\n    p: 8.4e-3\n    n: 103 cells, 15 mice\n  - about: projection onto the retrograde tracing axis\n    test: Pearson correlation\n    statistic: r = 0.36\n    p: 2.0e-4\n  - about: projection onto the MERFISH axis\n    test: Pearson correlation\n    statistic: r = 0.36\n    p: 2.2e-4\n  expected:\n  - quantity: fraction of neurons with p < 0.05\n    value: 0.465\n    tolerance: 0.0465\n  criterion: Per neuron, linear regression of the baseline rate 2 s before each go cue on\n    respond against ignore (Methods, Linear regression models of spike rates); spatial tests as\n    in Methods, Analysing relationships with space (5,000 permutations; kNN with k = 20, 5\n    folds). Reproduced when the fraction is within tolerance and the linear permutation p <\n    0.05 with ventral neurons more positive for ignore.\n- id: dorsal-switch-stay\n  statement: LC-NE neurons with higher activity in the 500 ms after the go cue on switch than on\n    stay choices lie in dorsal LC, and those preferring stay in ventral LC.\n  source: Results, LC-NE activity during action-outcome learning, paragraph 6; Fig. 5f-h\n  quote: Neurons with higher activity during switch choices tended to be in dorsal LC, whereas\n    those with higher activity during stay choices tended to be in ventral LC\n  statistics:\n  - about: t-statistics against CCF location, linear model\n    test: permutation test of linear regression\n    statistic: R2 = 0.168\n    p: 3.0e-4\n    n: 114 cells, 15 mice\n  - about: t-statistics against CCF location, kNN\n    test: kNN cross-validated permutation test\n    statistic: R2 = -4.96e-2\n    p: 0.15\n    n: 114 cells, 15 mice\n  - about: projection onto the retrograde tracing axis\n    test: Pearson correlation\n    statistic: r = 0.37\n    p: 4.4e-5\n  - about: projection onto the MERFISH axis\n    test: Pearson correlation\n    statistic: r = 0.35\n    p: 1.3e-4\n  criterion: Per neuron, linear regression of the go-cue period rate (0.5 s) on switch against\n    stay (Methods, Linear regression models of spike rates); spatial tests as in Methods,\n    Analysing relationships with space. Reproduced when the linear permutation p < 0.05 with\n    dorsal neurons more positive for switch.\n- id: cortex-input-switch\n  statement: LC-NE axonal fluorescence in prelimbic cortex and the spiking of LC-NE neurons\n    identified as projecting to cortex are higher on switch than on stay choices, more so than\n    the population of single neurons.\n  source: Results, LC-NE activity during action-outcome learning, paragraph 7; Fig. 5j,k\n  quote: LC-NE axonal fluorescence changes in PL and single-neuron spiking projecting to frontal\n    cortex were significantly higher during switch versus stay choices (Fig. 5j,k , Fisher’s\n    exact test, P = 7.8 × 10 −5 ).\n  statistics:\n  - test: Fisher's exact test\n    p: 7.8e-5\n  criterion: Sign-based comparison of switch-versus-stay t-statistics (proportion positive)\n    between groups, Fisher's exact test (Methods, Comparison between single-neuron activity and\n    axonal GCaMP); axonal regression in 0.75 s after the go cue (Methods, Linear regression\n    models of axonal GCaMP). Reproduced when p < 0.05 with a larger positive share for the\n    cortex-projecting signals.\n- id: outcome-responses-spatial\n  statement: LC-NE neurons respond variously to reward or its absence (76.8% with significant\n    regressions); reward-excited neurons lie more dorsal and anterior than no-reward-excited\n    neurons, a nonuniform distribution in space.\n  source: Results, Frontal cortex LC-NE activity correlates with RPE, paragraphs 1 and 3; Fig. 6a\n  quote: Neurons with increased activity in response to reward tended to lie more dorsal and\n    anterior in LC than neurons with increased activity in response to no reward\n  statistics:\n  - about: spatial distribution of reward- and no-reward-excited neurons\n    p: 3.0e-4\n  expected:\n  - quantity: fraction of cells with significant outcome regressions\n    value: 0.768\n    tolerance: 0.0768\n  criterion: Outcome regressions as in Methods, Linear regression models of spike rates (reward\n    and no-reward windows, the larger absolute t kept). The test behind P = 3.0 x 10^-4 is not\n    named; the LDA trend test (Methods, Global linear trend test for single features using LDA)\n    is the one the Methods give for categorical labels. Reproduced when the fraction is within\n    tolerance and the spatial test gives p < 0.05 with reward-excited neurons dorsal.\n- id: rpe-predicts-choice-change\n  statement: The change in choice between consecutive trials correlates with model-estimated\n    RPE (rank correlation 0.84).\n  source: Fig. 6c; Results, Frontal cortex LC-NE activity correlates with RPE, paragraph 1\n  quote: Relationship between how choices changed on consecutive trials and RPE (rank\n    correlation, ρ = 0.84, P = 0.0).\n  statistics:\n  - test: rank correlation\n    statistic: rho = 0.84\n    p: 0\n  expected:\n  - quantity: rank correlation\n    value: 0.84\n    tolerance: 0.084\n  criterion: RPE from the hierarchical Q-learning model fit in Stan, change of choice likelihood\n    as defined in Methods, Analyses and models of behaviour.\n- id: outcome-coefficients-cluster\n  statement: Regression coefficients of outcome-period spiking on reward and chosen value are\n    nonuniformly distributed in angle, and neurons projecting to isocortex are biased towards\n    RPE (excited by reward, inhibited by predicted reward).\n  source: Fig. 6e,f; Results, Frontal cortex LC-NE activity correlates with RPE, paragraph 3\n  quote: Polar histogram of coefficients from regressions in e shows a nonuniform distribution\n    of activity (Rayleigh test, z = 19.53, P = 2.3 × 10 −9 ).\n  statistics:\n  - about: angles of reward and chosen value coefficients\n    test: Rayleigh test\n    statistic: z = 19.53\n    p: 2.3e-9\n  - about: cortex-projecting neurons against the population\n    test: Watson-Wheeler test, permutation\n    statistic: W = 0.04\n    p: 0.01\n  criterion: Angle of the (R, Qc) coefficients per neuron (Methods, Linear regression models of\n    spike rates); Mardia-Watson-Wheeler permutation test with 5,000 permutations (Methods,\n    Circular distribution comparison). Reproduced when both p < 0.05.\n- id: frontal-axons-rpe\n  statement: LC-NE axonal activity in prelimbic cortex 1.5 s after outcome correlates with RPE,\n    and the regressions of axonal activity and of cortex-projecting neurons are more positive\n    than those of the population of single neurons.\n  source: Results, Frontal cortex LC-NE activity correlates with RPE, paragraph 4; Fig. 6i-l\n  quote: Regression t -statistics (Fig. 6j ) and coefficients (Fig. 6k ) were more positive than\n    the population of single neurons (Fisher’s exact test, P = 5.7 × 10 −3 ) and consistent with\n    modulation by RPE.\n  statistics:\n  - about: sign of t-statistics, axons and cortex-projecting neurons against the population\n    test: Fisher's exact test\n    p: 5.7e-3\n  - about: angles of axonal coefficients against single neurons\n    test: Watson-Wheeler test, permutation\n    statistic: W = 0.1\n    p: 2.0e-4\n    n: 67 sessions, 7 mice\n  criterion: Axonal regressions in a 2 s window after outcome (Methods, Linear regression models\n    of axonal GCaMP); comparisons as in Methods, Comparison between single-neuron activity and\n    axonal GCaMP and Circular distribution comparison. Reproduced when both p < 0.05 with axonal\n    coefficients towards positive reward and negative chosen value.\n- id: extracellular-waveform-spatial\n  statement: Extracellular spike waveforms of LC-NE neurons vary in space; dorsal neurons have\n    more symmetric waveforms and longer peak-to-trough times than ventral neurons.\n  source: Results, LC-NE activity during action-outcome learning, paragraph 3; Extended Data Fig.\n    11b-d\n  quote: dorsal LC-NE neurons tended to have more symmetric spike waveforms and longer\n    peak-to-trough times than ventral LC-NE neurons\n  statistics:\n  - about: slope symmetry, kNN\n    test: kNN cross-validated permutation test\n    p: 5.0e-4\n  - about: slope symmetry, linear model\n    test: permutation test of linear regression\n    p: 5.0e-4\n  - about: waveform PC1, kNN\n    test: kNN cross-validated permutation test\n    p: 0.014\n  - about: waveform PC1, linear model\n    test: permutation test of linear regression\n    p: 2.0e-4\n  criterion: Waveform features of optotagged units (Methods, Spike waveform extraction) and the\n    spatial tests of Methods, Analysing relationships with space (kNN with k = 30 for waveforms).\n    Reproduced when slope symmetry and PC1 both show a linear trend at p < 0.05 with dorsal\n    neurons more symmetric.\n"
}
```

```
File created successfully at: claims/001893/10.1038-s41586-026-11026-0.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  f=claims/001893/10.1038-s41586-026-11026-0.yaml; python3 - <<'EOF'
p='claims/001893/10.1038-s41586-026-11026-0.yaml'
s=open(p).read()
s=s.replace("""  quote: In some cases, two related genes were expressed in opposing gradients - for example,
    Epha6 versus Epha7 and Col18a1 versus Col6a5 .""","""  quote: In some cases, two related genes were expressed in opposing gradients ... Epha6 versus
    Epha7 and Col18a1 versus Col6a5""")
s=s.replace("""  quote: This effect was strongest in neurons in ventral LC (Fig. 5c ; P values from permutation
    test of linear regression between t -statistics and spatial location - R 2 = 0.152, P = 1.4 × 10
    −3 ).""","""  quote: "This effect was strongest in neurons in ventral LC (Fig. 5c ; P values from permutation
    test of linear regression between t -statistics and spatial location: R 2 = 0.152, P = 1.4 ×
    10 −3 )." """.rstrip())
open(p,'w').write(s)
import yaml
d=yaml.safe_load(open(p))
print(len(d['claims']))
EOF
grep -n ": .*: " $f | grep -v '^[0-9]*:#' | head; python tools/claims_check.py $f paper/10.1038-s41586-026-11026-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -c "—" claims/001893/*.yaml; grep -n -i "rather" claims/001893/*.yaml; python3 -c "
import yaml;d=yaml.safe_load(open('claims/001893/10.1038-s41586-026-11026-0.yaml'))
c=d['claims'];print(sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c))"; git status --short
```

```
0
16 29 12
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
?? claims/001893/
?? scripts
```

**Agent**

I wrote `claims/001893/10.1038-s41586-026-11026-0.yaml`. The quote checker passes: 29 claims, 29 quotes, 29 statistical values, 0 problems.

**Text read.** The version of record, from Crossref and the publisher's HTML (stored 2026-10-21): main text, Methods, figure legends and the Extended Data Fig. 1–15 legends. Supplementary Tables 1–3 are a PDF and are not in the text. The paper cites them only for injection coordinates, volumes and model priors, and no result rests on them. I also read the bioRxiv preprint v1, only to compare. The paper is titled "Topographic structure and function of locus coeruleus noradrenaline neurons"; "Patch-seq profiling of mouse locus coeruleus norepinephrine neurons" is the dataset's title on DANDI.

**Code read.**
- The linked index repository at commit 43f7083.
- `LCNE-patchseq-figures` at 79fa20a. It builds Extended Data Fig. 11j,k from dandiset 001893 version 0.260817.1647: 96 NWB files, with projection target and donor from `participants.tsv`.
- `LCNE-patchseq-analysis` at 1190697.

**Claims.** 29 in total, all with quotes; 16 have statistics, 29 have criteria and 12 have expected values.
- **Testable here (6 Patch-seq claims):**
  - Cell and mouse counts per projection target (96 cells, 28 mice).
  - Identity of each cell as noradrenergic. The transcriptomes are marked as held elsewhere, in NeMO collection col-p9d5w39.
  - Action-potential waveform, spinal cord against cortex (p < 0.01) and spinal cord against cerebellum (p < 0.05).
  - Membrane time constant, cortex longer than spinal cord and than cerebellum (both p < 0.001).
- **Not in this dataset (23 claims):** whole-brain anatomy, single-neuron reconstructions, MAPseq, retrograde tracing, snRNA-seq, MERFISH, retro-seq, in vivo recordings during behaviour, axonal photometry, and extracellular waveforms. The paper names where its data are only as a GitHub index, NeMO and a Code Ocean collection, without saying which data each holds.

**Details the paper leaves open, and the readings named:**
- **Which action-potential measure:** the legend names none. The code settles it, so the criterion follows the code: PC1 of the averaged rheobase spike waveform, with its windows, normalisation and spike detection, tested with a two-sided Welch t-test per cell.
- **Sweep inclusion for the waveform:** the Methods give a sweep quality rule that the code does not apply. Readings: (a) the code's, with no further rule; (b) the Methods' rule, applied where the files hold the values it needs.
- **Membrane time constant:** the code does not compute it; it reads a frozen IPFX value, missing for 14 of the 96 cells. Main reading: compute it with IPFX at default settings from the dataset, as the Methods say. Variant: the code's frozen table, which is an outside input.
- **How cell identity was confirmed:** not stated. Readings: (a) Dbh detected; (b) all four markers (Dbh, Th, Slc6a2, Slc18a2) detected; (c) the cell maps to the LC-NE type.
- **Go-cue responses:** the paper gives no threshold for counting a cell as responding. Readings: (a) paired t-test p < 0.05 with a higher rate after the cue; (b) a higher mean rate after the cue.
- **Outcome responses in space:** the test behind P = 3.0 × 10⁻⁴ is not named. The criterion uses the LDA trend test, which the Methods give for categorical labels.

**Inconsistencies in the paper, recorded in the file:**
- Fig. 3e gives χ²₂ = 29.9 with bootstrapped P = 10⁻⁴; Extended Data Fig. 15c gives the same statistic with p = 3.25 × 10⁻⁷.
- The preprint says "paired t-tests" for the Patch-seq comparisons; the version of record says two-sided Welch's t-tests. I followed the version of record.

**Missing from the paper.** Nothing the Patch-seq claims need. The only gaps are the details above that the code did not settle: how the time constant was computed, sweep inclusion, and how identity was confirmed.

## End of run

31 turns, 66 minutes, $2.65 at API prices, result: success.
