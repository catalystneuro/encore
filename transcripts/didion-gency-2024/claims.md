# dryad-4j0zpc8hz · claims · run 40503727775

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls claims/001453/ paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 170
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
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
18	  claim, and it asks a reader for any method detail the file lacks.
19	- The **verifier** checks the author's work and must not be the author.
20	
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001453/ paper/; ls claims/dryad-4j0zpc8hz 2>&1; ls claims | grep dryad
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
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
wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1093-plphys-kiad565.txt",
 "offset": 30,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1093-plphys-kiad565.txt",
 "offset": 229,
 "limit": 1170
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "4j0zpc8hz",
 "output_mode": "content",
 "-n": true
}
```

```
targets/dryad.json:120:   "id": "4j0zpc8hz",
targets/dryad.json:122:   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.4j0zpc8hz",
targets/dryad.json:123:   "doi": "10.5061/dryad.4j0zpc8hz",
```

**Agent calls Read**

```json
{
 "file_path": "targets/dryad.json",
 "offset": 110,
 "limit": 40
}
```

```
110	     "doi": "10.1093/evlett/qrad056",
111	     "title": "Phage selection drives resistance–virulence trade-offs in <i>Ralstonia solanacearum</i> plant-pathogenic bacterium irrespective of the growth temperature",
112	     "relation": "primary_article",
113	     "resource_type": "JournalArticle",
114	     "preprint": false
115	    }
116	   ],
117	   "catalystneuro": []
118	  },
119	  {
120	   "id": "4j0zpc8hz",
121	   "name": "Chronic warming and dry soils limit carbon uptake and growth despite a longer growing season in beech and oak",
122	   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.4j0zpc8hz",
123	   "doi": "10.5061/dryad.4j0zpc8hz",
124	   "published_version": "260590",
125	   "version_number": 3,
126	   "published": "2023-10-17",
127	   "license": "https://spdx.org/licenses/CC0-1.0.html",
128	   "asset_count": 3,
129	   "size_gb": 0.0002,
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -A5 "dryad" docs/archives.md | head -60; ls claims | grep -v '^[0-9]' ; grep -rl "archive: " claims | xargs grep -h "archive:" | sort | uniq -c
```

```
82:## Dryad
83-
84:- **Datasets.** A Dryad dataset, named by its DOI's suffix without the
85:  `dryad.` prefix: `10.5061/dryad.bvq83bkk9` is `DRYAD:bvq83bkk9`, in folders
86:  `dryad-bvq83bkk9` (Dryad DOIs ignore case). The registry's list,
87:  `targets/dryad.json`, is built from chosen DOIs by
88:  `tools/build_dryad_targets.py`, which reads each dataset's metadata, latest
89-  version and file list from the public API v2; for now it holds three datasets
90-  outside neuroscience, to test the pipeline on a general-purpose repository.
91-  The papers are the dataset's related works marked `primary_article` (and
92-  `preprint`); related works marked `software` are the paper's code, usually on
93-  Zenodo.
--
103:  `https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.<id>` and
104-  `/api/v2/versions/<version id>/files`. Downloading a file is not:
105-  `/api/v2/files/<file id>/download` answers 401 without a bearer token, and
106-  the website's download links (`/downloads/file_stream/<file id>`) answer 403
107-  to scripts. A token comes from an API account, which a person makes from
108:  their Dryad account (an ORCID login), "My account", "API account"; its client
109-  id and secret are exchanged for a token, which lasts 10 hours, at
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
head -20 claims/crcns-ret-1/*.yaml; head -60 tools/claims_check.py; grep -rn "kind:" claims | awk '{print $NF}' | sort | uniq -c
```

```
# Claims for Lefebvre, Zhang, Meister, Wang & Sanes (2008), Development 135:4141-4151, on CRCNS
# data set ret-1 (doi:10.6080/K0RF5RZT).
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20,
# protocol pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read: the NIH author manuscript in PubMed Central (PMC2644426), as supplied under paper/,
# with its Methods, Results, Discussion and the legends of Figures 1 to 9; the version of
# record's abstract is appended to it. No PDF was supplied. The supplement (Supplementary
# Figures 1 to 3, which PMC lists as present) is not in the text and was not read. Its
# contents are known only from the main text's citations: the Chx10-Cre recombination pattern
# (S1), synapse density in Bax mutants and example spike-triggered averages (S2; the
# manuscript cites S2 for both), and receptive field surrounds (S3). Its legends were not seen
# and may hold method details (the test of S2, the measure of S3). The claims that cite it are
# quoted from the main text and take no number from it. The paper links no analysis code, so none was read.
#
# Data the paper used. Mice on a C57/B6J background. Conditional Pcdh-gamma alleles (fdel, the
# whole cluster floxed; fcon3, the last constant exon floxed), excised in retina by Chx10-Cre
# or Pax6alpha-Cre (Pax6alpha-Cre spares a central sector except for Pax6alpha amacrines); some
# crossed onto Bax-/-. Histology (Figures 1 to 8): sections and dissociated cells, layer
# thickness and cell counts at E17.5 to P150, 3 to 8 animals per genotype; none of it is in
[... 62 more lines not kept]
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
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
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

**Agent calls Read**

```json
{
 "file_path": "targets/dryad.json",
 "offset": 148,
 "limit": 30
}
```

```
148	     "path": "README.md",
149	     "size": 886,
150	     "file_id": 2652096,
151	     "sha256": "4382b7943736808911d1cb886c72342833e23606766a712e656b31806d2a39eb"
152	    }
153	   ],
154	   "readme": true,
155	   "code": [],
156	   "species": [],
157	   "approaches": [],
158	   "keywords": [
159	    "Downy oak",
160	    "Low soil moisture",
161	    "European beech",
162	    "Phenology",
163	    "Photosynthesis",
164	    "Species interactions",
165	    "Global warming",
166	    "growth"
167	   ],
[... 10 more lines not kept]
```

**Agent**

The full text and supplement are present (no PDF, no linked code). Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml",
 "content": "# Claims for Didion-Gency, Vitasse, Buchmann, Gessler, Gisler, Schaub & Grossiord (2024), Plant\n# Physiology 194, doi:10.1093/plphys/kiad565, on Dryad dataset 4j0zpc8hz (doi:10.5061/dryad.4j0zpc8hz).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-10-27,\n# protocol pilot-10 as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record from Europe PMC (PMC10828195, full-text XML) as supplied under\n# paper/, with Results, Discussion, Materials and methods, the legends of Figures 1 to 7, and the\n# supplement (kiad565_supplementary_data.pdf as extracted text) with the legends of Supplemental\n# Figures S1 to S7, Supplemental Tables S1 to S6 and Supplemental Methods S1 to S4. No PDF was\n# supplied, so the figures were not seen. The R2 and P values printed inside Figures 1, 2 and S1\n# are therefore not recorded. Equations 3 and 4 of Supplemental Methods S4 (complementarity and\n# selection effects) are garbled in the extracted text (an averaging bar is lost). The paper links\n# no analysis code (analyses in R 4.2.0, nlme lme and multcomp), so none was read.\n#\n# Data the paper used. Open-top chambers (OTCs) at WSL Birmensdorf, 16 chambers, each with eight\n# soil compartments. Seedlings of European beech (Fagus sylvatica) and downy oak (Quercus\n# pubescens), 3 yr old, planted October 2018 as single trees, monocultures (four trees of one\n# species) and mixtures (two of each); only monocultures and mixtures are analysed, one tree per\n# species measured per compartment. Four climatic treatments from June 2019, each in four\n# chambers, control (C), warming of about +5 C (W), soil moisture reduction of about 50% (MR) and\n# both (WMR). Six trees per climatic treatment, species and interaction treatment, 96 trees.\n# Measured 2019 to 2021; the paper reports 2020 and 2021 (2019 in Supplemental Figs. S5 and S6).\n# Variables per tree, phenology once a year (bud swelling date, leaf development duration from\n# stage 1 to 4, onset of senescence at 10% coloured or fallen leaves, senescence duration from\n# 10% to 90%, growing season length from bud swelling to onset of senescence, all in days of\n# year or days); leaf-level traits three campaigns a year (light-saturated assimilation Asat,\n# predawn and midday leaf water potential, starch and sugar concentration of the midday leaf);\n# growth once a year in September (height, basal diameter at 15 cm, and aboveground woody\n# biomass AGWB estimated from height, Supplemental Methods S3, with increments as the difference\n# from the previous year). Climate per chamber at 10 min (air temperature and relative humidity\n# at 50 cm and 2 m, soil temperature and moisture at 25 cm), from which GDD, chilling days,\n# Tspring, Tfall, Tannual, Mspring, Mfall and Mannual are computed.\n#\n# Outside data. AGWB uses the species-specific coefficients beta1 and beta2 of Annighofer et al.\n# (2016), Eur J For Res 135:313-329, doi:10.1007/s10342-016-0937-z, which the paper does not\n# print. If the dataset holds AGWB itself, they are not needed.\n#\n# Procedures used by the criteria below, each from the paper as cited; details it leaves open\n# are named with their readings.\n#\n# Phenology regression (Methods, Statistical analysis, paragraph 1; Figure 1 legend). Per species,\n# monoculture trees, 2020 and 2021 pooled, all four treatments, a linear regression (lm) of the\n# phenological trait on the daily mean air temperature of the season (Tspring February to April,\n# Tfall September to December, Tannual the year, as in Table S5), significant at P <= 0.05.\n# Open, the unit of the regression (P1) each tree and year against its chamber's mean, or (P2)\n# the eight treatment and year means against the treatment's mean, as Figure 1 plots them (Table\n# S5 gives the treatment means). Open, the sensor (H1) 50 cm or (H2) 2 m; the Methods name both.\n#\n# Treatment test (Methods, Statistical analysis, paragraph 2; Table S1 footnotes; Figures 3 and 4\n# legends). Per species, monoculture trees; leaf-level traits averaged per tree and year over the\n# three campaigns (Methods); lme(trait ~ (warming + moisture reduction + year)^3, random =\n# ~1|Chamber), warming and moisture reduction yes or no, year a factor; square root for starch,\n# sugar, Asat and the increments (Table S1), none for leaf water potentials; Tukey-type contrasts\n# among the four treatments within each year (multcomp), alpha 0.05. Open, (T1) the model on 2019\n# to 2021 as the Methods and Table S1 state, or (T2) on 2020 and 2021, the years reported. Open,\n# when an increment is negative, how the square root was taken; (S1) untransformed, (S2) square\n# root after adding the constant that brings the minimum to zero. The F tests of Table S1 are\n# read as nlme's anova (sequential); marginal tests are a variant.\n#\n# Interaction test (Methods, Statistical analysis, paragraph 3; Tables S2 and S3 footnotes). Per\n# species, monoculture and mixture trees, lme(trait ~ (warming + moisture reduction + year +\n# interaction)^3, random = ~1|Chamber), square root for all traits of Tables S2 and S3, and\n# Tukey-type contrasts of mixtures against monocultures. Open, (I1) within each climatic treatment\n# and year, or (I2) within each climatic treatment over 2020 and 2021.\n#\n# Biodiversity effects (Methods, Biodiversity, complementarity, and selection effects;\n# Supplemental Methods S4; Methods, Statistical analysis, paragraph 3). Net biodiversity effect\n# (NBE) by Eq. 2 as printed, [(FO x WO) - (FE x WO)] x 100, with FO the trait of the species in\n# mixture, FE in monoculture, WO = 0.5; complementarity effect by Eq. 3 as printed, [N x (FO x\n# WO / FE - WO) x FE] x 100, N = 2; selection effect by Eq. 4, whose averaging term is lost in the\n# text, read as in Loreau and Hector (2001), the term (FO x WO / FE - WO) minus its mean over the\n# trees of the species in that treatment and year, times FE, times 100. Tested against zero by\n# t-test per climatic treatment, year and species (Methods); the legends of Figure 5 and\n# Supplemental Figures S2 and S3 name Tukey's HSD, shown as a variant. The Methods run these\n# tests only where the interaction test found an effect; that is reported for each. Open, (B1)\n# each mixture tree against the mean of the monoculture trees of its species, treatment and year,\n# or (B2) against the monoculture tree of its own chamber; (L1) leaf-level values as yearly tree\n# means (Methods) or (L2) per campaign (the legends give n = 6 trees x 3 campaigns = 18).\nschema_version: 2\ndataset:\n  archive: dryad\n  id: 4j0zpc8hz\n  doi: 10.5061/dryad.4j0zpc8hz\npaper: doi:10.1093/plphys/kiad565\nclaims:\n- id: fig1ab-bud-swelling-advance\n  statement: Warmer spring air advanced bud swelling in both species, by 1.1 days per degree in\n    beech and 2.3 days per degree in oak, across 2020 and 2021 and the four treatments.\n  source: Results, Phenology, paragraph 1; Figure 1A and 1B\n  quote: Higher daily air temperatures in spring were linked to an earlier bud swelling in both\n    species, where beech was advanced by −1.1 d °C−1 and oak by −2.3 d °C−1 across the 2 yr and\n    treatments\n  statistics:\n  - test: linear regression\n    p: 0.05\n    p_relation: \"<\"\n    n: monoculture trees, 6 per treatment, species and year, 2020 and 2021\n  expected:\n  - quantity: slope of bud swelling date on Tspring, beech\n    value: -1.1\n    tolerance: 0.11\n    unit: days per degree C\n  - quantity: slope of bud swelling date on Tspring, oak\n    value: -2.3\n    tolerance: 0.23\n    unit: days per degree C\n  criterion: Phenology regression (opening comment) of bud swelling day of year on Tspring.\n    Reproduced when, under one of the readings P1 or P2 with H1 or H2, both slopes are within\n    tolerance and each regression has P <= 0.05.\n- id: fig1cd-development-duration\n  statement: Warmer spring air shortened leaf development duration by 0.7 days per degree in both\n    species.\n  source: Results, Phenology, paragraph 1; Figure 1C and 1D\n  quote: A shorter leaf development duration was also found, with a reduction of −0.7 d °C−1 in\n    both species\n  statistics:\n  - test: linear regression\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: slope of development duration on Tspring, beech\n    value: -0.7\n    tolerance: 0.07\n    unit: days per degree C\n  - quantity: slope of development duration on Tspring, oak\n    value: -0.7\n    tolerance: 0.07\n    unit: days per degree C\n  criterion: Phenology regression (opening comment) of development duration (stage 1 to stage 4)\n    on Tspring. Reproduced when, under one of the readings P1 or P2 with H1 or H2, both slopes\n    are within tolerance and each regression has P <= 0.05.\n- id: fig1gh-senescence-duration\n  statement: Warmer fall air extended leaf senescence duration by 3.4 days per degree in beech\n    and 3.1 days per degree in oak.\n  source: Results, Phenology, paragraph 1; Figure 1G and 1H\n  quote: Similarly, senescence duration was extended by +3.4 d °C−1 in beech and +3.1 d °C−1 in\n    oak\n  statistics:\n  - test: linear regression\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: slope of senescence duration on Tfall, beech\n    value: 3.4\n    tolerance: 0.34\n    unit: days per degree C\n  - quantity: slope of senescence duration on Tfall, oak\n    value: 3.1\n    tolerance: 0.31\n    unit: days per degree C\n  criterion: Phenology regression (opening comment) of senescence duration (10% to 90% of leaves\n    coloured or fallen, linearly interpolated between observation dates as the Methods say) on\n    Tfall. Reproduced when, under one of the readings P1 or P2 with H1 or H2, both slopes are\n    within tolerance and each regression has P <= 0.05.\n- id: fig1ij-growing-season\n  statement: Warmer annual air lengthened the growing season by 4.5 days per degree in beech and\n    5.7 days per degree in oak.\n  source: Results, Phenology, paragraph 1; Figure 1I and 1J\n  quote: The growing seasons were extended by +4.5 d °C−1 and +5.7 d °C−1 for beech and oak,\n    respectively, with an increase in daily mean annual air temperature\n  statistics:\n  - test: linear regression\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: slope of growing season length on Tannual, beech\n    value: 4.5\n    tolerance: 0.45\n    unit: days per degree C\n  - quantity: slope of growing season length on Tannual, oak\n    value: 5.7\n    tolerance: 0.57\n    unit: days per degree C\n  criterion: Phenology regression (opening comment) of growing season length (bud swelling to\n    onset of senescence) on Tannual. Reproduced when, under one of the readings P1 or P2 with H1\n    or H2, both slopes are within tolerance and each regression has P <= 0.05.\n- id: fig1-oak-steeper-advance\n  statement: The temperature-driven advance was larger in oak than in beech (P = 0.004, least\n    squares analysis).\n  source: Results, Phenology, paragraph 1\n  quote: However chronic warming was more advantageous to oak than to beech as the advancement of\n    bud swelling extension was higher in oak (P = 0.004 using Least-squares analysis)\n  statistics:\n  - test: least-squares analysis\n    p: 0.004\n  criterion: The paper names the analysis only as least squares, and \"advancement of bud swelling\n    extension\" is ambiguous. Readings (a) the species by Tspring interaction in a linear model of\n    bud swelling date on Tspring, species and their interaction; (b) the same for growing season\n    length on Tannual. Each fit on the units of the phenology regression (P1 and P2, H1 and H2).\n    Reproduced when, under one reading, the interaction has p < 0.05 with the oak slope the\n    larger in magnitude; p is reported against 0.004.\n- id: fig1ef-onset-senescence-no-temperature\n  statement: The onset of senescence was not related to fall air temperature in either species.\n  source: Results, Phenology, paragraph 1; Figure 1E and 1F\n  quote: No relationship between the onset of senescence and fall daily air temperatures was\n    found, suggesting that the onset of senescence is not driven by temperature changes in the\n    fall for both species\n  criterion: A claim of absence, on the paper's test, the phenology regression (opening comment)\n    of onset of senescence on Tfall at P <= 0.05. Reproduced when neither species' regression has\n    P <= 0.05. The unit and sensor are open (P1, P2, H1, H2); the outcome is the one they all\n    give, and the slopes are reported.\n- id: figs1-phenology-no-moisture\n  statement: No phenological trait was related to soil moisture in either species.\n  source: Results, Phenology, paragraph 1; Supplemental Figure S1\n  quote: We observed no significant relationship between phenology and soil moisture for both\n    species (Supplemental Fig. S1)\n  criterion: A claim of absence, on the paper's test, linear regressions as in the phenology\n    regression (opening comment), with soil moisture at 25 cm in place of air temperature, bud\n    swelling and development duration on Mspring, onset and duration of senescence on Mfall,\n    growing season length on Mannual (Supplemental Figure S1 legend, Methods, Statistical\n    analysis). Reproduced when none of the ten regressions has P <= 0.05. The unit (P1 or P2) is\n    open; the outcome is the one both give.\n- id: fig2-gdd-chilling\n  statement: The more chilling days trees received, the fewer growing degree days they needed to\n    reach bud swelling, in both species, following a negative exponential.\n  source: Results, Phenology, paragraph 2; Figure 2A and 2B\n  quote: With an increase in the number of chilling days, both species had lower GDD requirements\n    to budburst (Fig. 2)\n  statistics:\n  - test: negative exponential regression (nls)\n    p: 0.05\n    p_relation: \"<\"\n    n: monoculture trees, one point per tree and year, 2020 and 2021\n  criterion: Per species, monoculture trees in 2020 and 2021, one value per tree and year (Figure 2\n    legend). GDD is accumulated from January 1 to the bud swelling date over daily mean air\n    temperatures above 5 C, and chilling days are days with daily mean below 5 C from November 1\n    (Methods, Phenology, paragraph 2), from the chamber's record. Open, (a) GDD as the sum of the\n    excess over 5 C or (b) as the sum of the daily means above 5 C; the end of the chilling count\n    at (c) bud swelling (Methods) or (d) leaf flushing, stage 4 (Figure 2 legend); the sensor (H1\n    or H2); and the negative exponential as (e) GDD = a exp(b CD) or (f) GDD = a + b exp(c CD),\n    the paper giving only nls. Reproduced when, under every reading, the fitted curve decreases\n    with chilling days and its rate parameter has p <= 0.05 in both species; blocked as\n    methods_underspecified when readings differ.\n- id: disc-max-chilling-days\n  statement: Even without warming, trees received at most 97 chilling days.\n  source: Discussion, paragraph 1; Figure 2\n  quote: In our experiment, trees were exposed to a maximum of 97 d even in the absence of warming\n    (Fig. 2)\n  expected:\n    quantity: maximum chilling days, unwarmed (C and MR) monoculture trees, 2020 and 2021\n    value: 97\n    tolerance: 9.7\n    unit: days\n  criterion: Chilling days as in fig2-gdd-chilling, readings (c) and (d) and H1 and H2. Reproduced\n    when the maximum over C and MR trees is within tolerance under one reading.\n- id: fig3-psi-warming-2020\n  statement: Warming made predawn leaf water potential more negative in 2020 in both species, and\n    midday leaf water potential more negative in 2020 in beech only.\n  source: Results, Leaf water potential, paragraph 1; Figure 3\n  quote: Warming resulted in more negative ΨPD in 2020 in both species and more negative ΨMD in\n    2020 but only in beech (Fig. 3)\n  statistics:\n  - about: predawn water potential, warming by moisture reduction by year, beech\n    test: linear mixed-effects model ANOVA\n    statistic: F = 3.54\n    p: 0.031\n  - about: predawn water potential, warming by moisture reduction by year, oak\n    test: linear mixed-effects model ANOVA\n    statistic: F = 3.59\n    p: 0.030\n  - about: treatment contrasts within year\n    test: Tukey's HSD post-hoc test\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 monoculture trees per treatment, species and year\n  criterion: Treatment test (opening comment), untransformed, readings T1 and T2. Reproduced when,\n    in 2020, W is significantly more negative than C for predawn potential in both species and\n    for midday potential in beech, and not in oak; partially reproduced when two or three of\n    these four hold. The outcome is the one T1 and T2 both give.\n- id: fig3-psi-mr-oak-2020\n  statement: Lower soil moisture alone made predawn leaf water potential more negative in 2020 in\n    oak only.\n  source: Results, Leaf water potential, paragraph 1; Figure 3\n  quote: lower soil moisture reduced ΨPD in 2020 but only in oak (Fig. 3)\n  criterion: Treatment test (opening comment), untransformed, readings T1 and T2. Reproduced when,\n    in 2020, MR predawn potential is significantly below C in oak and not in beech; the outcome is\n    the one T1 and T2 both give.\n- id: fig3-psi-wmr-2021\n  statement: Combined warming and drier soil made predawn leaf water potential more negative in\n    2021 in both species.\n  source: Results, Leaf water potential, paragraph 1; Figure 3; Supplemental Table S1\n  quote: However, combined warming and drier soils resulted in more negative ΨPD in 2021 in both\n    species (Fig. 3, Supplemental Table S1)\n  criterion: Treatment test (opening comment), untransformed, readings T1 and T2. Reproduced when,\n    in 2021, WMR predawn potential is significantly below C in both species; partially reproduced\n    in one. The outcome is the one T1 and T2 both give.\n- id: disc-psi-minimum\n  statement: Under the low moisture treatment trees reached predawn water potentials of about\n    -1.9 MPa in beech and -1.2 MPa in oak.\n  source: Discussion, paragraph 3; Figure 3\n  quote: As the predawn (ΨPD) and midday leaf water potential (ΨMD) of our trees were slightly\n    affected by our low moisture treatment (Fig. 3), we considered the water availability level\n    as moderate. Indeed, trees reached ΨPD of about −1.9 and −1.2 MPa in beech and downy oak,\n    respectively\n  expected:\n  - quantity: predawn water potential reached, beech\n    value: -1.9\n    tolerance: 0.19\n    unit: MPa\n  - quantity: predawn water potential reached, oak\n    value: -1.2\n    tolerance: 0.12\n    unit: MPa\n  criterion: The paper does not say which value \"reached\" is. Readings (a) the lowest yearly\n    treatment mean of MR in 2020 or 2021 (Figure 3); (b) the lowest yearly treatment mean of MR\n    or WMR; (c) the lowest campaign treatment mean of MR or WMR. Yearly means are of the\n    tree-year means of monoculture trees. Reproduced when both values are within tolerance under\n    one reading.\n- id: fig4-beech-warming-none\n  statement: In beech, warming alone had no effect on starch, sugar, Asat, or height, diameter and\n    AGWB increments.\n  source: Results, Leaf-level carbon relations and tree growth, paragraph 1; Figure 4; Supplemental\n    Table S1\n  quote: In beech, warming had no impact on leaf-level carbon relations and growth (Fig. 4,\n    Supplemental Table S1)\n  statistics:\n  - about: warming main effect, starch\n    test: linear mixed-effects model ANOVA\n    statistic: F = 1.55\n    p: 0.236\n  - about: warming main effect, sugar\n    test: linear mixed-effects model ANOVA\n    statistic: F = 2.59\n    p: 0.133\n  - about: warming main effect, Asat\n    test: linear mixed-effects model ANOVA\n    statistic: F = 2.44\n    p: 0.144\n  - about: warming main effect, height increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 0.78\n    p: 0.395\n  - about: warming main effect, diameter increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 1.45\n    p: 0.252\n  - about: warming main effect, AGWB increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 0.17\n    p: 0.690\n  criterion: A claim of absence, on the paper's test, the treatment test (opening comment).\n    Reproduced when no W against C contrast is significant (alpha 0.05) for any of the six traits\n    in 2020 or 2021 in beech; not reproduced when any is. The contrasts' sizes and the Table S1\n    warming terms are reported. Readings T1, T2, S1 and S2; the outcome is the one they all give.\n- id: fig4-oak-warming-growth-2021\n  statement: In oak, warming alone reduced height, diameter and AGWB increments, in 2021 only.\n  source: Results, Leaf-level carbon relations and tree growth, paragraph 1; Figure 4G to 4L;\n    Supplemental Table S1\n  quote: In oak, warming reduced height increment, diameter increment, and AGWB increment but only\n    in 2021 (Fig. 4, Supplemental Table S1)\n  statistics:\n  - about: warming main effect, oak diameter increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 15.04\n    p: 0.002\n  - about: warming by year, oak height increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 5.00\n    p: 0.008\n  - about: warming by year, oak diameter increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 3.66\n    p: 0.026\n  - about: treatment contrasts within year\n    test: Tukey's HSD post-hoc test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Treatment test (opening comment), readings T1, T2, S1 and S2. Reproduced when, in oak,\n    W is significantly below C in 2021 for all three increments and for none in 2020; partially\n    reproduced when one or two of the 2021 contrasts are significant and none in 2020. The\n    outcome is the one all readings give.\n- id: disc-oak-warming-no-carbon-change\n  statement: In oak, warming had no effect on Asat or on starch and sugar concentrations.\n  source: Discussion, paragraph 4; Figure 4A to 4F\n  quote: downy oak, which occurs in environments of 19 °C MAT (Pasta et al. 2016), showed no effect\n    of warming on Asat and NSC but a substantial decrease in growth (Fig. 4)\n  criterion: A claim of absence, on the paper's test, the treatment test (opening comment).\n    Reproduced when no W against C contrast is significant for starch, sugar or Asat in oak in\n    2020 or 2021. Readings T1 and T2; the outcome is the one both give.\n- id: fig4-beech-mr\n  statement: In beech, lower soil moisture alone reduced Asat in 2021, height increment in 2021,\n    diameter increment in 2020 and 2021, and AGWB increment in 2021.\n  source: Results, Leaf-level carbon relations and tree growth, paragraph 1; Figure 4\n  quote: In beech, lower soil moisture led to a significant reduction of Asat in 2021, height\n    increment in 2021, diameter increment in 2020 and 2021, and AGWB increment in 2021\n  statistics:\n  - about: moisture reduction by year, beech Asat\n    test: linear mixed-effects model ANOVA\n    statistic: F = 19.00\n    p: 0.001\n    p_relation: \"<\"\n  - about: moisture reduction by year, beech height increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 13.82\n    p: 0.001\n    p_relation: \"<\"\n  - about: moisture reduction by year, beech diameter increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 10.26\n    p: 0.001\n    p_relation: \"<\"\n  - about: treatment contrasts within year\n    test: Tukey's HSD post-hoc test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Treatment test (opening comment), readings T1, T2, S1 and S2. Reproduced when MR is\n    significantly below C in all five named trait-years; partially reproduced in three or four;\n    not reproduced otherwise. The other MR against C contrasts are reported. The outcome is the\n    one all readings give.\n- id: fig4-oak-mr\n  statement: In oak, lower soil moisture alone reduced Asat and height, diameter and AGWB\n    increments in both 2020 and 2021.\n  source: Results, Leaf-level carbon relations and tree growth, paragraph 1; Figure 4\n  quote: Similarly, we observed a substantial reduction in Asat, height increment, diameter\n    increment, and AGWB increments in oak in 2020 and 2021 (Fig. 4, Supplemental Table S1)\n  statistics:\n  - about: moisture reduction by year, oak height increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 35.13\n    p: 0.001\n    p_relation: \"<\"\n  - about: moisture reduction main effect, oak diameter increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 5.01\n    p: 0.045\n  - about: moisture reduction by year, oak diameter increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 15.93\n    p: 0.001\n    p_relation: \"<\"\n  - about: moisture reduction by year, oak AGWB increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 7.27\n    p: 0.002\n  - about: treatment contrasts within year\n    test: Tukey's HSD post-hoc test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Treatment test (opening comment), readings T1, T2, S1 and S2. Reproduced when MR is\n    significantly below C in at least seven of the eight trait-years; partially reproduced in four\n    to six; not reproduced otherwise. The outcome is the one all readings give.\n- id: fig4-beech-wmr\n  statement: In beech, combined warming and low moisture reduced Asat and diameter increment in\n    2020 and 2021.\n  source: Results, Leaf-level carbon relations and tree growth, paragraph 1; Figure 4\n  quote: Under combined warming and low moisture, we observed a reduction of Asat, and diameter\n    increment in 2020 and 2021 in beech\n  criterion: Treatment test (opening comment), readings T1, T2, S1 and S2. Reproduced when WMR is\n    significantly below C in all four trait-years; partially reproduced in two or three. The\n    outcome is the one all readings give.\n- id: fig4-oak-wmr\n  statement: In oak, combined warming and low moisture reduced Asat and height, diameter and AGWB\n    increments in 2020 and 2021.\n  source: Results, Leaf-level carbon relations and tree growth, paragraph 1; Figure 4\n  quote: In oak, a reduction of Asat, height increment, diameter increment, and AGWB increment in\n    2020 and 2021 was observed\n  criterion: Treatment test (opening comment), readings T1, T2, S1 and S2. Reproduced when WMR is\n    significantly below C in at least seven of the eight trait-years; partially reproduced in four\n    to six. The outcome is the one all readings give.\n- id: fig4-wmr-same-as-mr\n  statement: Responses to combined warming and low moisture did not differ from responses to low\n    moisture alone.\n  source: Results, Leaf-level carbon relations and tree growth, paragraph 1; Figure 4\n  quote: No significant differences were found between responses to lower moisture alone and\n    combined warming and soil moisture reduction (Fig. 4, Supplemental Table S1)\n  criterion: A claim of absence, on the paper's test, the treatment test (opening comment).\n    Reproduced when no MR against WMR contrast is significant for the six traits of Figure 4 in\n    either species in 2020 or 2021; not reproduced when any is, with the number and sizes of\n    such contrasts reported. Readings T1, T2, S1 and S2; the outcome is the one all give.\n- id: disc-nsc-unchanged-drier-soil\n  statement: Drier soils did not change starch and sugar concentrations in either species.\n  source: Discussion, paragraph 5; Figure 4A to 4D\n  quote: Chronically drier soils strongly reduced the leaf-level carbon relations and growth of\n    both species, except for NSC where we found no changes (Fig. 4)\n  criterion: A claim of absence, on the paper's test, the treatment test (opening comment).\n    Reproduced when no MR against C contrast is significant for starch or sugar in either species\n    in 2020 or 2021. WMR against C is shown as a variant. Readings T1 and T2; the outcome is the\n    one both give.\n- id: disc-beech-asat-more-impaired\n  statement: Low soil moisture impaired Asat more strongly in beech than in oak.\n  source: Discussion, paragraph 5; Figure 4E and 4F\n  quote: However, while both species were negatively impacted by low soil moisture, beech Asat was\n    more strongly impaired (Fig. 4)\n  criterion: No test is reported. The measure, from Figure 4, is the relative reduction of mean\n    Asat, (C - X) / C, over monoculture tree-year means. Open, which treatment X (MR alone, or MR\n    and WMR) and which year (2020, 2021, or both pooled). Reproduced when the reduction is larger\n    in beech than in oak under every reading; blocked as methods_underspecified when readings\n    differ.\n- id: tables6-no-seasonal-variation\n  statement: Asat, starch and sugar did not vary among the three campaigns of the growing season.\n  source: Methods, Statistical analysis, paragraph 2; Supplemental Table S6\n  quote: As leaf-level responses (assimilation and starch and sugar concentrations) did not vary\n    during the growing season, we averaged them per year before the analyses (Supplemental Table\n    S6)\n  statistics:\n  - about: season effect, starch\n    test: linear mixed-effects model ANOVA\n    statistic: F = 2.64\n    p: 0.074\n  - about: season effect, sugar\n    test: linear mixed-effects model ANOVA\n    statistic: F = 1.56\n    p: 0.213\n  - about: season effect, Asat\n    test: linear mixed-effects model ANOVA\n    statistic: F = 2.03\n    p: 0.134\n  criterion: A claim of absence, on the paper's test (Table S6 footnote), lme(trait ~ (warming +\n    moisture reduction + season)^3, random = ~1|Chamber) on square-root values, season the\n    campaign (early, middle, late). Reproduced when the season term has p > 0.05 for all three\n    traits. Table S6 has no species or year column, so open, (a) both species and all years\n    pooled, (b) per species; and the trees (monocultures, or monocultures and mixtures). The\n    outcome is the one all readings give.\n- id: tables2-phenology-no-interaction\n  statement: Species mixture did not change phenology in either species, except a development\n    duration about 2 days shorter in oak mixtures than monocultures under lower moisture.\n  source: Results, Impact of species interactions, paragraph 1; Supplemental Table S2\n  quote: In both species, no impact of species interactions on phenology was found in any\n    treatment, except in oak where we observed a slightly shorter development duration of 2 d in\n    mixtures compared to the monocultures under lower moisture (Supplemental Table S2)\n  statistics:\n  - about: year by interaction, oak development duration\n    test: linear mixed-effects model ANOVA\n    statistic: F = 9.37\n    p: 0.003\n  - about: moisture reduction by year by interaction, oak development duration\n    test: linear mixed-effects model ANOVA\n    statistic: F = 11.21\n    p: 0.001\n  expected:\n    quantity: oak development duration, monoculture minus mixture, MR\n    value: 2\n    tolerance: 0.2\n    unit: days\n  criterion: Interaction test (opening comment) on the five phenological traits, readings I1 and\n    I2. Reproduced when the only significant mixture against monoculture contrast is oak\n    development duration under MR, shorter in mixtures by a difference within tolerance (in one\n    year under I1, or pooled under I2); partially reproduced when that contrast holds and one other\n    is also significant. The NBE of oak development duration under MR is tested as in the\n    biodiversity effects procedure and reported (the paper says it was not significant).\n- id: tables3-beech-warming-no-interaction\n  statement: Under warming, species mixture did not change beech leaf-level carbon relations or\n    growth, and beech showed no net biodiversity effect.\n  source: Results, Impact of species interactions, paragraph 2; Supplemental Table S3; Figure 5\n  quote: In beech, no impact of species interactions on leaf-level carbon relations or growth was\n    found under the warming treatment in 2020 and 2021 (Supplemental Table S3). Consequently,\n    beech did not show any impact of net biodiversity in response to warming\n  criterion: A claim of absence, on the paper's tests. Reproduced when, in beech under W, no\n    mixture against monoculture contrast of the interaction test (opening comment) is significant\n    for the six traits of Figure 5 in 2020 or 2021, and no NBE differs from zero by the t-test of\n    the biodiversity effects procedure. Readings I1, I2, B1, B2, L1 and L2; the outcome is the one\n    all give.\n- id: figs2-beech-asat-selection-warming\n  statement: Under warming, beech Asat showed a positive selection effect, too weak to change the\n    net biodiversity effect.\n  source: Results, Impact of species interactions, paragraph 2; Supplemental Figure S2E\n  quote: However, we observed a positive selection effect on beech Asat under warming\n    (Supplemental Fig. S2), suggesting positive interactions in the mixtures; although, this\n    effect was not strong enough to influence the overall net biodiversity effect\n  criterion: Biodiversity effects procedure (opening comment). The year is not stated; it may be\n    2020 or 2021. Reproduced when, in one of these years, the beech Asat selection effect under W\n    is positive and differs from zero by the t-test, and the NBE does not. The method readings\n    (B1, B2, L1, L2, and the reading of Eq. 4) must all agree; when they do not, blocked as\n    methods_underspecified.\n- id: tables3-oak-warming-diameter\n  statement: Under warming, oak in mixtures had a diameter increment about 0.3 cm per year lower\n    than in monocultures, and no other difference between mixtures and monocultures.\n  source: Results, Impact of species interactions, paragraph 2; Supplemental Table S3\n  quote: For oak, no differences between mixtures and monocultures were found under warming, except\n    for lower diameter increment of approximately 0.3 cm per year in mixtures compared to\n    monocultures (Supplemental Table S3)\n  statistics:\n  - about: warming by year by interaction, oak diameter increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 4.15\n    p: 0.016\n  expected:\n    quantity: oak diameter increment under W, monoculture minus mixture\n    value: 0.3\n    tolerance: 0.03\n    unit: cm per year\n  criterion: Interaction test (opening comment), readings I1 and I2. The unit is open, as the paper\n    prints cm here but Table S4 gives diameters in mm; readings (u1) 0.3 cm and (u2) 0.3 mm.\n    Reproduced when, under W, the oak diameter increment contrast is significant and lower in\n    mixtures with a difference within tolerance under one unit reading, and no other oak trait\n    contrast under W is significant.\n- id: fig5-oak-agwb-nbe-warming-2020\n  statement: Under warming in 2020, oak showed a negative net biodiversity effect on AGWB increment,\n    explained by a negative complementarity effect.\n  source: Results, Impact of species interactions, paragraph 2; Figure 5L; Supplemental Figure S3L\n  quote: Moreover, oak trees showed a negative net biodiversity effect for the AGWB increment in\n    response to warming in 2020 (Fig. 5), explained by a negative complementarity effect\n    (Supplemental Fig. S3)\n  criterion: Biodiversity effects procedure (opening comment). Reproduced when, for oak AGWB\n    increment under W in 2020, the NBE and the complementarity effect are both negative and differ\n    from zero by the t-test. The Discussion (paragraph 8) calls this complementarity effect\n    positive; the sign found is reported. Readings B1 and B2 must agree; when they do not, blocked\n    as methods_underspecified.\n- id: tables3-beech-mr-diameter\n  statement: Under lower soil moisture, beech in mixtures had a smaller diameter increment than in\n    monocultures.\n  source: Results, Impact of species interactions, paragraph 3; Supplemental Table S3\n  quote: Under lower soil moisture, we found a reduced diameter increment in mixtures compared to\n    the monocultures in beech (Supplemental Table S3)\n  statistics:\n  - about: moisture reduction by year by interaction, beech diameter increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 15.06\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Interaction test (opening comment). The year is not stated. Reproduced when, under MR,\n    the beech diameter increment is significantly lower in mixtures than in monocultures in 2020\n    or 2021 (I1) or over both years (I2).\n- id: fig5-beech-sugar-nbe-mr\n  statement: Under low soil moisture, beech showed a negative net biodiversity effect on sugar\n    concentration, driven by a negative complementarity effect.\n  source: Results, Impact of species interactions, paragraph 3; Figure 5C; Supplemental Figure S3C\n  quote: Similarly, a negative net biodiversity effect on sugar concentration in response to low\n    soil moisture was found in beech (Fig. 5), driven by a negative complementarity effect\n    (Supplemental Fig. S3)\n  criterion: Biodiversity effects procedure (opening comment). The Results give no year; the\n    Discussion (paragraph 8) places it in 2020 and calls the complementarity effect positive.\n    Reproduced when, for beech sugar under MR in 2020 or 2021, the NBE is negative and differs\n    from zero by the t-test, and the complementarity effect is negative and differs from zero;\n    the year and sign found are reported. The method readings (B1, B2, L1, L2) must agree; when\n    they do not, blocked as methods_underspecified.\n- id: oak-mr-no-interaction\n  statement: Under low soil moisture alone, oak showed no effect of species interactions and no\n    net biodiversity effect.\n  source: Results, Impact of species interactions, paragraph 3; Supplemental Table S3; Figure 5\n  quote: In contrast, we observed no impact of species interactions and net biodiversity effect in\n    oak (Supplemental Table S3, Fig. 5)\n  criterion: A claim of absence, on the paper's tests. Reproduced when, in oak under MR, no mixture\n    against monoculture contrast of the interaction test is significant for the six traits of\n    Figure 5 in 2020 or 2021, and no NBE differs from zero by the t-test (opening comment).\n    Readings I1, I2, B1, B2, L1 and L2; the outcome is the one all give.\n- id: tables3-beech-wmr-height\n  statement: Under combined warming and lower moisture, beech height increment was about 2 cm per\n    year larger in monocultures than in mixtures.\n  source: Results, Impact of species interactions, paragraph 4; Supplemental Table S3\n  quote: Under combined warming and lower moisture, a larger height increment by approximately 2 cm\n    per year was found in monocultures compared to the mixtures in beech (Supplemental Table S3)\n  statistics:\n  - about: warming by interaction, beech height increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 6.80\n    p: 0.009\n  - about: warming by moisture reduction by interaction, beech height increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 11.91\n    p: 0.001\n  expected:\n    quantity: beech height increment under WMR, monoculture minus mixture\n    value: 2\n    tolerance: 0.2\n    unit: cm per year\n  criterion: Interaction test (opening comment). Reproduced when, under WMR, beech height increment\n    is significantly larger in monocultures, with a difference within tolerance, in 2020 or 2021\n    (I1) or over both years (I2).\n- id: tables3-oak-wmr-diameter\n  statement: Under combined warming and lower moisture, oak diameter increment was 1.4 cm larger in\n    mixtures than in monocultures.\n  source: Results, Impact of species interactions, paragraph 4; Supplemental Table S3\n  quote: In oak, diameter increment was larger by 1.4 cm in mixtures compared to the monocultures\n    (Supplemental Table S3)\n  statistics:\n  - about: warming by year by interaction, oak diameter increment\n    test: linear mixed-effects model ANOVA\n    statistic: F = 4.15\n    p: 0.016\n  expected:\n    quantity: oak diameter increment under WMR, mixture minus monoculture\n    value: 1.4\n    tolerance: 0.14\n    unit: cm\n  criterion: Interaction test (opening comment), readings I1 and I2. The unit is open, as in\n    tables3-oak-warming-diameter, (u1) cm or (u2) mm. Reproduced when, under WMR, oak diameter\n    increment is significantly larger in mixtures with a difference within tolerance under one\n    reading.\n- id: fig5-oak-asat-nbe-wmr-2021\n  statement: Under combined warming and drier soils in 2021, oak showed a positive net biodiversity\n    effect on Asat, explained by complementarity.\n  source: Results, Impact of species interactions, paragraph 4; Figure 5F; Supplemental Figure S3F\n  quote: We also observed a positive net biodiversity effect for Asat in 2021 in oak (Fig. 5). This\n    effect was explained by complementarity effects, indicating a resource complementarity under\n    warmer air and drier soils (Supplemental Fig. S3)\n  criterion: Biodiversity effects procedure (opening comment). Reproduced when, for oak Asat under\n    WMR in 2021, the NBE and the complementarity effect are positive and differ from zero by the\n    t-test; partially reproduced when the NBE holds and the complementarity effect is positive\n    but not significant. Readings B1, B2, L1 and L2 must agree; when they do not, blocked as\n    methods_underspecified.\n- id: methods-treatment-magnitudes\n  statement: The treatments raised air temperature by 5.19 C (W) and 5.02 C (WMR) and reduced soil\n    moisture by 52.77% (MR) and 51.96% (WMR) relative to the control.\n  source: Materials and methods, Experimental set-up, paragraph 2; Figure 6\n  quote: an air warming treatment with an increase of around 5 °C (i.e. +5.19 ± 0.2 °C) relative\n    to the (ambient) air temperature in the control (W) ... a soil moisture reduction treatment\n    with a reduction of soil moisture of around 50% (i.e. −52.77 ± 9.7%) relative to the control\n    ... (WMR, i.e. +5.02 ± 0.2 °C and −51.96 ± 10.3%, Fig. 6, Supplemental Table S5)\n  expected:\n  - quantity: W air temperature minus C\n    value: 5.19\n    tolerance: 0.2\n    unit: degree C\n  - quantity: WMR air temperature minus C\n    value: 5.02\n    tolerance: 0.2\n    unit: degree C\n  - quantity: MR soil moisture change relative to C\n    value: -52.77\n    tolerance: 9.7\n    unit: percent\n  - quantity: WMR soil moisture change relative to C\n    value: -51.96\n    tolerance: 10.3\n    unit: percent\n  criterion: Tolerances are the paper's stated spreads. From the chamber records, treatment means\n    of daily means (n = 4 chambers per treatment, Figure 6). Open, the period (from June 2019 to\n    the end of 2021, or 2020 and 2021) and the air sensor (H1, H2). Reproduced when all four\n    values are within tolerance under one reading.\n- id: fig6-soil-moisture-mr-equals-wmr\n  statement: Soil moisture at 25 cm did not differ between the single and the combined treatments.\n  source: Discussion, paragraph 6; Figure 6E and 6F\n  quote: We found no differences in soil moisture conditions at 25 cm depth between single and\n    combined treatments (Fig. 6)\n  criterion: A claim of absence, on the paper's test, Tukey's HSD at alpha 0.05 on the averages\n    over the entire time per treatment (Figure 6 legend). Reproduced when MR and WMR do not differ;\n    W against C is shown as a variant. Open, the unit of the test, (a) chamber means over the\n    period (n = 4 per treatment) or (b) daily treatment means; the outcome is the one both give.\n- id: tables5-annual-climate\n  statement: Annual mean air temperature was about 12 C without warming and 16 to 17 C with\n    warming, and annual soil moisture about 10% without and 5% with moisture reduction, in 2020\n    and 2021.\n  source: Supplemental Table S5\n  inferred: Numbers from Supplemental Table S5 (annual rows, 2020 and 2021); no sentence states them\n    except the Discussion's maximum of 17 C in the warmed treatments in 2020.\n  expected:\n  - quantity: annual air temperature 2020, C\n    value: 11.8\n    tolerance: 0.4\n    unit: degree C\n  - quantity: annual air temperature 2020, MR\n    value: 12.1\n    tolerance: 0.4\n    unit: degree C\n  - quantity: annual air temperature 2020, W\n    value: 17.0\n    tolerance: 0.4\n    unit: degree C\n  - quantity: annual air temperature 2020, WMR\n    value: 16.8\n    tolerance: 0.4\n    unit: degree C\n  - quantity: annual air temperature 2021, C\n    value: 10.5\n    tolerance: 0.4\n    unit: degree C\n  - quantity: annual air temperature 2021, MR\n    value: 10.8\n    tolerance: 0.4\n    unit: degree C\n  - quantity: annual air temperature 2021, W\n    value: 15.7\n    tolerance: 0.4\n    unit: degree C\n  - quantity: annual air temperature 2021, WMR\n    value: 15.6\n    tolerance: 0.4\n    unit: degree C\n  - quantity: annual soil moisture 2020, C\n    value: 10.3\n    tolerance: 1.03\n    unit: percent\n  - quantity: annual soil moisture 2020, MR\n    value: 5.3\n    tolerance: 0.53\n    unit: percent\n  - quantity: annual soil moisture 2020, W\n    value: 10.3\n    tolerance: 1.03\n    unit: percent\n  - quantity: annual soil moisture 2020, WMR\n    value: 4.8\n    tolerance: 0.48\n    unit: percent\n  - quantity: annual soil moisture 2021, C\n    value: 10.0\n    tolerance: 1.0\n    unit: percent\n  - quantity: annual soil moisture 2021, MR\n    value: 4.6\n    tolerance: 0.46\n    unit: percent\n  - quantity: annual soil moisture 2021, W\n    value: 10.3\n    tolerance: 1.03\n    unit: percent\n  - quantity: annual soil moisture 2021, WMR\n    value: 4.8\n    tolerance: 0.48\n    unit: percent\n  criterion: Treatment means of the chamber records, January to December (Table S5). Air\n    temperature tolerances are the table's stated spread (0.4); the soil moisture spread is printed\n    as 0.0, below the table's precision, so 10% is used. The air sensor is open (H1, H2).\n    Reproduced when at least 14 of the 16 values are within tolerance under one reading;\n    partially reproduced for 10 to 13.\n- id: tables4-initial-sizes-similar\n  statement: Before the treatments began, tree height and diameter did not differ among the four\n    climatic treatments in either species.\n  source: Materials and methods, Experimental set-up, paragraph 2; Supplemental Table S4\n  quote: Tree sizes were statistically similar when delivered and planted (Supplemental Table S4)\n  expected:\n  - quantity: beech height, C\n    value: 66.7\n    tolerance: 13.2\n    unit: cm\n  - quantity: beech height, MR\n    value: 66.3\n    tolerance: 10.8\n    unit: cm\n  - quantity: beech height, W\n    value: 64.9\n    tolerance: 7.4\n    unit: cm\n  - quantity: beech height, WMR\n    value: 61.1\n    tolerance: 11.6\n    unit: cm\n  - quantity: oak height, C\n    value: 66.6\n    tolerance: 11.4\n    unit: cm\n  - quantity: oak height, MR\n    value: 65.3\n    tolerance: 14.7\n    unit: cm\n  - quantity: oak height, W\n    value: 64.3\n    tolerance: 13.2\n    unit: cm\n  - quantity: oak height, WMR\n    value: 68.9\n    tolerance: 12.9\n    unit: cm\n  - quantity: beech diameter, C\n    value: 6.0\n    tolerance: 1.6\n    unit: mm\n  - quantity: beech diameter, MR\n    value: 6.1\n    tolerance: 1.3\n    unit: mm\n  - quantity: beech diameter, W\n    value: 5.2\n    tolerance: 1.3\n    unit: mm\n  - quantity: beech diameter, WMR\n    value: 5.5\n    tolerance: 1.4\n    unit: mm\n  - quantity: oak diameter, C\n    value: 5.7\n    tolerance: 1.5\n    unit: mm\n  - quantity: oak diameter, MR\n    value: 5.5\n    tolerance: 1.5\n    unit: mm\n  - quantity: oak diameter, W\n    value: 5.4\n    tolerance: 1.5\n    unit: mm\n  - quantity: oak diameter, WMR\n    value: 5.8\n    tolerance: 1.3\n    unit: mm\n  criterion: Tolerances are the standard deviations Table S4 gives. Table S4 gives spring 2019\n    values. A claim of absence; the paper names no test. Readings (a) a one-way ANOVA of treatment\n    per species and trait, (b) the treatment test's model without year (opening comment), on\n    (c) the measured trees of monocultures and mixtures or (d) monocultures only, at p <= 0.05.\n    Reproduced when no reading finds a treatment difference in any species and trait, and the 16\n    means are within tolerance; blocked as methods_underspecified when readings differ.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml paper/10.1093-plphys-kiad565.txt; grep -n ": .*: " claims/dryad-4j0zpc8hz/*.yaml | grep -v "^\S*:[0-9]*:#" | head; grep -c "—\|rather" claims/dryad-4j0zpc8hz/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
39 38 17 38 39 13
```

**Agent**

I've written the claims file at `claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml`. The quote checker passes with 0 problems: 39 claims, 38 quotes and 38 statistical values. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC10828195), with the Results, Discussion, Methods, the legends of Figs. 1–7, and the full supplement (Supplemental Figs. S1–S7, Tables S1–S6, Methods S1–S4). No PDF was supplied, so I saw no figures. The paper links no code, so I read none.

**Claims:**
- **39 claims:** 38 have quotes. The one without is the Table S5 climate values, which no sentence states, so it has an `inferred` note.
- **Statistics:** 17 claims carry statistics, 38 entries in all. They are regression significance, the Fig. 1 P = 0.004, the mixed-model F tests from Tables S1, S2, S3 and S6, and Tukey thresholds.
- **Criteria and expected values:** all 39 claims have a criterion; 13 also have expected values.
- **Shared methods in the opening comment:** four procedures, each cited, which the criteria refer to: the phenology regression, the treatment test, the interaction test, and the biodiversity effects.

**Details the paper leaves open, with the readings named:**
- **Phenology regressions:** fitted on each tree and year against its chamber's mean, or on the eight treatment-year means as Fig. 1 plots them. Air sensor at 50 cm or at 2 m.
- **Treatment model:** fitted on 2019–2021, as the Methods and Table S1 say, or on the reported years 2020–2021. For negative increments under the square root: untransformed, or shifted so the minimum is zero.
- **Mixture against monoculture contrasts:** within each year, or pooled over both years.
- **Net biodiversity, complementarity and selection effects:**
  - Each mixture tree is compared either with the treatment's mean monoculture value or with the monoculture tree in its own chamber.
  - Leaf traits enter as yearly tree means or as per-campaign values.
  - The test is a t-test against zero (Methods), with Tukey's HSD (legends) as a variant.
- **Growing degree days (GDD):** the excess over 5 °C, or the daily means above 5 °C. Chilling days end at bud swelling (Methods) or at leaf flushing (Fig. 2 legend). The negative exponential has two parameters, or three with an asymptote.
- **"Least-squares analysis" (P = 0.004):** a species-by-temperature interaction on bud swelling, or on growing season length.
- **Which year:** not stated for the beech Asat selection effect, the beech sugar effect under low moisture, or the beech diameter effect under low moisture.
- **Which value "reached":** the ΨPD of −1.9 and −1.2 MPa could be the lowest yearly or campaign mean, under low moisture alone or also combined with warming.
- **Units:** the mixture diameter differences are printed in cm, but Table S4 gives diameters in mm. Both units are named.
- **Table S6:** species and years pooled, or per species.
- **Table S4:** the test is not named; a one-way ANOVA or the mixed model are named.
- **Treatment magnitudes:** the averaging period.

**Missing from the paper:**
- **Figure values:** the R² and P values inside Figs. 1, 2 and S1 could not be read without the PDF.
- **Equations 3–4 (complementarity and selection effects):** garbled in the extracted text. I recorded a Loreau and Hector reading.
- **AGWB coefficients:** not printed. They are outside data from Annighöfer et al. 2016, named in the header.
- **Two internal contradictions:** the Results call the complementarity effect behind oak AGWB under warming and beech sugar under low moisture negative, while the Discussion calls it positive. The criteria report the sign found.

## End of run

18 turns, 6 minutes, result: success.
