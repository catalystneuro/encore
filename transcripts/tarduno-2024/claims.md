# figshare-24639285 · claims · run 40570074554

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^## " docs/protocol.md; ls claims/001453/ paper/ claims/figshare-24639285 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 185
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-12`. Record this version in the attempt's provenance.
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
[... 165 more lines not kept]
```

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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41597-024-03626-0.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "24639285",
 "output_mode": "content"
}
```

```
targets/figshare.json:12:   "id": "24639285",
targets/figshare.json:14:   "url": "https://figshare.com/articles/dataset/Data_associated_with_Replicate_Apollo_sample_magnetizations_showing_evidence_for_impact_plasmas_and_absence_of_a_long-lived_dynamo_/24639285",
targets/figshare.json:15:   "doi": "10.6084/m9.figshare.24639285.v1",
```

**Agent calls Read**

```json
{
 "file_path": "targets/figshare.json",
 "limit": 40
}
```

```
1	{
2	 "schema_version": 1,
3	 "archive": "figshare",
4	 "generated": "2026-10-27T02:42:30+00:00",
5	 "source": "https://api.figshare.com/v2, chosen by hand (tools/build_figshare_targets.py)",
6	 "note": "Scientific Data deposits outside neuroscience and ecology, chosen by hand to test the pipeline on a general-purpose repository.",
7	 "counts": {
8	  "with_a_paper": 3
9	 },
10	 "targets": [
11	  {
12	   "id": "24639285",
13	   "name": "Data associated with \"Replicate Apollo sample magnetizations showing evidence for impact plasmas and absence of a long-lived dynamo\"",
14	   "url": "https://figshare.com/articles/dataset/Data_associated_with_Replicate_Apollo_sample_magnetizations_showing_evidence_for_impact_plasmas_and_absence_of_a_long-lived_dynamo_/24639285",
15	   "doi": "10.6084/m9.figshare.24639285.v1",
16	   "published_version": "1",
17	   "versions": 1,
18	   "item_type": "dataset",
19	   "published": "2024-04-10",
20	   "license": "https://creativecommons.org/licenses/by/4.0/",
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims | grep -i -E "figshare|dryad|zenodo" | head; sed -n 1,80p tools/claims_check.py | head -60; grep -n -i "figshare\|kind:\|data:" docs/archives.md | head -30
```

```
dryad-4j0zpc8hz
dryad-bvq83bkk9
dryad-tdz08kq5d
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
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/dryad-4j0zpc8hz; head -40 claims/dryad-4j0zpc8hz/*.yaml; python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
```

```
10.1093-plphys-kiad565.yaml
# Claims for Didion-Gency, Vitasse, Buchmann, Gessler, Gisler, Schaub & Grossiord (2024), Plant
# Physiology 194, doi:10.1093/plphys/kiad565, on Dryad dataset 4j0zpc8hz (doi:10.5061/dryad.4j0zpc8hz).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
# protocol pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read: the version of record from Europe PMC (PMC10828195, full-text XML) as supplied under
# paper/, with Results, Discussion, Materials and methods, the legends of Figures 1 to 7, and the
# supplement (kiad565_supplementary_data.pdf as extracted text) with the legends of Supplemental
# Figures S1 to S7, Supplemental Tables S1 to S6 and Supplemental Methods S1 to S4. No PDF was
# supplied, so the figures were not seen. The R2 and P values printed inside Figures 1, 2 and S1
# are therefore not recorded. Equations 3 and 4 of Supplemental Methods S4 (complementarity and
# selection effects) are garbled in the extracted text (an averaging bar is lost). The paper links
# no analysis code (analyses in R 4.2.0, nlme lme and multcomp), so none was read.
#
# Data the paper used. Open-top chambers (OTCs) at WSL Birmensdorf, 16 chambers, each with eight
# soil compartments. Seedlings of European beech (Fagus sylvatica) and downy oak (Quercus
# pubescens), 3 yr old, planted October 2018 as single trees, monocultures (four trees of one
# species) and mixtures (two of each); only monocultures and mixtures are analysed, one tree per
# species measured per compartment. Four climatic treatments from June 2019, each in four
[... 170 more lines not kept]
```

**Agent**

The full text is present (Scientific Data descriptor: Methods, Tables 1 and 2, figure legends; no code, no supplement beyond the Figshare deposit itself). Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml",
 "content": "# Claims for Tarduno, Cottrell & Zhou (2024), Scientific Data, doi:10.1038/s41597-024-03626-0,\n# on Figshare dataset 24639285 (doi:10.6084/m9.figshare.24639285.v1).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-10-27,\n# protocol pilot-12 as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record from Europe PMC (PMC11271266, full-text XML converted to text)\n# as supplied under paper/, with Background & Summary, Methods, Data Records, Technical\n# Validation, the legends of Figures 1 to 3 and Tables 1 and 2. The paper is a Data Descriptor\n# and has no supplement; its additional plots are in the Figshare deposit itself. No PDF was\n# supplied, so the figures were not seen: the nominal paleointensities printed in Figure 1 and\n# the step ranges marked by arrows in Figures 1 and 2 are not recorded. The footnote legends of\n# both tables (the marks after \"M590 20 uT\" and \"Max intensity\" in Table 1, and the marks after\n# the specimen names, after n and after T Range in Table 2) are missing from the text.\n# Code: the paper states that no custom code was used. It names PmagPy for looking at the\n# directional and paleointensity data during collection and for checking quality factors\n# (Technical Validation), with no version; no repository was read.\n#\n# Data the paper used. Two sets of measurements, all made with the WSGI three-component DC SQUID\n# magnetometer (6.3 mm bore) in the shielded room at the University of Rochester, moments in emu.\n# Per the Data Records, each sample's data are a sheet of an Excel file with columns sample name,\n# demagnetization step, moment (emu), declination and inclination; AF steps carry an \"mT\" label,\n# all other steps are degrees Celsius.\n# (1) Glass of Apollo 64455,24: mm and smaller subsamples (ss numbers, one \"g2\", one printed\n# \"s11\"), Thellier-Coe paired heating with a CO2 laser (90 s for specimens under 1 mm, 120 s for\n# 1 to 2 mm), laboratory field 18 uT (Figure 1 legend). Step labels are the step temperature\n# followed by .0 (field-off), .1 (field-on) and .2 (pTRM check, field-on). 25 subsamples in all,\n# 13 measured in 2014 and 2015 without AF pre-treatment and 12 later with AF demagnetization along\n# six directions at 5 and 10 mT (some also at 2.5, 7.5 and 20 mT); three passed the selection\n# criteria of Tarduno et al. (ref. 1) and the 22 that failed are the ones presented (Table 2).\n# (2) Single silicate crystals (feldspar or pyroxene) from Apollo 14053,262, 12021,30, 12053,283,\n# 12040,209 and 71055,2, twelve crystals named as in Table 1 (12021g2, 12021g3, 12040g1 to g3,\n# 12053g1, 12053g2, 14053g1 to g3, 71055g1, 71055g3). Each: NRM, then 590 C in zero field (label\n# 590.0), 590 C in a 20 uT field (590.1), 590 C in zero field as alteration check (590.3), 590 C\n# in a 40 uT field (590.4). The NRM, 590.0 and 590.3 steps were measured several times\n# (replicates). One crystal, 14053g1, was also measured after 400 C during initial tests.\n# The magnetometer sensitivity threshold is 8e-11 emu (8e-14 A m2).\n#\n# Procedures used by the criteria below, each from the paper as cited.\n# - TRM (pTRM) gained at a step is the vector subtraction of the field-on and field-off\n#   measurements (Methods, Thermal measurements, paragraph 3). NRM lost is read from the\n#   field-off measurements; whether it is NRM minus the remaining moment or plotted as remaining\n#   does not change R2, MAD or the slope magnitude.\n# - Paleointensity is the absolute slope of the NRM lost against TRM gained line times the\n#   laboratory field, 18 uT for the glass (Figure 1 legend).\n# - Selection criteria (Methods, Paleointensity Selection criteria): linear NRM-TRM relationship\n#   with R2 about 0.9, four or more points, evenly distributed, pTRM checks within 15%, MAD\n#   threshold relaxed (no value given), a three-point sliding window on orthogonal vector plots.\n# - Threshold field detection limit (Technical Validation) = 8e-14 A m2 / TRM at 590 C x 20 uT.\n#\n# Open details, named here and in the criteria that use them.\n# - MAD: the paper says neither whether the line is anchored to the origin nor whether it is fit\n#   to the three-point smoothed directions. Readings (a) free line on the measured field-off\n#   directions, (b) anchored line, (c) free line on the three-point running mean of the\n#   field-off vectors.\n# - pTRM check percentage: the paper gives no formula. It cites \"standard paleointensity\n#   definitions\" (ref. 31) without detail here. Readings (a) difference between the check's pTRM\n#   and the original pTRM at the same temperature, over the original pTRM; (b) the same\n#   difference over the length of the fitted TRM segment (a DRAT-like measure). The check's pTRM\n#   is the .2 vector minus (i) the field-off vector measured just before it, or (ii) the\n#   field-off vector at the check's temperature.\n# - M590 in Table 1: (a) the TRM vector difference 590.1 minus 590.0, (b) the magnitude of the\n#   590.1 measurement. Which replicate of 590.0 is used: (i) the first, which the paper says was\n#   used for the nominal paleointensities of ref. 1, (ii) the mean of the replicates.\n# - Consistency of replicate directions: the paper names no measure, only stereonets. Readings\n#   (a) Fisher precision parameter k of the replicate directions compared between steps, (b)\n#   Watson's test of randomness on the replicates at p < 0.05 (a standard test, not named by the\n#   paper).\n#\n# Table 2 marks. Twelve specimens carry one mark and ten another; with the three successful\n# specimens these split 13 and 12, the counts the Methods give for experiments without and with\n# AF pre-treatment, and ss19 and ss43, which Figure 1 shows with AF steps, carry the second mark.\n# The legend is missing, so this reading is not stated by the paper.\n#\n# Text errors noted. The Results cite Figure 3 for \"12041g1\"; the Figure 3 legend and Table 1 have\n# 12040g1. The Technical Validation example for 14053g1 uses a TRM of 8e-12 A m2 and gives 0.2 uT,\n# while Table 1 gives 14053g1 3.203E-09 emu (3.2e-12 A m2) and 0.51 uT; the example's numbers\n# are those of 12040g1 in Table 1 (8.002E-09 emu, 0.20 uT). Table 1 values are 1 to 3% above\n# 8e-11 / M590 x 20 uT computed from its own M590 column.\nschema_version: 2\ndataset:\n  archive: figshare\n  id: \"24639285\"\n  doi: 10.6084/m9.figshare.24639285.v1\npaper: doi:10.1038/s41597-024-03626-0\nclaims:\n- id: glass-specimen-set\n  kind: link\n  statement: The deposit holds the measurements of the 22 Apollo 64455 glass subsamples that\n    failed the paleointensity selection criteria, named as in Table 2, and replicate measurements\n    for the twelve single crystals of Table 1.\n  source: Background & Summary, Glass, paragraph 2; Methods, paragraph 2; Table 2; Data Records\n  quote: Plots for all the data not meeting paleointensity criteria1 (n=22) are provided26 with\n    photomicrographs of specimens that were measured\n  expected:\n  - quantity: glass subsamples failing the selection criteria\n    value: 22\n    tolerance: 0\n  - quantity: single crystals with replicate measurements\n    value: 12\n    tolerance: 0\n  criterion: Specimens are matched by the names in Table 2 and Table 1 (s11 in Table 2 may be\n    ss11; both are accepted). Holds when each named specimen has measurements with steps,\n    moments, declinations and inclinations as the Data Records describe. Reported either way:\n    which glass specimens have AF steps, compared with the reading of the Table 2 marks given\n    in the opening comment (12 without, 10 with).\n- id: glass-success-rate\n  statement: Of the Apollo 64455 glass subsamples given thermal paleointensity experiments, 12%\n    passed the selection criteria (3 of 25, 13 run without and 12 with AF pre-treatment).\n  source: Background & Summary, paragraph 3; Methods, paragraph 2\n  quote: In the thermal studies1 of Apollo 64455 (Methods), the success rate was 12%\n  expected:\n  - quantity: success rate\n    value: 12\n    tolerance: 1.2\n    unit: percent\n  - quantity: glass subsamples without AF pre-treatment\n    value: 13\n    tolerance: 0\n  - quantity: glass subsamples with AF pre-treatment\n    value: 12\n    tolerance: 0\n  criterion: The three successful specimens are in ref. 1 and its dataset, not in this deposit,\n    so the rate is 3 over (3 plus the failed specimens found here). The split by AF\n    pre-treatment is counted from AF steps in the deposit's failed specimens plus the Methods'\n    count of successful ones (one without, two with AF). Holds when 22 failed specimens are\n    found and 10 of them have AF steps.\n  depends_on:\n  - glass-specimen-set\n- id: table2-fit-statistics\n  statement: For the nine failed glass specimens with a line fit (ss19, ss43, ss22, ss41, ss6,\n    ss9, ss10, ss30, ss34), the number of points, temperature range, MAD, R2 and pTRM check\n    differences are as in Table 2, and the failure criteria listed follow from them.\n  source: Methods, Paleointensity Selection criteria, paragraph 2; Table 2\n  quote: Reasons for de-selection are provided in Table 2\n  inferred: The numbers are in Table 2 only; no sentence states them.\n  expected:\n  - quantity: ss19 MAD (175-450 C, n 4)\n    value: 30.1\n    tolerance: 3.0\n    unit: degrees\n  - quantity: ss19 R2\n    value: 0.94\n    tolerance: 0.094\n  - quantity: ss43 MAD (250-400 C, n 3)\n    value: 10.0\n    tolerance: 1.0\n    unit: degrees\n  - quantity: ss43 R2\n    value: 0.90\n    tolerance: 0.09\n  - quantity: ss22 MAD (250-500 C, n 4)\n    value: 35.4\n    tolerance: 3.5\n    unit: degrees\n  - quantity: ss22 R2\n    value: 0.38\n    tolerance: 0.038\n  - quantity: ss41 MAD (500-580 C, n 3)\n    value: 24.0\n    tolerance: 2.4\n    unit: degrees\n  - quantity: ss41 R2\n    value: 0.38\n    tolerance: 0.038\n  - quantity: ss6 MAD (175-360 C, n 3)\n    value: 21.0\n    tolerance: 2.1\n    unit: degrees\n  - quantity: ss6 R2\n    value: 0.91\n    tolerance: 0.091\n  - quantity: ss9 MAD (250-550 C, n 4)\n    value: 37.6\n    tolerance: 3.8\n    unit: degrees\n  - quantity: ss9 R2\n    value: 0.74\n    tolerance: 0.074\n  - quantity: ss10 MAD (360-550 C, n 3)\n    value: 42.9\n    tolerance: 4.3\n    unit: degrees\n  - quantity: ss10 R2\n    value: 0.15\n    tolerance: 0.015\n  - quantity: ss30 MAD (175-500 C, n 4)\n    value: 12.5\n    tolerance: 1.25\n    unit: degrees\n  - quantity: ss30 R2\n    value: 0.59\n    tolerance: 0.059\n  - quantity: ss34 MAD (100-450 C, n 5)\n    value: 12.1\n    tolerance: 1.2\n    unit: degrees\n  - quantity: ss34 R2\n    value: 0.06\n    tolerance: 0.006\n  - quantity: pTRM check differences, as listed per temperature in Table 2 for these nine\n      specimens (for example ss19 30% at 250 C and 9% at 450 C)\n    value: 1\n    tolerance: 0.1\n    unit: ratio of computed to printed percentage\n  criterion: Per specimen, the field-off and field-on steps within the Table 2 temperature range\n    (the range and n fix the points), NRM lost against TRM gained as in the opening comment, R2\n    of the least-squares line, MAD of a principal component fit to the field-off directions,\n    and the pTRM check percentage at each listed temperature. MAD and pTRM check percentages\n    are computed under each reading named in the opening comment; a value matches when one\n    reading puts it within tolerance. Reproduced when n matches for all nine and at least 80%\n    of the MAD, R2 and pTRM values match; partially reproduced for 50 to 80%. A 10% tolerance\n    on R2 near 0.06 or 0.15 is narrow; values within 0.03 of these two are also counted as\n    matching, as R2 is printed to two places. Whether each listed failure follows is reported\n    against the stated thresholds (n of 4 or more, pTRM within 15%, R2 about 0.9), not judged,\n    as ss6 is listed as failing R2 at 0.91 while ss43 at 0.90 is not, and no MAD threshold is\n    given.\n- id: table2-no-fit\n  statement: The other thirteen failed glass specimens (g2, ss8, s11, ss18, ss24, ss27, ss29,\n    ss36, ss38, ss39, ss45, ss46, ss48) gave no fit, most because they did not acquire TRM in a\n    regular fashion and some because their directions trend out of the origin.\n  source: Methods, Paleointensity Selection criteria, paragraph 2; Table 2\n  quote: We note that some specimens did not acquire TRM in a regular fashion, or showed directions\n    that trended out of, rather toward, the origin of their respective orthogonal vector plots\n  criterion: The paper gives no measure of regular TRM acquisition. Over each specimen's Table 2\n    range, TRM gained per step is computed as in the opening comment and the pTRM check\n    percentages listed for these specimens are compared with Table 2 as in table2-fit-statistics.\n    Regularity is read as (a) TRM gained increasing with each temperature step, or (b) a TRM\n    gained against temperature curve with no step falling by more than 15% (the pTRM tolerance\n    of the selection criteria). Reproduced when, under one reading, at least 9 of the 11\n    specimens marked \"no regular TRM acquisition\" show irregular acquisition, and ss36 and ss39\n    have field-off vectors whose distance from the origin grows over the last steps of the range.\n    The counts under each reading are reported.\n- id: fig1-linear-components\n  statement: Glass subsamples ss43 and ss19, which failed the reliability criteria, show hints of\n    linear directional components on orthogonal vector plots, from which nominal paleointensities\n    can be calculated with the 18 uT laboratory field.\n  source: Background & Summary, Glass, paragraph 2; Figure 1\n  quote: some of these data reveal linear directional components, and nominal paleointensities can\n    be calculated (Fig. 1)\n  criterion: Over the Table 2 ranges (ss43 250 to 400 C, ss19 175 to 450 C), MAD and R2 as in\n    table2-fit-statistics, and the nominal paleointensity as the absolute slope times 18 uT\n    (Figure 1 legend). The figure's values were not seen (no PDF), so none is expected. Holds\n    when both MADs and R2 values match Table 2 under one reading; the nominal paleointensities\n    are reported under each reading.\n  depends_on:\n  - table2-fit-statistics\n- id: fig2-changing-field\n  statement: Glass subsamples ss41 and ss22 show field-off directions that change over a\n    temperature interval, consistent with a changing ambient field during magnetization, and\n    curved NRM lost against TRM gained plots.\n  source: Background & Summary, Glass, paragraph 2; Figure 2; Table 2\n  quote: Other specimens show a changing vector, consistent with a changing ambient field (Fig. 2)\n  criterion: The arrows marking the interval in Figure 2 were not seen, so the Table 2 ranges\n    are used (ss41 500 to 580 C, ss22 250 to 500 C), with the earlier steps shown. The paper\n    names no measure of a changing direction. Readings (a) the angle between the first and the\n    last field-off direction of the range exceeds the MAD of a line fit over the range, (b) a\n    great-circle fit over the range has a smaller MAD than a line fit. Reproduced when both\n    specimens show a changing direction under one reading and R2 is within tolerance of Table 2\n    (0.38 each); the angles and MADs are reported.\n  depends_on:\n  - table2-fit-statistics\n- id: glass-directions-not-random\n  statement: The field-off directions of the failed glass specimens, as seen on orthogonal vector\n    plots, are not random, implying the presence of an ambient field.\n  source: Background & Summary, Glass, paragraph 2\n  quote: The directions, as viewed on orthogonal vector plots, are not random and imply the presence\n    of an ambient field\n  criterion: The paper names no test. Per specimen, the field-off directions of its thermal steps\n    are tested for randomness with Watson's test (n directions, resultant length R, p < 0.05),\n    a standard choice. Reproduced when more than half of the 22 specimens reject randomness,\n    partially reproduced for a quarter to a half. Because successive demagnetization steps of\n    one remanence are not independent, the count is also given for the steps within each\n    specimen's Table 2 range where one is printed.\n  depends_on:\n  - glass-specimen-set\n- id: glass-af-no-change\n  statement: For nearly all glass samples given AF pre-treatment, AF cleaning did not\n    significantly change the NRM direction or magnitude.\n  source: Methods, paragraph 2\n  quote: For nearly all samples, AF cleaning did not significantly change the NRM direction or\n    magnitude\n  criterion: Per specimen with AF steps, the angle between the NRM direction and the direction\n    after the last AF step, and the ratio of the moments. The paper gives no threshold for\n    \"significantly\". Readings (a) angle under 15 degrees and moment change under 15% (the pTRM\n    check tolerance of the selection criteria), (b) angle under the specimen's Table 2 MAD where\n    one is printed and moment change under 15%. Reproduced when, under one reading, all but at\n    most two of the AF-treated specimens show no significant change.\n  depends_on:\n  - glass-specimen-set\n- id: table1-max-intensity\n  statement: For each of the twelve single crystals, the maximum field that cannot be excluded,\n    given the magnetometer threshold of 8e-11 emu and the moment acquired at 590 C in a 20 uT\n    field, is as in Table 1, between 0.20 and 0.51 uT.\n  source: Results, Single crystal measurements, paragraph 4; Table 1; Technical Validation,\n    Example of threshhold detection limit\n  quote: Considering a magnetometer threshold value (see Methods) the maximum field that cannot be\n    excluded by the data can be calculated from the data for each crystal. These values are\n    presented in Table 1\n  expected:\n  - {quantity: 12021g2 M590 20 uT, value: 7.011e-9, tolerance: 7.0e-10, unit: emu}\n  - {quantity: 12021g2 max intensity, value: 0.23, tolerance: 0.023, unit: uT}\n  - {quantity: 12021g3 M590 20 uT, value: 6.292e-9, tolerance: 6.3e-10, unit: emu}\n  - {quantity: 12021g3 max intensity, value: 0.26, tolerance: 0.026, unit: uT}\n  - {quantity: 12040g1 M590 20 uT, value: 8.002e-9, tolerance: 8.0e-10, unit: emu}\n  - {quantity: 12040g1 max intensity, value: 0.20, tolerance: 0.020, unit: uT}\n  - {quantity: 12040g2 M590 20 uT, value: 6.021e-9, tolerance: 6.0e-10, unit: emu}\n  - {quantity: 12040g2 max intensity, value: 0.27, tolerance: 0.027, unit: uT}\n  - {quantity: 12040g3 M590 20 uT, value: 6.292e-9, tolerance: 6.3e-10, unit: emu}\n  - {quantity: 12040g3 max intensity, value: 0.26, tolerance: 0.026, unit: uT}\n  - {quantity: 12053g1 M590 20 uT, value: 5.283e-9, tolerance: 5.3e-10, unit: emu}\n  - {quantity: 12053g1 max intensity, value: 0.31, tolerance: 0.031, unit: uT}\n  - {quantity: 12053g2 M590 20 uT, value: 7.982e-9, tolerance: 8.0e-10, unit: emu}\n  - {quantity: 12053g2 max intensity, value: 0.20, tolerance: 0.020, unit: uT}\n  - {quantity: 14053g1 M590 20 uT, value: 3.203e-9, tolerance: 3.2e-10, unit: emu}\n  - {quantity: 14053g1 max intensity, value: 0.51, tolerance: 0.051, unit: uT}\n  - {quantity: 14053g2 M590 20 uT, value: 5.294e-9, tolerance: 5.3e-10, unit: emu}\n  - {quantity: 14053g2 max intensity, value: 0.31, tolerance: 0.031, unit: uT}\n  - {quantity: 14053g3 M590 20 uT, value: 4.523e-9, tolerance: 4.5e-10, unit: emu}\n  - {quantity: 14053g3 max intensity, value: 0.36, tolerance: 0.036, unit: uT}\n  - {quantity: 71055g1 M590 20 uT, value: 3.883e-9, tolerance: 3.9e-10, unit: emu}\n  - {quantity: 71055g1 max intensity, value: 0.42, tolerance: 0.042, unit: uT}\n  - {quantity: 71055g3 M590 20 uT, value: 4.202e-9, tolerance: 4.2e-10, unit: emu}\n  - {quantity: 71055g3 max intensity, value: 0.39, tolerance: 0.039, unit: uT}\n  criterion: Max intensity = 8e-11 emu / M590 x 20 uT (Technical Validation). M590 is computed\n    under the readings named in the opening comment, (a) or (b) crossed with (i) or (ii).\n    Reproduced when, under one reading, all 24 values are within tolerance; partially\n    reproduced when at least 18 are. The reading that matches is reported, and whether Table 1\n    max intensities equal the formula applied to its own M590 column to two places.\n- id: baseline-range\n  statement: The maximum fields that the single crystal data cannot exclude define a baseline of\n    about 0.2 to 0.5 uT below which fields cannot be evaluated with these data.\n  source: Background & Summary, paragraph 6\n  quote: they nevertheless define a baseline of ~0.2 to ~0.5 μT below which fields cannot be\n    evaluated with the present data\n  expected:\n    quantity: range of max intensity over the twelve crystals\n    value: [0.2, 0.5]\n    tolerance: [0.02, 0.05]\n    unit: uT\n  criterion: Holds when the lowest and highest of the twelve values computed in\n    table1-max-intensity, under the reading that matches there, lie in 0.18 to 0.22 and 0.45 to\n    0.55 uT.\n  depends_on:\n  - table1-max-intensity\n- id: example-14053g1-threshold\n  statement: For crystal 14053g1, the threshold field detection limit computed from the\n    magnetometer sensitivity (8e-14 A m2) and a TRM at 590 C of 8e-12 A m2 in a 20 uT field is\n    0.2 uT.\n  source: Technical Validation, Example of threshhold detection limit\n  quote: Threshold field detection = Magnetometer sensitivity (8 × 10−14 A m2) / TRM590o (8 × 10−12\n    A m2) × Lab Field (20 μT) = 0.2 μT\n  expected:\n  - quantity: 14053g1 TRM at 590 C in 20 uT\n    value: 8.0e-12\n    tolerance: 8.0e-13\n    unit: A m2\n  - quantity: 14053g1 threshold field\n    value: 0.2\n    tolerance: 0.02\n    unit: uT\n  criterion: The example conflicts with Table 1, which gives 14053g1 3.203E-09 emu and 0.51 uT.\n    Readings (a) the example as written, for 14053g1; (b) a misprint of the crystal name, the\n    numbers belonging to 12040g1 (8.002E-09 emu, 0.20 uT in Table 1). TRM computed as in\n    table1-max-intensity. Reproduced as written when reading (a) matches; when only (b) matches,\n    the claim is reported as matching the misprint reading, with the 14053g1 values shown.\n  depends_on:\n  - table1-max-intensity\n- id: fig3-nrm-consistent\n  statement: For most crystals the replicate NRM measurements have a consistent direction, as\n    shown on stereonets for 12040g1 and 14053g2.\n  source: Results, Single crystal measurements, paragraph 2; Figure 3a and 3d\n  quote: These show that for most of the crystals there is consistency of the NRM direction (Fig.\n    3a,d)\n  criterion: Per crystal, the replicate NRM (step 0.0) directions, with Fisher mean, k and\n    alpha95. Readings for \"consistent\", named in the opening comment, (a) k of the NRM replicates\n    higher than k of the 590.0 replicates, (b) Watson's test rejects randomness of the NRM\n    replicates at p < 0.05. Reproduced when, under one reading, more than half of the twelve\n    crystals are consistent, including 12040g1 and 14053g2.\n  depends_on:\n  - glass-specimen-set\n- id: fig3-590-inconsistent\n  statement: After demagnetization at 590 C in zero field, the replicate directions of the\n    crystals are inconsistent, consistent with a null magnetization state.\n  source: Results, Single crystal measurements, paragraph 2; Figure 3b and 3e; Methods, Thermal\n    measurements, paragraph 5\n  quote: but this consistency is not seen after demagnetization at 590 °C (Fig. 3b,e)\n  criterion: Per crystal, the replicate 590.0 directions, with Fisher mean, k and alpha95. Readings\n    (a) k of the 590.0 replicates lower than k of the NRM replicates, (b) Watson's test does not\n    reject randomness of the 590.0 replicates at p < 0.05. Reproduced when, under one reading,\n    more than half of the twelve crystals are inconsistent, including 12040g1 and 14053g2. The\n    590.0 moments are reported against the 8e-11 emu threshold.\n  depends_on:\n  - fig3-nrm-consistent\n- id: fig3-alteration-check-inconsistent\n  statement: The replicate directions after the zero-field alteration check at 590 C are also\n    inconsistent.\n  source: Results, Single crystal measurements, paragraph 2; Figure 3c and 3f\n  quote: The directions are also inconsistent after the alteration check at 590 °C (Fig. 3c,f)\n  criterion: As fig3-590-inconsistent, for the replicate 590.3 directions.\n  depends_on:\n  - fig3-590-inconsistent\n- id: crystal-14053g1-400c-stable\n  statement: Crystal 14053g1, measured after heating to 400 C during initial tests, held a stable\n    remanence, which was removed by treatment at 590 C.\n  source: Results, Single crystal measurements, paragraph 3\n  quote: One crystal (14053g1) was measured after heating to an intermediate temperature (400 °C)\n    during initial tests, and found to be stable\n  criterion: Applies only if the deposit holds 400 C measurements for 14053g1. The paper names no\n    measure of stability; stable is read, as for the NRM, as replicate 400 C directions\n    consistent under fig3-nrm-consistent's readings, with the 590.0 replicates of the same\n    crystal inconsistent. Reproduced when both hold under one reading.\n  depends_on:\n  - fig3-nrm-consistent\n- id: no-alteration-recording-efficiency\n  statement: Alteration during the laser heating of the single crystals was not significant;\n    apparent recording efficiencies far above 100% were not observed and the alteration checks\n    did not fail.\n  source: Background & Summary, paragraph 5\n  quote: If alteration had resulted in the formation of new magnetic minerals, apparent recording\n    efficiencies ≫ 100% should have be observed (but these were not), and alteration checks\n    should fail\n  criterion: The paper does not define recording efficiency or the failure of the alteration\n    check for the crystals. Readings (a) the 590.3 moment does not exceed the 590.0 moment by\n    more than the 8e-11 emu threshold, and the 590.3 directions are inconsistent as in\n    fig3-alteration-check-inconsistent; (b) the 590.4 TRM (40 uT, vector difference from 590.3)\n    is no more than about twice the 590.1 TRM (20 uT), as linear recording predicts. Reproduced\n    when every crystal passes under one reading; the ratios are reported. Recording efficiency\n    against a theoretical TRM needs grain properties the paper does not give, so it is not\n    computed.\n  depends_on:\n  - fig3-alteration-check-inconsistent\n- id: interpretation-impact-no-dynamo\n  statement: Together with ref. 1, the data are consistent with impact plasma magnetization of the\n    64455 glass and with the absence of a long-lived lunar core dynamo recorded in the 3.9 to\n    3.2 Ga crystals.\n  source: Background & Summary, paragraphs 2 and 6\n  quote: These 64455 field strengths1 match those predicted by the charge separation mechanism\n  criterion: An interpretation that rests on ref. 1 and on models of impact plasmas, not on a\n    measurement this deposit can repeat. Not tested; it is judged as following from the\n    outcomes of fig2-changing-field, glass-directions-not-random, fig3-590-inconsistent and\n    table1-max-intensity, which are reported together.\n  data: elsewhere\n  depends_on:\n  - fig2-changing-field\n  - glass-directions-not-random\n  - fig3-590-inconsistent\n  - table1-max-intensity\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i '/^  data: elsewhere$/d' claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml; python tools/claims_check.py claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml paper/10.1038-s41597-024-03626-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml; grep -n ': .*: ' $f | grep -v '^[0-9]*:#' | grep -v '{quantity'
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  f=claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml; grep -nE '[^ ]: ' $f | grep -vE '^[0-9]+:#' | grep -vE '^[0-9]+: *(- )?[a-z_]+: '
```

```
300:  - {quantity: 12021g2 M590 20 uT, value: 7.011e-9, tolerance: 7.0e-10, unit: emu}
301:  - {quantity: 12021g2 max intensity, value: 0.23, tolerance: 0.023, unit: uT}
302:  - {quantity: 12021g3 M590 20 uT, value: 6.292e-9, tolerance: 6.3e-10, unit: emu}
303:  - {quantity: 12021g3 max intensity, value: 0.26, tolerance: 0.026, unit: uT}
304:  - {quantity: 12040g1 M590 20 uT, value: 8.002e-9, tolerance: 8.0e-10, unit: emu}
305:  - {quantity: 12040g1 max intensity, value: 0.20, tolerance: 0.020, unit: uT}
306:  - {quantity: 12040g2 M590 20 uT, value: 6.021e-9, tolerance: 6.0e-10, unit: emu}
307:  - {quantity: 12040g2 max intensity, value: 0.27, tolerance: 0.027, unit: uT}
308:  - {quantity: 12040g3 M590 20 uT, value: 6.292e-9, tolerance: 6.3e-10, unit: emu}
309:  - {quantity: 12040g3 max intensity, value: 0.26, tolerance: 0.026, unit: uT}
310:  - {quantity: 12053g1 M590 20 uT, value: 5.283e-9, tolerance: 5.3e-10, unit: emu}
311:  - {quantity: 12053g1 max intensity, value: 0.31, tolerance: 0.031, unit: uT}
312:  - {quantity: 12053g2 M590 20 uT, value: 7.982e-9, tolerance: 8.0e-10, unit: emu}
313:  - {quantity: 12053g2 max intensity, value: 0.20, tolerance: 0.020, unit: uT}
314:  - {quantity: 14053g1 M590 20 uT, value: 3.203e-9, tolerance: 3.2e-10, unit: emu}
315:  - {quantity: 14053g1 max intensity, value: 0.51, tolerance: 0.051, unit: uT}
316:  - {quantity: 14053g2 M590 20 uT, value: 5.294e-9, tolerance: 5.3e-10, unit: emu}
317:  - {quantity: 14053g2 max intensity, value: 0.31, tolerance: 0.031, unit: uT}
318:  - {quantity: 14053g3 M590 20 uT, value: 4.523e-9, tolerance: 4.5e-10, unit: emu}
319:  - {quantity: 14053g3 max intensity, value: 0.36, tolerance: 0.036, unit: uT}
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml; grep -nE ':$' $f | grep -vE '^[0-9]+:#' | grep -vE '^[0-9]+: *(- )?[a-z_]+:$'
```

```
103:    moments, declinations and inclinations as the Data Records describe. Reported either way:
```

**Agent calls Bash**

```bash
cd  f=claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml; sed -i '103s/Reported either way:$/Reported either way,/' $f; python tools/claims_check.py $f paper/10.1038-s41597-024-03626-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs']['expected'],indent=1))"; grep -n -B2 -A4 "range" claims/dryad-*/*.yaml | grep -A4 "expected" | head -30
```

```
{
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
   "type": "string"
[... 3 more lines not kept]
```

**Agent**

Ranges go in as two entries. Fixing both schema problems.

**Agent calls Bash**

```bash
cd  f=claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml; python - "$f" <<'EOF'
import sys
p=sys.argv[1]; s=open(p).read()
s=s.replace("""  inferred: The numbers are in Table 2 only; no sentence states them.
""","")
s=s.replace(""" A 10% tolerance on R2 near 0.06 or 0.15 is narrow; values within 0.03 of these two are also counted as
    matching, as R2 is printed to two places.""","")
old="""  expected:
    quantity: range of max intensity over the twelve crystals
    value: [0.2, 0.5]
    tolerance: [0.02, 0.05]
    unit: uT
"""
new="""  expected:
  - quantity: lowest max intensity over the twelve crystals
    value: 0.2
    tolerance: 0.02
    unit: uT
  - quantity: highest max intensity over the twelve crystals
    value: 0.5
    tolerance: 0.05
    unit: uT
"""
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
grep -n "narrow\|inferred" $f; python tools/claims_check.py $f paper/10.1038-s41597-024-03626-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml",
 "offset": 205,
 "limit": 10
}
```

```
205	    (the range and n fix the points), NRM lost against TRM gained as in the opening comment, R2
206	    of the least-squares line, MAD of a principal component fit to the field-off directions,
207	    and the pTRM check percentage at each listed temperature. MAD and pTRM check percentages
208	    are computed under each reading named in the opening comment; a value matches when one
209	    reading puts it within tolerance. Reproduced when n matches for all nine and at least 80%
210	    of the MAD, R2 and pTRM values match; partially reproduced for 50 to 80%. A 10% tolerance
211	    on R2 near 0.06 or 0.15 is narrow; values within 0.03 of these two are also counted as
212	    matching, as R2 is printed to two places. Whether each listed failure follows is reported
213	    against the stated thresholds (n of 4 or more, pTRM within 15%, R2 about 0.9), not judged,
214	    as ss6 is listed as failing R2 at 0.91 while ss43 at 0.90 is not, and no MAD threshold is
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml",
 "old_string": "partially reproduced for 50 to 80%. A 10% tolerance\n    on R2 near 0.06 or 0.15 is narrow; values within 0.03 of these two are also counted as\n    matching, as R2 is printed to two places. Whether",
 "new_string": "partially reproduced for 50 to 80%. Whether"
}
```

```
The file claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  f=claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml; python tools/claims_check.py $f paper/10.1038-s41597-024-03626-0.txt; grep -c "—\|rather" $f; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/figshare-24639285/*.yaml
```

```
220:    that trended out of, rather toward, the origin of their respective orthogonal vector plots
```

**Agent calls Bash**

```bash
cd  f=claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml; sed -i '220s/trended out of, rather toward, the origin/trended out of ... the origin/' $f; sed -n 220p $f; python tools/claims_check.py $f paper/10.1038-s41597-024-03626-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file is written at `claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml`. It has 17 claims (1 link check and 16 findings), and `tools/claims_check.py` passes it with 0 problems. Nothing was committed.

**Text read:** the version of record, from Europe PMC (PMC11271266, full-text XML). This includes the Methods, Data Records, Technical Validation, the legends of Figs. 1 to 3, and Tables 1 and 2. As a Data Descriptor, the paper has no supplement. It also has no code: it states no custom code was used and names PmagPy without a version, so no repository was read.

**Counts:**
- **Quotes:** all 17 claims have one. One quote is cut with "..." to leave out the word "rather".
- **Statistics:** none, because the paper reports no tests.
- **Expected values:** 7 claims have them. The main ones are Table 1 (M590 and the maximum field for each of the 12 crystals), the Table 2 MAD and R2 values for the 9 fitted glass specimens, the 12% success rate with the 13/12 split by AF pre-treatment, the 0.2 to 0.5 μT baseline, and the 14053g1 example.
- **Criteria:** 15 claims have one.

**Details the paper leaves open, with the readings named:**
- **MAD:** (a) a free line fit, (b) a line anchored to the origin, (c) a free fit to the three-point smoothed vectors.
- **pTRM check %:** normalized by (a) the original pTRM at that temperature or (b) the length of the fitted TRM segment. The check's own pTRM subtracts either (i) the field-off vector measured just before it or (ii) the field-off vector at the same temperature.
- **M590 in Table 1:** (a) the vector difference 590.1 minus 590.0 or (b) the magnitude of 590.1. Either one uses (i) the first replicate or (ii) the mean of the replicates.
- **Consistent or inconsistent replicate directions (Fig. 3):** (a) Fisher k compared between steps, (b) Watson's randomness test at p < 0.05.
- **Regular TRM acquisition, a changing field (Fig. 2), AF cleaning causing "no significant change", and stability at 400 °C:** each has two readings, built from the paper's own 15% pTRM tolerance or the specimen's MAD.
- **Directions "not random":** the paper names no test, so Watson's test is used as a standard choice.
- **Selection thresholds:** Table 2 lists ss6 as failing R2 at 0.91 while ss43 at 0.90 does not fail, and no MAD threshold is given. The claim therefore reports each listed failure against the stated thresholds without judging it.

**Missing or inconsistent in the paper:**
- **Figures not seen:** no PDF was supplied. The nominal paleointensities printed in Fig. 1 and the temperature ranges the arrows mark in Figs. 1 and 2 are therefore not recorded; the criteria use the Table 2 ranges instead.
- **Table footnotes:** the text lacks the footnote legends of both tables. My reading that the Table 2 marks separate specimens without and with AF pre-treatment is inferred and labelled as such.
- **14053g1 example:** the Technical Validation example for 14053g1 (8e-12 A m², 0.2 μT) conflicts with Table 1 (3.203E-09 emu, 0.51 μT). Its numbers match 12040g1, so both readings are named.
- **Rounding in Table 1:** its maximum-field values are 1 to 3% above what the formula gives from its own M590 column. That is within the 10% tolerance.
- **Sample name:** the Results cite "12041g1" where the Fig. 3 legend and Table 1 have 12040g1.
- **Interpretation:** the claim that the glass was magnetized by an impact plasma and that there was no long-lived dynamo rests on ref. 1 and on models. Its claim is included but marked as not tested; it is judged only from the outcomes of the related data claims.

## End of run

22 turns, 4 minutes, result: success.
