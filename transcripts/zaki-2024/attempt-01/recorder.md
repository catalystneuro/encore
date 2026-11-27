# 000718 · recorder · run 39088718844

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000718 --write; git diff; ls transcripts/000718/ claims/000718/; cat attempts/000718-zaki-2024-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '000718' in json.dumps(x)];print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (218.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a4c01902-d912-4ff4-947b-05e44a495574/tool-results/bluw96hjw.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 0df8428..0851140 100644
--- a/README.md
+++ b/README.md
@@ -85,6 +85,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000552](https://dandiarchive.org/dandiset/000552) | [Huszar et al. 2022](https://doi.org/10.1038/s41593-022-01138-x) | 5 | 4 | 3 | 23 | [`000552-huszar-2022`](entries/000552-huszar-2022) |
 | [000568](https://dandiarchive.org/dandiset/000568) | [Valero et al. 2022](https://doi.org/10.1126/science.abm1891) | 4 | 6 | 6 | 6 | [`000568-valero-2022`](entries/000568-valero-2022) |
 | [000559](https://dandiarchive.org/dandiset/000559) | [Markowitz et al. 2023](https://doi.org/10.1038/s41586-022-05611-2) | 7 | 3 | 2 | 12 | [`000559-markowitz-2023`](entries/000559-markowitz-2023) |
+| [000718](https://dandiarchive.org/dandiset/000718) | [Zaki et al. 2024](https://doi.org/10.1038/s41586-024-08168-4) | 2 (+1) | 0 | 2 | 21 | [`000718-zaki-2024`](entries/000718-zaki-2024) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000718/:
10.1038-s41586-024-08168-4.yaml

transcripts/000718/:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^| Dandiset\|^|---" README.md | head; sed -n 70,84p README.md; grep -n "^### " docs/pilot-notes.md | tail -6; cat attempts/000718-zaki-2024-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else (d['dandisets'] if 'dandisets' in d else list(d.values()))
for x in it:
  if isinstance(x,dict) and str(x.get('id',x.get('dandiset','')))=='000718': print(json.dumps(x,indent=1))
" | head -60
```

```
<persisted-output>
Output too large (41.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a4c01902-d912-4ff4-947b-05e44a495574/tool-results/b9f9k2kpa.txt

Preview (first 2KB):
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50:|---|---|---|---|---|---|---|
| [000044](https://dandiarchive.org/dandiset/000044) | [Grosmark et al. 2016](https://doi.org/10.1126/science.aad1935) | 3 | 3 | 6 | 8 | [`000044-grosmark-2016`](entries/000044-grosmark-2016) |
| [000056](https://dandiarchive.org/dandiset/000056) | [Peyrache et al. 2015](https://doi.org/10.1038/nn.3968) | 6 | 2 | 0 | 13 | [`000056-peyrache-2015`](entries/000056-peyrache-2015) |
| [000059](https://dandiarchive.org/dandiset/000059) | [Petersen et al. 2020](https://doi.org/10.1016/j.neuron.2020.05.023) | 12 | 15 | 10 | 1 | [`000059-petersen-2020`](entries/000059-petersen-2020) |
| [000061](https://dandiarchive.org/dandiset/000061) | [Girardeau et al. 2017](https://doi.org/10.1038/nn.4637) | 4 | 0 | 1 | 1 | [`000061-girardeau-2017`](entries/000061-girardeau-2017) |
| [000067](https://dandiarchive.org/dandiset/000067) | [Fujisawa et al. 2008](https://doi.org/10.1038/nn.2134) | 0 | 5 | 7 | 4 | [`000067-fujisawa-2008`](entries/000067-fujisawa-2008) |
| [000070](https://dandiarchive.org/dandiset/000070) | [Churchland et al. 2012](https://doi.org/10.1038/nature11129) | 5 | 7 | 4 | 6 | [`000070-churchland-2012`](entries/000070-churchland-2012) |
| [000121](https://dandiarchive.org/dandiset/000121) | [Even-Chen et al. 2019](https://doi.org/10.1371/journal.pcbi.1006808) | 6 | 7 | 6 | 1 | [`000121-even-chen-2019`](entries/000121-even-chen-2019) |
| [000114](https://dandiarchive.org/dandiset/000114) | [Carcea et al. 2021](https://doi.org/10.1038/s41586-021-03814-7) | 1 | 3 | 3 | 12 | [`000114-carcea-2021`](entries/000114-carcea-2021) |
| [000213](https://dandiarchive.org/dandiset/000213) | [Tingley et al. 2018](https://doi.
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 84,100p README.md; grep -n "^### \|^## " docs/pilot-notes.md | tail -8; wc -l docs/pilot-notes.md
```

```
| [000409](https://dandiarchive.org/dandiset/000409) | [Ibl et al. 2025](https://doi.org/10.1038/s41586-025-09235-0) | 17 | 3 | 3 | 7 | [`000409-ibl-2025`](entries/000409-ibl-2025) |
| [000552](https://dandiarchive.org/dandiset/000552) | [Huszar et al. 2022](https://doi.org/10.1038/s41593-022-01138-x) | 5 | 4 | 3 | 23 | [`000552-huszar-2022`](entries/000552-huszar-2022) |
| [000568](https://dandiarchive.org/dandiset/000568) | [Valero et al. 2022](https://doi.org/10.1126/science.abm1891) | 4 | 6 | 6 | 6 | [`000568-valero-2022`](entries/000568-valero-2022) |
| [000559](https://dandiarchive.org/dandiset/000559) | [Markowitz et al. 2023](https://doi.org/10.1038/s41586-022-05611-2) | 7 | 3 | 2 | 12 | [`000559-markowitz-2023`](entries/000559-markowitz-2023) |
| [000718](https://dandiarchive.org/dandiset/000718) | [Zaki et al. 2024](https://doi.org/10.1038/s41586-024-08168-4) | 2 (+1) | 0 | 2 | 21 | [`000718-zaki-2024`](entries/000718-zaki-2024) |

Counts are of claims that rest on the dandiset, including those that take
names for its own codes from elsewhere. Claims that also use data from
outside the dandiset are counted apart, in brackets. Claims on data the
paper deposited in other archives are not in this table; the dashboard
shows them on each dandiset's page.

## Agent runs

Attempts by agents are made in GitHub Actions, one role at a time, on the
subscription token in the `CLAUDE_CODE_OAUTH_TOKEN` secret:

2059:### 000226, Severson et al. 2017
2142:### 000232, Chang et al. 2023
2226:### 000239, Xu et al. 2022
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 2310
}
```

```
2310	### 000350, Mu et al. 2019
2311	
2312	Two claims reproduced, three partially, four not reproduced and ten blocked,
2313	all on the dandiset. Round 1 gave its own outcome for each claim from the
2314	notebook with its conclusions removed and agreed with all 19, but gave a
2315	different reason for five blocked claims, and the author changed them:
2316	`fig2dg-nmf-components` to `methods_underspecified` and `fig1k`, `fig1f`,
2317	`fig7-ne-mismatch` and `fig7-glia-accumulate` to `metadata_insufficient`.
2318	Round 2 agreed with all 19 and nothing was proposed, so there was no third
2319	round. The paper reports that larval zebrafish in virtual reality give up
2320	swimming when swims produce no visual feedback, that radial astrocytes
2321	accumulate evidence of this futility and suppress swimming, and that
2322	noradrenergic neurons in NE-MO drive them, with perturbation experiments.
2323	The epoch durations, swim intervals, passivity in open loop, swim vigor
2324	after a switch to open loop, intervals before passivity, the whole-brain
2325	neuronal and glial signals at passivity, in open against closed loop and at
2326	closed-loop pauses were tested. The NMF components are blocked as
2327	`methods_underspecified`, the L-MO and NE-MO claims, the probe, replay and
2328	Figure 7 protocols as `metadata_insufficient`, and the ablation,
2329	activation and noradrenergic experiments as `data_missing`. Some outcomes
[... 434 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/000718-zaki-2024-01.yaml; wc -c claims/000718/* transcripts/000718/*-report.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
def walk(o):
  if isinstance(o,dict):
    if any(str(v)=='000718' for v in o.values()): print(json.dumps(o,indent=1)); return
    for v in o.values(): walk(v)
  elif isinstance(o,list):
    for v in o: walk(v)
walk(d)"
```

```
<persisted-output>
Output too large (39.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a4c01902-d912-4ff4-947b-05e44a495574/tool-results/b9vodjg5h.txt

Preview (first 2KB):
schema_version: 1
id: 000718-zaki-2024-01
dandiset: "000718"
dandiset_version: 0.260825.1902
paper: doi:10.1038/s41586-024-08168-4
date: 2026-10-18
entry: 000718-zaki-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
[... 27 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a4c01902-d912-4ff4-947b-05e44a495574/tool-results/b9vodjg5h.txt"
}
```

```
1	schema_version: 1
2	id: 000718-zaki-2024-01
3	dandiset: "000718"
4	dandiset_version: 0.260825.1902
5	paper: doi:10.1038/s41586-024-08168-4
6	date: 2026-10-18
7	entry: 000718-zaki-2024
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: Per-mouse freezing of Ca_EEG2-1 and Ca_EEG3-4 (ExtendedData9/ExtData9b.csv and ExtData9c.csv), used
18	    as reference values for source-data-link; the per-mouse true and shuffled burst frequency and skew of
19	    Extended Data Figure 3m and 3o (ExtData3m.csv, ExtData3o.csv, another cohort), used as the paper's
20	    chance level for offline-bursts-above-shuffle and as context for offline-skew-above-shuffle; and the
[... 672 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat transcripts/000718/*-report.md; grep -n "with_inputs\|^- id\|  id:" claims/000718/*.yaml | head -40; grep -n "(+[0-9])" README.md | head; grep -n "outside the dandiset\|with outside\|in brackets" docs/pilot-notes.md | head
```

```
<persisted-output>
Output too large (31.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a4c01902-d912-4ff4-947b-05e44a495574/tool-results/bbk327298.txt

Preview (first 2KB):
The attempt on dandiset 000718 is done through step 6 (protocol `pilot-7`). `tools/entry.py check` reports 0 errors, the notebook passes `all` in a clean environment in 81 s, and the handover is built in `executed/000718-zaki-2024/handover/`. I used the full text of the paper, which is open access (PMC11666460, CC BY), saved under `paper/`. Nothing is committed.

## 1. Outcomes (26 claims)

| Claim | Outcome |
|---|---|
| `source-data-link` (uses outside data): the two mice match the paper's per-mouse freezing | reproduced (4 of 4 values within 10%) |
| `ed9b-aversive-freezing-high-vs-low` | reproduced (64.1% against 8.8%, one mouse per group) |
| `offline-bursts-above-shuffle` | blocked, `methods_underspecified` |
| `offline-skew-above-shuffle` | reproduced (3 of 3 recordings above all 1000 surrogates) |
| `burst-locomotion-pause` | not reproduced (telemetry movement proxy) |
| `fig5c-wake-overlap-neutral-coburst` | partially reproduced (holds only with wake as the `wake` label alone; 2 against 1 discordant bursts) |
| 20 other claims (behaviour-only, one-hour offline and single-experience, inhibitory tagging, no-shock, EEG sleep and low-shock) | blocked, `data_missing` |

On the burst claim: under the procedure the criterion fixed, the true burst rate is below the surrogates, which would be "not reproduced". But the paper's own chance level (surrogate/true 0.72 to 0.96, from its source data) is far from mine (1.26 to 1.60), so the protocol's chance-level rule makes it blocked.

[... 7 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a4c01902-d912-4ff4-947b-05e44a495574/tool-results/bbk327298.txt"
}
```

```
1	The attempt on dandiset 000718 is done through step 6 (protocol `pilot-7`). `tools/entry.py check` reports 0 errors, the notebook passes `all` in a clean environment in 81 s, and the handover is built in `executed/000718-zaki-2024/handover/`. I used the full text of the paper, which is open access (PMC11666460, CC BY), saved under `paper/`. Nothing is committed.
2	
3	## 1. Outcomes (26 claims)
4	
5	| Claim | Outcome |
6	|---|---|
7	| `source-data-link` (uses outside data): the two mice match the paper's per-mouse freezing | reproduced (4 of 4 values within 10%) |
8	| `ed9b-aversive-freezing-high-vs-low` | reproduced (64.1% against 8.8%, one mouse per group) |
9	| `offline-bursts-above-shuffle` | blocked, `methods_underspecified` |
10	| `offline-skew-above-shuffle` | reproduced (3 of 3 recordings above all 1000 surrogates) |
11	| `burst-locomotion-pause` | not reproduced (telemetry movement proxy) |
12	| `fig5c-wake-overlap-neutral-coburst` | partially reproduced (holds only with wake as the `wake` label alone; 2 against 1 discordant bursts) |
13	| 20 other claims (behaviour-only, one-hour offline and single-experience, inhibitory tagging, no-shock, EEG sleep and low-shock) | blocked, `data_missing` |
14	
15	On the burst claim: under the procedure the criterion fixed, the true burst rate is below the surrogates, which would be "not reproduced". But the paper's own chance level (surrogate/true 0.72 to 0.96, from its source data) is far from mine (1.26 to 1.60), so the protocol's chance-level rule makes it blocked.
16	
17	## 2. What was found about the dandiset
18	
19	- **Coverage:** it holds 2 of the 9 mice of the EEG/EMG experiment: Ca_EEG2-1 (1.5 mA, high shock) and Ca_EEG3-4 (0.25 mA, low shock). Of each offline period only the first 10 min recording of 24 is there. Ca_EEG2-1 has no neutral or novel recall session and no offline-day-1 recording.
20	- **Missing cohorts:** none of the mice behind Figures 2 to 4 and 6 or the behaviour-only experiments are deposited.
[... 233 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 2059,2064p docs/pilot-notes.md; grep -n "plus one\|one more that uses\|uses outside data\|with outside data" docs/pilot-notes.md | head; sed -n 1,40p claims/000718/*.yaml
```

```
### 000226, Severson et al. 2017

Twelve claims reproduced, two partially and eleven blocked on the dandiset.
With outside data, counted apart: two reproduced and one partially. Round 1
gave its own outcome for each claim from the notebook with its conclusions
removed and agreed with all 28; round 2 agreed again and nothing was
581:dandiset with outside data cannot say which of them failed. So:
584:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
940:on the dandiset, plus one claim using outside data, not reproduced; both
1031:plus one claim linking the dandiset to the paper's Zenodo deposit,
# Claims for Zaki et al. (2024), "Offline ensemble co-reactivation links memories across days",
# Nature 637, 145-155 (issue of January 2025, published online 6 November 2024), on dandiset 000718.
# Source: the full text, open access under CC BY (PMC11666460), read from its Results, figure and
# Extended Data legends and Methods.
#
# When these criteria were written, the author had seen the data check only: the file list and
# metadata of version 0.260825.1902, the contents of every NWB file, the ranges and timestamps of
# the deconvolved traces, the sleep-state intervals of the three offline sessions (wake and quiet
# wake only), the cell registration tables of mouse Ca_EEG2-1 and the sizes of the four ensembles
# they give for its offline session (97 neutral, 80 aversive, 166 overlap, 282 remaining), the
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A3 "statement:" claims/000718/*.yaml | head -120
```

```
40:  statement: The two deposited mice are the mice of the same names in the paper's per-mouse source
41-    data, with the same shock group, and the freezing computed from the dandiset's freezing intervals
42-    agrees with the per-mouse freezing the paper reports for them.
43-  source: Extended Data Figure 9b and 9c; source-data repository denisecailab/RetrospectiveMemoryLinkingData_2024
--
70:  statement: In the calcium imaging and EEG/EMG experiment, high-shock mice froze more during
71-    aversive recall than low-shock mice (t7 = 8.99, p = 0.020).
72-  source: Extended Data Figure 9b
73-  criterion: The dandiset holds one mouse per group, so the paper's t-test cannot be run. Freezing
--
79:  statement: During offline periods, hippocampal population bursts occur more often than expected
80-    from shuffled neuronal activity, so CA1 neurons fire in a more coordinated way than chance.
81-  source: Results, section "Neutral ensemble recruited into population bursts"; Extended Data Figure 3l and 3m
82-  criterion: In each of the three deposited offline recordings, burst frequency (events per minute)
--
89:  statement: The mean population activity during offline periods is more right-skewed than in
90-    shuffled data, showing brief burst-like activations that need coordinated activity of groups of
91-    neurons.
92-  source: Extended Data Figure 3n and 3o
--
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd  tail -c 200 docs/pilot-notes.md | od -c | tail -3
```

```
0000260   o   v   e   r       t   h   e       1   0   -   m   i   n   u
0000300   t   e       a   i   m   .  \n
0000310
```

**Agent calls Bash**

```bash
cd  cat >> docs/pilot-notes.md <<'EOF'

### 000718, Zaki et al. 2024

Two claims reproduced, two not reproduced and twenty-one blocked on the
dandiset. With outside data, counted apart: one reproduced. Round 1 gave its
own outcome for each claim from the notebook with its conclusions removed and
agreed with 25 of the 26; it gave not reproduced for
`offline-bursts-above-shuffle`, as the criterion is written, and suggested
blocking it as `methods_underspecified`, which the record already did, as
round 1 had not seen the record. Round 1 agreed that
`fig5c-wake-overlap-neutral-coburst` was partially reproduced by the letter of
the criterion, but argued that the Methods' scoring has no quiet-wake class;
applied to Ca_EEG2-1's EMG it puts 94.1% of quiet-wake frames and all 87
bursts in wake, and under that reading the overlap ensemble co-bursts less
with the neutral than with the aversive ensemble (26.4 against 35.6%, McNemar
p = 0.13), so the author changed the claim to not reproduced and recorded the
departure from the criterion as a deviation. Round 2 agreed with all 26 and
nothing was proposed, so there was no third round. The paper reports that a
strong aversive experience links fear to a neutral context experienced two
days before, that neutral and aversive ensembles in CA1 co-reactivate in
offline population bursts, mostly during wake, and that this co-bursting of
the overlap ensemble with the neutral ensemble goes with the linking. The link
to the paper's per-mouse source data, aversive freezing of the high- against
the low-shock mouse, bursts and skew against shuffled data, the pause in
movement before bursts and wake co-bursting were tested, the last four on the
EEG/EMG cohort where the paper shows three of them in another cohort. The
bursts claim is blocked as `methods_underspecified`, since surrogate over true
burst rate is 1.26 to 1.60 against the paper's 0.72 to 0.96, and a synthetic
control shows the criterion's test cannot detect coordination (5.6 true
against 34.98 surrogate bursts per min); the other 20 blocked claims are
`data_missing`. Some outcomes rest on weak ground:
`ed9b-aversive-freezing-high-vs-low` compares one mouse per group over 30 s
bins that are not independent; in `offline-skew-above-shuffle` both arms are
below the paper's Extended Data Figure 3o values, so the chance level is not
shown to match the paper's; `burst-locomotion-pause` uses the telemetry
activity signal as a proxy for the paper's webcam tracking, and the test gives
p = 0.016 at 300 random times in Ca_EEG2-1; and
`fig5c-wake-overlap-neutral-coburst` rests on one 10 min recording of one
mouse, z-scored within it, and on a log EMG RMS measure chosen after the data
were seen. The author used the open access full text (PMC11666460).

The dandiset was converted by CatalystNeuro (catalystneuro/cai-lab-to-nwb). It
holds two of the nine mice of the calcium imaging and EEG/EMG experiment
(Ca_EEG2-1, high shock; Ca_EEG3-4, low shock) and, of each offline period,
only the first 10 min recording of the 24 the Methods describe; Ca_EEG2-1 has
no offline-day-1 recording and no neutral or novel recall session, and the
mice of the one-hour imaging and offline experiments, the behaviour-only
experiments and the inhibitory tagging and no-shock experiments are not
deposited, so twenty of the 26 claims cannot be tested. Ca_EEG3-4 has no cell
registration, so its ensembles cannot be formed, and the Week file of
Ca_EEG2-1 holds 19 registration tables for offline-day-2 recordings, of which
only the first recording is deposited, and none for offline day 1. The
dandiset does not say why these two mice and only the first offline recording
of each period were deposited, nor that the paper analysed more. The session
start times of the Ca_EEG2-1 behaviour sessions, and the Week epochs built
from them, are about 1 h later than the telemetry and Miniscope clock, so that
OfflineDay2Session1 starts 47 min before the FC session it follows; the
telemetry is absent in windows that contain each of these epochs moved 1 h
earlier. Other findings: the OnePhotonSeries timestamps of three files run at
16.7 ms and end at half the recording's length, while their frame counts fit
30 Hz over the full length; the sleep states include `quiet wake`, which the
paper neither uses nor maps to its states, and the three offline recordings
hold no NREM or REM epochs; the telemetry is sampled at 500 Hz where the
Methods say 100 Hz; the offline session description speaks of an hour of
recording with a webcam, where the deposited recordings last 10 min and hold
telemetry and no video; the fluorescence series carry placeholder
descriptions and unit "n.a.", the FC session descriptions give the shock
amplitude without a unit, and the Week file has an empty session
description; and the analysis code repository the paper names returns 404.
The registration tables agree with the ROI centroids, no recording is
deposited twice, and calcium, behaviour and telemetry are consistent with a
shared clock except in Ca_EEG3-4 offline day 1, where it could not be
established.

The notebook ran in 81 s in the first clean run, and `tools/entry.py all`
took about 2 minutes after round 1. `git clone` from GitHub asked for
credentials, so the source-data and conversion repositories were fetched as
tarballs at pinned commits; removing `__pycache__` and an empty `.claude/`
directory in the entry was denied, and untracked files in the repository root
that the author did not create were left alone. Round 2 found sentences the
outputs did not support, among them that the skew values lie in the range of
the paper's, and a wrong grouping of `fig1ef` and `fig1g`, and these were
corrected. The author's points on the protocol: general claims shown only in a
cohort that is not deposited; a chance level the paper states only in its
source data, for another cohort at another frame rate; whether the lab's
repository of per-mouse figure values counts as data deposited elsewhere; a
link claim on which no claim depends; across-mouse claims with one mouse per
group; a clock check that covers streams within a session but not start times
across sessions; a value seen in the data check before the criteria were
written; and which year to use in the entry name for a paper online in 2024
and in an issue of 2025.
EOF
git status --short
```

```
M README.md
 M docs/pilot-notes.md
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
?? scripts
```

**Agent**

I ran `tools/readme_row.py 000718 --write`, which added the row `2 (+1) | 0 | 2 | 21` to README.md, and appended the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed.

### 000718, Zaki et al. 2024

Two claims reproduced, two not reproduced and twenty-one blocked on the
dandiset. With outside data, counted apart: one reproduced. Round 1 gave its
own outcome for each claim from the notebook with its conclusions removed and
agreed with 25 of the 26; it gave not reproduced for
`offline-bursts-above-shuffle`, as the criterion is written, and suggested
blocking it as `methods_underspecified`, which the record already did, as
round 1 had not seen the record. Round 1 agreed that
`fig5c-wake-overlap-neutral-coburst` was partially reproduced by the letter of
the criterion, but argued that the Methods' scoring has no quiet-wake class;
applied to Ca_EEG2-1's EMG it puts 94.1% of quiet-wake frames and all 87
bursts in wake, and under that reading the overlap ensemble co-bursts less
with the neutral than with the aversive ensemble (26.4 against 35.6%, McNemar
p = 0.13), so the author changed the claim to not reproduced and recorded the
departure from the criterion as a deviation. Round 2 agreed with all 26 and
nothing was proposed, so there was no third round. The paper reports that a
strong aversive experience links fear to a neutral context experienced two
days before, that neutral and aversive ensembles in CA1 co-reactivate in
offline population bursts, mostly during wake, and that this co-bursting of
the overlap ensemble with the neutral ensemble goes with the linking. The link
to the paper's per-mouse source data, aversive freezing of the high- against
the low-shock mouse, bursts and skew against shuffled data, the pause in
movement before bursts and wake co-bursting were tested, the last four on the
EEG/EMG cohort where the paper shows three of them in another cohort. The
bursts claim is blocked as `methods_underspecified`, since surrogate over true
burst rate is 1.26 to 1.60 against the paper's 0.72 to 0.96, and a synthetic
control shows the criterion's test cannot detect coordination (5.6 true
against 34.98 surrogate bursts per min); the other 20 blocked claims are
`data_missing`. Some outcomes rest on weak ground:
`ed9b-aversive-freezing-high-vs-low` compares one mouse per group over 30 s
bins that are not independent; in `offline-skew-above-shuffle` both arms are
below the paper's Extended Data Figure 3o values, so the chance level is not
shown to match the paper's; `burst-locomotion-pause` uses the telemetry
activity signal as a proxy for the paper's webcam tracking, and the test gives
p = 0.016 at 300 random times in Ca_EEG2-1; and
`fig5c-wake-overlap-neutral-coburst` rests on one 10 min recording of one
mouse, z-scored within it, and on a log EMG RMS measure chosen after the data
were seen. The author used the open access full text (PMC11666460).

The dandiset was converted by CatalystNeuro (catalystneuro/cai-lab-to-nwb). It
holds two of the nine mice of the calcium imaging and EEG/EMG experiment
(Ca_EEG2-1, high shock; Ca_EEG3-4, low shock) and, of each offline period,
only the first 10 min recording of the 24 the Methods describe; Ca_EEG2-1 has
no offline-day-1 recording and no neutral or novel recall session, and the
mice of the one-hour imaging and offline experiments, the behaviour-only
experiments and the inhibitory tagging and no-shock experiments are not
deposited, so twenty of the 26 claims cannot be tested. Ca_EEG3-4 has no cell
registration, so its ensembles cannot be formed, and the Week file of
Ca_EEG2-1 holds 19 registration tables for offline-day-2 recordings, of which
only the first recording is deposited, and none for offline day 1. The
dandiset does not say why these two mice and only the first offline recording
of each period were deposited, nor that the paper analysed more. The session
start times of the Ca_EEG2-1 behaviour sessions, and the Week epochs built
from them, are about 1 h later than the telemetry and Miniscope clock, so that
OfflineDay2Session1 starts 47 min before the FC session it follows; the
telemetry is absent in windows that contain each of these epochs moved 1 h
earlier. Other findings: the OnePhotonSeries timestamps of three files run at
16.7 ms and end at half the recording's length, while their frame counts fit
30 Hz over the full length; the sleep states include `quiet wake`, which the
paper neither uses nor maps to its states, and the three offline recordings
hold no NREM or REM epochs; the telemetry is sampled at 500 Hz where the
Methods say 100 Hz; the offline session description speaks of an hour of
recording with a webcam, where the deposited recordings last 10 min and hold
telemetry and no video; the fluorescence series carry placeholder
descriptions and unit "n.a.", the FC session descriptions give the shock
amplitude without a unit, and the Week file has an empty session
description; and the analysis code repository the paper names returns 404.
The registration tables agree with the ROI centroids, no recording is
deposited twice, and calcium, behaviour and telemetry are consistent with a
shared clock except in Ca_EEG3-4 offline day 1, where it could not be
established.

The notebook ran in 81 s in the first clean run, and `tools/entry.py all`
took about 2 minutes after round 1. `git clone` from GitHub asked for
credentials, so the source-data and conversion repositories were fetched as
tarballs at pinned commits; removing `__pycache__` and an empty `.claude/`
directory in the entry was denied, and untracked files in the repository root
that the author did not create were left alone. Round 2 found sentences the
outputs did not support, among them that the skew values lie in the range of
the paper's, and a wrong grouping of `fig1ef` and `fig1g`, and these were
corrected. The author's points on the protocol: general claims shown only in a
cohort that is not deposited; a chance level the paper states only in its
source data, for another cohort at another frame rate; whether the lab's
repository of per-mouse figure values counts as data deposited elsewhere; a
link claim on which no claim depends; across-mouse claims with one mouse per
group; a clock check that covers streams within a session but not start times
across sessions; a value seen in the data check before the criteria were
written; and which year to use in the entry name for a paper online in 2024
and in an issue of 2025.

## End of run

13 turns, 1 minutes, result: success.
