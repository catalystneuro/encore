# yang-2026 · recorder · run 44928132864

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/yang-2026/; python tools/readme_row.py yang-2026; ls summaries | head
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/asari-2009-02.md
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
| [000363](https://dandiarchive.org/dandiset/000363) | [Yang et al. 2026](https://doi.org/10.21203/rs.3.rs-11447300/v1) | 16 | 9 | 0 | 0 | [`yang-2026`](entries/yang-2026) |
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/pilot-notes/amjad-2025-01.md docs/pilot-notes/andrews-2024-01.md docs/pilot-notes/armstrong-2026-01.md docs/pilot-notes/asari-2009-01.md docs/pilot-notes/asari-2009-02.md; grep -n "^| Dandiset\|^| Data" README.md | head; cat summaries/amjad-2025-01.md summaries/asari-2009-02.md
```

```
<persisted-output>
Output too large (35.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b976a49c-6648-4de8-a727-415e391681ca/tool-results/bcug2omrc.txt

Preview (first 2KB):
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
thousands; the bipolar LFP is stored in volts with a conversion factor that
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/yang-2026-01.yaml claims/yang-2026.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
x=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for e in (x if isinstance(x,list) else x.values()):
  if '000363' in json.dumps(e): print(json.dumps(e,indent=1))
"
```

```
<persisted-output>
Output too large (106.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b976a49c-6648-4de8-a727-415e391681ca/tool-results/bpu4jdq54.txt

Preview (first 2KB):
schema_version: 3
id: yang-2026-01
datasets:
- archive: dandi
  id: '000363'
  version: 0.231012.2129
  doi: 10.48324/dandi.000363/0.231012.2129
  relation: reuses
paper: doi:10.21203/rs.3.rs-11447300/v1
date: '2026-11-21'
entry: yang-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 46 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b976a49c-6648-4de8-a727-415e391681ca/tool-results/bcug2omrc.txt"
}
```

```
1	# 002013, Amjad et al. 2025
2	
3	Seven claims reproduced, one partially and five blocked on the dandiset,
4	plus one claim linking the dandiset to the paper's Zenodo deposit,
5	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
6	agreed with every outcome. The paper describes microinvasive probes for
7	recording dopamine and electrical activity in monkeys; the beta burst,
8	reward and unit isolation claims reproduce, the dopamine reward effect
9	weakly (p = 0.023, and not in the stored trial-aligned `da`).
10	
11	The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
12	the same conversion as 002014), and many findings are the same: each event
13	is stored about five times, once per overlapping trial window; trial
14	conditions are not in the trials table; the FSCV table columns carry no
15	units and the raw FSCV current is labelled amperes with values in the
16	thousands; the bipolar LFP is stored in volts with a conversion factor that
17	makes it picovolts; and the raw ephys of one session and the spike times of
18	Monkey P are on different clocks from the rest of the file, by 9831.35 s and
19	6800.666 s, with nothing saying so. In addition, one session's trial-aligned
20	FSCV covers only the first half of its trials, the second recording site of
[... 476 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b976a49c-6648-4de8-a727-415e391681ca/tool-results/bpu4jdq54.txt"
}
```

```
1	schema_version: 3
2	id: yang-2026-01
3	datasets:
4	- archive: dandi
5	  id: '000363'
6	  version: 0.231012.2129
7	  doi: 10.48324/dandi.000363/0.231012.2129
8	  relation: reuses
9	paper: doi:10.21203/rs.3.rs-11447300/v1
10	date: '2026-11-21'
11	entry: yang-2026
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 881 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b976a49c-6648-4de8-a727-415e391681ca/tool-results/bpu4jdq54.txt",
 "offset": 902,
 "limit": 250
}
```

```
902	    outcome: partially_reproduced
903	    reason: Cell 83 and the attempt record list medulla and thalamus as outside 0.036-0.088 in the delay
904	      bins. Cell 82 also lists ALM at 0.035 in the overlapping bins.
905	    response: Cell 83 and the notes now also name ALM (0.035, 50 ms steps). Outcome unchanged.
906	  - claim: fig2-1-energy-outside-subspace
907	    agrees: true
908	    outcome: partially_reproduced
909	    reason: I agree; the new runs change none of the outcomes.
910	    response: No change.
911	  - claim: fig3a-matched-pairs
912	    agrees: true
913	    outcome: reproduced
914	    reason: I agree; seed 17 gives the same outcome as the claim's seed.
915	    response: No change.
916	  - claim: table1-prelick-residual
917	    agrees: true
918	    outcome: reproduced
919	    reason: I agree; seed 17 gives the same outcome as the claim's seed.
920	    response: No change.
921	  - claim: fig3e-residual-ratio
[... 230 more lines not kept]
```

**Agent**

Read the attempt record; now the claim statements, the dandiset entry and the reports.

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-encore/b976a49c-6648-4de8-a727-415e391681ca/tool-results/bpu4jdq54.txt; tail -n 30 $F; grep -n "^- id:\|^  source:" claims/yang-2026.yaml
```

```
- quantity: fraction of early matched difference on the first control principal component
    value: 0.04
    tolerance: 0.004
  criterion: In the example session (fig1b-example-session), the plane spanned by the choice
    axis and the early laser-minus-control direction orthogonal to the choice and action axes
    (Methods, Example session), held fixed. Early matched difference, mean of the matched
    laser trials minus mean of their matched controls (M9) in the early window. Fraction, its
    energy in the plane over its total energy (as M6). Principal component, first PC of
    control-trial activity in the early window after projecting out the choice axis; open,
    which control trials and window; readings (a) all control trials in the early window, (b)
    the matched control trials in the early window. Open, whether the plane's off-subspace
    direction comes from the unmatched (M5) or matched early difference; both are run.
    Reproduced when, under one combination, both fractions are within tolerance and the
    matched laser-control separation in the plane is smaller at Go than in the early window;
    partially reproduced when the separation holds and a fraction is outside tolerance.
checks:
- date: 2026-11-21
  kind: agent
  model: claude-opus-5-5
  ready: true
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 -A25 '"000363"' targets/dandisets.json | head -60; grep -n -A3 "^  statement:" claims/yang-2026.yaml | grep -v "^--$" | head -150
```

```
134:  statement: Of the 168 sessions with photoinhibition, the late-delay bilateral sessions give
135-    ALM estimates from 19 mice and 93 sessions, with 13 mice and 48 sessions for striatum, 10
136-    and 31 for thalamus, 16 and 71 for midbrain and 8 and 35 for medulla.
137-  source: Methods, Dataset, paragraph 2, and Units and regions; Table 1, column Mice / sessions
180:  statement: In the 20 to 120 ms after bilateral laser onset only 5 to 8% of the laser-control
181-    population difference lies in the joint choice-action subspace, from 0.052 in ALM (the
182-    lowest) to 0.080 in thalamus (the highest).
183-  source: Results, The early population difference lies mostly outside the choice and action
213:  statement: The choice axis alone holds 0.030 to 0.059 of the early difference and the action
214-    axis 0.021 to 0.032, by region as in Table 1.
215-  source: Results, The early population difference lies mostly outside the choice and action
216-    axes, paragraph 2; Table 1, Choice fraction and Action fraction; Figure 1C
256:  statement: The choice and action axes are not orthogonal; their cosine ranges from 0.29 in
257-    thalamus to 0.52 in ALM.
258-  source: Results, The early population difference lies mostly outside the choice and action
259-    axes, paragraph 3; Figure 1-1A
278:  statement: The early laser difference is larger than the difference between size-matched
279-    splits of control trials in every mouse, with a median ratio across mice of 152 in ALM and
280-    3.3 to 8.7 in the other regions.
281-  source: Results, The early population difference lies mostly outside the choice and action
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -m3 '000363' targets/dandisets.json; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else d[0].keys())
E
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
```

**Agent calls Bash**

```bash
python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
t=d['targets']; print(type(t), len(t))
items = t if isinstance(t,list) else list(t.values())
print(json.dumps(items[0],indent=1)[:800])
for e in items:
  if '363' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))
E
```

```
<class 'list'> 298
{
 "dandiset": "000003",
 "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
 "published_version": "0.260218.2052",
 "asset_count": 101,
 "size_gb": 1922.23,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Mus musculus - House mouse"
 ],
 "approaches": [
  "electrophysiological approach",
  "behavioral approach"
 ],
 "papers": [
  {
   "doi": "10.1016/j.neuron.2016.12.011",
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
grep -c . targets/dandisets.json; grep -rn "000363" targets/ | head; ls targets
```

```
8429
targets/reuse_datasets.json:62:   "dandiset": "000363",
targets/contributors.yaml:4198:  dandi:000363:
targets/reuse.yaml:117:  dataset: dandi:000363
targets/reuse.yaml:119:  evidence: The data used for this study are publicly available via the DANDI archive at https://doi.org/10.48324/dandi.000363/0.230822.0128
targets/reuse.yaml:201:  dataset: dandi:000363
targets/reuse.yaml:203:  evidence: We reanalyzed the Mesoscale Activity Map dataset (DANDI 000363, version 0.231012.2129).
targets/reuse.yaml:341:  dataset: dandi:000363
targets/reuse.yaml:343:  evidence: 'We used publicly available data (MAP: https://dandiarchive.org/dandiset/000363 ) consisting of Neuropixels
contributors.yaml
crcns.json
dandisets.json
description_papers.yaml
dryad.json
ebrains.json
figshare.json
openneuro.json
pilot.yaml
reuse.yaml
reuse_datasets.json
[... 1 more lines not kept]
```

**Agent**

The dandiset 000363 has no entry in `targets/dandisets.json`, so the record doesn't say whether CatalystNeuro converted it. Reading the reports next.

**Agent calls Bash**

```bash
cd transcripts/yang-2026; wc -w *-report.md; cat author-report.md
```

```
981 author-report.md
  606 author-revise-1-report.md
  514 author-revise-2-report.md
  419 claims-check-report.md
  660 claims-report.md
 1620 verifier-1-report.md
 1074 verifier-2-report.md
 5874 total
## Report: yang-2026, attempt 01 (author run)

All 25 claims were tested and none is blocked. 15 are reproduced (one of them rests on an assumption, one is seed-sensitive) and 10 are partially reproduced. The notebook passes `tools/entry.py all` in a clean environment, taking about 29 minutes with a peak memory of 9 GB. The handover is built in `executed/yang-2026/handover/`. Nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| session-counts | reproduced (all eleven counts equal the paper's) |
| table1-early-joint-fraction | reproduced |
| table1-early-axis-fractions | reproduced (10/10 within tolerance) |
| axes-cosine | reproduced |
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/yang-2026; cat author-revise-1-report.md author-revise-2-report.md claims-check-report.md claims-report.md
```

```
No outcome changed in this round. The verifier agreed with all 25 outcomes (15 reproduced, 10 partially reproduced), and the new analyses it asked for confirm them. The final run passed (`python tools/entry.py all entries/yang-2026`: 0 errors, 41 minutes), and every conclusion matches its numbers. Nothing is committed.

**What changed in the outcomes**
- **fig2d-choice-share-flat** stays partially reproduced, but is now marked as resting on an assumption. I read the criterion's partial clause with the same SEM rule as its reproduced clause, and recorded that as a deviation. Counting any rise of the mean, only three regions don't rise and the outcome would be not reproduced. I added this as a question for a reader in `questions/yang-2026.yaml`.
- **fig3-1c-alm-early-residual** stays reproduced, resting on the two-50 ms-bin reading. The claims file reads the window as one 20 to 120 ms window and doesn't list the binning as open. I asked a reader about this in the same questions file and left the claim unchanged.

**What I added or corrected, by report point**
1. **Laser-only decoding (M8 reading a):** now run on the 26 entries that qualify, under all six seeds.
   - table1-decoding-early-vs-prelick: 0 of 10 values within tolerance under the claim's seed (1 to 4 under the others), so it stays partial.
   - fig2a fails every part on this reading and stays reproduced on reading (b), which the criterion allows.
   - The fig2d and fig2e session sets match less well with laser trials alone.
   - I corrected the false markdown sentence ("no entry passes the rule").
2. **Seed 17:** the paper's seed now runs as a variant for every random step.
   - It gives the same outcome as the claim's seed everywhere except fig3c-late-residuals (4 of 5 regions).
   - The failing region there is thalamus, in the bin centred 375 ms after Go: 0.76 to 0.81 against a lower bound of 0.81, at seeds +1000, +3000, +4000 and 17. That claim stays reproduced and marked seed-sensitive.
   - The seed de
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/yang-2026; cat verifier-1-report.md verifier-2-report.md
```

```
**Verifier report, round 1: Yang (2026) on DANDI:000363**

The claims file has 25 claims and the notebook tests all 25, with none blocked. My outcomes are 15 reproduced and 10 partially reproduced, with none not reproduced or blocked. I checked the helper functions on synthetic inputs and they behave as specified. `fractions` gives the right joint, choice and action values. `match` keeps the side and lick direction, stays within the 100 ms caliper and never reuses a control. `residual` is about 0 under the null and positive when shifted. `control_splits` gives the expected split energy. `mouse_summary` and `_side_diff` weight correctly. `decode` gives 0.52 on random labels and about 0.75 with a signal, so there is no label leakage.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| session-counts | reproduced | Cell 13: 168 photoinhibition sessions. With early-lick laser trials dropped, every region count equals Table 1 exactly (19/93, 13/48, 10/31, 16/71, 8/35). |
| table1-early-joint-fraction | reproduced | Cell 15: own,fill,licks gives 0.0549 / 0.0601 / 0.0844 / 0.0587 / 0.0521, 5/5 within tolerance, all below 0.10. Lowest is medulla, not ALM; the claim reports this but does not require it. |
| table1-early-axis-fractions | reproduced | Cell 18: 10/10 values within tolerance under both "fill" readings. |
| axes-cosine | reproduced | Cell 20, signed cosine: thalamus 0.297, ALM 0.523, and the other three regions lie between them. |
| fig1e-laser-vs-control-split | partially_reproduced | Cell 22: every mouse ratio is above 1 (minimum 1.16). ALM 147–156 and highest other 7.6–8.8 are within tolerance. Lowest other is 2.73–2.84 (striatum) against 3.3 ± 0.33, out under every reading and seed. |
| fig1-1b-corrected-joint-fraction | partially_reproduced | Cell 24: no combination of correction and reading puts both medulla and thalamus in tolerance; the nearest miss is thalamus 0.1094 against an upper bound of 0.1089. All region means are below 0.15. |
| fig1-1
[... 96 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/yang-2026-01.md",
 "content": "# yang-2026, Yang et al. 2026\n\nSixteen claims reproduced, nine partially, none not reproduced and none\nblocked; two outcomes, `fig2d-choice-share-flat` and\n`fig3-1c-alm-early-residual`, rest on an assumption, and\n`fig3c-late-residuals` is seed-sensitive. Both verification rounds agreed\nwith all 25 outcomes, and nothing was proposed after the second, so there\nwas no third round. The author's report and the opening sentence of the\nround-1 report counted 15 reproduced and 10 partial, a miscount of the same\noutcomes that the round-2 verifier pointed out. It pins version\n0.231012.2129, which the paper cites and which is the latest published\nversion. The paper, Yang, \"Form, Timing, and Behavioral Matching of the\nPopulation Response to ALM Photoinhibition\" (Research Square preprint,\nversion 1), reanalyses the Mesoscale Activity Map of Chen et al. 2024 (mice\nin a memory-guided directional licking task, Neuropixels recordings from\nALM, striatum, thalamus, midbrain and medulla) and reports that the early\npopulation difference after bilateral ALM photoinhibition at the end of the\ndelay lies mostly outside the choice and action axes, that lick decoding\nrises after Go without a matching rise on the choice axis, and that a\ndifference remains after laser and control trials are matched on lick\ndirection and reaction time. The claims were written from the preprint's\ntext with no figure read, and the code is in a private repository, so no\nmethod detail is settled by code; the paper reports no hypothesis test.\nReproduced are the session counts (every count of Table 1), the early\njoint, choice and action fractions, the cosine between the axes (0.297 in\nthalamus, 0.523 in ALM), the trend with neuron count, the fit without the\nvideo regression, the Go-aligned decoding rise, the matched pairs (2,667,\nmedian 1.3 ms) and reaction times, the pre-lick residuals and their ratios,\nand the residual time courses. Partial are the ratio to control splits (the\nlowest other region 2.73 to 2.84 against 3.3 +- 0.33), the corrected joint\nfraction of Figure 1-1B, the example session (the paper's\nses-20200922T135318 is within tolerance but the rule selects\nses-20210419T161140, 0.00200 against 0.00210 from the mouse mean), the\nearly and pre-lick decoding (7 of 10 within tolerance, 8 needed), the\nchoice and action shares, the Go-aligned joint fraction, the energy before\nonset (0.053 against 0.09) and the example plane (0.696 or 0.965 against\n0.25). Round 1 found that decoding laser trials alone had not been run\nthough 26 entries allow it, that seed 17 was never run, that the\nearly-residual binning and the fig2d partial clause decide their outcomes,\nand that the example-session rule had been run under one reading; in reply\nlaser-only decoding (0 of 10 within tolerance under the claim's seed) and\nseed 17 were run as variants, the rule was run under all eight readings,\nand the two ambiguities were put to a reader in `questions/yang-2026.yaml`.\nRound 2 found sentences the outputs did not support, among them a wrong\nsession name for fig1b, which were corrected. After round 2 the author\nfound that the reading dropping trials without keypoints gave different\nnumbers on two runners, left the 48 affected region entries out of it, and\nnoted that this fix has not been verified; no outcome rests on that\nreading. The author's session took about 3 h 45 min with four full runs\nand nothing failed; the notebook ran in about 29 minutes at first, with\npeak memory 9 GB, and takes 35 to 60 minutes at the end, depending on the\nrunner (62.1 in the round-2 copy).\n\nThe video keypoints (jaw, nose, tongue) hold x, y and a likelihood per\nframe with no detection flag or recommended cut; the tongue has likelihood\nof at least 0.9 in about 10% of frames and in no frame of the choice window\non 82% of trials, so how missing keypoints are handled changes any analysis\nthat regresses out tongue position, and dropping such trials leaves 48 of\n278 region entries with no more control trials than the regression's seven\ncolumns. A unit's region is given two ways, as the probe target in the\nelectrode location (`brain_regions`) and as a CCF annotation (`anno_name`),\nand neither is described as the analysis label; the probe targets give the\npaper's per-region counts exactly. Four units in the late-delay sessions\nhave spike times out of order, and in two of the 112 late-delay sessions\nthe side-camera video does not span the trials to within 5 s. Otherwise\nthe data hold what the paper describes: 168 of 174 files have\nphotostimulation trials, 112 late-delay bilateral sessions come from 19\nmice, no recording is deposited twice, every photostimulation trial has one\nonset event, and spikes and trials share a clock (the ALM laser effect in\nall 99 sessions with ALM units), as do licks and video (the tongue detected\nin 97% of frames after a lick against 40% at shifted times, in all 112\nsessions). Several choices the Methods leave open were settled by the\ndata: only dropping laser trials with an early lick gives the Table 1\ncounts, only the closest match gives the 1.3 ms median (a random match\ngives 43.3 ms), and with laser trials alone only 26 of 278 region entries\nhave the trials the decoding rule requires. Questions are put to the\npaper's author: whether the early-window residual was computed in two 50\nms bins (12.59 here, against 18.36 over one window); to confirm the\nearly-lick, matching, keypoint and decoding choices; and how the\ncontrol-split correction of Figure 1-1B, the 25% plane fraction of Figure\n3B and the pre-onset energy of 0.09 in Figure 2-1A were computed.\n\nThe author's points on the protocol: the paper states one seed, 17, while\nthe protocol requires the claim seeds, which were used as a deviation; any\nedit to the entry forces a full re-run, which cost three extra runs of a\n30-minute notebook, and markdown-only edits without re-execution would\nhelp; it is unclear how \"reproduced under any reading\" interacts with\nadopting one reading when the author adds a reading the criterion does not\nlist, and step 1.6 was applied with `assumed` set; it does not say what\n`measured` holds when no reading matches; the suggested decoding clock\ncheck does not fit this dataset, and the photoinhibition and lick-tongue\ncontrasts were used; and region reading (b) needs the Allen ontology, an\noutside input the claims file does not name, so it was not run.\n"
}
```

```
File created successfully at: docs/pilot-notes/yang-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/yang-2026-01.md",
 "content": "The paper's main findings on ALM photoinhibition held up in this data. In all five regions the early population difference lies mostly outside the choice and action axes, lick decoding rises after Go, and a difference remains after matching laser and control trials on lick direction and reaction time. Finer values matched only in part, among them the early decoding accuracies, the choice and action shares before the lick and the ratio to control-trial splits. In the example session the displayed plane held 70 to 97% of the early difference against 25%, by a computation the paper does not describe.\n"
}
```

```
File created successfully at: summaries/yang-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/yang-2026-01.md; grep -c "—\|rather\|\*\*" docs/pilot-notes/yang-2026-01.md summaries/yang-2026-01.md; git status --short
```

```
100 summaries/yang-2026-01.md
docs/pilot-notes/yang-2026-01.md:0
summaries/yang-2026-01.md:0
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
?? docs/pilot-notes/yang-2026-01.md
?? scripts
?? summaries/yang-2026-01.md
```

**Agent**

I wrote both files and changed nothing else. One gap in the sources: `targets/dandisets.json` has no entry for 000363, so there is no `catalystneuro` field to check. The record doesn't say whether CatalystNeuro converted this dataset, and the notes say nothing about a conversion. Separately, `git status` shows untracked files I didn't create (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others); I left them alone.

**docs/pilot-notes/yang-2026-01.md**

# yang-2026, Yang et al. 2026

Sixteen claims reproduced, nine partially, none not reproduced and none blocked; two outcomes, `fig2d-choice-share-flat` and `fig3-1c-alm-early-residual`, rest on an assumption, and `fig3c-late-residuals` is seed-sensitive. Both verification rounds agreed with all 25 outcomes, and nothing was proposed after the second, so there was no third round. The author's report and the opening sentence of the round-1 report counted 15 reproduced and 10 partial, a miscount of the same outcomes that the round-2 verifier pointed out. It pins version 0.231012.2129, which the paper cites and which is the latest published version. The paper, Yang, "Form, Timing, and Behavioral Matching of the Population Response to ALM Photoinhibition" (Research Square preprint, version 1), reanalyses the Mesoscale Activity Map of Chen et al. 2024 (mice in a memory-guided directional licking task, Neuropixels recordings from ALM, striatum, thalamus, midbrain and medulla) and reports that the early population difference after bilateral ALM photoinhibition at the end of the delay lies mostly outside the choice and action axes, that lick decoding rises after Go without a matching rise on the choice axis, and that a difference remains after laser and control trials are matched on lick direction and reaction time. The claims were written from the preprint's text with no figure read, and the code is in a private repository, so no method detail is settled by code; the paper reports no hypothesis test. Reproduced are the session counts (every count of Table 1), the early joint, choice and action fractions, the cosine between the axes (0.297 in thalamus, 0.523 in ALM), the trend with neuron count, the fit without the video regression, the Go-aligned decoding rise, the matched pairs (2,667, median 1.3 ms) and reaction times, the pre-lick residuals and their ratios, and the residual time courses. Partial are the ratio to control splits (the lowest other region 2.73 to 2.84 against 3.3 +- 0.33), the corrected joint fraction of Figure 1-1B, the example session (the paper's ses-20200922T135318 is within tolerance but the rule selects ses-20210419T161140, 0.00200 against 0.00210 from the mouse mean), the early and pre-lick decoding (7 of 10 within tolerance, 8 needed), the choice and action shares, the Go-aligned joint fraction, the energy before onset (0.053 against 0.09) and the example plane (0.696 or 0.965 against 0.25). Round 1 found that decoding laser trials alone had not been run though 26 entries allow it, that seed 17 was never run, that the early-residual binning and the fig2d partial clause decide their outcomes, and that the example-session rule had been run under one reading; in reply laser-only decoding (0 of 10 within tolerance under the claim's seed) and seed 17 were run as variants, the rule was run under all eight readings, and the two ambiguities were put to a reader in `questions/yang-2026.yaml`. Round 2 found sentences the outputs did not support, among them a wrong session name for fig1b, which were corrected. After round 2 the author found that the reading dropping trials without keypoints gave different numbers on two runners, left the 48 affected region entries out of it, and noted that this fix has not been verified; no outcome rests on that reading. The author's session took about 3 h 45 min with four full runs and nothing failed; the notebook ran in about 29 minutes at first, with peak memory 9 GB, and takes 35 to 60 minutes at the end, depending on the runner (62.1 in the round-2 copy).

The video keypoints (jaw, nose, tongue) hold x, y and a likelihood per frame with no detection flag or recommended cut; the tongue has likelihood of at least 0.9 in about 10% of frames and in no frame of the choice window on 82% of trials, so how missing keypoints are handled changes any analysis that regresses out tongue position, and dropping such trials leaves 48 of 278 region entries with no more control trials than the regression's seven columns. A unit's region is given two ways, as the probe target in the electrode location (`brain_regions`) and as a CCF annotation (`anno_name`), and neither is described as the analysis label; the probe targets give the paper's per-region counts exactly. Four units in the late-delay sessions have spike times out of order, and in two of the 112 late-delay sessions the side-camera video does not span the trials to within 5 s. Otherwise the data hold what the paper describes: 168 of 174 files have photostimulation trials, 112 late-delay bilateral sessions come from 19 mice, no recording is deposited twice, every photostimulation trial has one onset event, and spikes and trials share a clock (the ALM laser effect in all 99 sessions with ALM units), as do licks and video (the tongue detected in 97% of frames after a lick against 40% at shifted times, in all 112 sessions). Several choices the Methods leave open were settled by the data: only dropping laser trials with an early lick gives the Table 1 counts, only the closest match gives the 1.3 ms median (a random match gives 43.3 ms), and with laser trials alone only 26 of 278 region entries have the trials the decoding rule requires. Questions are put to the paper's author: whether the early-window residual was computed in two 50 ms bins (12.59 here, against 18.36 over one window); to confirm the early-lick, matching, keypoint and decoding choices; and how the control-split correction of Figure 1-1B, the 25% plane fraction of Figure 3B and the pre-onset energy of 0.09 in Figure 2-1A were computed.

The author's points on the protocol: the paper states one seed, 17, while the protocol requires the claim seeds, which were used as a deviation; any edit to the entry forces a full re-run, which cost three extra runs of a 30-minute notebook, and markdown-only edits without re-execution would help; it is unclear how "reproduced under any reading" interacts with adopting one reading when the author adds a reading the criterion does not list, and step 1.6 was applied with `assumed` set; it does not say what `measured` holds when no reading matches; the suggested decoding clock check does not fit this dataset, and the photoinhibition and lick-tongue contrasts were used; and region reading (b) needs the Allen ontology, an outside input the claims file does not name, so it was not run.

**summaries/yang-2026-01.md**

The paper's main findings on ALM photoinhibition held up in this data. In all five regions the early population difference lies mostly outside the choice and action axes, lick decoding rises after Go, and a difference remains after matching laser and control trials on lick direction and reaction time. Finer values matched only in part, among them the early decoding accuracies, the choice and action shares before the lick and the ratio to control-trial splits. In the example session the displayed plane held 70 to 97% of the early difference against 25%, by a computation the paper does not describe.

## End of run

18 turns, 2 minutes, $1.13 at API prices, result: success.
