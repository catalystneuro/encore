# pelot-2020 · claims · run 44219229727

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-16`. Record this version in the attempt's provenance.
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
[... 180 more lines not kept]
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
grep -l "written by an agent" claims/*.yaml | head; grep -rl "sparc" claims/*.yaml | head -3; head -60 tools/claims_check.py; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnins.2020.601479.txt",
 "offset": 30
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnins.2020.601479.txt",
 "offset": 30,
 "limit": 80
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnins.2020.601479.txt",
 "offset": 110
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls papers/datasets/ | grep -i pelot; cat papers/datasets/pelot-2020.yaml 2>/dev/null; grep -rn -i "pelot" --include=*.yaml --include=*.json -l . 2>/dev/null | grep -v transcripts | head
```

```
pelot-2020.yaml
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.3389/fnins.2020.601479
title: Quantified Morphology of the Cervical and Subdiaphragmatic Vagus Nerves of Human, Pig, and Rat
datasets:
- archive: sparc
  id: '60'
  relation: primary
./papers/keys.yaml
./targets/sparc.json
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/sparc.json'))
items=d if isinstance(d,list) else d.get('targets',d)
for t in (items if isinstance(items,list) else items.values()):
  s=json.dumps(t)
  if '\"60\"' in s or 'pelot' in s.lower(): print(json.dumps(t,indent=1)[:3000])
"; head -40 claims/payne-2020.yaml
```

```
{
 "id": "60",
 "name": "Quantified morphology of the rat vagus nerve",
 "url": "https://sparc.science/datasets/60?type=dataset",
 "doi": "10.26275/lg3c-1kjf",
 "published_version": "5",
 "latest": "5",
 "versions": 5,
 "version_dois": [
  "10.26275/lg3c-1kjf",
  "10.26275/ilb9-0e2a",
  "10.26275/bsoi-uash",
  "10.26275/feie-1f8u",
  "10.26275/naiu-etls"
 ],
 "published": "2025-02-24",
 "license": "Creative Commons Attribution",
 "bucket": "sparc-prod-aod-discover-publish50-use1",
 "manifest_version": "7StJiyPYtSBkyV9XnmU0AcrXETX4pUUS",
 "asset_count": 147,
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/sparc.json'))
items=d if isinstance(d,list) else d.get('targets',d)
for t in (items if isinstance(items,list) else items.values()):
  if t.get('id')=='60':
    print({k:v for k,v in t.items() if k!='files'})
"; sed -n 40,80p claims/payne-2020.yaml
```

```
{'id': '60', 'name': 'Quantified morphology of the rat vagus nerve', 'url': 'https://sparc.science/datasets/60?type=dataset', 'doi': '10.26275/lg3c-1kjf', 'published_version': '5', 'latest': '5', 'versions': 5, 'version_dois': ['10.26275/lg3c-1kjf', '10.26275/ilb9-0e2a', '10.26275/bsoi-uash', '10.26275/feie-1f8u', '10.26275/naiu-etls'], 'published': '2025-02-24', 'license': 'Creative Commons Attribution', 'bucket': 'sparc-prod-aod-discover-publish50-use1', 'manifest_version': '7StJiyPYtSBkyV9XnmU0AcrXETX4pUUS', 'asset_count': 147, 'size_gb': 0.2058, 'data_standards': ['SDS', 'TIFF', 'MATLAB', 'JPEG 2000', 'XML', 'Excel', 'MATLAB code', 'text', 'no extension', 'JPEG', 'PDF'], 'sds': {'folders': ['code', 'derivative', 'docs', 'primary', 'protocol'], 'sheets': ['dataset_description', 'samples', 'subjects'], 'folder_manifests': 5}, 'files_listed': 'all', 'readme': True, 'description': "Binary traces from segmentation of cross sections of cervical and subdiaphragmatic rat vagus nerves stained with Masson's trichrome. Quantified effective nerve diameter, effective fascicle diameter, number of fascicles, and perineurium thickness.", 'code': [], 'protocols': ['10.17504/protocols.io.y6hfzb6'], 'contributors': [{'name': 'Nicole Pelot', 'orcid': '0000-0003-2844-0190'}, {'name': 'Gabriel Goldhagen', 'orcid': None}, {'name': 'Jake Cariello', 'orcid': None}, {'name': 'Warren Grill', 'orcid': None}], 'species': [], 'approaches': [], 'keywords': ['autonomic nervous system', 'vagus nerve stimulation', 'neural anatomy', 'vagus nerve morphology'], 'papers': [{'doi': '10.3389/fnins.2020.601479', 'title': 'Quantified Morphology of the Cervical and Subdiaphragmatic Vagus Nerves of Human, Pig, and Rat', 'relation': 'IsDescribedBy', 'resource_type': 'JournalArticle', 'preprint': False, 'pmid': '33250710', 'pmcid': 'PMC7672126'}], 'catalystneuro': []}
#   (3 days, 30 min a day). Sessions of 2 h between day 7 and 18 after surgery, and in 2 rats
#   at 8 weeks. Saline infused at 100 ul/min; b
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:12000])"
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "Pelot" paper/*.txt | grep -i -E "doi|2020[a-g]?\)|sparc|10.26275" | tail -20; sed -n '181,$p' paper/*.txt | grep -i "pelot"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/sparc.json'))
items=d if isinstance(d,list) else d.get('targets',d)
for t in (items if isinstance(items,list) else items.values()):
  c=' '.join(x['name'] for x in t.get('contributors',[]))
  if 'Pelot' in c: print(t['id'],t['doi'],t['name'],'|',[p['doi'] for p in t.get('papers',[])])
"
```

```
60 10.26275/lg3c-1kjf Quantified morphology of the rat vagus nerve | ['10.3389/fnins.2020.601479']
```

**Agent calls Write**

```json
{
 "file_path": "claims/pelot-2020.yaml",
 "content": "# Claims for Pelot, Goldhagen, Cariello, Musselman, Clissold, Ezzell & Grill (2020), \"Quantified\n# Morphology of the Cervical and Subdiaphragmatic Vagus Nerves of Human, Pig, and Rat\", Front.\n# Neurosci. 14, 601479, on SPARC:60.\n#\n# Provenance: written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub\n# Actions\"), 2026-11-18, protocol pilot-16 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read: the version of record, from Europe PMC (PMC7672126, JATS XML flattened;\n# paper/10.3389-fnins.2020.601479.txt), the abstract, Introduction, Materials and Methods,\n# Results, figure legends and Discussion. No PDF was supplied, so no figure was read; Figures\n# 6, 7 and 9 are known here only from their legends and the Results. Three parts are missing\n# from the text read. (1) Eqs. 1 to 4, the perineurium thickness fits, were dropped in the\n# flattening; only their R2 values and fascicle counts survive, so the fit coefficients are\n# not available as expected values. (2) The supplement (Supplements 1 to 6, Supplementary\n# Tables 1 to 6 and Supplementary Figures 13 to 18) is not under paper/; the paper's numbers\n# are all in the main text, but Supplement 4 (literature values) and Supplement 6 (age\n# trends) are what two claims rest on. (3) The reference list is empty, so the identifiers of\n# the SPARC datasets Pelot et al. (2020a to g) are not in the text read.\n#\n# Code read: none. The paper links no code repository. The archive's file listing for SPARC:60\n# shows a code folder of MATLAB scripts; as part of the dataset it was not opened here. The\n# Methods name the tools: NIS-Elements Ar v5.02.01 for segmentation, MATLAB R2018b\n# (bwboundaries, polyarea, fit with linear least squares) for morphometry and fits, JMP Pro\n# 14.3.0 for the mixed model ANOVAs and Tukey's HSD.\n#\n# The dataset. SPARC:60, \"Quantified morphology of the rat vagus nerve\" (doi:10.26275/lg3c-1kjf),\n# described as binary traces from segmentation of Masson's trichrome cross sections of cervical\n# and subdiaphragmatic rat vagus nerves, with quantified effective nerve diameter, effective\n# fascicle diameter, number of fascicles and perineurium thickness. It is the rat part of the\n# paper, most likely Pelot et al. (2020g), which the legends of Figures 6 and 9 cite for the\n# rat morphology. The human data (Pelot et al., 2020a) and the pig data (2020b, IF; 2020d and\n# f, MT) are other SPARC datasets. Claims on rat data alone are `dataset`; claims that compare\n# rat with human or pig need those data as inputs (`with_inputs`); claims on human or pig data\n# alone are `elsewhere`.\n#\n# Data the paper used (Materials and Methods).\n# - Rats. 10 adult Sprague-Dawley rats (Charles River), 5M/5F, 75 to 268 days old, 381 +/- 118 g\n#   (SD), perfused with PBS and 4% paraformaldehyde. 18 cervical samples (both sides, about 6 to\n#   8 mm, excised with the carotid artery) and 9 subdiaphragmatic samples (the whole\n#   subdiaphragmatic esophagus with anterior and posterior trunks, 1.3 to 2.3 cm). R18's\n#   subdiaphragmatic sample was unusual and R26 was collected in its place. Post-fixed 2 to 8\n#   days, paraffin, 5 um sections, MT staining, imaged at 20x.\n# - Rat samples analysed. All 9 left cervical (4F/5M) and all 9 anterior subdiaphragmatic\n#   (4F/5M) samples, segmented manually in NIS-Elements (nerve, outer and inner perineurium).\n#   Cervical, the vagus is the largest nerve in the carotid sheath. Subdiaphragmatic, the\n#   largest fascicle on the anterior esophagus, plus smaller fascicles within about twice its\n#   diameter from its edge and a nerve boundary at the dense to loose connective tissue\n#   transition; but all statistics use the largest fascicle only, with its outer perineurium\n#   boundary as the nerve boundary.\n# - Humans. 30 embalmed cadavers (15M/15F, 54 to 90+ years); 9 left cervical (4F/5M) and 9\n#   anterior subdiaphragmatic (4F/5M) samples, randomly chosen within sex after excluding known\n#   neuropathies; anti-claudin-1 IHC, 10x, semi-automatic segmentation.\n# - Pigs. 12 Yorkshire pigs (3M/9F, 10.5 to 15 weeks); 9 left cervical (6F/3M) and 9 anterior\n#   subdiaphragmatic (3M, 6 of 9 F at random) MT samples (nerve and inner perineurium only); 4\n#   cervical and 4 subdiaphragmatic samples also with anti-fibronectin IF (perineurium).\n# - Measures (Methods, Imaging and Image Analysis, last paragraph). Boundaries by bwboundaries;\n#   area by polyarea; effective diameter, that of the circle of equal area, for nerve and\n#   fascicles; fascicle diameter from the inner perineurium boundary; perineurium thickness,\n#   half the difference of the effective diameters of the outer and inner perineurium\n#   boundaries. Epineurium area is nerve area minus endoneurium and perineurium areas (Figure\n#   7 legend). Fascicle counts count inner perineurium traces (Figure 6 legend).\n# - Statistics (Methods, Statistics and Data Analyses). SDs throughout. Mixed model ANOVAs in\n#   JMP with fixed effects species and level and random effect subject; for fascicle diameter,\n#   log10 of the data and a further random effect of sample; Tukey's HSD post hoc. Number of\n#   fascicles excludes rats. Perineurium fits by MATLAB fit, linear least squares.\n#\n# Inconsistencies in the paper, noted for the author. The Discussion gives the rat ratio of\n# mean subdiaphragmatic to cervical nerve diameter as 0.68, but the Results' means (0.135 and\n# 0.260 mm) give 0.52; the human (0.89 against 0.87) and pig (0.73 against 0.75) ratios agree\n# with their means. The Discussion gives the rat weight as 381 +/- 38 g (SEM), the Methods 381\n# +/- 118 g (SD); these agree for n = 10.\n#\n# Details the paper leaves open, named in the criteria with the readings it allows: the form\n# of the perineurium fits (Eqs. 1 to 3 are missing); which rat fascicles enter the fit and the\n# ratios of endoneurial area and nerve diameter; how \"for a given fascicle diameter\" is\n# compared across species; the test, if any, behind \"did not suggest a difference\" between\n# levels in the perineurium relationship and behind the absence of age trends; how the\n# interaction term and the estimation method of the JMP mixed models are set (the Results\n# report an interaction, so it is in the model; JMP's default REML is a standard choice).\nschema_version: 2\npaper: doi:10.3389/fnins.2020.601479\nclaims:\n- id: rat-sample-set\n  kind: link\n  statement: The dataset holds the rat samples the paper analysed, segmented traces of nine left\n    cervical and nine anterior subdiaphragmatic vagus nerve samples from Sprague-Dawley rats, 4F\n    and 5M at each level, from 10 rats (5M/5F).\n  source: Materials and Methods, Sample Collections, paragraph 1, and Imaging and Image Analysis,\n    paragraph 2\n  quote: We analyzed all left cervical (4F/5M) and anterior subdiaphragmatic (4F/5M) rat VN\n    samples.\n  criterion: Reproduced when the dataset holds segmentations of nine cervical and nine\n    subdiaphragmatic rat samples whose subjects are 4F and 5M at each level, drawn from no more\n    than 10 rats, with subject metadata consistent with the Methods (Sprague-Dawley, 75 to 268\n    days, 381 +/- 118 g over the 10 rats). Partially reproduced when the sample counts match\n    but the metadata differ; not reproduced when the sample counts differ. Extra samples (the\n    right cervical and posterior samples, R18) are reported, not counted against the link.\n- id: nerve-diameter-anova\n  statement: Effective nerve diameter differs across species and across nerve levels, with no\n    detected interaction of species and level.\n  source: Results, paragraph 3\n  quote: The nerve diameter differed across species ( p < 0.0001; F = 577.1) and nerve levels ( p\n    = 0.0030; F = 11.01), but we did not detect an interaction of species and level ( p = 0.1085;\n    F = 2.445).\n  statistics:\n  - about: species\n    test: mixed model ANOVA\n    statistic: F = 577.1\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 cervical and 9 subdiaphragmatic samples per species (human, pig MT, rat)\n  - about: nerve level\n    test: mixed model ANOVA\n    statistic: F = 11.01\n    p: 0.003\n  - about: species by level interaction\n    test: mixed model ANOVA\n    statistic: F = 2.445\n    p: 0.1085\n  data: with_inputs\n  depends_on:\n  - rat-nerve-diameter\n  criterion: As in the Methods (Statistics and Data Analyses), a mixed model ANOVA of effective\n    nerve diameter with fixed effects species, level and their interaction and a random effect\n    of subject, on the 54 samples (rat from the dataset, human from Pelot et al. 2020a, pig MT\n    from Pelot et al. 2020f), REML as the standard estimation choice. Reproduced when species\n    and level have p < 0.05 and the interaction has p >= 0.05 (the absence is judged on this\n    test). Partially reproduced when species and level hold but the interaction is\n    significant. The F values are reported against the paper's.\n- id: human-pig-nerve-diameter-similar\n  statement: Human and pig vagus nerves have similar effective diameters, 1.9 +/- 0.5 against\n    2.2 +/- 0.2 mm cervically and 1.7 +/- 0.3 against 1.6 +/- 0.2 mm subdiaphragmatically, with\n    no significant difference by Tukey's test.\n  source: Results, paragraph 3\n  quote: The human and pig nerves had similar effective diameters (1.9 ± 0.5 vs. 2.2 ± 0.2 mm at\n    the cervical level and 1.7 ± 0.3 vs. 1.6 ± 0.2 mm at the subdiaphragmatic level; p = 0.1830,\n    Tukey's test)\n  statistics:\n  - test: Tukey's test\n    p: 0.183\n    n: 9 human and 9 pig samples per level\n  data: elsewhere\n  where: SPARC Portal, Pelot et al. (2020a) for human and (2020f) for pig MT; identifiers not in\n    the text read\n  expected:\n  - quantity: human cervical effective nerve diameter, mean\n    value: 1.9\n    tolerance: 0.5\n    unit: mm\n  - quantity: pig cervical effective nerve diameter, mean\n    value: 2.2\n    tolerance: 0.2\n    unit: mm\n  - quantity: human subdiaphragmatic effective nerve diameter, mean\n    value: 1.7\n    tolerance: 0.3\n    unit: mm\n  - quantity: pig subdiaphragmatic effective nerve diameter, mean\n    value: 1.6\n    tolerance: 0.2\n    unit: mm\n  criterion: Means within the stated SDs, and the human against pig Tukey comparison from the\n    model of nerve-diameter-anova with p >= 0.05. The paper prints one p for the comparison;\n    it can be read as (a) the species main-effect contrast human against pig or (b) human\n    against pig at each level in the species by level Tukey; the absence holds under either.\n- id: rat-nerve-diameter\n  statement: Rat vagus nerves have effective diameters of 0.260 +/- 0.025 mm at the cervical\n    level and 0.135 +/- 0.015 mm at the subdiaphragmatic level.\n  source: Results, paragraph 3\n  quote: the rat nerves were approximately ten times smaller (0.260 ± 0.025 mm at the cervical\n    level and 0.135 ± 0.015 mm at the subdiaphragmatic level\n  expected:\n  - quantity: rat cervical effective nerve diameter, mean over 9 samples\n    value: 0.26\n    tolerance: 0.025\n    unit: mm\n  - quantity: rat cervical effective nerve diameter, SD\n    value: 0.025\n    tolerance: 0.0025\n    unit: mm\n  - quantity: rat subdiaphragmatic effective nerve diameter, mean over 9 samples\n    value: 0.135\n    tolerance: 0.015\n    unit: mm\n  - quantity: rat subdiaphragmatic effective nerve diameter, SD\n    value: 0.015\n    tolerance: 0.0015\n    unit: mm\n  criterion: Effective diameter is the diameter of the circle of the area within the traced\n    boundary (bwboundaries and polyarea, Methods). Cervical, the nerve boundary of the vagus;\n    subdiaphragmatic, the outer perineurium boundary of the largest fascicle, as the Methods fix\n    for all statistics. Mean tolerances are the paper's SDs; SD tolerances are 10%. Reproduced\n    when both means are within tolerance; the SDs are reported and judged too (partially\n    reproduced when only the means hold). The connective tissue boundary of the three\n    multifascicular samples is shown as a variant.\n- id: rat-ten-times-smaller\n  statement: Rat vagus nerves are about ten times smaller in diameter than human and pig nerves,\n    significantly so at both levels.\n  source: Results, paragraph 3; Discussion, paragraph 3\n  quote: while the rat nerves were approximately ten times smaller (0.260 ± 0.025 mm at the\n    cervical level and 0.135 ± 0.015 mm at the subdiaphragmatic level; p < 0.0001, for both\n    comparisons of rat to larger species)\n  statistics:\n  - test: Tukey's test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 samples per species and level\n  data: with_inputs\n  depends_on:\n  - nerve-diameter-anova\n  criterion: Tukey's HSD after the model of nerve-diameter-anova. Reproduced when rat against\n    human and rat against pig both have p < 0.0001 with rat smaller, and the ratio of the rat\n    mean to each larger species' mean is between 0.05 and 0.2 at each level (a factor of\n    about ten, read as 5 to 20; 0.260/2.2 and 0.135/1.6 from the paper's means give 0.12 and\n    0.08). Partially reproduced when p < 0.05 but not below 0.0001.\n- id: nerve-cervical-larger\n  statement: Cervical vagus nerves are larger than subdiaphragmatic nerves, a trend clearest in\n    pigs and rats.\n  source: Results, paragraph 3\n  quote: The cervical nerves were significantly larger than the subdiaphragmatic nerves;\n    qualitatively, this trend was clearest for the pig and rat nerves.\n  statistics:\n  - test: mixed model ANOVA, level effect\n    statistic: F = 11.01\n    p: 0.003\n  data: with_inputs\n  depends_on:\n  - nerve-diameter-anova\n  criterion: Reproduced when the level effect of nerve-diameter-anova has p < 0.05 with the\n    cervical least squares mean larger, and the relative difference of means (cervical minus\n    subdiaphragmatic over cervical) is larger for pig and for rat than for human. The rat part\n    alone (cervical mean above subdiaphragmatic) is testable on the dataset and is reported\n    apart.\n- id: fascicle-number-human-pig\n  statement: Pig vagus nerves have almost ten times more fascicles than human nerves (47 +/- 10\n    and 38 +/- 7 against 6.7 +/- 4.5 and 4.9 +/- 4.0 at the cervical and subdiaphragmatic\n    levels), the number differs by species and level with no detected interaction, and there\n    are more fascicles cervically.\n  source: Results, paragraph 4\n  quote: The number of fascicles differed across species ( p < 0.0001; F = 213.8) and nerve levels\n    ( p = 0.0300; F = 5.486), but we did not detect an interaction of species and level ( p =\n    0.1322; F = 2.481) ... The pig nerves had almost ten times more fascicles than the human nerves\n    (47 ± 10 at the cervical level and 38 ± 7 at the subdiaphragmatic level for pigs vs. 6.7 ±\n    4.5 and 4.9 ± 4.0 for humans), and there were more fascicles at the cervical level.\n  statistics:\n  - about: species\n    test: mixed model ANOVA\n    statistic: F = 213.8\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 human and 9 pig samples per level\n  - about: nerve level\n    test: mixed model ANOVA\n    statistic: F = 5.486\n    p: 0.03\n  - about: species by level interaction\n    test: mixed model ANOVA\n    statistic: F = 2.481\n    p: 0.1322\n  data: elsewhere\n  where: SPARC Portal, Pelot et al. (2020a) for human and (2020f) for pig MT; identifiers not in\n    the text read\n  expected:\n  - quantity: pig cervical number of fascicles, mean\n    value: 47\n    tolerance: 10\n  - quantity: pig subdiaphragmatic number of fascicles, mean\n    value: 38\n    tolerance: 7\n  - quantity: human cervical number of fascicles, mean\n    value: 6.7\n    tolerance: 4.5\n  - quantity: human subdiaphragmatic number of fascicles, mean\n    value: 4.9\n    tolerance: 4.0\n  criterion: Fascicles counted as inner perineurium traces (Figure 6 legend). Mixed model ANOVA\n    as in the Methods, fixed species, level and interaction, random subject, rats excluded.\n    Reproduced when the means are within the stated SDs, species and level have p < 0.05 and\n    the interaction p >= 0.05.\n- id: rat-subdiaphragmatic-multifascicular\n  statement: Rat vagus nerves are generally monofascicular; three of the nine rat\n    subdiaphragmatic samples (R16-1, R22-1 and R23-1) are multifascicular.\n  source: Figure 6 legend; Results, paragraph 6\n  quote: The three rat samples with asterisks are multifascicular\n  criterion: Count, per rat sample, the fascicles segmented (inner perineurium traces).\n    Reproduced when all nine cervical samples have one fascicle and exactly three\n    subdiaphragmatic samples (R16-1, R22-1, R23-1) have more than one; partially reproduced\n    when three subdiaphragmatic samples are multifascicular but not those three. The counts in\n    those samples are reported (Figure 6, row 3, was not read).\n- id: rat-multifascicular-proportions\n  statement: Counting all segmented fascicles and the surrounding tissue, the epineurium,\n    perineurium and endoneurium proportions are 58.0, 3.8 and 38.2% for R16-1, 55.1, 4.2 and\n    40.7% for R23-1, and 63.4, 3.6 and 33.0% for R22-1.\n  source: Figure 6 legend\n  quote: If the multiple fascicles and surrounding tissue were included, the proportions of\n    epineurium, perineurium, and endoneurium would be ... 58.0, 3.8, and 38.2% for R16-1; 55.1,\n    4.2, and 40.7% for R23-1; 63.4, 3.6, 33.0% for R22-1.\n  depends_on:\n  - rat-subdiaphragmatic-multifascicular\n  expected:\n  - quantity: R16-1 epineurium proportion\n    value: 58.0\n    tolerance: 5.8\n    unit: \"%\"\n  - quantity: R16-1 perineurium proportion\n    value: 3.8\n    tolerance: 0.38\n    unit: \"%\"\n  - quantity: R16-1 endoneurium proportion\n    value: 38.2\n    tolerance: 3.82\n    unit: \"%\"\n  - quantity: R23-1 epineurium proportion\n    value: 55.1\n    tolerance: 5.51\n    unit: \"%\"\n  - quantity: R23-1 perineurium proportion\n    value: 4.2\n    tolerance: 0.42\n    unit: \"%\"\n  - quantity: R23-1 endoneurium proportion\n    value: 40.7\n    tolerance: 4.07\n    unit: \"%\"\n  - quantity: R22-1 epineurium proportion\n    value: 63.4\n    tolerance: 6.34\n    unit: \"%\"\n  - quantity: R22-1 perineurium proportion\n    value: 3.6\n    tolerance: 0.36\n    unit: \"%\"\n  - quantity: R22-1 endoneurium proportion\n    value: 33.0\n    tolerance: 3.3\n    unit: \"%\"\n  criterion: Areas by polyarea within the traces (Methods); endoneurium is the area within all\n    inner perineurium traces, perineurium the area between outer and inner traces, epineurium\n    the nerve (connective tissue boundary) area minus the two (Figure 7 legend). Reproduced when\n    all nine values are within 10%; partially reproduced for six to eight.\n- id: fascicle-diameter-anova\n  statement: Effective fascicle diameter differs across species and nerve levels, with a\n    significant species by level interaction.\n  source: Results, paragraph 5\n  quote: The fascicle diameters differed across species ( p = 0.0015; F = 8.989) and nerve levels\n    ( p < 0.0001; F = 51.88), and there was an interaction of species and level ( p = 0.0121; F =\n    5.273).\n  statistics:\n  - about: species\n    test: mixed model ANOVA on log10 fascicle diameter\n    statistic: F = 8.989\n    p: 0.0015\n  - about: nerve level\n    test: mixed model ANOVA on log10 fascicle diameter\n    statistic: F = 51.88\n    p: 0.0001\n    p_relation: \"<\"\n  - about: species by level interaction\n    test: mixed model ANOVA on log10 fascicle diameter\n    statistic: F = 5.273\n    p: 0.0121\n  data: with_inputs\n  depends_on:\n  - rat-fascicle-diameter\n  criterion: As in the Methods, log10 of every fascicle's effective diameter (inner perineurium\n    boundary), fixed species, level and interaction, random effects of subject and of sample;\n    rats contribute their largest fascicle per sample; human from Pelot et al. 2020a and pig MT\n    from 2020f. Reproduced when all three effects have p < 0.05; partially reproduced when two\n    do.\n- id: rat-fascicle-diameter\n  statement: The largest rat fascicle has an effective diameter of 0.249 +/- 0.024 mm at the\n    cervical level and 0.121 +/- 0.032 mm at the subdiaphragmatic level.\n  source: Results, paragraph 5\n  quote: while rat fascicles (0.249 ± 0.024 mm) were comparable sizes to both human ( p = 0.7270)\n    and pig ( p = 0.1707) fascicles ... rat: 0.121 ± 0.032 mm\n  expected:\n  - quantity: rat cervical effective fascicle diameter, mean over 9 samples\n    value: 0.249\n    tolerance: 0.024\n    unit: mm\n  - quantity: rat subdiaphragmatic effective fascicle diameter, mean over 9 samples\n    value: 0.121\n    tolerance: 0.032\n    unit: mm\n  criterion: The effective diameter of the inner perineurium boundary of the largest fascicle\n    in each sample (Methods). Tolerances are the paper's SDs. Reproduced when both means are\n    within tolerance. The arithmetic mean is taken, as the Results report mean +/- SD; the\n    geometric mean (the analysis is on log10) is shown as a variant.\n- id: cervical-fascicle-diameter-species\n  statement: At the cervical level human fascicles (0.355 +/- 0.226 mm) are larger than pig\n    fascicles (0.155 +/- 0.058 mm), while rat fascicles are comparable to both.\n  source: Results, paragraph 5\n  quote: Comparing across species at the cervical level, the human fascicles (0.355 ± 0.226 mm)\n    were larger than the pig fascicles (0.155 ± 0.058 mm; p = 0.0002), while rat fascicles (0.249\n    ± 0.024 mm) were comparable sizes to both human ( p = 0.7270) and pig ( p = 0.1707)\n    fascicles.\n  statistics:\n  - about: human against pig, cervical\n    test: Tukey's HSD\n    p: 0.0002\n  - about: rat against human, cervical\n    test: Tukey's HSD\n    p: 0.727\n  - about: rat against pig, cervical\n    test: Tukey's HSD\n    p: 0.1707\n  data: with_inputs\n  depends_on:\n  - fascicle-diameter-anova\n  expected:\n  - quantity: human cervical effective fascicle diameter, mean over fascicles\n    value: 0.355\n    tolerance: 0.226\n    unit: mm\n  - quantity: pig cervical effective fascicle diameter, mean over fascicles\n    value: 0.155\n    tolerance: 0.058\n    unit: mm\n  criterion: Tukey's HSD on the species by level groups of the model in fascicle-diameter-anova.\n    Reproduced when human against pig has p < 0.05 with human larger and the two rat\n    comparisons have p >= 0.05 (absence judged on this test), with the means within the stated\n    SDs. The human and pig means are read as means over all fascicles of the nine samples,\n    the Figure 6 legend giving per-sample means separately; the mean of per-sample means is\n    shown as a second reading.\n- id: subdiaphragmatic-fascicle-diameter-comparable\n  statement: At the subdiaphragmatic level fascicle diameters are comparable across species\n    (human 0.163 +/- 0.146, pig 0.110 +/- 0.044, rat 0.121 +/- 0.032 mm), although human\n    fascicles trend larger than pig fascicles.\n  source: Results, paragraph 5\n  quote: At the subdiaphragmatic level, the fascicles diameters were comparable across all species\n    (human - 0.163 ± 0.146 mm\n  statistics:\n  - about: human against pig, subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.3049\n  - about: human against rat, subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.896\n  - about: pig against rat, subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.9947\n  data: with_inputs\n  depends_on:\n  - fascicle-diameter-anova\n  expected:\n  - quantity: human subdiaphragmatic effective fascicle diameter, mean over fascicles\n    value: 0.163\n    tolerance: 0.146\n    unit: mm\n  - quantity: pig subdiaphragmatic effective fascicle diameter, mean over fascicles\n    value: 0.11\n    tolerance: 0.044\n    unit: mm\n  criterion: A claim of absence, judged on the paper's test, Tukey's HSD on the species by level\n    groups of the model in fascicle-diameter-anova. Reproduced when none of the three\n    subdiaphragmatic species pairs has p < 0.05 and the means are within the stated SDs; not\n    reproduced when any pair differs. Effect sizes are reported either way.\n- id: fascicles-larger-cervical\n  statement: All three species have larger fascicles at the cervical than at the\n    subdiaphragmatic level.\n  source: Results, paragraph 5\n  quote: All species had larger fascicles at the cervical level ( p < 0.0001 for humans; p =\n    0.0009 for pigs; p = 0.0234 for rats).\n  statistics:\n  - about: humans, cervical against subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.0001\n    p_relation: \"<\"\n  - about: pigs, cervical against subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.0009\n  - about: rats, cervical against subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.0234\n  data: with_inputs\n  depends_on:\n  - fascicle-diameter-anova\n  criterion: Tukey's HSD on the species by level groups of the model in fascicle-diameter-anova.\n    Reproduced when each species has cervical larger with p < 0.05; partially reproduced for\n    two species. The rat comparison is the one the dataset bears on; a rat-only mixed model of\n    log10 largest-fascicle diameter on level with random subject is shown as a variant.\n- id: rat-diameter-like-fascicle\n  statement: The monofascicular rat nerves have diameters close to that of a single human or pig\n    fascicle.\n  source: Results, paragraph 6\n  quote: The monofascicular rat nerves were ∼10× smaller, and their diameters approximated the\n    diameter of a single human or pig fascicle.\n  data: with_inputs\n  depends_on:\n  - rat-nerve-diameter\n  - cervical-fascicle-diameter-species\n  - subdiaphragmatic-fascicle-diameter-comparable\n  criterion: The paper fixes no measure. Readings (a) at each level the rat mean nerve diameter\n    lies between the pig and the human mean fascicle diameters (from the paper's means, 0.260\n    between 0.155 and 0.355 mm, and 0.135 between 0.110 and 0.163 mm); (b) at each level the rat\n    mean nerve diameter lies within the range of the human and pig fascicle diameters.\n    Reproduced when either reading holds at both levels.\n- id: human-pig-tissue-proportions\n  statement: Endoneurium is a larger share of the human nerve cervically (32 +/- 7.9%) than\n    subdiaphragmatically (8.8 +/- 5.3%), while in pigs it is more even across levels (27 +/- 5.3%\n    and 20 +/- 4.0%, MT); perineurium follows the same trends (human 8.9 +/- 2.5% and 3.4 +/-\n    1.6%, pig 5.1 +/- 1.8% and 4.0 +/- 0.5%).\n  source: Results, paragraph 7\n  quote: The human endoneurium occupied a larger proportion of the nerve at the cervical level (32\n    ± 7.9%) than at the subdiaphragmatic level (8.8 ± 5.3%) whereas the endoneurial proportions\n    were more consistent across levels in pigs, slightly lower than in the human cervical VN (27\n    ± 5.3% at the cervical level and 20 ± 4.0% at the subdiaphragmatic level for the MT\n    micrographs ... These same trends between species and levels were present for the proportion\n    of perineurium (8.9 ± 2.5% and 3.4 ± 1.6% at the cervical and subdiaphragmatic levels in\n    humans; 5.1 ± 1.8% and 4.0 ± 0.5% in pigs).\n  data: elsewhere\n  where: SPARC Portal, Pelot et al. (2020a) for human, (2020f) for pig MT and (2020b) for pig\n    IF; identifiers not in the text read\n  expected:\n  - quantity: human cervical endoneurium proportion\n    value: 32\n    tolerance: 7.9\n    unit: \"%\"\n  - quantity: human subdiaphragmatic endoneurium proportion\n    value: 8.8\n    tolerance: 5.3\n    unit: \"%\"\n  - quantity: pig cervical endoneurium proportion, MT\n    value: 27\n    tolerance: 5.3\n    unit: \"%\"\n  - quantity: pig subdiaphragmatic endoneurium proportion, MT\n    value: 20\n    tolerance: 4.0\n    unit: \"%\"\n  - quantity: human cervical perineurium proportion\n    value: 8.9\n    tolerance: 2.5\n    unit: \"%\"\n  - quantity: human subdiaphragmatic perineurium proportion\n    value: 3.4\n    tolerance: 1.6\n    unit: \"%\"\n  - quantity: pig cervical perineurium proportion\n    value: 5.1\n    tolerance: 1.8\n    unit: \"%\"\n  - quantity: pig subdiaphragmatic perineurium proportion\n    value: 4.0\n    tolerance: 0.5\n    unit: \"%\"\n  criterion: Proportions are tissue area over nerve area, mean over samples. The pig perineurium\n    can only come from the IF micrographs (MT has no perineurium segmented), so it is read as\n    the IF value. Reproduced when every value is within its stated SD.\n- id: rat-level-ratios\n  statement: In rats the ratio of mean subdiaphragmatic to mean cervical endoneurial area is 0.32\n    and the ratio of mean nerve diameters is 0.68.\n  source: Discussion, paragraph 3\n  quote: The ratios of the mean endoneurial area of the subdiaphragmatic VN to the cervical VN were\n    0.20, 0.42, and 0.32 for human, pig, and rat, respectively ... where the ratios of the mean\n    diameter of the subdiaphragmatic VN to the cervical VN were 0.87, 0.75, and 0.68 for human,\n    pig, and rat, respectively.\n  depends_on:\n  - rat-nerve-diameter\n  expected:\n  - quantity: rat ratio of mean endoneurial area, subdiaphragmatic over cervical\n    value: 0.32\n    tolerance: 0.032\n  - quantity: rat ratio of mean effective nerve diameter, subdiaphragmatic over cervical\n    value: 0.68\n    tolerance: 0.068\n  criterion: The paper does not say which rat subdiaphragmatic tissue enters these ratios, and\n    its own Results means give a diameter ratio of 0.52 (0.135/0.260), not 0.68. Readings (a)\n    the largest fascicle only, as in all statistics (nerve boundary its outer perineurium); (b)\n    for the three multifascicular samples, all segmented fascicles for endoneurial area and the\n    connective tissue boundary for nerve diameter (Figure 6 legend). Each ratio is reproduced\n    when within 10% under either reading; the claim is reproduced when both are, partially when\n    one is. The 0.52 from the Results means is reported.\n- id: human-pig-level-ratios\n  statement: The ratio of mean subdiaphragmatic to mean cervical endoneurial area is 0.20 in\n    humans and 0.42 in pigs, and the ratio of mean nerve diameters is 0.87 and 0.75.\n  source: Discussion, paragraph 3\n  quote: The ratios of the mean endoneurial area of the subdiaphragmatic VN to the cervical VN were\n    0.20, 0.42, and 0.32 for human, pig, and rat, respectively\n  data: elsewhere\n  where: SPARC Portal, Pelot et al. (2020a) for human and (2020f) for pig MT; identifiers not in\n    the text read\n  expected:\n  - quantity: human ratio of mean endoneurial area\n    value: 0.2\n    tolerance: 0.02\n  - quantity: pig ratio of mean endoneurial area\n    value: 0.42\n    tolerance: 0.042\n  - quantity: human ratio of mean effective nerve diameter\n    value: 0.87\n    tolerance: 0.087\n  - quantity: pig ratio of mean effective nerve diameter\n    value: 0.75\n    tolerance: 0.075\n- id: human-variability\n  statement: Nerve and fascicle diameters are more consistent across samples in pigs (and rats)\n    than in humans.\n  source: Results, paragraph 7; Discussion, paragraph 2\n  quote: Qualitatively, the nerve and fascicle diameters were more consistent across samples for\n    the pig nerves than for the humans nerves ( Figure 6 )\n  data: with_inputs\n  criterion: The paper judges this qualitatively from Figure 6. Readings (a) the coefficient of\n    variation across samples of effective nerve diameter and of per-sample mean fascicle\n    diameter; (b) the SDs reported in the Results relative to the means. Reproduced when, at\n    both levels, the human value exceeds the pig value for both measures under either reading;\n    the rat values are reported against the Discussion's statement that pig and rat ranges were\n    more consistent than human.\n- id: literature-comparison-human-pig\n  statement: Human cervical fascicle numbers and endoneurial areas match prior reports while the\n    nerve areas and diameters are generally smaller; human subdiaphragmatic sizes match prior\n    reports; pig fascicle numbers match literature, with slightly smaller mean diameters.\n  source: Results, paragraph 8; Discussion, paragraph 4\n  quote: The numbers of fascicles and endoneurial cross-sectional areas of the human cervical VNs\n    were comparable to previous reports, but the nerve cross-sectional areas and effective\n    diameters were generally smaller, albeit with overlapping ranges.\n  data: elsewhere\n  where: SPARC Portal, Pelot et al. (2020a, 2020f); literature values in Supplement 4 (not in the\n    text read)\n  criterion: Judged as Figure 7 shows it, the paper's mean +/- SD against each literature mean.\n    The Discussion gives the literature human cervical diameter as 3.0 mm (left and right,\n    three studies) and 2.0 mm (Stakenborg et al., 2020); reproduced when the human cervical mean\n    nerve diameter is below 3.0 mm and its range overlaps 3.0 mm. The other parts need the\n    literature values of Supplement 4, which was not supplied, and are not decidable from the\n    text read.\n- id: rat-literature-comparison\n  statement: Rat cervical nerve diameters and areas agree with published data, while the rat\n    subdiaphragmatic nerves are slightly larger than prior data.\n  source: Results, paragraph 8; Discussion, paragraph 6\n  quote: The nerve diameters and cross-sectional areas of the rat cervical VNs compared well to\n    published data, while our rat subdiaphragmatic nerves were slightly larger than prior data\n  data: with_inputs\n  depends_on:\n  - rat-nerve-diameter\n  criterion: The literature values are in Supplement 4 and Figure 7 (Fazan and Lachat, 1997;\n    Licursi de Alcântara et al., 2008, cervical; Prechtl and Powley, 1985, subdiaphragmatic),\n    none of them in the text read. With those values as inputs, reproduced when each published\n    cervical mean lies within the rat cervical mean +/- SD and the rat subdiaphragmatic mean\n    exceeds each published subdiaphragmatic mean. Without them the claim cannot be decided.\n- id: perineurium-species-order\n  statement: For a given fascicle diameter, human fascicles have the thickest perineurium and\n    rat fascicles the thinnest.\n  source: Results, paragraph 10; Figure 8; Figure 9A\n  quote: For a given fascicle diameter, the human samples had the thickest perineurium while the\n    rat samples had the thinnest perineurium.\n  data: with_inputs\n  depends_on:\n  - rat-perineurium-fit\n  criterion: Perineurium thickness is half the difference of the outer and inner effective\n    diameters; non-peanut fascicles only (Figure 9 legend); human IHC (Pelot et al. 2020a), pig\n    IF (2020b), rat MT (dataset). The paper does not say how \"for a given diameter\" is compared.\n    Readings (a) each species' fit (fit form as in rat-perineurium-fit) evaluated across the\n    diameters common to all three species; (b) the fits evaluated at 250 um, the size of the\n    Figure 8 examples. Reproduced when human > pig > rat under either reading (over the whole\n    common range for a).\n- id: perineurium-ratio-decreases\n  statement: The ratio of perineurium thickness to fascicle diameter decreases as fascicle\n    diameter increases, particularly in humans and pigs.\n  source: Results, paragraph 10; Figure 9B\n  quote: The ratio of perineurium thickness to fascicle diameter decreased with increased fascicle\n    diameter, particularly for the human and pig samples ( Figure 9B ).\n  data: with_inputs\n  criterion: The paper shows this in Figure 9B without a test. Readings (a) the ratio implied by\n    each species' fit (rat-perineurium-fit) decreases over the species' range of diameters; (b)\n    Spearman correlation of the ratio with diameter is negative. Reproduced when human and pig\n    show the decrease under either reading; the rat result, of which the paper claims less, is\n    reported and not required.\n- id: human-perineurium-fit\n  statement: The fit of perineurium thickness against fascicle diameter for 73 human non-peanut\n    fascicles has R2 = 0.75.\n  source: Results, paragraphs 10 and 11 (Eq. 1)\n  quote: We fit the data from 73 human fascicles (excluding fascicles with more than one inner\n    perineurium trace for a given outer perineurium trace, i.e., peanut fascicles) as ... with d\n    fasc in microns, yielding R 2 = 0.75.\n  data: elsewhere\n  where: SPARC Portal, Pelot et al. (2020a); identifier not in the text read\n  expected:\n  - quantity: number of human non-peanut fascicles fitted\n    value: 73\n    tolerance: 0\n  - quantity: R2 of the human fit\n    value: 0.75\n    tolerance: 0.075\n  criterion: As for rat-perineurium-fit, with the same fit-form readings. The count tolerance is\n    0, as it is a count of traces. Eq. 1's coefficients are missing from the text read.\n- id: pig-perineurium-fit\n  statement: The fit of perineurium thickness against fascicle diameter for 284 pig non-peanut\n    fascicles (IF) has R2 = 0.30.\n  source: Results, paragraphs 11 and 12 (Eq. 2)\n  quote: We fit the data from 284 pig non-peanut fascicles as ... with d fasc in microns, yielding\n    R 2 = 0.30.\n  data: elsewhere\n  where: SPARC Portal, Pelot et al. (2020b); identifier not in the text read\n  expected:\n  - quantity: number of pig non-peanut fascicles fitted\n    value: 284\n    tolerance: 0\n  - quantity: R2 of the pig fit\n    value: 0.3\n    tolerance: 0.03\n  criterion: As for rat-perineurium-fit, with the same fit-form readings. Eq. 2's coefficients\n    are missing from the text read.\n- id: rat-perineurium-fit\n  statement: The fit of perineurium thickness against fascicle diameter for 22 rat fascicles has\n    R2 = 0.77.\n  source: Results, paragraphs 12 and 13 (Eq. 3)\n  quote: We fit the data from 22 rat fascicles as ... with d fasc in microns, yielding R 2 = 0.77.\n  expected:\n  - quantity: number of rat fascicles fitted\n    value: 22\n    tolerance: 0\n  - quantity: R2 of the rat fit\n    value: 0.77\n    tolerance: 0.077\n  criterion: Per rat fascicle with an inner and an outer perineurium trace, effective fascicle\n    diameter (inner boundary, um) and thickness, half the outer minus inner effective diameter\n    (Methods). Fit by linear least squares (MATLAB fit, Methods). Two details are open, as Eq. 3\n    is missing from the text read. The fascicle set, read as (a) every segmented rat fascicle,\n    including the smaller ones of the multifascicular subdiaphragmatic samples, or (b) the 18\n    largest fascicles only; 22 fascicles across 18 samples points to (a). The fit form, read as\n    (i) thickness linear in diameter with an intercept, which the paper's \"also ... with a\n    linear equation with forced zero intercept\" for Eq. 4 suggests, (ii) linear through zero,\n    or (iii) another model linear in its coefficients (a power law fitted in log space is\n    excluded, as the Methods name linear least squares on the data). Reproduced when, under\n    one combination, the count is 22 and R2 is within tolerance; partially reproduced when the\n    count matches and R2 is outside. The coefficients are reported for comparison with Eq. 3\n    once it is read from the PDF.\n- id: perineurium-no-level-difference\n  statement: The relationship between perineurium thickness and fascicle diameter does not\n    differ between cervical and subdiaphragmatic nerves in any of the three species.\n  source: Results, paragraph 13\n  quote: The data did not suggest a difference in the relationship between perineurium thickness\n    and fascicle diameter for cervical versus subdiaphragmatic nerves for any of the three\n    species.\n  data: with_inputs\n  depends_on:\n  - rat-perineurium-fit\n  criterion: A claim of absence for which the paper names no test, so the paper's own method is\n    used. Per species, the fit of rat-perineurium-fit fitted separately to cervical and to\n    subdiaphragmatic fascicles. Readings (a) the 95% confidence bounds of each coefficient (as\n    MATLAB fit reports them) overlap between levels; (b) an F-test of a level term (intercept\n    and slope by level) in the pooled linear model at p < 0.05. Reproduced when no species shows\n    a difference under reading (a); reading (b) is shown as a variant, and any species where\n    the two disagree is recorded. The rat part is testable on the dataset alone.\n- id: sunderland-reanalysis\n  statement: Refitting all 777 fascicles of Sunderland and Bradley (1952) gives a zero-intercept\n    slope of 2.75% of fascicle diameter for perineurium thickness, with R2 = 0.51.\n  source: Results, paragraphs 13 and 14 (Eq. 4); Discussion, paragraph 7; Figure 9C and 9D\n  quote: We re-analyzed the original ( Sunderland and Bradley, 1952 ) data, including all 777\n    fascicles ... and identified the slope of the best-fit line with zero intercept as 2.75% ( R 2\n    = 0.51)\n  data: elsewhere\n  where: Sunderland and Bradley (1952), the published human somatic nerve fascicle measurements;\n    no archive identifier\n  expected:\n  - quantity: slope of zero-intercept fit, perineurium thickness over fascicle diameter\n    value: 2.75\n    tolerance: 0.275\n    unit: \"%\"\n  - quantity: R2 of the fit\n    value: 0.51\n    tolerance: 0.051\n  - quantity: fascicles fitted\n    value: 777\n    tolerance: 0\n- id: rat-perineurium-near-3-percent\n  statement: Rat perineurium thickness is close to the published 3% of fascicle diameter,\n    slightly thicker for smaller fascicles and thinner for larger ones.\n  source: Discussion, paragraph 7; Figure 9A and 9B\n  quote: While we found that the rat perineurium thickness was similar to this published\n    relationship, albeit slightly thicker for smaller fascicle diameters and thinner for larger\n    fascicle diameters\n  depends_on:\n  - rat-perineurium-fit\n  criterion: The comparison line is thickness = 3% of fascicle diameter (Figure 9 legend,\n    Grinberg et al., 2008); \"this published relationship\" can also be read as the 2.75% slope\n    of the re-analysis, so both are run. With the rat fit of rat-perineurium-fit, reproduced\n    when the fitted thickness over thickness of the reference line is between 0.5 and 2 across\n    the rat diameter range (similar, read as within a factor of two, a choice of this file), and\n    the fit lies above the line at the smallest rat diameter and below it at the largest\n    (one crossing). Partially reproduced when the rat data are within the factor but do not\n    cross the line.\n- id: human-pig-perineurium-thicker\n  statement: Human and pig vagal perineurium is substantially thicker than the 3% of fascicle\n    diameter found for human somatic nerves, especially for smaller fascicles.\n  source: Discussion, paragraph 7; Figure 9B\n  quote: the human and pig perineurium was substantially thicker, especially for smaller fascicles\n    ( Figure 9B )\n  data: elsewhere\n  where: SPARC Portal, Pelot et al. (2020a) for human and (2020b) for pig IF; identifiers not in\n    the text read\n  criterion: For non-peanut fascicles, the ratio of thickness to diameter. Reproduced when, for\n    both species, the median ratio exceeds 0.03 and the ratio's excess over 0.03 is larger for\n    fascicles below the species' median diameter than above it.\n- id: pig-if-mt-consistent\n  statement: Pig fascicle diameters from anti-fibronectin IF (14 to 303 um, mean 123, median 123,\n    interquartile range 91 to 155 um) are consistent with those from MT (5 to 399 um, mean 135,\n    median 130, interquartile range 96 to 168 um).\n  source: Results, paragraph 12\n  quote: Note that the fascicle diameters for the pig anti-fibronectin IF ( Figures 9A,B ; 14 to\n    303 μm, mean = 123 μm, median = 123 μm, interquartile range = 91 to 155 μm) are consistent\n    with the MT data ( Figure 6 ; 5 to 399 μm, mean = 135 μm, median = 130 μm, interquartile\n    range = 96 to 168 μm).\n  data: elsewhere\n  where: SPARC Portal, Pelot et al. (2020b) for pig IF and (2020f) for pig MT; identifiers not\n    in the text read\n  expected:\n  - quantity: pig IF fascicle diameter, mean\n    value: 123\n    tolerance: 12.3\n    unit: um\n  - quantity: pig IF fascicle diameter, median\n    value: 123\n    tolerance: 12.3\n    unit: um\n  - quantity: pig MT fascicle diameter, mean\n    value: 135\n    tolerance: 13.5\n    unit: um\n  - quantity: pig MT fascicle diameter, median\n    value: 130\n    tolerance: 13\n    unit: um\n  criterion: The IF values are over the 284 non-peanut fascicles of Figure 9A and B. Reproduced\n    when the four values are within 10% and the ranges and interquartile ranges are within the\n    reported ones widened by 10% of each bound.\n- id: peanut-fascicle-counts\n  statement: Human IHC micrographs have 60 cervical inner perineurium traces (27 bundles in 10\n    peanut fascicles) and 44 subdiaphragmatic (4 in 2); pig IF micrographs have 210 cervical (57\n    in 25) and 179 subdiaphragmatic (48 in 19).\n  source: Figure 9 legend\n  quote: For the human anti-claudin-1 IHC micrographs, the cervical level had 60 fascicles total\n    (inner perineurium traces) of which 27 were intrafascicular bundles in 10 peanut fascicles;\n    the subdiaphragmatic level had 44 fascicles total (inner perineurium traces) of which 4 were\n    intrafascicular bundles in 2 peanut fascicles.\n  data: elsewhere\n  where: SPARC Portal, Pelot et al. (2020a) for human and (2020b) for pig IF; identifiers not in\n    the text read\n  expected:\n  - quantity: human cervical inner perineurium traces\n    value: 60\n    tolerance: 0\n  - quantity: human subdiaphragmatic inner perineurium traces\n    value: 44\n    tolerance: 0\n  - quantity: pig IF cervical inner perineurium traces\n    value: 210\n    tolerance: 0\n  - quantity: pig IF subdiaphragmatic inner perineurium traces\n    value: 179\n    tolerance: 0\n  criterion: Counts of traces, tolerance 0. Reproduced when the four totals and the peanut\n    counts (27 in 10, 4 in 2, 57 in 25, 48 in 19) match. A check that 60 - 27 + 4 ... the\n    non-peanut counts (33 + 40 = 73 human; 153 + 131 = 284 pig) match the fit counts is\n    reported.\n- id: no-age-trend\n  statement: The morphology metrics show no trend with age in any species.\n  source: Discussion, paragraph 5 (Supplement 6)\n  quote: Our morphology metrics did not show trends with age for any species ( Supplement 6 )\n  data: with_inputs\n  criterion: A claim of absence whose test, if any, is in Supplement 6, which was not supplied.\n    Until it is read, the readings are (a) Pearson correlation of each per-sample metric\n    (nerve diameter, number of fascicles, mean fascicle diameter, tissue proportions) with\n    subject age at p < 0.05 per species and level; (b) the same with Spearman correlation. The\n    rat part needs only the dataset's subject ages. Reproduced when no metric shows a trend\n    under reading (a), (b) shown as a variant; the claim rests on an assumption until\n    Supplement 6 fixes the method.\n- id: rat-carotid-sheath-bundles\n  statement: The rat cervical carotid sheath holds up to six fascicles, of which the largest,\n    taken as the vagus, was segmented.\n  source: Discussion, paragraph 6 (Supplementary Figure 16)\n  quote: The rat cervical VN was identified as monofascicular in prior studies ( Fazan and Lachat,\n    1997 ; Licursi de Alcântara et al., 2008 ), but we observed up to six fascicles within the\n    carotid sheath ( Supplementary Figure 16 ).\n  criterion: Testable only if the dataset holds the cervical micrographs or traces of the other\n    bundles in the sheath. Reproduced when the largest cervical bundle per sample is the one\n    segmented as the vagus and no sample has more than six bundles, with at least one sample\n    having more than one. Not testable when only the vagus is traced.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/pelot-2020.yaml",
 "old_string": "    counts (27 in 10, 4 in 2, 57 in 25, 48 in 19) match. A check that 60 - 27 + 4 ... the\n    non-peanut counts (33 + 40 = 73 human; 153 + 131 = 284 pig) match the fit counts is\n    reported.",
 "new_string": "    counts (27 in 10, 4 in 2, 57 in 25, 48 in 19) match. Whether the non-peanut counts (60 -\n    27 + 44 - 4 = 73 human; 210 - 57 + 179 - 48 = 284 pig) match the fit counts is reported."
}
```

```
The file claims/pelot-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/pelot-2020.yaml",
 "old_string": "  quote: At the subdiaphragmatic level, the fascicles diameters were comparable across all species\n    (human - 0.163 ± 0.146 mm",
 "new_string": "  quote: At the subdiaphragmatic level, the fascicles diameters were comparable across all species\n    ... although the human fascicles trended larger than the pig fascicles."
}
```

```
The file claims/pelot-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/pelot-2020.yaml paper/10.3389-fnins.2020.601479.txt; grep -nP "[^\"']: |—|rather" claims/pelot-2020.yaml | grep -v "^[0-9]*:#" | grep -vP "^\d+:\s*(- )?[a-z_]+: " | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/pelot-2020.yaml",
 "old_string": "    and pig ( p = 0.1707) fascicles ... rat: 0.121 ± 0.032 mm",
 "new_string": "    and pig ( p = 0.1707) fascicles ... 0.121 ± 0.032 mm"
}
```

```
The file claims/pelot-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/pelot-2020.yaml paper/10.3389-fnins.2020.601479.txt 2>&1 | tail -30; grep -n "—\|rather" claims/pelot-2020.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/pelot-2020.yaml'))
c=d['claims'];from collections import Counter
print(len(c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c),Counter(x.get('data','dataset') for x in c),Counter(x.get('kind','finding') for x in c))"
```

```
34 9 21 32 16 Counter({'with_inputs': 14, 'elsewhere': 11, 'dataset': 9}) Counter({'finding': 33, 'link': 1})
```

**Agent**

I wrote `claims/pelot-2020.yaml`. The quote checker passes: 34 claims, 34 quotes, 21 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC7672126, flattened JATS XML). That covers the abstract, Introduction, Methods, Results, figure legends and Discussion. No PDF was supplied, so I read no figure. The paper links no code. The archive's file list shows a MATLAB `code` folder inside SPARC:60, but it belongs to the dataset, so I did not open it.

**Contents:**
- **Claims:** 34 in total, all with quotes. That is 33 findings and 1 link check that the dataset holds the 9 + 9 rat samples.
- **Statistics:** 9 claims carry 21 entries. These are the mixed-model ANOVA F and p values for nerve diameter, fascicle number and fascicle diameter, and the Tukey HSD p values.
- **Criteria and expected values:** 32 claims have criteria and 16 have expected values. Tolerances are the paper's SDs for means, 10% otherwise, and 0 for counts.
- **Data:** 9 claims test the rat dataset alone. 14 combine rat with the human or pig data (`with_inputs`). 11 rest on human or pig data only (`elsewhere`).

**Details the paper leaves open, and the readings named:**
- **Form of the perineurium fit (Eq. 3):** a straight line with an intercept, a line through zero, or another model fitted by linear least squares.
- **Which rat fascicles are fitted:** all 22 segmented fascicles, or only the 18 largest.
- **Rat ratios of subdiaphragmatic to cervical size (0.32 for endoneurial area, 0.68 for diameter):** the largest fascicle only, or all fascicles plus the connective-tissue boundary in the three multifascicular samples.
- **"Thickest/thinnest perineurium for a given diameter":** the fits compared over the diameters all three species share, or at 250 µm (the size of the Figure 8 examples).
- **Ratio of perineurium thickness to diameter falling with diameter:** the slope implied by the fit, or the sign of a Spearman correlation.
- **No difference between levels in the perineurium relationship (no test named):** overlap of the fit coefficients' confidence bounds, or an F-test of a level term.
- **No age trend (its test is in Supplement 6):** Pearson or Spearman correlation with age.
- **The single human vs pig Tukey p:** the species main-effect contrast, or the comparison at each level.
- **Mean fascicle diameter:** the mean over all fascicles, or the mean of per-sample means. For rats, the arithmetic or geometric mean.
- **"Similar to 3%" for rat perineurium:** the 3% line, or the paper's 2.75% re-fit. I set "within a factor of two" myself, and the file says so.
- **Variability:** the coefficient of variation, or the reported SDs.

**Missing from the paper as supplied:**
- **Eqs. 1 to 4:** dropped in the flattening, so the fit coefficients are not available as expected values. Only R² and the fascicle counts are.
- **The whole supplement:**
  - Supplement 4 holds the literature values that the rat literature-comparison claim needs; that claim can't be decided without it.
  - Supplement 6 fixes the age-trend test.
- **The reference list is empty:** the SPARC identifiers of the human and pig datasets (Pelot et al. 2020a to f) can't be pinned. The `where` fields cite them by name only.

**An inconsistency noted in the file:** the rat diameter ratio of 0.68 in the Discussion does not follow from the Results' means, which give 0.135/0.260 = 0.52.

## End of run

23 turns, 6 minutes, $1.77 at API prices, result: success.
