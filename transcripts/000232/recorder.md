# 000232 · recorder · run 39017436402

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000232 --write; git diff; ls claims/000232 transcripts/000232; cat attempts/000232-chang-2023-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));d=d if isinstance(d,list) else d.get('dandisets',d);print([x for x in (d if isinstance(d,list) else d.values()) if '000232' in json.dumps(x)])"
```

```
<persisted-output>
Output too large (198.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/5857a2ba-8373-44c0-9fe1-018acde8b355/tool-results/b2s3a654s.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 2b30051..54931c4 100644
--- a/README.md
+++ b/README.md
@@ -78,6 +78,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000213](https://dandiarchive.org/dandiset/000213) | [Tingley et al. 2018](https://doi.org/10.1016/j.neuron.2018.04.028) | 3 | 8 | 9 | 5 | [`000213-tingley-2018`](entries/000213-tingley-2018) |
 | [000218](https://dandiarchive.org/dandiset/000218) | [Tingley et al. 2019](https://doi.org/10.1016/j.neuron.2019.10.012) | 4 | 7 | 10 | 10 | [`000218-tingley-2019`](entries/000218-tingley-2019) |
 | [000226](https://dandiarchive.org/dandiset/000226) | [Severson et al. 2017](https://doi.org/10.1016/j.neuron.2017.03.045) | 12 (+2) | 2 (+1) | 0 | 11 | [`000226-severson-2017`](entries/000226-severson-2017) |
+| [000232](https://dandiarchive.org/dandiset/000232) | [Chang et al. 2023](https://doi.org/10.1101/2023.08.21.554194) | 19 | 7 | 2 | 1 | [`000232-chang-2023`](entries/000232-chang-2023) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000232:
10.1101-2023.08.21.554194.yaml

transcripts/000232:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000232-chang-2023-01.yaml; grep -n "^| Dandiset\|^|---" README.md | head; sed -n 60,70p README.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
import sys
s=json.dumps(d)
items=d if isinstance(d,list) else d.get('dandisets', list(d.values()))
for x in items:
  if '000232' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (218.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/5857a2ba-8373-44c0-9fe1-018acde8b355/tool-results/b3zecrdc4.txt

Preview (first 2KB):
schema_version: 1
id: 000232-chang-2023-01
dandiset: "000232"
dandiset_version: 0.240510.2038
paper: doi:10.1101/2023.08.21.554194
date: 2026-10-17
entry: 000232-chang-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l attempts/000232-chang-2023-01.yaml transcripts/000232/*-report.md docs/pilot-notes.md; sed -n 1,60p README.md | grep -n "^|" ; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets', d)
if isinstance(items,dict): items=list(items.values())
for x in items:
  if isinstance(x,dict) and str(x.get('id',x.get('dandiset','')))=='000232': print(json.dumps(x,indent=1))
E
```

```
777 attempts/000232-chang-2023-01.yaml
    69 transcripts/000232/author-report.md
    33 transcripts/000232/author-revise-1-report.md
    23 transcripts/000232/author-revise-2-report.md
    72 transcripts/000232/verifier-1-report.md
    83 transcripts/000232/verifier-2-report.md
  2140 docs/pilot-notes.md
  3197 total
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50:|---|---|---|---|---|---|---|
51:| [000582](https://dandiarchive.org/dandiset/000582) | [Sargolini et al. 2006](https://doi.org/10.1126/science.1125572) | 2 | 1 | 0 | 0 | [`000582-sargolini-2006`](entries/000582-sargolini-2006) |
52:| [000127](https://dandiarchive.org/dandiset/000127) | [Chowdhury et al. 2020](https://doi.org/10.7554/eLife.48198) | 4 | 2 | 0 | 4 | [`000127-chowdhury-2020`](entries/000127-chowdhury-2020) |
53:| [000207](https://dandiarchive.org/dandiset/000207) | [Zheng et al. 2022](https://doi.org/10.1038/s41593-022-01020-w) | 5 | 1 | 0 | 14 | [`000207-zheng-2022`](entries/000207-zheng-2022) |
54:| [000147](https://dandiarchive.org/dandiset/000147) | [Guan et al. 2022](https://doi.org/10.7554/eLife.74478) | 9 (+3) | 0 | 1 | 4 (+3) | [`000147-guan-2022`](entries/000147-guan-2022) |
55:| [001097](https://dandiarchive.org/dandiset/001097) | [Liu et al. 2024](https://doi.org/10.1038/s41586-024-07916-w) | 7 | 2 | 3 | 12 | [`001097-liu-2024`](entries/001097-liu-2024) |
56:| [000625](https://dandiarchive.org/dandiset/000625) | [Geiller et al. 2020](https://doi.org/10.1016/j.neuron.2020.09.013) | 4 | 4 | 6 | 12 | [`000625-geiller-2020`](entries/000625-geiller-2020) |
57:| [000035](https://dandiarchive.org/dandiset/000035) | [Scala et al. 2021](https://doi.org/10.1038/s41586-020-2907-3) | 3 (+2) | 1 (+1) | 0 | 9 (+1) | [`000035-scala-2021`](entries/000035-scala-2021) |
58:| [001453](https://dandiarchive.org/dandiset/001453) | [Fouke et al. 2025](https://doi.org/10.1016/j.cub.2025.04.027) | 7 | 1 | 2 | 10 | [`001453-fouke-2025`](entries/001453-fouke-2025) |
59
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "000232" targets/dandisets.json | head; grep -n "^### " docs/pilot-notes.md | tail -6
```

```
1650:   "dandiset": "000232",
1670:### 000070, Churchland et al. 2012
1743:### 000121, Even-Chen et al. 2019
1817:### 000114, Carcea et al. 2021
1890:### 000213, Tingley et al. 2018
1975:### 000218, Tingley et al. 2019
2059:### 000226, Severson et al. 2017
```

**Agent calls Bash**

```bash
sed -n 1640,1680p targets/dandisets.json; sed -n 1743,2140p docs/pilot-notes.md
```

```
"doi": "10.1101/2022.05.10.491259",
     "title": "A detailed behavioral, videographic, and neural dataset on object recognition in mice",
     "relation": "Describes",
     "resource_type": null,
     "preprint": true
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000232",
   "name": "Rule-based modulation of a sensorimotor transformation across cortical areas",
   "published_version": "0.240510.2038",
   "asset_count": 179,
   "size_gb": 23.59,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Mus musculus - House mouse"
[... 419 more lines not kept]
```

**Agent**

README row written (19 reproduced, 7 partially, 2 not reproduced, 1 blocked). Now reading the reports and the attempt record.

**Agent calls Bash**

```bash
cd transcripts/000232; cat author-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md
```

```
<persisted-output>
Output too large (30KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/5857a2ba-8373-44c0-9fe1-018acde8b355/tool-results/bsg05xbg5.txt

Preview (first 2KB):
I've done steps 1 to 6 for dandiset 000232: the entry is locked, checked and runs cleanly from a fresh environment, and the verifier's package is built in `executed/000232-chang-2023/handover/`. Nothing is committed or pushed. The notebook runs in 14.3 minutes (867 s), and the run gave the same numbers as the earlier test run.

**Paper text.** I used the full text of preprint version 2, which is open access (CC-BY). bioRxiv refused the download (rate-limit error 1015), so I took the same text from eLife's copy of the reviewed preprint (92620v2), whose source is bioRxiv v2. It is saved under `paper/`. Table 1 and the table of coding-dimension trial types are images there and were not read.

**Version.** I pinned 0.240510.2038, the only published version. The preprint cites no version ("available upon request"); the paper's code repository cites this one. The draft has identical files and differs only in contributor metadata.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1e-recording-counts | reproduced |
| fig6-session-counts | reproduced |
| fig1d-performance | reproduced (73.6 / 74.8%, p = 0.561 against the paper's 0.56) |
| fig1d-outcome-fractions | reproduced |
| fig1h-thit-tcr-selective | partially reproduced (MM 36.4% against 32.9%) |
| fig2c-rule-prestim-units | partially reproduced (S1 5.6% against 4.5%) |
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/5857a2ba-8373-44c0-9fe1-018acde8b355/tool-results/bsg05xbg5.txt"
}
```

```
1	I've done steps 1 to 6 for dandiset 000232: the entry is locked, checked and runs cleanly from a fresh environment, and the verifier's package is built in `executed/000232-chang-2023/handover/`. Nothing is committed or pushed. The notebook runs in 14.3 minutes (867 s), and the run gave the same numbers as the earlier test run.
2	
3	**Paper text.** I used the full text of preprint version 2, which is open access (CC-BY). bioRxiv refused the download (rate-limit error 1015), so I took the same text from eLife's copy of the reviewed preprint (92620v2), whose source is bioRxiv v2. It is saved under `paper/`. Table 1 and the table of coding-dimension trial types are images there and were not read.
4	
5	**Version.** I pinned 0.240510.2038, the only published version. The preprint cites no version ("available upon request"); the paper's code repository cites this one. The draft has identical files and differs only in contributor metadata.
6	
7	## 1. Outcomes
8	
9	| Claim | Outcome |
10	|---|---|
11	| fig1e-recording-counts | reproduced |
12	| fig6-session-counts | reproduced |
13	| fig1d-performance | reproduced (73.6 / 74.8%, p = 0.561 against the paper's 0.56) |
14	| fig1d-outcome-fractions | reproduced |
15	| fig1h-thit-tcr-selective | partially reproduced (MM 36.4% against 32.9%) |
16	| fig2c-rule-prestim-units | partially reproduced (S1 5.6% against 4.5%) |
17	| fig2d-stimulus-prestim-units | reproduced |
18	| fig2e-stimulus-poststim-units | reproduced |
19	| fig2f-prestim-predicts-touch-response | reproduced |
20	| fig3b-rule-decoding | reproduced |
[... 261 more lines not kept]
```

**Agent**

Now the record's findings and verification sections.

**Agent calls Bash**

```bash
cd  grep -n "^[a-z_]*:" attempts/000232-chang-2023-01.yaml; python - <<'E'
import yaml
d=yaml.safe_load(open('attempts/000232-chang-2023-01.yaml'))
for k in d:
  if k not in ('outcomes','verifications','inputs','provenance'): print(k, yaml.safe_dump(d[k],width=200,allow_unicode=True))
for v in d.get('verifications',[]):
  print({k:v[k] for k in v if k!='claims' and k!='outcomes'})
E
grep -n "paper\|title\|text" claims/000232/*.yaml | head -20
```

```
1:schema_version: 1
2:id: 000232-chang-2023-01
3:dandiset: "000232"
4:dandiset_version: 0.240510.2038
5:paper: doi:10.1101/2023.08.21.554194
6:date: 2026-10-17
7:entry: 000232-chang-2023
8:provenance:
16:inputs:
21:outcomes:
299:findings:
353:verifications:
schema_version 1
...

id 000232-chang-2023-01
...

dandiset '000232'

[... 63 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000232/10.1101-2023.08.21.554194.yaml",
 "limit": 60
}
```

```
1	# Claims for Chang, Finkel, Xu & O'Connor, "Rule-based modulation of a sensorimotor transformation
2	# across cortical areas", bioRxiv preprint doi:10.1101/2023.08.21.554194, on dandiset 000232.
3	# Source: the full text of preprint version 2 (posted 2024-03-09, CC-BY), read from the copy
4	# eLife serves for its reviewed preprint 92620v2, whose source is bioRxiv version 2; bioRxiv
5	# itself refused the download. Results, figure legends and Methods were read. Table 1 and the
6	# table of coding-dimension trial types are images in that copy and were not read.
7	#
8	# When these criteria were written, the author had seen the data check only: the file list and
9	# metadata, the contents of one ephys file and one file of each optogenetic task, and per file
10	# the area, subject, number of units, number of trials, block and trial types, the coding of
11	# the response column against lick times, and the absence of trials with licks between -1 and
12	# 0.1 s of the stimulus. The counts of sessions, mice and units per area and of optogenetic
13	# sessions per condition had been seen (claims fig1e-recording-counts and fig6-session-counts).
14	# No other claim's analysis had been run. The author had read the paper's analysis code
15	# (github.com/YitingChang/cross_modal_task, commit 227631e), and the method choices below follow
16	# it where the Methods are silent.
17	#
18	# Common choices: a session's trials are those in the file, without cue ("Change") trials;
19	# a correct trial is a tactile hit (respond-to-touch block, tactile stimulus, right lick),
20	# visual correct rejection (touch block, visual stimulus, no lick), tactile correct rejection
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import yaml
d=yaml.safe_load(open('claims/000232/10.1101-2023.08.21.554194.yaml'))
for c in d['claims']: print(c['id'],'|',c['statement'][:260])
E
```

```
fig1e-recording-counts | Single units were recorded with 64-channel probes in S1 (6 mice, 10 sessions, 177 neurons), S2 (5 mice, 8 sessions, 162 neurons), MM (7 mice, 9 sessions, 140 neurons) and ALM (8 mice, 13 sessions, 256 neurons), one area per session, and in AMM (110 neurons).
fig6-session-counts | The optogenetic experiments in the cross-modal task comprise S1/S2 (4 mice, 10 sessions), MM (4, 11), ALM (4, 10), sham (7, 28), AMM (7, 21) and PPC (7, 21); in the tactile detection task sham (5, 9), S1/S2 (3, 3), MM (3, 5), ALM (3, 4), AMM (3, 4) and PPC (3,
fig1d-performance | Performance was about 75% correct under both rules (respond-to-touch 74 plus or minus 1%, respond-to-light 75 plus or minus 1%, mean and SEM over 12 mice), with no difference between them (paired t-test, p = 0.56).
fig1d-outcome-fractions | The fractions of trial outcomes were similar under the two rules (touch against light; hit 36 against 35%, correct rejection 38 against 40%, miss 13 against 14%, false alarm 13 against 12%).
fig1h-thit-tcr-selective | 18 to 33% of neurons discriminate tactile hits from tactile correct rejections in the first 150 ms after the stimulus (S1 28.8%, S2 17.9%, MM 32.9%, ALM 23.4%), and most of these respond more in tactile hits (AUC above 0.5).
fig2c-rule-prestim-units | Before the stimulus (-100 to 0 ms), fewer than 5% of neurons in S1 and S2 discriminate the rule, while about 10 to 20% do in MM and ALM (S1 4.5%, S2 2.5%, MM 21.4%, ALM 10.2%).
fig2d-stimulus-prestim-units | As a negative control, almost no neuron discriminates tactile from visual trials before the stimulus (S1 0%, S2 0%, MM 0%, ALM 0.8%).
fig2e-stimulus-poststim-units | After the stimulus (0 to 100 ms), more than 35% of neurons in S1 and S2 and about 15% in MM and ALM discriminate tactile from visual trials (S1 37.3%, S2 35.2%, MM 15%, ALM 14.1%).
fig2f-prestim-predicts-touch-response | Among neurons with significant rule discrimination before the stimulus, the pre-stimulus rule preference pr
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'E'

### 000232, Chang et al. 2023

Nineteen claims reproduced, seven partially, two not reproduced and one
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 28 of the 29;
it gave not reproduced for `fig5b-first-hit-switches`, where both block counts
fail, and the author changed that claim from partially reproduced to not
reproduced, as the criterion allows a partial outcome only when one condition
fails. Round 2 agreed with all 29 and nothing was proposed, so there was no
third round. The paper reports that in mice switching between a
respond-to-touch and a respond-to-light rule, neurons and populations in MM
and ALM encode the rule before the stimulus more than those in S1 and S2,
that this pre-stimulus state shapes the touch response and tracks rule
switches, and that inhibiting MM or ALM before the stimulus lowers tactile
sensitivity. The recording and optogenetic session counts, task performance,
the fractions of selective neurons, rule and stimulus decoding with LDA, SVMs
and random forests, trajectory distances, subspace overlap, coding
dimensions, the first hits after a switch, state tracking across transitions
and the optogenetic effects on sensitivity, hit rate and laser-only licks were
tested; the claim on the histological probe locations is blocked as
`data_missing`. Some outcomes rest on weak ground: `fig1h-thit-tcr-selective`
and `fig2c-rule-prestim-units` are judged on the main seed, and on the means
over five seeds all four areas of both would be within tolerance, while on
single seeds fig1h MM is within tolerance in 3 of 5 and fig2c S1 in none; in
`fig6c-pre-inhibition-tactile` the ALM upper bound is 0.005, averages -0.001
(SD 0.003) over ten other seeds and is below 0 in 7 of 10, and the code's
resampling gives the paper's interval; `fig4c-prestim-distance-predicts-divergence`
gives p = 0.004 with the Methods' normalization and p = 0.001 with the
code's, and the units of the offset are not stated; in
`figs4h-choice-right-left` S2 is 0.422 against 0.32 and within tolerance in 1
of 5 seeds; the absence in `figs5-sensory-states-no-tracking` rests on wide
intervals; and in `fig6ij-laser-only-licks` the one failing interval, detection
task, MM, short laser, [0.045, 0.483], excludes 0 in all ten other seeds, but
the paper's detection intervals match none of the short, long or pooled rows.
The author read the full text of preprint version 2 from eLife's copy of the
reviewed preprint, as bioRxiv refused the download, and read the paper's
analysis code at commit 227631e for method choices the Methods leave open,
taking no data from it.

The dandiset was converted by CatalystNeuro (Luiz Tauffer and Benjamin
Dichter of CatalystNeuro are contributors). Sessions, mice and units per area
match the paper exactly, as do all 24 optogenetic session and mouse counts,
but the ephys files hold only the trials and units the paper analysed: no
trial has a lick between -1 and 0.1 s of the stimulus, gaps of 8 to 64 per
session remain in the trial times, the units are those passing the quality
filter and the 50 Hz cut, and the dandiset does not say that trials or units
were removed. Units carry only spike times and observation intervals, with no
quality metrics, waveforms, channel or depth, and ids that run from 0, so
units the paper names by cluster number cannot be identified; electrode x, y
and z are NaN in all 49 ephys files, locations are "unknown", and the
histology of Figure 1E is not deposited. The trials table columns have no
descriptions, and `response`, `blockType` ("Change" for the cue trial), the
opto trial types and the indicator columns are explained only by the paper's
code. In the 130 behaviour files `start_time` equals the stimulus onset, so
trial intervals overlap, and in the tactile detection files trials without a
whisker stimulus are labelled "Stim_Vis" and "Stim_Vis_NoCue" with a visual
stimulus type. Figure 5B's 88 and 91 switches equal the touch and light
blocks of the 40 recording sessions when each session's first block is
counted, against 63 and 75 non-first blocks with a hit. Other findings: the
Methods' soft normalization differs from the code's in each population
analysis, and the Methods exclude sessions with fewer than ten units from the
subspace analysis where the code requires more than ten; the code's
optogenetic bootstrap resamples only hits; the coding-dimension code keeps 8,
7, 5 and 11 sessions where Figure S4 reports 10, 8, 9 and 13; two laser
trials start 1.6 and 2.7 s before the reference time and one lasts 9.5 s; the
stimulus-decoding check could not establish a shared clock for three
sessions, YT084 2020-02-02 and 2020-02-03 (AMM, 2 and 5 units) and YT086
2020-03-20 (MM, 5 units), which are kept; and one of the 28 cross-modal sham
sessions fails the code's own performance check as ported here. The draft
version has identical files and differs only in contributor metadata.

Two test runs before the final one failed or gave wrong values, from a
pandas duplicate-index error, a string column in a median and a light-block
mask bug, all fixed before the final run. Untracked files in the repository
root that the author did not create were left alone. The author's points on
the protocol: a paper download that bioRxiv refused; a Methods rule that
leads the analysis although the reported numbers fit the code; no guidance
for a Methods step that may already have been applied to the files; a
criterion that could not decide, whose tie was broken after one area's result
had been seen; a reading not listed before the analysis that matches the
paper's numbers; an absence claim whose test in the paper is ambiguous; no
slot for code that is read but supplies no data; and no rule on whether the
main seed or the spread over seeds decides a bootstrap result.
E
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

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes.md",
 "old_string": "Methods' soft normalization differs from the code's in each population\nanalysis, and",
 "new_string": "Methods' soft normalization differs from the code's in the trajectory\ndistance, subspace overlap, coding dimensions and decoding, and"
}
```

```
The file docs/pilot-notes.md has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent**

I added the README row for 000232 (19 reproduced, 7 partially, 2 not reproduced, 1 blocked) and appended the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed.

The `catalystneuro` field for this dandiset lists two contributors, Luiz Tauffer and Benjamin Dichter, and names no repository. So the opening sentence names the contributors, as the 000226 subsection does, in place of a repository.

### 000232, Chang et al. 2023

Nineteen claims reproduced, seven partially, two not reproduced and one
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 28 of the 29;
it gave not reproduced for `fig5b-first-hit-switches`, where both block counts
fail, and the author changed that claim from partially reproduced to not
reproduced, as the criterion allows a partial outcome only when one condition
fails. Round 2 agreed with all 29 and nothing was proposed, so there was no
third round. The paper reports that in mice switching between a
respond-to-touch and a respond-to-light rule, neurons and populations in MM
and ALM encode the rule before the stimulus more than those in S1 and S2,
that this pre-stimulus state shapes the touch response and tracks rule
switches, and that inhibiting MM or ALM before the stimulus lowers tactile
sensitivity. The recording and optogenetic session counts, task performance,
the fractions of selective neurons, rule and stimulus decoding with LDA, SVMs
and random forests, trajectory distances, subspace overlap, coding
dimensions, the first hits after a switch, state tracking across transitions
and the optogenetic effects on sensitivity, hit rate and laser-only licks were
tested; the claim on the histological probe locations is blocked as
`data_missing`. Some outcomes rest on weak ground: `fig1h-thit-tcr-selective`
and `fig2c-rule-prestim-units` are judged on the main seed, and on the means
over five seeds all four areas of both would be within tolerance, while on
single seeds fig1h MM is within tolerance in 3 of 5 and fig2c S1 in none; in
`fig6c-pre-inhibition-tactile` the ALM upper bound is 0.005, averages -0.001
(SD 0.003) over ten other seeds and is below 0 in 7 of 10, and the code's
resampling gives the paper's interval; `fig4c-prestim-distance-predicts-divergence`
gives p = 0.004 with the Methods' normalization and p = 0.001 with the
code's, and the units of the offset are not stated; in
`figs4h-choice-right-left` S2 is 0.422 against 0.32 and within tolerance in 1
of 5 seeds; the absence in `figs5-sensory-states-no-tracking` rests on wide
intervals; and in `fig6ij-laser-only-licks` the one failing interval, detection
task, MM, short laser, [0.045, 0.483], excludes 0 in all ten other seeds, but
the paper's detection intervals match none of the short, long or pooled rows.
The author read the full text of preprint version 2 from eLife's copy of the
reviewed preprint, as bioRxiv refused the download, and read the paper's
analysis code at commit 227631e for method choices the Methods leave open,
taking no data from it.

The dandiset was converted by CatalystNeuro (Luiz Tauffer and Benjamin
Dichter of CatalystNeuro are contributors). Sessions, mice and units per area
match the paper exactly, as do all 24 optogenetic session and mouse counts,
but the ephys files hold only the trials and units the paper analysed: no
trial has a lick between -1 and 0.1 s of the stimulus, gaps of 8 to 64 per
session remain in the trial times, the units are those passing the quality
filter and the 50 Hz cut, and the dandiset does not say that trials or units
were removed. Units carry only spike times and observation intervals, with no
quality metrics, waveforms, channel or depth, and ids that run from 0, so
units the paper names by cluster number cannot be identified; electrode x, y
and z are NaN in all 49 ephys files, locations are "unknown", and the
histology of Figure 1E is not deposited. The trials table columns have no
descriptions, and `response`, `blockType` ("Change" for the cue trial), the
opto trial types and the indicator columns are explained only by the paper's
code. In the 130 behaviour files `start_time` equals the stimulus onset, so
trial intervals overlap, and in the tactile detection files trials without a
whisker stimulus are labelled "Stim_Vis" and "Stim_Vis_NoCue" with a visual
stimulus type. Figure 5B's 88 and 91 switches equal the touch and light
blocks of the 40 recording sessions when each session's first block is
counted, against 63 and 75 non-first blocks with a hit. Other findings: the
Methods' soft normalization differs from the code's in the trajectory
distance, subspace overlap, coding dimensions and decoding, and the Methods
exclude sessions with fewer than ten units from the subspace analysis where
the code requires more than ten; the code's optogenetic bootstrap resamples
only hits; the coding-dimension code keeps 8, 7, 5 and 11 sessions where
Figure S4 reports 10, 8, 9 and 13; two laser trials start 1.6 and 2.7 s
before the reference time and one lasts 9.5 s; the stimulus-decoding check
could not establish a shared clock for three sessions, YT084 2020-02-02 and
2020-02-03 (AMM, 2 and 5 units) and YT086 2020-03-20 (MM, 5 units), which are
kept; and one of the 28 cross-modal sham sessions fails the code's own
performance check as ported here. The draft version has identical files and
differs only in contributor metadata.

Two test runs before the final one failed or gave wrong values, from a
pandas duplicate-index error, a string column in a median and a light-block
mask bug, all fixed before the final run. Untracked files in the repository
root that the author did not create were left alone. The author's points on
the protocol: a paper download that bioRxiv refused; a Methods rule that
leads the analysis although the reported numbers fit the code; no guidance
for a Methods step that may already have been applied to the files; a
criterion that could not decide, whose tie was broken after one area's result
had been seen; a reading not listed before the analysis that matches the
paper's numbers; an absence claim whose test in the paper is ambiguous; no
slot for code that is read but supplies no data; and no rule on whether the
main seed or the spread over seeds decides a bootstrap result.

## End of run

13 turns, 1 minutes, result: success.
