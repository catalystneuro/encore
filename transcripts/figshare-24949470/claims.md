# figshare-24949470 · claims · run 40570084318

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/^## Reader/,/^## [A-Z]/p'; ls claims/001453/ paper/; ls claims/figshare-24949470 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -120 claims/001453/*.yaml; wc -l paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml",
 "offset": 28,
 "limit": 150
}
```

```
28	  archive: dandi
29	  id: "001453"
30	paper: doi:10.1016/j.cub.2025.04.027
31	claims:
32	- id: stimulus-code-link
33	  kind: link
34	  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using
35	    the paper's analysis code and the protocol file of its stimulus software, and the values
36	    computed through that link agree with those the paper's code printed.
37	  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
38	  data: with_labels
39	  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
40	    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
41	    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
42	    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
43	    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
44	    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
45	    the counts per species are compared instead. The sign of the zebrafish turning response
46	    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them
47	    is lateral right.
[... 130 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41597-024-03777-0.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims/ | grep -i fig; for d in claims/figshare-*; do head -40 $d/*.yaml; done; ls tools/
```

```
head: cannot open 'claims/figshare-*/*.yaml' for reading: No such file or directory
__pycache__
agent_run.py
archive_transcripts.sh
archives
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
notify.py
papers_manifest.py
progress.py
readme_row.py
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims | head -50; grep -rl "dryad" claims | head; grep -n -i "code\b.*deposit\|deposit.*code\|same archive" -r claims docs/protocol.md | head -20
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
000016
000017
000019
000023
000034
000035
000036
000037
000041
000044
[... 57 more lines not kept]
```

**Agent**

Precedent (claims/001773) leaves code that sits inside the dataset's own deposit unread, so I will do the same here. Next I'm checking a Scientific Data claims file for style.

**Agent calls Bash**

```bash
head -60 claims/001262/*.yaml; grep -n "^  [a-z_]*:" -h claims/*/*.yaml | sed 's/^[0-9]*://' | awk '{print $1}' | sort | uniq -c | sort -rn | head -30
```

```
# Claims for Heeringa (2024), Scientific Data 11, 411, on dandiset 001262.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (open access, PMC11035566), as served by Europe PMC, in
# paper/10.1038-s41597-024-03259-3.txt: Background & Summary, Methods, Data Records, Technical
# Validation, Usage Notes, Code availability, Table 1 and the figure legends. The paper is a
# Data Descriptor and has no supplement. The PDF was not needed.
#
# Code read: the software toolbox the paper links, Zenodo record 10370064
# (doi:10.5281/zenodo.10370064, the only version, published 2024-04-15), 21 MATLAB files:
# check_dataset_metadata.m (Table 1, Fig. 3, metadata.csv), check_dataset_units.m (all panels
# of Figs. 6 and 7), check_dataset_animal.m, checkAN.m (Fig. 4), makePSTH.m (Fig. 5b),
# call_extract_func.m and the analysis functions BFextract_func.m, RLFextract_func.m,
# getDrivenRatesRLF.m, PHextract_func.m, TytoView_calcVS.m, CFextract_func.m, getQ10dB.m,
# Clickextract_func.m, getFSL2bins.m, getFSLpoisson.m, SRextract_func.m, getSpikeCounts.m,
# and bandwidthBF.m, getQ10dB_withCF.m, getRasterData3.m, which no criterion uses.
# Details the code settles, used in the criteria below:
#   - Age groups (both scripts): young adult age <= 365 days, middle aged > 365 and <= 1095
#     days, old > 1095 days; months are days / (365/12). Table 1 statistics are over animals.
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn "figshare" tools/claims_check.py tools/datasets.py tools/build_figshare_targets.py | head -20; grep -rn -B2 -A8 "24949470" --include=*.yaml --include=*.json --include=*.md . 2>/dev/null | grep -v "^./paper" | head -40
```

```
tools/build_figshare_targets.py:1:"""Build targets/figshare.json, the registry's list of Figshare datasets, from their article ids.
tools/build_figshare_targets.py:3:    python tools/build_figshare_targets.py 24949470=10.1038/s41597-024-03777-0 26877211 ... [--out targets/figshare.json]
tools/build_figshare_targets.py:6:not crawled. Give each dataset as its article id, a Figshare DOI (10.6084/m9.figshare.<id>[.v<n>]) or a page URL
tools/build_figshare_targets.py:7:(including an institutional portal's, *.figshare.com), optionally with .v<n> to pin a version other than the
tools/build_figshare_targets.py:15:A dataset is named by its article id (FIGSHARE:24949470, folder figshare-24949470). Reading the files needs no
tools/build_figshare_targets.py:31:API = "https://api.figshare.com/v2"
tools/build_figshare_targets.py:52:    found = (re.fullmatch(r"([0-9]+)(?:\.v([0-9]+))?", item) or re.search(r"figshare\.([0-9]+)(?:\.v([0-9]+))?$", item)
tools/build_figshare_targets.py:109:    parser.add_argument("--out", type=Path, default=ROOT / "targets" / "figshare.json")
tools/build_figshare_targets.py:117:    out = {"schema_version": 1, "archive": "figshare",
tools/build_figshare_targets.py:119:           "source": f"{API}, chosen by hand (tools/build_figshare_targets.py)", "note": args.note,
./targets/figshare.json-146-  },
./targets/figshare.json-147-  {
./targets/figshare.json:148:   "id": "24949470",
./targets/figshare.json-149-   "name": "The Volebny Kompas Datasets on Slovak Voter and Party Positions",
./targets/figshare.json:150:   "url": "https://figshare.com/articles/dataset/The_Volebny_Kompas_Datasets_on_Slovak_Voter_and_Party_Positions/24949470",
./targets/figshare.json:151:   "doi": "10.6084/m9.figshare.24949470.v1",
./targets/figshare.json-152-   "published_version": "1",
./targets/figshare.json-153-   "versions": 1,
./targets/figshare.json-154-   "item_type": "dataset",
./targets/figshare.json-155-   "published": "2024-07-09",
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/figshare.json'))
for t in d['datasets'] if 'datasets' in d else d['targets']:
  if t['id']=='24949470': print({k:v for k,v in t.items() if k not in ('files',)})
" 2>&1 | head -40; grep -n "archive:" claims/dryad-*/*.yaml | head -3
```

```
{'id': '24949470', 'name': 'The Volebny Kompas Datasets on Slovak Voter and Party Positions', 'url': 'https://figshare.com/articles/dataset/The_Volebny_Kompas_Datasets_on_Slovak_Voter_and_Party_Positions/24949470', 'doi': '10.6084/m9.figshare.24949470.v1', 'published_version': '1', 'versions': 1, 'item_type': 'dataset', 'published': '2024-07-09', 'license': 'https://creativecommons.org/licenses/by/4.0/', 'asset_count': 8, 'size_gb': 0.0325, 'data_standards': ['CSV', 'Excel', 'R script', 'text'], 'readme': True, 'code': [], 'species': [], 'approaches': [], 'keywords': ['Political Transformation in Post-Socialist Europe', 'Voter Behavior and Party Dynamics', 'Slovakia', 'Central Europe', 'Elections'], 'categories': ['Political science not elsewhere classified', 'Political geography', 'Public policy', 'Sociology not elsewhere classified', 'Other economics not elsewhere classified'], 'papers': [{'doi': '10.1038/s41597-024-03777-0', 'title': 'The Volebny Kompas Datasets on Slovak Voter and Party Positions', 'relation': 'given', 'resource_type': 'JournalArticle', 'preprint': False}], 'catalystneuro': []}
claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml:96:  archive: dryad
claims/dryad-bvq83bkk9/10.1098-rspb.2024.2556.yaml:86:  archive: dryad
claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml:56:  archive: dryad
```

**Agent calls Bash**

```bash
python3 -c "
g=[44919,61626,1420];a=[1264,7020,12280,34894,27847,15178,6083,2716,683];e=[990,1665,30644,2570,2554,69542]
for x in (g,a,e): print(sum(x),[round(100*v/sum(x),2) for v in x])
print(39*11)"; sed -n 1,80p tools/claims_check.py | grep -n "kind\|where\|inferred\|data" | head -30
```

```
107965 [41.61, 57.08, 1.32]
107965 [1.17, 6.5, 11.37, 32.32, 25.79, 14.06, 5.63, 2.52, 0.63]
107965 [0.92, 1.54, 28.38, 2.38, 2.37, 64.41]
429
18:import unicodedata
35:    s = unicodedata.normalize("NFKC", html.unescape(s))
```

**Agent calls Bash**

```bash
grep -n -B3 -A6 "data: elsewhere" claims/dryad-*/*.yaml claims/001262/*.yaml | head -40; grep -n "inferred:" -A3 claims/dryad-*/*.yaml | head -12
```

```
claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml:769:  inferred: Numbers from Supplemental Table S5 (annual rows, 2020 and 2021); no sentence states them
claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml-770-    except the Discussion's maximum of 17 C in the warmed treatments in 2020.
claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml-771-  expected:
claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml-772-  - quantity: annual air temperature 2020, C
```

**Agent calls Bash**

```bash
grep -rn -A4 "data: elsewhere" claims | head -30
```

```
claims/000294/10.1162-neco_a_01672.yaml:192:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml-193-  where: NeuroMorpho.org Buccino_Hierlemann_Cell1 and Buccino_Hierlemann_Cell2; GitHub
claims/000294/10.1162-neco_a_01672.yaml-194-    alejoe91/multimodalfitting at commit 24e8e61, cell_models/<cell>/morphology_corrected.swc
claims/000294/10.1162-neco_a_01672.yaml-195-  criterion: In each reconstructed morphology (SWC), the AIS is the path labeled "apic" (type 4,
claims/000294/10.1162-neco_a_01672.yaml-196-    Methods 5.7.2). Reproduced when, in both cells, the first AIS point's parent is a dendrite
--
claims/000294/10.1162-neco_a_01672.yaml:203:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml-204-  where: GitHub alejoe91/multimodalfitting at commit 24e8e61, cell_models/hay_ais (model) and
claims/000294/10.1162-neco_a_01672.yaml-205-    notebooks/ground-truth/1-generate-ecode-protocols-and-features-hay_ais.ipynb
claims/000294/10.1162-neco_a_01672.yaml-206-  expected:
claims/000294/10.1162-neco_a_01672.yaml-207-    quantity: ground-truth rheobase
--
claims/000294/10.1162-neco_a_01672.yaml:218:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml-219-  where: GitHub alejoe91/multimodalfitting at commit 24e8e61, cell_models/hay_ais and
claims/000294/10.1162-neco_a_01672.yaml-220-    notebooks/ground-truth/7-AIS-test.ipynb
claims/000294/10.1162-neco_a_01672.yaml-221-  criterion: Simulate the released model with IDrest 300% (7-AIS-test.ipynb) and record the
claims/000294/10.1162-neco_a_01672.yaml-222-    membrane potential at the soma, the middle and the distal AIS, as in Figure 3B; the code plots
--
claims/000294/10.1162-neco_a_01672.yaml:234:  data: elsewhere
claims/000294/10.1162-neco_a_01672.yaml-235-  where: GitHub alejoe91/multimodalfitting at commit 24e8e61, cell_models/hay_ais/fitting
[... 10 more lines not kept]
```

**Agent**

I've read the paper: version of record from Europe PMC, with no PDF. Supplementary Table 1 is listed only by title. The main results do not rest on it, so I'm writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/figshare-24949470/10.1038-s41597-024-03777-0.yaml",
 "content": "# Claims for Mesežnikov Mikuš et al. (2024), Scientific Data, on Figshare item 24949470.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-10-27, protocol as stated in docs/protocol.md.\n#\n# Text read: the version of record (open access, PMC11374779), as served by Europe PMC, in\n# paper/10.1038-s41597-024-03777-0.txt: Background & Summary, Methods, Data Records, Technical\n# Validation, Usage Notes, Code availability, Tables 1 and 2 and the figure titles. The text\n# gives only the titles of Figs. 1 to 7, not their content, and there is no PDF, so the party\n# placements of Figs. 2, 3 and 7 and the daily counts of Fig. 4 could not be read. The paper's\n# one supplement, Supplementary Table 1 (the 39 statements, with the uni-dimensions,\n# landscape axes and polarities assigned to them), is named but not in the text read. No\n# claim's expected value rests on it; the claim on the uni-dimension and landscape\n# placements needs its assignments, and the factor analysis needs its list of negatively\n# worded statements (see those claims).\n#\n# Code read: none. The paper's code (\"R code for pre-processing the data and conducting basic\n# analysis\", Code availability) is deposited in the same Figshare item as the data\n# (doi:10.6084/m9.figshare.24949470), and the reader does not open the dataset's files. The\n# code may settle several details named as open below; the author should read it and record\n# what it fixes.\n#\n# Data the paper used. User Responses Dataset (data_without_email.csv): n = 134,699 raw\n# responses to the Volebný Kompas voting advice application, collected from its launch on\n# 5 September 2023 to election day, 30 September 2023. Per response: a timestamp\n# (TIME.STAMP); answers S1 to S39 on 0, 25, 50, 75, 100 (completely disagree to completely\n# agree), with an empty string for \"no opinion\" and -1 for an unanswered statement; up to\n# three most salient statements; the parties the user would consider voting for and would\n# never vote for (e.g. UN26, 0/1); GENDER, AGE (categories), EDUCATION (categories);\n# EMAIL_ID (pseudonymized placeholder, duplicates allowed). Party Positions Dataset\n# (VAA_party_positions coded.xlsx): the 39 statements in Slovak, Hungarian and English and\n# 429 party positions (11 parties by 39 statements), with expert-coded positions, party\n# self-placements (4 of the 11 parties answered), sources, snippets and links. The Figshare\n# item also holds a data dictionary, a README, R scripts, the raw data and a pre-processed\n# Slovak census CSV (Data Records, Usage Notes).\n#\n# Cleaning, from Technical Validation, Data cleaning: rows with -1 in any of S1 to S39 are\n# removed as incomplete; empty demographics become NA; empty Likert answers (\"no opinion\")\n# become 50. Which claims use the cleaned rows is not always said; the readings are named\n# in each criterion.\n#\n# Not claimed: the political background (Background & Summary), the 3% polling rule for\n# party selection (a method), the platform's matching by Manhattan distance (a method), the\n# President's Instagram video likes (outside data the paper does not cite).\nschema_version: 2\ndataset:\n  archive: figshare\n  id: \"24949470\"\npaper: doi:10.1038/s41597-024-03777-0\nclaims:\n- id: user-responses-count\n  statement: The User Responses Dataset holds 134,699 voter responses, each with answers to the\n    39 statements, along with demographics, the three most salient statements and the parties\n    the respondent would and would never vote for, for most responses.\n  source: Data Records, User Responses Dataset; Table 1\n  quote: This raw dataset provides n = 134,699 individual Likert-scale responses to a series of\n    39 policy issues and value statements along with additional user demographics and\n    preferences for most of the responses\n  expected:\n  - quantity: rows of the raw user responses file\n    value: 134699\n    tolerance: 13470\n  criterion: Count the rows of the raw user responses file (data_without_email.csv) and check\n    that it has the columns of Table 1 (TIME.STAMP, S1 to S39, the would-not-vote columns such\n    as UN26, GENDER, AGE, EDUCATION, EMAIL_ID). Reproduced when the row count is within\n    tolerance and the columns are present. The count is of the raw file, before cleaning, as\n    the Data Records say (\"This raw dataset\"); the count after removing incomplete rows is\n    reported as well.\n- id: collection-window\n  statement: The responses were gathered during the 26 days leading up to and including\n    election day, from the launch on 5 September 2023 to the election on 30 September 2023.\n  source: Background & Summary, paragraph 3; Methods, Volebný Kompas implementation and usage,\n    paragraph 5\n  quote: gathered during the 26 days leading up to and including the day of the 2023 snap\n    Slovak Parliamentary Elections\n  criterion: From TIME.STAMP of the raw rows. Reproduced when every timestamp falls between\n    2023-09-05 and 2023-09-30 inclusive. The time zone of TIME.STAMP is not stated; dates are\n    read as given. Table 1's sample entry (2023-10-09 08:57:38) falls outside this window, so\n    the number and share of rows outside it are reported, and the claim is partially\n    reproduced when 99% or more of rows fall inside (the 99% is this file's choice; the paper\n    sets no share).\n- id: party-positions-structure\n  statement: The Party Positions Dataset lists the 39 statements in Slovak, Hungarian and\n    English and holds 429 party positions, both party self-placements and expert-coded\n    positions, with sources, snippets and links.\n  source: Data Records, Party Positions Dataset\n  quote: This dataset lists the n = 39 statements used in the survey across three languages —\n    Slovak, Hungarian, and English and offers detailed information on various parties’ positions\n    concerning specific statements with n = 429 observations\n  expected:\n  - quantity: statements\n    value: 39\n    tolerance: 0\n    unit: statements\n  - quantity: party positions (observations)\n    value: 429\n    tolerance: 0\n    unit: observations\n  criterion: Tolerance 0, as these are counts of a fixed design (11 parties by 39 statements).\n    Reproduced when the file holds 39 statements, each with a Slovak, Hungarian and English\n    wording, and 429 party-by-statement positions with expert-coded positions, self-placement\n    columns, and source, snippet and link columns.\n- id: eleven-parties\n  statement: Eleven parties are positioned on the 39 statements.\n  source: Abstract and Methods, Party selection and coding, paragraph 1\n  quote: Out of 25 political parties, 11 met the inclusion criteria and were incorporated into\n    our VAA\n  expected:\n  - quantity: parties in the Party Positions Dataset\n    value: 11\n    tolerance: 0\n    unit: parties\n  criterion: Tolerance 0, a count. Reproduced when the Party Positions Dataset names 11 distinct\n    parties, each with positions on the 39 statements.\n- id: party-self-placements\n  statement: Four of the eleven parties returned the self-placement questionnaire.\n  source: Methods, Party selection and coding, paragraph 3\n  quote: Responses were garnered from four political entities out of eleven\n  depends_on:\n  - eleven-parties\n  expected:\n  - quantity: parties with self-placements\n    value: 4\n    tolerance: 0\n    unit: parties\n  criterion: Tolerance 0, a count. Reproduced when exactly 4 of the 11 parties have\n    self-placement values in the Party Positions Dataset. A party counts when it has a\n    self-placement for at least one statement; the number of statements each answered is\n    reported.\n- id: coder-agreement-kappa\n  statement: Agreement between the two expert coders of party positions was high, with a\n    weighted Cohen's kappa of 0.84.\n  source: Methods, Party selection and coding, paragraph 2\n  quote: we employed Weighted Cohen’s Kappa37, which provided a value of κ = 0.84, indicating a\n    high level of consistency among coders\n  expected:\n  - quantity: weighted Cohen's kappa between the two coders\n    value: 0.84\n    tolerance: 0.084\n  criterion: Weighted Cohen's kappa (Methods, citing ref. 37) between the two coders' positions\n    over the 429 party-by-statement positions, ordered Completely Disagree, Tend to Disagree,\n    Neutral, Tend to Agree, Completely Agree. Two details are open in the text. The weights,\n    readings (a) linear and (b) quadratic. The \"No Opinion\" category, readings (i) pairs with\n    No Opinion from either coder left out, (ii) No Opinion scored as Neutral (50), as the\n    cleaning does for users. Reproduced when kappa is within tolerance under one reading;\n    every reading is reported. The claim needs each coder's separate positions; whether the\n    dataset holds them is the author's to find.\n- id: uni-and-landscape-placements\n  statement: The platform placed each party on five uni-dimensions, using 18 of the 39\n    statements, and on a two-dimensional socio-economic and socio-cultural landscape from 0 to\n    100, using 16 statements; the placements (Figs. 2 and 3) conform to the anticipated\n    placements of Slovak parties.\n  source: Methods, Volebný Kompas implementation and usage, paragraphs 3 and 4; Figs. 2 and 3;\n    Technical Validation, Content validation, last paragraph\n  quote: Out of the 39 statements, 18 were assigned to the five uni-dimensions ... Of the 39\n    statements, 16 influenced this two-dimensional political landscape\n  criterion: The dimensions and polarities of each statement come from Supplementary Table 1,\n    which was not in the text read; the author takes them from it or from the data dictionary.\n    Party positions on 0 to 100 as in the Methods (Completely disagree 0 to Completely agree\n    100). The scoring is said to follow the euandi method (ref. 30) and is not given in full.\n    Readings for a dimension score (a) the mean over its statements of the position for\n    polarity +1 and 100 minus the position for polarity -1; (b) for the landscape, a start at\n    50 moved by each statement's polarity-adjusted deviation from 50, averaged over the axis's\n    statements. \"No Opinion\" party positions are left out under both. Reproduced when the\n    counts of assigned statements are 18 and 16 and, under one reading, the order of the\n    parties on each uni-dimension and each landscape axis matches Figs. 2 and 3 of the\n    published paper. The figures were not readable here, so the expected placements are read\n    from the published figures by the author.\n  data: with_labels\n- id: party-clustering\n  statement: Hierarchical clustering of the parties' recoded positions, by Manhattan distance\n    and average linkage, groups the parties largely as anticipated (Fig. 7).\n  source: Technical Validation, Content validation, paragraph 6; Fig. 7\n  quote: We used the ‘recoded_party_positions’ dataset and computed pairwise Manhattan\n    distances to emphasize the absolute differences in policy positions, applying average\n    linkage clustering\n  depends_on:\n  - eleven-parties\n  criterion: Method from the Technical Validation; party positions coded 0, 25, 50, 75, 100 as\n    in the Methods; pairwise Manhattan distances between the 11 parties over the 39 statements;\n    average linkage. The recoding behind 'recoded_party_positions' is made by the deposited R\n    code and is not described; for \"No Opinion\" the readings are (a) recoded to 50, as the\n    cleaning does for users, and (b) left out of each pairwise distance. Reproduced when, under\n    one reading, the dendrogram's merge order (its topology) matches Fig. 7 of the published\n    paper. The text names no expected grouping and the figure was not readable here, so the\n    author reads it from the published figure.\n- id: table2-gender\n  statement: Of the responses with gender given, 41.61% are female (44,919), 57.08% male\n    (61,626) and 1.32% other or prefer not to say (1,420).\n  source: Table 2, Gender rows\n  inferred: The numbers are only in Table 2; no sentence of the text states them.\n  expected:\n  - quantity: female\n    value: 44919\n    tolerance: 4492\n  - quantity: male\n    value: 61626\n    tolerance: 6163\n  - quantity: other or prefer not to say\n    value: 1420\n    tolerance: 142\n  - quantity: female, percent\n    value: 41.61\n    tolerance: 4.16\n    unit: percent\n  - quantity: male, percent\n    value: 57.08\n    tolerance: 5.71\n    unit: percent\n  - quantity: other or prefer not to say, percent\n    value: 1.32\n    tolerance: 0.13\n    unit: percent\n  criterion: The paper does not say which rows Table 2 counts. Each of its three blocks sums to\n    107,965 (computed here from the table), fewer than the 134,699 raw rows, and each\n    percentage is over that sum. Readings (a) rows left after the cleaning (no -1 in S1 to\n    S39), with gender not NA; (b) all raw rows with gender not empty. Reproduced when, under one\n    reading, every count and percentage is within tolerance. The total under each reading is\n    reported.\n- id: table2-age\n  statement: Respondents are skewed toward younger ages; 32.32% are 25 to 34 (34,894) and\n    25.79% are 35 to 44 (27,847), with 2,716 aged 65 to 74 and 683 aged 75 or older (Table 2).\n  source: Technical Validation, Content validation, paragraph 2; Table 2, Age rows\n  quote: the substantial numbers within the younger age brackets, particularly those aged 25–34\n    (n = 34,894, 32.32%) and 35–44 (n = 27,847, 25.79%), highlight this trend (Table 2)\n  expected:\n  - quantity: under 18\n    value: 1264\n    tolerance: 126\n  - quantity: 18-20\n    value: 7020\n    tolerance: 702\n  - quantity: 21-24\n    value: 12280\n    tolerance: 1228\n  - quantity: 25-34\n    value: 34894\n    tolerance: 3489\n  - quantity: 35-44\n    value: 27847\n    tolerance: 2785\n  - quantity: 45-54\n    value: 15178\n    tolerance: 1518\n  - quantity: 55-64\n    value: 6083\n    tolerance: 608\n  - quantity: 65-74\n    value: 2716\n    tolerance: 272\n  - quantity: 75 or older\n    value: 683\n    tolerance: 68\n  - quantity: 25-34, percent\n    value: 32.32\n    tolerance: 3.23\n    unit: percent\n  - quantity: 35-44, percent\n    value: 25.79\n    tolerance: 2.58\n    unit: percent\n  criterion: The rows counted are open, with the readings of table2-gender (a) cleaned rows with\n    age not NA, (b) raw rows with age not empty. Reproduced when, under one reading, every count\n    and the two percentages are within tolerance. The other percentages of Table 2 (1.17, 6.50,\n    11.38, 14.06, 5.63, 2.52, 0.63) are reported against the result.\n- id: table2-education\n  statement: Respondents are skewed toward the well educated; 64.41% have a university degree\n    or academic higher education (69,542), with 990 reporting no education and 1,665 only\n    primary education (Table 2).\n  source: Technical Validation, Content validation, paragraph 2; Table 2, Education rows\n  quote: The pronounced presence of individuals with university degrees or academic higher\n    education (n = 69,542, 64.41%)\n  expected:\n  - quantity: no education\n    value: 990\n    tolerance: 99\n  - quantity: primary education\n    value: 1665\n    tolerance: 167\n  - quantity: secondary education\n    value: 30644\n    tolerance: 3064\n  - quantity: applied higher education\n    value: 2570\n    tolerance: 257\n  - quantity: vocational education\n    value: 2554\n    tolerance: 255\n  - quantity: university degree/academic higher education\n    value: 69542\n    tolerance: 6954\n  - quantity: university degree/academic higher education, percent\n    value: 64.41\n    tolerance: 6.44\n    unit: percent\n  criterion: The rows counted are open, with the readings of table2-gender (a) cleaned rows with\n    education not NA, (b) raw rows with education not empty. Reproduced when, under one\n    reading, every count and the percentage are within tolerance.\n- id: age-education-inconsistencies\n  statement: The multivariate check found 40 respondents under 18 and 400 aged 18 to 20\n    reporting university-level education, which is not congruent with their age.\n  source: Technical Validation, Structural validation, paragraph 3\n  quote: specifically n = 40 cases under the age of 18 and n = 400 cases aged ‘18–20’, which\n    were not congruent with university-level education attainment\n  expected:\n  - quantity: under 18 with a university degree/academic higher education\n    value: 40\n    tolerance: 4\n  - quantity: 18-20 with a university degree/academic higher education\n    value: 400\n    tolerance: 40\n  criterion: Count rows with EDUCATION \"University degree/Academic higher education\" and AGE\n    \"Under 18\", and with AGE \"18–20\". The rows checked are open; the structural validation is\n    run \"After cleaning\" (Structural validation, paragraph 1), so reading (a) is the cleaned\n    rows and reading (b) all raw rows. Whether \"university-level\" also takes in \"Applied higher\n    education\" is open, readings (i) the university category only, as the paragraph names it,\n    and (ii) both higher education categories. Reproduced when both counts are within tolerance\n    under one reading.\n- id: s2-s3-wide-range\n  statement: Opinions on S2 (higher earners should face a higher income tax rate) and S3 (the\n    retirement age should rise with life expectancy) span a wide range, with means of 43 and\n    42, standard deviations of 33 and medians of 25.\n  source: Technical Validation, Content validation, paragraph 4; Fig. 5\n  quote: S2 — ‘People who earn higher wages should have a higher income tax rate’ (mean = 43,\n    s.d. = 33, median = 25) and S3— ‘The retirement age should rise as life expectancy\n    increases’ (mean = 42, s.d. = 33, median = 25) highlight the diversity of opinions\n  expected:\n  - quantity: S2 mean\n    value: 43\n    tolerance: 4.3\n  - quantity: S2 standard deviation\n    value: 33\n    tolerance: 3.3\n  - quantity: S2 median\n    value: 25\n    tolerance: 2.5\n  - quantity: S3 mean\n    value: 42\n    tolerance: 4.2\n  - quantity: S3 standard deviation\n    value: 33\n    tolerance: 3.3\n  - quantity: S3 median\n    value: 25\n    tolerance: 2.5\n  criterion: Statistics are taken \"prior to the re-coding of ‘no opinion’ with a value of 50\"\n    (same paragraph), so \"no opinion\" answers are left out. The rows are open, readings (a) rows\n    left after removing those with -1 in S1 to S39; (b) all raw rows, leaving out -1 and empty\n    answers to the statement. Standard deviation with the n - 1 denominator (R's sd), a\n    standard choice that cannot change the outcome at this sample size. Reproduced when, under\n    one reading, all six values are within tolerance.\n- id: s4-s5-consensus\n  statement: S4 (more personal responsibility in health care) and S5 (heavier taxes on banks and\n    big corporations) show stronger consensus, with medians of 75 (means 70 and 69, standard\n    deviations 26 and 29), though more than 17,435 respondents for S4 and 23,344 for S5\n    disagree with scores of 0 or 25.\n  source: Technical Validation, Content validation, paragraph 4; Fig. 5\n  quote: S4 — ‘In the health care system, more emphasis should be placed on the personal\n    responsibility of the individual’ (mean = 70, s.d. = 26, median = 75,) and S5 —‘Banks and\n    big corporations should be taxed more heavily’ (mean = 69, s.d. = 29, median = 75) suggest a\n    stronger consensus ... more than n = 17,435 for S4 and n = 23,344 for S5 — diverging on\n    these views, with scores of 0 and 25\n  expected:\n  - quantity: S4 mean\n    value: 70\n    tolerance: 7\n  - quantity: S4 standard deviation\n    value: 26\n    tolerance: 2.6\n  - quantity: S4 median\n    value: 75\n    tolerance: 7.5\n  - quantity: S5 mean\n    value: 69\n    tolerance: 6.9\n  - quantity: S5 standard deviation\n    value: 29\n    tolerance: 2.9\n  - quantity: S5 median\n    value: 75\n    tolerance: 7.5\n  - quantity: S4 respondents scoring 0 or 25\n    value: 17435\n    tolerance: 1744\n  - quantity: S5 respondents scoring 0 or 25\n    value: 23344\n    tolerance: 2334\n  criterion: Rows as in s2-s3-wide-range, readings (a) cleaned rows and (b) raw rows, \"no\n    opinion\" left out. \"More than n = 17,435\" can be read as (i) the count of answers 0 or 25 is\n    about 17,435 (within tolerance) or (ii) the count exceeds 17,435; likewise for S5.\n    Reproduced when, under one combination of readings, the six statistics are within\n    tolerance and both counts hold.\n- id: efa-eleven-factors\n  statement: Parallel analyses on both the polychoric and the Pearson correlation matrices of\n    S1 to S39 indicated that 11 factors should be extracted.\n  source: Technical Validation, Content validation, paragraphs 5 and 6; Fig. 6\n  quote: Both parallel analyses indicated that 11 factors should be extracted.\n  expected:\n  - quantity: factors indicated by parallel analysis, polychoric correlations\n    value: 11\n    tolerance: 0\n    unit: factors\n  - quantity: factors indicated by parallel analysis, Pearson correlations\n    value: 11\n    tolerance: 0\n    unit: factors\n  criterion: Tolerance 0, a count of factors. Method from the Technical Validation, R package\n    psych (ref. 45) on S1 to S39, with negatively worded statements reversed (which ones is in\n    Supplementary Table 1 or the R code; reversing an item does not change the eigenvalues, so\n    this cannot change the count). Open details, all of which could change the count. Rows,\n    readings (a) the cleaned rows with \"no opinion\" as 50 and (b) the cleaned rows with \"no\n    opinion\" as missing, pairwise complete. The parallel analysis settings are not given;\n    reading psych's fa.parallel defaults (minres factoring, 20 iterations, the factor count it\n    reports, not the component count), once with cor \"poly\" and once with \"cor\". The random\n    seed is a standard choice that may move the count by one; it is reported. Reproduced when\n    both counts are 11 under one reading of the rows.\n- id: efa-loadings-consistent\n  statement: With 11 factors and promax rotation, maximum likelihood and principal axis\n    factoring gave consistent results, and S1 (real estate tax raised to lower labour taxes) and\n    S3 (retirement age) loaded strongly.\n  source: Technical Validation, Content validation, paragraph 6\n  quote: various estimation strategies were employed, including Maximum Likelihood (ML) and\n    principal axis factoring, with promax rotation. This approach yielded consistent results.\n    Notably statements such as S1 — ‘Real estate tax should be increased to lower labor taxes\n    rises’ and S3 — ‘The retirement age should rise as life expectancy rises’ had strong\n    loadings\n  depends_on:\n  - efa-eleven-factors\n  criterion: psych fa with nfactors 11, rotate \"promax\", fm \"ml\" and fm \"pa\", on the matrices\n    and rows of efa-eleven-factors. \"Strong\" and \"consistent\" are not defined in the paper; the\n    thresholds here are this file's choices and an outcome resting on them rests on an\n    assumption. S1 and S3 have strong loadings when their largest absolute loading is at least\n    0.4 under reading (i) and 0.5 under reading (ii). The two solutions are consistent when each\n    statement's factor of largest absolute loading, matched between solutions by Tucker\n    congruence, agrees for at least 35 of 39 statements. Reproduced when, under one reading,\n    S1 and S3 load strongly in both solutions and the solutions are consistent; all loadings\n    are reported.\n- id: selected-parties-top-vote\n  statement: The 11 selected parties were the top 11 vote recipients in the 2023 election; each\n    received at least 2% of the vote and no excluded party reached 1%.\n  source: Methods, Party selection and coding, paragraph 1\n  quote: The inclusion closely corresponded to election results, correctly anticipating the top\n    11 vote recipients. All of the 11 selected parties received at least 2% of the vote while no\n    excluded party reached the 1%.\n  data: elsewhere\n  where: Official results of the 30 September 2023 Slovak parliamentary election (Statistical\n    Office of the Slovak Republic); the paper cites no source for them beyond ref. 20.\n  depends_on:\n  - eleven-parties\n  criterion: Reproduced when the 11 parties of the Party Positions Dataset are the 11 lists with\n    the most votes, each at 2% or more, and every other list is below 1%.\n- id: website-views\n  statement: The platform registered 270,836 website views in the 26 days leading up to the\n    election.\n  source: Methods, Volebný Kompas implementation and usage, paragraph 6; Fig. 4\n  quote: registering 270,836 website views within the 26-day span leading up to the elections\n  data: elsewhere\n  where: The platform's usage records (the euandi2019 platform run by the Robert Schuman Centre,\n    European University Institute); the paper does not say they are deposited.\n  expected:\n  - quantity: website views\n    value: 270836\n    tolerance: 27084\n  criterion: Reproduced when the platform's view count for 5 to 30 September 2023 is within\n    tolerance. The user responses alone cannot test it, since views are not responses.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/figshare-24949470/10.1038-s41597-024-03777-0.yaml paper/10.1038-s41597-024-03777-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/figshare-24949470/10.1038-s41597-024-03777-0.yaml; sed -i '1s/.*/# Claims for "The Volebny Kompas Datasets on Slovak Voter and Party Positions" (Scientific Data, 2024),\n# on Figshare item 24949470. The text read names the authors by initials only (J.M.M., K.B. and others)./' $f; sed -i 's/^  source: Abstract and Methods, Party selection and coding, paragraph 1$/  source: Methods, Party selection and coding, paragraph 1/' $f; head -4 $f; grep -n "Party selection and coding, paragraph 1" $f; python tools/claims_check.py $f paper/10.1038-s41597-024-03777-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/figshare-24949470/10.1038-s41597-024-03777-0.yaml` and the quote checker passes it: 18 claims, 17 quotes, 0 problems.

**Text read:** the version of record from Europe PMC (PMC11374779). That covers the main text, Methods, Technical Validation, Usage Notes, and Tables 1 and 2. There is no PDF.

**Counts:**
- **Claims:** 18.
- **Quotes:** 17. The gender rows of Table 2 have no sentence stating them, so that claim has an `inferred` note instead.
- **Statistics:** 0. The paper reports no tests or intervals. Its kappa, means and SDs are recorded as expected values with the default 10% tolerance. Counts fixed by the design (39 statements, 429 positions, 11 parties, 4 self-placements, 11 factors) get tolerance 0, with the reason given.
- **Criteria:** all 18 claims have one.
- **Outside data:** 2 claims use `data: elsewhere`. One is the official 2023 election results; the other is the platform's 270,836 website views.

**Missing from the paper:**
- **Supplementary Table 1** (the 39 statements, with their dimensions and polarities) is named but not in the text. No expected value rests on it. The uni-dimension and landscape claim needs its assignments. The factor analysis needs its list of reversed statements, but reversing items cannot change the factor count.
- **Figure content:** without a PDF, Figs. 2, 3, 4 and 7 are titles only. The two claims on party placements and the clustering dendrogram say the expected result must be read from the published figures.
- **Code not read:** the paper's R code sits in the same Figshare item as the data, so I did not open it, following the precedent in claims/001773. It may settle several of the open details below, and the author should read it.

**Details left open, with the readings named:**
- **Which rows Table 2 counts:** each block sums to 107,965, not 134,699. Readings are (a) cleaned rows with the variable not NA, or (b) raw rows with the variable not empty.
- **Age–education mismatches (40 and 400):** which rows, cleaned or raw. Also whether "university-level" means (i) the university category only, or (ii) both higher-education categories.
- **S2–S5 statistics:** which rows, cleaned or raw, with "no opinion" left out in both. For "more than n = 17,435" (and 23,344 for S5), the readings are (i) the count is about that number, or (ii) the count exceeds it.
- **Weighted kappa:** (a) linear or (b) quadratic weights; "No Opinion" either (i) dropped or (ii) scored as Neutral. The claim also needs each coder's separate positions in the dataset, which the author has to confirm.
- **Uni-dimension and landscape scoring:** the euandi formula is not given. Readings are (a) the mean of polarity-adjusted positions, or (b) a start at 50 moved by polarity-adjusted deviations.
- **Clustering recode:** "No Opinion" either (a) set to 50, or (b) left out of each distance.
- **Factor analysis:**
  - "No opinion" either (a) set to 50, or (b) treated as missing, pairwise.
  - The parallel-analysis settings are taken as psych's defaults, and the seed is reported.
  - "Strong loading" (reading (i) 0.4, (ii) 0.5) and "consistent" (the same top factor for at least 35 of 39 items) are thresholds I chose. They are marked as assumptions in the file.
- **Collection window:** Table 1's sample timestamp (2023-10-09) falls after the stated window. The time zone is not stated. The 99% share that counts as partial reproduction is my choice, not the paper's.

Nothing was committed.

## End of run

16 turns, 3 minutes, result: success.
