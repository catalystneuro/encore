# 000023 · recorder · run 39957383232

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 000023; ls claims/000023 transcripts/000023; cat attempts/000023-berg-2020-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));print([x for x in (d if isinstance(d,list) else d.values()) if '000023' in json.dumps(x)][:1])"
```

```
<persisted-output>
Output too large (249.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ffcec5f3-57ac-40e2-b930-f71d91f84522/tool-results/bbucx3nm3.txt

Preview (first 2KB):
docs/pilot-notes/000045-ibl-2021-01.md
docs/pilot-notes/001828-mantas-2024-01.md
docs/pilot-notes/000037-gillon-2023-01.md
docs/pilot-notes/000036-mayner-2022-01.md
docs/pilot-notes/000003-senzai-2017-01.md
| [000023](https://dandiarchive.org/dandiset/000023) | [Berg et al. 2020](https://doi.org/10.1101/2020.03.31.018820) | 4 (+3) | 3 (+1) | 3 | 1 | [`000023-berg-2020`](entries/000023-berg-2020) |
claims/000023:
10.1101-2020.03.31.018820.yaml

transcripts/000023:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/000023-berg-2020-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else d.get('dandisets', d)
for x in (it if isinstance(it,list) else it.values()):
  if '000023' in json.dumps(x)[:200]: print(json.dumps(x,indent=1)[:3000]); break
"
```

```
<persisted-output>
Output too large (62.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ffcec5f3-57ac-40e2-b930-f71d91f84522/tool-results/bslg7y07s.txt

Preview (first 2KB):
schema_version: 2
id: 000023-berg-2020-01
dataset:
  archive: dandi
  id: "000023"
  version: 0.210914.1900
  doi: 10.48324/dandi.000023/0.210914.1900
paper: doi:10.1101/2020.03.31.018820
date: 2026-10-23
entry: 000023-berg-2020
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in 000045-ibl-2021-01 001828-mantas-2024-01 000037-gillon-2023-01 000036-mayner-2022-01 000003-senzai-2017-01 001754-knierim-2000-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done
```

```
<persisted-output>
Output too large (35.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ffcec5f3-57ac-40e2-b930-f71d91f84522/tool-results/bvs3u6vab.txt

Preview (first 2KB):
=== 000045-ibl-2021-01
# 000045, International Brain Laboratory et al. 2021

Nineteen claims reproduced, thirteen partially, five not reproduced and one
blocked, all on the dandiset, with the link claim `lab-link`, which the
author added, also reproduced. It pins version 0.211209.1413; the paper cites
no version, and the two published versions, made a minute apart, hold the
same files. The paper, "Standardized and reproducible measurement of
decision-making in mice" in eLife, trains mice in seven laboratories on a
basic and a full visual decision task and reports that learning rates differ
across laboratories but that performance, psychometric parameters and the use
of block priors at proficiency do not, so that a classifier cannot tell the
laboratories apart. The cohort counts, days and trials to proficiency, the
Figure 2 psychometric ranges, the lab tests and classifiers of Figures 3 and
4, the GLM weights and accuracy of Figure 5, win-stay/lose-switch, updating
by contrast and the session end criteria were tested. Only
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ffcec5f3-57ac-40e2-b930-f71d91f84522/tool-results/bvs3u6vab.txt"
}
```

```
1	=== 000045-ibl-2021-01
2	# 000045, International Brain Laboratory et al. 2021
3	
4	Nineteen claims reproduced, thirteen partially, five not reproduced and one
5	blocked, all on the dandiset, with the link claim `lab-link`, which the
6	author added, also reproduced. It pins version 0.211209.1413; the paper cites
7	no version, and the two published versions, made a minute apart, hold the
8	same files. The paper, "Standardized and reproducible measurement of
9	decision-making in mice" in eLife, trains mice in seven laboratories on a
10	basic and a full visual decision task and reports that learning rates differ
11	across laboratories but that performance, psychometric parameters and the use
12	of block priors at proficiency do not, so that a classifier cannot tell the
13	laboratories apart. The cohort counts, days and trials to proficiency, the
14	Figure 2 psychometric ranges, the lab tests and classifiers of Figures 3 and
15	4, the GLM weights and accuracy of Figure 5, win-stay/lose-switch, updating
16	by contrast and the session end criteria were tested. Only
17	`early-sessions-predict-slow-learners` is blocked, as
18	`methods_underspecified`: the paper gives no code or method for its Random
19	Forest, and the criterion's readings disagree, 3 of 20 accuracy values within
20	0.53 +- 0.053 and the others from 0.143 to 0.667. The author put seven
[... 505 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ffcec5f3-57ac-40e2-b930-f71d91f84522/tool-results/bslg7y07s.txt"
}
```

```
1	schema_version: 2
2	id: 000023-berg-2020-01
3	dataset:
4	  archive: dandi
5	  id: "000023"
6	  version: 0.210914.1900
7	  doi: 10.48324/dandi.000023/0.210914.1900
8	paper: doi:10.1101/2020.03.31.018820
9	date: 2026-10-23
10	entry: 000023-berg-2020
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code (GitHub Actions)
17	    model: claude-opus-5-5
18	    protocol: pilot-10
19	  runner:
20	    platform: GitHub Actions
[... 866 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ffcec5f3-57ac-40e2-b930-f71d91f84522/tool-results/bslg7y07s.txt",
 "offset": 887
}
```

```
887	    outcome: partially_reproduced
888	    reason: Agrees, with no caveat.
889	    response: No change needed.
890	  - claim: fig4e-mouse-ephys-anova
891	    agrees: true
892	    outcome: reproduced
893	    reason: Agrees, with no caveat.
894	    response: No change needed.
895	  - claim: fig4-glp2r-sag
896	    agrees: true
897	    outcome: reproduced
898	    reason: Agrees under the claims file as written, but the result is fragile. Sag BH p is 0.046; with
899	      the Methods' cell QC it is 0.060, and the claim is not reproduced (cell 61). Cell QC is not applied
900	      (problem 3); the paper requires it as a condition for including a cell, and the claims file's link
901	      criterion names only sweep QC, an omission in the claims file, not a misreading of the paper.
902	    response: Outcome kept, as the verifier agrees under the claims file. The notes already give the
903	      cell QC result (BH p 0.060). Whether cell QC applies is asked in questions/000023.yaml and not yet
904	      answered; the claims file is not changed by the author.
905	  - claim: edtable1-species-ephys
906	    agrees: true
[... 158 more lines not kept]
```

**Agent**

I've read the attempt record. Next: how the README row counts are defined, the dataset entry, the claims file and the reports.

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/readme_row.py; grep -n "Reproduced\|^| Dandiset" README.md | head; python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else len(d))
"; grep -n '"000023"' -A30 targets/dandisets.json | head -50
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
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/000023/10.1101-2020.03.31.018820.yaml'))
print({k:v for k,v in d.items() if k!='claims'})
for c in d['claims']: print(c['id'], c.get('kind'), c.get('data'), '|', str(c.get('statement',''))[:150])
"; wc -w transcripts/000023/*-report.md
```

```
{'schema_version': 2, 'dataset': {'archive': 'dandi', 'id': '000023'}, 'paper': 'doi:10.1101/2020.03.31.018820', 'checks': [{'date': datetime.date(2026, 10, 22), 'kind': 'agent', 'model': 'claude-opus-5-5', 'ready': True, 'changes': ['Read the code at AllenInstitute/patchseq_human_L23 3daf9f0 and confirmed the details the criteria cite (HC3 type-2 F test and BH in run_cluster_anova, two-sided pairwise Mann-Whitney with BH over pairs, deep FREM3 as depth above 0.575 with CARM1P1 and COL22A1 not cut by depth, non-positive input resistance, f-I slope and sag set missing, scipy 1.4 one-sided mannwhitneyu at 0.05/18 per marker with low at most 1 and high above 1 in pathology_analysis.ipynb, random forest settings and drop of cells with any missing feature).', "edtable1-species-ephys. Removed the statistics entry (FDR below 0.05); it is the threshold used to count the 17 features, a method, not a result. Student's and Welch's t-test are method readings, so the outcome must now be the one both give, blocked as methods_underspecified when they differ, not either.", 'fig5c-frem3-ephys-depth. Removed the first statistics entry (FDR below 0.05), the threshold used to count the 9 features; kept the FDR below 1e-7 of the three regressions shown, which the Figure 5 legend reports as their result.', 'fig5b-frem3-morph-depth and fig5d-frem3-gene-depth. Removed the statistics entries (FDR below 0.05), the thresholds used to count the 37 features and 790 genes.', "fig6-deep-ephys-anova. Removed the statistics entry (FDR below 0.05), the threshold used to count the 15 features; the cell counts it held and the counting rule are now in the criterion, with the code's choice of not cutting CARM1P1 and COL22A1 by depth.", 'fig6c-carm1p1-upstroke-rin. The two readings of "faster upstroke" (upstroke rate, upstroke/downstroke ratio) are a choice of measure, so the upstroke part must hold under both, methods_underspecified when they differ, not under one.', 'fig3d-depth-by-type. The 90% and 80
[... 43 more lines not kept]
```

**Agent**

The README row counts only the 16 claims on the dandiset (the link claim plus 17 claims on data held elsewhere are left out). Now the reports.

**Agent calls Bash**

```bash
cd transcripts/000023; for f in claims-report claims-check-report author-report answer-report author-answers-report; do echo "=== $f"; cat $f.md; done
```

```
=== claims-report
I've written `claims/000023/10.1101-2020.03.31.018820.yaml`. The quote checker passes except for two values it can't parse: the GO p-values printed as "p=3.5 10 −6" and "p=5.3 10 −5". I read them in the text and they are correct. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1 (the version the dandiset names), from the JATS XML: main text, Methods, figure legends, and the legends of the Extended Data figures and tables. There is no PDF, so none of the figures could be read.

**Code read:** `AllenInstitute/patchseq_human_L23` at commit `3daf9f0803ea0c220a040ea523f23af5f93c56ac`. That commit was updated for the later Nature version, so some of its outputs differ from the preprint. In those places the criteria follow the preprint's Methods and run the code's choice as a variant:
- its feature table has 316 human cells, against the preprint's 283;
- its comparison of the three homologous types uses only the superficial FREM3 cells;
- the updated pathology notebook finds 2 significant comparisons out of 18, against 1 in the original.

**Counts:** 33 claims (1 link check, 32 findings). 32 have quotes; the link has none and needs none. 17 statistical values, and every claim has a criterion or expected values.
- 13 can be tested on the dandiset once each cell's t-type and depth are attached: 12 `with_labels` (cell counts, depth by type, the type ANOVAs, FREM3 depth correlations, the human classifier, pairwise deep-type tests) plus the link.
- 4 are `with_inputs`: pathology against electrophysiology, the mouse ANOVA, the mouse classifier, and the human against mouse comparison.
- 16 are `elsewhere`: histology, transcriptomics, morphology and SMI-32.

**Details the paper leaves open, and the readings named:**
- **Which cells have features:** at least one feature, all 18, or no more than 3 of 18 missing.
- **Donor count of 90:** all subjects in the dandiset, or the donors of the paper's 385 cells.
- **Cells in the pathology comparison:**
[... 172 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000023; for f in verifier-1-report author-revise-1-report verifier-2-report author-revise-2-report; do echo "=== $f"; cat $f.md; done
```

```
=== verifier-1-report
**A. Outcomes** (all 33 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| features-and-labels-link | reproduced (M2); M1 not reproduced | M1 links 0 files (cell 12). Under M2, 318 files link to 318 distinct cells, and all 283 of the code's cells that have features have a file. The median relative difference is 0 for all 18 features over 282 cells, and a match on features alone picks the M2 cell 282 of 282 times. |
| cohort-cells | not_reproduced | 318 cells, not 385. 283 is not reached under any reading: (a) 307, (b) 256, (c) 306 (cell 16). |
| cohort-donors | not_reproduced | 56 under both readings, not 90 (cell 18). The pathology table has 89 distinct donors in 90 rows. |
| cohort-type-counts | not_reproduced | At most 2 of 6 counts match under any reading (cell 20). The criterion needs at least 3 for partial. |
| fig1a-thickness | reproduced | 1.231 ± 0.155 mm over 5 sections, inside 1.23 ± 0.15 (cell 60). The mouse value is untested, as the criterion says. |
| fig1b-density | partially_reproduced | Human 27.70 ± 4.46, highest in L2 and falling to 0.43× at −0.575 (cell 62). The mouse figure (349.8) comes from a faulty port (problem 2), so the mouse part was not validly tested. |
| fig1c-soma-area | partially_reproduced | Human quartiles 107.5/252.6 and largest soma 886 µm² pass (cell 64). Mouse quartiles 24.4/61.0 fail, but they come from the faulty port; the claims file says Code7 prints 44.7/96.5 from the same files. |
| fig1c-soma-variation | blocked (other) | The ratio is NaN because all 1419 mouse somata sit at scaled depth −1.0 (cell 65). This is a port fault, not missing data, so the claim is testable. |
| fig1f-frem3-heterogeneity | blocked (data_missing) | Not in the archive: it holds only 318 `*_icephys.nwb` files (checked through the API). |
| fig1g-deep-types-de-genes | blocked (data_missing) | Same reason. |
| fig3a-platform-correlation | blocked (data_missing) | Same reason. |
| fig2d-pathology-scores | r
[... 141 more lines not kept]
```

**Agent**

I have everything I need. Writing the note now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000023-berg-2020-01.md",
 "content": "# 000023, Berg et al. 2020\n\nFour claims reproduced, three partially, three not reproduced and one blocked\non the dandiset, with three more reproduced and one more partially reproduced\non the dandiset together with the paper's code tables; the link claim\n`features-and-labels-link` is reproduced, and of the 17 claims on data\nelsewhere, 10 are reproduced and 7 blocked. It pins version 0.210914.1900, the\nonly published version; the paper cites none. The paper, the bioRxiv preprint\n\"Human cortical expansion involves diversification and specialization of\nsupragranular intratelencephalic-projecting neurons\", describes Patch-seq\nneurons of human L2 and L3 from neurosurgical donors in five glutamatergic\nt-types (LTK, GLP2R, FREM3, CARM1P1 and COL22A1) and compares them with mouse\nL2/3. The claims were written from the preprint's text without its figures,\nand the code, read at commit 3daf9f0, had been updated for the later Nature\nversion, so its feature table, FREM3 cell set and pathology notebook differ\nfrom the preprint's. The cohort counts, depth by t-type, the type ANOVAs of\nelectrophysiology, GLP2R sag, the human against mouse comparison, the\nclassifiers, the FREM3 depth correlations, the deep L3 type tests and\npathology against electrophysiology were tested on the dandiset, and the\npathology scores, the NeuN sections and the morphology on the code's tables.\n`fig6c-carm1p1-upstroke-rin` is blocked as `methods_underspecified`, as it is\nreproduced with upstroke rate and partially reproduced with the\nupstroke/downstroke ratio (CARM1P1 4.63 against COL22A1 4.83, BH p 0.054), as\nis `fig6a-deep-dendrites`; four transcriptomic claims are blocked as `other`\nbecause the Allen Brain Map RNA-seq data cannot be pinned, `fig6f-smi32`\nbecause its images are public nowhere, and `fig5d-frem3-gene-depth` because the\nonly public table is the revision's (4417 genes against 790). The author put\nseven questions to a reader; the answers moved\n`edfig6-classifier-morphoelectric` from blocked to reproduced (0.720 and 0.582)\nand `fig1a-thickness` to reproduced on the human value alone (1.231 +/- 0.155\nmm). Round 1 gave its own outcome for 32 claims, none for\n`fig6-deep-morph-anova`, and agreed with the record on 26; on six blocked\nclaims it gave `data_missing` where the record gives `other`, which the\nclaims' `elsewhere` marking does not allow. It found the port of the mouse\nsection script faulty, and fixing it moved `fig1b-density` and\n`fig1c-soma-area` from partially reproduced and `fig1c-soma-variation` from\nblocked to reproduced (ratio 3.94); its question on sweep QC showed that IPFX\n2.1.2 applies only the noise limits, and adding the Methods' bias current and\nbridge balance limits moved `fig6-deep-ephys-anova` from partially reproduced\nto reproduced. Round 2 agreed with all 33, so there was no third round; it\nfound statements the outputs did not support, among them a run time of 14\nminutes against 21.0 printed and the link said to be confirmed by features\nfor all 283 cells where 261 have features on both sides, and these were\ncorrected. Some outcomes rest on weak ground: `fig4-glp2r-sag` has BH p 0.046\nand 0.060 with cell QC; `edtable1-species-ephys` gives 16 with Student's test\nunder cell QC; `fig6-deep-ephys-anova` turns on one feature, with tau at R2\n0.395; and `fig2ef-pathology-ephys` is not reproduced on the code's 283 cells.\nWhether cell QC applies and which input resistance the 15% bridge balance\nlimit means are asked in questions/000023.yaml and unanswered. Opening the 318\nfiles with remfile took about 8 minutes for metadata alone, so each was read\nwhole into memory; the notebook ran in 23.5 minutes at first and about 21 in\nthe last run, beyond the protocol's aim of ten.\n\nThe files carry no SpecimenID, the identifier by which the paper's code and\ntables name cells, so each was linked by its donor and its ephys session id,\nwhich lies 13 to 685 below the cell's SpecimenID; the code's features confirm\nthe link for 261 of the 283 cells that have them under the Methods' sweep QC\nand for 282 under IPFX's sweep QC alone, and for the 35 cells without features\nin the code the sample dates and tube order support it without proving it.\nThe files also carry no t-type, soma depth, brain region or medical condition,\non which every finding of the paper rests, so all labels come from the code;\nsession_description and the filtering field read PLACEHOLDER, and the archive\nsummary gives the variable measured as ProcessingModule and the technique as\n\"analytical technique\". The dandiset holds 318 of the 385 cells of the paper's\ntable, including all 283 with features in the code, from 56 donors against 90;\nof the 35 cells without features in the code, 19 give features here under the\nMethods' sweep QC (2 of them fail cell QC) and 25 under IPFX's sweep QC alone,\nand which recordings were judged too incomplete, or why, is not said. The\nmouse recordings are not in the dandiset, so the mouse claims rest on the\ncode's tables. The code's feature table measures adaptation, initial firing\nrate and tau differently from the Methods, and the features recomputed here\nmatch the code; it is consistent with sweep QC on noise alone, as with the\nMethods' limits 22 of its 283 cells give no features here, against 1, and 29\nof them fail cell QC as IPFX computes it. Code7_cortical_depth_code_mouse.r as\ncommitted does not give the values its comments print (mouse L2/3 thicknesses\nof 32, 133 and 90 um against 281, 223 and 257), and reading the lines as L1 to\nL4 with case_set_1 at 100 um = 165 pixels, the scale its own comment gives,\nreproduces them; Code6_cortical_depth_code_human.r never sets q9 to NULL, so\nthe human bin table counts the five sections unequally, which explains the\nprinted SD ratios of 2.4 and 4.0 against 2.33 and 3.94 with each section\ncounted once. Other findings: donor H18.03.318 is female in the files and male\nin the paper's tables, and donor H18.06.005 is 56 years old in the files and\n57 in both tables; the gene-depth table is from the revision, and the\nPatch-seq transcriptomes behind either version are not in the repository; and\nthe spike times computed with IPFX equal those stored in the files for the\nrheobase sweep of all 280 cells with features, with no spike in the second\nbefore any long-square step, so the stored spikes, responses and stimuli share\none clock.\n\nThe author's points on the protocol: the link claim names an identifier the\ndataset lacks while its matching is fixed in a criterion the author may not\nchange; `elsewhere` claims whose criterion is only \"Not tested on the\ndandiset\" must be tested or blocked for a reason other than `data_missing`;\ndata that is public but cannot be pinned has no `blocked_by` category; images\npublic nowhere cannot be `data_missing` when the claim is marked `elsewhere`;\nno category fits when the only public data is the wrong version; it does not\nsay whether one unmeasurable expected value makes a claim partial or blocked;\nit does not say how to treat an outside input that proves inconsistent; IPFX\nreads only a file path or an in-memory buffer, so streaming was slow; the\n1000-split classifiers the criterion requires put the run beyond ten minutes;\nit does not say whether to restrict to the paper's cohort when the link finds\nmore cells; the suggested clock check does not fit intracellular recordings;\nand the `with_labels` definition does not fit t-types and depths measured by\nother methods.\n"
}
```

```
File created successfully at: docs/pilot-notes/000023-berg-2020-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/000023-berg-2020-01.md",
 "old_string": "give no features here, against 1, and 29",
 "new_string": "give no features here, against 1 with IPFX's sweep QC alone, and 29"
}
```

```
The file docs/pilot-notes/000023-berg-2020-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -cn "—\|rather\|\*\*" docs/pilot-notes/000023-berg-2020-01.md; git status --short; wc -w docs/pilot-notes/000023-berg-2020-01.md
```

```
0
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
?? docs/pilot-notes/000023-berg-2020-01.md
?? scripts
1206 docs/pilot-notes/000023-berg-2020-01.md
```

**Agent**

I wrote `docs/pilot-notes/000023-berg-2020-01.md` and changed nothing else. It has no em dashes, no "rather" and no bold. The untracked dotfiles, `.idea`, `.vscode` and `scripts` in the repository root were not created by me, and I left them alone. Nothing is committed.

# 000023, Berg et al. 2020

Four claims reproduced, three partially, three not reproduced and one blocked
on the dandiset, with three more reproduced and one more partially reproduced
on the dandiset together with the paper's code tables; the link claim
`features-and-labels-link` is reproduced, and of the 17 claims on data
elsewhere, 10 are reproduced and 7 blocked. It pins version 0.210914.1900, the
only published version; the paper cites none. The paper, the bioRxiv preprint
"Human cortical expansion involves diversification and specialization of
supragranular intratelencephalic-projecting neurons", describes Patch-seq
neurons of human L2 and L3 from neurosurgical donors in five glutamatergic
t-types (LTK, GLP2R, FREM3, CARM1P1 and COL22A1) and compares them with mouse
L2/3. The claims were written from the preprint's text without its figures,
and the code, read at commit 3daf9f0, had been updated for the later Nature
version, so its feature table, FREM3 cell set and pathology notebook differ
from the preprint's. The cohort counts, depth by t-type, the type ANOVAs of
electrophysiology, GLP2R sag, the human against mouse comparison, the
classifiers, the FREM3 depth correlations, the deep L3 type tests and
pathology against electrophysiology were tested on the dandiset, and the
pathology scores, the NeuN sections and the morphology on the code's tables.
`fig6c-carm1p1-upstroke-rin` is blocked as `methods_underspecified`, as it is
reproduced with upstroke rate and partially reproduced with the
upstroke/downstroke ratio (CARM1P1 4.63 against COL22A1 4.83, BH p 0.054), as
is `fig6a-deep-dendrites`; four transcriptomic claims are blocked as `other`
because the Allen Brain Map RNA-seq data cannot be pinned, `fig6f-smi32`
because its images are public nowhere, and `fig5d-frem3-gene-depth` because the
only public table is the revision's (4417 genes against 790). The author put
seven questions to a reader; the answers moved
`edfig6-classifier-morphoelectric` from blocked to reproduced (0.720 and 0.582)
and `fig1a-thickness` to reproduced on the human value alone (1.231 +/- 0.155
mm). Round 1 gave its own outcome for 32 claims, none for
`fig6-deep-morph-anova`, and agreed with the record on 26; on six blocked
claims it gave `data_missing` where the record gives `other`, which the
claims' `elsewhere` marking does not allow. It found the port of the mouse
section script faulty, and fixing it moved `fig1b-density` and
`fig1c-soma-area` from partially reproduced and `fig1c-soma-variation` from
blocked to reproduced (ratio 3.94); its question on sweep QC showed that IPFX
2.1.2 applies only the noise limits, and adding the Methods' bias current and
bridge balance limits moved `fig6-deep-ephys-anova` from partially reproduced
to reproduced. Round 2 agreed with all 33, so there was no third round; it
found statements the outputs did not support, among them a run time of 14
minutes against 21.0 printed and the link said to be confirmed by features
for all 283 cells where 261 have features on both sides, and these were
corrected. Some outcomes rest on weak ground: `fig4-glp2r-sag` has BH p 0.046
and 0.060 with cell QC; `edtable1-species-ephys` gives 16 with Student's test
under cell QC; `fig6-deep-ephys-anova` turns on one feature, with tau at R2
0.395; and `fig2ef-pathology-ephys` is not reproduced on the code's 283 cells.
Whether cell QC applies and which input resistance the 15% bridge balance
limit means are asked in questions/000023.yaml and unanswered. Opening the 318
files with remfile took about 8 minutes for metadata alone, so each was read
whole into memory; the notebook ran in 23.5 minutes at first and about 21 in
the last run, beyond the protocol's aim of ten.

The files carry no SpecimenID, the identifier by which the paper's code and
tables name cells, so each was linked by its donor and its ephys session id,
which lies 13 to 685 below the cell's SpecimenID; the code's features confirm
the link for 261 of the 283 cells that have them under the Methods' sweep QC
and for 282 under IPFX's sweep QC alone, and for the 35 cells without features
in the code the sample dates and tube order support it without proving it.
The files also carry no t-type, soma depth, brain region or medical condition,
on which every finding of the paper rests, so all labels come from the code;
session_description and the filtering field read PLACEHOLDER, and the archive
summary gives the variable measured as ProcessingModule and the technique as
"analytical technique". The dandiset holds 318 of the 385 cells of the paper's
table, including all 283 with features in the code, from 56 donors against 90;
of the 35 cells without features in the code, 19 give features here under the
Methods' sweep QC (2 of them fail cell QC) and 25 under IPFX's sweep QC alone,
and which recordings were judged too incomplete, or why, is not said. The
mouse recordings are not in the dandiset, so the mouse claims rest on the
code's tables. The code's feature table measures adaptation, initial firing
rate and tau differently from the Methods, and the features recomputed here
match the code; it is consistent with sweep QC on noise alone, as with the
Methods' limits 22 of its 283 cells give no features here, against 1 with
IPFX's sweep QC alone, and 29 of them fail cell QC as IPFX computes it.
Code7_cortical_depth_code_mouse.r as committed does not give the values its
comments print (mouse L2/3 thicknesses of 32, 133 and 90 um against 281, 223
and 257), and reading the lines as L1 to L4 with case_set_1 at 100 um = 165
pixels, the scale its own comment gives, reproduces them;
Code6_cortical_depth_code_human.r never sets q9 to NULL, so the human bin
table counts the five sections unequally, which explains the printed SD
ratios of 2.4 and 4.0 against 2.33 and 3.94 with each section counted once.
Other findings: donor H18.03.318 is female in the files and male in the
paper's tables, and donor H18.06.005 is 56 years old in the files and 57 in
both tables; the gene-depth table is from the revision, and the Patch-seq
transcriptomes behind either version are not in the repository; and the spike
times computed with IPFX equal those stored in the files for the rheobase
sweep of all 280 cells with features, with no spike in the second before any
long-square step, so the stored spikes, responses and stimuli share one clock.

The author's points on the protocol: the link claim names an identifier the
dataset lacks while its matching is fixed in a criterion the author may not
change; `elsewhere` claims whose criterion is only "Not tested on the
dandiset" must be tested or blocked for a reason other than `data_missing`;
data that is public but cannot be pinned has no `blocked_by` category; images
public nowhere cannot be `data_missing` when the claim is marked `elsewhere`;
no category fits when the only public data is the wrong version; it does not
say whether one unmeasurable expected value makes a claim partial or blocked;
it does not say how to treat an outside input that proves inconsistent; IPFX
reads only a file path or an in-memory buffer, so streaming was slow; the
1000-split classifiers the criterion requires put the run beyond ten minutes;
it does not say whether to restrict to the paper's cohort when the link finds
more cells; the suggested clock check does not fit intracellular recordings;
and the `with_labels` definition does not fit t-types and depths measured by
other methods.

## End of run

14 turns, 2 minutes, result: success.
