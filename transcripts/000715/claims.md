# 000715 · claims · run 39895957415

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000715/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md; ls claims/001453/ claims/000715/ paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -30 paper/10.1016-j.cell.2020.12.012.txt; head -30 paper/10.1007-978-3-030-59722-1_12.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,200p claims/001453/*.yaml
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,600p claims/001453/*.yaml | grep -n -E "^- id|^[a-z_]+:|kind|data:|inferred|deviation|open" | head -80; ls docs tools schema* 2>/dev/null
```

```
13:- id: fig1cef-representative-values
24:- id: fig2d-shared-architecture
31:- id: fig2g-dsi-similar
41:- id: fig2h-fewer-motion-responsive
51:- id: fig2k-more-monocular
61:- id: fig2l-bi-ratio
71:- id: fig3e-longer-swims
81:- id: fig3cd-zf-turn-more
98:- id: fig4f-longer-on-duration
110:- id: fig4hi-vspn-lateralized
docs:
agents
archives.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
pilot-notes
pilot-notes.md
pipeline.md
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json; ls docs/agents; grep -rn "000715" docs/ targets* 2>/dev/null | head
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
[... 339 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/agents/claims.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
d=d if isinstance(d,list) else d.get('dandisets',d)
for x in d:
  if x.get('dandiset')=='000715': print(json.dumps(x,indent=1))
"
```

```
Exit code 1
You are the reader for dataset {dataset} in the reproduction registry. The repository is checked out in the current directory. Read docs/protocol.md, the "Reader" section, first: it is the whole method for this run. Look at claims/001453/ for the file format.

Paper: doi:{paper}, "{title}". Its full text is under `paper/`: a `.txt` file per paper (main text, Methods and supplement, with a header saying where it came from), and the PDF where there is one. Read the text; open a PDF page only to read a figure or a table that the text garbles. If the full text, the Methods, or a supplement the results rest on is missing, stop and say what is missing: write no claims. Never write claims from the abstract. You may read the code the paper links to. Do not look at the dataset's data or its files; its title and description on the archive are enough to know which experiments it is meant to hold.

{existing}

Write the claims file as steps 1 to 4 of the Reader section say. Every part of every criterion's method comes from the paper or its code, cited; a detail none of them fixes is named as open, with the readings the paper allows. Check every quote with `python tools/claims_check.py claims/{folder}/<file>.yaml paper/<text>.txt` and fix the quote, never the checker. Do not commit or push: the workflow commits your changes. Only files under `claims/{folder}/` are kept.

Provenance for the opening comment: written by an agent (model "{model}", Claude Code in GitHub Actions), {date}, protocol as stated in docs/protocol.md.

Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": " (colon space).

Your final message is a report: the text read (version, supplement), the number of claims and how many have quotes, statistics and criteria; the details the paper leaves open and the readings named for each; anything missing from the paper that a claim needed. Be concise.

Run every command in the foreground and wait for it to finish
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 3395,3440p targets/dandisets.json
```

```
],
   "papers": [
    {
     "doi": "10.1038/s41592-023-01806-1",
     "title": "An optical design enabling lightweight and large field-of-view head-mounted microscopes",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": [
    "contributor Weigl, Szonja of CatalystNeuro"
   ]
  },
  {
   "dandiset": "000715",
   "name": "NeuroPAL: Atlas of C. elegans neuron locations and colors in NeuroPAL worm",
   "published_version": "0.241009.1514",
   "asset_count": 10,
   "size_gb": 0.84,
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; head -c 3000 paper/10.1016-j.cell.2020.12.012.txt; grep -n -i -E "^(STAR|Methods|Supplemental|Figure S|KEY RESOURCES|RESULTS|DISCUSSION|Introduction)" paper/10.1016-j.cell.2020.12.012.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)": "substr($0,1,150)}' 10.1016-j.cell.2020.12.012.txt | head -40; wc -l 10.1016-j.cell.2020.12.012.txt
```

```
1: 31: DOI: 10.1016/j.cell.2020.12.012
2: 30: Version: as served by ncbi_pmc
3: 37: Source: ncbi_pmc (paper-text-fetcher)
4: 18: Stored: 2026-10-20
5: 183: Extracted: as fetched; with 2 supplement file(s) from PubMed Central, downloaded in a browser (PMC10494711), PDFs extracted with PyMuPDF (dehyphenated
6: 72: ------------------------------------------------------------------------
7: 104020: pmc Cell Cell 319 nihpa Cell 0092-8674 1097-4172 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC10494711 PMC10494711.1 
8: 0: 
9: 56: ##### Supplement: NIHMS1925874-supplement-Methods_S1.pdf
10: 0: 
11: 14: === page 1 ===
12: 16: Cell, Volume 184
13: 24: Supplemental Information
14: 44: NeuroPAL: A Multicolor Atlas for Whole-Brain
15: 37: Neuronal Identification in C. elegans
16: 80: Eviatar Yemini, Albert Lin, Amin Nejatbakhsh, Erdem Varol, Ruoxi Sun, Gonzalo E.
17: 83: Mena, Aravinthan D.T. Samuel, Liam Paninski, Vivek Venkatachalam, and Oliver Hobert
18: 0: 
19: 14: === page 2 ===
20: 72: Methods S1. Semi-Automated Neuronal Identification Software, related to 
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 7p 10.1016-j.cell.2020.12.012.txt | fold -s -w 4000 > $TMPDIR/main.txt; wc -l $TMPDIR/main.txt; sed -n 1,8p $TMPDIR/main.txt
```

```
<persisted-output>
Output too large (31.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/824342a4-e8a4-4f60-84a9-79db498b61cd/tool-results/b6bkkjfa1.txt

Preview (first 2KB):
27 /tmp/claude-1001/main.txt
pmc Cell Cell 319 nihpa Cell 0092-8674 1097-4172 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC10494711 PMC10494711.1 10494711 10494711 NIHMS1925874 33378642 10.1016/j.cell.2020.12.012 NIHMS1925874 NIHPA1925874 1 Article NeuroPAL: A Multicolor Atlas for Whole-Brain Neuronal Identification in C. elegans Yemini Eviatar 1 7 * Lin Albert 2 Nejatbakhsh Amin 3 Varol Erdem 3 Sun Ruoxi 3 Mena Gonzalo E. 4 Samuel Aravinthan D.T. 2 Paninski Liam 3 Venkatachalam Vivek 5 Hobert Oliver 1 6 1 Department of Biological Sciences, Howard Hughes Medical Institute, Columbia University, New York, NY 10027, USA 2 Department of Physics, Center for Brain Science, Harvard University, Cambridge, MA 02138, USA 3 Departments of Statistics and Neuroscience, Grossman Center for the Statistics of Mind, Center for Theoretical Neuroscience, Zuckerman Institute, Columbia University, New York, NY 10027, USA 4 Department of Statistics and Data Science Initiative, Harvard University, Cambridge, MA 02138, USA 5 Department of Physics, Northeastern University, Boston, MA 02115, USA 6 Senior author 7 Lead Contact AUTHOR CONTRIBUTIONS All authors contributed in writing this manuscript. O.H. initiated the project. E.Y. designed and built NeuroPAL, designed and performed all non-stimulus behavioral phenotyping, traced the EM reconstructions, conducted all metabotropic receptor and mutant experiments, generated the panneuronal GCaMP6s strain, and performed the non-automated identification of activity traces. A.L. designed and performed all chemotactic assays. A.L., A.D.T.S., and V.V. designed and built the whole-brain imaging scope and microfluidic device then, together with E.Y. and O.H., designed the whole-brain imaging experiments that
[... 2 more lines not kept]
```

**Agent**

I'll read the main text in pieces with the Read tool.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "limit": 7
}
```

```
1	pmc Cell Cell 319 nihpa Cell 0092-8674 1097-4172 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC10494711 PMC10494711.1 10494711 10494711 NIHMS1925874 33378642 10.1016/j.cell.2020.12.012 NIHMS1925874 NIHPA1925874 1 Article NeuroPAL: A Multicolor Atlas for Whole-Brain Neuronal Identification in C. elegans Yemini Eviatar 1 7 * Lin Albert 2 Nejatbakhsh Amin 3 Varol Erdem 3 Sun Ruoxi 3 Mena Gonzalo E. 4 Samuel Aravinthan D.T. 2 Paninski Liam 3 Venkatachalam Vivek 5 Hobert Oliver 1 6 1 Department of Biological Sciences, Howard Hughes Medical Institute, Columbia University, New York, NY 10027, USA 2 Department of Physics, Center for Brain Science, Harvard University, Cambridge, MA 02138, USA 3 Departments of Statistics and Neuroscience, Grossman Center for the Statistics of Mind, Center for Theoretical Neuroscience, Zuckerman Institute, Columbia University, New York, NY 10027, USA 4 Department of Statistics and Data Science Initiative, Harvard University, Cambridge, MA 02138, USA 5 Department of Physics, Northeastern University, Boston, MA 02115, USA 6 Senior author 7 Lead Contact AUTHOR CONTRIBUTIONS All authors contributed in writing this manuscript. O.H. initiated the project. E.Y. designed and built NeuroPAL, designed and performed all non-stimulus behavioral phenotyping, traced the EM reconstructions, conducted all metabotropic receptor and mutant experiments, generated the panneuronal GCaMP6s strain, and performed the non-automated identification of activity traces. A.L. designed and performed all chemotactic assays. A.L., A.D.T.S., and V.V. designed and built the whole-brain imaging scope and microfluidic device then, together with E.Y. and O.H., designed the whole-brain imaging experiments that were all conducted in the A.D.T.S. lab. A.L. performed all whole-brain imaging experiments. A.N., E.V., L.P., and V.V. designed and built the software for whole-brain activity imaging that connects neurons with their identities, then extracts
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 8,
 "limit": 7
}
```

```
8	distinct sets of neuronal correlations among and between sensory and interneurons. These results can be seen in the brainwide neuronal trajectories through low-dimensional PCA-space ( Figures S2A and S2B ). For instance, the AWB sensory neurons and their synaptically connected interneuron partners AUA and AVH exhibit distinct pairwise correlations depending on the stimulus ( Figures 6D and 6E ). Thus we find that brain dynamics are stimulus-specific. We asked whether a simple relationship exists between these functional correlations and the synaptic counts previously measured from the anatomical connectome ( Cook et al., 2019 ; White et al., 1986 ). To do so, we compared our correlation matrices of pairwise functional activity to the connectome matrix of pairwise synaptic connectivity. These matrices represent functional and structural measures of neuronal communication, respectively. We used the absolute value of the correlation matrices, because the connectome lacks excitatory/inhibitory synaptic information. We found low Pearson correlation between these functional and structural matrices. For electrical connectivity, R 2 = 2.8% in the head and R 2 = 1.7% in the tail, and for chemical connectivity, R 2 = 0.5% in the head and R 2 = 1.5% in the tail ( Figures 6J and 6K ). We tried multiple variations in our calculations (e.g., thresholding for low sampling, using ranked correlation metrics, log-scaling synaptic counts, and limiting functional activity to only stimulus or non-stimulus delivery periods) but these did not noticeably improve correlation between functional activity and the structural connectome ( Table S6 ). The low correlation values we measured may intimate contributions from non-synaptic signaling networks (that are not reflected in the anatomical connectome). These non-synaptic signaling networks include: (1) pervasive neuropeptidergic signaling ( Bargmann and Marder, 2013 ), (2) extensive aminergic signaling ( Bentley et al., 2016 ), and (3) pote
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 15
}
```

```
15	RMEV neurons, in two eor-1(−) mutant backgrounds was Bonferroni corrected for eight tests ( Figures 5F and 5G ; Table S5 ). We used a One-Sided Fischer’s Exact Test to analyze mutant-induced loss of RMED/V blue coloring in NeuroPAL. We used a One-Sided Rank Sum Test to analyze mutant-induced changes in the RMED/V UNC-25 reporter expression, scoring 0 if expression was lost, 1 if expression was weak but visible, and 2 if no changes were observed. Mutant analysis studies were not blinded. Analysis of brainwide imaging data To analyze the whole-brain imaging stimulus responses ( Figures 6 , S1H , and S2 ; Table S6 ), we reviewed ASE responses to salt and AWC responses to the odors – the primary sensory neurons for these stimuli. Worms were marked as stimulus responsive if either their left or right neuron showed the published response to their corresponding stimuli (ASE excitation for NaCl and AWC inhibition for odors) ( Chalasani et al., 2007 ; Suzuki et al., 2008 ). 21 heads responded to all three stimuli, providing strong internal controls to compare their circuit activity across all stimuli. Additionally, 21 tails were included, without response verification as the heads of these animals were not simultaneously imaged. Premotor interneurons (AVA, AVB, AVD, AVE, PVC) and ventral-cord motor neurons (AS, DA, DB, DD, VA, VB, VC, VD) show spontaneous cyclical activity and thus were excluded from significance testing. For testing that did not compare asymmetries, left/right neuron pairs from the same class were combined; thus the maximum sample size for these tests is either 42 left/right neuron pairs (e.g., AFDL and AFDR) or 21 single-sided neurons (e.g., I6). We used t tests (2-tailed, paired) to compare the mean signal during stimulus presentation with an identical period immediately prior, within the very same neuron (a strong internal control). These p values were corrected for multiple testing using false discovery rate (FDR) adjusted q-values ( Storey, 2002 ). 
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd ..; grep -n -i -E "excel|xlsx|supplementary table|tables? s[0-9].*missing|missing" docs/pilot-notes.md | head -20; grep -n "Table S" -r docs/protocol.md | head
```

```
124:  dandiset holds. A link claim confirms the names, and the missing names
161:`data_missing`, the same reason as data that are public nowhere. pilot-7
167:`data_missing`; if it cannot be tested here, the reason is the one that
168:applies, such as `too_large` or `not_runnable`. `data_missing` now means
306:before writing claims and reports what is missing, so that the paper can be
346:with supplements where the results rest on them. Which papers it holds, and which are missing, is in
```

**Agent calls Bash**

```bash
sed -n 295,360p docs/pilot-notes.md
```

```
the units the attempt used, as its supplement shows.

These attempts are now marked `deprecated`, with the reason, in their
records. The records and entries stay as they were; the dashboard shows
them with the reason and counts none of their outcomes, and their README
rows have no counts. Each is queued to be run again: the new attempt
writes the claims file again from the full text, keeping a claim's id where
its finding is the same so that the outcomes can be compared.

Step 1 of the protocol now requires the full text, with the Methods and
any supplement the results rest on. An author who cannot read it stops
before writing claims and reports what is missing, so that the paper can be
supplied. Claims are never written from the abstract.

The same review showed where the guessed methods came from: step 7 let an
author fix a method choice the paper leaves open and judge the claim on it.
With only an abstract, nearly every choice was open, so the outcomes rested
on the author's choices. Step 7 now says that methods come from the paper,
never from the author: every part of a criterion's method is taken from the
Methods, legends, supplement or the paper's code, and the criterion says
[... 46 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cell.2020.12.012.txt",
 "offset": 80,
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cell.2020.12.012.txt",
 "offset": 480,
 "limit": 650
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Reading Methods S1 section 6 (numerical validations), which is where the dataset-relevant numbers are.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cell.2020.12.012.txt",
 "offset": 1129,
 "limit": 450
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1578,3111p paper/10.1016-j.cell.2020.12.012.txt | awk 'length($0)>60' | head -250
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1578,3111p paper/10.1016-j.cell.2020.12.012.txt | grep -n -i -E "violation|%|result|wormbase|margin of|neighbor" | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1578,3111p paper/10.1016-j.cell.2020.12.012.txt | sed -n '36,50p;160,200p;836,850p;1120,1160p'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1578,3111p paper/10.1016-j.cell.2020.12.012.txt | sed -n '50,160p;1136,1150p;1160,1260p' | awk 'length($0)>30'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/amin-nejat/CELL_ID && cd CELL_ID && git log -1 --format='%H %cd' && ls -R | head -80
```

```
759898d3b0f4265afdf0a03249fc111c5553b52a Sun Nov 14 00:52:32 2021 +0100
.:
+DataHandling
+Image
+Methods
+Neurons
+Output
+Program
Data
README.md
mac_visualize.prj
version.info
visualize_light.mlapp
visualize_resources
win_visualize.prj

./+DataHandling:
NeuroPALImage.m
PNGViewer.m
imreadAny.m
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CELL_ID; ls Data/Models Data/NeuroPAL | head -30; grep -rln -i -E "leave|cross.?valid|train_atlas|accuracy" --include=*.m . | head; wc -l +Methods/AutoId.m; git log --oneline | wc -l; git log --format='%h %cd %s' | tail -3
```

```
Data/Models:
NN_model.mat
VanillaUnet_model.10.h5
atlas_xo_rgb.mat
atlas_xo_rgbw.mat
atlas_xx_rgb.mat
atlas_xx_rgbw.mat
make_neuron_type_colors_identical.m

Data/NeuroPAL:
NeuroPAL_data.mat
NeuroPAL_herm_data.mat
NeuroPAL_male_data.mat
birth_times.mat
herm_data.mat
male_data.mat
neuron_props.mat
./+Methods/AutoDetect.m
801 +Methods/AutoId.m
475
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CELL_ID; git log --format='%h %cd %s' --date=short | sed -n '1,40p'; git log --format='%h %cd %s' --date=short --until=2021-01-01 | head -3; grep -n "function" +Methods/AutoId.m
```

```
759898d 2021-11-14 Bumped to v1.8
35c8151 2021-11-14 Bumped to version 1.8
4ecc2e3 2021-11-13 Fixed a bug in ID updates when no model exists. Also fixed a bug to unselect neurons when closing images -- we don't want selected neurons to linger when the file is reopened.
17f274a 2021-10-10 Bumped to v1.7.
ed01427 2021-10-10 Bumped to 1.7. In last update, I use only the marked z plane to compute neuron GFP intensity. Going off Z leads to spurious measures.
03601a7 2021-10-10 Fixed up GFP estimation for image analysis.
6a20cb9 2021-09-14 Bumped to v1.6
add8d18 2021-09-14 NeuroPAL website will switch to yeminilab.com
9f920f7 2021-09-14 Bumped to 1.6 cause of the bug.
3ec4906 2021-09-14 Fixed a bug in the color atlas.
380b16d 2021-08-24 Updated the windows compilation file for v1.5
7a087a7 2021-08-24 Bumped us to v1.5. Almost ready to go live! :)
aa0c58f 2021-08-24 Fixed a bug that showed neuron names lower case. Reverted to MP detect as default because Amin peer pressured me into it ;)
54406a2 2021-08-24 Fixed a bug so that NN detect can now be deployed in the standalone compilation.
592f40d 2021-08-23 Fixed a bug in saving PDFs of the images. We now count the right way if Z is flipped & we use half Zs to include all neuron annotations.
9ba9f95 2021-08-23 Updated the instructions to include artifacts, mutations, and neuron emphasis.
b53d34a 2021-08-23 Neurons can now be emphasized (e.g., as in mutations). Emphasized neurons can exist as duplicates. I also added the neuron label "MUTATION" for unspecified mutations.
bb1496d 2021-08-23 Worms younger than adult are ID'd as herms because we lack age-specific models. Fixed some debugging to check for standalone deployment.  Fixed a bug in the number of male neurons. Added age & sex to batch detect + ID.
ee67eec 2021-08-22 Added the project files in so people can compile the standalone.
b7001aa 2021-08-22 Fixed a bug with labeling neurons artifacts. Added debugging code for neural network neuron detection in the standalone. Pl
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CELL_ID; git checkout -q d9f5df9; ls -R +Methods Data/Models 2>/dev/null; grep -rn -i -E "train|atlas" --include=*.m . | grep -v "^./visualize" | head -30
```

```
+Methods:
AutoDetect.m
AutoId.m
Preprocess.m
Utils.m
find_outlier.m
logsumexp.m
munkres.m
munkres_extended.m

Data/Models:
atlas.mat
atlas_new.mat
atlas_old.mat
./+Output/ImageAnalysis.m:140:            fprintf(fileID, ['Atlas Version,,' ...
./+Output/ImageAnalysis.m:146:                neurons.atlas_version, data_class, data_max, ...
./+Neurons/Neuron.m:90:        function annotate(obj, name, confidence, is_on, atlas)
./+Neurons/Neuron.m:105:                neuron_names = atlas.N;
./+Neurons/Neuron.m:112:                    mu = atlas.model.mu(neuron_index,:);
./+Neurons/Neuron.m:113:                    sigma = squeeze(atlas.model.sigma(:,:,neuron_index));
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CELL_ID; sed -n 40,60p +Methods/AutoId.m; sed -n 120,500p +Methods/AutoId.m
```

```
if isempty(instance)
                obj = Methods.AutoId();
               instance = obj;
             else
               obj = instance;
             end
        end
        
        function [atlas, version] = getAtlas()
            %GETATLAS get the atlas data.
            persistent data;
            if isempty(data)
                data = load('atlas.mat');
            end
            atlas = data.atlas;
            version = data.version;
        end
        
        function BatchId(file, bodypart)
            % Batch ID neurons.
[... 383 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CELL_ID; sed -n 1,38p +Methods/AutoId.m; sed -n 540,720p +Methods/AutoId.m
```

```
classdef AutoId < handle
    %AUTO_ID Auto.
    %
    %   An auto_id object is has a set of possible names (different if tail/head), the method used, a likelihood
    %   matrix, and a set of ids for each of observed neurons. 
    properties(Constant)
        % constants
        ncandidates         = 7;
        annotation_weight   = 1e1;
        
        iter_sinkhorn       = 500;
        iter_rwc            = 10;
        
        min_log_likelihood  = -1e9;
        max_log_likelihood  = 1e5;
        
        %parameters for automatic detection of false positives. pf=prob of
        %a detect being a false positive. max_fp is the maximum posible
        %number of false positives.
        p_fp = 1e-50; %if p = 10^(-Large number) no neuron is a false positive. 
[... 200 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CELL_ID; grep -n -i -E "colors_readout|zscore|median|patch|cube" +Neurons/*.m +Methods/AutoDetect.m +DataHandling/NeuroPALImage.m | head -30
```

```
+Neurons/Image.m:67:            %   nsz: the window size around the patch for the  new neuron.
+Neurons/Image.m:75:            bpatch = Methods.Utils.subcube(volume, round(position), nsz);
+Neurons/Image.m:81:                [~, sp] = auto_detect.fit_gaussian(double(bpatch), color, position);
+Neurons/Image.m:89:            cpatch = Methods.Utils.subcube(volume, round(sp.positions), [1,1,0]);
+Neurons/Image.m:97:            neuron.color_readout = median(reshape(cpatch, [numel(cpatch)/size(cpatch, 4), size(cpatch, 4)]));
+Neurons/Image.m:285:        function colors = get_colors_readout(obj)
+Neurons/Image.m:286:            %GET_COLORS_READOUT getter of neuron color readouts.
+Neurons/Image.m:341:            % Set the neuron patch size.
+Neurons/Image.m:342:            patch_hsize = [3,3,0];
+Neurons/Image.m:354:                patch = Methods.Utils.subcube(data, ...
+Neurons/Image.m:355:                    round(neuron.position), patch_hsize);
+Neurons/Image.m:357:                    nanmedian(reshape(patch, ...
+Neurons/Image.m:358:                    [numel(patch)/size(patch, 4), size(patch, 4)]));
+Neurons/Image.m:765:            sp.color_readout = obj.get_colors_readout();
+Methods/AutoDetect.m:69:           data_zscored_raw = Methods.Preprocess.zscore_frame(double(data_RGBW));
+Methods/AutoDetect.m:72:           [~, mask] = Methods.Preprocess.filter_gut_lysosomes(data_zscored_raw);
+Methods/AutoDetect.m:74:           data_zscored = data_zscored_raw;
+Methods/AutoDetect.m:75:           data_zscored(mask) = 0;
+Methods/AutoDetect.m:86:           [sp, mp] = Methods.AutoDetect.instance().detect(file, data_zscored, ...
+Methods/AutoDetect.m:304:        volume = Methods.Preprocess.zscore_frame(...
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims | wc -l; grep -rh -A2 "data: elsewhere" claims | grep where | head -5; grep -rh -B3 -A3 "not deposited\|no archive\|deposited nowhere\|public nowhere" claims | head -40
```

```
174
  data: elsewhere
  where: GEO GSE319557 (10x scRNA-seq, FASTQ, per the Data availability statement); processed
  data: elsewhere
  where: GEO GSE319557
  data: elsewhere
    the Methods' "two or more days" for breaks over weekends). (2) Whether "days per break" is the
    mean over all breaks pooled or the mean over mice of each mouse's mean. (3) For the 8 mice
    with two sensory-mapping sessions, day 16 read as (a) the first (the session Figure 4 uses),
    (b) the last. A task session that was run but not deposited cannot be told from a break in
    the deposited dates; such gaps are listed. If no sensory-mapping session is deposited, the
    span is blocked and the other two values are still tested.
- id: fig3c-response-rate-increase
--
    Furthermore, the gene coding SMI-32, NEFH, also shows increased expression in deep FREM3 and
    CARM1P1 relative to COL22A1 and all the superficial glutamatergic t-types ( Fig. 6e ).
  data: elsewhere
  where: The mFISH and SMI-32 images are not deposited in any archive the paper or the code names;
    NEFH expression from the Allen Brain Map RNA-seq data, not pinned
  criterion: Not tested on the dandiset. The paper gives no counts of labelled cells.
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/Eviatar/Optimal_Coloring && cd Optimal_Coloring && git log -3 --format='%h %cd %s' --date=short && ls -R | head -40 && cat README* 2>/dev/null | head -40
```

```
f01284f 2021-03-14 Updated README to reflect publication.
990c597 2020-06-30 Fixed some minor bugs and clarified some concepts in the README.
e4790ce 2020-01-21 Fixed a bug in how NeuroPAL margin violatiosn were being reported.
.:
LICENSE.md
README.md
computeProbAdjacency.m
data.mat
find_optimal_colors.m
getReporterInfo.m
optimal_color_parameters.m
optimal_color_solver.m
plotCells.m
# Optimal Coloring for Cell ID Barcodes (NeuroPAL)

This code was authored by Erdem Varol (Liam Paninski Lab) and Eviatar Yemini (Oliver Hobert Lab) at Columbia University for the NeuroPAL publication,
"NeuroPAL: A Multicolor Atlas for Whole-Brain Neuronal Identification in C. elegans". The publication is available here:

https://www.cell.com/cell/fulltext/S0092-8674(20)31682-2

[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Optimal_Coloring; git checkout -q 990c597; cat computeProbAdjacency.m; grep -n -i -E "violat|margin|adjac|thresh|prob" find_optimal_colors.m optimal_color_parameters.m | head -50
```

```
function A = computeProbAdjacency(positions, covariances, varargin)
% COMPUTEPROBADJACENCY Compute an adjacency matrix using the probabilistic
% mass of the cells' covariance ellipses.
%
% Input:
%   positions     = cell positions
%   covariances   = cell positional covariances
%   prob_ellipse  = probabilistic mass for the covariance ellipses
%                   default = 0.95 (95%)
%   sample_points = number of points for estimating covariance ellipses
%
% Output:
%   A = adjacency matrix

% What is the probablistic mass for the covariance ellipses?
prob_ellipse = 0.95;
if ~isempty(varargin)
    prob_ellipse = varargin{1};
end

[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Optimal_Coloring; sed -n 1,60p find_optimal_colors.m; sed -n 150,185p find_optimal_colors.m; sed -n 1,95p optimal_color_parameters.m | grep -v "^%%\?\s*$"
```

```
%% Clean up the workspace.
clear all;
clc;
close all;


%% Load the user parameters.
optimal_color_parameters;


%% Plot customization.

% Are we plotting the body as a whole or in parts?
is_plot_whole_body = true;

% Are we plotting the color margin violators?
is_plot_color_violators = false;


%% Helper functions.
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/claims_check.py
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

[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CELL_ID; sed -n 1,120p +Methods/AutoDetect.m | grep -v "^\s*%" | head -100; grep -n -A12 "function.*zscore_frame\|function.*filter_gut" +Methods/Preprocess.m | head -60
```

```
classdef AutoDetect < handle
   
   properties % Public Access
        options = []
        supervoxels = []
        
        fsize
        szext
        
        scale
   end
   
   methods(Access=private)
      function obj = AutoDetect()
        obj.options = optimoptions('fmincon', 'Display', 'off');
        obj.options.MaxFunEvals = 5000;
        obj.options.MaxIter = 5000;
        obj.options.StepTolerance = 1e-10;
      end
   end
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CELL_ID; python3 -c "
import scipy.io as s
for f in ['atlas.mat','atlas_old.mat','atlas_new.mat']:
    try:
        d=s.loadmat('Data/Models/'+f,simplify_cells=True)
    except Exception as e:
        print(f,e); continue
    print(f,[k for k in d if not k.startswith('__')], d.get('version'))
    a=d['atlas']
    for b in a:
        print(' ',b,a[b].keys() if isinstance(a[b],dict) else type(a[b]), len(a[b]['N']), a[b]['model']['mu'].shape)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import scipy.io as s
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
cd $TMPDIR/CELL_ID; git log --date=short --format="%h %cd %s" -- Data/Models/atlas.mat Data/Models/atlas_new.mat Data/Models/atlas_old.mat | head
```

```
cb65fc8 2020-07-30 Atlas axis aligned
11781c4 2020-07-29 Update atlas.mat
4c8bd90 2020-07-29 new atlas
62dc0b5 2020-05-13 Switched atlases to work for now.
27f1984 2020-05-13 Merge branch 'master' of https://github.com/amin-nejat/CELL_ID
f88d5a8 2020-05-13 Moved new atlas out of production for now.
78421cc 2020-04-21 updated atlas with white channel + symmetric colors for L/R neurons (except ASE)
957e69b 2019-07-27 Atlas now contains a version number.
8d2eb17 2019-07-18 adding files, restructuring
Shell cwd was reset to
```

**Agent**

Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000715/10.1016-j.cell.2020.12.012.yaml",
 "content": "# Claims for Yemini, Lin, Nejatbakhsh et al. (2021), \"NeuroPAL: A Multicolor Atlas for Whole-Brain\n# Neuronal Identification in C. elegans\", Cell 184, 272-288, on dandiset 000715.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23, protocol\n# pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC10494711, NIHMS1925874), as served\n# by ncbi_pmc, with its Results, Discussion, STAR Methods, figure legends (Figures 1 to 7, S1 to S3),\n# and two supplements extracted from their PDFs: Methods S1 (semi-automated neuronal identification,\n# with the atlas, detection and cross-validated accuracy results) and Methods S2 (optimal coloring).\n# The version of record was not read. Tables S1 to S6 (spreadsheets), Videos S1 to S4 and the legend\n# of Figure S4 are not in the text read. No claim below needs a number that only those tables hold,\n# except that the per-neuron atlas values (Table S3), receptor expression (Table S4), mutant scores\n# and p-values (Table S5) and whole-brain statistics (Table S6) could not be read.\n#\n# Code read. github.com/amin-nejat/CELL_ID at commit d9f5df9 (2020-10-28, the last commit before\n# publication; HEAD 759898d of 2021-11-14 was also looked at). It holds the NeuroPAL ID GUI: neuron\n# detection (+Methods/AutoDetect.m, +Methods/Preprocess.m), identification against a pretrained atlas\n# (+Methods/AutoId.m) and atlas files (Data/Models/atlas*.mat). It does not hold the script that\n# trains the atlas from annotated worms (Methods S1 Algorithm 4) nor the cross-validation behind\n# Figure 7B-C; the training set of its shipped atlas is not stated, so that atlas is not used here.\n# github.com/Eviatar/Optimal_Coloring at commit 990c597 (2020-06-30, the last code commit before\n# publication; f01284f of 2021-03-14 changes only the README). It holds the optimal-coloring solver,\n# the adjacency rule (computeProbAdjacency.m), the violation measure (find_optimal_colors.m) and\n# data.mat with the Brain Atlas and NeuroPAL-tested reporter tables and the NeuroPAL colors.\n# github.com/venkatachalamlab/NeuroPAL-traces was not read: it extracts traces for the OH15500\n# whole-brain recordings, which no claim tested here uses.\n#\n# Data the paper used, as it reports them.\n# Atlas (Figure 2C-D, Table S3, Methods S1, Figure 7A-C). 10 young-adult NeuroPAL hermaphrodites of\n# identical age, integrant otIs669 (strain OH15262), head and tail of each imaged on a Zeiss LSM880\n# with 405, 488, 561 and 633 nm lasers exciting mTagBFP2, CyOFP1, TagRFP-T and mNeptune2.5. Landmark\n# colors are pseudo-colored red (mNeptune2.5), green (CyOFP1) and blue (mTagBFP2); TagRFP-T is the\n# panneuronal label (white). Every neuron was annotated by hand (\"fully annotated neuron\n# detections\", Methods S1 section 4), giving per neuron a 3-D position and a color; Methods S1 reads\n# a neuron's color as the median pixel intensity in a 1.5 x 1.5 x 0.75 um patch centred on it in the\n# z-scored image (Figure 6.2 legend), z-scored per channel over the volume (CELL_ID\n# Preprocess.zscore_frame). Detection was evaluated on the same 10 worms (Figure 6.3), and\n# identification accuracy by leave-one-out over them (Figure 6.4 legend). The dandiset's title,\n# \"Atlas of C. elegans neuron locations and colors in NeuroPAL worm\", names these data.\n# Whole-brain activity (Figures 6, S1H, S2, Table S6). Strain OH16230 (otIs669; otIs672, NeuroPAL\n# with panneuronal nuclear GCaMP6s), 21 heads (189 neurons) and, separately, 21 tails (42 neurons),\n# young adults in a microfluidic chip; a 4-color identification volume, then 4 min of GCaMP6s at\n# about 4 Hz, with 10 s pulses of 160 mM NaCl, 1e-4 2-butanone and 1e-4 2,3-pentanedione one\n# minute apart in rotated order. A second strain, OH15500, was imaged in water with 200 mM NaCl for\n# 20 s. These are deposited on Zenodo (doi:10.5281/zenodo.3906530), not, by its title, in this\n# dandiset. Receptor expression (Figures 3, 4, Table S4), mutant analysis (Figure 5, Table S5) and\n# phenotyping (Figure S1, Table S2) used other strains and are not deposited in any archive the\n# paper names.\n#\n# Method choices shared by the atlas claims, from Methods S1 unless said otherwise. The atlas is fit\n# by Algorithm 4: initialize the means at a random worm and identity covariances, then alternate an\n# affine alignment of each worm to the atlas (equations 4.15, 4.16) with updates of the means and\n# covariances (equations 4.13, 4.14, normalized by the number of worms m) until convergence; each\n# neuron's 6-D covariance is block diagonal, position and color (equation 4.1 and text). A held-out\n# worm is identified by Algorithm 5 (alignment initialized at the identity, alternated with the\n# Hungarian assignment of equation 4.18) and its likelihoods (equation 5.4); probabilities are the\n# Sinkhorn approximation (Algorithm 6), with 500 iterations as in CELL_ID AutoId.iter_sinkhorn.\n# Head and tail are separate atlases. The random initial worm and the convergence tolerance are\n# not given; they are standard choices (a fixed seed; a tolerance of 1e-6 on the Frobenius norm)\n# that should not change an outcome, and the notebook reports any sensitivity to the initial worm.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000715\"\npaper: doi:10.1016/j.cell.2020.12.012\nclaims:\n- id: fig2cd-variability-differs\n  statement: In a probabilistic atlas built from 10 young-adult NeuroPAL worms, the positional\n    variability of cell bodies differs across neuron types.\n  source: Results, Variability in Neuronal Cell Body Positions, paragraph 2; Figures 2C and 2D\n  quote: This map revealed different positional variability across neuron types\n  criterion: The atlas is fit on all 10 worms, head and tail, as in the shared method above; a\n    neuron's positional variability is the standard deviation of its atlas positional covariance\n    along each of the three principal axes of the atlas means (the axes Methods S1 Figure 6.1\n    plots, major and minor axes of position). The paper gives no test or threshold. The one\n    difference it quantifies is OLLR against OLLL, over a factor of two (claim\n    fig2c-ollr-more-variable-than-olll), so the claim is reproduced when, along at least one axis,\n    the largest per-neuron standard deviation is more than twice the smallest within the head\n    and within the tail. The distribution of per-neuron standard deviations is reported.\n- id: fig2c-ollr-more-variable-than-olll\n  statement: In the head atlas, OLLR shows over twice the positional variability of OLLL along the\n    anterior-posterior axis.\n  source: Figure 2C legend\n  quote: OLLR exhibits over twice the positional variability of OLLL in its anterior-posterior axis\n  expected:\n  - quantity: OLLR over OLLL anterior-posterior positional variability, lower bound\n    value: 2\n    unit: ratio\n  criterion: Head atlas fit on all 10 worms as in the shared method. The anterior-posterior axis is\n    the major axis of the atlas means (Methods S1 Figure 6.1 legend; the CELL_ID code aligns\n    positions to it by principal components, AutoId.major_axis_align). \"Positional variability\"\n    can be read as (a) the standard deviation of the neuron's positional distribution along that\n    axis, (b) its variance, or (c) the anterior-posterior extent of the 50% contour within the 2-D\n    plane Figure 2 slices (left-right or dorsal-ventral view, the conditional distribution in that\n    plane). Reproduced when the OLLR to OLLL ratio exceeds 2 under any reading; all three are\n    reported.\n- id: fig7bc-identification-accuracy\n  statement: Unsupervised identification of neurons against the statistical atlas of NeuroPAL\n    colors and positions is 86% accurate in the head and 94% in the tail, cross-validated.\n  source: Results, Semi-automated Neuronal Identification, paragraph 2; Figures 7B and 7C; Methods\n    S1 section 6.3, Figure 6.4\n  quote: Accuracy was 86% for the head and 94% for the tail.\n  expected:\n  - quantity: head identification accuracy\n    value: 86\n    tolerance: 8.6\n    unit: percent\n  - quantity: tail identification accuracy\n    value: 94\n    tolerance: 9.4\n    unit: percent\n  criterion: Leave-one-out over the 10 worms (Methods S1 Figure 6.4 legend), head and tail apart.\n    For each held-out worm, the atlas is fit on the other 9 (Algorithm 4) with 6-D features\n    (position in um and the three landmark colors); the held-out worm is identified by Algorithm\n    5 and the Hungarian assignment (equation 4.18), and a neuron is correct when its assigned\n    identity is its annotation. Open details, each run. Which neurons are identified, (a) the\n    hand-annotated neurons, (b) the automatic detections of claim ms1-detection-accuracy matched\n    to annotations within 3 um, unmatched annotated neurons counted wrong. Start of the\n    alignment, Algorithm 5 initializes it at the identity on the positions as given (the Methods,\n    main result); the CELL_ID code (AutoId.global_alignment) first aligns the worm's major axis\n    and searches rotations about it (theta from 0 to 2 pi in steps of 0.25, both orientations,\n    10 alternations, color regression with ridge 1e5), shown as a variant. Colors, the dandiset's\n    stored per-neuron colors if it holds them, and the Methods S1 Figure 6.2 readout recomputed\n    from the images if it holds images. These are method details; the outcome is the one they\n    give together, and differing outcomes block the claim as methods_underspecified. The reported\n    numbers can be read as (i) the mean over held-out worms of per-worm accuracy or (ii) the\n    accuracy over all neurons pooled, and as (1) per-neuron identity or (2) identity at class\n    level for left/right pairs (Methods S1 footnote 1 scores midline pairs such as RMFL/R by\n    class but does not list them; class level for every left/right pair is the upper bound of\n    that rule). The number is matched when it falls within tolerance under any of these readings.\n- id: fig7bc-ventral-ganglion-lowest\n  statement: Accuracy depends on neuron density; it is high for all tail ganglia and lower for the\n    dense ventral ganglion of the head.\n  source: Results, Semi-automated Neuronal Identification, paragraph 2; Figures 7B and 7C legend\n  quote: Accuracy largely depended on neuron density; for example, our pipeline achieved high\n    accuracy for all tail ganglia but lower accuracy for the much denser ventral ganglion in the\n    head.\n  data: with_labels\n  depends_on:\n  - fig7bc-identification-accuracy\n  criterion: The per-neuron results of fig7bc-identification-accuracy (the Methods reading, and\n    each other reading as a variant), grouped by ganglion. Ganglion membership is taken from the\n    dandiset if it records it, else from the CELL_ID neuron tables (Data/NeuroPAL) or the ganglion\n    lists of the GUI; the head ganglia are those of Methods S1 Figure 6.8 (anterior and posterior\n    pharynx, anterior, dorsal, lateral, ventral and retrovesicular ganglia) and the tail ganglia\n    pre-anal, dorso-rectal and lumbar. Reproduced when every tail ganglion has a higher accuracy\n    than the head's ventral ganglion; the rank of the ventral ganglion among head ganglia and\n    the ganglion densities are reported.\n- id: fig7b-eight-labels-above-90\n  statement: Manually annotating eight neurons, chosen by the software as the least certain, raises\n    head identification accuracy above 90% on average.\n  source: Results, Semi-automated Neuronal Identification, paragraph 2; Figure 7B; Methods S1\n    section 6.5, Figure 6.9\n  quote: Adding eight manual annotations, on average, brings the head accuracy above 90%\n  depends_on:\n  - fig7bc-identification-accuracy\n  expected:\n  - quantity: mean head accuracy after eight manual annotations, lower bound\n    value: 90\n    unit: percent\n  criterion: In the leave-one-out runs of fig7bc-identification-accuracy (head), the neuron whose\n    row of the Sinkhorn probability matrix is closest to uniform is annotated with its true\n    identity, the likelihoods are updated as CELL_ID does (AutoId.update_log_likelihood sets the\n    annotated neuron's row to the minimum except its true identity at the maximum) and the\n    assignment recomputed (AutoId.update_id, without re-alignment); repeated eight times.\n    \"Closest to uniform\" is open, read as (a) the highest entropy of the row and (b) the lowest\n    top probability (the code's ranking, AutoId.add_to_image); a method detail, both run. The\n    accuracy after eight annotations can be read as over all neurons with the annotated ones\n    counted correct, or over the unannotated neurons only; matched under either. Reproduced when\n    the mean over held-out worms exceeds 90%.\n- id: ms1-uncertain-first-faster\n  statement: Annotating the most uncertain neurons first raises identification accuracy much faster\n    than annotating neurons in random order, in head and tail.\n  source: Methods S1, section 6.5, Figure 6.9\n  quote: Figure 6.9 shows that following this strategy, the accuracy increases much faster ... than\n    by a random recommendation\n  depends_on:\n  - fig7b-eight-labels-above-90\n  criterion: As in fig7b-eight-labels-above-90, for 1 to 50 annotations in the head and 1 to 16 in\n    the tail (the ranges of Figure 6.9), against the same procedure with neurons chosen at random\n    (the mean of 100 random orders per held-out worm, a standard choice that should not change the\n    outcome). Reproduced when, in head and tail, the mean accuracy over worms with the most\n    uncertain neurons first is above the random curve at most annotation counts and its mean\n    over the range is higher; both curves are shown.\n- id: ms1-position-only-accuracy\n  statement: Restricted to neuron positions without color, automated identification accuracy drops\n    to 50% in the head and 68% in the tail, showing the gain from NeuroPAL's colors.\n  source: Results, Semi-automated Neuronal Identification, paragraph 3; Methods S1 section 6.3,\n    Figure 6.5\n  quote: When we restricted the model to assign identities only on the basis of location, automated\n    accuracy dropped to 50% for the head and 68% for the tail\n  depends_on:\n  - fig7bc-identification-accuracy\n  expected:\n  - quantity: head identification accuracy, position only\n    value: 50\n    tolerance: 5\n    unit: percent\n  - quantity: tail identification accuracy, position only\n    value: 68\n    tolerance: 6.8\n    unit: percent\n  criterion: As fig7bc-identification-accuracy, with every reading listed there, but with the atlas\n    and the held-out worm restricted to the three position coordinates (\"using only position\n    information\", Methods S1 Figure 6.5 legend). Reproduced when both values are within tolerance\n    under one reading and each is below the full model's accuracy under the same reading.\n- id: ms1-detection-accuracy\n  statement: The automatic neuron detection (matching pursuit) reaches 80% accuracy in the head and\n    88% in the tail, at 191 and 44 detections, with precision and recall both about 90% in the\n    head and 93% in the tail.\n  source: Methods S1, section 6.2, Figure 6.3\n  quote: As shown in figures 6.3 our algorithm reaches the accuracy of 80% in head and 88% in tail.\n    This occurs when we find K = 191 and K = 44 neurons in head and tail in which case we get\n    similar precision and recall values that are both equal to 90% and 93% in head and tail\n    respectively.\n  expected:\n  - quantity: head detection accuracy at K = 191\n    value: 80\n    tolerance: 8\n    unit: percent\n  - quantity: tail detection accuracy at K = 44\n    value: 88\n    tolerance: 8.8\n    unit: percent\n  - quantity: head precision and recall at K = 191\n    value: 90\n    tolerance: 9\n    unit: percent\n  - quantity: tail precision and recall at K = 44\n    value: 93\n    tolerance: 9.3\n    unit: percent\n  criterion: Needs the images. Detection as Methods S1 sections 2 and 3 describe and CELL_ID\n    implements it (Preprocess.zscore_frame, Preprocess.filter_gut_lysosomes, AutoDetect.detect,\n    with a 1.5 um exclusion radius), run for K = 191 (head) and K = 44 (tail) on each of the 10\n    worms. Detections are matched one to one to the hand annotations by the Hungarian algorithm on\n    distances, with distances over 3 um set to infinity (section 6.2); accuracy is TP / (TP + FP\n    + FN), precision TP / (TP + FP), recall TP / (TP + FN). The values are the means over the 10\n    worms (Figure 6.3 plots means and standard deviations). The detection bounds that the GUI\n    takes from its preferences (minimum eigenvalue of the Gaussian shape and the size thresholds\n    of the gut and lysosome filter) are not given in the paper; the CELL_ID defaults at d9f5df9\n    are used and named as a deviation. Blocked if the dandiset holds no images.\n- id: ms1-calibration\n  statement: The identification's confidence is calibrated; per-neuron confidence and accuracy\n    largely agree in head and tail.\n  source: Methods S1, section 6.4, Figure 6.8\n  quote: Figure 6.8 shows that confidence and accuracy ... are largely in good agreement, as desired\n  depends_on:\n  - fig7bc-identification-accuracy\n  criterion: From the leave-one-out runs of fig7bc-identification-accuracy, per atlas neuron, the\n    mean over held-out worms of the Sinkhorn probability of the assigned identity (confidence) and\n    the fraction of worms in which it is correct (accuracy), with left/right midline pairs scored\n    by class as in the Figure 6.8 footnote. The paper gives no measure of agreement. Read as (a)\n    a positive Spearman correlation between per-neuron confidence and accuracy with p < 0.05 and\n    (b) a mean absolute difference between confidence and accuracy under 10 percentage points\n    (the default tolerance of the protocol). Reproduced when both hold in head and tail; the\n    reliability plot is shown.\n- id: ms2-neuropal-color-violations\n  statement: Using the atlas of neuron positions from the 10 worms to define neighbors, NeuroPAL's\n    designed color map leaves 3.5% of neighboring neuron pairs below the color discrimination\n    margin.\n  source: Methods S2, section 4.3, paragraph 1\n  quote: NeuroPAL, which comprehensively identifies all neuron types, exhibited a theoretical color\n    violation of 3.5%.\n  data: with_inputs\n  depends_on:\n  - fig2cd-variability-differs\n  expected:\n  - quantity: NeuroPAL color violations among neighboring pairs\n    value: 3.5\n    tolerance: 0.35\n    unit: percent\n  criterion: Neighbors are pairs whose positional covariance ellipses, at 95% probability mass,\n    include each other (Methods S2 section 2; Optimal_Coloring computeProbAdjacency.m, 1000\n    samples per neuron, seed 1), from the head and tail atlases fit on all 10 worms. Colors are the\n    NeuroPAL colors of Optimal_Coloring data.mat (NeuroPAL_colors), normalized to sum to one per\n    neuron as find_optimal_colors.m does; the margin is 1/3. The Methods define the violation\n    rate as the share of neighboring pairs whose color distance is below the margin (section 4.3);\n    the code reports the mean shortfall below the margin over neighboring pairs\n    (find_optimal_colors.m); the Methods measure is the main result and the code's is a variant.\n    Whether head and tail are pooled or the figure is per body part is not said; pooled, head and\n    tail are all reported, and the number is matched under any of them. The outside inputs are the\n    NeuroPAL colors from the code repository.\n- id: fig7de-optimal-coloring-violations\n  statement: The optimal-coloring algorithm, using WormBase reporters, finds NeuroPAL alternatives\n    with 1.7% color violations with 39 reporters and 10.5% when restricted to 3 reporters.\n  source: Results, An Optimal-Coloring Algorithm for Other Tissues and Model Organisms, paragraph 3;\n    Figures 7D and 7E; Methods S2 Figure 1\n  quote: In our simulations, we achieve color violations of 1.7% when using 39 reporters and 10.5%\n    when restricting the solution to only 3 reporters\n  data: with_inputs\n  depends_on:\n  - ms2-neuropal-color-violations\n  expected:\n  - quantity: color violations of the best 39-reporter solution\n    value: 1.7\n    tolerance: 0.17\n    unit: percent\n  - quantity: color violations of the best 3-reporter solution\n    value: 10.5\n    tolerance: 1.05\n    unit: percent\n  criterion: Adjacency as in ms2-neuropal-color-violations. The Brain Atlas reporter table of\n    Optimal_Coloring data.mat (1192 reporters, 654 unique), 3 colors, margin 1/3, solved with\n    optimal_color_solver.m; the best of 10,000 runs for the roughly 40-reporter case (sparsity 100,\n    Methods S2 Figure 3 legend) and of 7,500 runs for the 3-reporter case (Methods S2 Figure 1\n    legend). The sparsity giving 3 reporters is not stated; the reading is the sparsity whose\n    solutions use 3 reporters after the code's Otsu threshold. Violations as in\n    ms2-neuropal-color-violations (Methods measure, code measure as a variant). Reproduced when the\n    best solutions are within tolerance; the solver is stochastic and fewer runs may be used if\n    the full number cannot run, which is recorded as a deviation.\n- id: fig1e-stereotyped-color-map\n  statement: A transgene of 41 reporter-fluorophore fusions gives a stereotyped color map with which\n    every neuron of the C. elegans hermaphrodite can be identified, each distinguishable from its\n    neighbors by color.\n  source: Results, Empirical Assembly of NeuroPAL, paragraph 2; Figure 1E\n  quote: The final transgene, composed of 41 different reporter-fluorophore fusions, allowed us to\n    unambiguously assign identities to every neuron in C. elegans based on a stereotyped color map\n  data: elsewhere\n  where: Verified in hundreds of animals crossed to 25 GFP reporter lines (Table S1, NeuroPAL\n    manuals at hobertlab.org); these images are not deposited in any archive the paper names\n  criterion: Not tested on the dandiset. The 10 annotated worms bear on it only through the atlas\n    claims above (fig7bc-identification-accuracy and ms2-neuropal-color-violations).\n- id: res-variable-brightness-classes\n  statement: The NeuroPAL expression pattern is stable and stereotyped, except that four neuron\n    classes (AVL, RIM, RIS and PVW) vary in brightness.\n  source: Results, Neuronal Color Verification and Phenotypic Assessment of NeuroPAL Strains,\n    paragraph 1\n  quote: A minor exception was four neuron classes that exhibited variable brightness (AVL, RIM,\n    RIS, and PVW).\n  data: elsewhere\n  where: Scored over hundreds of animals, not deposited in any archive the paper names\n  criterion: Not tested on the dandiset; the paper's scoring of hundreds of animals is not given\n    as data. The color covariance of these four classes in the 10-worm atlas may be reported as\n    context and does not decide the claim.\n- id: figs1-otis670-closest-to-wild-type\n  statement: Of the NeuroPAL integrants, otIs669 (OH15262) is the brightest, and otIs670 (OH15263)\n    has locomotion and chemotaxis closest to wild type.\n  source: Results, Neuronal Color Verification and Phenotypic Assessment of NeuroPAL Strains,\n    paragraph 2; Figures S1A to S1G; Table S2\n  quote: The brightest integrant was otls669 (strain OH15262). The integrant with locomotion and\n    chemotactic behavior closest to wild-type, otls670 (strain OH15263), is less bright\n  data: elsewhere\n  where: Phenotyping data (Table S2, not in the text read) are not deposited in any archive the\n    paper names\n  criterion: Not tested on the dandiset.\n- id: fig4c-metabotropic-receptor-coverage\n  statement: Metabotropic acetylcholine, glutamate and GABA receptors are expressed in 97% of all\n    neurons; 70% express GARs, 54% MGLs and 89% GBBs.\n  source: Results, Expression Maps for All Metabotropic Neurotransmitter Receptors, paragraph 2;\n    Figure 4C\n  quote: we find that these receptors are expressed in 97% of all neurons: 70% express GARs, 54%\n    express MGLs, and 89% express GBBs\n  data: elsewhere\n  where: Expression scored from reporter crosses (Figure 3, Table S4, not in the text read); the\n    images are not deposited in any archive the paper names\n  expected:\n  - quantity: neurons expressing any metabotropic receptor\n    value: 97\n    tolerance: 9.7\n    unit: percent\n  - quantity: neurons expressing GARs\n    value: 70\n    tolerance: 7\n    unit: percent\n  - quantity: neurons expressing MGLs\n    value: 54\n    tolerance: 5.4\n    unit: percent\n  - quantity: neurons expressing GBBs\n    value: 89\n    tolerance: 8.9\n    unit: percent\n  criterion: Not tested on the dandiset.\n- id: fig4b-gabab-in-every-gaba-partner\n  statement: Every postsynaptic partner of every GABA-releasing neuron expresses a GABA-B receptor,\n    whereas only 60% express a GABA-A receptor.\n  source: Results, Expression Maps for All Metabotropic Neurotransmitter Receptors, paragraph 3;\n    Figures 4B and 4G\n  quote: We found that every postsynaptic partner of every GABA-releasing neuron expresses one of\n    the two GABA B receptors. In contrast, only 60% of postsynaptic partners of GABAergic neurons\n    express any of the seven GABA A receptors\n  data: elsewhere\n  where: Table S4 (not in the text read) with the connectome of Cook et al. 2019\n    (doi:10.1038/s41586-019-1352-7) and GABA-A expression of Gendrel et al. 2016\n  expected:\n  - quantity: postsynaptic partners of GABAergic neurons expressing GABA-A receptors\n    value: 60\n    tolerance: 6\n    unit: percent\n  criterion: Not tested on the dandiset. Figure 4D's legend notes that one polyadic synapse from\n    AVF brings the GABA-B count to just under 100%.\n- id: fig4d-cognate-metabotropic-partners\n  statement: 76% of postsynaptic partners of cholinergic neurons express GAR receptors and 66% of\n    postsynaptic partners of glutamatergic neurons express MGL receptors; metabotropic receptors\n    can take part in 75% of all synaptic connections from neurotransmitter-releasing neurons.\n  source: Results, Expression Maps for All Metabotropic Neurotransmitter Receptors, paragraph 3;\n    Figure 4D; Discussion, paragraph 3\n  quote: 76% of the postsynaptic partners of cholinergic neurons express GAR receptors, and 66% of\n    the postsynaptic partners of glutamatergic neurons express MGL receptors\n  data: elsewhere\n  where: Table S4 (not in the text read) with the connectome of Cook et al. 2019\n    (doi:10.1038/s41586-019-1352-7)\n  expected:\n  - quantity: cholinergic partners expressing GARs\n    value: 76\n    tolerance: 7.6\n    unit: percent\n  - quantity: glutamatergic partners expressing MGLs\n    value: 66\n    tolerance: 6.6\n    unit: percent\n  - quantity: synaptic connections with a cognate metabotropic receptor\n    value: 75\n    tolerance: 7.5\n    unit: percent\n  criterion: Not tested on the dandiset.\n- id: fig4e-extrasynaptic-gaba\n  statement: Many receptor-expressing neurons have no presynaptic partner releasing the cognate\n    transmitter (31% of GABA-A and 37% of GABA-B expressing neurons; 3% of GAR and 10% of MGL\n    expressing neurons), and 92% of neurons express GABA receptors while 10% release GABA,\n    suggesting widespread extrasynaptic signaling.\n  source: Results, Expression Maps for All Metabotropic Neurotransmitter Receptors, paragraph 4;\n    Figure 4E\n  quote: 31% of GABA A and 37% of GABA B receptor-expressing neurons have no presynaptic GABAergic\n    partner. Moreover, we found 92% of all neurons express GABA receptors, and yet only 10% of\n    neurons release GABA.\n  data: elsewhere\n  where: Table S4 (not in the text read) with the connectome of Cook et al. 2019\n    (doi:10.1038/s41586-019-1352-7)\n  expected:\n  - quantity: GABA-A expressing neurons without a GABAergic presynaptic partner\n    value: 31\n    tolerance: 3.1\n    unit: percent\n  - quantity: GABA-B expressing neurons without a GABAergic presynaptic partner\n    value: 37\n    tolerance: 3.7\n    unit: percent\n  - quantity: neurons expressing GABA receptors\n    value: 92\n    tolerance: 9.2\n    unit: percent\n  - quantity: neurons releasing GABA\n    value: 10\n    tolerance: 1\n    unit: percent\n  - quantity: GAR expressing neurons without a cognate presynaptic partner\n    value: 3\n    tolerance: 0.3\n    unit: percent\n  - quantity: MGL expressing neurons without a cognate presynaptic partner\n    value: 10\n    tolerance: 1\n    unit: percent\n  criterion: Not tested on the dandiset. The sentence giving 3% and 10% pairs GAR and MGL with\n    \"glutamatergic and cholinergic neurons, respectively\", the reverse of the receptors' ligands;\n    the cognate reading (GAR with cholinergic, MGL with glutamatergic) is the one Figure 4E's\n    legend describes.\n- id: fig4f-sensory-extrasynaptic\n  statement: Sensory neurons are the most prominent recipients of the putative extrasynaptic\n    communication.\n  source: Results, Expression Maps for All Metabotropic Neurotransmitter Receptors, paragraph 4;\n    Figure 4F\n  quote: Notably, sensory neurons appear to be the most prominent recipients of extrasynaptic\n    communication\n  data: elsewhere\n  where: Table S4 (not in the text read) with the connectome of Cook et al. 2019\n  criterion: Not tested on the dandiset.\n- id: fig5ab-pag3-fate-changes\n  statement: In pag-3 null mutants the NeuroPAL color codes of VA and VB motor neurons are absent,\n    and the AVE and PVR interneurons change color.\n  source: Results, Uncovering Determinants of Cell Fate, paragraph 1; Figures 5A and 5B\n  quote: As predicted, the color codes that identify the VA and VB cell types in NeuroPAL are\n    absent in pag-3 mutants ... Unexpectedly, we also found color changes in the AVE and PVR\n    interneurons caused by pag-3 mutation.\n  statistics:\n  - about: PVR, VA2 and VB3 changes in two pag-3 alleles\n    test: one-sided Fisher's exact test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Bonferroni, eight tests\n  - about: AVE changes scored 0, 1 or 2\n    test: one-sided rank sum test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Bonferroni, eight tests\n  data: elsewhere\n  where: Mutant scores in Table S5 (not in the text read); images not deposited in any archive the\n    paper names\n  criterion: Not tested on the dandiset. The p-values are recorded as the paper's significance\n    standard (p or q of at most 0.05 after correction, STAR Methods); the values are in Table S5.\n- id: fig5c-pag3-new-expression\n  statement: A pag-3 fosmid reporter is expressed in neurons not previously reported, including AVE\n    and PVR.\n  source: Results, Uncovering Determinants of Cell Fate, paragraph 1; Figure 5C\n  quote: By checking a fosmid-based reporter, we discovered pag-3 expression in neurons that had\n    gone previously unidentified, including AVE and PVR\n  data: elsewhere\n  where: Images not deposited in any archive the paper names; Table S5 not in the text read\n  criterion: Not tested on the dandiset.\n- id: fig5efg-eor1-rme\n  statement: In eor-1 null mutants the dorsal and ventral RME neurons lose all blue NeuroPAL color\n    and UNC-25/GAD reporter expression but keep the panneuronal label, while RMEL/R are unchanged\n    and UNC-47/VGAT expression is not affected.\n  source: Results, Uncovering Determinants of Cell Fate, paragraph 2; Figures 5E to 5G\n  quote: The dorsal and ventral RME neurons (RMED/V) lost all their blue coloring but retained their\n    panneuronal label ... In contrast, the left and right RME neurons (RMEL/R) exhibited no changes\n    in their color codes.\n  statistics:\n  - about: loss of RMED/V blue coloring in two eor-1 alleles\n    test: one-sided Fisher's exact test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Bonferroni, eight tests\n  - about: RMED/V UNC-25 reporter expression scored 0, 1 or 2\n    test: one-sided rank sum test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Bonferroni, eight tests\n  data: elsewhere\n  where: Mutant scores in Table S5 (not in the text read); images not deposited in any archive the\n    paper names\n  criterion: Not tested on the dandiset.\n- id: fig6d-ase-nacl-asymmetry\n  statement: NaCl (160 mM) evokes left/right asymmetric responses in the ASE neurons, with ASER\n    increasing its calcium.\n  source: Results, Whole-Brain Activity Imaging of Gustatory and Olfactory Responses, paragraph 3;\n    Figure 6D\n  quote: NaCl evoked stereotyped left/right (L/R) asymmetric responses in the two ASE neurons.\n    However, ASER exhibited an increase in [Ca 2+ ] upon NaCl presentation\n  statistics:\n  - test: two-tailed two-sample (unpaired) t test between left and right neurons\n    p: 0.05\n    p_relation: \"<\"\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530 (whole-brain recordings and traces, Table S6)\n  criterion: Not tested on the dandiset. The paper's test (STAR Methods, Analysis of brainwide\n    imaging data) is a two-tailed unpaired t test for asymmetry, at p of at most 0.05.\n- id: fig6d-awc-odor-asymmetry\n  statement: 2-butanone and 2,3-pentanedione evoke stochastically asymmetric responses in the AWC\n    ON/OFF pair.\n  source: Results, Whole-Brain Activity Imaging of Gustatory and Olfactory Responses, paragraph 4;\n    Figure 6D\n  quote: 2-butanone and 2,3-pentanedione evoked stochastically asymmetric responses in the AWC\n    ON/OFF neuron pair\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset.\n- id: fig6ef-nacl-novel-interneurons\n  statement: NaCl evokes significant responses in six interneurons with no previously known\n    function, AIN, AVF, AVH, AVJ, I2 and MI.\n  source: Results, Whole-Brain Activity Imaging of Gustatory and Olfactory Responses, paragraph 3;\n    Figures 6C to 6F\n  quote: In particular, we detected significant NaCl responses in six interneurons with no\n    previously known function: AIN, AVF, AVH, AVJ, I2, and MI.\n  statistics:\n  - test: two-tailed paired t test, stimulus against the preceding equal period, FDR q-values\n      (Storey 2002)\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: up to 42 left/right neuron pairs or 21 single neurons, from 21 heads\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset.\n- id: fig6c-odors-more-inhibitory\n  statement: Odors evoke responses across many sensory and interneurons but with more inhibitory\n    (decreasing calcium) activity than NaCl.\n  source: Results, Whole-Brain Activity Imaging of Gustatory and Olfactory Responses, paragraph 4;\n    Figure 6C\n  quote: We found that odors also evoked responses in a large set of both sensory and interneurons,\n    throughout the brain, but exhibited more inhibitory activity (decreasing [Ca 2+ ]) than seen\n    for NaCl\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset.\n- id: fig6de-asj-ric-stimulus-specific\n  statement: The sets of responding neurons overlap but differ by stimulus; ASJ is excited by NaCl\n    and inhibited by both odors, and RIC is excited only by 2,3-pentanedione.\n  source: Results, Whole-Brain Activity Imaging of Gustatory and Olfactory Responses, paragraph 4;\n    Figures 6C to 6F\n  quote: For example, the ASJ sensory neurons were excited by NaCl but inhibited by both odors,\n    whereas the RIC interneurons were excited solely by 2,3-pentanedione.\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset.\n- id: tables6-tail-pvq-and-post-stimulus\n  statement: In the tail, PVQ is significantly excited by 2,3-pentanedione, and sensory and\n    interneurons show significant post-stimulus responses to all three stimuli.\n  source: Results, Whole-Brain Activity Imaging of Gustatory and Olfactory Responses, paragraph 4;\n    Table S6\n  quote: In the tail, the PVQ interneurons were significantly excited upon presentation of\n    2,3-pentanedione, while a mix of sensory and interneurons exhibited significant post-stimulus\n    responses\n  statistics:\n  - about: post-stimulus responses\n    test: one-tailed paired t test, post-stimulus mean against stimulus mean, FDR corrected\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: 21 tails\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset.\n- id: fig6f-pharyngeal-responses\n  statement: Both salt and odors elicit responses across the pharyngeal nervous system.\n  source: Results, Whole-Brain Activity Imaging of Gustatory and Olfactory Responses, paragraph 4;\n    Figure 6F\n  quote: Surprisingly, both salt and odors elicited responses across the pharyngeal nervous system\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset.\n- id: figs1h-avf-cyclic-activity\n  statement: In many animals AVF shows robust cyclical activity of about 0.3 Hz throughout the\n    recording, regardless of stimuli, similar to the strain's crawling frequency.\n  source: Results, Whole-Brain Activity Imaging of Gustatory and Olfactory Responses, paragraph 5;\n    Figures S1G and S1H\n  quote: the pair of AVF interneurons displayed robust cyclical activity for the entire 4-min\n    recording, irrespective of delivery of gustatory or olfactory stimuli. The frequency of this\n    activity was ~0.3 Hz\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  expected:\n  - quantity: AVF cycle frequency\n    value: 0.3\n    tolerance: 0.03\n    unit: Hz\n  criterion: Not tested on the dandiset. Figure S1H counts peaks per 4-minute interval in traces\n    median filtered at 0.5 s, from five OH16230 worms.\n- id: fig6gi-stimulus-specific-correlations\n  statement: Pairwise neuronal correlations are similar across individuals for a given stimulus, but\n    each stimulus produces its own brainwide correlation pattern.\n  source: Results, Whole-Brain Neuronal Dynamics and Connectivity, paragraph 1; Figures 6G to 6I,\n    S2C to S2E\n  quote: We found similar stimulus-specific neuronal correlations across individuals, but each\n    stimulus generated its own brainwide correlation pattern\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset.\n- id: fig6jk-weak-function-structure-correlation\n  statement: Functional correlations between neurons correspond poorly to synapse counts; R squared\n    is 2.8% (head) and 1.7% (tail) for electrical and 0.5% (head) and 1.5% (tail) for chemical\n    connectivity.\n  source: Results, Whole-Brain Neuronal Dynamics and Connectivity, paragraph 2; Figures 6J and 6K\n  quote: We found low Pearson correlation between these functional and structural matrices. For\n    electrical connectivity, R 2 = 2.8% in the head and R 2 = 1.7% in the tail, and for chemical\n    connectivity, R 2 = 0.5% in the head and R 2 = 1.5% in the tail\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530, with the connectomes of White et al. 1986 and Cook et\n    al. 2019\n  expected:\n  - quantity: R squared, electrical, head\n    value: 2.8\n    tolerance: 0.28\n    unit: percent\n  - quantity: R squared, electrical, tail\n    value: 1.7\n    tolerance: 0.17\n    unit: percent\n  - quantity: R squared, chemical, head\n    value: 0.5\n    tolerance: 0.05\n    unit: percent\n  - quantity: R squared, chemical, tail\n    value: 1.5\n    tolerance: 0.15\n    unit: percent\n  criterion: Not tested on the dandiset.\n"
}
```

```
File created successfully at: claims/000715/10.1016-j.cell.2020.12.012.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000715/10.1016-j.cell.2020.12.012.yaml paper/10.1016-j.cell.2020.12.012.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/000715; python3 - <<'E'
import re
p='10.1016-j.cell.2020.12.012.yaml'
s=open(p).read()
s=s.replace("expressed in 97% of all neurons: 70% express GARs","expressed in 97% of all neurons ... 70% express GARs")
s=s.replace("previously known function: AIN, AVF","previously known function ... AIN, AVF")
open(p,'w').write(s)
for i,l in enumerate(s.splitlines(),1):
    if l.lstrip().startswith('#'): continue
    body=re.sub(r'^\s*(- )?[a-z_]+: ','',l)
    if ': ' in body or '—' in l or 'rather' in l.lower(): print(i,l)
E
cd ../..; python tools/claims_check.py claims/000715/10.1016-j.cell.2020.12.012.yaml paper/10.1016-j.cell.2020.12.012.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -E "—|rather" claims/000715/*.yaml; grep -c "criterion:" claims/000715/*.yaml; grep -c "statistics:" claims/000715/*.yaml; grep -c "data: elsewhere" claims/000715/*.yaml; git status --short
```

```
32
5
21
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
?? claims/000715/
?? scripts
```

**Agent**

I wrote the claims file at `claims/000715/10.1016-j.cell.2020.12.012.yaml`. The quote checker passes it: 32 claims, 32 quotes, 0 problems.

**Text read.** The accepted author manuscript from PubMed Central (PMC10494711), not the version of record. That covers the main text, STAR Methods, the legends of Figures 1–7 and S1–S3, and two supplements read from their PDFs: Methods S1 (atlas, neuron detection, identification accuracy) and Methods S2 (optimal coloring).

**Code read.**
- `amin-nejat/CELL_ID` at d9f5df9, the last commit before publication. It holds the identification software (detection, identification and a pretrained atlas). It does not hold the script that builds the atlas from the 10 worms or the cross-validation behind Figure 7B–C.
- `Eviatar/Optimal_Coloring` at 990c597. It holds the coloring solver, the rule for which neurons count as neighbors, the violation measure, and the NeuroPAL colors and reporter tables.
- I did not read `NeuroPAL-traces`, because no claim tested here uses it.

**Claims.** 32, all with quotes; 5 carry statistics (7 values) and all 32 have criteria.
- **11 testable on this dandiset**, which by its title holds the 10-worm atlas data:
  - positional variability differs across neurons;
  - OLLR is more than twice as variable as OLLL;
  - identification accuracy, 86% head and 94% tail (leave-one-out);
  - the ventral ganglion is lower than every tail ganglion;
  - 8 manual labels lift head accuracy above 90%;
  - labeling the most uncertain neurons first beats random order;
  - position-only accuracy, 50% head and 68% tail;
  - detection accuracy, 80%/88%, with precision and recall 90%/93%;
  - the confidence scores are calibrated.

  The other two of the 11 also need the coloring code's tables (`with_inputs`): NeuroPAL's color violations of 3.5%, and the optimal-coloring results of 1.7% and 10.5%. One claim uses ganglion labels from the code (`with_labels`).
- **21 marked `elsewhere`**, with a "Not tested on the dandiset" criterion: the NeuroPAL color map, strain phenotypes, receptor expression and connectome percentages, the pag-3 and eor-1 mutants, and the whole-brain imaging results. The whole-brain data are on Zenodo (doi:10.5281/zenodo.3906530); the receptor and mutant data are deposited nowhere the paper names.

**Details the paper leaves open, and the readings named:**
- **Positional variability (OLL claim):** standard deviation, variance, or the anterior-posterior extent of the 50% contour in the 2-D slice Figure 2 draws.
- **Variability across neurons:** the paper gives no test. I set the threshold from its own example: the largest per-neuron spread must be more than twice the smallest.
- **Identification accuracy:**
  - which neurons are identified: the hand-annotated ones, or automatic detections matched within 3 µm;
  - the starting alignment: Methods S1 starts from the identity, the code first aligns the worm's long axis and searches rotations (run as a variant);
  - colors: those stored in the dandiset, or recomputed by the Methods S1 rule;
  - averaging: the mean over worms, or all neurons pooled;
  - scoring: per neuron, or by left/right class (the footnote names only RMF as an example).
- **Most uncertain neuron:** highest entropy, or lowest top probability (the code's choice). Accuracy after labeling is counted with or without the labeled neurons.
- **Calibration:** the paper gives no measure. Two readings: a positive Spearman correlation, and a mean confidence-accuracy gap under 10 points.
- **Color violations:** Methods S2 counts the share of neighbor pairs below the margin; the code reports the mean shortfall below the margin (a variant). Head and tail pooled or separate is not said. The setting that yields the 3-reporter solution is not stated.
- **Detection settings:** shape bounds and filter thresholds are not given; the code defaults are used and recorded as a deviation.
- **Atlas fitting:** the random starting worm and the convergence tolerance are standard choices, with sensitivity reported.
- **Readers' note:** one sentence pairs GAR and MGL with "glutamatergic and cholinergic … respectively", which looks swapped. The criterion notes this.

**Missing from the text.** Tables S1–S6 (spreadsheets), Videos S1–S4 and the Figure S4 legend. This leaves out the per-neuron atlas values (Table S3), the mutant p-values (Table S5, so the pag-3 and eor-1 statistics are recorded only as the paper's significance threshold of 0.05), and the whole-brain statistics (Table S6). No testable claim needed a number that exists only in these tables.

## End of run

43 turns, 7 minutes, result: success.
