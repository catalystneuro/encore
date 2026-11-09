# crcns-hc-7 · recorder · run 42364775784

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py crcns-hc-7; ls claims/crcns-hc-7/ transcripts/crcns-hc-7/; cat attempts/crcns-hc-7-kohus-2016-01.yaml
```

```
<persisted-output>
Output too large (86.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6bec2232-1172-43fb-9e33-b661d7bb1250/tool-results/bx1uki76d.txt

Preview (first 2KB):
docs/pilot-notes/000055-peterson-2021-01.md
docs/pilot-notes/001950-su-2026-01.md
docs/pilot-notes/crcns-hc-24-varela-2020-01.md
docs/pilot-notes/crcns-ear-1-farrell-2020-01.md
docs/pilot-notes/crcns-pag-2-moaddab-2020-01.md
| [CRCNS:hc-7](http://crcns.org/data-sets/hc/hc-7) | [Kohus et al. 2016](https://doi.org/10.1113/jp272231) | 10 | 4 | 12 | 18 | [`crcns-hc-7-kohus-2016`](entries/crcns-hc-7-kohus-2016) |
claims/crcns-hc-7/:
10.1113-jp272231.yaml

transcripts/crcns-hc-7/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/crcns-hc-7-kohus-2016-01.yaml; for f in 000055-peterson-2021-01 001950-su-2026-01 crcns-hc-24-varela-2020-01 crcns-ear-1-farrell-2020-01 crcns-pag-2-moaddab-2020-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; cat docs/pilot-notes/001754-knierim-2000-02.md | head -3; ls summaries | head; cat summaries/crcns-hc-24-varela-2020-01.md summaries/000055-peterson-2021-01.md
```

```
Exit code 1
schema_version: 2
id: crcns-hc-7-kohus-2016-01
dataset:
  archive: crcns
  id: hc-7
  version: unversioned
  doi: 10.6080/K0MK69T5
paper: doi:10.1113/jp272231
date: 2026-11-06
entry: crcns-hc-7-kohus-2016
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
[... 161 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-hc-7-kohus-2016-01.yaml",
 "offset": 95
}
```

```
File content (34501 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Bash**

```bash
cd  for f in 000055-peterson-2021-01 001950-su-2026-01 crcns-hc-24-varela-2020-01 crcns-ear-1-farrell-2020-01 crcns-pag-2-moaddab-2020-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; echo "--- summary"; cat summaries/$f.md 2>/dev/null; done; head -3 docs/pilot-notes/001754-knierim-2000-02.md
```

```
<persisted-output>
Output too large (45.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6bec2232-1172-43fb-9e33-b661d7bb1250/tool-results/bsljxu1od.txt

Preview (first 2KB):
=== 000055-peterson-2021-01
# 000055, Peterson et al. 2021

Seven claims reproduced (four on an assumption), four partially, one not
reproduced and none blocked; the claims that also use the paper's projection
matrices from electrodes to AAL regions on Figshare (`with_inputs`) are counted
apart, with eight reproduced (six on an assumption), two partially (one on an
assumption) and `fig3-lfb-more-widespread` blocked as methods_underspecified,
and the two link claims, `subject-days` and `roi-projection-link`, are left out,
both reproduced. The first verification round agreed with 19 of the 25 outcomes
as they stood and the second with all 25; nothing was proposed after the
second, so there was no third round. The version is 0.220127.0436, the only
published one, which the paper does not cite. The paper, Peterson, Singh, Wang,
Rao and Brunton in eNeuro (8(3), ENEURO.0007-21.2021), studies contralateral
wrist movements detected from video pose in 12 epilepsy patients with ECoG over
several days of clinical monitoring, describes ten behavioural and
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6bec2232-1172-43fb-9e33-b661d7bb1250/tool-results/bsljxu1od.txt"
}
```

```
1	=== 000055-peterson-2021-01
2	# 000055, Peterson et al. 2021
3	
4	Seven claims reproduced (four on an assumption), four partially, one not
5	reproduced and none blocked; the claims that also use the paper's projection
6	matrices from electrodes to AAL regions on Figshare (`with_inputs`) are counted
7	apart, with eight reproduced (six on an assumption), two partially (one on an
8	assumption) and `fig3-lfb-more-widespread` blocked as methods_underspecified,
9	and the two link claims, `subject-days` and `roi-projection-link`, are left out,
10	both reproduced. The first verification round agreed with 19 of the 25 outcomes
11	as they stood and the second with all 25; nothing was proposed after the
12	second, so there was no third round. The version is 0.220127.0436, the only
13	published one, which the paper does not cite. The paper, Peterson, Singh, Wang,
14	Rao and Brunton in eNeuro (8(3), ENEURO.0007-21.2021), studies contralateral
15	wrist movements detected from video pose in 12 epilepsy patients with ECoG over
16	several days of clinical monitoring, describes ten behavioural and
17	environmental features of these movements, projects movement-related spectral
18	power onto eight AAL regions, and fits regression models of single-event power
19	on the features; the dandiset (AJILE12) holds 55 NWB files, one per
20	subject-day, 845.87 GB in all. The claims were written from the version of
[... 602 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l attempts/crcns-hc-7-kohus-2016-01.yaml claims/crcns-hc-7/*.yaml transcripts/crcns-hc-7/*-report.md transcripts/crcns-hc-7/author-report.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
items = d if isinstance(d,list) else d.get('dandisets', d)
import sys
for x in (items if isinstance(items,list) else items.values()):
    if 'hc-7' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
1350 attempts/crcns-hc-7-kohus-2016-01.yaml
  1381 claims/crcns-hc-7/10.1113-jp272231.yaml
    12 transcripts/crcns-hc-7/answer-report.md
    17 transcripts/crcns-hc-7/author-answers-report.md
    96 transcripts/crcns-hc-7/author-report.md
    32 transcripts/crcns-hc-7/author-revise-1-report.md
    31 transcripts/crcns-hc-7/author-revise-2-report.md
    24 transcripts/crcns-hc-7/claims-check-report.md
    25 transcripts/crcns-hc-7/claims-report.md
    82 transcripts/crcns-hc-7/verifier-1-report.md
    47 transcripts/crcns-hc-7/verifier-2-report.md
    96 transcripts/crcns-hc-7/author-report.md
  3193 total
```

**Agent**

The sources are large, so I'm reading the reports and target entry first, then the attempt record.

**Agent calls Bash**

```bash
cd  grep -n -B3 -A12 'hc-7"' targets/dandisets.json | head -40; cd transcripts/crcns-hc-7; for f in author-report answer-report author-answers-report verifier-1-report author-revise-1-report verifier-2-report author-revise-2-report; do echo "=== $f"; cat $f.md; done
```

```
<persisted-output>
Output too large (34.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6bec2232-1172-43fb-9e33-b661d7bb1250/tool-results/bxpukr9hv.txt

Preview (first 2KB):
=== author-report
I've finished steps 1 to 5 for CRCNS hc-7 and run the handover (step 6). `check` reports 0 errors, and `entry.py all` passes: the notebook runs from a clean environment in 342 s. I did not verify my own work and did not commit.

## 1. Outcomes (44 claims)

| Claim | Outcome |
|---|---|
| fig4b-in-pc-kruskal-wallis | reproduced |
| fig4b-in-pc-posthoc | not reproduced (4 of 8 comparisons hold) |
| fig4c-cckdti-pc-silent-single-ap | not reproduced (3 of 7 pairs silent) |
| fig5c-pv-rip-depression | reproduced |
| fig5c-cck-rip-facilitation | reproduced |
| fig5db-recovery | reproduced (only without multiple-comparison correction) |
| fig6-pv-trains-depression | not reproduced (fails at 1 Hz) |
| fig6-cckbc-pc-trains | not reproduced |
| cckdti-pc-transmission | not reproduced |
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6bec2232-1172-43fb-9e33-b661d7bb1250/tool-results/bxpukr9hv.txt"
}
```

```
1	=== author-report
2	I've finished steps 1 to 5 for CRCNS hc-7 and run the handover (step 6). `check` reports 0 errors, and `entry.py all` passes: the notebook runs from a clean environment in 342 s. I did not verify my own work and did not commit.
3	
4	## 1. Outcomes (44 claims)
5	
6	| Claim | Outcome |
7	|---|---|
8	| fig4b-in-pc-kruskal-wallis | reproduced |
9	| fig4b-in-pc-posthoc | not reproduced (4 of 8 comparisons hold) |
10	| fig4c-cckdti-pc-silent-single-ap | not reproduced (3 of 7 pairs silent) |
11	| fig5c-pv-rip-depression | reproduced |
12	| fig5c-cck-rip-facilitation | reproduced |
13	| fig5db-recovery | reproduced (only without multiple-comparison correction) |
14	| fig6-pv-trains-depression | not reproduced (fails at 1 Hz) |
15	| fig6-cckbc-pc-trains | not reproduced |
16	| cckdti-pc-transmission | not reproduced |
17	| async-charge-epi-vs-160 | partially reproduced |
18	| decay-epi-vs-160 | partially reproduced |
19	| fig8-pvbc-pvbc-uipsc | partially reproduced (3 of 5 values within tolerance) |
20	| fig8-cck-pairs-uipsc | not reproduced (rests on an assumption) |
[... 305 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n 'hc-7' targets/dandisets.json | head; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if any('hc-7'==str(v) or str(v).endswith('hc-7') for v in x.values()): print(json.dumps(x,indent=1)); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  ls targets; grep -il 'hc-7\|hc_7\|K0MK69T5' targets/* ; grep -n 'hc-24' targets/*.json | head -5
```

```
crcns.json
dandisets.json
description_papers.yaml
dryad.json
ebrains.json
figshare.json
openneuro.json
pilot.yaml
targets/crcns.json
targets/crcns.json:646:   "id": "hc-24",
targets/crcns.json:648:   "url": "http://crcns.org/data-sets/hc/hc-24",
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
d=json.load(open('targets/crcns.json'))
items = d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list))
for x in items:
    if x.get('id')=='hc-7': print(json.dumps(x,indent=1))
E
```

```
{
 "id": "hc-7",
 "name": "Temporal properties of mouse hippocampal CA3 area PV and CCK inhibitory neuron transmission measured by physiologically relevant action potential sequences.",
 "url": "http://crcns.org/data-sets/hc/hc-7",
 "doi": "10.6080/K0MK69T5",
 "published_version": null,
 "asset_count": 3,
 "size_gb": 0.24,
 "data_standards": [
  "compressed archives"
 ],
 "species": [
  "House mouse"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.1113/jp272231",
[... 8 more lines not kept]
```

**Agent**

The dataset's target entry is in `targets/crcns.json`, not `dandisets.json`, and its `catalystneuro` field is empty. Next I'm reading the full attempt record.

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-hc-7-kohus-2016-01.yaml",
 "offset": 60,
 "limit": 420
}
```

```
60	  output: claim:fig4b-in-pc-kruskal-wallis
61	  notes: With the single AP 1.3 s before the RIP burst (M3 a), all five measures differ across PV+BC (7 pairs),
62	    AAC (7) and CCK+BC (12) to PC pairs at p < 0.05, with the authors' failures (M2 a; rise 0.0191, latency
63	    0.00842, amplitude 0.00405, potency 0.00624, transmission probability 0.00951) and with detected failures
64	    (M2 b; 0.00653 to 0.0179). The 1 Hz train (M3 b; 4, 3 and 3 pairs) gives no difference and the pooled reading
65	    (M3 c) three or four. The decay time constant does not differ (p 0.122). Medians (M3 a, M2 a) PV+BC, AAC,
66	    CCK+BC; rise 0.601, 0.547, 0.709 ms; latency 0.747, 0.664, 0.999 ms; amplitude 113.1, 226.1, 40.3 pA; transmission
67	    probability 1.0, 1.0, 0.875. With only the 6 CCK+BC to PC pairs at or below the type's median holding current,
68	    rise and latency no longer differ (p 0.26 and 0.14, against 0.021 and 0.0084 with all 12 pairs, on the per-pair
69	    table of the pipette check), so these two differences depend on the pairs where a CsCl admixture would lengthen
70	    latency; with 6 pairs the tests also lose power.
71	  deviations:
72	  - The data set holds 7 PV+BC, 8 AAC (7 with a RIP recording) and 12 CCK+BC to PC pairs, against the paper's
73	    8, 9 and 14 high KCl pairs.
74	  - Rise, latency and peak are measured on averaged sweeps with a baseline 4 to 0.8 ms before the AP peak and
75	    a response window 0.3 to 8 ms after it, standard choices the paper does not give.
76	  - The files do not say which pipette solution each pair was recorded with. Assumed that every IN to PC pair
77	    is a high KCl pair, as no type has more pairs than the paper's high KCl count and the paper says most pairs
78	    were recorded with it (Methods, paired recordings). Checked per pair in the notebook (holding current,
79	    rise time and latency by recording day); no type splits into two groups (holding currents -376.0 to 23.4
[... 400 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-hc-7-kohus-2016-01.yaml",
 "offset": 480,
 "limit": 330
}
```

```
480	    holds and the decreases lie in 10 to 50%, the criterion's partial. With other seeds of the starting points
481	    one fit stops at a worse optimum (seed 2, PV+BC to PV+BC under a; decrease 4.5% and lowest BIC UDR with
482	    facilitation); keeping the best of 16 starting points gives the numbers above.
483	  deviations:
484	  - Four starting points per fit (a standard choice); the optimizer is trust-region least squares. The notebook
485	    repeats the fits with three more seeds and keeps the best of the 16 starting points as a check.
486	  - Fitted on the authors' mean amplitudes (M4 a) of the 10-AP trains with the 11th AP; the 1 Hz train has
487	    no 11th AP in the sweeps.
488	  - The files do not say which pipette solution each pair was recorded with. Assumed that every IN to PC pair
489	    is a high KCl pair, as no type has more pairs than the paper's high KCl count and the paper says most pairs
490	    were recorded with it (Methods, paired recordings). Checked per pair in the notebook (holding current,
491	    rise time and latency by recording day); no type splits into two groups (holding currents -376.0 to 23.4
492	    pA, spread continuously), but a mixture with CsCl pairs cannot be ruled out, and CsCl lengthens rise time
493	    and latency (Results, Fig. 7). In CCK+BC to PC pairs latency rises with the holding current (rho 0.58,
494	    p 0.048), one sign against the assumption.
495	  assumed: true
496	- claim: fig11-model-cck-facilitation
497	  outcome: reproduced
498	  notebook: reproduce_kohus_2016.ipynb
499	  output: claim:fig11-model-cck-facilitation
[... 310 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '^[a-z_]*:' attempts/crcns-hc-7-kohus-2016-01.yaml; grep -n '^- date\|^  reviewed\|^  date\|^  kind' attempts/crcns-hc-7-kohus-2016-01.yaml
```

```
1:schema_version: 2
2:id: crcns-hc-7-kohus-2016-01
3:dataset:
8:paper: doi:10.1113/jp272231
9:date: 2026-11-06
10:entry: crcns-hc-7-kohus-2016
11:provenance:
22:outcomes:
635:verifications:
1290:findings:
12:  kind: agent
636:- date: '2026-11-07'
637:  kind: agent
639:  reviewed: Round 1. The handover of the author-answers run, the executed notebook with the conclusions and
988:- date: '2026-11-07'
989:  kind: agent
991:  reviewed: Round 2. The full executed notebook of the author-revise-1 run with its conclusions and summary, the
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-hc-7-kohus-2016-01.yaml",
 "offset": 985,
 "limit": 15
}
```

```
985	    outcome: blocked
986	    reason: There are no field potential recordings.
987	    response: No change of outcome.
988	- date: '2026-11-07'
989	  kind: agent
990	  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
991	  reviewed: Round 2. The full executed notebook of the author-revise-1 run with its conclusions and summary, the
992	    attempt record, the README, the helper module and the claims file, with the paper under paper/. The verifier
993	    counted 21 assumed outcomes; the record marks 16, all on IN to PC pairs.
994	  results:
995	  - claim: fig2b-pv-cck-clusters
996	    agrees: true
997	    outcome: blocked
998	    reason: I agree with all 44 outcomes.
999	    response: No change.
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-hc-7-kohus-2016-01.yaml",
 "offset": 1290
}
```

```
1290	findings:
1291	- kind: metadata_error
1292	  statement: The stimulation timings in the data differ from the data descriptor and the paper. RIP bursts
1293	    are four APs 4.5 ms apart (222 Hz), not 160 Hz; the EPI burst is 30 APs 6.7 ms apart (147 Hz) and four
1294	    3.3 ms apart (303 Hz), not 160 and 320 Hz; the single AP precedes the RIP and EPI bursts by 1.3 s, not
1295	    1 s. The 10-AP trains are at their nominal rates.
1296	- kind: metadata_error
1297	  statement: Experiments_description.txt mislabels two recordings (PV+BC to PV+BC pair 10 s130807-0205, listed
1298	    as 5 Hz, and CCK+DTI to PC pair 5 s150222-0305, listed as 40 Hz, are 10 Hz trains), names eight files that
1299	    are not in the zip (three misdated s1508.. for s1308..), lists one file for two protocols in two pairs,
1300	    leaves 20 recordings of the zip unnamed, lists no PV+BC to AAC pairs, and numbers the IN to PC pairs differently
1301	    from the PairNN folders.
1302	- kind: data_missing
1303	  statement: Three recordings have a header but no sweeps (CCK+BC to PC Pair07 s140616-0105 and -0106, CCK+DTI
1304	    to PC Pair01 s150119-0104), three have sweeps but no _EPA table, and the RIP recording listed for PV+BC
1305	    to PC pair 4 is absent. The data set holds 7 PV+BC, 8 AAC, 12 CCK+BC and 7 CCK+DTI to PC and 14 PV+BC to
1306	    PV+BC pairs, fewer than the paper's 8, 9, 14, 8 and 16. The CCK+ to CCK+ pairs were recorded only with
1307	    10, 40 and 160 Hz trains, with no RIP recording, 1 Hz train or 320 Hz train, so their single-AP uIPSCs
1308	    (Fig. 8) and 320 Hz charges (Fig. 10B) cannot be measured.
1309	- kind: data_missing
[... 42 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-hc-7/10.1113-jp272231.yaml",
 "limit": 90
}
```

```
1	# Claims for Kohus, Kali, Rovira-Esteban, Schlingloff, Papp, Freund, Hajos & Gulyas (2016), J Physiol,
2	# "Properties and dynamics of inhibitory synaptic communication within the CA3 microcircuits of
3	# pyramidal cells and interneurons expressing parvalbumin or cholecystokinin", doi:10.1113/jp272231,
4	# on CRCNS data set hc-7 (doi:10.6080/K0MK69T5).
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
6	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
7	#
8	# Text read: the version of record (J Physiol 2016, pp 1 to 30), as supplied under paper/ (text
9	# extracted from the PDF with PyMuPDF): Key points, Methods, Results, Discussion, the legends of
10	# Figures 1 to 13 and Tables 1 to 4. The paper has no supplement. The PDF could not be opened as
11	# images in this run (no renderer installed), so values printed only inside figures (the medians of
12	# Fig. 4B, 5C, 5Db, 6B and C, 7, 10, 11B and 12) were not read; claims on those figures rest on the
13	# Results and the legends. The extracted Table 4 holds every column: for the three PV+ types U0,
14	# tau_r (1080, 1620, 1700 ms), tau_e (23.7, 13.5, 13.6 ms), a_e, k_e and Imax; for CCK+BC to PC U0
15	# 0.15 (0.11, 0.18), tau_r 71 ms, tau_f 10.9 (7.2, 53.5) ms and Imax 499 (252, 708) pA. Table 4 gives
16	# the best model of each type; the Figure 11 legend gives the type parameters of a fit that includes
17	# use-dependent replenishment for all four types, and differs from Table 4 for CCK+BC to PC (tau_r
18	# 12.9 s against 71 ms) and for PV+BC to PV+BC tau_e (2.37 against 23.7 ms).
19	#
20	# Code. The paper links no code. Its Methods name in-house and third-party programs (Stimulog, EVAN,
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i 'check\|added\|amended' claims/crcns-hc-7/10.1113-jp272231.yaml | head -20; grep -n '^- id:\|^  - id:\|^  id:' claims/crcns-hc-7/10.1113-jp272231.yaml | head -50; sed -n 1,40p questions/crcns-hc-7.yaml 2>/dev/null | head -5
```

```
81:#   correction on the Figure 3A counts (checked by hand), so the chi-squared tests are run without it.
1338:checks:
1358:  - table2-pvbc-aac-features, added the Table 2 Mann-Whitney p-values for input resistance (1.0e-4)
1362:  - fig6-pv-trains-depression, the statement's synchrony under EPI had no test; added one from the
1369:  - fig10-cck-cck-heterogeneity, added the Fig. 10Ac legend reading (asynchronous release above 10
88:  id: hc-7
92:- id: fig2b-pv-cck-clusters
117:- id: fig2b-pvbc-aac-clusters
135:- id: cck-no-subclusters
150:- id: table1-pv-cck-features
201:- id: table2-pvbc-aac-features
254:- id: fig3-cp-pv
295:- id: fig3-cp-cck
328:- id: fig3-cp-pv-cck
357:- id: fig4b-in-pc-kruskal-wallis
388:- id: fig4b-in-pc-posthoc
411:- id: fig4c-cckdti-pc-silent-single-ap
431:- id: fig7a-cscl-kinetics
453:- id: fig5c-pv-rip-depression
474:- id: fig5c-cck-rip-facilitation
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-hc-7/10.1113-jp272231.yaml",
 "offset": 1338
}
```

```
1338	checks:
1339	- date: 2026-11-06
1340	  kind: agent
1341	  model: claude-opus-5-5
1342	  ready: true
1343	  changes:
1344	  - Header comment, the extracted Table 4 is not missing columns; it gives tau_r, tau_e, a_e and
1345	    k_e for the PV+ types and tau_r 71 ms for CCK+BC to PC. The comment now records the values and the
1346	    two conflicts with the Figure 11 legend (CCK+BC tau_r 71 ms against 12.9 s; PV+BC to PV+BC tau_e
1347	    23.7 against 2.37 ms).
1348	  - table4-model-parameters, CCK+BC tau_r changed from 12.9 s (Fig. 11 legend) to 71 ms (Table 4),
1349	    the value of the best model the claim tests; 12.9 s kept as a named variant for the comprehensive
1350	    model; inferred note and statement corrected, as the text did not lose the cells.
1351	  - fig13-pvbc-pc-recovery-halftime, tolerance 147.8 changed to 152.2 ms, the distance from 495.8 to
1352	    either quartile (343.6, 648.0) under M7.
1353	  - M6, recorded that the chi-squared p-values 9.42e-4, 0.0175 and 0.0181 match a 2 x 2 Pearson test
1354	    without Yates correction on the Figure 3A counts (14/32 against 0/18; 36/94 against 4/28; 22/44
1355	    against 2/14), so the tests are run that way.
1356	  - fig3-cp-pv, recorded that the counts give 3.2e-4 (uncorrected) or 1.2e-3 (Yates) for PV+BC against
1357	    AAC, not the printed 6.21e-4; both are shown.
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -B2 -A4 'abstract\|key points' claims/crcns-hc-7/10.1113-jp272231.yaml | grep -v '^--$' | head -60
```

```
7-#
8-# Text read: the version of record (J Physiol 2016, pp 1 to 30), as supplied under paper/ (text
9:# extracted from the PDF with PyMuPDF): Key points, Methods, Results, Discussion, the legends of
10-# Figures 1 to 13 and Tables 1 to 4. The paper has no supplement. The PDF could not be opened as
11-# images in this run (no renderer installed), so values printed only inside figures (the medians of
12-# Fig. 4B, 5C, 5Db, 6B and C, 7, 10, 11B and 12) were not read; claims on those figures rest on the
13-# Results and the legends. The extracted Table 4 holds every column: for the three PV+ types U0,
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml,collections
d=yaml.safe_load(open('attempts/crcns-hc-7-kohus-2016-01.yaml'))
c=collections.Counter((o['outcome'],o.get('assumed',False),o.get('blocked_by')) for o in d['outcomes'])
for k,v in sorted(c.items(),key=str): print(k,v)
for v in d['verifications']:
    print(v['reviewed'][:30], sum(r['agrees'] for r in v['results']), len(v['results']))
E
```

```
('blocked', False, 'data_missing') 16
('blocked', False, 'metadata_insufficient') 2
('not_reproduced', False, None) 6
('not_reproduced', True, None) 6
('partially_reproduced', False, None) 1
('partially_reproduced', True, None) 3
('reproduced', False, None) 3
('reproduced', True, None) 7
Round 1. The handover of the a 34 44
Round 2. The full executed not 44 44
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
d=yaml.safe_load(open('attempts/crcns-hc-7-kohus-2016-01.yaml'))
for r in d['verifications'][0]['results']:
    if not r['agrees']: print(r['claim'], r['outcome'])
E
```

```
Exit code 1
fig6-cckbc-async-onset not_reproduced
cckdti-async-onset not_reproduced
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
KeyError: 'outcome'
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
d=yaml.safe_load(open('attempts/crcns-hc-7-kohus-2016-01.yaml'))
for r in d['verifications'][0]['results']:
    if not r['agrees']: print(r['claim'], r.get('outcome'), '|', r['reason'][:150])
E
```

```
fig6-cckbc-async-onset not_reproduced | The claims file defines two onset rules and both were run. EPI median onset is 2 (rule a) and 1 (rule b), against 11 in the paper. That the rules also
cckdti-async-onset not_reproduced | EPI median onset is 3 (rule a) and 1 (rule b), against 7. At 160 Hz, rule a gives onsets 2, 7, 2.
async-charge-epi-vs-160 None | Cannot be judged from the outputs. The 160 Hz arm is measured after the wrong AP (problem 1); for the 10-AP trains train = times[first:] keeps the 11t
decay-epi-vs-160 None | Cannot be judged from the outputs; same bug. The 160 Hz decay constants (7.4 and 8.2 ms) are those of the isolated 11th IPSC. The EPI medians, 96.05 a
fig8-cck-pairs-uipsc blocked | Blocked (data_missing). The CCK+ pairs have no RIP or 1 Hz recordings, so none of the claims-file M3 readings applies. Under the notebook's own readin
fig8-cckbc-vs-cckdti-pairs blocked | Blocked (data_missing), same reason. Under reading d, CCK+BC rise is slower than CCK+DTI, the opposite of the claim.
fig10-cck-cck-heterogeneity not_reproduced | Rule a gives asynchronous release in 9 of 10 pairs (all at 160 Hz). Rule b gives 1 of 10. The target is 45 to 66%. The verifier asked for the per-pair
fig10-cck-cck-async not_reproduced | Rule a onsets at 160 Hz are at the 2nd to 5th AP, not after the 5th. Rule b finds no onset in 8 of 9 pairs. The duration and charge parts were never p
fig10bd-be-async-charge blocked | Blocked (data_missing for the 320 Hz parts). CCK+ to CCK+ pairs have only 10, 40 and 160 Hz trains. The 10/40/160 Hz parts could be tested; the charge
decay-pc-vs-interneuron blocked | PV+BC half reproduced; CCK+BC half blocked (data_missing). PV+BC 7.78 against 3.38 ms, p 2e-4, both medians within tolerance. The CCK+BC side can only
```

**Agent**

I have everything I need. The `catalystneuro` field is empty, so the notes won't open with the conversion sentence. Writing both files now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/crcns-hc-7-kohus-2016-01.md",
 "content": "# crcns-hc-7, Kohus et al. 2016\n\nTen claims reproduced (seven on an assumption), four partially (three on an\nassumption), 12 not reproduced (six on an assumption) and 18 blocked, 16 for\nmissing data and two for insufficient metadata. The first verification round\nagreed with 34 of the 44 outcomes as they stood and the second with all 44;\nnothing was proposed after the second, so there was no third round. CRCNS does\nnot version data sets, so the version is recorded as unversioned with the data\nset's DOI (10.6080/K0MK69T5), and the notebook header gives the MD5 sum of\n`Data.zip`, the only copy in the bucket. The paper, Kohus, Kali,\nRovira-Esteban, Schlingloff, Papp, Freund, Hajos and Gulyas in the Journal of\nPhysiology, records pairs of CA3 interneurons and pyramidal cells (PC) in mouse\nslices, with parvalbumin-expressing basket cells (PV+BC) and axo-axonic cells\n(AAC) and cholecystokinin-expressing basket cells (CCK+BC) and dendritic-region\ntargeting cells (CCK+DTI) as the presynaptic cells, and compares the kinetics,\nshort-term plasticity and asynchronous release of their uIPSCs under 10-AP\ntrains, ripple-like bursts (RIP) and epileptiform bursts (EPI), fits models of\nshort-term plasticity, and relates PV+BC to PC recovery to the refractoriness of\nsharp-wave ripples; the data set is one zip of raw paired sweeps and the\nauthors' per-sweep tables (`_EPA`) for 60 pairs in 8 connection types. The\nclaims were written from the version of record, whose text was extracted from\nthe PDF, without the figure images, as the PDF could not be rendered, and\nwithout code, as the paper links none; the claims check corrected the Table 4\nvalues and a tolerance, and added `sipsc-continuum`, for 44 claims. The uIPSC\nproperties of Figs. 4 and 8, the plasticity under RIP, trains and recovery\n(Figs. 5, 6, 9 and 10), the asynchronous release and the models of Fig. 11\ncould be tested; the firing-pattern clusters of Fig. 2 and Tables 1 and 2, the\nconnection probabilities of Fig. 3, the CsCl comparisons of Fig. 7, the\nspontaneous IPSCs of Fig. 12 and the field potential and optogenetic results of\nFig. 13 could not. Every outcome on interneuron to PC pairs except the CCK+DTI\nones rests on the assumption that all were recorded with high KCl. Reproduced\nare, among others, `fig4b-in-pc-kruskal-wallis` (all five measures differ,\nlatency p 0.00842, though rise and latency no longer differ on the 6 CCK+BC\npairs at or below the median holding current, p 0.26 and 0.14),\n`fig5c-pv-rip-depression`, `fig9-pvbc-pvbc-depression` (Spearman rho -0.737),\n`fig10-cck-cck-frequency` (medians 1.559 at 10 Hz and 2.153 at 40 Hz),\n`fig11-model-cck-facilitation`, on a BIC margin of 1.8 under one reading, and\n`fig13-pvbc-pc-recovery-halftime` (median tau 525.8 ms), which only 3 of 8 fit\ncombinations meet. Partial are `decay-epi-vs-160`, `fig8-pvbc-pvbc-uipsc` (3 of\n5 medians within 10%), `fig11-model-pv-udr` (SSE decreases of 22.9, 13.1 and\n24.7% against 35, 22 and 34%) and `table4-model-parameters` (8 of 13 values).\nNot reproduced are, among others, `fig4b-in-pc-posthoc` (4 of 8 comparisons),\n`fig4c-cckdti-pc-silent-single-ap` (3 of 7 pairs silent; 7 of 7 counting only\nthe first sweep), `fig6-pv-trains-depression` (fails at 1 Hz),\n`fig6-cckbc-pc-trains` (1 of 6 pairs facilitates at every frequency),\n`fig9-pvbc-pvbc-transmission-probability`, `fig11c-parameter-differences` and\nthe four onset claims, `fig6-cckbc-async-onset` (CCK+BC EPI median onset 2.0\nagainst 10 to 12), `cckdti-async-onset`, `fig10-cck-cck-heterogeneity` and\n`fig10-cck-cck-async`, whose two onset rules from the claims file also mark\nrelease in the PV+ pairs the paper calls synchronous. The author's first run\nhad 10 reproduced, 5 partially, 10 not reproduced and 19 blocked, with the four\nonset claims and `fig10bd-be-async-charge` blocked as methods_underspecified.\nThe author asked no questions of a reader, so the answer and author-answers\nruns changed nothing. Round 1 disagreed on ten claims: the onset claims should\nbe judged on the claims file's two rules, the three claims resting on a reading\nthe claims file does not list (`fig8-cck-pairs-uipsc`,\n`fig8-cckbc-vs-cckdti-pairs`, `decay-pc-vs-interneuron`) should be blocked, and\n`async-charge-epi-vs-160` and `decay-epi-vs-160` could not be judged, as the 160\nHz arm was measured after the isolated 11th AP and not the 10th; it also asked\nthat the high KCl assumption be checked. In reply the code was fixed, the onset\nclaims became not reproduced, the three claims blocked, `async-charge-epi-vs-160`\nwent from partially to not reproduced (p 0.0934), the 16 outcomes on\ninterneuron to PC pairs were marked as assumed with a per-pair check, and\nquestions on the fig4c and fig5c criteria and on the onset rules went to a\nreader in `questions/crcns-hc-7.yaml`, written after the answer run, so they\nare unanswered. Round 2 agreed with all 44, found that the fig11 text came from\na different run than the one saved (a tau_f p of 0.0339 where the output\nprinted 0.026, and a test error said to be finite that was infinite), noted\nthat onset rule (b) cannot tell asynchronous release from summation at 160 Hz,\nand counted 21 assumed outcomes where the record marks 16; in reply the fig11\nfits were repeated with three more seeds and the best of 16 starting points,\nwhich kept every fig11 outcome, a sensitivity test of the high KCl assumption\nwas added and the text was corrected. The author's run took about 1.5 h; the\nnotebook ran in 342 s at first, 431 s after the author-answers run, 306 s after\nround 1 and 1378 s after round 2, and nothing failed in the final runs. The\nuntracked entries in the repository root were left alone.\n\nThe current-step recordings of the 67 interneurons (Fig. 2, Tables 1 and 2),\nthe connectivity tests with unconnected pairs (Fig. 3), the spontaneous IPSCs\n(Fig. 12) and the field potential and optogenetic recordings (Fig. 13A, C) are\nnot in the data set, which is described as holding the paired recordings only.\nThe data set holds 7 PV+BC, 8 AAC, 12 CCK+BC and 7 CCK+DTI to PC and 14 PV+BC\nto PV+BC pairs, fewer than the paper's 8, 9, 14, 8 and 16, and the CCK+ to CCK+\npairs were recorded only with 10, 40 and 160 Hz trains, with no RIP recording,\n1 Hz train or 320 Hz train, so their single-AP uIPSCs (Fig. 8) and 320 Hz\ncharges (Fig. 10B) cannot be measured. The pairs are not labelled by pipette\nsolution (high KCl, or low KCl with CsCl), which the comparisons of Fig. 7\nneed; the pair counts do not exceed the paper's high KCl counts, but in CCK+BC\nto PC pairs latency rises with the holding current (rho 0.58, p 0.048), one\nsign against the assumption. The stimulation timings differ from the data\ndescriptor and the paper: RIP bursts are at 222 Hz, not 160 Hz, the EPI burst\nis at 147 and 303 Hz, not 160 and 320 Hz, and the single AP precedes the bursts\nby 1.3 s, not 1 s. The `_EPA` tables use a code AR, not described in the\ndescriptor, that cuts off the mean row of every CCK+BC and CCK+DTI to PC EPI\ntable from some AP on; read as the onset of asynchronous release, it gives a\nCCK+BC median of 12 against the paper's 11, but it was shown only. The block\nthe descriptor calls Relative ampl. holds amplitudes in pA, and the order of\nthe recovery intervals across sweeps is not documented.\n`Experiments_description.txt` mislabels two recordings, names eight files that\nare not in the zip, leaves 20 recordings unnamed, lists no PV+BC to AAC pairs\nand numbers the interneuron to PC pairs differently from the folders. Three\nrecordings have a header but no sweeps, three have sweeps but no `_EPA` table,\ntwo `_EPA` tables hold column labels in place of the mean values, several list\nfewer sweeps than the raw data without a note, and a few mean rows differ from\nthe mean of their own per-sweep values by up to 38 pA. The files carry no\nanimal or slice identifiers. The Results say seven of eight CCK+DTI to PC pairs\ndid not transmit for a single AP or an AP after RIP, and also that four of\neight responded at 1 to 40 Hz or to RIP. Questions are put to the paper's\nauthors: how the onset of asynchronous release was determined and whether the\nAR code marks it; which APs and windows gave the single-AP uIPSCs of the CCK+\ninterneuron pairs; and whether the recovery half-time of Fig. 13B was fitted\nwith the plateau fixed or free, and whether it is tau or tau ln 2.\n\nThe author's points on the protocol: it has no rule for when none of the claims\nfile's readings can be run on the data, so a reading from the paper's protocol\npassage was added and marked assumed; the false-positive rule is written for a\nchance level the paper states, and here was applied by analogy; there is no\nslot for the authors' own scoring inside the data set, so the AR marks were\nshown as a variant only; it does not say what `measured` holds when no reading\nmatches; some criteria are fixed counts of 8 where the data hold 7 pairs, and\neach was judged as written; blocking every claim that depends on a blocked\nclaim takes out fig10 claims whose other parts could have been tested; results\ncannot be broken down by animal without identifiers, so recording days were\nreported; and CRCNS offers no published version to pin, so unversioned and the\nMD5 sum were recorded.\n"
}
```

```
File created successfully at: docs/pilot-notes/crcns-hc-7-kohus-2016-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
d=yaml.safe_load(open('attempts/crcns-hc-7-kohus-2016-01.yaml'))
for o in d['outcomes']:
    dev=' '.join(o.get('deviations',[]))
    if ('pipette' in dev) != bool(o.get('assumed')): print(o['claim'], o.get('assumed'))
E
```

```
(Bash completed with no output)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/crcns-hc-7-kohus-2016-01.md",
 "old_string": "Hz arm was measured after the isolated 11th AP and not the 10th; it also asked\nthat the high KCl assumption be checked. In reply the code was fixed, the onset\nclaims became not reproduced, the three claims blocked, `async-charge-epi-vs-160`",
 "new_string": "Hz arm was measured after the isolated 11th AP and not the 10th, and\n`fig10bd-be-async-charge` lacks only its 320 Hz data; it also asked that the\nhigh KCl assumption be checked. In reply the code was fixed, the onset claims\nbecame not reproduced, the three claims were blocked, fig10bd was blocked for\nmissing data with its other parts printed, `async-charge-epi-vs-160`"
}
```

```
The file docs/pilot-notes/crcns-hc-7-kohus-2016-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/crcns-hc-7-kohus-2016-01.md",
 "content": "The paper's main findings on short-term plasticity largely held up here: uIPSC kinetics and amplitude differ by presynaptic cell type, PV+ interneuron synapses depress more at higher frequencies, and CCK+ synapses facilitate during short bursts. The late onset of asynchronous release at CCK+ synapses did not reproduce, likely because the paper does not describe its onset rule and the rules tried also flag PV+ pairs the paper calls synchronous. CCK+ basket cell to pyramidal cell trains facilitated in only 1 of 6 pairs, and the plasticity models reproduced in part. The interneuron firing clusters, connection probabilities, spontaneous IPSCs and sharp-wave ripple results could not be tested, as those recordings are not in the dataset.\n"
}
```

```
File created successfully at: summaries/crcns-hc-7-kohus-2016-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/crcns-hc-7-kohus-2016-01.md; grep -n -c '—\|rather\|\*\*' docs/pilot-notes/crcns-hc-7-kohus-2016-01.md summaries/crcns-hc-7-kohus-2016-01.md; git status --short
```

```
114 summaries/crcns-hc-7-kohus-2016-01.md
docs/pilot-notes/crcns-hc-7-kohus-2016-01.md:0
summaries/crcns-hc-7-kohus-2016-01.md:0
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
?? docs/pilot-notes/crcns-hc-7-kohus-2016-01.md
?? scripts
?? summaries/crcns-hc-7-kohus-2016-01.md
```

**Agent**

I wrote both files and changed nothing else; nothing is committed. The summary is 114 words in four sentences. The task said to read the hc-7 entry from `targets/dandisets.json`, but it is in `targets/crcns.json`, and its `catalystneuro` field is empty, so the notes don't open with the conversion sentence. The untracked dotfiles and `scripts` in the repository root were already there before this run and I left them alone.

**`docs/pilot-notes/crcns-hc-7-kohus-2016-01.md`**

# crcns-hc-7, Kohus et al. 2016

Ten claims reproduced (seven on an assumption), four partially (three on an assumption), 12 not reproduced (six on an assumption) and 18 blocked, 16 for missing data and two for insufficient metadata. The first verification round agreed with 34 of the 44 outcomes as they stood and the second with all 44; nothing was proposed after the second, so there was no third round. CRCNS does not version data sets, so the version is recorded as unversioned with the data set's DOI (10.6080/K0MK69T5), and the notebook header gives the MD5 sum of `Data.zip`, the only copy in the bucket. The paper, Kohus, Kali, Rovira-Esteban, Schlingloff, Papp, Freund, Hajos and Gulyas in the Journal of Physiology, records pairs of CA3 interneurons and pyramidal cells (PC) in mouse slices, with parvalbumin-expressing basket cells (PV+BC) and axo-axonic cells (AAC) and cholecystokinin-expressing basket cells (CCK+BC) and dendritic-region targeting cells (CCK+DTI) as the presynaptic cells, and compares the kinetics, short-term plasticity and asynchronous release of their uIPSCs under 10-AP trains, ripple-like bursts (RIP) and epileptiform bursts (EPI), fits models of short-term plasticity, and relates PV+BC to PC recovery to the refractoriness of sharp-wave ripples; the data set is one zip of raw paired sweeps and the authors' per-sweep tables (`_EPA`) for 60 pairs in 8 connection types. The claims were written from the version of record, whose text was extracted from the PDF, without the figure images, as the PDF could not be rendered, and without code, as the paper links none; the claims check corrected the Table 4 values and a tolerance, and added `sipsc-continuum`, for 44 claims. The uIPSC properties of Figs. 4 and 8, the plasticity under RIP, trains and recovery (Figs. 5, 6, 9 and 10), the asynchronous release and the models of Fig. 11 could be tested; the firing-pattern clusters of Fig. 2 and Tables 1 and 2, the connection probabilities of Fig. 3, the CsCl comparisons of Fig. 7, the spontaneous IPSCs of Fig. 12 and the field potential and optogenetic results of Fig. 13 could not. Every outcome on interneuron to PC pairs except the CCK+DTI ones rests on the assumption that all were recorded with high KCl. Reproduced are, among others, `fig4b-in-pc-kruskal-wallis` (all five measures differ, latency p 0.00842, though rise and latency no longer differ on the 6 CCK+BC pairs at or below the median holding current, p 0.26 and 0.14), `fig5c-pv-rip-depression`, `fig9-pvbc-pvbc-depression` (Spearman rho -0.737), `fig10-cck-cck-frequency` (medians 1.559 at 10 Hz and 2.153 at 40 Hz), `fig11-model-cck-facilitation`, on a BIC margin of 1.8 under one reading, and `fig13-pvbc-pc-recovery-halftime` (median tau 525.8 ms), which only 3 of 8 fit combinations meet. Partial are `decay-epi-vs-160`, `fig8-pvbc-pvbc-uipsc` (3 of 5 medians within 10%), `fig11-model-pv-udr` (SSE decreases of 22.9, 13.1 and 24.7% against 35, 22 and 34%) and `table4-model-parameters` (8 of 13 values). Not reproduced are, among others, `fig4b-in-pc-posthoc` (4 of 8 comparisons), `fig4c-cckdti-pc-silent-single-ap` (3 of 7 pairs silent; 7 of 7 counting only the first sweep), `fig6-pv-trains-depression` (fails at 1 Hz), `fig6-cckbc-pc-trains` (1 of 6 pairs facilitates at every frequency), `fig9-pvbc-pvbc-transmission-probability`, `fig11c-parameter-differences` and the four onset claims, `fig6-cckbc-async-onset` (CCK+BC EPI median onset 2.0 against 10 to 12), `cckdti-async-onset`, `fig10-cck-cck-heterogeneity` and `fig10-cck-cck-async`, whose two onset rules from the claims file also mark release in the PV+ pairs the paper calls synchronous. The author's first run had 10 reproduced, 5 partially, 10 not reproduced and 19 blocked, with the four onset claims and `fig10bd-be-async-charge` blocked as methods_underspecified. The author asked no questions of a reader, so the answer and author-answers runs changed nothing. Round 1 disagreed on ten claims: the onset claims should be judged on the claims file's two rules, the three claims resting on a reading the claims file does not list (`fig8-cck-pairs-uipsc`, `fig8-cckbc-vs-cckdti-pairs`, `decay-pc-vs-interneuron`) should be blocked, `async-charge-epi-vs-160` and `decay-epi-vs-160` could not be judged, as the 160 Hz arm was measured after the isolated 11th AP and not the 10th, and `fig10bd-be-async-charge` lacks only its 320 Hz data; it also asked that the high KCl assumption be checked. In reply the code was fixed, the onset claims became not reproduced, the three claims were blocked, fig10bd was blocked for missing data with its other parts printed, `async-charge-epi-vs-160` went from partially to not reproduced (p 0.0934), the 16 outcomes on interneuron to PC pairs were marked as assumed with a per-pair check, and questions on the fig4c and fig5c criteria and on the onset rules went to a reader in `questions/crcns-hc-7.yaml`, written after the answer run, so they are unanswered. Round 2 agreed with all 44, found that the fig11 text came from a different run than the one saved (a tau_f p of 0.0339 where the output printed 0.026, and a test error said to be finite that was infinite), noted that onset rule (b) cannot tell asynchronous release from summation at 160 Hz, and counted 21 assumed outcomes where the record marks 16; in reply the fig11 fits were repeated with three more seeds and the best of 16 starting points, which kept every fig11 outcome, a sensitivity test of the high KCl assumption was added and the text was corrected. The author's run took about 1.5 h; the notebook ran in 342 s at first, 431 s after the author-answers run, 306 s after round 1 and 1378 s after round 2, and nothing failed in the final runs. The untracked entries in the repository root were left alone.

The current-step recordings of the 67 interneurons (Fig. 2, Tables 1 and 2), the connectivity tests with unconnected pairs (Fig. 3), the spontaneous IPSCs (Fig. 12) and the field potential and optogenetic recordings (Fig. 13A, C) are not in the data set, which is described as holding the paired recordings only. The data set holds 7 PV+BC, 8 AAC, 12 CCK+BC and 7 CCK+DTI to PC and 14 PV+BC to PV+BC pairs, fewer than the paper's 8, 9, 14, 8 and 16, and the CCK+ to CCK+ pairs were recorded only with 10, 40 and 160 Hz trains, with no RIP recording, 1 Hz train or 320 Hz train, so their single-AP uIPSCs (Fig. 8) and 320 Hz charges (Fig. 10B) cannot be measured. The pairs are not labelled by pipette solution (high KCl, or low KCl with CsCl), which the comparisons of Fig. 7 need; the pair counts do not exceed the paper's high KCl counts, but in CCK+BC to PC pairs latency rises with the holding current (rho 0.58, p 0.048), one sign against the assumption. The stimulation timings differ from the data descriptor and the paper: RIP bursts are at 222 Hz, not 160 Hz, the EPI burst is at 147 and 303 Hz, not 160 and 320 Hz, and the single AP precedes the bursts by 1.3 s, not 1 s. The `_EPA` tables use a code AR, not described in the descriptor, that cuts off the mean row of every CCK+BC and CCK+DTI to PC EPI table from some AP on; read as the onset of asynchronous release, it gives a CCK+BC median of 12 against the paper's 11, but it was shown only. The block the descriptor calls Relative ampl. holds amplitudes in pA, and the order of the recovery intervals across sweeps is not documented. `Experiments_description.txt` mislabels two recordings, names eight files that are not in the zip, leaves 20 recordings unnamed, lists no PV+BC to AAC pairs and numbers the interneuron to PC pairs differently from the folders. Three recordings have a header but no sweeps, three have sweeps but no `_EPA` table, two `_EPA` tables hold column labels in place of the mean values, several list fewer sweeps than the raw data without a note, and a few mean rows differ from the mean of their own per-sweep values by up to 38 pA. The files carry no animal or slice identifiers. The Results say seven of eight CCK+DTI to PC pairs did not transmit for a single AP or an AP after RIP, and also that four of eight responded at 1 to 40 Hz or to RIP. Questions are put to the paper's authors: how the onset of asynchronous release was determined and whether the AR code marks it; which APs and windows gave the single-AP uIPSCs of the CCK+ interneuron pairs; and whether the recovery half-time of Fig. 13B was fitted with the plateau fixed or free, and whether it is tau or tau ln 2.

The author's points on the protocol: it has no rule for when none of the claims file's readings can be run on the data, so a reading from the paper's protocol passage was added and marked assumed; the false-positive rule is written for a chance level the paper states, and here was applied by analogy; there is no slot for the authors' own scoring inside the data set, so the AR marks were shown as a variant only; it does not say what `measured` holds when no reading matches; some criteria are fixed counts of 8 where the data hold 7 pairs, and each was judged as written; blocking every claim that depends on a blocked claim takes out fig10 claims whose other parts could have been tested; results cannot be broken down by animal without identifiers, so recording days were reported; and CRCNS offers no published version to pin, so unversioned and the MD5 sum were recorded.

**`summaries/crcns-hc-7-kohus-2016-01.md`**

The paper's main findings on short-term plasticity largely held up here: uIPSC kinetics and amplitude differ by presynaptic cell type, PV+ interneuron synapses depress more at higher frequencies, and CCK+ synapses facilitate during short bursts. The late onset of asynchronous release at CCK+ synapses did not reproduce, likely because the paper does not describe its onset rule and the rules tried also flag PV+ pairs the paper calls synchronous. CCK+ basket cell to pyramidal cell trains facilitated in only 1 of 6 pairs, and the plasticity models reproduced in part. The interneuron firing clusters, connection probabilities, spontaneous IPSCs and sharp-wave ripple results could not be tested, as those recordings are not in the dataset.

## End of run

29 turns, 3 minutes, $1.51 at API prices, result: success.
