# 001752 · recorder · run 41714196744

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/001752 transcripts/001752; python tools/readme_row.py 001752; cat attempts/001752-liu-2026-01.yaml
```

```
<persisted-output>
Output too large (69.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9f817c8d-0329-4aa7-a184-318030422410/tool-results/bke21uvaj.txt

Preview (first 2KB):
docs/pilot-notes/001751-liu-2026-01.md
docs/pilot-notes/001750-liu-2026-01.md
docs/pilot-notes/001773-fujimoto-2026-01.md
docs/pilot-notes/001683-gao-2026-01.md
docs/pilot-notes/001687-xiao-2026-01.md
claims/001752:
10.1038-s41556-026-02009-4.yaml

transcripts/001752:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001752-liu-2026-01.yaml; for f in docs/pilot-notes/001751-liu-2026-01.md docs/pilot-notes/001750-liu-2026-01.md docs/pilot-notes/001773-fujimoto-2026-01.md docs/pilot-notes/001683-gao-2026-01.md docs/pilot-notes/001687-xiao-2026-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (119.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9f817c8d-0329-4aa7-a184-318030422410/tool-results/bmqnw52zk.txt

Preview (first 2KB):
schema_version: 2
id: 001752-liu-2026-01
dataset:
  archive: dandi
  id: '001752'
  version: 0.260825.0222
  doi: 10.48324/dandi.001752/0.260825.0222
paper: doi:10.1038/s41556-026-02009-4
date: 2026-11-03
entry: 001752-liu-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001752-liu-2026-01.yaml"
}
```

```
1	schema_version: 2
2	id: 001752-liu-2026-01
3	dataset:
4	  archive: dandi
5	  id: '001752'
6	  version: 0.260825.0222
7	  doi: 10.48324/dandi.001752/0.260825.0222
8	paper: doi:10.1038/s41556-026-02009-4
9	date: 2026-11-03
10	entry: 001752-liu-2026
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-13
19	  runner:
20	    platform: GitHub Actions
[... 760 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/001751-liu-2026-01.md"
}
```

```
1	# 001751, Liu et al. 2026
2	
3	Two claims reproduced, four partially, two not reproduced and one blocked for
4	missing data; the one claim that also uses inputs from outside the dataset,
5	`fig5-pc-rate-comparable-primate`, is counted apart and blocked as methods
6	underspecified, by its own criterion. Of the 35 claims, one is a link check,
7	`code-table-link`, added by the author and reproduced, and 24 have their data
8	elsewhere, in the paper's code repository, other dandisets, GEO, MetaboLights,
9	NeuroMorpho.org or the model, and are counted apart: six reproduced (two on an
10	assumption), three partially and 15 blocked. The first verification round
11	agreed with 31 of the 35 outcomes as they stood and the second with 34,
12	disagreeing on `patchseq-mapping`, which was kept blocked with the disagreement
13	recorded, and nothing was proposed after the second, so there was no third
14	round. It pins version 0.260825.0222, the only published version, with the
15	same file count and bytes as the draft; the paper cites none. The paper, Liu,
16	Huang, Shen, Shao, Jing et al., "An atlas of primate insular cortex reveals a
17	signal-processing strategy in von Economo neurons" in Nature Cell Biology, has
18	its Patch-seq, Na+ current and postsynaptic current recordings in DANDI:001746,
19	001750 and 001752; this dandiset holds the multi-patch recordings of Fig. 5d-i,
20	301 files of up to eight layer 5b neurons, for the finding that von Economo
[... 126 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/001750-liu-2026-01.md"
}
```

```
1	# 001750, Liu et al. 2026
2	
3	No claim on the dandiset reproduced: all three are blocked, two as methods
4	underspecified and one for missing data. Of the 34 claims, one is a link check,
5	`na-cell-table-link`, partially reproduced, and 30 have their data elsewhere,
6	in the paper's code repository, MetaboLights, other dandisets, GEO,
7	NeuroMorpho.org or the model, and are counted apart: three reproduced, one
8	partially, one not reproduced and 25 blocked. The first verification round
9	agreed with 32 of the 34 outcomes as they stood and the second with all 34, and
10	nothing was proposed after the second, so there was no third round. It pins
11	version 0.260825.0222, the only published version; the paper cites none. The
12	paper, Liu, Huang, Shen, Shao, Jing et al., "An atlas of primate insular cortex
13	reveals a signal-processing strategy in von Economo neurons" in Nature Cell
14	Biology, has its main Patch-seq recordings in DANDI:001746; this dandiset holds only its
15	outside-out recordings of somatic Na+ currents, 35 patches from one macaque in
16	two sessions, for the Fig. 4d finding that the currents are lower in von
17	Economo neurons (VENs, n = 14) than in L5 PCs (n = 21). The claims were written
18	from the version of record in Europe PMC (PMC13457102) without a PDF, the
19	Supplementary Information or the Source Data, and from the paper's code
20	(AIC_proj at commit 44cd8a6 and PatchAnaLab 1.0); the check made nine changes,
[... 107 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/001773-fujimoto-2026-01.md"
}
```

```
1	# 001773, Fujimoto et al. 2026
2	
3	Twenty-seven claims reproduced (11 on an assumption), none partially, one not
4	reproduced and four blocked, two as methods underspecified and two for missing
5	data. All 32 claims are on the dandiset. The first verification round agreed
6	with all 32 outcomes as they stood and so did the second, and nothing was
7	proposed after the second, so there was no third round. It pins version
8	0.260416.1939, the version the paper cites; the latest version, 0.260615.1838,
9	has identical asset ids. The paper, Fujimoto, Fujimoto, Elorette et al., "Deep
10	brain stimulation induces white matter remodeling and functional changes to
11	brain-wide networks" in Nature Neuroscience, implants an SCC-DBS lead in
12	monkeys N and T, stimulated for 6 weeks, and in monkey D, never stimulated, with
13	nonsurgical controls B, W and H, and reports home-cage behaviour (Extended Data
14	Fig. 1), FA of the white matter tracts (Fig. 2, Extended Data Fig. 2),
15	CC1-positive oligodendrocytes and EM g-ratios (Fig. 3, Extended Data Figs. 5
16	and 6), the whole-brain connectome (Fig. 4), seed connectivity of area 25 by
17	ROI and network (Fig. 5, Extended Data Figs. 7 and 9) and the same measures in
18	monkey D (Fig. 6, Extended Data Fig. 10). The claims were written from the
19	version of record in Europe PMC (PMC13337501) and the Supplementary
20	Information, without a PDF of the main article or the Source Data; the paper's
[... 107 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/001683-gao-2026-01.md"
}
```

```
1	# 001683, Gao et al. 2026
2	
3	Seven claims reproduced (three on an assumption), five partially (two on an
4	assumption), eight not reproduced (four on an assumption) and two blocked, one
5	as methods underspecified and one for missing data. All 22 claims are on the
6	dandiset. The first verification round agreed with 19 of the 22 outcomes as
7	they stood and the second with all 22, and nothing was proposed after the
8	second, so there was no third round. It pins version 0.260109.2104, the only
9	published version; the paper cites none. The paper, Gao, Frake, Durand and He,
10	"Transcranial Focused Ultrasound Stimulation Targeting White Matter Inhibits
11	Seizures in a Rat Model of Epilepsy" in IEEE Transactions on Neural Systems and
12	Rehabilitation Engineering, applies tFUS to the corpus callosum of rats with
13	seizures induced by 4-AP in right S1, 10 tFUS and 6 sham, and reports the
14	seizure metrics of the sham group (Fig. 2) and of both groups (Fig. 3), band
15	power and the asymmetry index (AI) of the EEG (Fig. 4, Figures S4 and S5), the
16	evoked potentials and phase lag index (PLI) of all 23 rats before 4-AP (Fig.
17	5) and the PLI of the epileptic rats (Fig. 6, Figure S7). The claims were
18	written from the NIH author manuscript in Europe PMC (PMC12848950) and its
19	supplement, without a PDF of the main paper, so the significance marks inside
20	Figs. 2 to 6 were not read; the paper links no code. The check made five
[... 107 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/001687-xiao-2026-01.md"
}
```

```
1	# 001687, Xiao et al. 2026
2	
3	Twelve claims reproduced, three partially, three not reproduced and 22 blocked,
4	16 for missing data and six for insufficient metadata; no outcome rests on an
5	assumption. Of the 41 claims, 40 are on the dandiset and one,
6	`fig6-model-telc-loses-map`, runs the paper's PrV circuit model from its code
7	repository and is counted apart: reproduced. The first verification round agreed
8	with 38 of the 41 outcomes as they stood and the second with all 41, and nothing
9	was proposed after the second, so there was no third round. It pins version
10	0.260821.2126, the latest published version; the paper cites none, and it holds
11	the same 191 assets as 0.260805.1529. The paper, Xiao, Severson et al.,
12	"Peri-head distance coding in the mouse brainstem" in Neuron, records units in
13	PrV of awake head-fixed mice while a wall passes the face at distances of 7 to
14	23 mm, and reports the proximity and map units of wild-type silicon-probe
15	recordings (Fig. 2, Figure S4), the decoding of wall distance from them (Fig. 3,
16	Figure S5), the effect of cutting all but one whisker (Fig. 4), SpVi-TeLC mice
17	(Fig. 5, Fig. 6, Figure S6), GtACR optogenetics (Figure S6), tungsten recordings
18	(Figure S2), whisker kinematics from video (Figure S1) and a circuit model (Fig.
19	6). The claims were written from the accepted author manuscript in PubMed
20	Central (NIHMS2191201, PMC13336321) and its supplement file, without the version
[... 120 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001752-liu-2026-01.yaml",
 "offset": 780
}
```

```
780	  - claim: scrna-no-sex-difference
781	    agrees: true
782	    outcome: blocked
783	    reason: The scRNA claims need GEO FASTQ or Zenodo (probably too_large).
784	    response: No change; the claim stays blocked as methods_underspecified by its criterion, with the size of the
785	      data in the notes.
786	  - claim: ven-firing-rate-variability
787	    agrees: true
788	    outcome: blocked
789	    reason: ven-firing-rate-variability is methods_underspecified.
790	    response: No change.
791	- date: '2026-11-03'
792	  kind: agent
793	  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)
794	  reviewed: Round 2. The re-executed notebooks reproduce_liu_2026.ipynb and elsewhere_liu_2026.ipynb in full, with their
795	    conclusions and summaries, the README, the claims file and the attempt record. The verifier did not re-run anything.
796	  results:
797	  - claim: psc-file-labels-link
798	    agrees: true
799	    outcome: partially_reproduced
[... 266 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat tools/readme_row.py | head -120; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if '001752' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
"
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
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 -A25 '"001752"' targets/dandisets.json | head -60; python - <<'E'
import yaml
d=yaml.safe_load(open('claims/001752/10.1038-s41556-026-02009-4.yaml'))
print({k:v for k,v in d.items() if k!='claims'})
for c in d['claims']: print(c['id'], c.get('kind'), c.get('data'), c.get('depends_on'))
E
```

```
7247-   "catalystneuro": []
7248-  },
7249-  {
7250:   "dandiset": "001752",
7251-   "name": "Electrophysiological Dataset of Neuronal Post-Synaptic Currents in the Primate Anterior Insular Cortex",
7252-   "published_version": "0.260825.0222",
7253-   "asset_count": 84,
7254-   "size_gb": 0.18,
7255-   "data_standards": [
7256-    "Neurodata Without Borders (NWB)"
7257-   ],
7258-   "species": [
7259-    "Macaca fascicularis - Cynomolgus monkeys"
7260-   ],
7261-   "approaches": [
7262-    "electrophysiological approach"
7263-   ],
7264-   "papers": [
7265-    {
7266-     "doi": "10.1038/s41556-026-02009-4",
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001752; ls -la --time-style=+%T; wc -w *-report.md
```

```
total 932
drwxr-xr-x   2 runner runner   4096 20:39:21 .
drwxr-xr-x 235 runner runner   4096 20:39:04 ..
-rw-r--r--   1 runner runner    536 20:39:20 answer-report.md
-rw-r--r--   1 runner runner   3577 20:39:20 answer.md
-rw-r--r--   1 runner runner   1985 20:39:20 author-answers-report.md
-rw-r--r--   1 runner runner   8293 20:39:20 author-answers.md
-rw-r--r--   1 runner runner   4771 20:39:20 author-report.md
-rw-r--r--   1 runner runner   4872 20:39:20 author-revise-1-report.md
-rw-r--r--   1 runner runner 229543 20:39:20 author-revise-1.md
-rw-r--r--   1 runner runner   3595 20:39:20 author-revise-2-report.md
-rw-r--r--   1 runner runner  82400 20:39:20 author-revise-2.md
-rw-r--r--   1 runner runner   1823 20:39:20 author-revise-3-report.md
-rw-r--r--   1 runner runner  41197 20:39:21 author-revise-3.md
-rw-r--r--   1 runner runner 279882 20:39:21 author.md
-rw-r--r--   1 runner runner   3524 20:39:04 claims-check-report.md
-rw-r--r--   1 runner runner  30465 20:39:04 claims-check.md
-rw-r--r--   1 runner runner   3705 20:39:04 claims-report.md
-rw-r--r--   1 runner runner  65465 20:39:04 claims.md
-rw-r--r--   1 runner runner   1205 20:39:04 paper-match-report.md
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001752; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md verifier-3-report.md author-revise-3-report.md; do echo "=== $f"; cat $f; echo; done
```

```
<persisted-output>
Output too large (42.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9f817c8d-0329-4aa7-a184-318030422410/tool-results/bm51kitp6.txt

Preview (first 2KB):
=== author-report.md
I finished steps 1 to 6: the entry passes `tools/entry.py all` and `check` with no errors, and the handover is built. The run took 1 h 20 min (14:30 to 15:50 UTC). Only one version of the dandiset is published, 0.260825.0222, so I pinned it; the paper cites none.

**1. Outcome per claim**

| Claim | Data | Outcome |
|---|---|---|
| psc-file-labels-link (link claim I added) | dataset plus the code's file table | partially reproduced |
| fig5b sEPSC frequency | with labels | blocked, methods_underspecified: at 5 pA VEN is lower (p = 0.029); at the RMS-noise threshold VEN is higher |
| fig5b sIPSC frequency | with labels | not reproduced |
| fig5b mEPSC frequency | with labels | not reproduced (depends on the mEPSC label conflict below) |
| fig5b mIPSC frequency | with labels | blocked, methods_underspecified: at 5 pA p = 0.0074; at RMS noise p = 0.24 |
| fig5c amplitudes (sEPSC, sIPSC, mEPSC, mIPSC) | with labels | reproduced (p = 0.23, 0.082, 0.61, 0.46) |
| ven-map-et-ct, fig3e, fig4j-amplitude, fig4d (DANDI:001750), ven-subtypes-similar-physiology (DANDI:001746) | elsewhere | reproduced |
| patchseq-mapping | elsewhere | reproduced, resting on an assumption |
| fig5-connectivity-total, fig5-connectivity-by-type, fig8a, fig8de | elsewhere | partially reproduced |
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/9f817c8d-0329-4aa7-a184-318030422410/tool-results/bm51kitp6.txt"
}
```

```
1	=== author-report.md
2	I finished steps 1 to 6: the entry passes `tools/entry.py all` and `check` with no errors, and the handover is built. The run took 1 h 20 min (14:30 to 15:50 UTC). Only one version of the dandiset is published, 0.260825.0222, so I pinned it; the paper cites none.
3	
4	**1. Outcome per claim**
5	
6	| Claim | Data | Outcome |
7	|---|---|---|
8	| psc-file-labels-link (link claim I added) | dataset plus the code's file table | partially reproduced |
9	| fig5b sEPSC frequency | with labels | blocked, methods_underspecified: at 5 pA VEN is lower (p = 0.029); at the RMS-noise threshold VEN is higher |
10	| fig5b sIPSC frequency | with labels | not reproduced |
11	| fig5b mEPSC frequency | with labels | not reproduced (depends on the mEPSC label conflict below) |
12	| fig5b mIPSC frequency | with labels | blocked, methods_underspecified: at 5 pA p = 0.0074; at RMS noise p = 0.24 |
13	| fig5c amplitudes (sEPSC, sIPSC, mEPSC, mIPSC) | with labels | reproduced (p = 0.23, 0.082, 0.61, 0.46) |
14	| ven-map-et-ct, fig3e, fig4j-amplitude, fig4d (DANDI:001750), ven-subtypes-similar-physiology (DANDI:001746) | elsewhere | reproduced |
15	| patchseq-mapping | elsewhere | reproduced, resting on an assumption |
16	| fig5-connectivity-total, fig5-connectivity-by-type, fig8a, fig8de | elsewhere | partially reproduced |
17	| fig2d-f (DANDI:001746) | elsewhere | not reproduced |
18	| scrna ×3, fig6f-g, fig6h, fig7c | elsewhere | blocked: too_large (two of the scRNA claims) or methods_underspecified (the third); the scRNA data are a 23 GB tar.gz, beyond this runner's 15 GB of memory |
19	| model ×3 | elsewhere | blocked, not_runnable: the hoc scripts are not in the repository |
20	| fig3c, fig4j-latency, fig6 morphology | elsewhere | blocked, metadata_insufficient |
[... 358 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -c 6000 claims/001752/10.1038-s41556-026-02009-4.yaml; echo; grep -n -i -E 'europe pmc|PMC1|nature cell|supplement|source data|version of record' claims/001752/10.1038-s41556-026-02009-4.yaml | head -30
```

```
# Claims for Liu, Huang, Shen, Shao, Jing et al. (2026), "An atlas of primate insular cortex
# reveals a signal-processing strategy in von Economo neurons", Nature Cell Biology 28,
# 1742-1757, doi:10.1038/s41556-026-02009-4 (named on the archive "Cell Atlas and Novel Signal
# Processing Strategy in Primate Insular Cortex"), on dandiset 001752.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Text read: the version of record, open access, as served by Europe PMC (PMC13457102), stored
# under paper/: main text, figure legends, Extended Data figure legends, Methods, Data and Code
# availability. No PDF was available, so values printed only inside figures (for example the
# p-values of Fig. 5b,c) could not be read. The Supplementary Information (Supplementary Figs.
# 1 to 17, Supplementary Tables 1 to 12) and the Source Data files were not in the text read;
# claims that cite them rest on the main text, and say so. The claims this dataset can test
# (Fig. 5a-c) rest on the main text, the Fig. 5 legend and the Methods, all of which were read.
#
# Code read: github.com/RFLiu2021/AIC_proj at commit 44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d
# (2026-07-05). It holds MATLAB and Python scripts per figure (its file names follow an older
# figure numbering; ephysio/Fig5ab_ana_sPSC.m and Fig5ab_ana_mPSC.m make the paper's Fig. 5b,c),
# per-cell summary tables (ephysio/data_ephy/sPSCs_Fig7ab.xlsx and miniEPSCs_Fig7ab.xlsx give one
# frequency and one mean amplitude per cell, already detected with miniAnalysis), and a table
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('attempts/001752-liu-2026-01.yaml'))
for v in d['verifications']: r=v['results']; print(len(r), sum(x['agrees'] for x in r), [x['claim'] for x in r if not x['agrees']])
print([k for k in d if k not in ('outcomes','verifications','findings','inputs')])
"; git log --format='%h %ad %s' --date=iso -- attempts/001752-liu-2026-01.yaml | tail -3
```

```
30 24 ['fig8a-metabolite-gradient', 'ven-subtypes-similar-physiology', 'fig4ac-ap-width-amplitude', 'fig6f-g-ven-subtype-mapping', 'fig3c-ais-distance-length', 'fig6-ven-subtype-morphology']
34 31 ['fig5b-sipsc-frequency', 'fig5c-sipsc-amplitude', 'fig4ac-ap-width-amplitude']
3 3 []
['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'provenance']
cb116c28b0 2026-11-03 19:42:47 +0000 Agent run on 001752: author-revise-2 (success)
f9b8fbc4c1 2026-11-03 18:30:12 +0000 Agent run on 001752: author-revise-1 (success)
14ce8b16e7 2026-11-03 15:51:21 +0000 Agent run on 001752: author (success)
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/notes.txt <<'EOF'
# 001752, Liu et al. 2026

Three claims reproduced, none partially, one not reproduced and four blocked, all four as methods underspecified; no outcome on the dandiset rests on an assumption. Of the 34 claims, one is a link check, `psc-file-labels-link`, added by the author and partially reproduced, and 25 have their data elsewhere, in the paper's code repository, DANDI:001746, 001750 and 001751, GEO, MetaboLights, Zenodo or the model, and are counted apart: five reproduced (two on an assumption), five partially, three not reproduced and 12 blocked. The first verification round agreed with 24 of the 30 outcomes it gave a view on and the second with 31 of 34; three outcome changes were proposed after the second, and a third round agreed with all three. It pins version 0.260825.0222, the only published version; the paper cites none. The paper, Liu, Huang, Shen, Shao, Jing et al., "An atlas of primate insular cortex reveals a signal-processing strategy in von Economo neurons" in Nature Cell Biology, has its Patch-seq, Na+ current and multi-patch recordings in DANDI:001746, 001750 and 001751; this dandiset holds the 84 voltage-clamp recordings of spontaneous and miniature postsynaptic currents of Fig. 5a-c, from von Economo neurons (VENs) and pyramidal cells (PCs), for the finding that VENs receive less frequent synaptic input with similar amplitudes. The claims were written from the version of record in Europe PMC (PMC13457102) without a PDF, the Supplementary Information or the Source Data, and from the paper's code (AIC_proj at commit 44cd8a6); the check made ten changes, one of them a new claim, and left three points open. The Fig. 5 claims rest on the cell types of the code's table metadata_PSC.csv, as the files carry none, and events were detected with a detector of miniAnalysis's scheme, not with miniAnalysis. Reproduced are `fig5c-sepsc-amplitude` (VEN 8.20 against PC 8.51 pA, p = 0.24, though the RMS, first 30 s and three times the noise variants give p = 0.012, 0.033 and 0.016), `fig5c-mepsc-amplitude` (p = 0.61) and `fig5c-mipsc-amplitude` (p = 0.46). `fig5b-mepsc-frequency` is not reproduced: with the table's labels the VEN median is above the PC median (0.92 against 0.69 Hz at 5 pA, p = 0.61), while the sheet's own frequencies give VEN 1.39 against PC 1.80 Hz (p = 0.028) with the sheet's labels and VEN 1.97 against PC 1.39 Hz (p = 0.029) with the table's, so the paper's result follows from its labelling. `fig5b-sepsc-frequency` and `fig5b-mipsc-frequency` are blocked because the threshold readings disagree: at 5 pA VENs are lower (2.06 against 9.36 Hz, p = 0.026, and 1.23 against 2.35 Hz, p = 0.0074), while at the recording's RMS noise, a reading the detector check shows counts noise, VENs are higher for sEPSC (p = 0.091) and the mIPSC difference is not significant (p = 0.24). `fig5b-sipsc-frequency` and `fig5c-sipsc-amplitude` are blocked because the detection does not separate events from noise in the sIPSC files. The link is partial because file fwphyw is named by no row and 1s3ysck by two, the mEPSC cell types are opposite to the sheet's for all 15 matched cells, and the frequencies measured here correlate with the sheet's only for mIPSC (rho 0.73). Of the claims on other data, `ven-map-et-ct` (15 and 14), `fig3e-phase-peak-index` (VEN median 0.117, Kruskal-Wallis p = 4.9e-08) and `fig4j-eepsp-amplitude` (cell type p = 0.0034, the paper's value) are reproduced on the code's per-cell tables, `patchseq-mapping` on the assumption that the inhibitory neurons are the 33 cells the code labels as interneurons (273 excitatory neurons, 17 clusters each), and `fig4d-sodium-current` on the 35 files of DANDI:001750, on the assumption that one patch area for all patches is an acceptable density reading (VEN median 23.0 against PC 34.6 pA, p = 0.0023). Partial are `fig5-connectivity-total` (1,416 tested pairs within the tolerance of 1,292, 26 connections outside that of 31), `fig6-ven-subtype-morphology` (the axon part holds, the basal field area is not in the table), `fig6f-g-ven-subtype-mapping` (12 and 10, or 10 and 7 for traced VENs, against 10 and 11), `ven-subtypes-similar-physiology` (no difference on 34 of the paper's 126 VENs, which holds only for lack of power) and `fig8de-glycolytic-bias` (2-ketobutyrate lower but p = 0.18). Not reproduced are `fig2d-f-l23-it-tau-width` (no pairwise tau difference survives FDR, and IT RORB has the lower AP half-width, 1.92 against 2.10 ms), `fig4ac-ap-width-amplitude` (p = 0.015 and 0.073 on the 68 VENs and 135 L5 PCs of DANDI:001746, against the criterion's p < 0.001, and these may not be the cells of Fig. 4a-c) and `fig8a-metabolite-gradient` (179 and 85 metabolites against 228 and 108). Four claims are blocked as too large, as the scRNA-seq data are one 23 GB archive on GEO, beyond the runner's 15 GB of memory; three as not runnable, as the NEURON model is not in the repository; `fig3c-ais-distance-length` and `fig4j-eepsp-latency` as metadata insufficient; and `scrna-no-sex-difference`, `ven-firing-rate-variability` and `fig5-connectivity-by-type` as methods underspecified, the last by its criterion, as DANDI:001751 holds no annotations. The author's first run gave on the dandiset four reproduced, two not reproduced and two blocked, with the sIPSC frequency not reproduced and the sIPSC amplitude reproduced, and differed on six of the claims on other data. The author asked no questions of a reader, so the answer and author-answers runs changed nothing. Round 1 disagreed on `fig8a-metabolite-gradient`, `ven-subtypes-similar-physiology`, `fig4ac-ap-width-amplitude`, `fig6f-g-ven-subtype-mapping`, `fig3c-ais-distance-length` and `fig6-ven-subtype-morphology`, and found that the RMS threshold counts noise, that at 5 pA the threshold is at or below the noise in many spontaneous-current files, that the sheet's own mEPSC values were never tested, that the rank-sum test was not exact as MATLAB's is, that the fig2d-f extraction had obvious failures, that fig8a used the code's table, not MetaboLights, and that the connectivity counts came from the code's annotation without a check of the deposit; in reply a detector check with opposite-polarity peaks and injected events, noise strata, tests on the sheets' values, MATLAB's ranksum, a revised AP threshold, the MetaboLights test and a check of DANDI:001751 were added, five outcomes changed, `fig6f-g-ven-subtype-mapping` to partially reproduced against the verifier's not reproduced, `fig3c-ais-distance-length` was kept blocked, and a question on the threshold reading was filed in `questions/001752.yaml`, after the reader's run. Round 2 disagreed on the two sIPSC claims and `fig4ac-ap-width-amplitude`, asked that `fig4d-sodium-current` be marked as resting on an assumption, and found sentences the outputs did not support (an overstated detector check, the wrong cell type for S02C0321, three notebook sentences) and 464 tau values for 462 cells; in reply the flag was set, the text was corrected, the duplicate was traced to a file named twice in the code's table, and the three changes were proposed. Round 3 agreed with all three, which were made, and a question on whether DANDI:001746 holds the cells of Fig. 4a-c was filed. The author's run took 1 h 20 min (14:30 to 15:50 UTC) and nothing failed; the two notebooks ran in about 65 and 215 s at first, 143 and 445 s after the author-answers run, 91 and 633 s after round 1 and 106 and 693 s after round 2. `tools/build_site.py` and `tools/site_assets/app.css`, modified before the last run, were left alone.

The NWB files carry no cell type, the variable every Fig. 5 comparison needs; it is given only in the code's table metadata_PSC.csv, and the cell_id in the files is not unique within a session (three pairs share one). For every mEPSC cell that table gives the opposite cell type to the code's analysis sheet miniEPSCs_Fig7ab.xlsx, which the Fig. 5 script reads, so with the table's labels VENs have the higher mEPSC frequency and with the sheet's the lower, and the dandiset cannot settle which is right. The dandiset holds 15 mEPSC recordings (7 VENs and 8 PCs by the table) where the paper reports 8 VENs and 8 PCs; the sheet's cell S02C0321 has no file. The table gives one sIPSC file (obj-1s3ysck) to two cells, PC 20201126s5c11a and VEN 20201126s5c11b, and names the other file of that session's Cell_AS011 (obj-fwphyw) in no row. The Methods state that IPSCs were recorded at -60 mV with a CsCl internal, while the spontaneous IPSC files are described as held at +20 mV, hold positive currents of 107 to 979 pA and outward events, and the code names them +20mV. No sIPSC file has noise below 2 pA, and a standard detector at the Methods' 5 pA threshold finds opposite-polarity peaks at 0.87 to 1.54 times the rate of events in 13 of the 15 files; in the noisier sEPSC and sIPSC recordings it finds 4.6 to 15 times the sheet's events. 22 of the 36 mIPSC files end in runs of exact zeros (6,795 to 30,167 samples, up to 30 s), 44 of the 84 recordings are shorter than the 5 min the Methods give as the minimum, and the noise of 11 of 15 sIPSC and 2 of 18 sEPSC recordings exceeds the 5 pA the Methods give as the largest RMS noise. Of the other data, DANDI:001751 holds no cell type for any electrode and no connection annotation; the code's annotation metadata_multiPatch.xlsx, which names 288 of its 301 files, lists 1,416 tested pairs and 26 connections, including one VEN-to-PC connection, where the paper reports 1,292 pairs, 31 connections and none, types 7 of its 18 PC-to-PC connections as inhibitory and gives two connections a projection label naming other channels than their row. The Fig. 8 legend and Results name Welch's ANOVA and the Games-Howell test, while the code's metabolomics notebook uses Dunn's test with Holm correction; the MetaboLights deposit MTBLS13927 and the code's table hold 558 identified metabolites where the paper reports 581, the deposit swaps the values of samples V1-4-Q and V1-4-S relative to the code's table and names the sample of AIC animal 1 A1C-1-Q. The code's README places the NEURON model in a 'modelling/' folder the repository at commit 44cd8a6 does not hold. The morphology table morphFeatTables_PC_VENL_VENS.xlsx codes cell types as 1, 3, 4 and 5 with no key, which only the cell lists of the Fig. 6d script give, and lacks the basal dendritic field area. In the Patch-seq cell table metaInfo_ephysio_patchSeq.csv, 5 of the 34 cells with a VEN subtype have cell type PC, INTER or none, one VEN_Short maps to an inhibitory cluster, one file (obj-1gxrou) is named by two rows and one file of DANDI:001746 by none. Questions are put to the paper's authors: which miniAnalysis settings detected the Fig. 5 events and which stretch of each recording was analysed; which rows of the Patch-seq mapping tables are the 34 inhibitory neurons and which cluster numbering they follow; and whether Fig. 4d compares peak currents or densities from each patch's own capacitance, and where the capacitances are.

The author's points on the protocol: the criteria block when the two threshold readings disagree while step 1.6 allows adopting the best-supported reading, and the criteria were followed; the claims say "the dataset's labels" though the dataset has none, so `data: with_labels` and `depends_on` were set on the eight Fig. 5 claims, and the protocol does not say whether an author may change those fields; the clock check assumes trial tables these recordings lack, so the time base was checked with event decay times and the code's per-cell counts; streaming with remfile was about 100 times slower for DANDI:001746, so each file was read whole into memory; the first too_large estimates used remfile's 4.4 MB/s where bulk reads ran at about 300 MB/s, so the protocol should say to time the read method itself; it is unclear whether code tables count as the elsewhere data, and data missing from the named deposit cannot be blocked as data_missing for an elsewhere claim, so `other` was used; the supplement PDFs are now under `paper/` but the claims file was written without them, and the criteria that block unless supplied were kept; and a link criterion that checks per-cell agreement also tests the author's detector, not only which file is which.
EOF
python - <<'E'
import textwrap,os
src=open(os.environ['TMPDIR']+'/notes.txt').read().split('\n\n')
out=[]
for p in src:
    out.append(p if p.startswith('#') else textwrap.fill(p,79,break_on_hyphens=False,break_long_words=False))
open('docs/pilot-notes/001752-liu-2026-01.md','w').write('\n\n'.join(o.rstrip('\n') for o in out)+'\n')
E
grep -n -E '—|rather|\*\*' docs/pilot-notes/001752-liu-2026-01.md; wc -w docs/pilot-notes/001752-liu-2026-01.md docs/pilot-notes/001751-liu-2026-01.md; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -A3 -E 'id: fig5(b-sepsc-frequency|c-sepsc-amplitude)' claims/001752/10.1038-s41556-026-02009-4.yaml
```

```
90:- id: fig5b-sepsc-frequency
91-  statement: The frequency of spontaneous EPSCs is lower in VENs than in neighbouring PCs.
92-  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 1; Figure 5b
93-  quote: The frequencies of both excitatory and inhibitory events were significantly lower in VENs
--
170:- id: fig5c-sepsc-amplitude
171-  statement: The amplitude of spontaneous EPSCs does not differ significantly between VENs and
172-    PCs.
173-  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 1; Figure 5c
```

**Agent calls Bash**

```bash
cd  sed -i -e 's/for the finding that VENs receive less frequent synaptic input with similar amplitudes/for the finding that excitatory and inhibitory events are less frequent in VENs than in PCs while their amplitudes do not differ/' -e 's/were added, five outcomes changed, /were added, six outcomes changed, /' $TMPDIR/notes.txt; grep -c 'six outcomes changed' $TMPDIR/notes.txt; grep -c 'less frequent in VENs' $TMPDIR/notes.txt
python - <<'E'
import textwrap,os
src=open(os.environ['TMPDIR']+'/notes.txt').read().split('\n\n')
out=[p.rstrip('\n') if p.startswith('#') else textwrap.fill(p,79,break_on_hyphens=False,break_long_words=False) for p in src]
open('docs/pilot-notes/001752-liu-2026-01.md','w').write('\n\n'.join(out)+'\n')
E
cat docs/pilot-notes/001752-liu-2026-01.md
```

```
1
1
# 001752, Liu et al. 2026

Three claims reproduced, none partially, one not reproduced and four blocked,
all four as methods underspecified; no outcome on the dandiset rests on an
assumption. Of the 34 claims, one is a link check, `psc-file-labels-link`,
added by the author and partially reproduced, and 25 have their data elsewhere,
in the paper's code repository, DANDI:001746, 001750 and 001751, GEO,
MetaboLights, Zenodo or the model, and are counted apart: five reproduced (two
on an assumption), five partially, three not reproduced and 12 blocked. The
first verification round agreed with 24 of the 30 outcomes it gave a view on
and the second with 31 of 34; three outcome changes were proposed after the
second, and a third round agreed with all three. It pins version 0.260825.0222,
the only published version; the paper cites none. The paper, Liu, Huang, Shen,
Shao, Jing et al., "An atlas of primate insular cortex reveals a
signal-processing strategy in von Economo neurons" in Nature Cell Biology, has
its Patch-seq, Na+ current and multi-patch recordings in DANDI:001746, 001750
and 001751; this dandiset holds the 84 voltage-clamp recordings of spontaneous
and miniature postsynaptic currents of Fig. 5a-c, from von Economo neurons
[... 148 more lines not kept]
```

**Agent**

I've written `docs/pilot-notes/001752-liu-2026-01.md`, and it is the only file I added or changed. The counts in the first paragraph match what `python tools/readme_row.py 001752` prints. The `catalystneuro` field for 001752 is empty, so the second paragraph doesn't open with the CatalystNeuro sentence. The run's two unusual points are in the first paragraph: there was a third verification round, and nothing failed. Nothing is committed. Here is the subsection:

# 001752, Liu et al. 2026

Three claims reproduced, none partially, one not reproduced and four blocked,
all four as methods underspecified; no outcome on the dandiset rests on an
assumption. Of the 34 claims, one is a link check, `psc-file-labels-link`,
added by the author and partially reproduced, and 25 have their data elsewhere,
in the paper's code repository, DANDI:001746, 001750 and 001751, GEO,
MetaboLights, Zenodo or the model, and are counted apart: five reproduced (two
on an assumption), five partially, three not reproduced and 12 blocked. The
first verification round agreed with 24 of the 30 outcomes it gave a view on
and the second with 31 of 34; three outcome changes were proposed after the
second, and a third round agreed with all three. It pins version 0.260825.0222,
the only published version; the paper cites none. The paper, Liu, Huang, Shen,
Shao, Jing et al., "An atlas of primate insular cortex reveals a
signal-processing strategy in von Economo neurons" in Nature Cell Biology, has
its Patch-seq, Na+ current and multi-patch recordings in DANDI:001746, 001750
and 001751; this dandiset holds the 84 voltage-clamp recordings of spontaneous
and miniature postsynaptic currents of Fig. 5a-c, from von Economo neurons
(VENs) and pyramidal cells (PCs), for the finding that excitatory and
inhibitory events are less frequent in VENs than in PCs while their amplitudes
do not differ. The claims were written from the version of record in Europe PMC
(PMC13457102) without a PDF, the Supplementary Information or the Source Data,
and from the paper's code (AIC_proj at commit 44cd8a6); the check made ten
changes, one of them a new claim, and left three points open. The Fig. 5 claims
rest on the cell types of the code's table metadata_PSC.csv, as the files carry
none, and events were detected with a detector of miniAnalysis's scheme, not
with miniAnalysis. Reproduced are `fig5c-sepsc-amplitude` (VEN 8.20 against PC
8.51 pA, p = 0.24, though the RMS, first 30 s and three times the noise
variants give p = 0.012, 0.033 and 0.016), `fig5c-mepsc-amplitude` (p = 0.61)
and `fig5c-mipsc-amplitude` (p = 0.46). `fig5b-mepsc-frequency` is not
reproduced: with the table's labels the VEN median is above the PC median (0.92
against 0.69 Hz at 5 pA, p = 0.61), while the sheet's own frequencies give VEN
1.39 against PC 1.80 Hz (p = 0.028) with the sheet's labels and VEN 1.97
against PC 1.39 Hz (p = 0.029) with the table's, so the paper's result follows
from its labelling. `fig5b-sepsc-frequency` and `fig5b-mipsc-frequency` are
blocked because the threshold readings disagree: at 5 pA VENs are lower (2.06
against 9.36 Hz, p = 0.026, and 1.23 against 2.35 Hz, p = 0.0074), while at the
recording's RMS noise, a reading the detector check shows counts noise, VENs
are higher for sEPSC (p = 0.091) and the mIPSC difference is not significant (p
= 0.24). `fig5b-sipsc-frequency` and `fig5c-sipsc-amplitude` are blocked
because the detection does not separate events from noise in the sIPSC files.
The link is partial because file fwphyw is named by no row and 1s3ysck by two,
the mEPSC cell types are opposite to the sheet's for all 15 matched cells, and
the frequencies measured here correlate with the sheet's only for mIPSC (rho
0.73). Of the claims on other data, `ven-map-et-ct` (15 and 14),
`fig3e-phase-peak-index` (VEN median 0.117, Kruskal-Wallis p = 4.9e-08) and
`fig4j-eepsp-amplitude` (cell type p = 0.0034, the paper's value) are
reproduced on the code's per-cell tables, `patchseq-mapping` on the assumption
that the inhibitory neurons are the 33 cells the code labels as interneurons
(273 excitatory neurons, 17 clusters each), and `fig4d-sodium-current` on the
35 files of DANDI:001750, on the assumption that one patch area for all patches
is an acceptable density reading (VEN median 23.0 against PC 34.6 pA, p =
0.0023). Partial are `fig5-connectivity-total` (1,416 tested pairs within the
tolerance of 1,292, 26 connections outside that of 31),
`fig6-ven-subtype-morphology` (the axon part holds, the basal field area is not
in the table), `fig6f-g-ven-subtype-mapping` (12 and 10, or 10 and 7 for traced
VENs, against 10 and 11), `ven-subtypes-similar-physiology` (no difference on
34 of the paper's 126 VENs, which holds only for lack of power) and
`fig8de-glycolytic-bias` (2-ketobutyrate lower but p = 0.18). Not reproduced
are `fig2d-f-l23-it-tau-width` (no pairwise tau difference survives FDR, and IT
RORB has the lower AP half-width, 1.92 against 2.10 ms),
`fig4ac-ap-width-amplitude` (p = 0.015 and 0.073 on the 68 VENs and 135 L5 PCs
of DANDI:001746, against the criterion's p < 0.001, and these may not be the
cells of Fig. 4a-c) and `fig8a-metabolite-gradient` (179 and 85 metabolites
against 228 and 108). Four claims are blocked as too large, as the scRNA-seq
data are one 23 GB archive on GEO, beyond the runner's 15 GB of memory; three
as not runnable, as the NEURON model is not in the repository;
`fig3c-ais-distance-length` and `fig4j-eepsp-latency` as metadata insufficient;
and `scrna-no-sex-difference`, `ven-firing-rate-variability` and
`fig5-connectivity-by-type` as methods underspecified, the last by its
criterion, as DANDI:001751 holds no annotations. The author's first run gave on
the dandiset four reproduced, two not reproduced and two blocked, with the
sIPSC frequency not reproduced and the sIPSC amplitude reproduced, and differed
on six of the claims on other data. The author asked no questions of a reader,
so the answer and author-answers runs changed nothing. Round 1 disagreed on
`fig8a-metabolite-gradient`, `ven-subtypes-similar-physiology`,
`fig4ac-ap-width-amplitude`, `fig6f-g-ven-subtype-mapping`,
`fig3c-ais-distance-length` and `fig6-ven-subtype-morphology`, and found that
the RMS threshold counts noise, that at 5 pA the threshold is at or below the
noise in many spontaneous-current files, that the sheet's own mEPSC values were
never tested, that the rank-sum test was not exact as MATLAB's is, that the
fig2d-f extraction had obvious failures, that fig8a used the code's table, not
MetaboLights, and that the connectivity counts came from the code's annotation
without a check of the deposit; in reply a detector check with
opposite-polarity peaks and injected events, noise strata, tests on the sheets'
values, MATLAB's ranksum, a revised AP threshold, the MetaboLights test and a
check of DANDI:001751 were added, six outcomes changed,
`fig6f-g-ven-subtype-mapping` to partially reproduced against the verifier's
not reproduced, `fig3c-ais-distance-length` was kept blocked, and a question on
the threshold reading was filed in `questions/001752.yaml`, after the reader's
run. Round 2 disagreed on the two sIPSC claims and `fig4ac-ap-width-amplitude`,
asked that `fig4d-sodium-current` be marked as resting on an assumption, and
found sentences the outputs did not support (an overstated detector check, the
wrong cell type for S02C0321, three notebook sentences) and 464 tau values for
462 cells; in reply the flag was set, the text was corrected, the duplicate was
traced to a file named twice in the code's table, and the three changes were
proposed. Round 3 agreed with all three, which were made, and a question on
whether DANDI:001746 holds the cells of Fig. 4a-c was filed. The author's run
took 1 h 20 min (14:30 to 15:50 UTC) and nothing failed; the two notebooks ran
in about 65 and 215 s at first, 143 and 445 s after the author-answers run, 91
and 633 s after round 1 and 106 and 693 s after round 2. `tools/build_site.py`
and `tools/site_assets/app.css`, modified before the last run, were left alone.

The NWB files carry no cell type, the variable every Fig. 5 comparison needs;
it is given only in the code's table metadata_PSC.csv, and the cell_id in the
files is not unique within a session (three pairs share one). For every mEPSC
cell that table gives the opposite cell type to the code's analysis sheet
miniEPSCs_Fig7ab.xlsx, which the Fig. 5 script reads, so with the table's
labels VENs have the higher mEPSC frequency and with the sheet's the lower, and
the dandiset cannot settle which is right. The dandiset holds 15 mEPSC
recordings (7 VENs and 8 PCs by the table) where the paper reports 8 VENs and 8
PCs; the sheet's cell S02C0321 has no file. The table gives one sIPSC file
(obj-1s3ysck) to two cells, PC 20201126s5c11a and VEN 20201126s5c11b, and names
the other file of that session's Cell_AS011 (obj-fwphyw) in no row. The Methods
state that IPSCs were recorded at -60 mV with a CsCl internal, while the
spontaneous IPSC files are described as held at +20 mV, hold positive currents
of 107 to 979 pA and outward events, and the code names them +20mV. No sIPSC
file has noise below 2 pA, and a standard detector at the Methods' 5 pA
threshold finds opposite-polarity peaks at 0.87 to 1.54 times the rate of
events in 13 of the 15 files; in the noisier sEPSC and sIPSC recordings it
finds 4.6 to 15 times the sheet's events. 22 of the 36 mIPSC files end in runs
of exact zeros (6,795 to 30,167 samples, up to 30 s), 44 of the 84 recordings
are shorter than the 5 min the Methods give as the minimum, and the noise of 11
of 15 sIPSC and 2 of 18 sEPSC recordings exceeds the 5 pA the Methods give as
the largest RMS noise. Of the other data, DANDI:001751 holds no cell type for
any electrode and no connection annotation; the code's annotation
metadata_multiPatch.xlsx, which names 288 of its 301 files, lists 1,416 tested
pairs and 26 connections, including one VEN-to-PC connection, where the paper
reports 1,292 pairs, 31 connections and none, types 7 of its 18 PC-to-PC
connections as inhibitory and gives two connections a projection label naming
other channels than their row. The Fig. 8 legend and Results name Welch's ANOVA
and the Games-Howell test, while the code's metabolomics notebook uses Dunn's
test with Holm correction; the MetaboLights deposit MTBLS13927 and the code's
table hold 558 identified metabolites where the paper reports 581, the deposit
swaps the values of samples V1-4-Q and V1-4-S relative to the code's table and
names the sample of AIC animal 1 A1C-1-Q. The code's README places the NEURON
model in a 'modelling/' folder the repository at commit 44cd8a6 does not hold.
The morphology table morphFeatTables_PC_VENL_VENS.xlsx codes cell types as 1,
3, 4 and 5 with no key, which only the cell lists of the Fig. 6d script give,
and lacks the basal dendritic field area. In the Patch-seq cell table
metaInfo_ephysio_patchSeq.csv, 5 of the 34 cells with a VEN subtype have cell
type PC, INTER or none, one VEN_Short maps to an inhibitory cluster, one file
(obj-1gxrou) is named by two rows and one file of DANDI:001746 by none.
Questions are put to the paper's authors: which miniAnalysis settings detected
the Fig. 5 events and which stretch of each recording was analysed; which rows
of the Patch-seq mapping tables are the 34 inhibitory neurons and which cluster
numbering they follow; and whether Fig. 4d compares peak currents or densities
from each patch's own capacitance, and where the capacitances are.

The author's points on the protocol: the criteria block when the two threshold
readings disagree while step 1.6 allows adopting the best-supported reading,
and the criteria were followed; the claims say "the dataset's labels" though
the dataset has none, so `data: with_labels` and `depends_on` were set on the
eight Fig. 5 claims, and the protocol does not say whether an author may change
those fields; the clock check assumes trial tables these recordings lack, so
the time base was checked with event decay times and the code's per-cell
counts; streaming with remfile was about 100 times slower for DANDI:001746, so
each file was read whole into memory; the first too_large estimates used
remfile's 4.4 MB/s where bulk reads ran at about 300 MB/s, so the protocol
should say to time the read method itself; it is unclear whether code tables
count as the elsewhere data, and data missing from the named deposit cannot be
blocked as data_missing for an elsewhere claim, so `other` was used; the
supplement PDFs are now under `paper/` but the claims file was written without
them, and the criteria that block unless supplied were kept; and a link
criterion that checks per-cell agreement also tests the author's detector, not
only which file is which.

## End of run

20 turns, 3 minutes, $1.45 at API prices, result: success.
