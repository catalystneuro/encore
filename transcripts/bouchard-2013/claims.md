# 000019 · claims · run 39691082607

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims/000019 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^### 3. Write the claims file/,/^## Author/p' docs/protocol.md
```

```
### 3. Write the claims file

Write `claims/<folder>/<doi with / replaced by ->.yaml`. Its opening comment
says which text was read (the version of record or a preprint version, and the
supplement), and describes the data the paper used: the subjects, sessions,
conditions and measured variables, as the paper reports them, so that the
author can find them in the dataset.

   - One claim per finding, at the level of a figure panel or a reported
     number when the full text is available. Cover the paper's main findings,
     including those the dataset cannot test.
   - `statement`: the finding in words. `source`: where the paper shows it,
     precise enough to find without searching: a figure panel, or a section
     and paragraph ("Results, Place fields, paragraph 3").
   - `quote`: the sentence at `source` that states the finding, copied word
     for word from the full text, cut with "..." where it runs long. It lets a
     reader check the statement against the paper without opening it. For a
     finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -250; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | sed -n '250,600p' | grep -n -E "^  [a-z_]+:|^[a-z_]+:|kind" | sort | uniq -c | sort -rn | head -30; tail -40 claims/001453/*.yaml
```

```
1 6:  statistics:
      1 68:  statistics:
      1 65:  quote: neurons in the registered medial hindbrain area, specifically located within the
      1 64:  source: Figure 4H and 4I
      1 61:  statement: Motor-associated neurons in the putative ventromedial spinal projection neurons of
      1 5:  quote: DC show a higher proportion of purely monocular neurons (ZF = 0.16, DC = 0.37
      1 55:  statistics:
      1 52:  quote: While the active, above baseline, ‘ON’ duration of neural activity for non-motor associated
      1 51:  source: Figure 4E and 4F
      1 4:  source: Figure 2K
      1 49:  statement: Swim-onset-associated neurons in DC have a longer active (ON) phase than in ZF,
      1 38:  statistics:
      1 35:  quote: In ZF, swims during forward last significantly longer than those during turn-inducing
      1 34:  source: Figure 3C and 3D
      1 32:  statement: Head-fixed ZF show larger directional tail angles than DC to turn-inducing stimuli,
      1 2:  statement: DC have a higher proportion of purely monocular neurons than ZF (0.37 against 0.16,
      1 26:  statistics:
      1 25:  quote: DC performed significantly longer swims than ZF (DC = 0.75 s, ZF = 0.29 s
      1 24:  source: Figure 3E and 3F
      1 22:  statement: Head-fixed DC perform longer swims than ZF (median 0.75 s against 0.29 s, p <
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/ | head; ls claims/001340; head -60 claims/001340/*.yaml; ls tools docs
```

```
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
10.1371-journal.pcbi.1013226.yaml
# Claims for Qü, Tai, Hall, Tu, Eckstein, Mishchanchuk, Lin, Chase, MacAskill, Collins, Gershman
# & Wilbrecht (2025), "Nucleus accumbens dopamine release reflects Bayesian inference during
# instrumental learning", PLoS Comput Biol 21(7) e1013226, on dandiset 001340.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read. The version of record as served by Europe PMC (PMC12233953, "vor-update-to-uncorrected-
# proof", publication update 2025-07-07), full text with Results, figure legends, Table 1, Materials
# and methods, and the Supporting information legends (S1 to S8 Fig) and the published peer review
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '60,200p' claims/001340/*.yaml
```

```
# reports 34 sessions with valid dopamine recordings, 30,707 trials in total, and 20,952 trials
# after cleaning. The dataset's title and description on DANDI were not read further than to
# know it is meant to hold these behaviour and photometry recordings (Data Availability).
#
# Definitions used by several criteria, all from the paper unless marked.
# - Correct choice. The choice of the port that is rewarded in the current block. A block switch
#   is the first trial of a new block. Stay and switch compare the choice at t with t-1; the
#   first trial of a session is neither (code, add_switch). Trials with no choice are dropped
#   from behavioural measures (Methods, Task behavior analysis).
# - Timing measures (Methods, Task behavior analysis). MVMT = CI(t) - SOf(t-1); center_dur =
#   CO - CI; port_dur = SO1 - O; SO_lat = SO1 - SO0.
# - Z(DA) (Methods, Fiber Photometry, Neural data analysis). Trends of both channels removed
#   with airPLS, a robust linear regression of 415 nm onto 470 nm subtracted from 470 nm, then
#   z-scored per session. The airPLS settings and the robust regression's loss are not given.
#   If the dataset holds processed dLight, it is used; otherwise these steps with standard
#   settings, recorded as a deviation. Aligned to outcome by interpolation and de-based by
#   subtracting its value at outcome time.
# - DA-PT (Results, Predictions from BRLfwr and BIfp, paragraph 4; Fig 4B legend). The maximum
#   of de-based Z(DA) in the 1 s after outcome on rewarded trials, the minimum on unrewarded
#   trials.
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/10.1038-nature11911.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c26a6670-70bf-419a-8390-3c70d360c513/tool-results/bttwswuz5.txt"
}
```

```
1	DOI: 10.1038/nature11911
2	Version: as served by ncbi_pmc
3	Source: ncbi_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC3606666), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	Nature Nature 319 nihpa 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC3606666 PMC3606666.1 3606666 3606666 NIHMS436351 23426266 10.1038/nature11911 NIHMS436351 NIHPA436351 1 Article Functional Organization of Human Sensorimotor Cortex for Speech Articulation Bouchard Kristofer E. 1 2 Mesgarani Nima 1 2 Johnson Keith 3 Chang Edward F. 1 2 4 1 Departments of Neurological Surgery and Physiology, University of California, San Francisco 2 Center for Integrative Neuroscience, University of California, San Francisco 3 Department of Linguistics, University of California, Berkeley 4 UCSF Epilepsy Center, University of California, San Francisco Correspondence and requests for materials should be addressed to E.F.C. ( [removed: an e-mail address] ) 20 2 2013 21 3 2013 495 7441 221018 327 332 24 01 2013 21 09 2013 21 09 2013 11 10 2026 Users may view, print, copy, download and text and data- mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use: http://www.nature.com/authors/editorial_policies/license.html#terms Speaking is one of the most complex actions we perform, yet nearly all of us learn to do it effortlessly. Production of fluent speech requires the precise, coordinated movement of multiple articulators (e.g., lips, jaw, tongue, larynx) over rapid time scales. Here, we used high-resolution, multi-electrode cortical recordings during the production of consonant-vowel syllables to determine the organization of speech sensorimotor cortex in humans. We found speech artic
[... 222 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c26a6670-70bf-419a-8390-3c70d360c513/tool-results/bttwswuz5.txt",
 "offset": 229,
 "limit": 540
}
```

```
229	(c-d) Spatial location of individual articulator representations is statistically similar across subjects. 
230	We examined the across-subject similarity of spatial location for individual articulator representations 
231	by taking the spatial cross-correlation of each articulators map across pair-wise subject comparisons 
232	(S1-S2, S2-S3, and S1-S3). 
233	If the representation of an individual articulator occupies a similar spatial location across subjects, we 
234	expect to see large correlations centered at [0,0] and that fall off with distance.  This analysis revealed 
235	that the representations of individual articulators were in similar locations across subjects, as evidence 
236	by the large values (red) very near the center of the heat map, corresponding to zero relative shift.  The 
237	similarity in spatial localization is summarized in (c) by averaging the individual with-in articulator, 
238	cross-subject cross-correlations functions, which exhibits a peak near [0,0].  Given the anisotropy 
239	described in (a), we expect a similar anisotropy to be seen here.  For comparison, an example of the 
240	average with-in articulator, cross-subject correlation function derived from a single random permutation 
241	of the spatial location of each subject’s electrodes is presented on the right (c, Random).  (d) We 
242	quantified the difference between the observed and random correlations by averaging the values with in 
243	a 3 mm radius for individual comparisons.  The correlation values for the data (0.195 ± 0.064, mean ± 
244	s.e., 3 subjects x 4 articulators, n = 12) were significantly greater than for the randomized data (0.031 ± 
245	0.021, mean ± s.d., P < 10-3, 1000 iteration permutation test).  Therefore, the representation of individual 
246	articulators is more consistently located across subjects than expected by chance. 
247	 
248	(e-f) Spatial sequence of articulator representations is statistically observed for each subject 
[... 516 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rl "000019" --include=*.{json,yaml,yml,md,csv,tsv} . 2>/dev/null | grep -v transcripts | head; ls questions 2>/dev/null | head -3
```

```
./targets/dandisets.json
./papers/manifest.yaml
000005.yaml
000008.yaml
000009.yaml
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if '000019' in json.dumps(x)[:200]: print(json.dumps(x,indent=1)[:3000])
" ; grep -n -B2 -A12 "000019" papers/manifest.yaml
```

```
93-    pdf: false
94-    supplements: 2
95:  000019:
96-  - doi: 10.1038/nature11911
97-    status: stored
98-    version: as served by ncbi_pmc
99-    source: ncbi_pmc+crossref (paper-text-fetcher)
100-    pdf: false
101-    supplements: 1
102-  '000023':
103-  - doi: 10.1101/2020.03.31.018820
104-    status: stored
105-    version: preprint, version 1
106-    source: bioRxiv JATS XML (api.biorxiv.org)
107-    pdf: false
```

**Agent calls Bash**

```bash
grep -n -A25 '"000019"' targets/dandisets.json | head -60
```

```
373:   "dandiset": "000019",
374-   "name": "Human ECoG speaking consonant-vowel syllables",
375-   "published_version": "0.220126.2148",
376-   "asset_count": 31,
377-   "size_gb": 55.59,
378-   "data_standards": [
379-    "Neurodata Without Borders (NWB)"
380-   ],
381-   "species": [
382-    "Human"
383-   ],
384-   "approaches": [
385-    "electrophysiological approach"
386-   ],
387-   "papers": [
388-    {
389-     "doi": "10.1038/nature11911",
390-     "title": "Functional organization of human sensorimotor cortex for speech articulation",
391-     "relation": "IsDescribedBy",
392-     "resource_type": "JournalArticle",
[... 6 more lines not kept]
```

**Agent**

Paper text is the PMC author manuscript with the supplement (legends and Supplementary Methods); no code is linked. Let me check the supplement PDF for the feature matrices the criteria will need.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature11911.supp.pdf",
 "pages": "2"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature11911.supp.pdf",
 "pages": "15"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature11911.supp.pdf",
 "pages": "8"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "import fitz;print(fitz.__doc__)" 2>&1; cd $TMPDIR && python3 -c "
import fitz
d=fitz.open('paper/10.1038-nature11911.supp.pdf')
for p in (1,7,14):
  d[p].get_pixmap(dpi=110).save(f'p{p+1}.png')
print('ok')"; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pip install --quiet --target $TMPDIR/py pymupdf 2>&1 | tail -2; cd $TMPDIR && PYTHONPATH=$TMPDIR/py python3 -c "
import fitz
d=fitz.open('paper/10.1038-nature11911.supp.pdf')
for p in (1,7,14):
  d[p].get_pixmap(dpi=110).save(f'p{p+1}.png')
print('ok')"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p2.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p8.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/py python3 -W ignore -c "
import pymupdf as f
d=f.open('paper/10.1038-nature11911.supp.pdf')
r=d[1].rect
clip=f.Rect(r.x0+90, r.y0+305, r.x1-50, r.y0+400)
d[1].get_pixmap(dpi=300,clip=clip).save('m.png')
" 2>&1 | grep -v onnx
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/m.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/py python3 -W ignore -c "
import pymupdf as f
d=f.open('paper/10.1038-nature11911.supp.pdf')
r=d[1].rect
d[1].get_pixmap(dpi=250,clip=f.Rect(r.x0+90, r.y0+278, r.x0+330, r.y0+352)).save('m1.png')
d[1].get_pixmap(dpi=250,clip=f.Rect(r.x0+320, r.y0+278, r.x1-60, r.y0+352)).save('m2.png')
" 2>&1 | grep -v onnx
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/m1.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/m2.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
grep -n -E "with_labels|with_inputs|elsewhere|kind:" docs/protocol.md docs/design.md | head -20; sed -n 1,80p tools/claims_check.py
```

```
docs/protocol.md:137:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:197:4. Decide what comes from outside the dataset. Data from elsewhere may be
docs/protocol.md:206:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:207:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:209:   - `with_labels` is for outside sources that only name or map codes the
docs/protocol.md:214:     or subjects, a claim of its own (`kind: link`) tests the link. Link
docs/protocol.md:231:   - `elsewhere` is for a claim whose data the dataset does not hold at
docs/protocol.md:240:   - The notes of a `with_inputs` claim say which side a difference comes
docs/protocol.md:251:     `data: elsewhere` instead (step 4).
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 195,255p docs/protocol.md; python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
     the missing names are recorded as a finding (`metadata_insufficient`).
   - When outside data has to be matched to the dataset's cells, sessions
     or subjects, a claim of its own (`kind: link`) tests the link. Link
[... 246 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000])"
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
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "content": "# Claims for Bouchard, Mesgarani, Johnson & Chang (2013), \"Functional organization of human\n# sensorimotor cortex for speech articulation\", Nature 495, 327-332, on dandiset 000019\n# (\"Human ECoG speaking consonant-vowel syllables\").\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read. The NIH author manuscript as served by PubMed Central (PMC3606666, NIHMS436351),\n# not the version of record: main text, figure legends and Methods, with the supplement\n# (NIHMS436351-supplement-1.pdf, Supplementary Figures 1 to 13 with their legends,\n# Supplementary Table 1 and Supplementary Methods), as extracted to text. No PDF of the main\n# text was supplied, so the main figures were read from their legends and from the Results\n# sentences that cite them. Supplement pages 2 and 8 were opened in the supplement PDF, to\n# see Supplementary Figure 1d and to confirm a printed p-value on page 8.\n#\n# Code. The paper links no code, and none is named in the Methods or the supplement. Every\n# method below is from the Methods, the legends or the Supplementary Methods.\n#\n# Data the paper describes. Three native English speakers (Supplementary Table 1 names them\n# EC2, EC33 and EC31) with a high-density subdural ECoG array over peri-Sylvian cortex, left\n# hemisphere in two (EC2, EC31) and right in one (EC33), implanted for epilepsy monitoring.\n# Each read aloud consonant-vowel syllables (CVs), 19 consonants (/b d f g h k l m n p r s sh t\n# th v w j z/) for two subjects and 18 for one, each followed by /a/, /i/ or /u/; each CV was\n# produced 15 to 100 times. 168 syllables in all (57 + 57 + 54). The microphone signal was\n# recorded with the ECoG at 3052 Hz (TDT system) and transcribed with WaveSurfer; every\n# analysis is aligned to the acoustic onset of the consonant-to-vowel transition (t = 0).\n# Measured variables. ECoG voltage per channel; electrode positions on each subject's MRI\n# reconstruction, expressed as dorsal-ventral distance from the Sylvian fissure and\n# anterior-posterior distance from the central sulcus (mm), and whether each electrode lies on\n# ventral sensorimotor cortex (vSMC, pre- and post-central gyri and the guenon); the audio; and\n# the CV label and the C-V transition time of each utterance. The dataset's title is enough to\n# know it is meant to hold these recordings; its files were not looked at.\n#\n# Definitions used by several criteria, from the Methods unless marked.\n# - High gamma (Hg). Channels with artifacts or excessive noise are excluded (by inspection;\n#   if the dataset marks bad channels, those marks are used). Common average reference over\n#   the remaining channels. Analytic amplitude from eight Gaussian band-pass filters with\n#   logarithmically spaced centres from 85 to 175 Hz and semi-logarithmically increasing\n#   bandwidths, by the Hilbert transform; averaged over the eight bands; down-sampled to\n#   200 Hz (5 ms steps); z-scored per channel against \"baseline data\". The exact centres and\n#   bandwidths are not given; the bank of Mesgarani and Chang (2012, ref. 17/48), the paper's\n#   cited source, is the standard choice, and it cannot change an outcome beyond what the\n#   baseline does. OPEN, the baseline. The Methods do not say which data are baseline.\n#   Readings (a) a silent window before each utterance (the 500 ms before the start of the\n#   plotted epochs, -1000 to -500 ms from the C-V transition, is used for this reading);\n#   (b) the mean and SD of the whole recording of the channel. Both are run.\n# - Per-syllable responses. The analyses use cross-syllable variability in the average Hg\n#   (Methods, Acoustic Analysis), so each CV's response at each electrode is the mean over\n#   its renditions, aligned at the C-V transition. Epoch -500 to +750 ms (the range of the\n#   Fig. 5a symbols); the analysis windows below lie within it.\n# - vSMC electrodes. Electrodes on the pre- and post-central gyri and the guenon (Methods,\n#   Fig. 1a, b). If the dataset gives anatomical labels, those are used; if it gives\n#   neither labels nor positions relative to the central sulcus and Sylvian fissure, the\n#   spatial claims are blocked (metadata_insufficient) and the others are run on all\n#   electrodes that pass the activity rule, as a variant only.\n# - Articulator state matrix. Supplementary Figure 1d: per CV, four binary consonant\n#   articulators (Lips, Tongue, Larynx, Jaw) and two vowel features (Back Tongue, High\n#   Tongue). It is given only as a figure; the author reads it from supplement page 2.\n# - Phonetic feature matrix. Supplementary Figure 12: nine constriction location features,\n#   six constriction degree/shape features and four vowel configuration features, white = 1.\n#   Given only as a figure (supplement page 15). The Methods point to Supplemental Figure 9\n#   for it; the legend of Supplementary Figure 12 is the matrix.\n# - Major oral articulator labels for consonants, labial, coronal and dorsal (Fig. 4a, c;\n#   Supplementary Figure 10, 11). Which consonant is which is from the phonetic feature matrix\n#   and Fig. 4c; /h/ and /r/ are not placed by any text sentence. OPEN; readings (a) /h/ and\n#   /r/ left out of the labelled sets, (b) /r/ coronal and /h/ dorsal.\n# - Cortical state-space. Per subject, PCA on the matrix of vSMC electrodes by\n#   concatenated (CV x time) Hg, each electrode's time series z-scored across syllables; the\n#   first nine PCs; a CV's state at time t is the projection of its electrode vector on them.\n#   Consonant time t = -25 ms; vowel time t = +250 ms (Fig. 4a, b legend).\n# - Time windows. Early window -375 to 120 ms and late window 125 to 620 ms (Results, Phonetic\n#   Organization, paragraph 3), in 5 ms steps.\n# - Tolerances. 10% of a reported value when the paper gives no spread; the paper's s.e. when\n#   it gives one; reasons for any other are given in the claim. Counts of subjects are exact.\n# - Readings. Where a claim lists readings of a reported number, it matches if it matches\n#   under any of them. Where a claim lists readings of a method detail, its outcome is the one\n#   all readings give, and it is methods_underspecified when they differ.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000019\"\npaper: doi:10.1038/nature11911\nclaims:\n- id: data-composition\n  statement: Three subjects with high-density ECoG (two left, one right hemisphere) read aloud CV\n    syllables made of 18 or 19 consonants followed by /a/, /i/ or /u/, each CV produced 15 to\n    100 times, with the microphone recorded with the ECoG at 3052 Hz.\n  source: Methods, Subjects and Experimental Task, and Data acquisition and Signal Processing;\n    Supplementary Table 1\n  quote: Three native English speaking human subjects underwent chronic implantation of a\n    high-density, subdural electrocortigraphic (ECoG) array over the left hemisphere (two\n    subjects) or right hemisphere (one subject) ... composed of 18–19 consonants (19 consonants\n    for two subjects, 18 consonants for one subject), followed by one of three vowels. Each CV\n    was produced between 15 and 100 times\n  expected:\n  - quantity: subjects\n    value: 3\n    tolerance: 0\n  - quantity: distinct CV syllables over all subjects\n    value: 168\n    tolerance: 0\n  - quantity: ECoG sampling rate\n    value: 3052\n    tolerance: 1\n    unit: Hz\n  criterion: Reproduced when the dataset holds three subjects with ECoG and audio, CV labels\n    with 19, 19 and 18 consonants by three vowels (168 distinct CVs, Fig. 3c legend), at least\n    15 renditions of every CV and at most 100, and two left and one right hemisphere grids.\n    Partially reproduced when it holds the three subjects but some counts differ; the counts\n    found are reported. The sampling rate within 1 Hz of 3052 Hz (TDT rates are often printed\n    rounded, e.g. 3051.76 Hz).\n- id: active-electrodes\n  statement: About 30 active vSMC electrodes were found per subject during syllable articulation,\n    an electrode being active when its high-gamma z-score changed by more than 2 for any\n    syllable.\n  source: Results, vSMC Physiology During Syllable Production, paragraph 1\n  quote: During syllable articulation, approximately 30 active vSMC electrode sites were\n    identified per subject (~1200 mm 2 , change in z-score > 2 for any syllable)\n  expected:\n  - quantity: active vSMC electrodes per subject\n    value: 30\n    tolerance: 3\n  criterion: Per subject, vSMC electrodes whose mean Hg for any CV exceeds a z-score of 2 at any\n    time in the epoch. OPEN, \"change in z-score\" read as (a) Hg above 2, (b) absolute Hg above\n    2 (increase or decrease). Reproduced when, under each baseline reading and one reading of\n    the change, the mean count over subjects is within 27 to 33; partially reproduced when the\n    count is within 20 to 40 (the paper says \"approximately\"). The ~1200 mm2 is not tested, as\n    the paper does not say how it was measured; the counts per subject are reported.\n- id: fig1c-e-articulator-electrodes\n  statement: In one subject, dorsal electrodes (e124, e108) were active for /b/ (lips), mid vSMC\n    electrodes (e129, e133, e105) for /d/ (front tongue), a more ventral electrode (e104) most\n    for /g/ (back tongue), and others (e154, e136, e119) during the vowel /a/.\n  source: Results, vSMC Physiology During Syllable Production, paragraph 1; Figure 1c-e\n  quote: Dorsally located electrodes (e.g. e124, e108; black) were active during production of\n    /b/, which requires transient closure of the lips. In contrast, mid-positioned electrodes\n    (e.g. e129, e133, e105; grey) were active during production of /d/ ... Amore ventral\n    electrode (e.g. e104; red) was most active during production of /g/\n  criterion: The paper does not say which subject Fig. 1 shows (\"single subject brain\", Fig. 1a\n    legend) or how electrodes are numbered. Readings of the numbering (a) the dataset's\n    electrode index counted from 1, (b) counted from 0; the subject is the one in which the\n    named electrodes are all vSMC electrodes, each subject tried. For /ba/, /da/ and /ga/, the\n    mean Hg from -500 to 0 ms (the consonant phase before the C-V transition, Fig. 1c-e).\n    Reproduced when, in one subject and numbering, e124 and e108 respond more to /ba/ than to\n    /da/ and /ga/, at least two of e129, e133 and e105 respond more to /da/ than to /ba/, e104\n    responds most to /ga/, and the order of the named electrodes' distance from the Sylvian\n    fissure is /b/ electrodes above /d/ electrodes above e104. Not testable, and blocked as\n    metadata_insufficient, when no subject and numbering puts all named electrodes on vSMC.\n- id: fig1f-h-phonetic-contrasts\n  statement: Fricatives with different tongue-tip constriction locations (/th/, /s/, /sh/)\n    engaged different electrodes; front-tongue consonants of different manner (/l/, /n/, /d/)\n    engaged overlapping electrodes with different magnitudes; and for /ja/, /ji/, /ju/ the\n    activity was similar before the C-V transition, while a dorsal electrode was active during\n    /u/ only and a mid vSMC electrode had prolonged activity for /i/ and /u/.\n  source: Results, vSMC Physiology During Syllable Production, paragraph 2; Figure 1f-h\n  quote: Syllables with the same consonant followed by different vowels ( Fig. 1h, /ja/, /ji/,\n    /ju/ ) revealed similar activity patterns preceding the CV transition. During vowel\n    phonation, a dorsal electrode is clearly active during /u/ (black arrow), but not /i/ or /a/\n  criterion: The paper shows selected electrodes it does not name, with no test, so only the\n  - placeholder\n"
}
```

```
File created successfully at: claims/000019/10.1038-nature11911.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

I left a placeholder mid-file by mistake; rewriting the whole file now.

**Agent calls Bash**

```bash
head -c 0 /dev/null; grep -n "Sylvian\|guenon\|geunon" paper/10.1038-nature11911.txt | head -3 >/dev/null; python3 - <<'EOF'
t=open('paper/10.1038-nature11911.txt').read()
for s in ["10 −10","P < 10-3","P > 0.4","R 2 range","Average Silhouette = 0.47","~60% of variance","n = 211","F = 40"]:
    i=t.find(s); print(repr(s), i, repr(t[i-60:i+80]) if i>=0 else '')
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='claims/000019/10.1038-nature11911.yaml'
t=open(p).read()
i=t.index('- id: fig1c-e-articulator-electrodes')
open(p,'w').write(t[:i])
EOF
tail -5 claims/000019/10.1038-nature11911.yaml
```

```
time in the epoch. OPEN, "change in z-score" read as (a) Hg above 2, (b) absolute Hg above
    2 (increase or decrease). Reproduced when, under each baseline reading and one reading of
    the change, the mean count over subjects is within 27 to 33; partially reproduced when the
    count is within 20 to 40 (the paper says "approximately"). The ~1200 mm2 is not tested, as
    the paper does not say how it was measured; the counts per subject are reported.
```

**Agent calls Bash**

```bash
cat >> claims/000019/10.1038-nature11911.yaml <<'EOF'
- id: fig1c-e-articulator-electrodes
  statement: In one subject, dorsal electrodes (e124, e108) were active for /b/ (lips), mid vSMC
    electrodes (e129, e133, e105) for /d/ (front tongue), and a more ventral electrode (e104)
    was most active for /g/ (back tongue).
  source: Results, vSMC Physiology During Syllable Production, paragraph 1; Figure 1c-e
  quote: Dorsally located electrodes (e.g. e124, e108; black) were active during production of
    /b/, which requires transient closure of the lips. In contrast, mid-positioned electrodes
    (e.g. e129, e133, e105; grey) were active during production of /d/ ... Amore ventral
    electrode (e.g. e104; red) was most active during production of /g/
  criterion: The paper does not say which subject Fig. 1 shows ("single subject brain", Fig. 1a
    legend) or how its electrodes are numbered. OPEN, the numbering; readings (a) the
    dataset's electrode index counted from 1, (b) counted from 0. The subject is the one in
    which all named electrodes are vSMC electrodes; each subject is tried. OPEN, the measure
    of activity for a syllable; readings (i) mean Hg at the paper's consonant time, -25 ms
    (Fig. 4a), (ii) peak mean Hg over the epoch (Fig. 1c-e shows the whole trace and says
    "most active"). Reproduced when, in one subject and numbering, e124 and e108 respond more
    to /ba/ than to /da/ and /ga/, e129, e133 and e105 respond more to /da/ than to /ba/ and
    /ga/, e104 responds more to /ga/ than to /ba/ and /da/, and the distance from the Sylvian
    fissure orders them /b/ electrodes above /d/ electrodes above e104; partially reproduced
    when the order holds but some named electrode prefers another syllable. Blocked as
    metadata_insufficient when no subject and numbering puts all named electrodes on vSMC.
- id: fig1f-h-phonetic-contrasts
  statement: Fricatives with different tongue-tip constriction locations (/th/, /s/, /sh/)
    engaged different electrodes; front-tongue consonants of different manner (/l/, /n/, /d/)
    engaged overlapping electrodes with different magnitudes; for /ja/, /ji/, /ju/ the activity
    was similar before the C-V transition, while a dorsal electrode was active during /u/ only.
  source: Results, vSMC Physiology During Syllable Production, paragraph 2; Figure 1f-h
  quote: Syllables with the same consonant followed by different vowels ( Fig. 1h, /ja/, /ji/,
    /ju/ ) revealed similar activity patterns preceding the CV transition. During vowel
    phonation, a dorsal electrode is clearly active during /u/ (black arrow), but not /i/ or /a/
  criterion: The paper calls these qualitative illustrations ("can be observed qualitatively")
    at electrodes it does not name, with no measure, window or test. Only the last part can be
    judged with the paper's own threshold. Reproduced when, in at least one subject, a vSMC
    electrode with a positive lips weight (claim fig2a-lips-dorsal) has mean Hg above a z-score
    of 2 (the activity rule of claim active-electrodes) at the vowel time, +250 ms, for /ju/
    and below 2 for /ja/ and /ji/. The other parts are shown as traces and not judged
    (methods_underspecified for those parts).
  depends_on:
  - fig2a-lips-dorsal
- id: fig2a-lips-dorsal
  statement: Each articulator is represented across vSMC; the lip representation lies in dorsal
    vSMC and the tongue representation is spread over its ventral part.
  source: Results, Spatial Representation of Articulators, paragraph 1; Figure 2a
  quote: We found representations for each articulator distributed across vSMC ( Fig. 2a ). For
    example, the lip representation was localized to the dorsal aspect of vSMC, whereas the
    tongue representation was more distributed across the ventral aspect
  criterion: GLM of Methods Eq. 2, at each time and vSMC electrode, of the CVs' mean Hg on the
    four consonant articulators (Supplementary Figure 1d), by least squares. Electrodes kept
    when the mean over T_A of the regression p-value (F-test of the model) is below 0.05 for
    any articulator A; W_iA is the mean of the weight over T_A (Methods Eq. 3); T_A is the
    subject's mean onset-to-offset window of significant partial correlations for A (claim
    fig3d-timing-sequence). Per subject, the W-weighted mean dorsal-ventral distance from the
    Sylvian fissure over electrodes with positive weights, for lips and for tongue.
    Reproduced when lips lie dorsal to tongue in every subject; partially reproduced in two
    of three. The paper's maps are smoothed with a 2 mm uniform circular kernel and averaged
    over subjects; the maps are shown for comparison.
  depends_on:
  - fig3d-timing-sequence
- id: fig2b-somatotopic-sequence
  statement: Across subjects the articulator representations are laid out from dorsal to ventral
    as larynx, lips, jaw, tongue and larynx, with a laryngeal representation at the dorsal end
    of vSMC as well as a ventral one.
  source: Results, Spatial Representation of Articulators, paragraph 2; Figure 2b; Discussion,
    paragraph 1
  quote: We found an overall somatotopic dorsal-ventral arrangement of articulator
    representations laid out in the following sequence:larynx (X), lips (L), jaw (J), tongue
    (T), and larynx (X)
  criterion: As in Methods, Somatotopic map. The W_iA maps of claim fig2a-lips-dorsal, per
    subject smoothed with a 2 mm uniform circular kernel in the (AP, DV) plane and averaged
    over subjects; the locations of the top 10% of weights for each articulator; then k = 4
    nearest neighbours within 3 mm, mixed when no articulator holds more than 50%. OPEN, the
    grid on which maps are smoothed and averaged; a 1 mm grid is the standard choice, and
    0.5 mm is shown as a variant. Reproduced when the DV positions of the top-10% points
    order as larynx (a dorsal group) above lips above jaw above tongue above larynx (a
    ventral group), read from the medians of each articulator's points with the larynx
    points split at the median DV of the lips and tongue points; partially reproduced when
    lips above jaw above tongue holds but the dorsal larynx group is absent. The 5% and 15%
    thresholds (Supplementary Figure 4) are shown as variants.
  depends_on:
  - fig2a-lips-dorsal
- id: suppfig3b-spatial-clustering
  statement: Electrodes with similar articulator representations lie closer together than
    chance; the mean spatial autocorrelation within 3 mm is 0.45 against 0.26 for permuted
    electrode positions.
  source: Supplementary Figure 3a, b legend
  quote: The correlation values for the data (0.45 ± 0.03, mean ± s.e., 3 subjects x 4
    articulators, n = 12) were significantly greater than for the randomized data (0.26 ± 0.02,
    mean ± s.d., 1000 randomizations for each subject; P < 10-3)
  statistics:
  - test: permutation test, electrode locations shuffled within subject, 1000 randomizations
    p: 0.001
    p_relation: "<"
    n: 3 subjects x 4 articulators, 12 maps
  expected:
  - quantity: mean autocorrelation within 3 mm, data
    value: 0.45
    tolerance: 0.03
  - quantity: mean autocorrelation within 3 mm, shuffled
    value: 0.26
    tolerance: 0.02
  criterion: Per subject and articulator, the smoothed W_iA map of claim fig2b-somatotopic-
    sequence; its normalized 2-D spatial autocorrelation; the mean within 3 mm of zero shift.
    Null by shuffling electrode locations within subject 1000 times before smoothing
    (Supplementary Methods). OPEN, the normalization of the 2-D correlation; readings (a)
    Pearson correlation of the overlapping parts at each shift, (b) the cross-correlation
    divided by its value at zero shift. Reproduced when the data's mean is within tolerance
    and above the 99.9th percentile of the null.
  depends_on:
  - fig2b-somatotopic-sequence
- id: suppfig3d-cross-subject
  statement: Each articulator's representation lies in a more consistent place across subjects
    than chance (mean cross-subject correlation within 3 mm 0.195 against 0.031).
  source: Supplementary Figure 3c, d legend
  quote: The correlation values for the data (0.195 ± 0.064, mean ± s.e., 3 subjects x 4
    articulators, n = 12) were significantly greater than for the randomized data (0.031 ±
    0.021, mean ± s.d., P < 10-3, 1000 iteration permutation test)
  statistics:
  - test: permutation test, 1000 iterations
    p: 0.001
    p_relation: "<"
    n: 3 subject pairs x 4 articulators, 12 comparisons
  expected:
  - quantity: mean cross-subject correlation within 3 mm, data
    value: 0.195
    tolerance: 0.064
  - quantity: mean cross-subject correlation within 3 mm, shuffled
    value: 0.031
    tolerance: 0.021
  criterion: As claim suppfig3b-spatial-clustering, with the cross-correlation of one
    articulator's maps between pairs of subjects (S1-S2, S2-S3, S1-S3). The right-hemisphere
    subject's AP axis is taken as the paper's coordinates give it (distance from the central
    sulcus, anterior positive), so no mirroring is needed. Reproduced when the data's mean is
    within tolerance and above the 99.9th percentile of the null.
  depends_on:
  - fig2b-somatotopic-sequence
- id: suppfig3f-dv-sequence
  statement: Within each subject, adjacent articulator representations (larynx-tongue,
    tongue-jaw, jaw-lips) are spatially sequenced along the dorsal-ventral axis, with positive
    cross-correlation on one side of the diagonal (0.099) and negative on the other (-0.102),
    both beyond chance.
  source: Supplementary Figure 3e, f legend
  quote: The correlation values for the above diagonal data were positive (0.099 ± 0.052, mean ±
    s.e., 3 subjects x 3 cross-articulator comparisons, n = 9) and significantly greater than
    for the randomized data ... the correlation values for the below diagonal data were negative
    (-0.102 ± 0.052, mean ± s.e., n = 9)
  statistics:
  - about: above the diagonal
    test: permutation test, 1000 permutations for each subject
    p: 0.001
    p_relation: "<"
    n: 3 subjects x 3 comparisons, 9
  - about: below the diagonal
    test: permutation test, 1000 permutations for each subject
    p: 0.001
    p_relation: "<"
    n: 3 subjects x 3 comparisons, 9
  expected:
  - quantity: mean cross-correlation within the 6 mm semicircle above the diagonal
    value: 0.099
    tolerance: 0.052
  - quantity: mean cross-correlation within the 6 mm semicircle below the diagonal
    value: -0.102
    tolerance: 0.052
  criterion: As claim suppfig3b-spatial-clustering, cross-correlating larynx with tongue, tongue
    with jaw and jaw with lips within each subject; the mean over the 6 mm semicircles above and
    below the diagonal that the legend draws, the anterior-dorsal to posterior-ventral axis.
    OPEN, the diagonal's exact angle; readings (a) 45 degrees, (b) the anisotropy axis of the
    mean autocorrelation of claim suppfig3b-spatial-clustering. Reproduced when both means are
    within tolerance with opposite signs and both exceed the null's 99.9th percentile in
    magnitude.
  depends_on:
  - suppfig3b-spatial-clustering
- id: suppfig5-intermediate-organization
  statement: The observed map is neither a perfect linear somatotopy nor random; the mean
    distance between electrodes preferring the same articulator (11.06 mm) and between those
    preferring different ones (15.11 mm) lie between the two null models.
  source: Supplementary Figure 5b legend
  quote: The observed intra-articulator distances (11.06 ± 1.01 mm. mean ± s.e., n = 3188
    pair-wise distances) and across articulator distances (15.11 ± 1.01mm, mean ± s.e., n = 4587
    pair-wise distances) are both intermediate to these bounding values
  statistics:
  - about: observed against both null models; printed as "P >10-3", which with the figure's
      *** marks reads as P < 10-3
    test: comparison with 1000 simulated maps per null model
    p: 0.001
    p_relation: ">"
    n: 3188 within- and 4587 across-articulator distances
  expected:
  - quantity: mean within-articulator distance
    value: 11.06
    tolerance: 1.01
    unit: mm
  - quantity: mean across-articulator distance
    value: 15.11
    tolerance: 1.01
    unit: mm
  criterion: Electrodes of claim fig2a-lips-dorsal labelled by their largest W_iA (winner take
    all); Euclidean distances in the (AP, DV) plane between pairs of electrodes, within and
    across labels. OPEN, whether pairs are formed within subjects only or over the pooled
    electrodes of all subjects; both are run. The Methods do not describe how the linear
    somatotopy maps were made (the legend says "see Methods" and the Methods are silent), so
    the bounds are the legend's own values (linear 7.43 and 17.7 mm; random 14.08 and 14.07
    mm). Reproduced when both observed means are within tolerance and lie strictly between
    the bounds; a random-scatter null, by permuting labels over the electrodes 1000 times, is
    shown as a variant.
  depends_on:
  - fig2a-lips-dorsal
- id: suppfig6-mixed-tuning
  statement: Single electrodes show a clear preferred articulator and also carry weights for
    other articulators.
  source: Results, Spatial Representation of Articulators, paragraph 2; Supplementary Figure 6
  quote: This analysis revealed clear preferred tuning for individual articulators at single
    electrodes (Fig. 2c, electrodes categorized according to the strongest articulator
    representation), and also demonstrated that single electrodes had functional
    representations of multiple articulators
  criterion: As in Methods (analysis of representational overlap) for the electrodes of claim
    fig2a-lips-dorsal. Electrodes grouped by their largest W_iA; for each, the positive
    weights as a percentage of their sum; the group means. Reproduced when, in every group,
    the preferred articulator has the largest mean percentage and at least one other
    articulator has a mean percentage above zero. The paper gives no number, so the group
    means are reported.
  depends_on:
  - fig2a-lips-dorsal
- id: fig3d-timing-sequence
  statement: Articulator correlations follow a staggered sequence consistent across subjects;
    lip and tongue correlations begin well before sound onset, jaw and larynx align to the C-V
    transition, and the high and back tongue vowel features peak near the vowel midpoint (~250
    ms).
  source: Results, Timing of Articulator Representations, paragraph 1; Figure 3a-d
  quote: lip and tongue correlations began well before sound onset ( Fig. 3a, c, d ); jaw and
    larynx correlations were aligned to the CV transition ( Fig. 3a, c, d ); high tongue and
    back tongue features showed high temporal specificity for the vowel phase, peaking near the
    acoustic mid-point of the vowels (~250 ms, Fig. 3b–d ). This sequence of articulator
    correlations was consistent across subjects
  statistics:
  - test: ANOVA
    statistic: F = 40, df = 5
    p: 1.0e-10
    p_relation: "<"
    n: 211 electrodes from 3 subjects
  expected:
  - quantity: electrodes over all articulators and subjects
    value: 211
    tolerance: 21
  - quantity: peak time of high and back tongue correlations
    value: 250
    tolerance: 25
    unit: ms
  criterion: Partial correlation (Methods Eq. 4), per vSMC electrode and time, of the CVs' mean
    Hg with each of the six articulator variables of Supplementary Figure 1d, the other five
    partialled out. For each articulator, electrodes whose peak rho exceeds the mean + 2.5 SD
    of rho over electrodes and time (per subject; OPEN whether over all articulators or per
    articulator, both run). Onset and offset are the first and last times of the contiguous
    run around the peak above that threshold (OPEN, the paper does not define them; reading
    (b) threshold at half the peak is shown). One-way ANOVA across the six articulators of
    the timing values pooled over subjects. OPEN, which timing value the ANOVA uses; readings
    (a) onset, (b) peak. Acoustic onset per CV from the audio of the prototype rendition
    (Methods Eq. 1, cochlear spectrogram, a threshold on acoustic power). Reproduced when the
    ANOVA has p < 1e-10, the mean onsets of lips and tongue precede the mean acoustic onset,
    the mean onsets of jaw and larynx are later than those of lips and tongue, and the mean
    peaks of high and back tongue are within tolerance of 250 ms; partially reproduced when
    the ANOVA holds and two of the three order conditions hold. Counts per articulator are
    reported against the 211 total.
- id: suppfig7-no-latency-difference
  statement: Onset latencies of the articulator model fit do not differ between electrodes
    just anterior and just posterior to the central sulcus (within 10 mm), nor across the
    guenon.
  source: Results, Timing of Articulator Representations, paragraph 1; Supplementary Figure 7
  quote: we found no significant latency differences in those areas immediately anterior and
    posterior to the central sulcus (±10 mm), or across the geunon (a-b, P > 0.4, Rank-Sum test;
    n = 71 and n = 67 electrodes
  statistics:
  - test: rank-sum test
    p: 0.4
    p_relation: ">"
    n: 71 electrodes (pre against post central) and 67 electrodes (across the guenon), three
      subjects
  criterion: A claim of absence, judged on the paper's test. Per electrode, the onset latency of
    the GLM R2 (Methods Eq. 2). OPEN, the onset; readings (a) first time R2 is significant
    (F-test p < 0.05) in the run that holds its peak, (b) first time R2 exceeds the mean + 2.5
    SD rule used for partial correlations. Electrodes within 10 mm anterior against within
    10 mm posterior of the central sulcus; electrodes on the guenon against those dorsal to it
    (OPEN, how the guenon boundary is set; the dataset's anatomical labels are used, and the
    comparison is blocked without them). Two-sided Wilcoxon rank-sum at p < 0.05. Reproduced
    when neither comparison is significant under every onset reading; not reproduced when
    one is under every reading; the medians and counts are reported against 71 and 67.
- id: pca-nine-components
  statement: The cortical state-space has nine spatial PCs in every subject, the eigenvalues
    falling fast up to the ninth and slowly after, together explaining about 60% of the
    variance.
  source: Results, Phonetic Organization of Spatial Patterns, paragraph 1; Methods, PCA and
    Cortical-State Space; Supplementary Figure 8
  quote: we used principal components analysis to transform the observed cortical activity
    patterns into a ‘cortical state-space’ (9 spatial PCs for all subjects, ~60% of variance
    explained
  expected:
  - quantity: variance explained by the first nine PCs
    value: 0.6
    tolerance: 0.06
  criterion: PCA as in the header, per subject, on the vSMC electrodes. OPEN, the time range
    concatenated; readings (a) the epoch -500 to 750 ms, (b) the union of the early and late
    windows, -375 to 620 ms. Reproduced when, under one reading, the mean over subjects of the
    variance explained by nine PCs is within tolerance and the inflection the paper reports
    is seen (the drop from PC 9 to 10 exceeds every later drop... read as the ratio of
    successive eigenvalues being larger at 9 than the median of later ratios). Values per
    subject are reported. The Methods cite Supplemental Figure 6 for the eigenvalues; the
    figure is Supplementary Figure 8.
- id: fig4a-consonant-clusters
  statement: At the consonant time (-25 ms) k-means clustering of the cortical state-space groups
    syllables by major oral articulator (labial, coronal, dorsal), and three clusters are more
    parsimonious than two or four (mean silhouette 0.47 against 0.45 and 0.43).
  source: Results, Phonetic Organization of Spatial Patterns, paragraph 1; Figure 4a; Methods,
    Clustering Analysis, paragraph 2
  quote: On average across subjects, this analysis validated the claim that three clusters
    (Average Silhouette = 0.47) was a more parsimonious clustering scheme than either two
    (Average Silhouette = 0.45) or four clusters (Average Silhouette = 0.43)
  expected:
  - quantity: mean silhouette, 3 clusters
    value: 0.47
    tolerance: 0.047
  - quantity: mean silhouette, 2 clusters
    value: 0.45
    tolerance: 0.045
  - quantity: mean silhouette, 4 clusters
    value: 0.43
    tolerance: 0.043
  criterion: Per subject, k-means with Euclidean distance on the CVs' nine-PC states at -25 ms,
    for k = 2, 3 and 4; mean silhouette per k, averaged over subjects. k-means starts are a
    standard choice (100 random starts, the best kept) that is not expected to change the
    outcome. Reproduced when k = 3 has the highest mean silhouette and the three values are
    within tolerance; partially reproduced when k = 3 is highest but values are outside it.
    The cluster-articulator match is claim suppfig11-co-clustering.
- id: suppfig11-co-clustering
  statement: Clusters of the cortical state-space match the major articulators at the consonant
    time (median co-clustering 0.50 against 0.32 by chance) and the vowels at the vowel time
    (0.65 against 0.37), across subjects.
  source: Results, Phonetic Organization of Spatial Patterns, paragraph 1; Supplementary Figure
    11a, b
  quote: clustering of CV’s in the cortical state-space co-clustered with the major articulators
    significantly more than expected by chance (Red:observed distribution, median = 0.50,
    Black:null distribution from 1000 random permutations of articulator assignments of CVs,
    median = 0.32
  statistics:
  - about: consonants
    test: Wilcoxon signed-rank test
    p: 1.0e-20
    p_relation: "<"
    n: 168 syllables from three subjects
  - about: vowels
    test: Wilcoxon signed-rank test
    p: 1.0e-15
    p_relation: "<"
    n: 168 syllables from three subjects
  - about: consonants and vowels, main text
    test: not named
    p: 1.0e-10
    p_relation: "<"
  expected:
  - quantity: median co-clustering, consonants
    value: 0.50
    tolerance: 0.05
  - quantity: median co-clustering, consonant null
    value: 0.32
    tolerance: 0.032
  - quantity: median co-clustering, vowels
    value: 0.65
    tolerance: 0.065
  - quantity: median co-clustering, vowel null
    value: 0.37
    tolerance: 0.037
  criterion: Per subject, k-means (k = 3) at -25 ms (consonants) and +250 ms (vowels) as in
    claim fig4a-consonant-clusters; the co-clustering coefficient of each CV against the
    major articulator labels (consonants) or vowel identity (vowels), Supplementary Methods
    Eq. 1, kappa = 1 - |NC delta AC| / (|NC| + |AC|); the null for each CV the mean of kappa
    over 1000 permutations of the labels within subject. Wilcoxon signed-rank, observed
    against null, over the 168 CVs. For consonants the two readings of the /h/ and /r/
    labels in the header. Reproduced when both medians are within tolerance and both tests
    give p < 1e-10 (the main text's bound); partially reproduced when the tests hold and a
    median is outside tolerance.
  depends_on:
  - fig4a-consonant-clusters
- id: fig4c-d-hierarchy
  statement: Hierarchical clustering of the state-space puts the major oral articulator
    (dorsal, labial, coronal) at the top tier for consonants, superordinate to constriction
    location, with constriction degree only at the lowest level; for vowels the first split
    is lip rounding (/u/ against /a/ and /i/).
  source: Results, Phonetic Organization of Spatial Patterns, paragraph 2; Figure 4c, d
  quote: For consonants, this analysis confirmed that the primary tier of organization was
    defined by the major oral articulator features:dorsal, labial, or coronal ( Fig. 4c ) ...
    during the vowel period, a primary distinction was based upon the presence/absence of
    lip-rounding (/u/ vs. /a/ & /i/)
  criterion: Agglomerative clustering with Ward's method on Euclidean distances between the
    CVs' nine-PC states (Methods), at -25 ms and +250 ms. The paper does not say whether Fig.
    4c, d is one subject or pooled; each subject is run. Consonants. The tree cut into three
    clusters; reproduced for a subject when the three clusters have different majority major
    articulators and at least two thirds of the labelled CVs fall in the cluster of their
    articulator's majority (OPEN, the paper gives no purity measure; the co-clustering
    coefficient of claim suppfig11-co-clustering for the cut is reported as well). Vowels.
    The tree cut into two clusters; reproduced for a subject when one cluster holds a
    majority of the /u/ syllables and the other a majority of the /a/ and /i/ syllables. The
    claim is reproduced when both hold in every subject and partially reproduced when they
    hold in some. The lowest-level manner grouping is shown, not judged.
- id: fig4ef-feature-correlations
  statement: Over early times (-375 to 120 ms) constriction location correlates with the
    state-space structure more than constriction degree, which correlates more than the
    upcoming vowel; over later times (125 to 620 ms) vowel configuration correlates most.
  source: Results, Phonetic Organization of Spatial Patterns, paragraph 3; Figure 4e, f
  quote: Across early time points (−375:120 ms), we found that consonant features describing
    constriction location yielded a significantly greater correlation with the cortical
    state-space than constriction degree, which in turn was significantly more correlated than
    the upcoming vowel ... across later time points (125:620 ms), we found that vowel features
    provided the greatest correlation
  statistics:
  - about: early window, location against degree against vowel
    test: Wilcoxon signed-rank test
    p: 1.0e-10
    p_relation: "<"
    n: 297 from 3 subjects
  - about: late window, vowel configuration against the others
    test: Wilcoxon signed-rank test
    p: 1.0e-10
    p_relation: "<"
    n: 297 from 3 subjects
  criterion: Per subject and time, R(t) of Methods Eq. 7, the Pearson correlation between the
    unique pairwise Euclidean distances of the CVs' nine-PC states and those of the CVs in each
    feature set of Supplementary Figure 12 (location, degree/shape, vowel). The n of 297 is
    read as 99 time points in each window x 3 subjects, at 5 ms steps (OPEN, which end point
    is left out; the result is not expected to depend on it). Paired Wilcoxon signed-rank
    tests over these values. Reproduced when location > degree and degree > vowel in the early
    window, and vowel > location and vowel > degree in the late window, each with p < 1e-10;
    partially reproduced when some of the four comparisons hold. Distances in Hamming form
    for the feature sets are a variant (Methods say both gave the same result).
- id: fig5c-separability-timing
  statement: Cluster separability, averaged over subjects, rises from about -300 ms and peaks
    about 200 ms before the C-V transition for consonants, and rises from about 50 ms and
    peaks at +250 ms for vowels.
  source: Results, Dynamics of Phonetic Representations, paragraph 2; Figure 5c
  quote: separability peaked ~200 ms before the CV transition for consonants (onset, ~−300 ms),
    and at +250 ms for vowels (onset, ~50 ms)
  expected:
  - quantity: consonant separability peak
    value: -200
    tolerance: 20
    unit: ms
  - quantity: consonant separability onset
    value: -300
    tolerance: 30
    unit: ms
  - quantity: vowel separability peak
    value: 250
    tolerance: 25
    unit: ms
  - quantity: vowel separability onset
    value: 50
    tolerance: 10
    unit: ms
  criterion: Separability at each time is the mean distance between CVs in different clusters
    minus the mean distance within clusters (Methods, Cluster Separability), on nine-PC states,
    per subject, then averaged over subjects. OPEN, the clusters; readings (a) the phonetic
    groups, major articulator for consonants and vowel identity for vowels, (b) k-means (k =
    3) at each time. OPEN, the onset; readings (a) the first time the mean exceeds its
    pre-epoch level by 2 bootstrap s.e. (1000 bootstrap samples of syllables, as the
    Methods), (b) the time at half the peak. The vowel onset tolerance is two 5 ms samples, as
    10% would be a single sample. Reproduced when, under each reading of the clusters and one
    of the onset, all four values are within tolerance; partially reproduced when the peaks
    are and an onset is not.
- id: fig5d-separability-coupling
  statement: Cluster separability and the correlation of the state-space with phonetic features
    are tightly linked over time for consonants and vowels in each subject (R2 0.42 to 0.98, all
    P < 1e-10).
  source: Results, Dynamics of Phonetic Representations, paragraph 2; Figure 5c, d
  quote: Across subjects, we found that cluster separability and the correlation between cortical
    state-space organization and phonetic features were tightly linked for both consonants and
    vowels in a time-dependent fashion (R 2 range = [0.42–0.98], P < 10 −10 for all)
  statistics:
  - test: linear regression R2 between time courses
    p: 1.0e-10
    p_relation: "<"
    n: 3 subjects x consonants and vowels, time points as samples
  expected:
  - quantity: lowest R2 over subjects and categories
    value: 0.42
    tolerance: 0.042
  - quantity: highest R2 over subjects and categories
    value: 0.98
    tolerance: 0.098
  criterion: Per subject, the separability time course of claim fig5c-separability-timing and
    R(t) of claim fig4ef-feature-correlations, constriction location for consonants and vowel
    configuration for vowels (OPEN; reading (b) the mean over the three feature sets);
    squared Pearson correlation over the epoch at 5 ms steps. Reproduced when the six R2
    values lie within 0.38 to 1 (the reported range widened by 10% of each bound) with each
    p < 1e-10; partially reproduced when all are positive and significant but some fall below
    0.38.
  depends_on:
  - fig5c-separability-timing
  - fig4ef-feature-correlations
- id: suppfig13-consonant-vowel-distance
  statement: Consonant and vowel representations occupy distinct regions of the state-space;
    consonant-vowel distances are larger than consonant-consonant and vowel-vowel distances,
    and consonant-consonant distances are larger than vowel-vowel ones.
  source: Results, Dynamics of Phonetic Representations, paragraph 3; Supplementary Figure 13
  quote: We found that the distribution of distances comparing consonants and vowels was
    significantly greater than the consonant-consonant comparison or vowel-vowel comparison,
    and the consonant-consonant comparison was greater than the vowel-vowel comparison
  statistics:
  - test: Wilcoxon signed-rank test
    p: 1.0e-10
    p_relation: "<"
    corrected: Bonferroni, 3 comparisons
    n: 4623 for all
  criterion: Per subject, nine-PC states of each CV at -25 ms (consonant) and +250 ms (vowel).
    For each unordered pair of CVs in a subject, the consonant-consonant distance, the
    vowel-vowel distance and the consonant-vowel distance (OPEN, which of the pair at which
    time; readings (a) the mean of the two cross pairings, (b) i at -25 ms and j at +250 ms).
    4623 is read as the pairs within subjects (1596 + 1596 + 1431). Paired Wilcoxon
    signed-rank tests over the pairs pooled over subjects, Bonferroni for 3. Reproduced when
    all three orderings hold with corrected p < 1e-10 and the pair count is 4623.
- id: suppfig9-pc-articulator-weights
  statement: The first three PCs are weighted toward tongue over lips, and toward lips over jaw
    and larynx, while jaw and larynx do not differ.
  source: Supplementary Figure 9a legend
  quote: the magnitude of the articulator weightings (log10(|(PCNi*Wij)|)) was significantly
    biased towards tongue over lips (P < 0.05) over jaw and larynx (P < 0.001 for each), while
    the difference between jaw and larynx was not significant (P > 0.2)
  statistics:
  - about: tongue against lips
    test: Wilcoxon signed-rank test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni, 6 comparisons per PC
    n: 266 electrodes across subjects for each PC
  - about: lips against jaw and larynx
    test: Wilcoxon signed-rank test
    p: 0.001
    p_relation: "<"
    corrected: Bonferroni, 6 comparisons per PC
    n: 266 electrodes across subjects for each PC
  - about: jaw against larynx
    test: Wilcoxon signed-rank test
    p: 0.2
    p_relation: ">"
    corrected: Bonferroni, 6 comparisons per PC
    n: 266 electrodes across subjects for each PC
  expected:
  - quantity: electrodes across subjects
    value: 266
    tolerance: 27
  criterion: Methods Eq. 6, PCw_ij = M_ij beta_j, with beta_j the GLM weights of claim
    fig2a-lips-dorsal averaged over each articulator's window (W_jA) for every vSMC electrode
    (OPEN, all 266 electrodes or only the significant ones; the n reads as all), for PCs 1 to
    3; log10 of the absolute value. Paired Wilcoxon signed-rank across electrodes for the six
    articulator pairs, per PC, Bonferroni for 6. Reproduced when, in each PC, tongue > lips at
    p < 0.05, lips > jaw and lips > larynx at p < 0.001, and jaw against larynx p > 0.05 (the
    absence judged on the paper's test); partially reproduced when this holds in one or two of
    the three PCs.
  depends_on:
  - fig2a-lips-dorsal
EOF
python tools/claims_check.py claims/000019/10.1038-nature11911.yaml paper/10.1038-nature11911.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "offset": 118,
 "limit": 12
}
```

```
118	  expected:
119	  - quantity: active vSMC electrodes per subject
120	    value: 30
121	    tolerance: 3
122	  criterion: Per subject, vSMC electrodes whose mean Hg for any CV exceeds a z-score of 2 at any
123	    time in the epoch. OPEN, "change in z-score" read as (a) Hg above 2, (b) absolute Hg above
124	    2 (increase or decrease). Reproduced when, under each baseline reading and one reading of
125	    the change, the mean count over subjects is within 27 to 33; partially reproduced when the
126	    count is within 20 to 40 (the paper says "approximately"). The ~1200 mm2 is not tested, as
127	    the paper does not say how it was measured; the counts per subject are reported.
128	- id: fig1c-e-articulator-electrodes
129	  statement: In one subject, dorsal electrodes (e124, e108) were active for /b/ (lips), mid vSMC
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    the change, the mean count over subjects is within 27 to 33; partially reproduced when the\n    count is within 20 to 40 (the paper says \"approximately\"). The ~1200 mm2 is not tested, as\n    the paper does not say how it was measured; the counts per subject are reported.",
 "new_string": "    the change, the mean count over subjects is within 27 to 33; partially reproduced when the\n    mean is within tolerance under some baseline readings only. The ~1200 mm2 is not tested,\n    as the paper does not say how it was measured; the counts per subject are reported."
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "  quote: We found an overall somatotopic dorsal-ventral arrangement of articulator\n    representations laid out in the following sequence:larynx (X), lips (L), jaw (J), tongue\n    (T), and larynx (X)",
 "new_string": "  quote: \"We found an overall somatotopic dorsal-ventral arrangement of articulator\n    representations laid out in the following sequence: larynx (X), lips (L), jaw (J), tongue\n    (T), and larynx (X)\""
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "  quote: clustering of CV’s in the cortical state-space co-clustered with the major articulators\n    significantly more than expected by chance (Red:observed distribution, median = 0.50,\n    Black:null distribution from 1000 random permutations of articulator assignments of CVs,\n    median = 0.32",
 "new_string": "  quote: \"clustering of CV’s in the cortical state-space co-clustered with the major articulators\n    significantly more than expected by chance (Red: observed distribution, median = 0.50,\n    Black: null distribution from 1000 random permutations of articulator assignments of CVs,\n    median = 0.32\""
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "  quote: For consonants, this analysis confirmed that the primary tier of organization was\n    defined by the major oral articulator features:dorsal, labial, or coronal ( Fig. 4c ) ...\n    during the vowel period, a primary distinction was based upon the presence/absence of\n    lip-rounding (/u/ vs. /a/ & /i/)",
 "new_string": "  quote: \"For consonants, this analysis confirmed that the primary tier of organization was\n    defined by the major oral articulator features: dorsal, labial, or coronal ( Fig. 4c ) ...\n    during the vowel period, a primary distinction was based upon the presence/absence of\n    lip-rounding (/u/ vs. /a/ & /i/)\""
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    variance explained by nine PCs is within tolerance and the inflection the paper reports\n    is seen (the drop from PC 9 to 10 exceeds every later drop... read as the ratio of\n    successive eigenvalues being larger at 9 than the median of later ratios). Values per\n    subject are reported.",
 "new_string": "    variance explained by nine PCs is within tolerance. The paper gives no measure of the\n    inflection at the ninth eigenvalue, so the eigenvalue spectra are shown and not judged.\n    Values per subject are reported."
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
f=claims/000019/10.1038-nature11911.yaml; python3 - <<'EOF'
p='claims/000019/10.1038-nature11911.yaml'
t=open(p).read()
t=t.replace("# - Readings. Where a claim lists readings of a reported number","# - Outside data. The paper relies on none and deposited nothing elsewhere; every claim\n#   uses the dataset alone (data: dataset, the default).\n# - Readings. Where a claim lists readings of a reported number",1)
open(p,'w').write(t)
EOF
grep -n -i "—\|rather" $f; python3 -c "
import yaml;d=yaml.safe_load(open('$f'))
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and ': ' in v: print(c['id'],k)
"; python tools/claims_check.py $f paper/10.1038-nature11911.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml;d=yaml.safe_load(open('claims/000019/10.1038-nature11911.yaml'))
c=d['claims'];print(len(c),sum('criterion' in x for x in c),sum('statistics' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
22 22 11 13
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
?? claims/000019/
?? scripts
```

**Agent**

I wrote `claims/000019/10.1038-nature11911.yaml` with 22 claims. The quote checker passes with 0 problems. Nothing was committed.

**Text read.** The NIH author manuscript from PubMed Central (PMC3606666, NIHMS436351), which is not the version of record. It includes the main text, figure legends and Methods, plus the full supplement: Supplementary Figures 1 to 13 with legends, Supplementary Table 1 and the Supplementary Methods. There was no PDF of the main text, so the main figures were read from their legends and from the Results sentences that cite them. To view supplement pages 2 and 8, I installed PyMuPDF into a temporary directory. The paper links no code.

**Counts.** 22 claims, all with a quote and a criterion. 11 record statistics (17 values), and 13 have expected values with tolerances. Every claim uses the dataset alone; the paper relies on no outside data.

**Details the paper leaves open, with the readings named:**
- **Baseline for the high-gamma z-score:** (a) a silent window before each utterance, (b) statistics of the channel's whole recording.
- **"Change in z-score > 2":** (a) above 2, (b) absolute value above 2.
- **Figure 1 electrodes (e124 and the others):** the subject is unnamed, and the numbering could start from 1 or from 0. The activity measure is either the response at -25 ms or the peak over the epoch.
- **Labial/coronal/dorsal labels for /h/ and /r/:** (a) both left out, (b) /r/ coronal and /h/ dorsal.
- **Supplementary Figure 3 cross-correlations:** normalisation is either Pearson correlation over the overlap or scaling by the zero-shift value. The diagonal is either at 45° or along the anisotropy axis. The map grid is 1 mm, with 0.5 mm as a variant.
- **Supplementary Figure 5:** pairs are formed either within subjects or pooled. The linear-somatotopy null is never described (the legend says "see Methods" and the Methods are silent), so the legend's own bounding values are used.
- **Partial-correlation timing (Fig. 3d):** the threshold is computed either per articulator or over all articulators. Onset and offset are either threshold crossings or half the peak. The ANOVA is either on onsets or on peaks.
- **R² onset latency (Supplementary Figure 7):** either the first significant time or the 2.5 SD rule. The guenon boundary comes from the dataset's anatomical labels.
- **Time range for PCA:** -500 to 750 ms, or -375 to 620 ms.
- **Clusters for separability:** phonetic groups, or k-means at each time. The separability onset is either a 2 bootstrap s.e. rise or half the peak.
- **Feature set paired with separability (Fig. 5d):** constriction location or vowel configuration, or the mean of the feature sets.
- **Consonant–vowel distance pairing:** either the mean of the two cross pairings or i at the consonant time with j at the vowel time.
- **n = 297** is read as 99 time points × 3 subjects; which end point is dropped is open.
- **n = 4623** is read as the syllable pairs within subjects (1596 + 1596 + 1431).
- **Supplementary Figure 9:** whether the electrodes are all 266 or only the significant ones.
- **Smaller gaps:**
  - Fig. 4c–d does not say whether it shows one subject or several, so each subject is run.
  - The paper gives no purity measure for the hierarchy, so I set a two-thirds majority rule. That threshold is my choice, flagged as open in the claim.
  - The filter-bank centres are not given; the cited Mesgarani and Chang (2012) bank is the standard choice.

**Missing or flawed in the paper:**
- The articulator matrix (Supplementary Figure 1d) and the phonetic feature matrix (Supplementary Figure 12) exist only as images. They are cited for the author, not transcribed.
- The Methods cite the wrong supplementary figures in places (Supplemental Figure 6 for the eigenvalues, which are Supplementary Figure 8; Supplemental Figure 9 for the feature matrix, which is Supplementary Figure 12). The claims note this.
- Supplementary Figure 5 prints "P >10-3" although its *** marks mean significance. It is recorded as printed, with a note.
- Fig. 1f–h gives only qualitative examples at unnamed electrodes. Only its /ju/ dorsal-electrode part is judged; the rest is shown, not judged.
- The spatial claims need electrode positions relative to the central sulcus and Sylvian fissure. If the dataset lacks them, those claims are blocked.

## End of run

40 turns, 6 minutes, result: success.
