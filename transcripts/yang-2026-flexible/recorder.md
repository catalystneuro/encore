# yang-2026-flexible · recorder · run 45067695545

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py yang-2026-flexible; ls transcripts/yang-2026-flexible/; grep -n -B2 -A12 '"000020"' targets/dandisets.json
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/asari-2009-02.md
| [000020](https://dandiarchive.org/dandiset/000020) | [Yang et al. 2026](https://doi.org/10.1523/eneuro.0275-26.2026) | 8 (+12) | 0 (+2) | 0 | 0 (+7) | [`yang-2026-flexible`](entries/yang-2026-flexible) |
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
```

**Agent calls Bash**

```bash
cd  for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 asari-2009-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; grep -n '000020' targets/dandisets.json | head; ls -la transcripts/yang-2026-flexible/
```

```
<persisted-output>
Output too large (35.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/89612152-fb12-488c-a69a-b54b0262214d/tool-results/bjza6q2u2.txt

Preview (first 2KB):
=== amjad-2025-01
# 002013, Amjad et al. 2025

Seven claims reproduced, one partially and five blocked on the dandiset,
plus one claim linking the dandiset to the paper's Zenodo deposit,
reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
agreed with every outcome. The paper describes microinvasive probes for
recording dopamine and electrical activity in monkeys; the beta burst,
reward and unit isolation claims reproduce, the dopamine reward effect
weakly (p = 0.023, and not in the stored trial-aligned `da`).

The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
the same conversion as 002014), and many findings are the same: each event
is stored about five times, once per overlapping trial window; trial
conditions are not in the trials table; the FSCV table columns carry no
units and the raw FSCV current is labelled amperes with values in the
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/89612152-fb12-488c-a69a-b54b0262214d/tool-results/bjza6q2u2.txt"
}
```

```
1	=== amjad-2025-01
2	# 002013, Amjad et al. 2025
3	
4	Seven claims reproduced, one partially and five blocked on the dandiset,
5	plus one claim linking the dandiset to the paper's Zenodo deposit,
6	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
7	agreed with every outcome. The paper describes microinvasive probes for
8	recording dopamine and electrical activity in monkeys; the beta burst,
9	reward and unit isolation claims reproduce, the dopamine reward effect
10	weakly (p = 0.023, and not in the stored trial-aligned `da`).
11	
12	The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
13	the same conversion as 002014), and many findings are the same: each event
14	is stored about five times, once per overlapping trial window; trial
15	conditions are not in the trials table; the FSCV table columns carry no
16	units and the raw FSCV current is labelled amperes with values in the
17	thousands; the bipolar LFP is stored in volts with a conversion factor that
18	makes it picovolts; and the raw ephys of one session and the spike times of
19	Monkey P are on different clocks from the rest of the file, by 9831.35 s and
20	6800.666 s, with nothing saying so. In addition, one session's trial-aligned
[... 496 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '20"' targets/dandisets.json | head; head -c 1500 targets/dandisets.json; echo; cat attempts/yang-2026-flexible-01.yaml
```

```
<persisted-output>
Output too large (60.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/89612152-fb12-488c-a69a-b54b0262214d/tool-results/bhlq15yod.txt

Preview (first 2KB):
2644:     "doi": "10.1101/2020.07.07.192120",
3045:   "dandiset": "000620",
3613:     "doi": "10.1016/j.celrep.2026.117420",
4028:     "doi": "10.1101/2023.09.08.556120",
4430:     "doi": "10.1016/j.yebeh.2023.109120",
5178:     "doi": "10.1016/j.yebeh.2023.109120",
8144:   "dandiset": "002020",
{
 "schema_version": 1,
 "generated": "2026-11-17T15:59:44+00:00",
 "source": "https://api.dandiarchive.org/api",
 "counts": {
  "public_dandisets": 678,
  "with_a_paper": 298,
  "with_a_published_version": 256,
  "papers": 316,
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
print([t for t in d['targets'] if t['dandiset']=='000020'])"
```

```
[]
```

**Agent**

No entry for 000020 exists in `targets/dandisets.json`, so the records don't say whether CatalystNeuro converted it. Next I'm reading the attempt record.

**Agent calls Read**

```json
{
 "file_path": "attempts/yang-2026-flexible-01.yaml"
}
```

```
1	schema_version: 3
2	id: yang-2026-flexible-01
3	datasets:
4	- archive: dandi
5	  id: '000020'
6	  version: 0.210913.1639
7	  doi: 10.48324/dandi.000020/0.210913.1639
8	  relation: reuses
9	paper: doi:10.1523/eneuro.0275-26.2026
10	date: '2026-11-22'
11	entry: yang-2026-flexible
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 973 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/yang-2026-flexible; for f in author-report.md author-revise-1-report.md author-revise-2-report.md claims-check-report.md claims-report.md verifier-1-report.md verifier-2-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (34.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/89612152-fb12-488c-a69a-b54b0262214d/tool-results/b01t838p5.txt

Preview (first 2KB):
=== author-report.md
## Report: yang-2026-flexible on DANDI:000020 (version 0.210913.1639)

The entry is locked, checked and run, and the handover is built (`executed/yang-2026-flexible/handover/`). Nothing is committed. The record is `attempts/yang-2026-flexible-01.yaml`.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| join-link (link claim I added) | reproduced |
| cohort-label-join, table1-phenotype-spaces (`assumed`), pc1-long-pulse-loadings | reproduced |
| fig1b-distance-correlation, fig1-fixed-five-pcs-ordering, fig1c-knn-jaccard, knn-scale-sweep | reproduced |
| split-half-reliability | partially reproduced |
| fig2c-eta2-ttype-over-cre, fig2d-knn-type-enrichment, fig2ab-ttype-structure-within-cre | reproduced |
| table2-alignment-ttype | partially reproduced |
| ttype-beyond-cre | partially reproduced |
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/89612152-fb12-488c-a69a-b54b0262214d/tool-results/b01t838p5.txt"
}
```

```
1	=== author-report.md
2	## Report: yang-2026-flexible on DANDI:000020 (version 0.210913.1639)
3	
4	The entry is locked, checked and run, and the handover is built (`executed/yang-2026-flexible/handover/`). Nothing is committed. The record is `attempts/yang-2026-flexible-01.yaml`.
5	
6	### 1. Outcomes
7	
8	| Claim | Outcome |
9	|---|---|
10	| join-link (link claim I added) | reproduced |
11	| cohort-label-join, table1-phenotype-spaces (`assumed`), pc1-long-pulse-loadings | reproduced |
12	| fig1b-distance-correlation, fig1-fixed-five-pcs-ordering, fig1c-knn-jaccard, knn-scale-sweep | reproduced |
13	| split-half-reliability | partially reproduced |
14	| fig2c-eta2-ttype-over-cre, fig2d-knn-type-enrichment, fig2ab-ttype-structure-within-cre | reproduced |
15	| table2-alignment-ttype | partially reproduced |
16	| ttype-beyond-cre | partially reproduced |
17	| fig3a, shared-map, subclass, equal-N, within-regime reliability, fig3b pair tags, threshold sensitivity, type-level-exceeds-cell-level | reproduced |
18	| mobility-distribution | reproduced |
19	| Six Figure 4 RNA claims, plus wgcna-mobility-within-type | blocked (`other`): the NeMO data server returned 502 or timed out from 09:20 to 11:49 UTC. WGCNA would also need R. |
20	
[... 298 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/readme_row.py; head -60 claims/yang-2026-flexible.yaml; grep -n "^- id:\|^  id:\|data:\|  figure\|location" claims/yang-2026-flexible.yaml | head -120
```

```
"""The README's table row for a paper, from its latest attempt.

    python tools/readme_row.py PAPER              # print the row (a paper key, or a dataset listed for one)

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/yang-2026-flexible.yaml'))
print({k:v for k,v in d.items() if k!='claims' and k!='checks'})
for c in d['claims']: print(c['id'],'|',c.get('location') or c.get('figure'),'|',c['statement'][:400]);print()
"
```

```
{'schema_version': 2, 'paper': 'doi:10.1523/eneuro.0275-26.2026'}
join-link | None | The NWB files of the dandiset are the cells of the paper's metadata join (results/m0/m0_molecular_join.csv of the paper's code at commit 61a5a41); matched by file stem, they have the same session, subject and genotype, and the same membership of the three regimes.

cohort-label-join | None | Of the cells, 4,430 have a row in the joined metadata table and 4,266 a non-empty t-type; the cells with a t-type number 4,183 in long-pulse, 3,988 in ramp and 4,266 in brief-pulse.

table1-phenotype-spaces | None | Built independently per regime, the phenotype spaces hold 4,344 long-pulse cells with 42 features and k80 = 11 components, 4,139 ramp cells with 20 features and k80 = 3, and 4,422 brief-pulse cells with 21 features and k80 = 5; the same-cell overlaps are 4,054 (long-pulse and ramp), 4,336 (long-pulse and brief-pulse), 4,134 (ramp and brief-pulse) and 4,049 (all three).

pc1-long-pulse-loadings | None | Long-pulse PC1 loads most strongly on rheobase or threshold current and on input resistance.

fig1b-distance-correlation | None | Pairwise cell-cell phenotypic distances are positively correlated across all three regime pairs, above shuffle and well below identity, strongest for long-pulse and ramp (Spearman rho 0.434), then ramp and brief-pulse (0.384), then long-pulse and brief-pulse (0.336).

fig1-fixed-five-pcs-ordering | None | The ordering of cross-regime distance correlations is unchanged when a fixed five principal components are kept in each regime instead of k80.

fig1c-knn-jaccard | None | Local neighborhoods are much less stable; the mean Jaccard overlap of each cell's 15 nearest neighbors across regimes is 0.023 (long-pulse and ramp), 0.022 (long-pulse and brief-pulse) and 0.019 (ramp and brief-pulse), only modestly above index-shuffle chance of about 0.002.

knn-scale-sweep | None | Across neighborhood sizes k = 15 to 600, chance-adjusted overlap rises with k but stays lo
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/yang-2026-flexible.yaml'))
print(list(d['claims'][3].keys()))
for c in d['claims']:
  q=c.get('quote') or c.get('quotes'); print(c['id'],'|',{k:v for k,v in c.items() if k in ('section','where','source','figure','panel','loc')}, '|', str(q)[:200])
"
```

```
['id', 'statement', 'source', 'quote', 'data', 'depends_on', 'criterion']
join-link | {'source': "Methods, Dataset and animals, last sentence; README of the paper's code, Data"} | n = 4,430 cells with a join row; n = 4,266 with a non-empty t-type
cohort-label-join | {'source': 'Methods, Dataset and animals, last sentence; Figure 2 legend'} | n = 4,430 cells with a join row; n = 4,266 with a non-empty t-type) ... Cell n with t-type: long-pulse 4,183; ramp 3,988; brief-pulse 4,266
table1-phenotype-spaces | {'source': 'Methods, Protocol-resolved cellular phenotype, paragraph 1; Table 1; Results, Cellular phenotypes are partially conserved, paragraph 1'} | Resulting dataset sizes are summarized in Table 1 (long-pulse: 4,344 cells, 42 features, k 80 = 11; ramp: 4,139 cells, 20 features, k 80 = 3; brief-pulse: 4,422 cells, 21 features, k 80 = 5) ... Same-
pc1-long-pulse-loadings | {'source': 'Results, Transcriptomic type anchors cellular phenotype, paragraph 1; Extended Data Figure 1-2D'} | Long-pulse PC1, used here only as a within-regime axis, loads most strongly on rheobase/threshold current and input resistance
fig1b-distance-correlation | {'source': 'Results, Cellular phenotypes are partially conserved, paragraph 2; Figure 1B; Table 2 rows a to c'} | Conservation was strongest between long-pulse and ramp responses (Spearman's ρ = 0.434 a , n = 4,054 shared cells), followed by ramp and brief-pulse responses ( ρ = 0.384 b , n = 4,134) and long-pulse
fig1-fixed-five-pcs-ordering | {'source': 'Results, Cellular phenotypes are partially conserved, paragraph 2; Extended Data Figure 1-2A'} | this ordering was unchanged when a fixed number of five principal components was retained instead of the 80% variance threshold
fig1c-knn-jaccard | {'source': 'Results, Cellular phenotypes are partially conserved, paragraph 3; Figure 1C'} | mean 15-nearest-neighbor Jaccard overlap was 0.023, 0.022, and 0.019 for the long-pulse–ramp, long-pulse–brief-pulse, and ramp–brief-pulse pairs, on
[... 23 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/yang-2026-flexible-01.md",
 "content": "# yang-2026-flexible, Yang et al. 2026\n\nEight claims reproduced on the dandiset alone and twelve more that also use\nthe Allen metadata, two partially, both with outside inputs, none not\nreproduced and seven blocked, all seven with outside inputs; `join-link`, the\nlink claim the author added to check the files against the paper's metadata\njoin, reproduced and is counted apart. One outcome, `table1-phenotype-spaces`,\nrests on an assumption. The first verification round agreed with all 30\noutcomes as they stood, giving the seven blocked claims the reason\ndata_missing where the record has other, and the second agreed with all 30\nafter `split-half-reliability` moved to reproduced; nothing was proposed after\nthe second, so there was no third round. It pins version 0.210913.1639, which\nthe paper cites and which is the only published version. The paper, Yang,\n\"Flexible Cellular Phenotypes Retain a Shared Type-Level Organization across\nResponse Regimes\" in eNeuro, reuses the Allen Institute Patch-seq recordings\nof mouse visual cortex neurons, builds a separate phenotype space for\nlong-pulse, ramp and brief-pulse responses, and reports that cell-level\ndistances and neighborhoods are only partly conserved across the regimes,\nthat t-type anchors the phenotype more than Cre line does, that type-type\ndistance maps are shared across regimes, and that transcriptomic distance\ntracks the shared map more than the regime-selective differences. The claims\nwere written from the version of record (PMC13737997) without the Extended\nData files, and from the paper's code at commit 61a5a41, which lacks the\nscript that ran IPFX on all cells and the one behind the 1,000-shuffle null of\nTable 2 rows m and n; the claims check corrected six criteria. Every claim on\nthe phenotype spaces, the cell-level and type-level comparisons and the t-type\nlabels was tested, and most counts equal the paper's exactly. Partial are the\nsize of the t-type alignment A_t (0.0337, 0.0278 and 0.0137 against 0.021,\n0.025 and 0.021, each p = 0.0099) and of the same after removing each Cre\nline's mean (0.0081, 0.0064 and 0.0103 against 0.011, 0.010 and 0.004), with\nno seed of five bringing all three within tolerance. The six Figure 4 claims\nand `wgcna-mobility-within-type` are blocked as other: the NeMO data server,\nthe only source the paper names for the public count matrix, answered 502 or\ntimed out on every request from 09:20 to 11:46 UTC and in both runs of the\nsecond revision, and the WGCNA claim would also need R. `split-half-reliability`\nwas partial in the first version, with the claim's seed giving 3,256 cells and\n16 random splits against 3,598 and 358; round 1 asked for the criterion's seed\n0, which gives the paper's 3,598 cells exactly, and the claim moved to\nreproduced, marked seed-sensitive. Round 2 found sentences the outputs did not\nsupport, among them a cause for the A_t offset given as the machine's sort,\nwhich was removed. In the first full pass a killed worker made the pool mark\n661 files as failed, fixed before the final runs; the first revision's run\ntook 77.5 minutes and needed the workflow's longer limits, as the default\n60-minute limit timed out during extraction, and the final runs took about 55\nminutes each.\n\nTwo files hold the same recording: sub-673135474_ses-680563483 and\nsub-673135516_ses-680897463 are from different mice, and the paper's join\ngives them different Cre lines (Vip-IRES-Cre and Ndnf-IRES2-dgCre), t-types\n(Vip Lmo1 Myl1 and Lamp5 Lsp1), layers and transcriptomic samples, yet the\nvoltage traces of all their usable long squares are identical (SHA-1) and so\nare all 94 of their IPFX features; no other two files share a trace or a\nfeature vector. The four files of subject 636828314 list two response series\nfor sweep number 1, so IPFX cannot open them, and the join has no row for\nthem either. The files hold no transcriptomic label or sample identifier, so\nt-types, subclasses and RNA sample ids come only from the Allen metadata,\njoined by session or file name; the Cre line can be read from the subject\ngenotype, which agrees with the Allen metadata for every cell. Otherwise every\ncount the paper reports for the dataset is in the files: of the 4,435 files,\n4,430 join to the paper's metadata with matching session, subject and\ngenotype, and IPFX 2.1.2 gives the paper's 4,344, 4,139 and 4,422 cells per\nregime, its 42, 20 and 21 retained features and its k80, with the long-square\nextraction failing in 87 of 4,431 files opened, the short-square in 9 and the\nramp in 2. Stimulus and response share a clock. On the paper's side, the code\nranks the binary t-type mismatch with ties in an arbitrary order, so A_t\ncarries an offset shared with its null; the code's own draws on the paper's\npublished PCA scores give 0.0370, 0.0316 and 0.0106 against the printed\n0.0214, 0.0250 and 0.0213, while A_t minus the null mean is within 0.0005 of\nthe printed difference, and what produces the gap is not shown. The\nsplit-half random fallback draws a fresh seed-0 permutation for each cell, so\nthe seed decides the pool (3,582 to 4,100 cells under the seeds 1000 to 4000),\nwhich the paper does not say. A question is put to the paper's author: which\nIPFX version and call made the feature table, what sets extract_ok, and where\nthe script for Table 2 rows m and n is.\n\nThe author's points on the protocol: adding a link claim means editing the\nclaims file, which the author is otherwise told not to change; notebook\nconclusions are part of the run hash, so writing them after the run forces a\nsecond 43-minute run; the protocol's seed rule can conflict with a reported\ncount that depends on the code's seed 0; no `blocked_by` value fits a public\ninput whose server is down, and `other` was used; Python 3.13 runs process\npools in spawn mode when a pool restarts its workers, and fork was used with\nthe author's own restarts; and nothing says how to rate a duplicate recording,\nrated critical.\n"
}
```

```
File created successfully at: docs/pilot-notes/yang-2026-flexible-01.md (file state is current in your context — no need to Read it back)
```

**Agent**

Notes written. Now the summary.

**Agent calls Write**

```json
{
 "file_path": "summaries/yang-2026-flexible-01.md",
 "content": "The paper's phenotype findings hold up in this data: cell-level distances are only partly conserved across long-pulse, ramp and brief-pulse responses, local neighborhoods hardly at all, t-type explains more phenotypic variance than Cre line, and type-level distance maps are shared across the three regimes. The transcriptomic findings of Figure 4 could not be tested, because the server holding the public gene count matrix did not answer during the run. The alignment of t-type with phenotype exceeds shuffled labels as reported, but its printed sizes were not matched, and the paper's code run on its own published scores does not give them either. Most counts, such as the 57 shared t-types, equal the paper's exactly.\n"
}
```

```
File created successfully at: summaries/yang-2026-flexible-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/yang-2026-flexible-01.md; grep -c '—\|rather' docs/pilot-notes/yang-2026-flexible-01.md summaries/yang-2026-flexible-01.md; git status --short
```

```
114 summaries/yang-2026-flexible-01.md
docs/pilot-notes/yang-2026-flexible-01.md:0
summaries/yang-2026-flexible-01.md:0
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
?? docs/pilot-notes/yang-2026-flexible-01.md
?? scripts
?? summaries/yang-2026-flexible-01.md
```

**Agent**

I wrote both files and changed nothing else (the untracked dotfiles, `.idea`, `.vscode` and `scripts` were already there). `targets/dandisets.json` has no entry for dandiset 000020, so the sources don't say whether CatalystNeuro converted it. The notes therefore say nothing about CatalystNeuro and do not open with that sentence.

`docs/pilot-notes/yang-2026-flexible-01.md`:

# yang-2026-flexible, Yang et al. 2026

Eight claims reproduced on the dandiset alone and twelve more that also use the Allen metadata, two partially, both with outside inputs, none not reproduced and seven blocked, all seven with outside inputs; `join-link`, the link claim the author added to check the files against the paper's metadata join, reproduced and is counted apart. One outcome, `table1-phenotype-spaces`, rests on an assumption. The first verification round agreed with all 30 outcomes as they stood, giving the seven blocked claims the reason data_missing where the record has other, and the second agreed with all 30 after `split-half-reliability` moved to reproduced; nothing was proposed after the second, so there was no third round. It pins version 0.210913.1639, which the paper cites and which is the only published version. The paper, Yang, "Flexible Cellular Phenotypes Retain a Shared Type-Level Organization across Response Regimes" in eNeuro, reuses the Allen Institute Patch-seq recordings of mouse visual cortex neurons, builds a separate phenotype space for long-pulse, ramp and brief-pulse responses, and reports that cell-level distances and neighborhoods are only partly conserved across the regimes, that t-type anchors the phenotype more than Cre line does, that type-type distance maps are shared across regimes, and that transcriptomic distance tracks the shared map more than the regime-selective differences. The claims were written from the version of record (PMC13737997) without the Extended Data files, and from the paper's code at commit 61a5a41, which lacks the script that ran IPFX on all cells and the one behind the 1,000-shuffle null of Table 2 rows m and n; the claims check corrected six criteria. Every claim on the phenotype spaces, the cell-level and type-level comparisons and the t-type labels was tested, and most counts equal the paper's exactly. Partial are the size of the t-type alignment A_t (0.0337, 0.0278 and 0.0137 against 0.021, 0.025 and 0.021, each p = 0.0099) and of the same after removing each Cre line's mean (0.0081, 0.0064 and 0.0103 against 0.011, 0.010 and 0.004), with no seed of five bringing all three within tolerance. The six Figure 4 claims and `wgcna-mobility-within-type` are blocked as other: the NeMO data server, the only source the paper names for the public count matrix, answered 502 or timed out on every request from 09:20 to 11:46 UTC and in both runs of the second revision, and the WGCNA claim would also need R. `split-half-reliability` was partial in the first version, with the claim's seed giving 3,256 cells and 16 random splits against 3,598 and 358; round 1 asked for the criterion's seed 0, which gives the paper's 3,598 cells exactly, and the claim moved to reproduced, marked seed-sensitive. Round 2 found sentences the outputs did not support, among them a cause for the A_t offset given as the machine's sort, which was removed. In the first full pass a killed worker made the pool mark 661 files as failed, fixed before the final runs; the first revision's run took 77.5 minutes and needed the workflow's longer limits, as the default 60-minute limit timed out during extraction, and the final runs took about 55 minutes each.

Two files hold the same recording: sub-673135474_ses-680563483 and sub-673135516_ses-680897463 are from different mice, and the paper's join gives them different Cre lines (Vip-IRES-Cre and Ndnf-IRES2-dgCre), t-types (Vip Lmo1 Myl1 and Lamp5 Lsp1), layers and transcriptomic samples, yet the voltage traces of all their usable long squares are identical (SHA-1) and so are all 94 of their IPFX features; no other two files share a trace or a feature vector. The four files of subject 636828314 list two response series for sweep number 1, so IPFX cannot open them, and the join has no row for them either. The files hold no transcriptomic label or sample identifier, so t-types, subclasses and RNA sample ids come only from the Allen metadata, joined by session or file name; the Cre line can be read from the subject genotype, which agrees with the Allen metadata for every cell. Otherwise every count the paper reports for the dataset is in the files: of the 4,435 files, 4,430 join to the paper's metadata with matching session, subject and genotype, and IPFX 2.1.2 gives the paper's 4,344, 4,139 and 4,422 cells per regime, its 42, 20 and 21 retained features and its k80, with the long-square extraction failing in 87 of 4,431 files opened, the short-square in 9 and the ramp in 2. Stimulus and response share a clock. On the paper's side, the code ranks the binary t-type mismatch with ties in an arbitrary order, so A_t carries an offset shared with its null; the code's own draws on the paper's published PCA scores give 0.0370, 0.0316 and 0.0106 against the printed 0.0214, 0.0250 and 0.0213, while A_t minus the null mean is within 0.0005 of the printed difference, and what produces the gap is not shown. The split-half random fallback draws a fresh seed-0 permutation for each cell, so the seed decides the pool (3,582 to 4,100 cells under the seeds 1000 to 4000), which the paper does not say. A question is put to the paper's author: which IPFX version and call made the feature table, what sets extract_ok, and where the script for Table 2 rows m and n is.

The author's points on the protocol: adding a link claim means editing the claims file, which the author is otherwise told not to change; notebook conclusions are part of the run hash, so writing them after the run forces a second 43-minute run; the protocol's seed rule can conflict with a reported count that depends on the code's seed 0; no `blocked_by` value fits a public input whose server is down, and `other` was used; Python 3.13 runs process pools in spawn mode when a pool restarts its workers, and fork was used with the author's own restarts; and nothing says how to rate a duplicate recording, rated critical.

`summaries/yang-2026-flexible-01.md` (114 words):

The paper's phenotype findings hold up in this data: cell-level distances are only partly conserved across long-pulse, ramp and brief-pulse responses, local neighborhoods hardly at all, t-type explains more phenotypic variance than Cre line, and type-level distance maps are shared across the three regimes. The transcriptomic findings of Figure 4 could not be tested, because the server holding the public gene count matrix did not answer during the run. The alignment of t-type with phenotype exceeds shuffled labels as reported, but its printed sizes were not matched, and the paper's code run on its own published scores does not give them either. Most counts, such as the 57 shared t-types, equal the paper's exactly.

## End of run

15 turns, 2 minutes, $1.01 at API prices, result: success.
