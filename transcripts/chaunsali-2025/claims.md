# 001702 · claims · run 39573740196

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001702 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d712f599-ac00-453e-8340-e79177bace41/tool-results/bk6xlmywv.txt; sed -n 25,200p $f
```

```
# pmc.ncbi.nlm.nih.gov).
schema_version: 2
dataset:
  archive: dandi
  id: "001453"
paper: doi:10.1016/j.cub.2025.04.027
claims:
- id: stimulus-code-link
  kind: link
  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using
    the paper's analysis code and the protocol file of its stimulus software, and the values
    computed through that link agree with those the paper's code printed.
  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
  data: with_labels
  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
[... 156 more lines not kept]
```

**Agent calls Bash**

```bash
f=/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d712f599-ac00-453e-8340-e79177bace41/tool-results/bk6xlmywv.txt; grep -n "^[a-z]" $f; grep -n "inferred\|elsewhere\|where:" $f | head; ls claims | head -50; cat tools/claims_check.py | head -80
```

```
<persisted-output>
Output too large (69.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d712f599-ac00-453e-8340-e79177bace41/tool-results/b0inkkgty.txt

Preview (first 2KB):
26:schema_version: 2
27:dataset:
30:paper: doi:10.1016/j.cub.2025.04.027
31:claims:
336:https://creativecommons.org/licenses/by/4.0/
340:journal=Medical Clinics&title=The Alzheimer's disease clinical spectrum: diagnosis and management&author=A Atri&volume=103&issue=2&publication_year=2019&pages=263-293&pmid=30704681&doi=10.1016/j.mcna.2018.10.009&
344:journal=Alzheimer's & dementia&title=The diagnosis of dementia due to Alzheimer's disease: recommendations from the National Institute on Aging‐Alzheimer's Association workgroups on diagnostic guidelines for Alzheimer's disease&author=GM McKhann&author=DS Knopman&author=H Chertkow&volume=7&issue=3&publication_year=2011&pages=263-269&pmid=21514250&doi=10.1016/j.jalz.2011.03.005&
345:http://10.3389/fnins.2023.1188065
349:journal=Front Neurosci&title=Matrix disequilibrium in Alzheimer's disease and conditions that increase Alzheimer's disease risk&author=M Amontree&author=S Deasy&author=RS Turner&author=K Conant&volume=17&publication_year=2023&pages=1188065&pmid=37304012&doi=10.3389/fnins.2023.1188065&
350:journal=Journal fur Psychologie und Neurologie&title=Studies on the structure of the cerebral cortex XI Continuation of the study of the ammonic system&author=RL De Nó&volume=46&publication_year=1934&pages=113-177&
351:http://10.1038/nn.3614
355:journal=Nat Neurosci&title=Cell type‐specific genetic and optogenetic tools reveal hippocampal CA2 circuits&author=K Kohara&author=M Pignatelli&author=AJ Rivest&volume=17&issue=2&publication_year=2014&pages=269-279&pmid=24336151&doi=10.1038/nn.3614&
356:http://10.1002/hipo.23509
360:journal=Hippocampus&title=Morphological and molecular markers of mouse area CA2 along the proximodistal and dorsoventral hippocampal axes&author=D Radzicki&a
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l -c paper/*.txt; sed -n 300,335p claims/001453/*.yaml | head -5; grep -n "^checks\|^  - \|inferred" claims/001453/*.yaml | head -20; sed -n 1,60p tools/claims_check.py
```

Result: not kept, because it reads the paper's text.

**Agent**

Now reading the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1002-alz.70813.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1002-alz.70813.txt').read()
print(t[50000:94000])"
```

```
<persisted-output>
Output too large (42.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d712f599-ac00-453e-8340-e79177bace41/tool-results/bo44uddtu.txt

Preview (first 2KB):
) from 6 M 5XFAD mice injected with vehicle (top), or GM6001 (2nd from top), and 6 M Control (5XFAD‐) mice injected with vehicle (3rd from top) or GM6001 (bottom). Scale 50 µm. (I) Bar graphs showing significantly higher CA2 PNN expression in GM6001‐treated mice compared to vehicle‐treated 5XFAD mice whereas age‐matched GM6001‐treated or vehicle‐treated controls exhibited PNN expression comparable to 6 M GM6001‐treated 5XFAD mice (one‐way ANOVA, Tukey's multiple comparisons test; n = 4–5 mice per group; * p < 0.05, ** p < 0.01). We injected 100 mg/kg/day (i.p.) GM6001, which was previously shown to be effective in blocking MMP activity in glioma‐associated epilepsy 29 and stroke. 37 Our behavior study included two groups: 5XFAD mice treated with GM6001 or vehicle. Following 1 M of treatment when mice turned 6 M old, we assessed social behavior in 5XFAD mice treated with vehicle and GM6001. 5XFAD mice treated with vehicle showed altered social memory behavior; however, the GM6001‐treated 5XFAD mice exhibited normal social behavior, with a significant difference in the difference score compared to vehicle‐treated 5XFAD mice (Figure 5E–G ). Besides normal social behavior, the IHC analysis of GM6001‐treated mice brains exhibited significantly higher CA2 PNN expression compared to vehicle‐treated 5XFAD mice (Figure 5H,I ). We also included age‐matched controls treated with GM6001 or vehicle for IHC analysis. Age‐matched controls treated with GM6001 or vehicle exhibited PNN expression comparable to GM6001‐treated 5XFAD mice, indicating GM6001 had no significant effect on control mice (Figure 5H,I ). In addition, the control mice treated with GM6001 and vehicle showed comparable PNN expression (Figure 5H,I ). These findings suggest
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d712f599-ac00-453e-8340-e79177bace41/tool-results/bo44uddtu.txt"
}
```

```
1	) from 6 M 5XFAD mice injected with vehicle (top), or GM6001 (2nd from top), and 6 M Control (5XFAD‐) mice injected with vehicle (3rd from top) or GM6001 (bottom). Scale 50 µm. (I) Bar graphs showing significantly higher CA2 PNN expression in GM6001‐treated mice compared to vehicle‐treated 5XFAD mice whereas age‐matched GM6001‐treated or vehicle‐treated controls exhibited PNN expression comparable to 6 M GM6001‐treated 5XFAD mice (one‐way ANOVA, Tukey's multiple comparisons test; n = 4–5 mice per group; * p < 0.05, ** p < 0.01). We injected 100 mg/kg/day (i.p.) GM6001, which was previously shown to be effective in blocking MMP activity in glioma‐associated epilepsy 29 and stroke. 37 Our behavior study included two groups: 5XFAD mice treated with GM6001 or vehicle. Following 1 M of treatment when mice turned 6 M old, we assessed social behavior in 5XFAD mice treated with vehicle and GM6001. 5XFAD mice treated with vehicle showed altered social memory behavior; however, the GM6001‐treated 5XFAD mice exhibited normal social behavior, with a significant difference in the difference score compared to vehicle‐treated 5XFAD mice (Figure 5E–G ). Besides normal social behavior, the IHC analysis of GM6001‐treated mice brains exhibited significantly higher CA2 PNN expression compared to vehicle‐treated 5XFAD mice (Figure 5H,I ). We also included age‐matched controls treated with GM6001 or vehicle for IHC analysis. Age‐matched controls treated with GM6001 or vehicle exhibited PNN expression comparable to GM6001‐treated 5XFAD mice, indicating GM6001 had no significant effect on control mice (Figure 5H,I ). In addition, the control mice treated with GM6001 and vehicle showed comparable PNN expression (Figure 5H,I ). These findings suggest that blocking MMP activity before the onset of PNN disruption in 5XFAD mice can prevent PNN degradation and consequently avert the loss of social memory. 4. DISCUSSION Recent studies provide compelling evidence of a progressive loss of PNNs in
[... 338 more lines not kept]
```

**Agent calls Bash**

```bash
cd ..; grep -n -i "supplement" docs/pilot-notes.md | head -30; ls paper/; grep -rl -i "supplement.*missing\|missing.*supplement" claims transcripts 2>/dev/null | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1245,1260p docs/pilot-notes.md; sed -n 1660,1670p docs/pilot-notes.md; sed -n 2610,2620p docs/pilot-notes.md; sed -n 3455,3470p docs/pilot-notes.md; head -30 claims/001746/*.yaml
```

```
states and movement to define WAKE; and in 14 sessions the state labels
agree best with the spikes when shifted 5 to 60 s earlier, while the LFP
agrees with the spikes to within 50 ms in 14 of 21 sessions, three others
have a clear extreme 56 to 64 ms from zero lag, and in three agreement is
not established.

The author's points on the protocol: "open access" is not defined, and a
free-to-read author manuscript was taken as full text; no rule for a main
text available without its supplement, whose claims were blocked as
`methods_underspecified` though that reason is defined for a procedure
neither the paper nor its code fixes; no guidance on looking for code when
none is linked (the author read the conversion code, which explained both
corrupt files); a clock check by decoding shifted labels that is coarse for
states lasting minutes and does not apply to LFP; no guidance on a label the
paper uses and the dandiset lacks, or on corruption of single sessions; the
10% tolerance for correlations that depend on binning the paper does not
documentation that the paper does not rely on; a stated spread across
neurons used as the tolerance of a mean; values given by layer with no layer
known for each rat; three criteria written after a timing run printed
connection counts; a Methods test that cannot reach significance, which the
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn "001702" --include=*.yaml --include=*.json --include=*.md --include=*.csv . 2>/dev/null | grep -v transcripts | head
```

```
./targets/dandisets.json:6968:   "dandiset": "001702",
./papers/manifest.yaml:2084:  '001702':
```

**Agent calls Bash**

```bash
sed -n 6960,7010p targets/dandisets.json; sed -n 2080,2100p papers/manifest.yaml
```

```
"preprint": true
    }
   ],
   "catalystneuro": [
    "contributor Adkisson-Floro, Paul of CatalystNeuro"
   ]
  },
  {
   "dandiset": "001702",
   "name": "Hippocampal CA2 Perineuronal Net Degradation and Social Memory Deficits in a 5XFAD Alzheimer\u2019s Disease Mouse Model",
   "published_version": "0.260216.2323",
   "asset_count": 656,
   "size_gb": 13.35,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Mus musculus - House mouse"
   ],
   "approaches": [],
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001702/versions/0.260216.2323/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'));print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | python3 -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:6000])"
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
python3 -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"
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
 "file_path": "claims/001702/10.1002-alz.70813.yaml",
 "content": "# Claims for Chaunsali, Li, Fleischel et al. (2025), \"Degradation of perineuronal nets in\n# hippocampal CA2 explains the loss of social cognition memory in Alzheimer's disease\",\n# Alzheimer's & Dementia 21, e70813, doi:10.1002/alz.70813, on dandiset 001702 (\"Hippocampal CA2\n# Perineuronal Net Degradation and Social Memory Deficits in a 5XFAD Alzheimer's Disease Mouse\n# Model\").\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol as stated in docs/protocol.md (version pilot-10).\n#\n# Text read: the version of record, open access, as served by Europe PMC (PMC12541281), stored\n# under paper/: main text, Methods, figure legends of Figures 1 to 5, Data Availability. No PDF\n# was available, so the asterisks in the figures (which comparison has which p level) could not\n# be read; where a legend lists several levels, the claims record the bound the legend allows\n# for the comparison. The article has a correction (Alzheimers Dement 2026, e71098) that was not\n# in the text read. The Supporting Information was not in the text read: Figures S1 to S9,\n# Table S1 (reagents), Tables S2 and S3 (means, SEM, n, test statistics and post hoc results\n# of every test) and Table S4 (the RNA-seq analysis). The main findings rest on the main\n# figures and are stated in the main text, so claims were written. Claims on the supplementary\n# figures quote the main text that cites them; their legends, tests and sample sizes are not\n# known here, and each says so. No exact p-value or test statistic is printed in the text read.\n#\n# Code: the paper links no code. Analyses were run in GraphPad Prism 9 (statistics), ImageJ\n# (images) and R 4.4.1 with DESeq2 1.44.0 and GOplot (RNA-seq). Data Availability says data\n# \"will be provided upon reasonable request\". The dandiset's description (not the paper) says it\n# holds immunohistochemical images quantifying CA2 PNNs, behavioral assay results and bulk\n# RNA-seq data with metadata, and that the transcriptomic data are also deposited in GEO under\n# GSE317499. The paper names no outside data; every claim is `data: dataset`, and whether the\n# RNA-seq counts are in the dandiset or only in GEO is the author's to find.\n#\n# Data the paper used.\n# Mice: 5XFAD (congenic on C57Bl/6J) and age-matched WT littermates (5XFAD-, \"control\"); J20\n# and 3XTg (Figure S4); Acan fl/fl and Acan wt/wt (WT) mice injected with AAV9 hSyn eGFP-Cre\n# into CA2; C57Bl/6J mice injected into CA2 with ChABC, heat-inactivated ChABC or penicillinase\n# (PNase, the sham control); 5XFAD and control mice injected daily i.p. for 1 month (from 5 M)\n# with GM6001 (100 mg/kg) or vehicle (4% CMC). IHC used both sexes; behavior used males only.\n# - IHC (Figure 1): coronal 50 um sections, WFA (PNNs), PCP4 (CA2 neurons), NeuN, PV. CA2 PNN\n#   area coverage (WFA area / PCP4 area inside a rotated rectangle covering all PCP4 neurons of\n#   CA2) and WFA intensity in that rectangle, for 5XFAD and controls at 3, 6, 9 and 12 M; n is\n#   slices (7 to 12 per group) from five mice per group. PV density (PV cells per PCP4 volume,\n#   ~20 um z-stacks) and NeuN density (NeuN cells per PCP4 area) at 3 and 6 M, 8 to 10 slices\n#   from five mice per group.\n# - Direct social interaction (Figures 2, 3, 5): three trials 1 h apart in a 35 cm open field\n#   (Novel 1, then the same mouse as Familiar, then Novel 2); the measure is the test mouse's\n#   interaction time with the other mouse in each trial; difference scores Novel 1 - Familiar\n#   and Familiar - Novel 2 per mouse. Groups (n mice): 3 M control 7, 5XFAD 9 (Fig 2B-D); 6 M\n#   control 10, 5XFAD 9 (Fig 2E-G); WT AAV Cre 10, Acan AAV Cre 10 (Fig 3C-E); PNase 8, ChABC 10\n#   at 5 and 14 days post injection (Fig 3H-M); 5 M control 7, 5XFAD 11 (Fig 5B-D); 6 M 5XFAD +\n#   GM6001 14, 5XFAD + vehicle 12 (Fig 5E-G). The trial length is not stated.\n# - Novel object recognition at 6 M (Figure 2I-K): 10 min familiarization with two identical\n#   objects, 30 min delay, 10 min test with one object replaced; time exploring each object\n#   (Ethovision XT), percent time, discrimination index (N - F) / (N + F); distance moved.\n#   n = 11 control, 17 5XFAD (2I, 2J); 17 control, 22 5XFAD (2K).\n# - GM6001 IHC (Figure 5I): CA2 PNN expression in 6 M 5XFAD + vehicle, 5XFAD + GM6001,\n#   control + vehicle, control + GM6001, n = 4 to 5 mice per group.\n# - Bulk RNA-seq (Figure 4): 1 mm punches of CA2 from 500 um acute slices of 3 M and 7 M 5XFAD\n#   and control mice; Illumina NovaSeq poly-A, STAR to mm39, featureCounts, DESeq2. The number of\n#   mice per group is not given in the text read (Table S4).\n#\n# Shared definitions used in the criteria (all from the Methods 2.6, 2.8 and 2.10 and the\n# legends, except where named open):\n# - SOCIAL: per mouse, the interaction time in each of the three trials as the Methods define\n#   it (nose-to-nose, nose-tail and anogenital sniffing, allogrooming, and following initiated\n#   by the test mouse). Open: the trial length, which the Methods do not state; the reading is\n#   the whole trial as the dataset records or scores it. No mouse is excluded (\"No data were\n#   excluded\", Methods 2.10).\n# - TRIALS-ANOVA: a two-way ANOVA of interaction time on group and trial (Novel 1, Familiar,\n#   Novel 2) with Tukey's multiple comparisons, as each legend names it. Open, where a legend\n#   says only \"two-way ANOVA\" (Figures 3C, 3H, 3K, 5B, 5E), whether trial is a repeated measure;\n#   Figure 2B and 2E name \"two-way repeated measures ANOVA\" for the same design. Readings (a)\n#   repeated measures on trial, (b) ordinary two-way ANOVA. Open in all panels, which means\n#   Tukey's test compares (Prism allows both): readings (i) the three trials within each group,\n#   (ii) all six group by trial cells. Each claim is judged under every combination.\n# - INTACT memory in a group: Familiar below Novel 1 and Novel 2 above Familiar, each with\n#   Tukey p < 0.05. IMPAIRED: neither of these two comparisons has p < 0.05.\n# - DIFF: the two difference scores per mouse, compared between groups by a two-tailed unpaired\n#   t-test (legends). Open, the sign of the second score: the legends label it Familiar - Novel\n#   2, which is negative with intact memory, while the Results call the scores of impaired mice\n#   \"lower\". The two-tailed test does not depend on the sign; the direction is judged as which\n#   group's score lies further from zero on the side of intact memory (Novel 1 above Familiar,\n#   Novel 2 above Familiar).\n# - PNN-AREA and PNN-INTENSITY: the measures of Methods 2.8. When the dataset holds the\n#   per-slice values, they are used as given. From images, the binary masks come from ImageJ\n#   auto thresholds; open, which of the two named (\"OTSU or Triangle\"); readings (a) Otsu,\n#   (b) Triangle, for every channel. PNN-AREA is WFA mask area / PCP4 mask area inside the CA2\n#   rectangle. PNN-INTENSITY is open between (a) the mean WFA intensity inside the WFA mask\n#   (\"intensity of the WFA-covered area\") and (b) the mean WFA intensity over the CA2 rectangle\n#   (\"WFA intensity within the CA2 area rectangle\"); both phrases are in Methods 2.8.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001702\"\npaper: doi:10.1002/alz.70813\nclaims:\n- id: fig1g-3m-pnn-area-no-difference\n  statement: At 3 M, CA2 PNN area coverage does not differ between 5XFAD and control mice.\n  source: Results 3.1, paragraph 2; Figure 1C and 1G\n  quote: At 3 M, CA2 PNNs were indistinguishable between 5XFAD and controls\n  criterion: A claim of absence, judged on the paper's test. PNN-AREA per slice (unit is the\n    slice, as the legend's n), 5XFAD and control at 3, 6, 9 and 12 M, in a two-way ANOVA on\n    genotype and age with Tukey's multiple comparisons (Figure 1 legend). Reproduced when the\n    Tukey comparison of 5XFAD against control at 3 M has p >= 0.05; not reproduced when p <\n    0.05. The mean difference and its p are reported, under each threshold reading.\n- id: fig1g-pnn-area-reduced-6-to-12m\n  statement: CA2 PNN area coverage is significantly lower in 5XFAD than in age-matched control\n    mice at 6 M, and stays lower at 9 and 12 M.\n  source: Results 3.1, paragraph 2; Figure 1D to 1G\n  quote: at 6 M, we observed a significant reduction in CA2 PNN area in the 5XFAD mice ... This\n    decrease in the PNN coverage persisted in the 9 and 12 M old 5XFAD\n  statistics:\n  - test: two-way ANOVA, Tukey's multiple comparisons test\n    p: 0.05\n    p_relation: \"<\"\n    n: 9 to 12 slices from five mice per group at 6, 9 and 12 M\n  criterion: PNN-AREA per slice, two-way ANOVA on genotype and age with Tukey's multiple\n    comparisons (Figure 1 legend). Reproduced when, at each of 6, 9 and 12 M, 5XFAD is below\n    control with Tukey p < 0.05 under a threshold reading; partially reproduced when this holds\n    at one or two of the three ages. The legend lists levels from p < 0.05 to p < 0.0001\n    without the figure, so p < 0.05 is the bound recorded.\n- id: fig1h-wfa-intensity-reduced-6-to-12m\n  statement: WFA intensity in CA2 is significantly lower in 5XFAD than in control mice at 6 to\n    12 M.\n  source: Results 3.1, paragraph 2; Figure 1H\n  quote: we computed WFA intensity in the CA2 area which was similarly reduced significantly at\n    6-12 M in 5XFAD mice\n  statistics:\n  - test: two-way ANOVA, Tukey's multiple comparisons test\n    p: 0.05\n    p_relation: \"<\"\n    n: 9 to 12 slices from five mice per group at 6, 9 and 12 M\n  criterion: PNN-INTENSITY per slice, two-way ANOVA on genotype and age with Tukey's multiple\n    comparisons (Figure 1 legend), under each intensity and threshold reading. Reproduced when,\n    under one reading, 5XFAD is below control with Tukey p < 0.05 at each of 6, 9 and 12 M;\n    partially reproduced when at one or two of these ages. If the readings give different\n    outcomes the claim is methods_underspecified, with every result shown. The 3 M comparison\n    is reported as well.\n- id: fig1gh-aging-reduction-smaller-than-5xfad\n  statement: Normal aging also reduces CA2 PNN coverage in control mice, but the loss is\n    significantly more pronounced in 5XFAD mice.\n  source: Results 3.1, paragraph 2; Figure 1G and 1H\n  quote: Note that normal aging also presented with a reduction in PNN coverage, yet the loss of\n    PNNs was significantly more pronounced in 5XFAD mice\n  statistics:\n  - test: two-way ANOVA, Tukey's multiple comparisons test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: PNN-AREA per slice, two-way ANOVA on genotype and age with Tukey's multiple\n    comparisons over all eight cells (Figure 1 legend). The paper does not say which\n    comparisons show the aging effect; the reading the legend allows is control at 3 M\n    against control at 9 or 12 M. Reproduced when control at 3 M is above control at 12 M or 9\n    M with Tukey p < 0.05, and at each of 6, 9 and 12 M the 5XFAD loss relative to its 3 M\n    group is larger than the control's loss relative to control at 3 M, with the genotype by\n    age interaction at p < 0.05. Partially reproduced when the aging decline holds and the\n    5XFAD loss is larger but the interaction is not significant. The same is reported for\n    PNN-INTENSITY.\n- id: fig1a-pv-pnns-intense-in-5xfad\n  statement: In 6 M 5XFAD mice, the PNNs around PV neurons in CA2 remain relatively intense,\n    while those around CA2 pyramidal neurons are lost.\n  source: Results 3.1, paragraph 1; Figure 1A to 1D\n  quote: however we observed relatively intense PV neuron-associated PNNs in 5XFAD mice\n  criterion: The paper reports no measure or test for this observation. With the Methods'\n    default for two groups (two-tailed unpaired t-test, Methods 2.10), the mean WFA intensity\n    around PV-positive cells in CA2 is compared between 6 M 5XFAD and control. Open, how the\n    region around a PV cell is drawn, as the paper says the PNNs of pyramidal and PV neurons\n    could not be separated; readings (a) a ring of 2 um outside the PV cell outline, (b) the\n    WFA mask overlapping the PV cell outline. Reproduced when, under a reading, the 5XFAD mean\n    is not below the control mean by the t-test at p < 0.05 while PNN-AREA at 6 M is lower in\n    5XFAD (claim fig1g-pnn-area-reduced-6-to-12m). If the dataset holds no PV channel at 6 M,\n    the claim is blocked.\n  depends_on:\n  - fig1g-pnn-area-reduced-6-to-12m\n- id: fig1b-loss-of-wfa-peaks\n  statement: Along the periphery of a single CA2 pyramidal neuron, the WFA line profile shows\n    many high-intensity peaks in control and loses this peak and valley pattern in 5XFAD.\n  source: Figure 1B\n  quote: showing many high-intensity WFA peaks in control (dark magenta line) compared to the\n    5XFAD (light magenta line) group\n  criterion: The paper shows one example neuron per group and defines no peak measure or test.\n    Testable only if the dataset holds the high magnification images or line profiles of\n    Figure 1B. Open, what counts as a peak; readings (a) local maxima whose prominence exceeds\n    10% of the control profile's intensity range, (b) the same at 25%. Reproduced when, under\n    both readings, the control profile has more peaks than the 5XFAD profile and a higher\n    maximum intensity. Otherwise blocked as methods_underspecified.\n- id: fig1i-pv-density-unchanged\n  statement: PV neuron density in CA2 does not differ between 5XFAD and control mice at 3 or 6\n    M.\n  source: Results 3.1, paragraph 5; Figure 1I\n  quote: We did not find any change in either PV ... or NeuN cell density at 6 M of 5XFAD\n    compared to age-matched controls\n  statistics:\n  - test: unpaired two-tailed t-test\n    p: 0.05\n    p_relation: \">\"\n    n: 8 to 10 brain slices from five mice per group\n  criterion: A claim of absence, judged on the paper's test. PV cells counted in ~20 um\n    z-stacks divided by the PCP4-covered CA2 volume, per slice (Methods 2.8); 5XFAD against\n    control by a two-tailed unpaired t-test at each age (Figure 1 legend). Reproduced when p >=\n    0.05 at both 3 and 6 M; not reproduced when either has p < 0.05. The difference and p are\n    reported for each age.\n- id: fig1j-neun-density-unchanged\n  statement: NeuN neuron density in CA2 does not differ between 5XFAD and control mice at 3 or\n    6 M, so PNN loss precedes neuronal loss.\n  source: Results 3.1, paragraph 5; Figure 1J\n  quote: showing no difference between any groups\n  statistics:\n  - test: unpaired two-tailed t-test\n    p: 0.05\n    p_relation: \">\"\n    n: 8 to 10 brain slices from five mice per group\n  criterion: A claim of absence, judged on the paper's test. NeuN cells in single-plane images\n    counted inside the PCP4-covered CA2 ROI and divided by its area, per slice (Methods 2.8);\n    5XFAD against control by a two-tailed unpaired t-test at each age (Figure 1 legend).\n    Reproduced when p >= 0.05 at both 3 and 6 M; not reproduced when either has p < 0.05.\n- id: figs2-pcp4-unchanged\n  statement: PCP4 expression in CA2 is unaltered in 5XFAD mice at all ages studied, which is\n    why it serves as the internal control for PNN area.\n  source: Methods 2.8; Figure S2 (not in the text read)\n  quote: The expression of PCP4 remained unaltered in all studied age groups\n  criterion: A claim of absence. The Figure S2 legend was not read, so the paper's measure and\n    test are not known. Readings the text allows, (a) PCP4 mask area in the CA2 rectangle per\n    slice, two-way ANOVA on genotype and age with Tukey's comparisons as for Figure 1G, (b) the\n    same measure, two-tailed unpaired t-test of 5XFAD against control at each age (Methods 2.10\n    default for two groups). Reproduced when no 5XFAD against control comparison has p < 0.05\n    under either reading; not reproduced when one does under both; if the readings disagree,\n    methods_underspecified with both shown.\n- id: figs3-other-regions-subtle\n  statement: Outside CA2, the PNNs in other brain regions of 6 M 5XFAD mice show only subtle\n    changes.\n  source: Results 3.1, paragraph 1; Discussion, paragraph 2; Figure S3 (not in the text read)\n  quote: Although subtle changes in PNN expression were visible in some brain regions\n  criterion: The Figure S3 legend was not read, so its regions, measure and test are not known.\n    Testable only if the dataset holds WFA images or values for regions outside CA2 at 6 M.\n    With the Methods 2.8 measures and the Methods 2.10 default test (two-tailed unpaired\n    t-test), reproduced when, in each region the dataset labels, the relative 5XFAD against\n    control difference in PNN-INTENSITY is smaller in size than in CA2 of the same mice.\n    Otherwise blocked.\n- id: figs4-ca2-pnn-loss-j20-3xtg\n  statement: CA2 PNNs are also conspicuously lost in two other AD models, J20 and 3XTg.\n  source: Results 3.1, paragraph 1; Figure S4A to S4C (not in the text read)\n  quote: we assessed two more widely used AD models namely J20 and 3XTg, which also showed a\n    conspicuous loss of PNN in CA2 area\n  criterion: The Figure S4 legend was not read, so the ages, sample sizes and test are not\n    known. PNN-AREA and PNN-INTENSITY per slice, each model against its controls by a\n    two-tailed unpaired t-test (Methods 2.10 default for two groups). Reproduced when both\n    models are lower than their controls at p < 0.05 on at least one of the two measures;\n    partially reproduced when one model is. Blocked if the dataset holds no J20 or 3XTg data.\n- id: figs5-aggrecan-unchanged\n  statement: Aggrecan expression in CA2 at 6 M is unaltered in 5XFAD mice, suggesting that the\n    loss of WFA-labelled PNNs reflects a loss of chondroitin sulfate chains.\n  source: Results 3.1, paragraph 3; Figure S5A and S5B (not in the text read)\n  quote: Aggrecan expression in CA2 at 6 M remains unaltered in 5XFAD mice\n  criterion: A claim of absence. The Figure S5 legend was not read. The text allows, for the\n    measure, (a) aggrecan mask area / PCP4 area and (b) aggrecan intensity in the CA2\n    rectangle (the Methods 2.8 measures applied to the aggrecan channel), and for the test the\n    Methods 2.10 default for two groups, a two-tailed unpaired t-test, on slices. Reproduced\n    when 5XFAD against control has p >= 0.05 under both readings; not reproduced when p < 0.05\n    under both; methods_underspecified if they disagree.\n- id: figs6-ca2-devoid-of-plaques\n  statement: Despite widespread amyloid beta plaques in the hippocampus of 5XFAD mice, the CA2\n    area is largely devoid of plaques.\n  source: Results 3.1, paragraph 4; Figure S6A to S6C (not in the text read)\n  quote: despite a widespread hippocampal deposition of amyloid beta plaques ... the CA2 area\n    remained largely devoid of amyloid beta plaques\n  criterion: The Figure S6 legend was not read, so the measure is not known. Readings, (a)\n    amyloid beta mask area fraction, (b) plaque count per area, in CA2 (the PCP4 rectangle)\n    against the rest of the hippocampus in the same 5XFAD sections. Reproduced when, under\n    both readings, CA2 is below the rest of the hippocampus in every 5XFAD section imaged with\n    an amyloid stain; blocked if the dataset holds no amyloid stain.\n- id: fig2b-3m-intact-social-memory\n  statement: At 3 M, both 5XFAD and control mice have normal social memory, spending less time\n    with the familiar mouse than with Novel 1 and more time with Novel 2.\n  source: Results 3.2, paragraph 3; Figure 2B\n  quote: We found that the 3 M old 5XFAD mice with intact PNNs behave identically to control\n    mice, spending less time with the familiar mouse and more time with the novel mouse\n  statistics:\n  - test: two-way repeated measures ANOVA, Tukey's multiple comparisons test\n    p: 0.05\n    p_relation: \"<\"\n    n: 7 control and 9 5XFAD mice\n  criterion: SOCIAL and TRIALS-ANOVA with repeated measures on trial (the legend names it),\n    under Tukey readings (i) and (ii). Reproduced when both groups show INTACT memory under a\n    reading; partially reproduced when both comparisons go in the INTACT direction in both\n    groups but only two or three of the four reach p < 0.05.\n- id: fig2cd-3m-difference-scores-no-difference\n  statement: At 3 M, the difference scores (Novel 1 - Familiar and Familiar - Novel 2) do not\n    differ between 5XFAD and control mice.\n  source: Results 3.2, paragraph 3; Figure 2C and 2D\n  quote: with no significant difference in the difference scores between the groups\n  criterion: A claim of absence, judged on the paper's test. DIFF, two-tailed unpaired t-test\n    for each score (n = 7 control, 9 5XFAD). Reproduced when both scores have p >= 0.05; not\n    reproduced when either has p < 0.05. Group means and p are reported.\n- id: fig2e-6m-impaired-social-memory\n  statement: At 6 M, control mice show intact social memory, while 5XFAD mice show no\n    difference in interaction time between Novel 1 and Familiar, nor between Familiar and\n    Novel 2.\n  source: Results 3.2, paragraph 3; Figure 2E\n  quote: Specifically, unlike age-matched controls, 5XFAD mice showed no difference in\n    investigation times between the first novel mouse and the familiar mouse, nor between the\n    familiar mouse and the second novel mouse\n  statistics:\n  - test: two-way repeated measures ANOVA, Tukey's multiple comparisons test\n    p: 0.05\n    p_relation: \"<\"\n    n: 10 control and 9 5XFAD mice\n  criterion: SOCIAL and TRIALS-ANOVA with repeated measures on trial (legend), Tukey readings\n    (i) and (ii). Reproduced when, under a reading, controls show INTACT memory and 5XFAD show\n    IMPAIRED memory; partially reproduced when controls are INTACT and 5XFAD have one of the\n    two comparisons at p < 0.05; not reproduced otherwise. The 5XFAD part is a claim of absence\n    and is judged on this test as written.\n- id: fig2fg-6m-difference-scores-lower\n  statement: At 6 M, both difference scores show weaker discrimination of familiar and novel\n    mice in 5XFAD than in control mice.\n  source: Results 3.2, paragraph 3; Figure 2F and 2G\n  quote: However, the lower difference scores in 5XFAD mice indicate a diminished ability to\n    distinguish between familiar and novel mice\n  statistics:\n  - about: Novel 1 - Familiar (Figure 2F)\n    test: unpaired two-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 10 control and 9 5XFAD mice\n  - about: Familiar - Novel 2 (Figure 2G)\n    test: unpaired two-tailed t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 10 control and 9 5XFAD mice\n  criterion: DIFF. Reproduced when both scores differ at p < 0.05 by the two-tailed unpaired\n    t-test with the control score further from zero on the side of intact memory; partially\n    reproduced when one does.\n- id: figs7-nor-training-no-side-preference\n  statement: During the training phase of the object recognition test, neither control nor\n    5XFAD mice prefer the right or the left object.\n  source: Results 3.2, paragraph 4; Figure S7 (not in the text read)\n  quote: During the training phase both control and 5XFAD mice did not show any preference\n    toward right or left object\n  criterion: A claim of absence. The Figure S7 legend was not read, so the paper's test is not\n    known. Readings, on percent time with each object in the 10 min familiarization phase, (a)\n    two-way mixed-effects ANOVA on genotype and side with Sidak's comparisons of left against\n    right within genotype, as the paper used for the test phase (Figure 2I), (b) a two-tailed\n    paired t-test of left against right within each genotype. Reproduced when no comparison has\n    p < 0.05 under either reading; not reproduced when one does under both;\n    methods_underspecified if they disagree.\n- id: fig2i-nor-novel-object-preference\n  statement: At 6 M, both control and 5XFAD mice spend significantly more time with the novel\n    object than with the familiar one.\n  source: Results 3.2, paragraph 4; Figure 2I\n  quote: Bar graph showing significantly higher time spent with the novel object compared to\n    familiar by both 6 M control and 5XFAD\n  statistics:\n  - test: two-way ANOVA mixed-effects, Sidak's multiple comparisons\n    p: 0.01\n    p_relation: \"<\"\n    n: 11 control and 17 5XFAD mice\n  criterion: Percent of object exploration time with the novel and the familiar object in the\n    10 min test phase (Methods 2.6.2), a two-way mixed-effects ANOVA on genotype and object\n    (object within mouse) with Sidak's comparisons of novel against familiar within each\n    genotype (legend). Reproduced when novel exceeds familiar with p < 0.05 in both genotypes;\n    partially reproduced when in one.\n- id: fig2j-nor-discrimination-index-no-difference\n  statement: The novel object discrimination index does not differ between 6 M control and\n    5XFAD mice.\n  source: Results 3.2, paragraph 4; Figure 2J\n  quote: with no significant differences in the discrimination index between the groups\n  criterion: A claim of absence, judged on the paper's test. Discrimination index (novel -\n    familiar) / (novel + familiar) exploration time in the test phase (Methods 2.6.2),\n    two-tailed unpaired t-test (n = 11 control, 17 5XFAD). Reproduced when p >= 0.05; not\n    reproduced when p < 0.05. Means and p are reported.\n- id: fig2k-distance-moved-no-difference\n  statement: Total distance moved does not differ between 6 M control and 5XFAD mice, so the\n    social memory deficit is not due to a change in locomotion.\n  source: Results 3.2, paragraph 5; Figure 2K\n  quote: We measured the total travel distance in 6-M-old 5XFAD and control mice and found no\n    significant difference between these groups\n  criterion: A claim of absence, judged on the paper's test, a two-tailed unpaired t-test (n =\n    17 control, 22 5XFAD). Open, in which session distance was measured, as the text does not\n    say and n differs from Figure 2J; readings (a) the 10 min habituation in the open field,\n    (b) the 10 min familiarization phase, (c) the 10 min test phase, each as the dataset holds\n    it. Reproduced when p >= 0.05 under the readings the dataset allows; not reproduced when p\n    < 0.05 under all; methods_underspecified if they disagree.\n- id: figs8-baseline-social-memory-before-injection\n  statement: Before AAV Cre injection, Acan fl/fl and WT mice both have normal social memory.\n  source: Results 3.3, paragraph 1; Figure S8 (not in the text read)\n  quote: We began by confirming the normal social behavior of Acan fl/fl and WT mice\n  criterion: SOCIAL and TRIALS-ANOVA, Figure S8 legend not read, so readings (a) and (b) and\n    (i) and (ii) all apply. Reproduced when both genotypes show INTACT memory under a reading;\n    partially reproduced when one does.\n- id: fig3b-acan-ko-eliminates-ca2-pnns\n  statement: Eight weeks after CA2-targeted AAV SynCre injection, the vast majority of\n    WFA-labelled PNNs in CA2 of Acan fl/fl mice are eliminated.\n  source: Results 3.3, paragraph 1; Figure 3A and 3B\n  quote: the vast majority of WFA-expressing PNNs were eliminated after 8 weeks of AAVCre\n    injection in Acan fl/fl mice\n  criterion: The paper shows images only and reports no test. With the Methods 2.8 measure and\n    the Methods 2.10 default for two groups, PNN-AREA in CA2 of Acan AAV Cre against WT AAV Cre\n    mice by a two-tailed unpaired t-test. Open, the unit (no n is given); readings (a) slices,\n    (b) mice, slices averaged per mouse. Reproduced when, under a reading, Acan AAV Cre is lower\n    at p < 0.05 and its mean is less than half the WT AAV Cre mean (\"vast majority\").\n- id: figs9-partial-knockout\n  statement: A minor population of CA2 neurons in Acan AAV Cre mice shows only a modest\n    reduction of aggrecan and WFA intensity, a partial knockout.\n  source: Results 3.3, paragraph 1; Figure S9A to S9C (not in the text read)\n  quote: However, a minor population of CA2 neurons showed modest reduction in Acan and WFA\n    fluorescence intensities\n  criterion: The Figure S9 legend was not read and the text defines no per-neuron measure.\n    Testable only if the dataset holds per-neuron aggrecan and WFA intensities or the images\n    of Figure S9; otherwise blocked as methods_underspecified. Reproduced when a minority (under\n    half) of PCP4 neurons in Acan AAV Cre mice keep aggrecan and WFA intensities above the\n    lowest WT AAV Cre neuron.\n- id: figs9-wt-cre-pnns-intact\n  statement: WT mice injected with AAV SynCre keep unaltered CA2 PNNs.\n  source: Results 3.3, paragraph 1; Figure S9D (not in the text read)\n  quote: WT mice injected with AAV SynCre displayed unaltered PNNs\n  criterion: A claim of absence. Figure S9D's legend was not read, so the comparison group is\n    not known; the reading the text allows is PNN-AREA in CA2 of WT AAV Cre mice against\n    uninjected WT or control mice of similar age held in the dataset, by a two-tailed unpaired\n    t-test (Methods 2.10 default). Reproduced when p >= 0.05; blocked if no comparison group is\n    in the dataset.\n- id: fig3c-acan-ko-impairs-social-memory\n  statement: After CA2 aggrecan deletion, Acan fl/fl mice show impaired social memory while WT\n    mice injected with AAV SynCre show normal social memory.\n  source: Results 3.3, paragraph 1; Figure 3C\n  quote: By contrast, Acan fl/fl mice injected with AAV SynCre showed impaired social memory as\n    evidenced by no difference in interaction times between familiar and novel mice\n  statistics:\n  - test: two-way ANOVA, Tukey's multiple comparisons test\n    p: 0.01\n    p_relation: \"<\"\n    n: 10 mice in each group\n  criterion: SOCIAL and TRIALS-ANOVA, readings (a), (b), (i), (ii). Reproduced when, under a\n    reading, WT AAV Cre shows INTACT memory and Acan AAV Cre shows IMPAIRED memory; partially\n    reproduced when WT AAV Cre is INTACT and Acan AAV Cre has one of the two comparisons at p <\n    0.05.\n- id: fig3de-acan-ko-difference-scores\n  statement: Both difference scores are significantly reduced in CA2 PNN-deleted mice (Acan\n    AAV Cre) compared with WT AAV Cre mice.\n  source: Results 3.3, paragraph 1; Figure 3D and 3E\n  quote: The difference score between the two groups was significantly different\n  statistics:\n  - about: Novel 1 - Familiar (Figure 3D)\n    test: unpaired two-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 10 mice per group\n  - about: Familiar - Novel 2 (Figure 3E)\n    test: unpaired two-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 10 mice per group\n  criterion: DIFF. Reproduced when both scores differ at p < 0.05 with the WT AAV Cre score\n    further from zero on the side of intact memory; partially reproduced when one does.\n- id: figs1-chabc-removes-wfa-adds-2b6\n  statement: ChABC injection removes WFA staining in CA2 while the chondroitin sulfate stub\n    epitope 2B6 appears; cortex near the injection site also shows low WFA intensity, while\n    cortex distal to it is unchanged.\n  source: Methods 2.2.1; Figure S1A to S1E (not in the text read)\n  quote: PNN disruption was confirmed by the loss of Wisteria floribunda agglutinin (WFA)\n    staining in CA2 ... in combination with the appearance of CS stub 2B6 staining ... Cortical\n    areas proximal to the injection site also showed a low WFA intensity ... however, cortical\n    areas distal to the injection site showed no change in WFA intensity\n  criterion: The Figure S1 legend was not read, so the tests and n are not known. WFA\n    intensity (Methods 2.8, PNN-INTENSITY readings) and 2B6 intensity in CA2, and WFA intensity\n    in proximal and distal cortex, ChABC against PNase mice by two-tailed unpaired t-tests\n    (Methods 2.10 default). Reproduced when CA2 WFA is lower and CA2 2B6 higher in ChABC at p <\n    0.05, proximal cortex WFA lower at p < 0.05, and distal cortex WFA has p >= 0.05; partially\n    reproduced when the CA2 parts hold and a cortical part does not. Blocked when the dataset\n    holds no 2B6 or cortical data, for those parts.\n- id: figs1-heat-inactivated-chabc-no-effect\n  statement: Heat-inactivated ChABC, like PNase, does not disrupt PNNs.\n  source: Methods 2.2.1; Results 3.3, paragraph 4; Figure S1 (not in the text read)\n  quote: we compared the effect of heat-inactivated ChABC with the PNase injected control, both\n    of which showed no disruption of PNNs\n  criterion: A claim of absence. Test not known (legend not read); the reading the Methods give\n    for two groups is a two-tailed unpaired t-test of PNN-AREA or PNN-INTENSITY in CA2,\n    heat-inactivated ChABC against PNase. Reproduced when p >= 0.05 on both measures; not\n    reproduced when p < 0.05 on either with heat-inactivated ChABC lower.\n- id: fig3g-chabc-pnn-loss-and-regrowth\n  statement: ChABC disrupts CA2 PNNs at 5 days post injection, and PNNs reappear by 14 days.\n  source: Results 3.3, paragraphs 3 and 4; Figure 3G\n  quote: At 5 DPI, ChABC-treated mice showed disrupted CA2 PNNs ... By 14 DPI, PNNs reappeared\n    in the CA2 area\n  criterion: The paper shows images only and reports no test. PNN-AREA in CA2, ChABC against\n    PNase at 5 and at 14 DPI, two-tailed unpaired t-tests (Methods 2.10 default). Open, the\n    unit; readings (a) slices, (b) mice. Reproduced when, under a reading, ChABC is lower at 5\n    DPI with p < 0.05 and its 14 DPI mean is above its 5 DPI mean; the 14 DPI comparison with\n    PNase is reported.\n- id: fig3h-5dpi-chabc-impairs-social-memory\n  statement: At 5 days after ChABC injection into CA2, social memory is impaired, while\n    PNase-injected control mice show normal social memory.\n  source: Results 3.3, paragraph 4; Figure 3H\n  quote: Graph showing impaired social memory in ChABC-injected mice at 5 DPI (5DPI ChABC)\n    whereas PNase-injected mice (control) show normal social memory\n  statistics:\n  - test: two-way ANOVA, Tukey's multiple comparisons test\n    p: 0.05\n    p_relation: \"<\"\n    n: 8 control (PNase) and 10 5DPI ChABC mice\n  criterion: SOCIAL and TRIALS-ANOVA, readings (a), (b), (i), (ii). Reproduced when, under a\n    reading, PNase mice show INTACT memory and ChABC mice IMPAIRED memory; partially\n    reproduced when PNase is INTACT and ChABC has one of the two comparisons at p < 0.05.\n- id: fig3ij-5dpi-difference-scores\n  statement: At 5 DPI, both difference scores of ChABC mice are significantly lower than those\n    of PNase mice.\n  source: Results 3.3, paragraph 4; Figure 3I and 3J\n  quote: the difference score of the ChABC-treated group was significantly lower than the\n    control at 5DPI\n  statistics:\n  - about: Novel 1 - Familiar and Familiar - Novel 2 (Figure 3I and 3J; the legend gives ** and\n      **** without saying which panel has which)\n    test: unpaired two-tailed t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 8 control and 10 5 DPI ChABC mice\n  criterion: DIFF. Reproduced when both scores differ at p < 0.05 with the PNase score further\n    from zero on the side of intact memory; partially reproduced when one does.\n- id: fig3k-14dpi-social-memory-restored\n  statement: By 14 days after ChABC injection, when PNNs have regrown, social memory is\n    reinstated, with normal interaction behavior like PNase mice.\n  source: Results 3.3, paragraph 4; Figure 3K\n  quote: the social memory was also reinstated in ChABC-treated mice by 14DPI, as they exhibited\n    normal social interaction behavior with familiar and novel mice, similar to PNase-treated\n    control mice\n  statistics:\n  - test: two-way ANOVA, Tukey's multiple comparisons test\n    p: 0.001\n    p_relation: \"<\"\n    n: 8 control and 10 14 DPI ChABC mice\n  criterion: SOCIAL and TRIALS-ANOVA, readings (a), (b), (i), (ii). Reproduced when, under a\n    reading, both PNase and 14 DPI ChABC mice show INTACT memory; partially reproduced when\n    ChABC shows one of the two comparisons at p < 0.05 in the INTACT direction.\n- id: fig3lm-14dpi-difference-scores-no-difference\n  statement: At 14 DPI, the difference scores of ChABC and PNase mice do not differ.\n  source: Results 3.3, paragraph 4; Figure 3L and 3M\n  quote: No difference was observed in the difference scores between the groups\n  criterion: A claim of absence, judged on the paper's test. DIFF, two-tailed unpaired t-test\n    for each score (n = 8 PNase, 10 ChABC). Reproduced when both have p >= 0.05; not reproduced\n    when either has p < 0.05.\n- id: fig4b-3m-degs\n  statement: In CA2 of 3 M 5XFAD mice compared with controls, 98 genes are upregulated and 133\n    downregulated.\n  source: Results 3.4, paragraph 1; Figure 4B\n  quote: In 3 M old 5XFAD mice compared to control, we found 98 upregulated genes and 133\n    downregulated genes\n  expected:\n  - quantity: upregulated genes, 3 M 5XFAD against control\n    value: 98\n    tolerance: 9.8\n  - quantity: downregulated genes, 3 M 5XFAD against control\n    value: 133\n    tolerance: 13.3\n  criterion: From the gene read counts, DESeq2 (Methods 2.5), genes with adjusted p < 0.05 and\n    absolute log2 fold change > 1.00 (Methods 2.5; the Results print \"log2FC < -1.00\" here and\n    \"> 1.00\" for 7 M, and the Methods' absolute threshold is followed). Adjusted p is DESeq2's\n    default Benjamini-Hochberg with its default independent filtering (the Methods name no\n    other). Open, the model; readings (a) DESeq2 on the 3 M samples alone with genotype as the\n    factor, (b) one DESeq2 model on all samples with a four-level group factor (age and\n    genotype) and the 3 M contrast, each (c) with unshrunken log2 fold changes (results()\n    default) or (d) with lfcShrink (apeglm, the DESeq2 1.44 default type). Reproduced when both\n    counts are within tolerance under a reading; partially reproduced when the direction\n    balance holds (more down than up) and one count is within tolerance.\n- id: fig4c-7m-degs\n  statement: In CA2 of 7 M 5XFAD mice compared with controls, 314 genes are upregulated and 6\n    downregulated.\n  source: Results 3.4, paragraph 1; Figure 4C\n  quote: In 7 M old 5XFAD mice compared to control, there were 314 upregulated genes and 6\n    downregulated genes\n  expected:\n  - quantity: upregulated genes, 7 M 5XFAD against control\n    value: 314\n    tolerance: 31.4\n  - quantity: downregulated genes, 7 M 5XFAD against control\n    value: 6\n    tolerance: 0.6\n  criterion: As fig4b-3m-degs, for the 7 M contrast, under the same readings. Reproduced when\n    both counts are within tolerance under a reading; partially reproduced when the up count\n    is within tolerance and the down count is below 20 (most changes up).\n- id: fig4d-3m-go-memory-terms-down\n  statement: Among the top 10 GO terms at 3 M, many pathways of learning, memory and cognition\n    are downregulated in 5XFAD mice.\n  source: Results 3.4, paragraph 2; Figure 4D\n  quote: we found many pathways associated with learning, memory, and cognition are\n    downregulated in 3 M old 5XFAD mice compared to their age-matched controls\n  depends_on:\n  - fig4b-3m-degs\n  criterion: The DEGs of fig4b-3m-degs; GO terms ranked by adjusted p, top 10 (Figure 4D\n    legend), each with the GOplot z-score (up - down) / sqrt(count) of its DEGs (GOplot,\n    Methods 2.5). Open, the enrichment method, ontology and background, as the paper names\n    only GOplot for plotting; readings (a) over-representation of the DEGs in GO Biological\n    Process against all genes tested by DESeq2, (b) the same against all annotated mouse\n    genes, both with Benjamini-Hochberg adjustment. Reproduced when, under a reading, at least\n    three of the top 10 terms name learning, memory or cognition and have negative z-scores;\n    partially reproduced for one or two such terms.\n- id: fig4e-7m-go-immune-terms-up\n  statement: Among the top 10 GO terms at 7 M, many immune response pathways are upregulated\n    in 5XFAD mice.\n  source: Results 3.4, paragraph 2; Figure 4E\n  quote: Whereas many pathways related to immune response were upregulated in 7 M old 5XFAD\n    mice compared to their age-matched controls\n  depends_on:\n  - fig4c-7m-degs\n  criterion: As fig4d-3m-go-memory-terms-down, on the DEGs of fig4c-7m-degs, readings (a) and\n    (b). Reproduced when at least three of the top 10 terms name immune, inflammatory or\n    defense responses, or immune cell activation, and have positive z-scores; partially\n    reproduced for one or two.\n- id: fig4fg-ecm-go-terms\n  statement: ECM organization, assembly, disassembly and secretion terms change in 7 M 5XFAD\n    against 3 M 5XFAD and against 7 M controls, but not in 3 M 5XFAD against 3 M controls.\n  source: Results 3.4, paragraph 2; Figure 4F and 4G\n  quote: GO term of the 3 M 5XFAD versus 7 M 5XFAD and 7 M 5XFAD versus 7 M control revealed\n    changes in genes associated with the ECM organization, assembly, disassembly, and secretion\n    ... Consistent with intact memory, 3 M 5XFAD versus 3 M control did not show any change in\n    these genes\n  criterion: DEGs per contrast as in fig4b-3m-degs (with the 3 M against 7 M 5XFAD contrast\n    added), GO enrichment under readings (a) and (b) of fig4d-3m-go-memory-terms-down.\n    Reproduced when, under a reading, terms naming extracellular matrix organization, assembly,\n    disassembly or secretion reach adjusted p < 0.05 in both the 7 M 5XFAD against 3 M 5XFAD\n    and the 7 M 5XFAD against 7 M control contrasts, and none does in 3 M 5XFAD against 3 M\n    control; partially reproduced when one of the two 7 M contrasts holds.\n- id: fig4h-pnn-synthesis-genes\n  statement: PNN synthesis genes are broadly stable; at 3 M, Vcan, Cspg5, Tnr and Hapln1 are\n    downregulated in 5XFAD, and at 7 M, Vcan and Bgn are increased.\n  source: Results 3.4, paragraph 3; Figure 4H\n  quote: however, a few genes including Vcan, CSPG5, Tnr, and Hapln1 were downregulated ...\n    Similarly, we found an increase in Vcan and Bgn components, while other genes remained\n    mostly unaltered in 7 M old 5XFAD mice\n  criterion: The heatmap shows z-scored expression and the paper reports no test per gene. The\n    direction is the sign of the DESeq2 log2 fold change of 5XFAD against control at each age\n    (readings of fig4b-3m-degs); DESeq2 adjusted p is reported per gene. Reproduced when all\n    four named genes are lower at 3 M and both named genes higher at 7 M under a reading;\n    partially reproduced when at least four of the six go the named direction.\n- id: fig4i-3m-remodeling-genes-up\n  statement: At 3 M, 5XFAD CA2 shows increased expression of Mmp2, 3, 9, 14, 15 and 17, Timp1,\n    2 and 3, and Adam10, 11, 15 and 17.\n  source: Results 3.4, paragraph 3; Figure 4I\n  quote: 3 M old 5XFAD compared to their age-matched controls shows an increase in MMP 2, 3, 9,\n    14, 15, 17, TIMP 1, 2, 3, and ADAM 10, 11, 15, 17\n  criterion: The sign of the DESeq2 log2 fold change of 5XFAD against control at 3 M for each\n    of the 13 named genes (readings of fig4b-3m-degs); no test per gene is reported, and DESeq2\n    adjusted p is reported per gene. Reproduced when all 13 are positive under a reading;\n    partially reproduced when at least 9 are.\n- id: fig4i-7m-remodeling-genes-up\n  statement: At 7 M, 5XFAD CA2 shows increased expression of Mmp2, 3 and 16, Timp1 and 3, and\n    Adam15 and 17.\n  source: Results 3.4, paragraph 3; Figure 4I\n  quote: The 7 M old 5XFAD compared to their age-matched controls shows an increase in MMP 2, 3,\n    16, TIMP1, 3, and ADAM 15, 17\n  criterion: As fig4i-3m-remodeling-genes-up, for the seven named genes at 7 M. Reproduced when\n    all 7 are positive; partially reproduced when at least 5 are.\n- id: fig4i-common-and-7m-vs-3m-up\n  statement: Mmp2, Mmp3 and Timp1 are upregulated at both 3 and 7 M, and 7 M 5XFAD mice show\n    higher Mmp3, Timp1, 2 and 3, and Adam10 and 17 than 3 M 5XFAD mice.\n  source: Results 3.4, paragraph 3; Figure 4I\n  quote: The common genes upregulated at both 3 and 7 M 5XFAD compared to their age-matched\n    controls were MMP2, MMP3, and TIMP1 ... whereas 7 M 5XFAD compared to 3 M 5XFAD mice show\n    an increase in MMP3, TIMP1, 2, 3, Adam 10, 17\n  criterion: The sign of the DESeq2 log2 fold change (readings of fig4b-3m-degs) for Mmp2, Mmp3\n    and Timp1 in both age contrasts, and for the six named genes in the 7 M 5XFAD against 3 M\n    5XFAD contrast. Reproduced when all are positive under a reading; partially reproduced when\n    at least two thirds are.\n- id: fig5-5m-pnns-normal\n  statement: In 5XFAD mice, CA2 PNNs are normal until 5 M of age and impaired by 6 M.\n  source: Results 3.5, paragraph 2\n  quote: we found that PNNs and social memory were normal until 5 M of age; however, by 6 M both\n    are impaired\n  inferred: null\n  criterion: No figure shows PNNs at 5 M. PNN-AREA in CA2 at 5 M, 5XFAD against control,\n    two-tailed unpaired t-test on slices (Methods 2.10 default; slices as in Figure 1).\n    Reproduced when p >= 0.05 at 5 M and claim fig1g-pnn-area-reduced-6-to-12m holds at 6 M;\n    blocked if the dataset holds no 5 M IHC.\n  depends_on:\n  - fig1g-pnn-area-reduced-6-to-12m\n- id: fig5b-5m-intact-social-memory\n  statement: At 5 M, 5XFAD and control mice both show normal social memory.\n  source: Results 3.5, paragraph 2; Figure 5B\n  quote: when these mice exhibited normal social memory behavior with no significant difference\n    in the difference score between 5 M old 5XFAD and age-matched controls\n  statistics:\n  - test: two-way ANOVA, Tukey's multiple comparisons test\n    p: 0.05\n    p_relation: \"<\"\n    n: 7 control and 11 5XFAD mice\n  criterion: SOCIAL and TRIALS-ANOVA, readings (a), (b), (i), (ii). Reproduced when both groups\n    show INTACT memory under a reading; partially reproduced when both comparisons go in the\n    INTACT direction in both groups but only two or three reach p < 0.05.\n- id: fig5cd-5m-difference-scores-no-difference\n  statement: At 5 M, the difference scores do not differ between 5XFAD and control mice.\n  source: Results 3.5, paragraph 2; Figure 5C and 5D\n  quote: with no significant difference in the difference score between 5 M old 5XFAD and\n    age-matched controls\n  criterion: A claim of absence, judged on the paper's test. DIFF, two-tailed unpaired t-test\n    for each score (n = 7 control, 11 5XFAD). Reproduced when both have p >= 0.05; not\n    reproduced when either has p < 0.05.\n- id: fig5e-gm6001-preserves-social-memory\n  statement: After a month of GM6001, 6 M 5XFAD mice show normal social memory, while\n    vehicle-treated 5XFAD mice show disrupted social memory.\n  source: Results 3.5, paragraph 3; Figure 5E\n  quote: 5XFAD mice treated with vehicle showed altered social memory behavior; however, the\n    GM6001-treated 5XFAD mice exhibited normal social behavior\n  statistics:\n  - test: two-way ANOVA, Tukey's multiple comparisons test\n    p: 0.05\n    p_relation: \"<\"\n    n: 14 5XFAD + GM6001 and 12 5XFAD + vehicle mice\n  criterion: SOCIAL and TRIALS-ANOVA on the two 5XFAD groups (the Results say the behavior study\n    included two groups; the legend's mention of age-matched controls gives no n), readings\n    (a), (b), (i), (ii). Reproduced when, under a reading, GM6001 mice show INTACT memory and\n    vehicle mice IMPAIRED memory; partially reproduced when GM6001 is INTACT and vehicle has one\n    of the two comparisons at p < 0.05.\n- id: fig5fg-gm6001-difference-scores\n  statement: Both difference scores of GM6001-treated 5XFAD mice differ significantly from\n    those of vehicle-treated 5XFAD mice.\n  source: Results 3.5, paragraph 3; Figure 5F and 5G\n  quote: with a significant difference in the difference score compared to vehicle-treated\n    5XFAD mice\n  statistics:\n  - about: Novel 1 - Familiar and Familiar - Novel 2 (Figure 5F and 5G; the legend gives *** and\n      **** without saying which panel has which)\n    test: unpaired two-tailed t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 14 5XFAD + GM6001 and 12 5XFAD + vehicle mice\n  criterion: DIFF. Reproduced when both scores differ at p < 0.05 with the GM6001 score further\n    from zero on the side of intact memory; partially reproduced when one does.\n- id: fig5i-gm6001-preserves-ca2-pnns\n  statement: GM6001-treated 6 M 5XFAD mice have significantly higher CA2 PNN expression than\n    vehicle-treated 5XFAD mice.\n  source: Results 3.5, paragraph 3; Figure 5H and 5I\n  quote: the IHC analysis of GM6001-treated mice brains exhibited significantly higher CA2 PNN\n    expression compared to vehicle-treated 5XFAD mice\n  statistics:\n  - test: one-way ANOVA, Tukey's multiple comparisons test\n    p: 0.05\n    p_relation: \"<\"\n    n: 4 to 5 mice per group\n  criterion: One value per mouse (the legend's n is mice), four groups, one-way ANOVA with\n    Tukey's comparisons (legend). Open, what \"PNN expression\" is; readings (a) PNN-AREA, (b)\n    PNN-INTENSITY (under its own readings). Open, how slices make a mouse's value; readings (1)\n    the mean over the mouse's slices, (2) one slice per mouse if the dataset holds one.\n    Reproduced when 5XFAD + GM6001 is above 5XFAD + vehicle with Tukey p < 0.05 under every\n    reading; methods_underspecified if readings disagree, with all shown.\n- id: fig5i-gm6001-controls-comparable\n  statement: Control mice treated with GM6001 or vehicle have CA2 PNN expression comparable to\n    each other and to GM6001-treated 5XFAD mice, so GM6001 has no significant effect in\n    controls.\n  source: Results 3.5, paragraph 3; Figure 5I\n  quote: Age-matched controls treated with GM6001 or vehicle exhibited PNN expression comparable\n    to GM6001-treated 5XFAD mice ... In addition, the control mice treated with GM6001 and\n    vehicle showed comparable PNN expression\n  criterion: A claim of absence, judged on the paper's test, the one-way ANOVA with Tukey's\n    comparisons of fig5i-gm6001-preserves-ca2-pnns, under its readings. Reproduced when control\n    + GM6001 against control + vehicle, and each control group against 5XFAD + GM6001, all have\n    p >= 0.05; not reproduced when any has p < 0.05. Differences and p are reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001702/10.1002-alz.70813.yaml",
 "old_string": "  inferred: null\n",
 "new_string": ""
}
```

```
The file claims/001702/10.1002-alz.70813.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001702/10.1002-alz.70813.yaml paper/10.1002-alz.70813.txt; grep -n "—\|rather" claims/001702/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml
d=yaml.safe_load(open('claims/001702/10.1002-alz.70813.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        [walk(v,p+'.'+k) for k,v in x.items()]
    elif isinstance(x,list):
        [walk(v,p) for v in x]
    elif isinstance(x,str) and ': ' in x: print(p,x[:80])
walk(d)
print(len(d['claims']), sum('criterion' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('expected' in c for c in d['claims']))"
```

```
50 50 18 2
```

**Agent**

I wrote `claims/001702/10.1002-alz.70813.yaml` with 50 claims. The quote checker reports 0 problems; nothing is committed.

**Text read:** the version of record from Europe PMC (PMC12541281): main text, Methods and the legends of Figures 1 to 5. There was no PDF, so I could not see which comparison carries which asterisk in the figures. Where a legend lists several p levels, I recorded the weakest bound it allows. The paper links no code. Its statistics were run in Prism, its image analysis in ImageJ, and its RNA-seq analysis in DESeq2 and GOplot.

**Missing from the paper text:**
- **The whole Supporting Information.** That is Figures S1 to S9 and Tables S1 to S4. Tables S2 and S3 hold every mean, SEM, test statistic and exact p; Table S4 holds the RNA-seq analysis. So no exact p-value or test statistic is available. I went ahead because the main findings are stated in the main text and legends, as earlier claims files here did. The 11 claims on supplementary figures quote the main text that cites them, but their tests, sample sizes and measures are unknown, and each criterion says so.
- **A published correction** (e71098), which was not in the text.
- **RNA-seq sample sizes**, which the main text does not give.

**Claims:**
- All 50 have quotes; none rests on `inferred`.
- 18 claims carry statistics (20 p bounds in all). Only two have expected values: the counts of differentially expressed genes (98 up and 133 down at 3 months, 314 up and 6 down at 7 months).
- Every claim has a criterion.
- All are `data: dataset`. The paper names no outside data. The dandiset's own description says the RNA-seq data are also in GEO (GSE317499); whether the dandiset holds the counts is left to the author.

**Details the paper leaves open, with the readings named:**
- **Social test:** the trial length is not stated; the reading is the whole trial as the dataset records it.
- **Social test ANOVA:** where a legend says only "two-way ANOVA" (Figures 3C, 3H, 3K, 5B, 5E), trial may or may not be a repeated measure. Tukey's test may compare the trials within each group, or all six cells. Every combination is run.
- **Difference score sign:** legends label the second score "Familiar − Novel 2", but the text calls impaired scores "lower". The criteria use the two-tailed test and judge direction by which group lies further from zero on the side of intact memory.
- **Image threshold:** Otsu or Triangle, both named in the Methods.
- **WFA intensity:** the mean inside the WFA mask, or the mean over the CA2 rectangle.
- **Figure 5I:** "PNN expression" could be area or intensity, and a mouse's value could be the mean over its slices or a single slice.
- **Units where the paper only shows images** (Figure 3B, 3G): slices or mice. These claims use the Methods' default test for two groups.
- **Distance moved (Figure 2K):** measured during habituation, familiarization or the test phase.
- **DESeq2:** a model per age or one model on all samples, each with or without log fold change shrinkage. The Results' thresholds contradict each other, so the Methods' absolute log2 fold change > 1 is used.
- **GO enrichment:** the tool, ontology and background are unstated. The readings are over-representation in Biological Process against the tested genes, or against all annotated genes.
- **Peak count (Figure 1B), PV-associated net region (Figure 1A), and the tests for Figures S2, S5 and S7:** readings are named in each criterion.

**Thresholds I set, not the paper:**
- "Many" GO terms is set as at least 3 of the top 10.
- "Vast majority" of nets eliminated is set as below half of the control mean.

## End of run

20 turns, 6 minutes, result: success.
