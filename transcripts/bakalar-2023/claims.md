# 001362 · claims · run 39669213338

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/001362/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md | sed -n '60,400p'
```

```
finding.
   - `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md | sed -n '30,60p'; cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -120 claims/001453/*.yaml; echo ----; grep -n "^  - id" claims/001453/*.yaml | head; wc -l claims/001453/*.yaml
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
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; head -c 60000 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; fold -s -w 200 10.1111-jne.13286.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; sed -n '1,200p' $TMPDIR/p.txt
```

```
<persisted-output>
Output too large (37.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/37990a4f-de17-4cec-ab68-20486237c808/tool-results/b9qhnu75j.txt

Preview (first 2KB):
828 /tmp/claude-1001/p.txt
DOI: 10.1111/jne.13286
Version: as served by ncbi_pmc
Source: ncbi_pmc+crossref (paper-text-fetcher)
Stored: 2026-10-20
Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC10620107), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
------------------------------------------------------------------------
pmc J Neuroendocrinol J Neuroendocrinol 319 nihpa 8913461 Journal of neuroendocrinology 0953-8194 1365-2826 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC10620107 
PMC10620107.319 10620107 10620107 NIHMS1900413 37309259 10.1111/jne.13286 NIHMS1900413 NIHPA1900413 319 Article Constitutive and conditional PACAP deletion reveals distinct phenotypes driven by 
developmental versus neurotransmitter actions of PACAP Bakalar Dana 1 Gavrilova Oksana 2 Jiang Sunny Z. 1 Zhang Hai-ying 1 Roy Snehashis 3 Williams Sarah K. 3 Liu Naili 2 Wisser Stephen 3 Usdin Ted 
B. 3 Eiden Lee E. 1 1. Section on Molecular Neuroscience, National Institute of Mental Heath - Intramural Research Program, Bethesda, MD, USA 2. Mouse Metabolism Core Laboratory, National Institute 
of Diabetes and Kidney Disease-Intramural Research Program, Bethesda, MD, USA 3. Systems Neuroscience Imaging Resource, National Institute of Mental Heath - Intramural Research Program, Bethesda, MD, 
USA 11 2023 12 6 2023 35 11 448345 e13286 e13286 06 06 2023 01 11 2024 01 11 2024 17 02 2024 01 11 2024 This file is available for text mining. It may also be used consistent with the principles of 
fair use under the copyright law. Neuropeptides may exert trophic effects during development, and then neurotransmitter roles in the developed nervous system. On
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 300
}
```

```
1	DOI: 10.1111/jne.13286
2	Version: as served by ncbi_pmc
3	Source: ncbi_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC10620107), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	pmc J Neuroendocrinol J Neuroendocrinol 319 nihpa 8913461 Journal of neuroendocrinology 0953-8194 1365-2826 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC10620107 
8	PMC10620107.319 10620107 10620107 NIHMS1900413 37309259 10.1111/jne.13286 NIHMS1900413 NIHPA1900413 319 Article Constitutive and conditional PACAP deletion reveals distinct phenotypes driven by 
9	developmental versus neurotransmitter actions of PACAP Bakalar Dana 1 Gavrilova Oksana 2 Jiang Sunny Z. 1 Zhang Hai-ying 1 Roy Snehashis 3 Williams Sarah K. 3 Liu Naili 2 Wisser Stephen 3 Usdin Ted 
10	B. 3 Eiden Lee E. 1 1. Section on Molecular Neuroscience, National Institute of Mental Heath - Intramural Research Program, Bethesda, MD, USA 2. Mouse Metabolism Core Laboratory, National Institute 
11	of Diabetes and Kidney Disease-Intramural Research Program, Bethesda, MD, USA 3. Systems Neuroscience Imaging Resource, National Institute of Mental Heath - Intramural Research Program, Bethesda, MD, 
12	USA 11 2023 12 6 2023 35 11 448345 e13286 e13286 06 06 2023 01 11 2024 01 11 2024 17 02 2024 01 11 2024 This file is available for text mining. It may also be used consistent with the principles of 
13	fair use under the copyright law. Neuropeptides may exert trophic effects during development, and then neurotransmitter roles in the developed nervous system. One way to associate peptide-deficiency 
14	phenotypes with either role is first to assess potential phenotypes in so-called constitutive knockout mice, and then proceed to specify, regionally and temporally, where and when neuropeptide 
15	expr
[... 285 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -o -E "Figure [0-9]+ [A-Z].{0,40}|Table [0-9] .{0,30}|SUPP|Supplement.{0,40}|===.{0,60}" /tmp/claude-1001/p.txt | sed -n '1,200p' | awk -F: '$1>300'
```

```
383:Table 2 as inputs. Data were standardi
409:Table 3 ). Plot represents individual 
412:Table 4 . Points represent data from P
418:Supplemental Figure 2 for 
710:Supplement: NIHMS1900413-supplement-SUPP_METHODS.d
711:SUPP
798:Supplemental Figure 1). The SPVI was also excluded
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 370,
 "limit": 460
}
```

```
370	10.1523/JNEUROSCI.0784-11.2011 PMC3864636 98. Aponte Y , Atasoy D , Sternson SM . AGRP neurons are sufficient to orchestrate feeding behavior rapidly and without training . Nature neuroscience . 2011 
371	; 14 ( 3 ): 351 – 5 . 21209617 10.1038/nn.2739 PMC3049940 99. Adamantidis AR , Zhang F , Aravanis AM , Deisseroth K , De Lecea L . Neural substrates of awakening probed with optogenetic control of 
372	hypocretin neurons . Nature . 2007 ; 450 ( 7168 ): 420 – 4 . 17943086 10.1038/nature06310 PMC6744371 100. Ernstsen C , Christensen SL , Rasmussen RH , Nielsen BS , Jansen-Olesen I , Olesen J , 
373	Kristensen DM . The PACAP pathway is independent of CGRP in mouse models of migraine: possible new drug target? Brain . 2022 . 10.1093/brain/awac040 35136961 101. Jiang SZ , Eiden LE . PACAPergic 
374	Synaptic Signaling and Circuitry Mediating Mammalian Responses to Psychogenic and Systemic Stressors . In: Tamas DRaA , ed. Pituitary Adenylate Cyclase-Activating Polypeptide-PACAP . Switzerland : 
375	Springer International 2016 . 102. Missig G , Roman CW , Vizzard MA , Braas KM , Hammack SE , May V . Parabrachial nucleus (PBn) pituitary adenylate cyclase activating polypeptide (PACAP) signaling 
376	in the amygdala: implication for the sensory and behavioral effects of pain . Neuropharmacology . 2014 ; 86 38 – 48 . 24998751 10.1016/j.neuropharm.2014.06.022 PMC4322675 103. Hokfelt T , Zhang X , 
377	Wiesenfeld-Hallin Z . Messenger plasticity in primary sensory neurons following axotomy and its functional implications . Trends Neurosci . 1994 ; 17 ( 1 ): 22 – 30 . 7511846 
378	10.1016/0166-2236(94)90031-0 104. Stroth N , Kuri BA , Mustafa T , Chan SA , Smith CB , Eiden LE . PACAP controls adrenomedullary catecholamine secretion and expression of catecholamine biosynthetic 
379	enzymes at high splanchnic nerve firing rates characteristic of stress transduction in male mice . Endocrinology . 2013 ; 154 ( 1 ): 330 – 9 . 23221599 10.1210/en.2012-1829 PMC3529367 Figure 1: 
380
[... 450 more lines not kept]
```

**Agent calls Bash**

```bash
cd ..; grep -rl "001362" --include=*.yaml --include=*.md --include=*.json --include=*.csv . 2>/dev/null | grep -v transcripts | head; ls; ls tools
```

```
./targets/dandisets.json
./papers/manifest.yaml
LICENSE
README.md
attempts
bunfig.toml
claims
docs
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
questions
schemas
scripts
targets
tests
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '001362' in json.dumps(x): print(json.dumps(x,indent=1)[:3000])
"; grep -n -B2 -A10 "001362" papers/manifest.yaml
```

```
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
    "doi": "10.1016/j.neuron.2016.12.011",
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d:
  if x['dandiset']=='001362': print(json.dumps(x,indent=1))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if x['dandiset']=='001362': print(json.dumps(x,indent=1))
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else '')
s=json.dumps(d); i=s.find('\"001362\"'); print(s[i-50:i+1500])
"; curl -s -m 20 https://api.dandiarchive.org/api/dandisets/001362/ | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 20 https://api.dandiarchive.org/api/dandisets/001362/versions/0.260923.2152/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('description'));print(d.get('keywords'));print(json.dumps(d.get('assetsSummary'),indent=0)[:800])"
```

Result: the fetched text is not kept.

**Agent**

Full text, legends, Methods and the Supplemental Methods are all present. The dataset holds the whole-brain c-Fos light-sheet data (Fig 5, Table 4). Next I'm reading the linked CATNIP code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/snehashis-roy/CATNIP && cd CATNIP && git log -1 --format='%H %cd' && ls -la && cat README* | head -150
```

```
4fb92da2226ae6fd6b4e5172ea4a58c282bf8e53 Wed Oct 2 13:04:41 2024 -0400
total 23148
drwxr-xr-x 10 runner runner     1000 Oct 21 20:21 .
drwx------  6 runner runner      140 Oct 21 20:21 ..
drwxr-xr-x  7 runner runner      240 Oct 21 20:21 .git
-rwxr-xr-x  1 runner runner     4445 Oct 21 20:21 AntsExample.sh
-rwxr-xr-x  1 runner runner   180054 Oct 21 20:21 ApplyFRST
-rwxr-xr-x  1 runner runner     1744 Oct 21 20:21 ApplyFRST.sh
-rwxr-xr-x  1 runner runner   129458 Oct 21 20:21 ApplyFRSTseg
-rwxr-xr-x  1 runner runner     1782 Oct 21 20:21 ApplyFRSTseg.sh
-rwxr-xr-x  1 runner runner    38083 Oct 21 20:21 CATNIP.sh
-rw-r--r--  1 runner runner 21204919 Oct 21 20:21 CATNIP_Documentation.pdf
-rwxr-xr-x  1 runner runner   164813 Oct 21 20:21 Downsample3D
-rwxr-xr-x  1 runner runner     1876 Oct 21 20:21 Downsample3D.sh
-rwxr-xr-x  1 runner runner   131087 Oct 21 20:21 FlipImages
-rwxr-xr-x  1 runner runner     1190 Oct 21 20:21 FlipImages.sh
-rwxr-xr-x  1 runner runner   149423 Oct 21 20:21 Generate_Stats
-rwxr-xr-x  1 runner runner     2148 Oct 21 20:21 Generate_Stats.sh
-rw-r--r--  1 runner runner    35149 Oct 21 20:21 LICENSE
-rwxr-xr-x  1 runner runner   134776 Oct 21 20:21 N4Process
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CATNIP && sed -n '150,260p' README.md; grep -n -i "csv\|Generate_Stats\|volume\|density\|stats" CATNIP.sh | head -40; ls atlas_v*; cat Generate_Stats.sh | tail -15
```

````
./CATNIP.sh --cfos [removed: a home directory path]/example_data/ --o [removed: a home directory path]/output/ --ob no --lrflip yes --udflip yes \
--thr 1000:1000:5000 --dsfactor 6x6x5 --cellradii 2,3,4 --ncpu 16 --atlasversion v2 \
--exclude_mask example_data_artifact_mask.tif --mask_ovl_ratio 0.33
```

For details of each of the arguments, please refer to the [documentation](CATNIP_documentation.pdf) section 6.
These default parameters are primarily applicable to 3.7x3.7x5um images. For images with different pixel sizes, the parameters
may need to be changed, e.g., see Fig 4 of the [documentation](CATNIP_documentation.pdf).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[... 128 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/CATNIP && for v in 1 2 3 4 5 6; do echo v$v $(wc -l < atlas_v$v/atlas_info.txt); done; head -5 atlas_v2/atlas_info.txt; grep -n -i "SPVI\|DG-sg\|STN\|^.*fiber" atlas_v2/atlas_info.txt | head; grep -n -A12 "Generating stats" CATNIP.sh | head -30; grep -n -i "density\|volume" CATNIP.sh | head
```

```
v1 562
v2 562
v3 562
v4 1123
v5 1123
v6 1123
id,name,acronym,red,green,blue,structure_order,parent_id,parent_acronym
1,Tuberomammillary_nucleus_ventral_part,TMv,255,78,86,75500,557,TM
2,Primary_somatosensory_area_mouth_layer_6b,SSp-m6b,137,205,161,6200,345,SSp-m
4,Inferior_colliculus,IC,255,152,255,79100,339,MBsen
6,internal_capsule,int,204,204,204,107000,784,cst
183:364,Parasubthalamic_nucleus,PSTN,255,79,80,77700,290,LZ
210:437,Spinal_nucleus_of_the_trigeminal_interpolar_part,SPVI,255,176,184,91400,386,MY-sen
227:470,Subthalamic_nucleus,STN,255,79,85,77900,290,LZ
298:632,Dentate_gyrus_granule_cell_layer,DG-sg,64,200,64,39600,726,DG
489:1009,fiber_tracts,fiber_tracts,204,204,204,97200,997,root
619:echo "============== Generating stats on the cell counts =================" 2>&1 | tee -a $LOG 
620-${INSTALL_PREFIX}/Generate_Stats.sh $OUTPUTDIR/FRST_seg/ ${INSTALL_PREFIX}/atlas_${ATLASVERSION}/atlas_info.txt   $OUTPUTDIR/atlaslabel_def_brain.nii $DSFACTOR $OUTPUTDIR/atlaslabel_def_origspace_masked/  $CELLRADII $OUTPUTDIR/FRST_seg/FRSTseg*/  2>&1 | tee -a  $LOG
621-
622-
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CATNIP && (pdftotext CATNIP_Documentation.pdf d.txt 2>&1 || python3 -c "import fitz" ) ; ls d.txt 2>/dev/null && grep -n -i -B2 -A6 "csv\|volume\|densit" d.txt | head -80
```

```
Exit code 2
/bin/bash: line 1: pdftotext: command not found
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd $TMPDIR/CATNIP && python3 -c "import pypdf" 2>&1; python3 -c "import PyPDF2" 2>&1; strings -n 8 CATNIP_Documentation.pdf | grep -i "csv\|volume" | head
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import PyPDF2
ModuleNotFoundError: No module named 'PyPDF2'
7a_=zCSv
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/CATNIP/CATNIP_Documentation.pdf",
 "pages": "1-3"
}
```

```
pdftoppm is not installed. Install poppler-utils (e.g. `brew install poppler` or `apt-get install poppler-utils`) to enable PDF page rendering.
```

**Agent calls Bash**

```bash
cd $TMPDIR/CATNIP && sed -n '60,200p' CATNIP.sh | grep -v "^\s*$" | head -110; sed -n '640,700p' CATNIP.sh
```

```
DSFACTOR        : (Required) Downsampling factor for registration in HxWxD orientation. 
                      Default is 6x6x5. Use bigger downsampling factor (e.g. 9x9x7) 
                      for larger size images.
                      ** This is a crucial parameter for good registration. Choose
                      downsampling factor so that the downsampled image size is 
                      similar to 528x320x277 (HxWxD) and resolution is approximately
                      25x25x25um, i.e. the size and resolution of the ABA atlas.
                      After resampling, the atlas should approximately be
                      isotropic in resolution. This can be modified based on actual 
                      brain size.
    RADII           : (Required) A range of cell radii in *pixels*, comma separated. 
                      For 3.77x3.77x5um images, the default is 2,3,4. Please estimate 
                      the range of cell radii from the image and enter as a comma
                      separated string.
    Optional arguments:
    NUMCPU          : (Optional) Number of parallel processing cores to be used.
                      This must be less/equal to the total available number of 
                      cpus. Usually 8 or 12 is fine. Maximum required memory is
                      also proportional to the number of processes. Default 8.
    THRESHOLD       : (Optional) FRST segmentation thresholds. FRST output is a 
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; sed -n '120,321p' claims/001453/*.yaml | grep -n -A12 "statistics:" | head -60; grep -n "open\|deviation" claims/001453/*.yaml | head
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
7:  statistics:
8-  - test: two-way ANOVA, Tukey post hoc
9-    p: 0.05
10-    p_relation: "<"
11-    n: 26 ZF and 12 DC fish
12-  criterion: Per stimulus, ZF against DC fish-by-stimulus median speeds with Tukey's HSD on the
13-    two groups, at the Bonferroni level 0.05/9, as in Fig1-S1.ipynb. "Oblique" can be read as
14-    (a) the intercardinal directions forward right, forward left, backward right and backward
15-    left, or (b) the motion of 90 degrees or more used for turning in the Results (right,
16-    left, backward right, backward left). Reproduced when, under one reading, at least two of
17-    its four stimuli show DC significantly faster than ZF.
18-  data: with_labels
19-  depends_on:
--
27:  statistics:
28-  - test: two-way ANOVA, Tukey post hoc
29-    p: 0.05
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; sed -n '1,40p' tools/claims_check.py
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
[... 223 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000])"
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
[... 82 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001362/10.1111-jne.13286.yaml",
 "content": "# Claims for Bakalar, Gavrilova, Jiang, Zhang, Roy, Williams, Liu, Wisser, Usdin & Eiden (2023),\n# J Neuroendocrinol 35(11) e13286, on dandiset 001362.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol as stated in docs/protocol.md (pilot-10), Reader steps 1 to 4.\n#\n# Text read: the NIH author manuscript in PubMed Central (PMC10620107, NIHMS1900413), as served\n# by ncbi_pmc: main text, Methods, figure legends 1 to 13 and Tables 1 to 5, and the one\n# supplement file, the Supplemental Methods (NIHMS1900413-supplement-SUPP_METHODS.docx), which\n# gives the whole-brain c-Fos pipeline and its statistics. Supplemental Figures 1 and 2 are\n# images (cerebellar staining; DAPI in the IHC regions) and were not read; no claim rests on\n# them. No PDF was supplied.\n#\n# Code read: the paper links one repository, CATNIP (https://github.com/snehashis-roy/CATNIP,\n# commit 4fb92da2226ae6fd6b4e5172ea4a58c282bf8e53, 2024-10-02). It holds compiled MATLAB\n# binaries with shell wrappers (CATNIP.sh and one script per step), six atlas versions\n# (v1 to v3 are single-hemisphere sagittal atlases with 561 labels, matching the 561 regions\n# of the Supplemental Methods) and a PDF manual that could not be read here (no PDF renderer).\n# CATNIP.sh settles that FRST segmentation and cell counts are produced at a list of\n# thresholds (--thr), that an optional exclusion mask removes the counts of labels it\n# overlaps, and that counts per label are written per threshold. It does not hold the Python\n# statistics (density, IQR outliers, Mann-Whitney U, BKY correction); that code is not linked.\n#\n# Data the paper used, as it reports them.\n# - Whole-brain c-Fos (Figure 5, Table 4; the subject of this dandiset): constitutive\n#   PACAPko mice and control PACAP fl/fl mice placed in the CleverSys homecage before lights\n#   out and perfused 2 to 3 h after lights out (Figure 1 legend: 1.5 to 2.5 h). Brains cleared\n#   by a modified iDISCO, stained for c-Fos, imaged on a LaVision UltraMicroscope II one\n#   hemisphere at a time, sagittal, 5 um z steps, 3.7 um pixels; Richardson-Lucy deconvolved,\n#   N4 corrected, registered to a customized Allen atlas of 561 regions and segmented by FRST\n#   (CATNIP). Unit of analysis: the hemisphere. N = 8 hemispheres from 6 PACAP fl/fl animals\n#   and 11 hemispheres from 6 PACAPko animals. Measure: c-Fos-positive cells per region\n#   divided by region size (plotted as cells per cubic mm), in 431 regions. The dandiset's\n#   description names Richardson-Lucy deconvolved, N4 corrected stacks and CATNIP derivatives;\n#   its archive summary lists 13 subjects, the paper 12 animals.\n# - Homecage Scan behaviour (Figures 2, 3, 4, 8, 10a, 11): time in each behaviour (distance\n#   for travel) over the 12 dark hours; constitutive PACAPko and controls, tamoxifen-induced\n#   CAG-Cre/Esr1::PACAP fl/fl (adult and postnatal day 1 to 3 inductions), Baf53b-Cre::PACAP\n#   fl/fl, PACAPko from heterozygous dams, wheel-raised PACAPko.\n# - c-Fos IHC sections (Figure 6): N = 4 wild-type C57BL/6N and 8 PACAPko mice.\n# - qRT-PCR of Adcyap1, Xaf1 and Pttg1 in hypothalamus, hippocampus and cerebellum (Figure 7).\n# - RNAscope Fos and Adcyap1 in PVN after restraint (Figure 9); HCR ISH in DG and STN (Figure\n#   10c); weight loss 24 h after 3 h restraint (Figure 10b).\n# - Telemetry of core body temperature and activity, 12-h averages over fed, 24-h fasted and\n#   refed periods (Figures 12, 13): PACAPko against WT, Sim1-Cre::PACAP fl/fl against Cre-\n#   littermates, PAC1ko against WT littermates.\n# Only the whole-brain c-Fos claims (fig5-dg-fos, table4-lenient-regions,\n# table4-region-values) concern the data the dandiset says it holds; the other claims are\n# recorded to cover the paper's main findings.\n#\n# Details the paper leaves open for the c-Fos claims, with the readings named in the\n# criteria: the FRST threshold used (chosen by an expert by eye, value not given); the region\n# size divided by (the region's volume in that hemisphere's registered label image, or the\n# atlas region volume); whether the 1.5 IQR outlier rule is applied within each genotype or\n# to both pooled; which hemispheres were left out (6 animals gave 8 and 11 hemispheres); how\n# \"PACAPko as % of PACAPfl/fl\" is formed (ratio of group means or of group medians); the\n# alpha passed to the BKY correction (not stated; the statsmodels default is 0.05).\n#\n# Inconsistencies noticed in the paper: the Figure 2 legend says the PCA inputs are listed in\n# Table 2, which holds TaqMan probes (Table 3 lists the behaviours); the Figure 5 legend points\n# to Table 3 for the lenient-cutoff regions, which are in Table 4; the Table 4 title says\n# regions with raw p <= 0.05 are shown, but every row has raw p <= 0.01; Methods 2.7 names\n# PACAP fl/fl controls for c-Fos, while the Figure 6 IHC legend names wild-type C57BL/6N\n# controls; Figure 12 prints F(1, 36) = 11.12 with p < 0.0001, while that F on those degrees\n# of freedom gives p near 0.002.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001362\"\npaper: doi:10.1111/jne.13286\nclaims:\n- id: fig2a-pca-components\n  statement: A principal component analysis of the homecage behaviours of PACAPko and control\n    mice gives three components, explaining 45.95%, 14.55% and 13.56% of the variance (80.05%\n    together).\n  source: Results 3.1, Jumping and repetitive jumping, paragraph 1; Figure 2A legend\n  quote: PC1 accounts for 45.95% of the variance, PC2 for 14.55%, and PC3 for 13.56%, for a\n    cumulative 80.05% of variability accounted for by these components.\n  expected:\n  - quantity: variance explained by PC1\n    value: 45.95\n    tolerance: 4.6\n    unit: percent\n  - quantity: variance explained by PC2\n    value: 14.55\n    tolerance: 1.46\n    unit: percent\n  - quantity: variance explained by PC3\n    value: 13.56\n    tolerance: 1.36\n    unit: percent\n  - quantity: cumulative variance of PC1 to PC3\n    value: 80.05\n    tolerance: 8.0\n    unit: percent\n  criterion: From the Figure 2 legend and Methods (Behavioral analysis). Inputs are the 16\n    behaviours of Table 3 (the legend says Table 2, which holds the TaqMan probes), as time\n    spent (distance for travel) over the 12 dark hours, for 38 PACAPko and 18 control mice\n    pooled; each behaviour standardized to mean 0 and SD 1; the number of components chosen by\n    parallel analysis. Open, could change the outcome - whether the components were rotated.\n    The loadings of Table 3 (all positive, each behaviour high on one component) suggest a\n    rotation, but none is named. Readings are (a) unrotated components, (b) varimax-rotated\n    components. Reproduced when, under one reading, parallel analysis keeps three components\n    and the variance values are within tolerance.\n- id: table3-pca-loadings\n  statement: PC1 loads most on locomotion (travel distance, 0.934) and hanging from the cage\n    top (0.89), PC2 on jumping (0.845) and repetitive jumping (0.779), PC3 on remaining low\n    (0.78) and grooming (0.72).\n  source: Results 3.1, Jumping and repetitive jumping, paragraph 1; Table 3\n  quote: PC1 is most heavily loaded towards locomotion (0.934) and climbing the cage top (0.89).\n    PC2 is most heavily loaded towards jumping (0.845) and repetitive jumping (0.779). PC3 is\n    most loaded towards remaining low in the cage (0.78) and grooming (0.72).\n  depends_on:\n  - fig2a-pca-components\n  expected:\n  - quantity: PC1 loading of travel distance\n    value: 0.934\n    tolerance: 0.093\n  - quantity: PC1 loading of remain hanging with all four paws from cage top\n    value: 0.89\n    tolerance: 0.089\n  - quantity: PC2 loading of jumping\n    value: 0.845\n    tolerance: 0.085\n  - quantity: PC2 loading of repetitive jumping\n    value: 0.779\n    tolerance: 0.078\n  - quantity: PC3 loading of remain low\n    value: 0.78\n    tolerance: 0.078\n  - quantity: PC3 loading of grooming\n    value: 0.72\n    tolerance: 0.072\n  criterion: Same PCA and the same two readings (unrotated, varimax) as fig2a-pca-components.\n    Table 3 gives 0.88 for \"Remain Hanging with all four paws from cage top\" where the text\n    gives 0.89 for climbing the cage top; the Table 3 behaviour is the one meant (the text\n    and legend call it hanging from the cage top in Figure 2B). Reproduced when, under one\n    reading, each of the six behaviours loads highest on its stated component and each\n    absolute loading is within tolerance.\n- id: fig2a-two-trajectories\n  statement: Control mice cluster at low PC1 and PC2 scores, while PACAPko mice spread along\n    two trajectories, high PC1 with lower PC2, or high PC2 with PC1 only slightly above\n    control.\n  source: Figure 2A\n  quote: While control mice appear tightly clustered at low levels of PC1 and PC2 behaviors,\n    PACAPko mice range widely, in two trajectories, towards high PC1 behaviors with lower PC2\n    behaviors, or high PC2 behaviors with PC1 behaviors only slightly above control levels\n  depends_on:\n  - fig2a-pca-components\n  criterion: The paper reports no test. Scores on PC1 and PC2 from the PCA of\n    fig2a-pca-components, under each of its readings. Reproduced when the spread (SD) of\n    PACAPko scores exceeds that of controls on both components, and among PACAPko mice above\n    the control range on either component, some lie above it on PC1 only and some on PC2\n    only. The scatter is shown.\n- id: fig2b-pc-index-behaviours\n  statement: PACAPko mice spend more time than controls in the top two PC1 behaviours (travel\n    distance, cage-top hanging) and PC2 behaviours (jumping, repetitive jumping), with no\n    difference in the PC3 behaviours (remaining low, grooming).\n  source: Results 3.1, Jumping and repetitive jumping, paragraph 1; Figure 2B\n  quote: We found significantly higher levels of PC1 and PC2 index behaviors in PACAPko mice\n    than controls, but no differences in PC3 index behaviors ( Figure 2b ).\n  statistics:\n  - about: travel distance\n    test: Mann-Whitney U\n    statistic: U = 28\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Holm-Šídák\n    n: 38 PACAPko and 18 control mice\n  - about: cage hanging\n    test: Mann-Whitney U\n    statistic: U = 79\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Holm-Šídák\n    n: 38 PACAPko and 18 control mice\n  - about: jumping\n    test: Mann-Whitney U\n    statistic: U = 26\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Holm-Šídák\n    n: 38 PACAPko and 18 control mice\n  - about: repetitive jumping\n    test: Mann-Whitney U\n    statistic: U = 33\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Holm-Šídák\n    n: 38 PACAPko and 18 control mice\n  - about: remaining low\n    test: Mann-Whitney U\n    statistic: U = 220\n    p: 0.063\n    corrected: Holm-Šídák\n    n: 38 PACAPko and 18 control mice\n  - about: grooming\n    test: Mann-Whitney U\n    statistic: U = 277\n    p: 0.261\n    corrected: Holm-Šídák\n    n: 38 PACAPko and 18 control mice\n  expected:\n  - quantity: U, travel distance\n    value: 28\n    tolerance: 2.8\n  - quantity: U, cage hanging\n    value: 79\n    tolerance: 7.9\n  - quantity: U, jumping\n    value: 26\n    tolerance: 2.6\n  - quantity: U, repetitive jumping\n    value: 33\n    tolerance: 3.3\n  - quantity: U, remaining low\n    value: 220\n    tolerance: 22\n  - quantity: U, grooming\n    value: 277\n    tolerance: 28\n  criterion: From the Figure 2B legend. For each of the six behaviours, a Mann-Whitney U test\n    of PACAPko against control mice, the six p-values adjusted by Holm-Šídák. The reported U\n    values are the smaller U (U = 28 of a possible 684). Reproduced when the four PC1 and PC2\n    behaviours are higher in PACAPko with adjusted p < 0.001 (the paper's bound), and the two\n    PC3 behaviours have adjusted p >= 0.05 (a claim of absence, on the paper's test), with the\n    U values within tolerance. Partially reproduced when the directions and significance hold\n    but U values fall outside tolerance.\n- id: fig3a-travel-development\n  statement: Travel distance of PACAPko mice does not differ from controls at weaning (p21) but\n    is higher from p29 to the end of testing at p57.\n  source: Results 3.1, Development of the constitutive PACAP knockout hyperlocomotor phenotype;\n    Figure 3A\n  quote: Šídák's multiple comparisons test showed that at postnatal day 21 (p21), travel\n    distance did not differ across genotypes (p = 0.068), but by p29 PACAPko mice (blue)\n    traveled significantly more than controls (orange), p = 0.001. The groups remained\n    different through the end of testing at p57.\n  statistics:\n  - about: main effect of developmental day\n    test: mixed-effects analysis\n    statistic: F (1.914, 18.37) = 15.97\n    p: 0.001\n    p_relation: \"<\"\n  - about: main effect of genotype\n    test: mixed-effects analysis\n    statistic: F (1, 12) = 76.79\n    p: 0.001\n    p_relation: \"<\"\n  - about: day by genotype interaction\n    test: mixed-effects analysis\n    statistic: F (5, 48) = 5.98\n    p: 0.0001\n    p_relation: \"<\"\n  - about: genotypes at p21\n    test: Šídák's multiple comparisons test\n    p: 0.068\n  - about: genotypes at p29\n    test: Šídák's multiple comparisons test\n    p: 0.001\n  criterion: From the Figure 3A legend. Travel distance per mouse and test day (p21 to p57),\n    a mixed-effects model of day, genotype and their interaction (Geisser-Greenhouse\n    corrected, as the fractional degrees of freedom show), with Šídák's comparisons of the\n    genotypes at each day. Reproduced when the genotype effect and interaction have p < 0.05,\n    the p21 comparison has p >= 0.05, and every comparison from p29 to p57 has p < 0.05 with\n    PACAPko higher.\n- id: fig3b-jumping-development\n  statement: Jumping of PACAPko mice does not differ from controls at p21 and p28 but is higher\n    at p36, p42, p50 and p57.\n  source: Figure 3B\n  quote: we found that on postnatal days 21 (t(4.98) = 0.473, adjusted p = 0.656) and 28\n    (t(10.45) = 2.347, adjusted p = 0.078) the genotypes did not differ, but on subsequent\n    days the groups differed significantly\n  statistics:\n  - about: p21\n    test: Welch's t-test\n    statistic: t(4.98) = 0.473\n    p: 0.656\n    corrected: Holm-Šídák\n  - about: p28\n    test: Welch's t-test\n    statistic: t(10.45) = 2.347\n    p: 0.078\n    corrected: Holm-Šídák\n  - about: p36\n    test: Welch's t-test\n    statistic: t(6.019) = 4.198\n    p: 0.033\n    corrected: Holm-Šídák\n  - about: p42\n    test: Welch's t-test\n    statistic: t(6.025) = 3.974\n    p: 0.036\n    corrected: Holm-Šídák\n  - about: p50\n    test: Welch's t-test\n    statistic: t(6.050) = 3.559\n    p: 0.040\n    corrected: Holm-Šídák\n  - about: p57\n    test: Welch's t-test\n    statistic: t(6.144) = 3.661\n    p: 0.040\n    corrected: Holm-Šídák\n  criterion: From the Figure 3B legend. Jumping time per mouse and day; a Welch's t-test of\n    the genotypes at each of the six days, adjusted by Holm-Šídák across the six. Reproduced\n    when p21 and p28 have adjusted p >= 0.05 and p36 to p57 have adjusted p < 0.05 with\n    PACAPko higher. The text says jumping \"emerged early, at postnatal day 28\"; the legend's\n    test at p28 is not significant, and the legend is followed.\n- id: fig4-wheel-repetitive-jumping\n  statement: PACAPko mice raised with running wheels for 4 weeks after weaning show less\n    repetitive jumping than littermates without wheels, with no change in single jumps,\n    travel distance or cage-top hanging.\n  source: Results 3.1, Development, paragraph 2; Figure 4\n  quote: We found significant amelioration of repetitive jumping after wheel access, but no\n    alterations in single jumps, travel distance, or cage top hanging ( Figure 4 ).\n  statistics:\n  - about: main effect of wheel access\n    test: two-way ANOVA\n    statistic: F (1 ,41) = 0.652\n    p: 0.424\n  - about: main effect of behavior\n    test: two-way ANOVA\n    statistic: F (3, 41) = 0.562\n    p: 0.643\n  - about: wheel access by behavior interaction\n    test: two-way ANOVA\n    statistic: F (3,41) = 3.075\n    p: 0.0381\n  - about: repetitive jumping, wheel against no wheel\n    test: Šídák's multiple comparisons\n    p: 0.0313\n    n: 6 wheel-raised and 7 control PACAPko mice\n  criterion: From the Figure 4 legend. The four behaviours (jumping, repetitive jumping,\n    travel distance, cage-top hanging) as values per mouse, a two-way ANOVA of wheel access by\n    behaviour, and Šídák's comparisons of wheel against no wheel within each behaviour.\n    Reproduced when the interaction has p < 0.05, repetitive jumping is lower with wheels at\n    p < 0.05, and the other three behaviours have p >= 0.05 (absence, on the paper's test).\n- id: fig5-dg-fos\n  statement: In whole-brain c-Fos counts after the early dark phase, PACAPko hemispheres have\n    a higher density of c-Fos-positive cells than PACAP fl/fl in the dentate gyrus granule\n    cell layer and polymorph layer, the only two regions significant after correction for\n    multiple testing; PACAPko densities are 224% and 326% of control.\n  source: Results 3.1, Association of the constitutive PACAP knockout hyperlocomotor phenotype\n    with Fos induction, paragraph 1; Figure 5; Table 4\n  quote: Cell counting and analysis revealed two regions where PACAPko mice had significantly\n    higher c-Fos-positive cell density than controls after p-values were adjusted for multiple\n    testing. These regions are the hippocampal dentate gyrus granule cell layer (DG-sg) and the\n    dentate gyrus polymorph layer (DG-po).\n  statistics:\n  - about: DG-sg\n    test: Mann-Whitney U\n    statistic: U = 88\n    p: 0.011\n    corrected: Benjamini, Krieger and Yekutieli two-stage step-up\n    n: 11 PACAPko hemispheres (6 mice) and 8 PACAP fl/fl hemispheres (6 mice)\n  - about: DG-po\n    test: Mann-Whitney U\n    statistic: U = 85\n    p: 0.039\n    corrected: Benjamini, Krieger and Yekutieli two-stage step-up\n    n: 11 PACAPko hemispheres (6 mice) and 8 PACAP fl/fl hemispheres (6 mice)\n  expected:\n  - quantity: DG-sg raw p\n    value: 2.65e-05\n    tolerance: 2.65e-06\n  - quantity: DG-po raw p\n    value: 1.85e-04\n    tolerance: 1.85e-05\n  - quantity: DG-sg Mann-Whitney U\n    value: 88\n    tolerance: 8.8\n  - quantity: DG-po Mann-Whitney U\n    value: 85\n    tolerance: 8.5\n  - quantity: DG-sg PACAPko density as percent of PACAP fl/fl\n    value: 224.23\n    tolerance: 22.4\n    unit: percent\n  - quantity: DG-po PACAPko density as percent of PACAP fl/fl\n    value: 325.82\n    tolerance: 32.6\n    unit: percent\n  criterion: Method from the Supplemental Methods (Statistical analysis) and the Figure 5\n    legend. Unit is the hemisphere, PACAPko against PACAP fl/fl. CATNIP cell counts per region\n    of the 561-region atlas; white matter tracts, nerves and ventricles, the cerebellum, SPVI\n    and all layer 1 regions excluded, leaving 431 regions; counts of regions overlapping an\n    artifact mask ignored; each count divided by the region's size (cells per cubic mm);\n    outliers removed per region by the 1.5 IQR rule; scipy.stats.mannwhitneyu per region;\n    statsmodels multipletests method \"fdr_tsbky\" over the 431 regions. The test is two-sided\n    and exact, as Table 4 implies (raw p 2.65E-05 for U = 88 at 11 and 8 hemispheres is\n    2/C(19,8), the exact two-sided value for complete separation); U is that of the PACAPko\n    sample (88 = 11 x 8 is its maximum). Open details, each named reading run - (1) the FRST\n    threshold, chosen by an expert by eye and not given; readings are the threshold the\n    dataset's derivatives mark as used, or, if none is marked, every threshold the\n    derivatives hold. (2) Region size; readings are (a) the region's volume in that\n    hemisphere's registered label image, (b) the atlas region volume. (3) The IQR rule;\n    readings are (a) within each genotype, (b) both genotypes pooled. (4) Which hemispheres;\n    the paper used 8 and 11 hemispheres from 6 and 6 mice without saying which were left out\n    or why; readings are (a) the hemispheres the dataset marks as used, if it does, (b) every\n    hemisphere of the two genotypes in the dataset. (5) The percentage; readings are the ratio\n    of group means and the ratio of group medians, after outlier removal. (6) The alpha of\n    the BKY procedure, not stated; the statsmodels default 0.05 is used and the result at\n    0.1 shown. Reproduced when, under the readings, DG-sg and DG-po both have PACAPko higher\n    with BKY-adjusted p < 0.05; reported values within tolerance are reported and do not\n    decide the outcome alone. Partially reproduced when one of the two holds. If the readings\n    of (1) to (4) give different outcomes, the claim is blocked as methods_underspecified with\n    every result shown.\n- id: table4-lenient-regions\n  statement: At an uncorrected cutoff of raw p <= 0.01, 13 further regions differ in c-Fos\n    cell density between PACAPko and PACAP fl/fl, including substantia nigra reticular part,\n    subthalamic nucleus and intergeniculate leaflet.\n  source: Results 3.1, Association of the constitutive PACAP knockout hyperlocomotor phenotype\n    with Fos induction, paragraph 1; Table 4; Figure 5\n  quote: A less stringent cutoff of raw p-value <= 0.01 revealed 13 more regions ( Table 4 ;\n    Figure 5 ) with differential cell counts. These included the Substantia Nigra reticulata\n    (SNr), Subthalamic Nucleus (STN), and Intergeniculate Leaflet (IGL), among other regions.\n  depends_on:\n  - fig5-dg-fos\n  expected:\n  - quantity: number of regions besides DG-sg and DG-po with raw p <= 0.01\n    value: 13\n    tolerance: 1.3\n  criterion: Same pipeline, tests and readings as fig5-dg-fos. Table 4 lists the 15 regions\n    with raw p <= 0.01 (its title says p <= 0.05, but every row is <= 0.01) - DG-sg, DG-po,\n    LGv, IGL, SNr, AUDp2/3, DTN, IO, AUDpo2/3, LGd, PST, LRN, STN, PGRNl and NB. Reproduced\n    when SNr, STN and IGL, the three the text names, have raw p <= 0.01 with PACAPko higher,\n    and the number of other regions with raw p <= 0.01 is within tolerance. Partially\n    reproduced when one or two of SNr, STN and IGL meet the cutoff. The overlap of the regions\n    found with the 15 of Table 4 is reported.\n- id: table4-region-values\n  statement: Table 4 gives, for each of the 15 regions with raw p <= 0.01, the Mann-Whitney U\n    and PACAPko density as a percentage of PACAP fl/fl; every region but DTN (45%) is higher\n    in PACAPko (167% to 326%).\n  source: Table 4\n  inferred: Numbers from Table 4; no sentence of the text states them region by region.\n  depends_on:\n  - fig5-dg-fos\n  expected:\n  - quantity: LGv U\n    value: 73\n    tolerance: 7.3\n  - quantity: LGv percent\n    value: 170.42\n    tolerance: 17.0\n    unit: percent\n  - quantity: IGL U\n    value: 72\n    tolerance: 7.2\n  - quantity: IGL percent\n    value: 258.62\n    tolerance: 25.9\n    unit: percent\n  - quantity: SNr U\n    value: 80\n    tolerance: 8.0\n  - quantity: SNr percent\n    value: 275.91\n    tolerance: 27.6\n    unit: percent\n  - quantity: AUDp2/3 U\n    value: 73\n    tolerance: 7.3\n  - quantity: AUDp2/3 percent\n    value: 261.06\n    tolerance: 26.1\n    unit: percent\n  - quantity: DTN U\n    value: 9\n    tolerance: 0.9\n  - quantity: DTN percent\n    value: 45.21\n    tolerance: 4.5\n    unit: percent\n  - quantity: IO U\n    value: 76\n    tolerance: 7.6\n  - quantity: IO percent\n    value: 297.49\n    tolerance: 29.7\n    unit: percent\n  - quantity: AUDpo2/3 U\n    value: 76\n    tolerance: 7.6\n  - quantity: AUDpo2/3 percent\n    value: 198.26\n    tolerance: 19.8\n    unit: percent\n  - quantity: LGd U\n    value: 76\n    tolerance: 7.6\n  - quantity: LGd percent\n    value: 276.46\n    tolerance: 27.6\n    unit: percent\n  - quantity: PST U\n    value: 68\n    tolerance: 6.8\n  - quantity: PST percent\n    value: 208.73\n    tolerance: 20.9\n    unit: percent\n  - quantity: LRN U\n    value: 76\n    tolerance: 7.6\n  - quantity: LRN percent\n    value: 293.57\n    tolerance: 29.4\n    unit: percent\n  - quantity: STN U\n    value: 70\n    tolerance: 7.0\n  - quantity: STN percent\n    value: 196.47\n    tolerance: 19.6\n    unit: percent\n  - quantity: PGRNl U\n    value: 75\n    tolerance: 7.5\n  - quantity: PGRNl percent\n    value: 239.16\n    tolerance: 23.9\n    unit: percent\n  - quantity: NB U\n    value: 75\n    tolerance: 7.5\n  - quantity: NB percent\n    value: 167.26\n    tolerance: 16.7\n    unit: percent\n  criterion: Same pipeline, tests and readings as fig5-dg-fos; U is that of the PACAPko sample.\n    The Figure 5 legend gives the sample per region - 8 PACAP fl/fl and 11 PACAPko hemispheres,\n    except LGv (one PACAP fl/fl outlier removed) and AUDp2/3 and STN (one PACAPko outlier\n    removed). Reproduced when, under one reading, the direction (PACAPko above or below 100%)\n    matches for all 13 regions and at least 10 of the 13 have both U and percentage within\n    tolerance; partially reproduced when the direction matches for all and fewer are within\n    tolerance; not reproduced when any direction differs. The threshold of 10 of 13 is this\n    reader's, as the paper states no criterion for a table; every value is shown.\n- id: fig6-ihc-fos-confirmation\n  statement: c-Fos IHC on sections confirms higher c-Fos-positive cell densities in PACAPko\n    than wild-type mice in DG-sg, DG-po, STN and SNr, but not in IGL.\n  source: Results 3.1, Association, paragraph 2; Figure 6A\n  quote: We confirmed that PACAPko mice had significantly higher c-Fos positive cell counts\n    during CleverSys testing in STN, SNr, DG-po, and DG-sg, but increased c-Fos in IGL was not\n    confirmed ( Figure 6 ).\n  statistics:\n  - about: DG-sg\n    test: unpaired t-test\n    statistic: t (10) = 5.500\n    p: 0.001\n    corrected: Holm-Šídák\n  - about: DG-po\n    test: unpaired t-test\n    statistic: t (10) = 4.371\n    p: 0.006\n    corrected: Holm-Šídák\n  - about: STN\n    test: unpaired t-test\n    statistic: t (9) = 4.147\n    p: 0.007\n    corrected: Holm-Šídák\n  - about: SNr\n    test: unpaired t-test\n    statistic: t (9) = 3.137\n    p: 0.024\n    corrected: Holm-Šídák\n  - about: IGL\n    test: unpaired t-test\n    statistic: t (9) = 0.390\n    p: 0.705\n    corrected: Holm-Šídák\n    n: 4 wild-type C57BL/6N and 8 PACAPko mice\n  criterion: From Methods 2.8 and the Figure 6 legend. Cells per square mm per region and\n    animal from sum-projected 3-image z-stacks, counted with Find Maxima, at least 4 images per\n    region and animal; unpaired t-tests (Student, as the integer degrees of freedom show) per\n    region, Holm-Šídák across the five. How an animal's images are combined is not stated;\n    readings are the mean density over images and total cells over total area. Reproduced\n    when DG-sg, DG-po, STN and SNr are higher in PACAPko at adjusted p < 0.05 and IGL has\n    adjusted p >= 0.05 (absence, on the paper's test).\n- id: fig7a-adult-induction-adcyap1\n  statement: Tamoxifen in adulthood depletes Adcyap1 transcript in hypothalamus, hippocampus\n    and cerebellum of CAG-Cre/Esr1::PACAP fl/fl mice.\n  source: Results 3.2, Adult and early postnatal KO, paragraph 2; Figure 7A\n  quote: In both adult- and early postnatally-induced Cre-positive mice, Adcyap1 levels were\n    significantly reduced in hypothalamus, hippocampus, and cerebellum\n  statistics:\n  - about: hypothalamus\n    test: unpaired t-test\n    statistic: t (4.062) = 6.119\n    p: 0.007\n    corrected: Holm-Šídák\n  - about: hippocampus\n    test: unpaired t-test\n    statistic: t (4.147) = 3.033\n    p: 0.037\n    corrected: Holm-Šídák\n  - about: cerebellum\n    test: unpaired t-test\n    statistic: t (3.089) = 13.44\n    p: 0.002\n    corrected: Holm-Šídák\n  criterion: From the Figure 7 legend and Methods 2.4. Relative Adcyap1 by 2^-ddCt against\n    Gapdh, triplicate wells per sample; unpaired t-tests per region (Welch, as the fractional\n    degrees of freedom show), Holm-Šídák across the three regions. The reference for ddCt\n    (the Cre-negative group mean) is the standard choice and does not change the test.\n    Reproduced when all three regions are lower in Cre-positive mice at adjusted p < 0.05.\n- id: fig7b-postnatal-induction-adcyap1\n  statement: Tamoxifen on postnatal days 1 to 3 depletes Adcyap1 transcript in hypothalamus,\n    hippocampus and cerebellum of adult CAG-Cre/Esr1::PACAP fl/fl mice.\n  source: Results 3.2, Adult and early postnatal KO, paragraph 2; Figure 7B\n  quote: In postnatally-induced animals, multiple unpaired t-tests with Holm-Šídák correction\n    for multiple tests show significant Adcyap1 depletion following tamoxifen\n  statistics:\n  - about: hypothalamus\n    test: unpaired t-test\n    statistic: t (3.102) = 9.483\n    p: 0.006\n    corrected: Holm-Šídák\n  - about: hippocampus\n    test: unpaired t-test\n    statistic: t (3.489) = 4.447\n    p: 0.030\n    corrected: Holm-Šídák\n  - about: cerebellum\n    test: unpaired t-test\n    statistic: t (2.180) = 4.399\n    p: 0.041\n    corrected: Holm-Šídák\n  criterion: As fig7a-adult-induction-adcyap1, for the postnatally induced mice. Reproduced\n    when all three regions are lower in Cre-positive mice at adjusted p < 0.05.\n- id: fig7-cprg-expression\n  statement: Adult induction does not change the cPRG Xaf1 and slightly increases Pttg1 in\n    cerebellum; postnatal induction changes neither Pttg1 nor Xaf1 in any region.\n  source: Results 3.2, Adult and early postnatal KO, paragraph 2; Figure 7A, 7B\n  quote: Adult-induced PACAP depletion did not alter expression of the cPRG Xaf1 , upregulated\n    in constitutive PACAPko mice. Pttg1, downregulated in constitutive PACAPko mice ( 14 ), was\n    slightly increased in cerebellum ( Figure 7a ). In mice induced on postnatal days 1, 2 and\n    3, no alterations in Pttg1 or Xaf1 transcription were seen in any region ( Figure 7b ).\n  criterion: The paper reports no test for Xaf1 or Pttg1. The test of the Adcyap1 panels of\n    the same figure is used - per gene and induction age, Welch unpaired t-tests per region\n    with Holm-Šídák across the three regions, 2^-ddCt against Gapdh. Whether the cerebellar\n    Pttg1 increase was significant is not said; readings are (a) higher in Cre-positive at\n    adjusted p < 0.05, (b) higher at unadjusted p < 0.05. Reproduced when Xaf1 (adult) and\n    Pttg1 and Xaf1 (postnatal) have adjusted p >= 0.05 in every region, and adult cerebellar\n    Pttg1 is higher under one reading; partially reproduced when only the absences hold.\n- id: fig8-induced-ko-no-hyperlocomotion\n  statement: PACAP knockout induced in adulthood or on postnatal days 1 to 3 does not change\n    jumping, repetitive jumping, locomotion or cage-top hanging.\n  source: Results 3.2, Adult and early postnatal KO, paragraph 2; Figure 8\n  quote: PACAP knockout induced either in adulthood or in early postnatal life did not induce\n    hyperlocomotion.\n  statistics:\n  - about: adult induction, genotype\n    test: two-way ANOVA\n    statistic: F (1, 64) = 0.671\n    p: 0.416\n    n: 9 Cre-positive and 9 Cre-negative mice\n  - about: adult induction, genotype by behavior\n    test: two-way ANOVA\n    statistic: F (3, 64) = 0.497\n    p: 0.686\n  - about: postnatal induction, genotype\n    test: two-way ANOVA\n    statistic: F (1, 64) = 0.761\n    p: 0.386\n    n: 7 Cre-positive and 11 Cre-negative mice\n  - about: postnatal induction, genotype by behavior\n    test: two-way ANOVA\n    statistic: F (3, 64) = 1.449\n    p: 0.237\n  criterion: A claim of absence, on the paper's test (Figure 8 legend). For each induction\n    age, the four behaviours per mouse, a two-way ANOVA of genotype by behaviour, with Šídák's\n    comparisons of genotype within each behaviour. Reproduced when, at both ages, the genotype\n    effect and the interaction have p >= 0.05; not reproduced when either has p < 0.05. Effect\n    sizes and the Šídák p-values are shown.\n- id: fig9-postnatal-ko-pvn-fos\n  statement: After 3 h restraint, a postnatally induced CAG-Cre/Esr1::PACAP fl/fl mouse shows\n    very little Adcyap1 or Fos mRNA in the PVN, where its Cre-negative littermate shows\n    abundant signal of both.\n  source: Results 3.2, Early postnatal KO of PACAP abrogates c-Fos induction; Figure 9\n  quote: In Cre positive animals, there was very little of either Adcyap1 or Fos signal (\n    Figure 9 ).\n  criterion: The paper shows one mouse per genotype and reports no quantification or test.\n    Measure open; readings are (a) the number of Fos-positive and of Adcyap1-positive cells in\n    the PVN, (b) mean RNAscope signal in the PVN. Reproduced when, under both readings, Fos and\n    Adcyap1 in the PVN are lower in the Cre-positive mouse than in its Cre-negative\n    littermate.\n- id: fig10a-baf53b-no-hyperlocomotion\n  statement: Baf53b-Cre::PACAP fl/fl mice do not differ from PACAP fl/fl mice in jumping,\n    repetitive jumping, travel distance or cage-top hanging.\n  source: Results 3.2, Abrogation of Adcyap1 transcription in new-born neurons; Figure 10A\n  quote: Baf53b-Cre:: PACAP fl/fl mice did not differ from PACAP fl/fl animals in jumping,\n    repetitive jumping, travel distance, or hanging from cage top ( Figure 10a ).\n  statistics:\n  - about: genotype\n    test: two-way ANOVA\n    statistic: F (1, 68) = 2.386\n    p: 0.127\n    n: 10 Baf53b-Cre::PACAP fl/fl and 10 PACAP fl/fl mice\n  - about: genotype by behavior\n    test: two-way ANOVA\n    statistic: F (3, 68) = 1.563\n    p: 0.206\n  criterion: A claim of absence, on the paper's test (Figure 10A legend). A two-way ANOVA of\n    genotype by behaviour over the four behaviours, with Šídák's comparisons. Reproduced when\n    the genotype effect and the interaction have p >= 0.05; not reproduced when either has\n    p < 0.05. Effect sizes are shown.\n- id: fig10b-baf53b-restraint-weight-loss\n  statement: Baf53b-Cre::PACAP fl/fl mice lose a smaller percentage of body weight than\n    Cre-negative controls 24 h after a 3-h restraint.\n  source: Results 3.2, Baf53-Cre-driven KO of PACAP in post-mitotic neurons abrogates weight\n    loss; Figure 10B\n  quote: Like constitutive PACAPko mice, Baf53b-Cre::PACAP fl/fl mice lost a significantly\n    smaller percentage of weight than controls 24 hours after a 3-hour restraint stress\n  statistics:\n  - test: unpaired t-test\n    statistic: t (11) = 2.269\n    p: 0.0444\n    n: 5 Baf53b-Cre::PACAP fl/fl and 8 Cre-negative mice\n  criterion: From Methods 2.5 and the Figure 10B legend. Percent weight loss from the weight\n    on the day of restraint to the weight 24 h after its start; an unpaired Student t-test (11\n    degrees of freedom). Reproduced when Cre-positive mice lose less weight at p < 0.05.\n- id: fig10c-baf53b-ish-knockdown\n  statement: In Baf53b-Cre::PACAP fl/fl mice, Adcyap1 transcripts are greatly diminished in\n    glutamatergic neurons of the dentate gyrus (Slc17a7) and subthalamic nucleus (Slc17a6).\n  source: Results 3.2, Baf53-Cre-driven KO, paragraph 1; Figure 10C\n  quote: In-situ hybridization confirms the knockdown, showing greatly diminished Adcyap1 in\n    neurons, identified by the expression of Slc17a7 , encoding Vglut1 or Slc17a6 , encoding\n    Vglut2 ( Figure 10c )\n  criterion: The paper shows images and reports no quantification. Measure open; readings are\n    (a) the fraction of Slc17a7- or Slc17a6-positive cells that are Adcyap1-positive, (b) mean\n    Adcyap1 signal within those cells, in the DG polymorph layer and STN. Reproduced when,\n    under both readings, Adcyap1 is lower in Cre-positive than Cre-negative mice in both\n    regions.\n- id: fig11-placental-pacap-no-effect\n  statement: PACAPko mice from heterozygous dams (exposed to maternal placental PACAP) do not\n    differ from PACAPko mice from homozygous PACAPko dams in jumping, travel distance,\n    repetitive jumping or cage-top hanging.\n  source: Results 3.2, Adcyap1 expression in maternal placenta; Figure 11\n  quote: we find no difference in hyperlocomotion in PACAPko mice bred from heterozygous dams\n    versus those from homozygous PACAPko dams ( Figure 11 )\n  statistics:\n  - about: jumping\n    test: Mann-Whitney U\n    statistic: U = 9\n    p: 0.486\n    corrected: Holm-Šídák\n    n: 4 PACAPko from heterozygous dams and 8 from homozygous dams\n  - about: travel distance\n    test: Mann-Whitney U\n    statistic: U = 6\n    p: 0.370\n    corrected: Holm-Šídák\n  - about: repetitive jumping\n    test: Mann-Whitney U\n    statistic: U = 7\n    p: 0.394\n    corrected: Holm-Šídák\n  - about: cage-top hanging\n    test: Mann-Whitney U\n    statistic: U = 14\n    p: 0.808\n    corrected: Holm-Šídák\n  criterion: A claim of absence, on the paper's test (Figure 11 legend). Per behaviour, a\n    Mann-Whitney U test of the two groups, Holm-Šídák across the four. Reproduced when all four\n    have adjusted p >= 0.05; not reproduced when any has p < 0.05. U values are shown.\n- id: fig12b-pacapko-fasting-hypothermia\n  statement: Fasting lowers light-phase body temperature in both WT and PACAPko mice, and it\n    returns on refeeding to the fed level.\n  source: Results 3.3, paragraph 1; Figure 12B\n  quote: Removal of food causes significantly decreased Tb in both wild-type and PACAPko mice,\n    indicating that this aspect of thermoregulation is intact\n  statistics:\n  - about: main effect of time (feeding status)\n    test: two-way ANOVA\n    statistic: F(1.305,46.97) = 157.3\n    p: 0.0001\n    p_relation: \"<\"\n    n: 20 WT and 17 PACAPko mice\n  - about: fed against fasting and fasting against refed, each genotype\n    test: Tukey post hoc\n    p: 0.0001\n    p_relation: \"<\"\n  - about: fed against refed, WT\n    test: Tukey post hoc\n    p: 0.407\n  - about: fed against refed, PACAPko\n    test: Tukey post hoc\n    p: 0.998\n  criterion: From Methods 2.1 (Body temperature telemetry) and the Figure 12B legend. Mean Tb\n    over each 12-h light period (fed, fasting, refed) per mouse; a two-way repeated-measures\n    ANOVA of feeding status by genotype (Geisser-Greenhouse corrected, as the fractional\n    degrees of freedom show), Tukey comparisons of feeding status within genotype. Which\n    baseline light period is \"fed\" is open (5 baseline days were recorded, three light\n    periods are plotted); readings are (a) the last light period before food removal, (b) the\n    mean of the baseline light periods. Reproduced when, under one reading, fasting Tb is\n    below fed and refed in both genotypes at p < 0.05, and fed against refed has p >= 0.05 in\n    both.\n- id: fig12b-pacapko-higher-tb\n  statement: PACAPko mice have a higher body temperature than WT, averaging 36.21 against 35.63\n    degrees C across light cycles.\n  source: Results 3.3, paragraph 1; Figure 12B\n  quote: We also see a significant main effect of genotype (F (1, 36) = 11.12, p < 0.0001), with\n    PACAPko mice averaging 36.21°C across light cycles and WT mice averaging 35.63°C.\n  statistics:\n  - about: main effect of genotype\n    test: two-way ANOVA\n    statistic: F (1, 36) = 11.12\n    p: 0.0001\n    p_relation: \"<\"\n    n: 20 WT and 17 PACAPko mice\n  depends_on:\n  - fig12b-pacapko-fasting-hypothermia\n  expected:\n  - quantity: PACAPko minus WT mean light-cycle Tb\n    value: 0.58\n    tolerance: 0.058\n    unit: degrees C\n  - quantity: PACAPko mean light-cycle Tb\n    value: 36.21\n    tolerance: 0.29\n    unit: degrees C\n  - quantity: WT mean light-cycle Tb\n    value: 35.63\n    tolerance: 0.29\n    unit: degrees C\n  criterion: Same ANOVA and readings as fig12b-pacapko-fasting-hypothermia; the averages are\n    over the three light periods. Tolerances - 10% of the difference; for each mean, half\n    the difference (0.29), since 10% of a body temperature would admit any physiological\n    value. The printed p (< 0.0001) does not match F(1, 36) = 11.12 (p near 0.002); the\n    genotype effect is judged at p < 0.05. Reproduced when the genotype effect has p < 0.05\n    with PACAPko higher and the difference is within tolerance; partially reproduced when the\n    effect holds and the difference is outside tolerance.\n- id: fig12d-pacapko-more-active\n  statement: PACAPko mice are more active than WT mice in most 12-h periods.\n  source: Results 3.3, paragraph 1; Figure 12D\n  quote: PACAPko mice are significantly more active than WT mice in most of the time periods.\n  criterion: From the Figure 12D legend. Mean telemetry activity per 12-h period (three light\n    and three dark, fed, fasting and refed) per mouse; unpaired t-tests per period with\n    Holm-Šídák across the six. \"Most\" is read as more than half, so at least 4 of 6 periods.\n    The fed baseline periods take the readings of fig12b-pacapko-fasting-hypothermia.\n    Reproduced when PACAPko is higher at adjusted p < 0.05 in at least 4 of the 6 periods.\n- id: fig13a-sim1-tb-unchanged\n  statement: In Sim1-Cre::PACAP fl/fl mice, body temperature does not differ from WT, and the\n    fasting-induced Tb decrease and its recovery on refeeding are intact.\n  source: Results 3.3, paragraph 2; Figure 13A\n  quote: Restriction of the PACAP knockout to hypothalamus abrogates the effect of PACAP loss on\n    locomotion and on body temperature, while normal Tb decrease after fasting remains intact (\n    Figure 13a , b ).\n  statistics:\n  - about: main effect of time (feeding status)\n    test: two-way ANOVA\n    statistic: F(2,30) = 112.0\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 WT (4 males, 5 females) and 10 Sim1-Cre::PACAP fl/fl mice (5 males, 5 females)\n  - about: fed against fasting and fasting against refed, each genotype\n    test: Tukey post hoc\n    p: 0.0001\n    p_relation: \"<\"\n  - about: fed against refed, WT\n    test: Tukey post hoc\n    p: 0.628\n  - about: fed against refed, Sim1-Cre::PACAP fl/fl\n    test: Tukey post hoc\n    p: 0.658\n  criterion: As fig12b-pacapko-fasting-hypothermia, with its readings, for Sim1-Cre::PACAP\n    fl/fl against Cre-negative littermates, sexes pooled as the legend's single ANOVA implies.\n    The genotype effect and interaction are a claim of absence, on the paper's test.\n    Reproduced when the genotype effect and interaction have p >= 0.05, fasting Tb is below fed\n    and refed in both genotypes at p < 0.05, and fed against refed has p >= 0.05 in both.\n- id: fig13b-sim1-activity-unchanged\n  statement: Activity of Sim1-Cre::PACAP fl/fl mice does not differ from WT in any period.\n  source: Figure 13B\n  quote: Activity of Sim1-Cre::PACAP fl/fl mice does not differ from activity of WT mice in any\n    period (multiple unpaired t-tests with Holm-Šídák correction).\n  criterion: A claim of absence, on the paper's test. Mean activity per 12-h period per mouse,\n    unpaired t-tests per period, Holm-Šídák across the six; fed baseline periods with the\n    readings of fig12b-pacapko-fasting-hypothermia. Reproduced when no period has adjusted\n    p < 0.05.\n- id: fig13c-pac1ko-tb-unchanged\n  statement: In PAC1ko mice, body temperature does not differ from WT, and the fasting-induced\n    Tb decrease and its recovery on refeeding are intact.\n  source: Results 3.3, paragraph 2; Figure 13C\n  quote: Similarly, body temperature, activity, and fasting-induced thermoregulation did not\n    differ between PAC1ko and wild-type mice ( Figure 13c , d ).\n  statistics:\n  - about: main effect of time (feeding status)\n    test: two-way ANOVA\n    statistic: F(2,24) = 40.07\n    p: 0.0001\n    p_relation: \"<\"\n    n: 8 WT (3 males, 5 females) and 6 PAC1ko mice (4 males, 2 females)\n  - about: fed against fasting and fasting against refed, each genotype\n    test: Tukey post hoc\n    p: 0.0001\n    p_relation: \"<\"\n  - about: fed against refed, WT\n    test: Tukey post hoc\n    p: 0.877\n  - about: fed against refed, PAC1ko\n    test: Tukey post hoc\n    p: 0.984\n  criterion: As fig13a-sim1-tb-unchanged, for PAC1ko against WT littermates. Reproduced when\n    the genotype effect and interaction have p >= 0.05, fasting Tb is below fed and refed in\n    both genotypes at p < 0.05, and fed against refed has p >= 0.05 in both.\n- id: fig13d-pac1ko-activity\n  statement: Activity of PAC1ko mice does not differ from WT in any period except the initial\n    fed light cycle, when it is slightly lower.\n  source: Figure 13D\n  quote: activity of PAC1ko mice does not differ from activity of WT mice in any period except\n    during the initial fed light cycle (p = 0.026), when PAC1ko animals show slightly lower\n    levels of activity than WT mice.\n  statistics:\n  - about: initial fed light cycle\n    test: unpaired t-test\n    p: 0.026\n    corrected: Holm-Šídák\n  criterion: Mean activity per 12-h period per mouse, unpaired t-tests per period, Holm-Šídák\n    across the six; fed baseline periods with the readings of\n    fig12b-pacapko-fasting-hypothermia. Reproduced when the initial fed light period is lower\n    in PAC1ko at adjusted p < 0.05 and no other period has adjusted p < 0.05 (absence, on the\n    paper's test); partially reproduced when only the absences hold.\n"
}
```

```
File created successfully at: claims/001362/10.1111-jne.13286.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001362/10.1111-jne.13286.yaml paper/10.1111-jne.13286.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "[^ ]: .*: " claims/001362/10.1111-jne.13286.yaml | grep -v "^\s*#"; grep -n -E "^\s{4,}[^ -].*: " claims/001362/10.1111-jne.13286.yaml | grep -v "^[0-9]*:\s*#" | head
```

```
690:  quote: Baf53b-Cre:: PACAP fl/fl mice did not differ from PACAP fl/fl animals in jumping,
80:    value: 45.95
81:    tolerance: 4.6
82:    unit: percent
84:    value: 14.55
85:    tolerance: 1.46
86:    unit: percent
88:    value: 13.56
89:    tolerance: 1.36
90:    unit: percent
92:    value: 80.05
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001362/10.1111-jne.13286.yaml",
 "old_string": "  quote: Baf53b-Cre:: PACAP fl/fl mice did not differ from PACAP fl/fl animals in jumping,\n    repetitive jumping, travel distance, or hanging from cage top ( Figure 10a ).",
 "new_string": "  quote: \"Baf53b-Cre:: PACAP fl/fl mice did not differ from PACAP fl/fl animals in jumping,\n    repetitive jumping, travel distance, or hanging from cage top ( Figure 10a ).\""
}
```

```
The file claims/001362/10.1111-jne.13286.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001362/10.1111-jne.13286.yaml paper/10.1111-jne.13286.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/001362/10.1111-jne.13286.yaml; grep -n -i "—\|rather" $f; python3 -c "
import yaml;d=yaml.safe_load(open('$f'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
27 17 27 7
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
?? claims/001362/
?? scripts
```

**Agent**

I wrote `claims/001362/10.1111-jne.13286.yaml`, and the quote checker passes it: 27 claims, 26 quotes, 59 statistical values, 0 problems. Nothing the claims needed was missing from the paper, so the run was not stopped.

**Text read:** the NIH author manuscript in PubMed Central (PMC10620107). That covers the main text, Methods, figure legends 1 to 13 and Tables 1 to 5, plus the one supplement file, the Supplemental Methods, which describes the whole-brain c-Fos pipeline and its statistics. Supplemental Figures 1 and 2 are images only and no claim rests on them. No PDF was supplied.

**Code read:** the paper links one repository, CATNIP (github.com/snehashis-roy/CATNIP, commit 4fb92da). It holds compiled MATLAB binaries, shell wrappers and atlases; the 561-label hemisphere atlases match the 561 regions in the Supplemental Methods. It does not hold the Python statistics, and that code is not linked anywhere. I could not read its PDF manual because no PDF renderer is installed.

**Claims:**
- **Counts:** 27 claims. 26 have quotes; one (Table 4 values per region) is marked `inferred` because no sentence states those numbers. 17 have statistics, 27 have criteria and 7 have expected values.
- **What the dataset can test:** the dandiset holds the whole-brain c-Fos light-sheet data, so only three claims bear on it: `fig5-dg-fos`, `table4-lenient-regions` and `table4-region-values`.
- **Rest of the paper:** the other 24 claims cover its main findings: the behaviour PCA, development of the phenotype, wheel running, section c-Fos staining, the induced and neuron-specific knockouts, restraint stress, placental PACAP, and body temperature and activity.

**Details the paper leaves open, with the readings named**

For the c-Fos claims:
- **Segmentation threshold:** chosen by an expert by eye and not given. Readings: the threshold the dataset marks as used, otherwise every threshold the dataset holds.
- **Region size used for density:** the region's volume in each hemisphere's registered labels, or the atlas region volume.
- **Outlier rule (1.5 × IQR):** applied within each genotype, or with both genotypes pooled.
- **Hemispheres:** 6 + 6 mice gave 8 + 11 hemispheres, and the paper doesn't say which were dropped. Readings: the hemispheres the dataset marks, or all of them.
- **"PACAPko as % of control":** ratio of group means, or of group medians.
- **Alpha for the multiple-testing correction:** not stated. The statsmodels default of 0.05 is used, with 0.1 also shown.
- **Settled by Table 4:** the Mann-Whitney test is exact and two-sided (U = 88 at n = 11 and 8 gives p = 2.65E-05), and U is the PACAPko sample's.

Elsewhere:
- **PCA rotation:** none, or varimax.
- **How section images are combined per animal:** mean density over images, or total cells over total area.
- **Which baseline light period counts as "fed":** the last one before fasting, or the mean of the baseline periods.
- **Whether the cerebellar Pttg1 increase is significant:** judged on adjusted or on unadjusted p.
- **Measures for the image-only panels (Figs 9 and 10c):** cell counts, or mean signal.
- **"Most" periods (Fig 12d):** read as at least 4 of 6.
- **Cut-off for the Table 4 values:** at least 10 of 13 regions within tolerance. This is my own threshold, and the criterion says so.

**Inconsistencies in the paper, noted in the file**
- The Figure 2 legend points to Table 2 for the PCA inputs; it should be Table 3.
- The Figure 5 legend points to Table 3 for the regions; it should be Table 4.
- The Table 4 title says p ≤ 0.05, but every row is ≤ 0.01.
- The Methods name PACAP fl/fl controls, while the Figure 6 legend names wild-type C57BL/6N.
- Figure 12 prints F(1,36) = 11.12 with p < 0.0001, which should be about 0.002.
- The archive lists 13 subjects; the paper reports 12 c-Fos animals.

I committed nothing. The checkout also shows untracked files I didn't create (dotfiles, `.idea`, `scripts`); I left them alone.

## End of run

31 turns, 5 minutes, result: success.
