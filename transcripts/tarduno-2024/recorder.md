# figshare-24639285 · recorder · run 40586100641

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py figshare-24639285; ls claims/figshare-24639285/ transcripts/figshare-24639285/; cat attempts/figshare-24639285-tarduno-2024-01.yaml; grep -n -B3 -A25 '24639285' targets/dandisets.json
```

```
<persisted-output>
Output too large (39.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4b756bd5-c98f-4509-b11d-2dcb1f551317/tool-results/b7nd77l5f.txt

Preview (first 2KB):
docs/pilot-notes/figshare-26877211-ocagli-2024-01.md
docs/pilot-notes/dryad-4j0zpc8hz-didion-gency-2024-01.md
docs/pilot-notes/dryad-tdz08kq5d-wang-2024-01.md
docs/pilot-notes/000115-gillespie-2021-01.md
docs/pilot-notes/000023-berg-2020-01.md
| [FIGSHARE:24639285](https://figshare.com/articles/dataset/Data_associated_with_Replicate_Apollo_sample_magnetizations_showing_evidence_for_impact_plasmas_and_absence_of_a_long-lived_dynamo_/24639285) | [Tarduno et al. 2024](https://doi.org/10.1038/s41597-024-03626-0) | 12 | 3 | 0 | 1 | [`figshare-24639285-tarduno-2024`](entries/figshare-24639285-tarduno-2024) |
claims/figshare-24639285/:
10.1038-s41597-024-03626-0.yaml

transcripts/figshare-24639285/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 20,400p /home/runner/.claude/projects/-home-runner-work-encore-encore/4b756bd5-c98f-4509-b11d-2dcb1f551317/tool-results/b7nd77l5f.txt
```

```
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
schema_version: 2
id: figshare-24639285-tarduno-2024-01
dataset:
  archive: figshare
  id: "24639285"
  version: "1"
  doi: 10.6084/m9.figshare.24639285.v1
paper: doi:10.1038/s41597-024-03626-0
date: 2026-10-27
entry: figshare-24639285-tarduno-2024
provenance:
[... 361 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,600p /home/runner/.claude/projects/-home-runner-work-encore-encore/4b756bd5-c98f-4509-b11d-2dcb1f551317/tool-results/b7nd77l5f.txt; for f in figshare-26877211-ocagli-2024-01 dryad-4j0zpc8hz-didion-gency-2024-01 dryad-tdz08kq5d-wang-2024-01 000115-gillespie-2021-01 000023-berg-2020-01; do echo "== $f"; cat docs/pilot-notes/$f.md; done; head -5 docs/pilot-notes/001754-knierim-2000-02.md; grep -n -A3 'Outcome\|reproduced |' README.md | head -20
```

```
<persisted-output>
Output too large (45.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4b756bd5-c98f-4509-b11d-2dcb1f551317/tool-results/brztz190z.txt

Preview (first 2KB):
    example's numbers are those of 12040g1. The text before Figure 3 names 12041g1, which is not a
    specimen of the deposit; the Figure 3 legend has 12040g1.
- kind: paper_inconsistency
  statement: Table 2 gives ss36 a pTRM check at 450 C (25%), but its sheet has no pTRM check step,
    and gives ss27 6 points from 100 to 550 C where its sheet has 5 paired steps (100, 305, 400, 500,
    550 C).
- kind: metadata_insufficient
  statement: The laboratory field of the glass experiments differs between sheets, 18 uT (10
    sheets), 15 uT (11) and 14.4 uT (g2), given in a footnote of each sheet. The paper states only
    the 18 uT of Figure 1.
- kind: other
  statement: The crystals' moments after zero-field heating to 590 C (37 measurements, 1.0e-10 to
    6.0e-10 emu per measurement) are all above the 8e-11 emu magnetometer threshold the paper uses
    for its bound on paleointensity. The directions of these measurements are random by Watson's
    test in every crystal.
- kind: metadata_error
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4b756bd5-c98f-4509-b11d-2dcb1f551317/tool-results/brztz190z.txt"
}
```

```
1	    example's numbers are those of 12040g1. The text before Figure 3 names 12041g1, which is not a
2	    specimen of the deposit; the Figure 3 legend has 12040g1.
3	- kind: paper_inconsistency
4	  statement: Table 2 gives ss36 a pTRM check at 450 C (25%), but its sheet has no pTRM check step,
5	    and gives ss27 6 points from 100 to 550 C where its sheet has 5 paired steps (100, 305, 400, 500,
6	    550 C).
7	- kind: metadata_insufficient
8	  statement: The laboratory field of the glass experiments differs between sheets, 18 uT (10
9	    sheets), 15 uT (11) and 14.4 uT (g2), given in a footnote of each sheet. The paper states only
10	    the 18 uT of Figure 1.
11	- kind: other
12	  statement: The crystals' moments after zero-field heating to 590 C (37 measurements, 1.0e-10 to
13	    6.0e-10 emu per measurement) are all above the 8e-11 emu magnetometer threshold the paper uses
14	    for its bound on paleointensity. The directions of these measurements are random by Watson's
15	    test in every crystal.
16	- kind: metadata_error
17	  statement: The item's description lists files named "SI Figure 1 - Other Thelliers n=18.pdf" and
18	    "SI Figure 2 - All Stereonets copy.pdf", while the files are "SupplFig1 - other Thelliers March
19	    2024.pdf" and "SuppFig2 - All Stereonet.pdf". The item's title differs from the paper's.
20	verifications:
[... 660 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '^| Dataset\|^|---' README.md | head; cat tools/readme_row.py | head -80; grep -n 'link\|^  id:\|^- id:\|data:' claims/figshare-24639285/*.yaml | head -60
```

```
"""The README's table row for a dataset, from its latest attempt.

    python tools/readme_row.py DATASET            # print the row

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
[... 77 more lines not kept]
```

**Agent**

Gathered the record; link claim `glass-specimen-set` is excluded from the row counts. Now reading the claims file head, the rest of the verifications and the reports.

**Agent calls Bash**

```bash
cd  sed -n 1,85p claims/figshare-24639285/*.yaml; awk '/^verifications:/{f=1} f' attempts/figshare-24639285-tarduno-2024-01.yaml | sed -n 180,400p; grep -n -B2 -A12 '24639285' targets/dandisets.json
```

```
# Claims for Tarduno, Cottrell & Zhou (2024), Scientific Data, doi:10.1038/s41597-024-03626-0,
# on Figshare dataset 24639285 (doi:10.6084/m9.figshare.24639285.v1).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
# protocol pilot-12 as stated in docs/protocol.md (Reader).
#
# Text read: the version of record from Europe PMC (PMC11271266, full-text XML converted to text)
# as supplied under paper/, with Background & Summary, Methods, Data Records, Technical
# Validation, the legends of Figures 1 to 3 and Tables 1 and 2. The paper is a Data Descriptor
# and has no supplement; its additional plots are in the Figshare deposit itself. No PDF was
# supplied, so the figures were not seen: the nominal paleointensities printed in Figure 1 and
# the step ranges marked by arrows in Figures 1 and 2 are not recorded. The footnote legends of
# both tables (the marks after "M590 20 uT" and "Max intensity" in Table 1, and the marks after
# the specimen names, after n and after T Range in Table 2) are missing from the text.
# Code: the paper states that no custom code was used. It names PmagPy for looking at the
# directional and paleointensity data during collection and for checking quality factors
# (Technical Validation), with no version; no repository was read.
#
# Data the paper used. Two sets of measurements, all made with the WSGI three-component DC SQUID
# magnetometer (6.3 mm bore) in the shielded room at the University of Rochester, moments in emu.
# Per the Data Records, each sample's data are a sheet of an Excel file with columns sample name,
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else d.get('dandisets', d)
import itertools
for x in (it if isinstance(it,list) else it.values()):
  if '24639285' in json.dumps(x): print(json.dumps(x,indent=1))
"; ls transcripts/figshare-24639285/; wc -w transcripts/figshare-24639285/*-report.md
```

```
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
  147 transcripts/figshare-24639285/answer-report.md
  262 transcripts/figshare-24639285/author-answers-report.md
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '24639285\|figshare' targets/dandisets.json | head; head -c 600 targets/dandisets.json
```

```
{
 "schema_version": 1,
 "generated": "2026-10-27T12:12:13+00:00",
 "source": "https://api.dandiarchive.org/api",
 "counts": {
  "public_dandisets": 665,
  "with_a_paper": 288,
  "with_a_published_version": 247,
  "papers": 300,
  "converted_by_catalystneuro": 51
 },
 "targets": [
  {
   "dandiset": "000003",
   "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
   "published_version": "0.260218.2052",
   "asset_count": 101,
   "size_gb": 2559.25,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
[... 3 more lines not kept]
```

**Agent**

There is no entry for this dataset in `targets/dandisets.json`, so the note won't say anything about who converted it. Next I'm reading the reports.

**Agent calls Bash**

```bash
cd transcripts/figshare-24639285; for f in author-report.md answer-report.md author-answers-report.md author-revise-1-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-report.md
I wrote the entry, the record and the handover package. The notebook runs in 27 s in a clean environment, `entry.py check` reports 0 errors, and nothing was committed. One claim misses its bar narrowly: the Table 2 fit statistics match 23 of 29 values (79%, the criterion asks for 80%), so it is partially reproduced.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| glass-specimen-set (link) | reproduced |
| glass-success-rate | reproduced |
| table2-fit-statistics | partially reproduced, rests on an assumption (23 of 29 values) |
| table2-no-fit | reproduced |
| fig1-linear-components | reproduced, rests on an assumption |
| fig2-changing-field | reproduced, rests on an assumption |
| glass-directions-not-random | partially reproduced (8 of 22 specimens) |
| glass-af-no-change | reproduced (8 of 10 unchanged) |
| table1-max-intensity | reproduced (24 of 24 values) |
| baseline-range | reproduced (0.200 to 0.500 µT) |
| example-14053g1-threshold | reproduced only under the misprint reading (the numbers are 12040g1's) |
| fig3-nrm-consistent, fig3-590-inconsistent, fig3-alteration-check-inconsistent | reproduced |
| crystal-14053g1-400c-stable | reproduced |
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/figshare-24639285; head -c 2500 verifier-1-report.md; echo; echo =====; head -c 2500 verifier-2-report.md; echo ====; cat claims-report.md | head -c 2000; ls questions/ | grep 2463
```

```
**Verifier report, round 1: Tarduno, Cottrell & Zhou 2024 (FIGSHARE:24639285 v1)**

The claims file has 17 claims. The notebook tests 16 and treats `interpretation-impact-no-dynamo` as blocked. I checked the archive through the Figshare API: version 1 is the only version, and its 16 files (13 xlsx, 3 pdf) have the same IDs and MD5s as notebook cell 1.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| glass-specimen-set | reproduced | Cell 8: 22 of 22 Table 2 glass specimens and 12 of 12 Table 1 crystals are present with step, moment, Dec and Inc. 10 glass specimens have AF steps, the same set as the Table 2 marks. Four of the glass sheets are not real replicate measurements (problem 1). |
| glass-success-rate | reproduced | Cell 10: 3/(3+22) = 12.0%. Without AF: 12+1 = 13; with AF: 10+2 = 12, which matches Methods paragraph 2. |
| table2-fit-statistics | partially_reproduced | Cells 12–13: n matches for all nine. With replicates averaged, 23 of 29 values match (79%), just under the 80% bar. The misses are ss10 MAD (33.3 vs 42.9), R2 for ss9, ss10 and ss34, and pTRM checks for ss19 at 250 °C and ss30 at 450 °C. Using only the first measurement gives 38%. Holding a single pTRM reading fixed gives about 66% (19/29), so the outcome is partial either way. |
| table2-no-fit | reproduced | Cell 16: 11 of 11 are irregular under reading (a) and 9 of 11 under (b). ss36 and ss39 grow away from the origin over their last step (1.77→6.00 and 2.31→9.67 ×1e-9 emu). Reading (b) passes exactly at the threshold, and 3 of its 9 are synthetic sheets (problem 1). |
| fig1-linear-components | reproduced | Cell 19, averaged replicates, free-line MAD: ss43 MAD 10.3 vs 10.0 and R2 0.902 vs 0.90; ss19 MAD 30.1 vs 30.1 and R2 0.956 vs 0.94. Nominal paleointensities are 9.6 and 23.0 µT (8.5 and 23.7 µT with first measurements). They cannot be compared with Figure 1 because the figure was not seen. |
| fig2-changing-field | reproduced | Cell 21, averaged replicates: both specimens 
[... 46 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/figshare-24639285-tarduno-2024-01.md",
 "content": "# figshare-24639285, Tarduno et al. 2024\n\nTwelve claims reproduced, three partially and one blocked, all on the dataset,\nwith the link claim `glass-specimen-set` also reproduced. It pins version 1,\nthe item's only version, which holds 13 Excel files and 3 PDFs. The paper, a\nData Descriptor in Scientific Data by Tarduno, Cottrell and Zhou, describes\nreplicate magnetization measurements of Apollo samples: Thellier-Coe\npaleointensity experiments on glass of 64455, of which 22 failed subsamples\nare presented in Table 2, and single silicate crystals from 14053, 12021,\n12053, 12040 and 71055 heated to 590 C in zero field and in 20 and 40 uT\nfields (Table 1). The claims were written from the version of record in\nEurope PMC (PMC11271266) without its figures, so the nominal\npaleointensities of Figure 1 and the step ranges marked in Figures 1 and 2\nremain unchecked; the paper used no custom code. The specimen set, the\nsuccess rate, the Table 2 fit statistics and irregular specimens, the\nFigure 1 and 2 examples, the randomness of the glass directions, the AF\npre-treatment, Table 1's maximum intensities and baseline, the consistency\nof the crystal replicates in Figure 3, the 400 C test on 14053g1 and the\nrecording efficiency were tested. `interpretation-impact-no-dynamo` is\nblocked as `other`, as the claims file says this interpretation is not\ntested. `table2-fit-statistics` is partially reproduced, with 23 of 29\nvalues matching (79%) against the 80% the criterion asks; it, and\n`fig1-linear-components` and `fig2-changing-field`, rest on the assumption\nthat the 2 to 19 repeated measurements of a step are averaged as vectors,\nand with the first measurement only 11 of 29 values match (38%).\n`glass-directions-not-random` is partially reproduced, with 8 of 22\nspecimens rejecting randomness, and `example-14053g1-threshold` matches only\nif the crystal name is a misprint for 12040g1. The author put no questions\nto a reader, so the answer run changed nothing. Round 1 gave its own outcome\nfor each claim and agreed with 16 of 17; the author took its outcome for\n`example-14053g1-threshold` (from reproduced to partially reproduced), and\nits points led to the per-step replicate scatter of ss9, ss10 and ss6, the\nscore under each fixed pTRM reading (14 to 19 of 29), a scan for steps with\ntwo groups of directions, null rates for the readings of\n`fig2-changing-field` and TRM40/TRM20 without the factor of two; one\nquestion, on the cutoff of `no-alteration-recording-efficiency`, was then\nput to a reader and is unanswered, as it was added after the answer step.\nRound 2 agreed with all 17, so there was no third round; it found statements\nthe outputs did not support, among them MADs said to match Table 2 to the\nprinted digit for six specimens where only ss19 and ss22 do, and \"several\ntimes\" the threshold for 590.0 moments 1.3 to 7.5 times it, and these were\ncorrected. In response the author read the deposit's Supplementary Figure 1\nfrom its vector drawing; with NRM read as that figure plots it, 24 of 29\nvalues match (83%) under any reading, but 23 of 29 (79%) with the pTRM\nreference the figure uses, so the outcome was kept. Some outcomes rest on\nweak ground: the readings of `fig2-changing-field` hold with no changing\nfield for 98% of random sets of 3 directions under reading (a) and 56%\nunder reading (b); and `no-alteration-recording-efficiency` passes every\ncrystal only under the claims file's cutoff of 2 on TRM40/(2 TRM20), while\nTRM40/TRM20 is 1.54 to 2.35 with three crystals above 2. The author's run\ntook about 17 minutes; one notebook cell failed on the first execution, a\npTRM-check table with no rows, and was fixed in the helper. The notebook ran\nin 27 s at first and 42 s in the last run.\n\nIn four glass sheets of 64455lunar_cryodata.xlsx (g2, ss8, ss39, ss48) the\nrows given as repeated measurements of each step are one row multiplied by\nfactors between 0.95 and 1.03, in g2, ss8 and ss39 with the same factor on\nthe moment, the declination and the inclination (one ss8 declination becomes\n361.7 deg), and no step of the other 18 sheets or the 12 crystal files is\nbuilt this way; the deposit does not say how they were made, and the points\nof Supplementary Figure 1 for these four sheets differ from every\ncombination of their deposited rows by 0.5% or more (median). Neither the\ndeposit nor the paper says how the repeated measurements were combined for\nTable 2 and Figures 1 and 2; Supplementary Figure 1 plots, for 12 of its 14\nspecimens that are not synthetic sheets, TRM gained from the mean vectors\nand NRM as the mean of the moments, to 0.1% or better, and eleven steps of\nseven glass sheets hold two groups of directions more than 45 deg apart,\nnine of them inside the specimen's Table 2 range. Table 1's M590 equals the\nmoment of the single 590.1 measurement to its four digits for all 12\ncrystals, while the Methods define the TRM as the vector subtraction of the\nfield-on and field-off steps. The crystals' 37 moments after zero-field\nheating to 590 C, 1.0e-10 to 6.0e-10 emu, are all above the 8e-11 emu\nthreshold the paper uses for its bound on paleointensity, and their\ndirections are random by Watson's test in every crystal. The paper and the\ndata disagree in places: the Technical Validation example for 14053g1 uses\na TRM of 8e-12 A m2 and gives 0.2 uT, the numbers of 12040g1, where the data\ngive 3.2e-12 A m2 and 0.50 to 0.51 uT; the text before Figure 3 names\n12041g1, not a specimen of the deposit; Table 2 gives ss36 a pTRM check at\n450 C (25%) that its sheet does not have, and ss27 6 points from 100 to\n550 C where its sheet has 5 paired steps; and ten of twelve of Table 1's\nmaximum intensities equal the formula rounded up. The laboratory field of\nthe glass experiments is 18 uT in 10 sheets, 15 uT in 11 and 14.4 uT in g2,\nwhile the paper states only the 18 uT of Figure 1. Other findings: sheet\nss19 has an inclination of -136 deg at its 10 mT step (likely -13.6), ss8\nan NRM declination of 361.692 deg, ss18 a 250 C row with no moment,\ndeclination or inclination, and ss48 an extra column CSD before the moment;\nNRM is labelled both 0 and 0.0 in ss27 and ss38; one ss27 point of\nSupplementary Figure 1 is labelled 210 C, a step with no field-on\nmeasurement in the sheet; and the item's description lists files named \"SI\nFigure 1 - Other Thelliers n=18.pdf\" and \"SI Figure 2 - All Stereonets\ncopy.pdf\" where the files are \"SupplFig1 - other Thelliers March 2024.pdf\"\nand \"SuppFig2 - All Stereonet.pdf\", and the item's title differs from the\npaper's.\n\nThe author's points on the protocol: it gives no outcome for a claim the\nclaims file says is not tested, so blocked with `other` was used; how\nrepeated measurements are combined was missing from the claims file and\nchanges the outcome, so both were run and averaging adopted as an\nassumption; counting a value as matched under any reading inflates matches\nwhen there are many readings, as the 4 named readings of each pTRM value\n(8 with both ways of combining repeats); the example claim's criterion does\nnot say what outcome to give when only the misprint reading matches; the\nclock check does not apply to static measurements with no time axis; the\nduplicate-recording check does not cover values made up from one\nmeasurement, and no finding kind fits them; and `tools/entry.py` needs\n`pyyaml`, `jsonschema` and `nbformat`, which the checkout's Python lacked.\n"
}
```

```
File created successfully at: docs/pilot-notes/figshare-24639285-tarduno-2024-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -c '—\|rather' docs/pilot-notes/figshare-24639285-tarduno-2024-01.md
```

```
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
?? docs/pilot-notes/figshare-24639285-tarduno-2024-01.md
?? scripts
0
```

**Agent**

I wrote the notes to `docs/pilot-notes/figshare-24639285-tarduno-2024-01.md`, and no other file changed. The dataset has no entry in `targets/dandisets.json`, so the note doesn't say whether CatalystNeuro converted it. `git status` also lists untracked dotfiles in the repo root, such as `.bashrc`, `.idea` and `scripts`. The run reports say these are sandbox mounts, so leave them out of the commit.

# figshare-24639285, Tarduno et al. 2024

Twelve claims reproduced, three partially and one blocked, all on the dataset, with the link claim `glass-specimen-set` also reproduced. It pins version 1, the item's only version, which holds 13 Excel files and 3 PDFs. The paper, a Data Descriptor in Scientific Data by Tarduno, Cottrell and Zhou, describes replicate magnetization measurements of Apollo samples: Thellier-Coe paleointensity experiments on glass of 64455, of which 22 failed subsamples are presented in Table 2, and single silicate crystals from 14053, 12021, 12053, 12040 and 71055 heated to 590 C in zero field and in 20 and 40 uT fields (Table 1). The claims were written from the version of record in Europe PMC (PMC11271266) without its figures, so the nominal paleointensities of Figure 1 and the step ranges marked in Figures 1 and 2 remain unchecked; the paper used no custom code. The specimen set, the success rate, the Table 2 fit statistics and irregular specimens, the Figure 1 and 2 examples, the randomness of the glass directions, the AF pre-treatment, Table 1's maximum intensities and baseline, the consistency of the crystal replicates in Figure 3, the 400 C test on 14053g1 and the recording efficiency were tested. `interpretation-impact-no-dynamo` is blocked as `other`, as the claims file says this interpretation is not tested. `table2-fit-statistics` is partially reproduced, with 23 of 29 values matching (79%) against the 80% the criterion asks; it, and `fig1-linear-components` and `fig2-changing-field`, rest on the assumption that the 2 to 19 repeated measurements of a step are averaged as vectors, and with the first measurement only 11 of 29 values match (38%). `glass-directions-not-random` is partially reproduced, with 8 of 22 specimens rejecting randomness, and `example-14053g1-threshold` matches only if the crystal name is a misprint for 12040g1. The author put no questions to a reader, so the answer run changed nothing. Round 1 gave its own outcome for each claim and agreed with 16 of 17; the author took its outcome for `example-14053g1-threshold` (from reproduced to partially reproduced), and its points led to the per-step replicate scatter of ss9, ss10 and ss6, the score under each fixed pTRM reading (14 to 19 of 29), a scan for steps with two groups of directions, null rates for the readings of `fig2-changing-field` and TRM40/TRM20 without the factor of two; one question, on the cutoff of `no-alteration-recording-efficiency`, was then put to a reader and is unanswered, as it was added after the answer step. Round 2 agreed with all 17, so there was no third round; it found statements the outputs did not support, among them MADs said to match Table 2 to the printed digit for six specimens where only ss19 and ss22 do, and "several times" the threshold for 590.0 moments 1.3 to 7.5 times it, and these were corrected. In response the author read the deposit's Supplementary Figure 1 from its vector drawing; with NRM read as that figure plots it, 24 of 29 values match (83%) under any reading, but 23 of 29 (79%) with the pTRM reference the figure uses, so the outcome was kept. Some outcomes rest on weak ground: the readings of `fig2-changing-field` hold with no changing field for 98% of random sets of 3 directions under reading (a) and 56% under reading (b); and `no-alteration-recording-efficiency` passes every crystal only under the claims file's cutoff of 2 on TRM40/(2 TRM20), while TRM40/TRM20 is 1.54 to 2.35 with three crystals above 2. The author's run took about 17 minutes; one notebook cell failed on the first execution, a pTRM-check table with no rows, and was fixed in the helper. The notebook ran in 27 s at first and 42 s in the last run.

In four glass sheets of 64455lunar_cryodata.xlsx (g2, ss8, ss39, ss48) the rows given as repeated measurements of each step are one row multiplied by factors between 0.95 and 1.03, in g2, ss8 and ss39 with the same factor on the moment, the declination and the inclination (one ss8 declination becomes 361.7 deg), and no step of the other 18 sheets or the 12 crystal files is built this way; the deposit does not say how they were made, and the points of Supplementary Figure 1 for these four sheets differ from every combination of their deposited rows by 0.5% or more (median). Neither the deposit nor the paper says how the repeated measurements were combined for Table 2 and Figures 1 and 2; Supplementary Figure 1 plots, for 12 of its 14 specimens that are not synthetic sheets, TRM gained from the mean vectors and NRM as the mean of the moments, to 0.1% or better, and eleven steps of seven glass sheets hold two groups of directions more than 45 deg apart, nine of them inside the specimen's Table 2 range. Table 1's M590 equals the moment of the single 590.1 measurement to its four digits for all 12 crystals, while the Methods define the TRM as the vector subtraction of the field-on and field-off steps. The crystals' 37 moments after zero-field heating to 590 C, 1.0e-10 to 6.0e-10 emu, are all above the 8e-11 emu threshold the paper uses for its bound on paleointensity, and their directions are random by Watson's test in every crystal. The paper and the data disagree in places: the Technical Validation example for 14053g1 uses a TRM of 8e-12 A m2 and gives 0.2 uT, the numbers of 12040g1, where the data give 3.2e-12 A m2 and 0.50 to 0.51 uT; the text before Figure 3 names 12041g1, not a specimen of the deposit; Table 2 gives ss36 a pTRM check at 450 C (25%) that its sheet does not have, and ss27 6 points from 100 to 550 C where its sheet has 5 paired steps; and ten of twelve of Table 1's maximum intensities equal the formula rounded up. The laboratory field of the glass experiments is 18 uT in 10 sheets, 15 uT in 11 and 14.4 uT in g2, while the paper states only the 18 uT of Figure 1. Other findings: sheet ss19 has an inclination of -136 deg at its 10 mT step (likely -13.6), ss8 an NRM declination of 361.692 deg, ss18 a 250 C row with no moment, declination or inclination, and ss48 an extra column CSD before the moment; NRM is labelled both 0 and 0.0 in ss27 and ss38; one ss27 point of Supplementary Figure 1 is labelled 210 C, a step with no field-on measurement in the sheet; and the item's description lists files named "SI Figure 1 - Other Thelliers n=18.pdf" and "SI Figure 2 - All Stereonets copy.pdf" where the files are "SupplFig1 - other Thelliers March 2024.pdf" and "SuppFig2 - All Stereonet.pdf", and the item's title differs from the paper's.

The author's points on the protocol: it gives no outcome for a claim the claims file says is not tested, so blocked with `other` was used; how repeated measurements are combined was missing from the claims file and changes the outcome, so both were run and averaging adopted as an assumption; counting a value as matched under any reading inflates matches when there are many readings, as the 4 named readings of each pTRM value (8 with both ways of combining repeats); the example claim's criterion does not say what outcome to give when only the misprint reading matches; the clock check does not apply to static measurements with no time axis; the duplicate-recording check does not cover values made up from one measurement, and no finding kind fits them; and `tools/entry.py` needs `pyyaml`, `jsonschema` and `nbformat`, which the checkout's Python lacked.

## End of run

13 turns, 2 minutes, result: success.
