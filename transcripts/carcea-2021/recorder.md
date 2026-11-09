# 000114 · recorder · run 38977613381

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000114 --write; git diff; ls transcripts/000114/ claims/000114/; cat attempts/000114-carcea-2021-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (37.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/33566991-4265-432f-bd3f-5e2cfe267500/tool-results/bomaztsm6.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index e9bcccd..e15c7a9 100644
--- a/README.md
+++ b/README.md
@@ -74,6 +74,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000067](https://dandiarchive.org/dandiset/000067) | [Fujisawa et al. 2008](https://doi.org/10.1038/nn.2134) | 0 | 5 | 7 | 4 | [`000067-fujisawa-2008`](entries/000067-fujisawa-2008) |
 | [000070](https://dandiarchive.org/dandiset/000070) | [Churchland et al. 2012](https://doi.org/10.1038/nature11129) | 5 | 7 | 4 | 6 | [`000070-churchland-2012`](entries/000070-churchland-2012) |
 | [000121](https://dandiarchive.org/dandiset/000121) | [Even-Chen et al. 2019](https://doi.org/10.1371/journal.pcbi.1006808) | 6 | 7 | 6 | 1 | [`000121-even-chen-2019`](entries/000121-even-chen-2019) |
+| [000114](https://dandiarchive.org/dandiset/000114) | [Carcea et al. 2021](https://doi.org/10.1038/s41586-021-03814-7) | 1 | 3 | 3 | 12 | [`000114-carcea-2021`](entries/000114-carcea-2021) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000114/:
10.1038-s41586-021-03814-7.yaml

transcripts/000114/:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,80p README.md; cat attempts/000114-carcea-2021-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md; python -c "import json;d=json.load(open('targets/dandisets.json'));print([x for x in (d if isinstance(d,list) else d.values()) if '000114' in json.dumps(x)])"
```

```
<persisted-output>
Output too large (193KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/33566991-4265-432f-bd3f-5e2cfe267500/tool-results/b337q3wnc.txt

Preview (first 2KB):
| [001754](https://dandiarchive.org/dandiset/001754) | [Knierim et al. 2000](https://doi.org/10.1038/72910) | 3 | 0 | 1 | 3 | [`001754-knierim-2000`](entries/001754-knierim-2000) |
| [000130](https://dandiarchive.org/dandiset/000130) | [Sohn et al. 2019](https://doi.org/10.1016/j.neuron.2019.06.012) | 9 | 4 | 7 | 3 | [`000130-sohn-2019`](entries/000130-sohn-2019) |
| [001616](https://dandiarchive.org/dandiset/001616) | [Gerken et al. 2025](https://doi.org/10.7554/elife.106758.1) | 6 | 5 | 0 | 9 | [`001616-gerken-2025`](entries/001616-gerken-2025) |
| [002014](https://dandiarchive.org/dandiset/002014) | [Choi et al. 2025](https://doi.org/10.1016/j.jneumeth.2025.110467) | 4 | 1 | 0 | 8 | [`002014-choi-2025`](entries/002014-choi-2025) |
| [001933](https://dandiarchive.org/dandiset/001933) | [Chen et al. 2026](https://doi.org/10.1038/s41467-026-75194-3) | 6 | 2 | 1 (+1) | 0 | [`001933-chen-2026`](entries/001933-chen-2026) |
| [000004](https://dandiarchive.org/dandiset/000004) | [Chandravadia et al. 2020](https://doi.org/10.1038/s41597-020-0415-9) | 10 | 8 (+2) | 4 | 1 | [`000004-chandravadia-2020`](entries/000004-chandravadia-2020) |
| [002013](https://dandiarchive.org/dandiset/002013) | [Amjad et al. 2025](https://doi.org/10.1021/acschemneuro.5c00071) | 7 (+1) | 1 | 0 | 5 | [`002013-amjad-2025`](entries/002013-amjad-2025) |
| [001636](https://dandiarchive.org/dandiset/001636) | [Pasquereau et al. 2013](https://doi.org/10.3389/fnsys.2013.00098) | 4 | 3 | 3 | 18 | [`001636-pasquereau-2013`](entries/001636-pasquereau-2013) |
| [000041](https://dandiarchive.org/dandiset/000041) | [Watson et al. 2016](https://doi.org/10.1016/j.neuron.2016.03.036) | 8 | 9 | 15 | 7 | [`000041-watson-2016`](entries/000041-watson-2016) |
| [000003](https
[... 2 more lines not kept]
```

**Agent**

The attempt yaml is large. Let me read pieces separately.

**Agent calls Bash**

```bash
grep -n -B3 '^| Dandiset' README.md; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md attempts/000114-carcea-2021-01.yaml claims/000114/*.yaml transcripts/000114/*report.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else list(d.values())
for x in it:
  s=json.dumps(x)
  if '000114' in s: print(s[:2000])
" ; python -c "import json;d=json.load(open('targets/dandisets.json'));print(type(d), list(d)[:3] if isinstance(d,dict) else '')"
```

```
46-
47-## Attempts so far
48-
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
1397:### 000056, Peyrache et al. 2015
1464:### 000059, Petersen et al. 2020
1534:### 000061, Girardeau et al. 2017
1594:### 000067, Fujisawa et al. 2008
1670:### 000070, Churchland et al. 2012
1743:### 000121, Even-Chen et al. 2019
  1815 docs/pilot-notes.md
   603 attempts/000114-carcea-2021-01.yaml
   248 claims/000114/10.1038-s41586-021-03814-7.yaml
    47 transcripts/000114/author-report.md
    28 transcripts/000114/author-revise-1-report.md
    30 transcripts/000114/author-revise-2-report.md
    50 transcripts/000114/verifier-1-report.md
    55 transcripts/000114/verifier-2-report.md
  2876 total
[{"dandiset": "000003", "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells", "published_version": "0.260218.2052", "asset_count": 101, "size_gb": 2559.25, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["House mouse"], "approaches": ["electrophysiological approach", "behavioral approach"], "papers": [{"doi": "10.1016/j.neuron.2016.12.011", "title": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells", "relation": "IsDescribedBy", "resource_type": "JournalArticle", "preprint": false}], "catalystneuro": ["contributor Baker, Cody of CatalystNeuro"]}, {"dandiset": "000004", "name": "A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task", "published_version": "0.220126.1852", "asset_count": 87, "size_gb": 6.2, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Human"], "approaches": ["electrophysiological approach"], "papers": [{"doi": "10.1038/s41597-020-0415-9", "title": "A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task", "relation": "IsDescribedBy", "resource_type": "JournalArticle", "preprint": false}], "catalyst
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
for k,v in d.items():
  if isinstance(v,list):
    for x in v:
      if x.get('dandiset')=='000114': print(json.dumps(x,indent=1))
"; sed -n 1594,1815p docs/pilot-notes.md
```

```
{
 "dandiset": "000114",
 "name": "Oxytocin neurons enable social transmission of maternal behaviour",
 "published_version": "0.230602.1643",
 "asset_count": 30,
 "size_gb": 387.2,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Mus musculus - House mouse"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.1038/s41586-021-03814-7",
   "title": "Oxytocin neurons enable social transmission of maternal behaviour",
   "relation": "IsDescribedBy",
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/000114/author-report.md transcripts/000114/verifier-1-report.md transcripts/000114/author-revise-1-report.md transcripts/000114/verifier-2-report.md transcripts/000114/author-revise-2-report.md
```

```
I've done steps 1 to 6 for dandiset 000114 and run the handover. `tools/entry.py check` reports 0 errors and the notebook runs clean in 65 s. Nothing is committed.

The paper's full text is open access (CC BY, PMC8387235), so I used it, along with its Source Data spreadsheets for the reported numbers. All of it is saved under `paper/`. I pinned version 0.230602.1643. It is the only published version, and the paper cites the dandiset without a version.

**1. Outcomes (19 claims)**

| Claim | Outcome |
|---|---|
| label-link (behaviour labels named through the paper's code) | reproduced (73.3% of nest dwells last 40 s or less; paper 70.5%) |
| ed7a-nest-entry-fraction | partially reproduced (21.6% activated against 26.5%; Fisher p = 1.9e-14) |
| ed7a-shepherding-fraction | not reproduced (1.5%, p = 0.12, against 11.9%) |
| ed7a-dam-retrieval-fraction | partially reproduced (9.8%, p = 9e-05, against 17.4%) |
| fig2j-shepherded-entry | not reproduced (p = 0.182) |
| fig1j-shepherding-rate | partially reproduced (0.65 per h, above 0.2 with p = 0.029, but far below 3.5 ± 0.9) |
| ed8a-dam-retrieval-rate | not reproduced (0.21 per h against about 0.5) |
| ot-pvn-units, ed6, fig1cd, fig2a, fig3fg, fig3ij, fig4c, fig4f, fig4jk, ed9 | blocked: data_missing (10 claims) |
| fig2f-virgin-chasing, fig4i-projection-photometry | blocked: metadata_insufficient |

**2. What I found about the dandiset**
- **What it holds:** PVN units and video annotations for 4 of the paper's 17 recorded virgins (228 units in 8 sessions), raw voltage only for a fifth virgin and for several other sessions, and photometry from 6 non-co-housed virgins. There is no optical tagging and no oxytocin-neuron identity. The code reads that identity from a spreadsheet that is not public.
[... 190 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000114-carcea-2021-01.yaml"
}
```

```
1	schema_version: 1
2	id: 000114-carcea-2021-01
3	dandiset: "000114"
4	dandiset_version: 0.230602.1643
5	paper: doi:10.1038/s41586-021-03814-7
6	date: 2026-10-16
7	entry: 000114-carcea-2021
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: Names of the behaviour labels ("Mom agressing" for shepherding, "Virgin in rest" for nest
18	    entry, "Mom retrieval" for dam retrieval, from behStrings in shepNestPup_xCorr_ForNature.m) and
19	    the parameters of the modulation index and shuffle test (calc_spike_freq_behavior_significance.m),
20	    including the 0.5 s gap before the baseline and the unit-removal threshold of 1,048,500 spikes.
[... 584 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000114/10.1038-s41586-021-03814-7.yaml"
}
```

```
1	# Claims for Carcea et al. (2021), "Oxytocin neurons enable social transmission of maternal
2	# behaviour", on dandiset 000114.
3	# Source: the full text in PubMed Central (PMC8387235, CC BY), its Methods, figure legends and
4	# Extended Data legends, and the paper's Source Data spreadsheets for Figures 2 to 4 and
5	# Extended Data Figures 7 and 8, read for the reported numbers.
6	#
7	# What the author had seen when these criteria were written: the file list and metadata of
8	# every file; the units tables (unit counts, spike counts, firing rates, the fraction of
9	# inter-spike intervals under 2 ms, the fraction of spikes coincident with another unit's);
10	# the event labels, their counts and durations per session (so the per-session fraction of
11	# "Virgin in rest" intervals of 40 s or less, and the per-session counts of "Mom agressing"
12	# and "Mom retrieval" events, which with the session lengths give the rates tested in
13	# fig1j-shepherding-rate and ed8a-dam-retrieval-rate); the gaps between the end of each
14	# "Mom agressing" event and the next "Virgin in rest" start; a test of the shared clock
15	# (population contrast at annotation onsets against shifted labels); and the mean
16	# retrieval-triggered photometry change per session. No firing-rate modulation, shuffle test
17	# or fraction of modulated units had been computed.
18	#
19	# The dandiset holds the PVN single-unit recordings of four co-housed virgins (V110, V111,
20	# V116, V118; 228 units over 8 sessions) with behaviour annotations, raw voltage of five
[... 229 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "to-nwb|to_nwb|github.com/catalystneuro",
 "path": "
 "glob": "{attempts/000114*,claims/000114/*,transcripts/000114/*report.md,entries/000114-carcea-2021/README.md}",
 "output_mode": "content"
}
```

```
No matches found
```

**Agent calls Bash**

```bash
grep -n "converted by CatalystNeuro" docs/pilot-notes.md
```

```
786:The dandiset was converted by CatalystNeuro (catalystneuro/mcnaughton2000-to-nwb),
913:The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb).
948:The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
1038:The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
1083:The dandiset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).
1153:The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
1219:The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
1291:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
1364:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
1421:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
1490:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
1559:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
1626:The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
1703:The dandiset was converted by CatalystNeuro (catalystneuro/shenoy-lab-to-nwb).
1774:The dandiset was converted by CatalystNeuro (catalystneuro/shenoy-lab-to-nwb).
```

**Agent calls Bash**

```bash
sed -n 1291,1293p docs/pilot-notes.md; sed -n 1421,1423p docs/pilot-notes.md
```

```
The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). In 24 files the end index of the first unit is short by a
multiple of 65,536 spikes (k = 1 to 7), and the missing spikes open the
The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The units tables hold only spike times, with no electrode,
shank, brain region, waveform or quality measure, and every electrode's
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 000114, Carcea et al. 2021

One claim reproduced, three partially, three not reproduced and twelve
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with all 19; round
2 agreed again and nothing was proposed, so there was no third round. The
paper reports that oxytocin neurons of the paraventricular nucleus (PVN) in
virgin mice co-housed with a dam and litter are activated by shepherding by
the dam, by nest entry and by the dam's pup retrievals, and that this lets
virgins learn to retrieve pups, also by watching dams through the auditory
cortex. The naming of the behaviour labels, the fractions of units activated
during nest entry, shepherding and dam retrieval, firing after shepherded
against voluntary nest entries, and the rates of shepherding and of
retrieval by the dam were tested on 194 units from 4 virgins in 7 sessions,
with oxytocin and other PVN units pooled. The ten claims on optically tagged
oxytocin units, the behavioural cohorts, unit recordings during observation,
the auditory cortex and the colliculus are blocked as `data_missing`, and
virgin chasing of the dam and the projection photometry of Fig. 4i as
`metadata_insufficient`. Some outcomes rest on weak ground: in
`ed7a-nest-entry-fraction` leaving out the 20 units above the code's limit
of 1,048,500 spikes gives 24.1%, inside tolerance, and counting V111 once
gives 28.8 to 30.3%; `fig2j-shepherded-entry` would pass without V116
03102018, whose clock is not known (p = 0.0237); in
`ed7a-dam-retrieval-fraction` 9 of the 13 activated units come from the
single retrieval of V111 03032018, share a median 71% of their spikes
pairwise within 0.1 ms, and the retrieval falls on one of the session's
largest synchronous bursts; and `fig1j-shepherding-rate` passes its t-test
over sessions (p = 0.0292) but not over mice (p = 0.193). The author used
the full text in PubMed Central, the Source Data for reported numbers only,
and the paper's code on GitHub for the label names and the parameters of the
shuffle test.

The dandiset was converted by CatalystNeuro (Benjamin Dichter of
CatalystNeuro is a contributor). It holds units for 4 of the paper's 17
recorded virgins (228 units in 8 sessions, against 541 in the paper) and
does not say which recordings were deposited or why; the optical tagging
recordings and the identity of the 21 OT-PVN units are not in it, so no
oxytocin-specific result can be tested, and the paper's code reads that
identity from a spreadsheet that is not public. The behaviour labels have no
description, and shepherding, nest entry and dam retrieval can be named only
from the paper's code; one file (V116 03122018) carries both the code's
labels and the paper's names. No test established that spikes and
annotations share a clock in any session, and in V116 03102018 the raw
voltage lasts 4.46 h while spike times and annotations run to 13.4 h. Units
in V110 and V111 have a median 7.0 to 9.2% of inter-spike intervals under 2
ms and 79 to 90% of their spikes within 0.1 ms of another unit's, although
the Methods say such spikes were removed, and V111's three sessions hold 31
units each with spike counts correlated 0.93 to 0.97, with nothing saying
whether they are the same units. The Methods cap nest entries at 40 s, which
the code does not, and on this data the cap changes the fraction activated
from 1.0% to 21.6%. Other findings: session start times disagree with the
dates in the session ids; the units table holds spike times and a name only,
and every electrode location is "unknown"; every subject is described as
co-housed, including the six photometry animals of the observation
experiment; photometry fibre location, fluorophore, wavelengths and gain are
"unknown" or NaN, the trace is stated in watts with values near 1000, and
commanded_voltage varies from 0.07 to 482 within sessions; and which
photometry animals learned to retrieve is known for 2 of 6, so the groups of
Fig. 4i cannot be formed.

In exploration, h5py's visititems hung on the large ecephys files, and a
first survey of all files hit the one-hour timeout before a plain group walk
replaced it. Untracked files in the repository root, which the author took
to be sandbox mounts, were left alone. The author's points on the protocol:
no rule for when the clock check fails to settle alignment; a data check that
showed counts and durations deciding some claims before the criteria were
written; fractions split by a label the dandiset lacks; whether
reference-only sources belong in `inputs`; a claim blocked for two reasons;
the choice between `data_missing` and `metadata_insufficient` for a label
that is absent while the units are present; units probably the same across
days, which the duplicate rule does not cover; and content comparison of
versions at 387 GB.
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

**Agent calls Bash**

```bash
python - <<'EOF'
p='docs/pilot-notes.md'
s=open(p).read()
old="""the dam, by nest entry and by the dam's pup retrievals, and that this lets
virgins learn to retrieve pups, also by watching dams through the auditory
cortex."""
new="""the dam, by nest entry and by the dam's pup retrievals, that silencing them
delays pup retrieval, and that virgins can learn to retrieve by watching
dams, which depends on oxytocin in the auditory cortex."""
assert old in s
open(p,'w').write(s.replace(old,new))
EOF
git diff --stat
```

```
README.md           |  1 +
 docs/pilot-notes.md | 73 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 74 insertions(+)
```

**Agent**

I ran `tools/readme_row.py 000114 --write`, which added this row to README.md: 1 reproduced, 3 partially, 3 not reproduced, 12 blocked. I then added the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed.

The `catalystneuro` field for 000114 names a contributor (Benjamin Dichter) but no conversion repository, and none of the other sources name one either. So the opening uses the "is a contributor" wording that earlier subsections use in the same case.

### 000114, Carcea et al. 2021

One claim reproduced, three partially, three not reproduced and twelve
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with all 19; round
2 agreed again and nothing was proposed, so there was no third round. The
paper reports that oxytocin neurons of the paraventricular nucleus (PVN) in
virgin mice co-housed with a dam and litter are activated by shepherding by
the dam, by nest entry and by the dam's pup retrievals, that silencing them
delays pup retrieval, and that virgins can learn to retrieve by watching
dams, which depends on oxytocin in the auditory cortex. The naming of the
behaviour labels, the fractions of units activated during nest entry,
shepherding and dam retrieval, firing after shepherded against voluntary
nest entries, and the rates of shepherding and of retrieval by the dam were
tested on 194 units from 4 virgins in 7 sessions, with oxytocin and other
PVN units pooled. The ten claims on optically tagged oxytocin units, the
behavioural cohorts, unit recordings during observation, the auditory cortex
and the colliculus are blocked as `data_missing`, and virgin chasing of the
dam and the projection photometry of Fig. 4i as `metadata_insufficient`.
Some outcomes rest on weak ground: in `ed7a-nest-entry-fraction` leaving out
the 20 units above the code's limit of 1,048,500 spikes gives 24.1%, inside
tolerance, and counting V111 once gives 28.8 to 30.3%;
`fig2j-shepherded-entry` would pass without V116 03102018, whose clock is
not known (p = 0.0237); in `ed7a-dam-retrieval-fraction` 9 of the 13
activated units come from the single retrieval of V111 03032018, share a
median 71% of their spikes pairwise within 0.1 ms, and the retrieval falls
on one of the session's largest synchronous bursts; and
`fig1j-shepherding-rate` passes its t-test over sessions (p = 0.0292) but
not over mice (p = 0.193). The author used the full text in PubMed Central,
the Source Data for reported numbers only, and the paper's code on GitHub
for the label names and the parameters of the shuffle test.

The dandiset was converted by CatalystNeuro (Benjamin Dichter of
CatalystNeuro is a contributor). It holds units for 4 of the paper's 17
recorded virgins (228 units in 8 sessions, against 541 in the paper) and
does not say which recordings were deposited or why; the optical tagging
recordings and the identity of the 21 OT-PVN units are not in it, so no
oxytocin-specific result can be tested, and the paper's code reads that
identity from a spreadsheet that is not public. The behaviour labels have no
description, and shepherding, nest entry and dam retrieval can be named only
from the paper's code; one file (V116 03122018) carries both the code's
labels and the paper's names. No test established that spikes and
annotations share a clock in any session, and in V116 03102018 the raw
voltage lasts 4.46 h while spike times and annotations run to 13.4 h. Units
in V110 and V111 have a median 7.0 to 9.2% of inter-spike intervals under 2
ms and 79 to 90% of their spikes within 0.1 ms of another unit's, although
the Methods say such spikes were removed, and V111's three sessions hold 31
units each with spike counts correlated 0.93 to 0.97, with nothing saying
whether they are the same units. The Methods cap nest entries at 40 s, which
the code does not, and on this data the cap changes the fraction activated
from 1.0% to 21.6%. Other findings: session start times disagree with the
dates in the session ids; the units table holds spike times and a name only,
and every electrode location is "unknown"; every subject is described as
co-housed, including the six photometry animals of the observation
experiment; photometry fibre location, fluorophore, wavelengths and gain are
"unknown" or NaN, the trace is stated in watts with values near 1000, and
commanded_voltage varies from 0.07 to 482 within sessions; and which
photometry animals learned to retrieve is known for 2 of 6, so the groups of
Fig. 4i cannot be formed.

In exploration, h5py's visititems hung on the large ecephys files, and a
first survey of all files hit the one-hour timeout before a plain group walk
replaced it. Untracked files in the repository root, which the author took
to be sandbox mounts, were left alone. The author's points on the protocol:
no rule for when the clock check fails to settle alignment; a data check that
showed counts and durations deciding some claims before the criteria were
written; fractions split by a label the dandiset lacks; whether
reference-only sources belong in `inputs`; a claim blocked for two reasons;
the choice between `data_missing` and `metadata_insufficient` for a label
that is absent while the units are present; units probably the same across
days, which the duplicate rule does not cover; and content comparison of
versions at 387 GB.

## End of run

13 turns, 1 minutes, result: success.
