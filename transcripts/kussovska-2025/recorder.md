# kussovska-2025 · recorder · run 42904250429

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py kussovska-2025; ls transcripts/kussovska-2025/; ls summaries | head; wc -c attempts/kussovska-2025-01.yaml claims/kussovska-2025.yaml transcripts/kussovska-2025/*
```

```
docs/pilot-notes/gao-2018-01.md
docs/pilot-notes/mah-2023-01.md
docs/pilot-notes/patel-2026-01.md
docs/pilot-notes/keles-2024-01.md
docs/pilot-notes/mehrotra-2024-01.md
| [000469](https://dandiarchive.org/dandiset/000469) | [Kussovska et al. 2025](https://doi.org/10.1101/2025.10.31.684900) | 29 | 8 | 7 | 0 | [`kussovska-2025`](entries/kussovska-2025) |
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author-revise-3-report.md
author-revise-3.md
author.md
claims-check-report.md
claims-check.md
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
for f in gao-2018-01 mah-2023-01 patel-2026-01 keles-2024-01 mehrotra-2024-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; head -3 docs/pilot-notes/knierim-2000-02.md; grep -n "| Dandiset\|^| ---" README.md | head; cat summaries/gao-2018-01.md summaries/mah-2023-01.md
```

```
<persisted-output>
Output too large (42.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fda61a83-83fa-4df8-b0e7-8fdff3580ce3/tool-results/b0bzv1pc1.txt

Preview (first 2KB):
=== gao-2018-01
# gao-2018, Gao et al. 2018

Ten claims reproduced, six partially, three not reproduced and 26 blocked, all
26 for missing data; two outcomes rest on an assumption,
`fig3e-alm-mean-rate-unchanged` and `cd-captures-selectivity`. The first
verification round agreed with 39 of the 45 outcomes as they then stood and
disagreed on `fig2cd-selectivity-emerges-gradually`, which it held partial where
the record had it blocked for methods underspecified, on
`fig3d-alm-altered-by-cn-inhibition`, `fig3e-alm-increase-decrease` and
`cd-captures-selectivity`, which it held one step lower, and on fig3e-alm-mean-rate
and `fig4-fastigial-activation-alm-latency`, which it held not reproduced; the
author took the first four and kept the last two partial, and the second round
accepted both and agreed with 44 of 45, the exception being that the record
still gave cd-captures-selectivity as reproduced, which the second revision
corrected. Nothing was proposed after the second round, so there was no third.
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/fda61a83-83fa-4df8-b0e7-8fdff3580ce3/tool-results/b0bzv1pc1.txt"
}
```

```
1	=== gao-2018-01
2	# gao-2018, Gao et al. 2018
3	
4	Ten claims reproduced, six partially, three not reproduced and 26 blocked, all
5	26 for missing data; two outcomes rest on an assumption,
6	`fig3e-alm-mean-rate-unchanged` and `cd-captures-selectivity`. The first
7	verification round agreed with 39 of the 45 outcomes as they then stood and
8	disagreed on `fig2cd-selectivity-emerges-gradually`, which it held partial where
9	the record had it blocked for methods underspecified, on
10	`fig3d-alm-altered-by-cn-inhibition`, `fig3e-alm-increase-decrease` and
11	`cd-captures-selectivity`, which it held one step lower, and on fig3e-alm-mean-rate
12	and `fig4-fastigial-activation-alm-latency`, which it held not reproduced; the
13	author took the first four and kept the last two partial, and the second round
14	accepted both and agreed with 44 of 45, the exception being that the record
15	still gave cd-captures-selectivity as reproduced, which the second revision
16	corrected. Nothing was proposed after the second round, so there was no third.
17	The dandiset is pinned at 0.220126.1903, its only published version. The paper,
18	Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li in Nature (563,
19	113-116), trains head-fixed mice to report a pole's location by licking left or
20	right after a delay, and reports that fastigial lesions and photo-activation and
[... 556 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/kussovska-2025; for f in author-report.md author-revise-1-report.md author-revise-2-report.md author-revise-3-report.md claims-check-report.md claims-report.md verifier-1-report.md verifier-2-report.md verifier-3-report.md answer-report.md author-answers-report.md; do echo "=== $f"; cat $f; done; cd ../..; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '000469' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (271.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fda61a83-83fa-4df8-b0e7-8fdff3580ce3/tool-results/bb295g8ix.txt

Preview (first 2KB):
=== author-report.md
I've finished steps 1 to 6 of the Author protocol for kussovska-2025. The entry passes `python tools/entry.py all` in a clean environment (0 errors, notebook ran in 19.6 min), and the handover is built in `executed/kussovska-2025/handover/`. Nothing is committed.

## 1. Outcomes (45 claims: 27 reproduced, 9 partially reproduced, 6 not reproduced, 3 blocked)

| Claim | Outcome |
|---|---|
| units-by-region, behavior-accuracy, fig1c-accuracy-load1-vs-load3, behavior-rt, rt-in-vs-out-memory, rt-correct-vs-incorrect | reproduced |
| fig1e-load-modulated-neurons | reproduced |
| fig1f-rt-modulation-not-significant | not reproduced |
| concept-cells-count, fig2ab, fig2c, ext1bc, fig2d, ext1de | reproduced |
| fig2e-maintenance-decoding-amy-mtl | reproduced |
| ext1f-maintenance-decoding-load2 | partially reproduced |
| fig2f-bin-width-decoding | partially reproduced |
| fig2f-bin-width-pairwise | not reproduced |
| ext1g-bin-width-load2 | reproduced |
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/kussovska-2025; wc -c *-report.md; cat author-report.md
```

```
1082 answer-report.md
 1234 author-answers-report.md
 5549 author-report.md
 4921 author-revise-1-report.md
 3990 author-revise-2-report.md
 2214 author-revise-3-report.md
 2969 claims-check-report.md
 4882 claims-report.md
14187 verifier-1-report.md
 9024 verifier-2-report.md
 4103 verifier-3-report.md
54155 total
I've finished steps 1 to 6 of the Author protocol for kussovska-2025. The entry passes `python tools/entry.py all` in a clean environment (0 errors, notebook ran in 19.6 min), and the handover is built in `executed/kussovska-2025/handover/`. Nothing is committed.

## 1. Outcomes (45 claims: 27 reproduced, 9 partially reproduced, 6 not reproduced, 3 blocked)

| Claim | Outcome |
|---|---|
| units-by-region, behavior-accuracy, fig1c-accuracy-load1-vs-load3, behavior-rt, rt-in-vs-out-memory, rt-correct-vs-incorrect | reproduced |
| fig1e-load-modulated-neurons | reproduced |
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/kussovska-2025; for f in author-revise-1-report.md author-revise-2-report.md author-revise-3-report.md claims-check-report.md claims-report.md answer-report.md author-answers-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-revise-1-report.md
Round 1 is revised. `python tools/entry.py all entries/kussovska-2025` passes with 0 errors: the main notebook ran in 46 min and the new dPCA notebook in 22 min. `check` passes and `handover` is rebuilt. Nothing is committed.

**Outcome changes**
- **The three Fig. 3 claims, blocked → reproduced.** They are now tested in a second notebook, `dpca_kussovska_2025.ipynb`. The earlier "too large" estimate came from fits competing for threads: on one thread each fit is fast, and the 100 splits run on 4 processes.
  - **fig3d:** with the code's trials, H = 457.62 and Dunn p 1.1e-38 and 2.39e-29, against the paper's 457.217, 2.38e-38 and 1.25e-29. The two maintenance conditions do not differ (p 0.077).
  - **fig3abc:** maintenance trajectories are more complex under both measures, but part of the difference is only that maintenance is longer.
  - **fig3h:** reproduced only when the early half is fitted with `protect=[]`. The code's own setting reverses the result, so I recorded it as a finding.
- **fig6cd, partially → not reproduced.** The verifier was right: the criterion's partial outcome needs the full pattern at load 1, and the interneuron encoding-versus-probe test fails under every reading.
- **fig6e, partially → reproduced.** It rests on the cell types: 3 of 15 interneuron concept cells (20.0%, p = 0.038). This run's ACG fit keeps 316 well-fit neurons where round 1 kept 317, with the same code. That one neuron changes the type (a) counts. The other cell-type reading does not reproduce it, which the notes say.
- **fig4d, still reproduced, on a revised assumption.** The verifier's problem 3 is confirmed. With the code's 2.8 s window, burst-free Poisson trains exceed the null, in 17 to 20 of 20 participants. The claim now rests on each trial's own maintenance window. That reading gives the paper's pattern with the Methods' groups and the prominence rule, but not with the code's groups. I added a finding and a question for the authors about 
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B2 "^| \[000469\|^| Dandiset" README.md | head; for f in verifier-1-report.md verifier-2-report.md verifier-3-report.md; do echo "=== $f"; cat transcripts/kussovska-2025/$f; done
```

```
=== verifier-1-report.md
**Verifier report, round 1: Kussovska et al. 2025 on DANDI:000469 (0.231213.2047)**

The claims file has 45 claims; all appear below. I queried the archive: the pinned version is valid, with 41 assets including 21 Sternberg `ses-2` files. It holds every input the three dPCA claims need (spike times and trial tables), and the notebook streamed those in 14 s.

### A. Outcomes

| claim id | outcome | reason |
|---|---|---|
| units-by-region | reproduced | 902 units from 21 patients; AMY 259, HPC 190, dACC 171, preSMA 250, vmPFC 32, all exact (cell 16). |
| behavior-accuracy | reproduced | 88.73% ± 1.25 (s.e.m.), exact (cell 18). |
| fig1c-accuracy-load1-vs-load3 | reproduced | Load 1 median 94.4% against 86.7% at load 3. Rank-sum raw p = 0.009, Bonferroni p = 0.027, which equals the paper (cell 20). |
| behavior-rt | reproduced | (a) 1.120 s (s.d. 0.252); (c) 1.097 s. Both are inside 0.78–1.34 (cell 22). |
| rt-in-vs-out-memory | reproduced | In-memory probes faster; p = 0.001–0.002 under all four readings (cell 24). |
| rt-correct-vs-incorrect | reproduced | Correct trials faster in 20 of 21 participants; p = 0.001 under both readings (cell 26). |
| fig1e-load-modulated-neurons | reproduced | Matched trials, shared permutation: preSMA 20.4%, vmPFC 18.75%, dACC 10.53%. All within tolerance, p = 0.000 / 0.009 / 0.025 (cell 28). |
| fig1f-rt-modulation-not-significant | not_reproduced | With each trial's own RT (the main reading), preSMA, AMY and dACC have BH p < 0.05 under every trial reading (cell 30). The paper's numbers (AMY 5.79%, preSMA 8.00%, vmPFC 6.25%, none significant) come out exactly only under the code's bug, which uses subject 1's RT vector for every neuron. |
| concept-cells-count | reproduced | Code reading gives 57–60 cells over seeds, with AMY 70.7% and HPC 19.0%. The Methods reading gives 49–54. Per participant 4.14 ± 3.66 (cell 32). |
| fig2ab-single-cells-not-persistent | reproduced | 50 of 58 cells are not persistent under 
[... 206 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Reproduced\|^| Dandiset\|^| Data" README.md | head -5; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if any('000469' in str(v) for v in x.values() if not isinstance(v,(dict,list))): print(json.dumps(x,indent=1)); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
```

```
{
 "dandiset": "000469",
 "name": "Dataset of human-single neuron activity during a Sternberg working memory task.",
 "published_version": "0.240123.1806",
 "asset_count": 41,
 "size_gb": 9.79,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Homo sapiens - Human"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.1038/s41597-024-02943-8",
   "title": "Dataset of human-single neuron activity during a Sternberg working memory task",
   "relation": "IsSupplementTo",
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/kussovska-2025-01.yaml",
 "limit": 400
}
```

```
1	schema_version: 3
2	id: kussovska-2025-01
3	datasets:
4	- archive: dandi
5	  id: 000469
6	  version: 0.231213.2047
7	  doi: 10.48324/dandi.000469/0.231213.2047
8	  relation: reuses
9	paper: doi:10.1101/2025.10.31.684900
10	date: '2026-11-10'
11	entry: kussovska-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/kussovska-2025.yaml; grep -n "^  - id:\|^    id:\|^- id:" claims/kussovska-2025.yaml | head -50
```

```
# Claims for Kussovska, Kim & Rungratsameetaweemana (2025), "Neural heterogeneity shapes the
# temporal structure of human working memory", bioRxiv, doi:10.1101/2025.10.31.684900, tested on
# DANDI:000469 (reused; the paper analyses the dataset of Kyzar et al. 2024, ref. 59).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read. paper/10.1101-2025.10.31.684900.txt, the bioRxiv full-text page of the preprint
# posted 1 November 2025 (its header says "version of record"; the page says "New Results" and
# offers a "current version", so a later version may exist; it was not read). It holds the
# abstract, Introduction, Results, legends of Figures 1 to 6, Discussion, Methods, Data and Code
# availability and references. No PDF was supplied. The Extended Data figures (Extended Data
# Figs 1 to 5, behind "Supplementary Material") and their legends are not in the text read; the
# Source Data are not either. The main findings are all stated in the main text and legends, so
# claims were written; claims on Extended Data panels rest on the main-text sentences that cite
# them, and their sources say "(not in the text read)". Several equations of the Methods (the GLM
# link, the local-peak and prominence formulas of Burst detection) were lost in extraction.
#
# Code read. github.com/dariakussovska/heterogeneitywm at commit 5144fe8 (2025-10-26), the last
# commit before the preprint was posted. Later commits (REVISIONS/ and R2_REVISIONS/, 2026) are
# for a revised version and were not used. The repository holds Python scripts named by figure
[... 65 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/kussovska-2025-01.yaml",
 "offset": 400,
 "limit": 400
}
```

```
400	    outcome rests on them.
401	- claim: fig4f-all-cells-epochs
402	  outcome: partially_reproduced
403	  notebook: reproduce_kussovska_2025.ipynb
404	  output: claim:fig4f-all-cells-epochs
405	  assumed: true
406	  notes: 'All 902 neurons, prominence rule: encoding median 6 bursts against 14 to 17 in M1 to M3, BH
407	    p 0.0003 to 0.035 under both window readings; probe 5.5, BH p 0.61 to 0.71, no increase under any
408	    reading. The well-fit population gives the same for M1 and M2. Three of the four comparisons hold.
409	    Under the Methods'' windows M3 lasts 0.67 s on average; per second its median is 16.6 (prominence)
410	    and 43.2 (height) against 17 and 46.5 bursts in M1, so the M3 decreases of the height rule there come
411	    from the shorter window; the outcome is decided on the code''s thirds. The per-trial thirds of maintenance
412	    of the Fig. 6c legend, a reading the claims file does not list (asked in questions/kussovska-2025.yaml),
413	    give the same under the prominence rule: M1 to M3 above encoding (BH p 0.0006 to 0.0007), the probe
414	    not (0.68).'
415	  deviations:
416	  - Cell types and ACG groups downstream use reading (a) of acg-fit-yield (every spike of the unit), assumed
417	    because the code's shipped Cell_metrics.xlsx equals it in firing rate and ISI CV and agrees within
418	    1% in normalised mean ACG and burst index for 99% of neurons; the ACG fit is a scipy port of the MATLAB
419	    fit, so the types (102 PY, 215 IN) differ from the paper's 92 and 202. Each claim on cell types is
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/kussovska-2025-01.yaml",
 "offset": 799,
 "limit": 200
}
```

```
799	- kind: code_mismatch
800	  statement: The column the code reports as CV2 for Fig. 5h (02_trial_info.py:42-46) is the plain coefficient
801	    of variation of the interspike intervals, not Holt's local CV2 that the Methods cite; the paper's
802	    values (PY 1.673, IN 1.319) match the plain CV.
803	- kind: methods_unavailable
804	  statement: 'Question for the authors: which peak rule detects population bursts, a smoothed value above
805	    the 90th percentile (Methods) or a prominence at or above it (Results and code), and what are the
806	    threshold of the surrogates and the minimum spacing (140 ms in the Methods, 70 ms in the Results)?
807	    Fig. 4c is reproduced only under the Methods'' height rule with the Methods'' groups, with a spacing
808	    of 70 ms (1 bin) or 140 ms (2 bins; low ACG BH p 0.0483, and 0.0601 under one rounding-level variant
809	    of the ACG fit), and under the code''s prominence rule concept cells also differ from the null.'
810	- kind: methods_unavailable
811	  statement: 'Question for the authors: what is the ''label-shuffled null'' of Fig. 6a,b, whose legend
812	    names rate-matched Poisson surrogates? Under the Poisson null interneurons exceed the null in encoding,
813	    and under a shuffle of cell-type labels within participant they fall below it.'
814	- kind: methods_unavailable
815	  statement: 'Question for the authors: which decay time constants are compared between preferred and
816	    nonpreferred trials in Extended Data Fig. 5g,h? The code reads them from a shipped table (decay_constant_change.xlsx)
817	    that no script computes; ACG tau_decay per trial type shows no effect here.'
818	- kind: methods_unavailable
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^[a-z_]*:" attempts/kussovska-2025-01.yaml; grep -n -A3 "^  claim: fig6e\|^- claim: fig6e" attempts/kussovska-2025-01.yaml | sed -n '1,4p'
```

```
1:schema_version: 3
2:id: kussovska-2025-01
3:datasets:
9:paper: doi:10.1101/2025.10.31.684900
10:date: '2026-11-10'
11:entry: kussovska-2025
12:provenance:
23:inputs:
34:outcomes:
770:findings:
863:verifications:
599:- claim: fig6e-load-modulation-in
600-  outcome: partially_reproduced
601-  notebook: reproduce_kussovska_2025.ipynb
602-  output: claim:fig6e-load-modulation-in
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
a=yaml.safe_load(open('attempts/kussovska-2025-01.yaml'))
for v in a['verifications']:
    print(v['date'], v.get('reviewed')[:300])
    r=v['results']; print(len(r), 'disagree:', [(x['claim'],x.get('outcome')) for x in r if not x['agrees']])
from collections import Counter
print(Counter(o['outcome'] for o in a['outcomes']))
print([o['claim'] for o in a['outcomes'] if o.get('assumed')].__len__())
E
grep -n "^  - id\|^- id\|questions" questions/kussovska-2025.yaml 2>/dev/null | head; sed -n 40,61p claims/kussovska-2025.yaml
```

```
2026-11-10 Round 1: the executed notebook reproduce_kussovska_2025.ipynb with the conclusion cells and the summary removed, the helper module wm.py and the claims file, with the paper's full text. The verifier queried the archive and tested group_bursts on synthetic Poisson data; it had no attempt record. It c
45 disagree: [('fig3abc-trajectory-complexity', 'blocked'), ('fig3d-encoding-vs-maintenance-separability', 'blocked'), ('fig3h-early-vs-late-maintenance', 'blocked'), ('fig6cd-celltype-epochs', 'not_reproduced')]
2026-11-10 Round 2: the full executed notebooks reproduce_kussovska_2025.ipynb (149 cells) and dpca_kussovska_2025.ipynb (18 cells) with their conclusions and summaries, wm.py, the README and the attempt record after the round-1 revision.
45 disagree: []
2026-11-10 Round 3: the proposed change of outcome of fig6e-load-modulation-in and the analysis behind it in the executed notebook reproduce_kussovska_2025.ipynb (the fit variants of acg-fit-yield and the second fig6e cell).
1 disagree: []
Counter({'reproduced': 30, 'partially_reproduced': 8, 'not_reproduced': 7})
17
3:questions:
#   2-byte placeholder, and the Python scripts read the outputs from the shipped
#   data/cell_analysis/Cell_metrics.xlsx. They can be recomputed from the dataset's spike times
#   with the MATLAB functions (or a port of them); the shipped table is outside data.
# - The concept-cell bootstrap (04_concept_cells.py:76-90) has no random seed.
#
# Data the paper used (as the paper reports it). 21 patients with intractable epilepsy, 41
# recording sessions (age 17 to 71), microwires in hybrid depth electrodes; 902 single units
# sorted with OSort, in amygdala (259), hippocampus (190), dACC (171), preSMA (250) and vmPFC
# (32). Task: a modified Sternberg task. Each trial is fixation (900 to 1000 ms), encoding of 1
# to 3 images (load 1 to 3) from a participant-specific set of five images, maintenance of 2.5
# to 2.8 s ("hold"), and a probe with a yes/no (old/new) button response; r
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
c=yaml.safe_load(open('claims/kussovska-2025.yaml'))
for x in c['claims']:
    print(x['id'], '|', str(x.get('source'))[:120], '|', x.get('statement','')[:230].replace('\n',' '))
E
```

```
units-by-region | Results, Behavior and single-neuron recordings in a working memory task, paragraph 1; Figure 1i; Methods, Electrophysiol | Recordings from the 21 patients yielded 902 well-isolated units, 259 in the amygdala, 171 in the dACC, 190 in the hippocampus, 250 in the preSMA and 32 in the vmPFC.
behavior-accuracy | Results, Behavior and single-neuron recordings in a working memory task, paragraph 2; Extended Data Fig. 1a (not in the  | Task accuracy was 88.73% ± 1.25%.
fig1c-accuracy-load1-vs-load3 | Results, Behavior and single-neuron recordings in a working memory task, paragraph 2; Figure 1c | Accuracy was higher for load 1 than for load 3 trials across patients.
behavior-rt | Results, Behavior and single-neuron recordings in a working memory task, paragraph 2; Figure 1d | Reaction time for correct trials was 1.06 ± 0.28 s.
rt-in-vs-out-memory | Results, Behavior and single-neuron recordings in a working memory task, paragraph 2 | Reaction time was faster for probes held in memory than for probes not in memory.
rt-correct-vs-incorrect | Results, Behavior and single-neuron recordings in a working memory task, paragraph 2 | Correct decisions were faster than incorrect ones.
fig1e-load-modulated-neurons | Results, Behavior and single-neuron recordings in a working memory task, paragraph 3; Figure 1e | During maintenance a significant proportion of neurons in the preSMA (19.6%), vmPFC (18.75%) and dACC (10.53%) was modulated by memory load.
fig1f-rt-modulation-not-significant | Results, Behavior and single-neuron recordings in a working memory task, paragraph 3; Figure 1f | No region had a significant proportion of neurons whose maintenance firing covaried with reaction time after correction, although the amygdala (5.79%), preSMA (8.00%) and vmPFC (6.25%) showed elevated percentages.
concept-cells-count | Results, Concept cell definition and criteria, paragraphs 1 and 2; Figure 1j; Methods, Identification of concept cells | Of 902 neurons, 58 (6.4%) were co
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat questions/kussovska-2025.yaml | head -40; ls entries/kussovska-2025
```

```
dandiset: "000469"
paper: doi:10.1101/2025.10.31.684900
questions:
- claim: fig6cd-celltype-epochs
  asked: 2026-11-10
  question: >-
    The criterion reads M1 to M3 as the Methods' three consecutive 1 s windows from maintenance
    onset or as the code's thirds of the whole concatenated train. The Fig. 6c legend defines them
    as "the first, second, and final thirds of the maintenance epoch", that is, thirds of each
    trial's own maintenance (2.53 to 2.84 s here). Should the criterion list this as a third reading
    of M1 to M3, here and in the claims that use the same windows (fig4f-all-cells-epochs,
    fig4hj-group-epochs, ext2-bursts-loads23, ext5bd-in-load-dependence)?
  passage: >-
    Fig. 6 legend, panel c, "Burst counts across task epochs (encoding; maintenance M1, M2, M3;
    probe) in load 1 trials for pyramidal neurons (PY), where M1, M2, and M3 denote the first,
    second, and final thirds of the maintenance epoch." The Results (Distinct temporal activity
    patterns, paragraph 3) say "Dividing the maintenance period into three consecutive 1 s windows
    (M1-M3) yielded the same pattern", and the Methods (Burst detection) give 1 s windows.
  why: >-
    The three readings count different bursts in M3: the Methods' third window runs from 2 s to
[... 27 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/kussovska-2025-01.md",
 "content": "# kussovska-2025, Kussovska et al. 2025\n\nTwenty-nine claims reproduced on the dandiset, eight partially, seven not\nreproduced and none blocked; `supp4-rodent-validation`, tested on the feature\ntable shipped with the paper's code (`data: elsewhere`), reproduced and is\ncounted apart. Seventeen outcomes rest on an assumption, most of them on the\ncell types of reading (a) of `acg-fit-yield` (every spike of the unit), among\nthem `fig4c-encoding-bursts-vs-poisson`, `fig4d-maintenance-bursts-vs-poisson`\nand `fig6e-load-modulation-in`. The first verification round agreed with 41 of\nthe 45 outcomes and disagreed on the three dPCA claims, which the author had\nblocked as too large and which it held testable, the block resting on run time\nonly, and on `fig6cd-celltype-epochs`, which it held not reproduced where the\nrecord had it partial; the author took all four. The second round agreed with\nall 45, calling fig4c and fig6e fragile, and the author proposed fig6e as\npartially reproduced, so there was a third round, which reviewed that one claim\nand agreed. The dandiset is pinned at 0.231213.2047, the version the paper\ncites; all published versions hold the same 41 assets, while the code's README\ndownloads 0.240123.1806. The paper, Kussovska, Kim and Rungratsameetaweemana,\n\"Neural heterogeneity shapes the temporal structure of human working memory\"\n(bioRxiv, doi:10.1101/2025.10.31.684900), reanalyses the 902 units recorded in\n21 epilepsy patients during a Sternberg task and reports that the persistence of\nconcept cells emerges only with population pooling and coarse temporal bins,\nthat encoding and maintenance occupy distinct dPCA subspaces, that population\nbursting reorganizes between encoding and maintenance, and that autocorrelogram\n(ACG) features split the neurons into putative pyramidal neurons (PY) and\ninterneurons (IN), whose concept cells differ in load and reaction time\nmodulation, spiking regularity and decoding during maintenance. The claims were\nwritten from the bioRxiv full-text page, without a PDF and without the Extended\nData figures, on which 9 claims rest only through the main-text sentences that\ncite them, and from the paper's code at commit 5144fe8, in which the matched\ntrial sets exist only as shipped tables and the ACG fit is MATLAB with an empty\nspike input; the claims check made six corrections, for 45 claims, all of which\ncould be tested. Reproduced are the unit counts (AMY 259, dACC 171, HPC 190,\npreSMA 250, vmPFC 32, exact), the behaviour claims (88.73%; load 1 against load\n3, p = 0.0270 with the code's Bonferroni factor, the paper's P = 0.027),\n`fig1e-load-modulated-neurons`, `concept-cells-count` (58 at seed 0, 57 to 60\nover ten seeds), the persistence and cross-temporal claims of Fig. 2, the three\ndPCA claims (`fig3d-encoding-vs-maintenance-separability`, H = 457.62, only with\nthe trials as the code selects them, and `fig3h-early-vs-late-maintenance` only\nwith protect [] for the early half), fig4c, fig4d over each trial's own\nmaintenance, `ext2-bursts-loads23`, acg-fit-yield (317 against 294),\n`fig5c-cell-type-clusters` under reading (b) (100 PY, 198 IN),\n`fig5gh-burst-index-cv2`, `fig5kl-concept-cell-types` (11 and 14),\n`ext5bd-in-load-dependence`, `fig6kl-cross-temporal-by-type` and\n`ext5ij-load2-decoding-by-type`. Partial are `ext1f-maintenance-decoding-load2`\n(AMY 26.43%, above the tolerance of 21.2 to 25.9%), `fig2f-bin-width-decoding`,\n`fig4-acg-group-differences`, `fig4f-all-cells-epochs` (no increase to the\nprobe, BH p 0.61 to 0.71), `fig4hj-group-epochs`,\n`fig6ab-celltype-bursts-vs-null`, `fig6j-in-bin-width-decoding` and fig6e, where\nIN concept cells come out at 3 of 16 = 18.75% (p = 0.042), just below the\ntolerance of 19.28 to 23.56%, and meet it under two of four fits that differ at\nrounding level. Not reproduced are `fig1f-rt-modulation-not-significant`, whose\nvalues come out exactly only with the code's predictor, `fig2f-bin-width-pairwise`,\nfig6cd (no IN probe difference, BH p 0.13 to 1.0), `fig6f-rt-modulation-in-concept`\n(IN concept 12.50%, p 0.19 to 0.20), `fig6gh-in-concept-cv2` (p = 0.86 at load\n1), `ext5gh-py-decay-preferred` and `fig6i-py-bin-width-decoding`. The author's\nfirst run had 27 reproduced, 9 partially, 6 not reproduced and 3 blocked. The\nauthor asked no questions of a reader, so the answer and author-answers runs\nchanged nothing; a question on the per-trial thirds of maintenance of the Fig. 6c\nlegend went to `questions/kussovska-2025.yaml` after round 2. Round 1 held that\nthe dPCA block rested on fits competing for threads, that the downstream claims\nused only the types of reading (a), whose PY count (102) is outside tolerance,\nthat the code's 2.8 s maintenance window lets the surrogates fill the silent tail\nafter the probe, that the scipy ACG fit is not stated as a limitation, and that\ndecoding p values are never compared with the paper's 20% chance; in reply the\ndPCA claims ran in a second notebook on 4 processes, every cell-type claim also\nran with the types of reading (b), fig4d moved to each trial's own maintenance\nafter a burst-free Poisson control, and binomial tests against 20% were added.\nRound 2 found that results changed between runs with fixed seeds (317 to 316\nwell-fit neurons, preSMA 51 to 50), stale numbers in the text, that fig4c rested\non the 1-bin variant, and that the tau decay groups were never compared with the\nshipped `Decay` column; in reply the changes were traced to ties at the GLM\nthreshold and a fit sensitive at the level of rounding, and groups from the\nshipped tau decay gave fig4-acg-group-differences its whole pattern, the outcome\nkept as that table is an outside input. Round 3 found that the fig6e text and\nthat of most fit-dependent claims described another run, and they were\ncorrected. The author's run took about 2 h 55 min; the notebook ran in 19.6 min\nat first, 2297 s after the author-answers run, 46 min (with 22 min for the dPCA\nnotebook) after round 1 and 52 and 23 min after round 2. The first full\ndevelopment run was killed at 66 min with nothing saved, because of a slow\ntwo-sided binomial test, and a fast SVM wrapper gave wrong predictions when\nlabels were not coded 0 to k-1, which was fixed before the final run.\n\nThe dandiset holds exactly the paper's 902 units with its region counts, and the\ncode's trial tables link to its trials exactly, but the matched trial sets of\nthe Methods (96 load-matched and 75 identity-matched trials per participant)\nexist only as the code's data/new_trial_info.xlsx and data/new_trial_final.xlsx,\nno script builds them and the paper does not say how they were chosen, so the\npseudo-population decoding depends on which trials enter (random draws of six\ntrials per image give 56.7 to 86.7% at 1000 ms against 76.67% with the code's\ntable). The paper's GLM code uses subject 1's reaction times as the predictor\nfor every neuron of every participant, and the Fig. 1f percentages (AMY 5.79%,\npreSMA 8.00%, vmPFC 6.25%) come out exactly only with it; with each trial's own\nreaction time preSMA, AMY and dACC have significant proportions after\ncorrection. The code's maintenance burst test concatenates trials with a 2.8 s\nstride while maintenance lasts 2.53 to 2.84 s, and homogeneous Poisson trains\nconfined to each trial's maintenance then exceed the null for all neurons in 17\nto 20 of 20 participants (BH p 0.0005 to 0.0025), so the maintenance results of\nFig. 4d and Fig. 6a,b against the Poisson null can arise from the window alone.\n08_dpca_matrices.py takes encoding trials by new_trial_id and maintenance trials\nby trial_id, which in 4 of the 14 sessions with concept cells (subjects 7, 8, 9\nand 16) are other trials, and the paper's Fig. 3d statistics are matched most\nclosely with the code as written; the code's protect setting for the early half\nof maintenance reverses Fig. 3g,h in all 100 splits. The code assigns M1 to M3\nby thirds of the concatenated train, that is of the trials, where the Methods\ngive three 1 s windows, and what it reports as CV2 for Fig. 5h is the plain\ncoefficient of variation (PY 1.673, IN 1.319 match it). The ACG features of the\nshipped Cell_metrics.xlsx are recomputed from the spike times to within 1% for\n99% of units, but the fitted R2 and time constants differ for part of the units\nin a scipy port, which gives 317 well-fit units in place of 294, and changing\nthe fit's start point by 1 +/- 1e-9 or the ACG by 1 + 1e-12 gives 315 to 317;\nin the GLM test 8 of the 902 neurons have |b1| equal to their null threshold, so\nrounding moves preSMA between 47 and 51 significant neurons and vmPFC between 6\nand 7. The paper states that sixteen participants completed 135 trials and five\n108, while the dandiset has fifteen sessions of 135 and six of 108 (subjects 6,\n7, 8, 9, 16 and 19). In sub-9's file one trial (row 29) has a maintenance of 0\ns, against 2.53 to 2.84 s in every other trial. The first encoding image lasts\n1.0, 1.2, 1.5 or 2.5 s depending on the session, which the paper does not state,\nand fixation lasts about 0.91 to 1.2 s in most sessions, with single longer\nfixations up to 14.07 s, where the paper gives 0.9 to 1.0 s. The clock could not\nbe checked by contrast in 7 sessions (subjects 1, 3, 6, 10, 17, 19, 20), which\nhave no image-selective neurons. Questions are put to the paper's authors: which\npeak rule detects population bursts, with what surrogate threshold and minimum\nspacing (140 ms in the Methods, 70 ms in the Results); what the label-shuffled\nnull of Fig. 6a,b is; which decay time constants Extended Data Fig. 5g,h\ncompares; how the temporal extent of a cross-temporal cluster is measured and\nwhether the binomial test is one- or two-sided; and over which window the\nPoisson surrogates of the maintenance burst test are drawn.\n\nThe author's points on the protocol: it does not say how to judge a result that\nholds in part when a criterion defines only \"reproduced\"; it does not say what\nto record for `measured` when the first listed reading matches for only 2 of 10\nseeds, as in concept-cells-count; it does not say whether downstream claims must\nrun every reading of an upstream claim, such as which spikes feed the ACG; it\nhas no category for outside inputs used only for comparison, such as the code's\nconcept-cell list and ACG table; its example entry uses bold labels that its\ninstructions forbid; and its advice to develop on a subset does not say to run\nthe full notebook cell by cell with saved progress, which cost a run.\n"
}
```

```
File created successfully at: docs/pilot-notes/kussovska-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/kussovska-2025-01.md",
 "old_string": "Round 1 held that\nthe dPCA block rested on fits competing for threads, that",
 "new_string": "Round 1 held that\nthe dPCA block rested on run time only and the splits could run in parallel, that"
}
```

```
The file docs/pilot-notes/kussovska-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/kussovska-2025-01.md",
 "old_string": "in reply the\ndPCA claims ran in a second notebook on 4 processes,",
 "new_string": "in reply the\nestimate was found to come from fits competing for threads and the dPCA claims\nran in a second notebook on 4 processes,"
}
```

```
The file docs/pilot-notes/kussovska-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the summary.

**Agent calls Bash**

```bash
cd  cat > summaries/kussovska-2025-01.md <<'E'
In this data the paper's findings on concept cells largely held up: persistent maintenance activity appears only with population pooling and coarse bins, encoding and maintenance occupy separable subspaces, and autocorrelogram features split neurons into putative pyramidal cells and interneurons. The subspace results matched only with the code's own trial selection and fit settings. The bursting findings held in part, as no single burst-detection rule, which the paper leaves open, supports them all. Of the cell-type differences, interneuron concept cells decoded the image at every bin width, but their reaction-time modulation and maintenance irregularity did not reproduce. That no region tracks reaction time held only with the code's predictor, which gives every neuron one participant's reaction times.
E
wc -w summaries/kussovska-2025-01.md; grep -c "—\|rather\|\*\*" summaries/kussovska-2025-01.md docs/pilot-notes/kussovska-2025-01.md; git status --short
```

```
117 summaries/kussovska-2025-01.md
summaries/kussovska-2025-01.md:0
docs/pilot-notes/kussovska-2025-01.md:0
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
?? docs/pilot-notes/kussovska-2025-01.md
?? scripts
?? summaries/kussovska-2025-01.md
```

**Agent**

I wrote both files, and changed nothing else. The outcome counts match what `tools/readme_row.py kussovska-2025` prints: 29 reproduced, 8 partially, 7 not reproduced and 0 blocked. The one claim tested on data outside the dandiset reproduced and is counted separately. There were three verification rounds. The first disagreed on four claims, the second agreed with all 45, and the third checked a single proposed change and agreed. The record says nothing was blocked, so the summary has no "could not be tested" part.

There are untracked dotfiles and a `scripts` directory in the repository root (`.bashrc`, `.vscode`, `.mcp.json` and others). The revision reports say they appeared during the attempt; I didn't create them. When the workflow commits, it should leave them out.

### docs/pilot-notes/kussovska-2025-01.md

# kussovska-2025, Kussovska et al. 2025

Twenty-nine claims reproduced on the dandiset, eight partially, seven not reproduced and none blocked; `supp4-rodent-validation`, tested on the feature table shipped with the paper's code (`data: elsewhere`), reproduced and is counted apart. Seventeen outcomes rest on an assumption, most of them on the cell types of reading (a) of `acg-fit-yield` (every spike of the unit), among them `fig4c-encoding-bursts-vs-poisson`, `fig4d-maintenance-bursts-vs-poisson` and `fig6e-load-modulation-in`. The first verification round agreed with 41 of the 45 outcomes and disagreed on the three dPCA claims, which the author had blocked as too large and which it held testable, the block resting on run time only, and on `fig6cd-celltype-epochs`, which it held not reproduced where the record had it partial; the author took all four. The second round agreed with all 45, calling fig4c and fig6e fragile, and the author proposed fig6e as partially reproduced, so there was a third round, which reviewed that one claim and agreed. The dandiset is pinned at 0.231213.2047, the version the paper cites; all published versions hold the same 41 assets, while the code's README downloads 0.240123.1806. The paper, Kussovska, Kim and Rungratsameetaweemana, "Neural heterogeneity shapes the temporal structure of human working memory" (bioRxiv, doi:10.1101/2025.10.31.684900), reanalyses the 902 units recorded in 21 epilepsy patients during a Sternberg task and reports that the persistence of concept cells emerges only with population pooling and coarse temporal bins, that encoding and maintenance occupy distinct dPCA subspaces, that population bursting reorganizes between encoding and maintenance, and that autocorrelogram (ACG) features split the neurons into putative pyramidal neurons (PY) and interneurons (IN), whose concept cells differ in load and reaction time modulation, spiking regularity and decoding during maintenance. The claims were written from the bioRxiv full-text page, without a PDF and without the Extended Data figures, on which 9 claims rest only through the main-text sentences that cite them, and from the paper's code at commit 5144fe8, in which the matched trial sets exist only as shipped tables and the ACG fit is MATLAB with an empty spike input; the claims check made six corrections, for 45 claims, all of which could be tested. Reproduced are the unit counts (AMY 259, dACC 171, HPC 190, preSMA 250, vmPFC 32, exact), the behaviour claims (88.73%; load 1 against load 3, p = 0.0270 with the code's Bonferroni factor, the paper's P = 0.027), `fig1e-load-modulated-neurons`, `concept-cells-count` (58 at seed 0, 57 to 60 over ten seeds), the persistence and cross-temporal claims of Fig. 2, the three dPCA claims (`fig3d-encoding-vs-maintenance-separability`, H = 457.62, only with the trials as the code selects them, and `fig3h-early-vs-late-maintenance` only with protect [] for the early half), fig4c, fig4d over each trial's own maintenance, `ext2-bursts-loads23`, acg-fit-yield (317 against 294), `fig5c-cell-type-clusters` under reading (b) (100 PY, 198 IN), `fig5gh-burst-index-cv2`, `fig5kl-concept-cell-types` (11 and 14), `ext5bd-in-load-dependence`, `fig6kl-cross-temporal-by-type` and `ext5ij-load2-decoding-by-type`. Partial are `ext1f-maintenance-decoding-load2` (AMY 26.43%, above the tolerance of 21.2 to 25.9%), `fig2f-bin-width-decoding`, `fig4-acg-group-differences`, `fig4f-all-cells-epochs` (no increase to the probe, BH p 0.61 to 0.71), `fig4hj-group-epochs`, `fig6ab-celltype-bursts-vs-null`, `fig6j-in-bin-width-decoding` and fig6e, where IN concept cells come out at 3 of 16 = 18.75% (p = 0.042), just below the tolerance of 19.28 to 23.56%, and meet it under two of four fits that differ at rounding level. Not reproduced are `fig1f-rt-modulation-not-significant`, whose values come out exactly only with the code's predictor, `fig2f-bin-width-pairwise`, fig6cd (no IN probe difference, BH p 0.13 to 1.0), `fig6f-rt-modulation-in-concept` (IN concept 12.50%, p 0.19 to 0.20), `fig6gh-in-concept-cv2` (p = 0.86 at load 1), `ext5gh-py-decay-preferred` and `fig6i-py-bin-width-decoding`. The author's first run had 27 reproduced, 9 partially, 6 not reproduced and 3 blocked. The author asked no questions of a reader, so the answer and author-answers runs changed nothing; a question on the per-trial thirds of maintenance of the Fig. 6c legend went to `questions/kussovska-2025.yaml` after round 2. Round 1 held that the dPCA block rested on run time only and the splits could run in parallel, that the downstream claims used only the types of reading (a), whose PY count (102) is outside tolerance, that the code's 2.8 s maintenance window lets the surrogates fill the silent tail after the probe, that the scipy ACG fit is not stated as a limitation, and that decoding p values are never compared with the paper's 20% chance; in reply the estimate was found to come from fits competing for threads and the dPCA claims ran in a second notebook on 4 processes, every cell-type claim also ran with the types of reading (b), fig4d moved to each trial's own maintenance after a burst-free Poisson control, and binomial tests against 20% were added. Round 2 found that results changed between runs with fixed seeds (317 to 316 well-fit neurons, preSMA 51 to 50), stale numbers in the text, that fig4c rested on the 1-bin variant, and that the tau decay groups were never compared with the shipped `Decay` column; in reply the changes were traced to ties at the GLM threshold and a fit sensitive at the level of rounding, and groups from the shipped tau decay gave fig4-acg-group-differences its whole pattern, the outcome kept as that table is an outside input. Round 3 found that the fig6e text and that of most fit-dependent claims described another run, and they were corrected. The author's run took about 2 h 55 min; the notebook ran in 19.6 min at first, 2297 s after the author-answers run, 46 min (with 22 min for the dPCA notebook) after round 1 and 52 and 23 min after round 2. The first full development run was killed at 66 min with nothing saved, because of a slow two-sided binomial test, and a fast SVM wrapper gave wrong predictions when labels were not coded 0 to k-1, which was fixed before the final run.

The dandiset holds exactly the paper's 902 units with its region counts, and the code's trial tables link to its trials exactly, but the matched trial sets of the Methods (96 load-matched and 75 identity-matched trials per participant) exist only as the code's data/new_trial_info.xlsx and data/new_trial_final.xlsx, no script builds them and the paper does not say how they were chosen, so the pseudo-population decoding depends on which trials enter (random draws of six trials per image give 56.7 to 86.7% at 1000 ms against 76.67% with the code's table). The paper's GLM code uses subject 1's reaction times as the predictor for every neuron of every participant, and the Fig. 1f percentages (AMY 5.79%, preSMA 8.00%, vmPFC 6.25%) come out exactly only with it; with each trial's own reaction time preSMA, AMY and dACC have significant proportions after correction. The code's maintenance burst test concatenates trials with a 2.8 s stride while maintenance lasts 2.53 to 2.84 s, and homogeneous Poisson trains confined to each trial's maintenance then exceed the null for all neurons in 17 to 20 of 20 participants (BH p 0.0005 to 0.0025), so the maintenance results of Fig. 4d and Fig. 6a,b against the Poisson null can arise from the window alone. 08_dpca_matrices.py takes encoding trials by new_trial_id and maintenance trials by trial_id, which in 4 of the 14 sessions with concept cells (subjects 7, 8, 9 and 16) are other trials, and the paper's Fig. 3d statistics are matched most closely with the code as written; the code's protect setting for the early half of maintenance reverses Fig. 3g,h in all 100 splits. The code assigns M1 to M3 by thirds of the concatenated train, that is of the trials, where the Methods give three 1 s windows, and what it reports as CV2 for Fig. 5h is the plain coefficient of variation (PY 1.673, IN 1.319 match it). The ACG features of the shipped Cell_metrics.xlsx are recomputed from the spike times to within 1% for 99% of units, but the fitted R2 and time constants differ for part of the units in a scipy port, which gives 317 well-fit units in place of 294, and changing the fit's start point by 1 +/- 1e-9 or the ACG by 1 + 1e-12 gives 315 to 317; in the GLM test 8 of the 902 neurons have |b1| equal to their null threshold, so rounding moves preSMA between 47 and 51 significant neurons and vmPFC between 6 and 7. The paper states that sixteen participants completed 135 trials and five 108, while the dandiset has fifteen sessions of 135 and six of 108 (subjects 6, 7, 8, 9, 16 and 19). In sub-9's file one trial (row 29) has a maintenance of 0 s, against 2.53 to 2.84 s in every other trial. The first encoding image lasts 1.0, 1.2, 1.5 or 2.5 s depending on the session, which the paper does not state, and fixation lasts about 0.91 to 1.2 s in most sessions, with single longer fixations up to 14.07 s, where the paper gives 0.9 to 1.0 s. The clock could not be checked by contrast in 7 sessions (subjects 1, 3, 6, 10, 17, 19, 20), which have no image-selective neurons. Questions are put to the paper's authors: which peak rule detects population bursts, with what surrogate threshold and minimum spacing (140 ms in the Methods, 70 ms in the Results); what the label-shuffled null of Fig. 6a,b is; which decay time constants Extended Data Fig. 5g,h compares; how the temporal extent of a cross-temporal cluster is measured and whether the binomial test is one- or two-sided; and over which window the Poisson surrogates of the maintenance burst test are drawn.

The author's points on the protocol: it does not say how to judge a result that holds in part when a criterion defines only "reproduced"; it does not say what to record for `measured` when the first listed reading matches for only 2 of 10 seeds, as in concept-cells-count; it does not say whether downstream claims must run every reading of an upstream claim, such as which spikes feed the ACG; it has no category for outside inputs used only for comparison, such as the code's concept-cell list and ACG table; its example entry uses bold labels that its instructions forbid; and its advice to develop on a subset does not say to run the full notebook cell by cell with saved progress, which cost a run.

### summaries/kussovska-2025-01.md

In this data the paper's findings on concept cells largely held up: persistent maintenance activity appears only with population pooling and coarse bins, encoding and maintenance occupy separable subspaces, and autocorrelogram features split neurons into putative pyramidal cells and interneurons. The subspace results matched only with the code's own trial selection and fit settings. The bursting findings held in part, as no single burst-detection rule, which the paper leaves open, supports them all. Of the cell-type differences, interneuron concept cells decoded the image at every bin width, but their reaction-time modulation and maintenance irregularity did not reproduce. That no region tracks reaction time held only with the code's predictor, which gives every neuron one participant's reaction times.

## End of run

21 turns, 3 minutes, $1.39 at API prices, result: success.
