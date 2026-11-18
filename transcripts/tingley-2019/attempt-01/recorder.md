# 000218 · recorder · run 39002623512

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000218 --write; git diff; ls claims/000218 transcripts/000218; cat attempts/000218-tingley-2019-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (53.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/331bf8a0-699d-44d7-82ba-9530804f764c/tool-results/buud3bvcr.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index d4c737f..6f8b3ab 100644
--- a/README.md
+++ b/README.md
@@ -76,6 +76,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000121](https://dandiarchive.org/dandiset/000121) | [Even-Chen et al. 2019](https://doi.org/10.1371/journal.pcbi.1006808) | 6 | 7 | 6 | 1 | [`000121-even-chen-2019`](entries/000121-even-chen-2019) |
 | [000114](https://dandiarchive.org/dandiset/000114) | [Carcea et al. 2021](https://doi.org/10.1038/s41586-021-03814-7) | 1 | 3 | 3 | 12 | [`000114-carcea-2021`](entries/000114-carcea-2021) |
 | [000213](https://dandiarchive.org/dandiset/000213) | [Tingley et al. 2018](https://doi.org/10.1016/j.neuron.2018.04.028) | 3 | 8 | 9 | 5 | [`000213-tingley-2018`](entries/000213-tingley-2018) |
+| [000218](https://dandiarchive.org/dandiset/000218) | [Tingley et al. 2019](https://doi.org/10.1016/j.neuron.2019.10.012) | 4 | 7 | 10 | 10 | [`000218-tingley-2019`](entries/000218-tingley-2019) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000218:
10.1016-j.neuron.2019.10.012.yaml

transcripts/000218:
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000218-tingley-2019-01.yaml; grep -n -B3 '^| \[000121' README.md | head; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (53.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/331bf8a0-699d-44d7-82ba-9530804f764c/tool-results/b35gesoxf.txt

Preview (first 2KB):
schema_version: 1
id: 000218-tingley-2019-01
dandiset: "000218"
dandiset_version: 0.250624.0439
paper: doi:10.1016/j.neuron.2019.10.012
date: 2026-10-16
entry: 000218-tingley-2019
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000218-tingley-2019-01.yaml"
}
```

```
1	schema_version: 1
2	id: 000218-tingley-2019-01
3	dandiset: "000218"
4	dandiset_version: 0.250624.0439
5	paper: doi:10.1016/j.neuron.2019.10.012
6	date: 2026-10-16
7	entry: 000218-tingley-2019
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: The detector bz_FindRipples.m and the EMG estimate bz_EMGFromLFP.m, read for the parameters
18	    the Methods leave open (zero-phase filtering, 11-sample smoothing, 30 ms merging, the trough as
19	    the event time, EMG exclusion at 0.9, the EMG window). No data are taken from it.
20	  source: https://github.com/buzsakilab/buzcode at commit 5981194ee764436383269d5fbe09980ae852c6fe
[... 901 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A6 '^| Dandiset' README.md | head -8; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md; python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '000218' in json.dumps(e): print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (173.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/331bf8a0-699d-44d7-82ba-9530804f764c/tool-results/b0wsrvisu.txt

Preview (first 2KB):
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50-|---|---|---|---|---|---|---|
51-| [000582](https://dandiarchive.org/dandiset/000582) | [Sargolini et al. 2006](https://doi.org/10.1126/science.1125572) | 2 | 1 | 0 | 0 | [`000582-sargolini-2006`](entries/000582-sargolini-2006) |
52-| [000127](https://dandiarchive.org/dandiset/000127) | [Chowdhury et al. 2020](https://doi.org/10.7554/eLife.48198) | 4 | 2 | 0 | 4 | [`000127-chowdhury-2020`](entries/000127-chowdhury-2020) |
53-| [000207](https://dandiarchive.org/dandiset/000207) | [Zheng et al. 2022](https://doi.org/10.1038/s41593-022-01020-w) | 5 | 1 | 0 | 14 | [`000207-zheng-2022`](entries/000207-zheng-2022) |
54-| [000147](https://dandiarchive.org/dandiset/000147) | [Guan et al. 2022](https://doi.org/10.7554/eLife.74478) | 9 (+3) | 0 | 1 | 4 (+3) | [`000147-guan-2022`](entries/000147-guan-2022) |
55-| [001097](https://dandiarchive.org/dandiset/001097) | [Liu et al. 2024](https://doi.org/10.1038/s41586-024-07916-w) | 7 | 2 | 3 | 12 | [`001097-liu-2024`](entries/001097-liu-2024) |
1534:### 000061, Girardeau et al. 2017
1594:### 000067, Fujisawa et al. 2008
1670:### 000070, Churchland et al. 2012
1743:### 000121, Even-Chen et al. 2019
1817:### 000114, Carcea et al. 2021
1890:### 000213, Tingley et al. 2018
1973 docs/pilot-notes.md
[
 {
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 1594
}
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
for e in d:
  if e['dandiset']=='000218': print(json.dumps({k:v for k,v in e.items() if k!='assets'},indent=1)[:3000])"
```

```
1594	### 000067, Fujisawa et al. 2008
1595	
1596	No claims reproduced, five partially, seven not reproduced and four blocked,
1597	all on the dandiset. Round 1 gave its own outcome for each claim from the
1598	notebook with its conclusions removed and agreed with all 16. The author then
1599	changed `fig4-position-dependence` from not reproduced to blocked as
1600	`methods_underspecified`, because the calibration the verifier asked for
1601	showed that the criterion's test flags 30.0% and 75.0% of synthetic pairs
1602	with constant efficacy, and wrote a criterion for `traj-diverge` that moved
1603	it from blocked to partially reproduced; round 2 disagreed with that change,
1604	the author proposed blocked as `data_missing`, and a third round agreed. The
1605	paper reports the firing of neurons in the medial prefrontal cortex of rats
1606	during an odor-place matching task on a maze, and the monosynaptic
1607	connections between them. The channel map, the counts of rats and units, the
1608	active fraction, field size, trajectory and odor selectivity, connection
1609	rates, cell classes, the fall of connection probability with distance,
1610	position dependence, facilitation and depression, and supralinear summation
1611	were tested on eight working memory sessions from three rats, with units
1612	placed on the prefrontal probe from their waveforms; task performance, the
1613	divergence of trajectories and the example session EE.188 are blocked as
[... 361 more lines not kept]
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if e['dandiset']=='000218': print(json.dumps({k:v for k,v in e.items() if k!='assets'},indent=1)[:3000])
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else '')
L=d['dandisets'] if isinstance(d,dict) and 'dandisets' in d else d
for e in L:
  if isinstance(e,dict) and e.get('dandiset')=='000218': print(json.dumps(e,indent=1)[:3000])"; wc -c transcripts/000218/*-report.md
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
 6352 transcripts/000218/author-report.md
 3439 transcripts/000218/author-revise-1-report.md
 3218 transcripts/000218/author-revise-2-report.md
 1216 transcripts/000218/author-revise-3-report.md
11647 transcripts/000218/verifier-1-report.md
 5392 transcripts/000218/verifier-2-report.md
 2697 transcripts/000218/verifier-3-report.md
33961 total
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
for e in d['targets']:
  if e.get('dandiset')=='000218': print(json.dumps({k:v for k,v in e.items() if k not in ('assets',)},indent=1)[:4000])"; cd transcripts/000218; for f in author-report.md author-revise-1-report.md author-revise-2-report.md author-revise-3-report.md verifier-3-report.md; do echo "=== $f"; cat $f; done
```

```
{
 "dandiset": "000218",
 "name": "Routing of Hippocampal Ripples to Subcortical Structures via the Lateral Septum",
 "published_version": "0.250624.0439",
 "asset_count": 98,
 "size_gb": 1512.86,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Rattus norvegicus - Norway rat"
 ],
 "approaches": [
  "electrophysiological approach",
  "behavioral approach"
 ],
 "papers": [
  {
   "doi": "10.1016/j.neuron.2019.10.012",
   "title": "Routing of Hippocampal Ripples to Subcortical Structures via the Lateral Septum",
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cat verifier-1-report.md verifier-2-report.md; head -60 ../../claims/000218/*.yaml; grep -n 'fetch\|full text\|PMC\|could not' verifier-1-report.md verifier-2-report.md
```

```
**Verifier report, round 1: Tingley and Buzsáki 2019 (doi:10.1016/j.neuron.2019.10.012) on DANDI 000218, version 0.250624.0439**

I read the paper from the PMC author manuscript, saved under `paper/`. The attempt record was not among my materials, so the claim count comes from the claims file (31 claims) and the outcomes below are mine. Two leftover files in `paper/` are error pages from failed downloads (`PMC6952543_bioc.json`, `PMC6952543.xml`). Deleting them needed approval, which this session could not give, so they are still there.

My tally: 4 reproduced, 7 partially reproduced, 10 not reproduced, 10 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| dataset-composition | partially_reproduced | Cell 13: 6 animals. Three counts are within tolerance: LS neurons with more than 50 spikes in high-power epochs, 2046; CA1+LS recordings by units, 37; recordings with LS electrodes, 94. Two are out: CA3+LS is 10 under both readings (the archive holds only 10 files with `ca3` electrodes), and CA1-rate recordings are 40, 72 or 43, against 53±5.3. That is 3 of 5. |
| fig1c-hfo-each-animal | not_reproduced | Cell 15: median frequency is between 152 and 158 Hz in all 6 animals. LS firing at HFOs exceeds random times by more than 3 SEM only in DT1; it is lower than at random times in DT7, DT8 and DT9. NREM-only events: 2 animals pass. |
| fig1c-event-count | reproduced | Cell 19: reading (b), recordings with LS units, gives 31,984, within 29,955±2,996. Reading (a) gives 67,186. DT7 contributes most events, so the agreement on the total is probably coincidental. |
| figs1-participation | not_reproduced | Cell 21: fraction of neurons firing 0.027 and spikes per event 0.051 (pooled), or 0.035 and 0.068 (per recording), against 0.16 and 0.23. |
| fig1d-phase-locking | partially_reproduced | Cell 23: 56.3% of tested neurons, or 47.0% of all, are phase-locked, against 92.5±9.25%. The trough preference holds: mean phase 189°, Rayleigh p≈0. DT7 has only 5.7% lock
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../.. && cat >> docs/pilot-notes.md <<'EOF'

### 000218, Tingley et al. 2019

Four claims reproduced, seven partially, ten not reproduced and ten blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 30 of the 31; it gave
not reproduced for `fig5d-lag`, which the author kept at partially
reproduced because the coupling part of the claim holds and the lag part
does not. Round 2 disagreed on the same claim, since the criterion defines no
partial outcome, the author proposed not reproduced, and a third round agreed.
The paper reports high-frequency oscillations (HFOs) in the lateral septum
(LS) of rats, their relation to LS firing and to CA1 ripples across sleep and
waking, LS correlations before, during and after behaviour, which features of
ripples predict LS firing, optogenetic experiments and a network model. The
dataset counts, the HFOs in each animal and their count, participation and
phase locking, HFO duration and frequency against ripples, the link between
amplitude and frequency, confinement to LS, the excess correlations and their
compression, the rise in LS rates after behaviour, HFO rates by state, the
lag and coupling with CA1 ripples, ripple-triggered firing, phase coherence,
and the prediction of LS firing from CA1 spikes, state and duration were
tested on events detected anew, as the files hold none, with `hpc` taken as
CA1. Depth within LS and travelling waves are blocked as
`metadata_insufficient`, the optogenetic HFOs and the CA1 depth of neurons as
`data_missing`, replay, seqNMF and the content-independent comparison as
`methods_underspecified`, and the model and two per-session claims, which have
7 and 4 recordings against 53 because this attempt's events hold few LS
spikes, as `other`. Some outcomes rest on weak ground: the event count of
`fig1c-event-count` matches at 31,984 against 29,955 but is probably a
coincidence, as DT7 contributes most events and the count depends on the
channel; the two `fig4b` claims rest on 106 pairs in 10 recordings against
7,172 in 53 sessions; the `fig7e` outcomes come largely from counting spikes
from ripple start to stop, and with a fixed +-25 ms window the CA1-spike and
duration values are 24.7% and 17.8%; and the tolerances of
`fig1f-shorter-than-ripples` are the paper's SDs, which makes them wide.
After round 1 every HFO analysis was repeated on the LS channel re-referenced
within its shank, and no result moved towards the paper. The author used the
author manuscript in PubMed Central (PMC6952543), whose supplementary figures
were not available.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The files hold no detected LS HFOs or hippocampal ripples,
nor the detection channels and parameters, which the Methods say are stored
with each event structure, so every analysis of events has to detect them
anew and the channels cannot be matched to the paper's. In this attempt's
detection 35% of LS HFOs within 50 ms of a CA1 ripple fall on the same 0.8 ms
sample as the ripple (71% in DT8, 62% in DT2, 7% in DT9), and the CA1-LS
phase difference is consistent even at random times (median phase-locking
value 0.134 against about 0.021 for random phases); re-referencing the LS
channel lowers the same-sample share to 4.1%, which points to a signal
common to the LS and hippocampal channels, such as the reference, which the
files do not document. The units carry no waveforms, no channel and no
quality metric, so the CA1 depth of each neuron cannot be estimated and
single units cannot be told from multi-unit clusters; 11 units fire above 50
Hz on average, and wide-band data are in 27 of the 98 files, with 1579 of
2778 hippocampal units having none. Electrode x, y and z are NaN in every
file, and neither the probe geometry and its orientation nor the relative
depth of each recording within LS is given. The 10 files with `ca3`
electrodes hold no CA1 channel, which the paper's CA3 recordings used to
detect ripples, and the paper reports 25 CA3 and LS recordings against 10
here. Other findings: nine files store units without a location column, so
their 268 units cannot be assigned to a region; `hpc` does not say whether a
site is in CA1, and four DT7 files label all electrodes `unknown`; the two
rats of the optogenetic experiments are not in the dandiset; 25 units in 10
files have spike times out of order (1 to 2782 inversions each); the paper's
Key Resources point to a repository that holds only the Figure 8 model and
the code of the 2018 paper; and the paper gives the HFO band as both 120-180
and 120-200 Hz and cites wrong figure numbers in its Methods. Spikes, LFP,
sleep states and trials are consistent with one clock, and no recording is
deposited twice.

The run took about 18 minutes against the 10-minute aim, as loading each
file's chunk index takes about 33 s, and the date rolled over during the run,
so the given date was kept. Untracked files in the repository root, which the
author took to be sandbox placeholders, were left alone. The author's points
on the protocol: no guidance for a dandiset that lacks the intermediate
products the results depend on; a paper's stated SD used as tolerance, which
gives wide bounds; no threshold for too few units under a claim's own rule;
clock-check examples that do not fit continuous sleep recordings; an `inputs`
field framed around data, used here for code read only for parameters; no
block reason for a model claim; no rule on whether `measured` should use one
reading for all quantities; a step that assumes linked code exists; a
two-part criterion with no partial outcome; a runtime aim that a 1.5 TB
dandiset cannot meet; and a date that rolled over during the run.
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

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes.md",
 "old_string": "After round 1 every HFO analysis was repeated on the LS channel re-referenced\nwithin its shank, and no result moved towards the paper.",
 "new_string": "After round 1 the HFO analyses were repeated on the LS channel re-referenced\nwithin its shank, and apart from the share of events on the same sample as a\nripple no result moved towards the paper."
}
```

```
The file docs/pilot-notes.md has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent**

I ran `python tools/readme_row.py 000218 --write`, which added the README row (4 / 7 / 10 / 10). I then added the subsection below at the end of `docs/pilot-notes.md`. Nothing is committed. The untracked dotfiles and `scripts` in the repository root were already there, and I left them alone.

Two things you might want to check. The `catalystneuro` field names a contributor (Cody Baker), not a repository, so the opening sentence names the contributor, as the 000213 subsection does. The README counts don't match two of the reports: the author's first report gives 5/9/9/8 and the round 3 verifier gives 8 partially reproduced. I used the README row, which matches the outcomes in the attempt record.

### 000218, Tingley et al. 2019

Four claims reproduced, seven partially, ten not reproduced and ten blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 30 of the 31; it gave
not reproduced for `fig5d-lag`, which the author kept at partially
reproduced because the coupling part of the claim holds and the lag part
does not. Round 2 disagreed on the same claim, since the criterion defines no
partial outcome, the author proposed not reproduced, and a third round agreed.
The paper reports high-frequency oscillations (HFOs) in the lateral septum
(LS) of rats, their relation to LS firing and to CA1 ripples across sleep and
waking, LS correlations before, during and after behaviour, which features of
ripples predict LS firing, optogenetic experiments and a network model. The
dataset counts, the HFOs in each animal and their count, participation and
phase locking, HFO duration and frequency against ripples, the link between
amplitude and frequency, confinement to LS, the excess correlations and their
compression, the rise in LS rates after behaviour, HFO rates by state, the
lag and coupling with CA1 ripples, ripple-triggered firing, phase coherence,
and the prediction of LS firing from CA1 spikes, state and duration were
tested on events detected anew, as the files hold none, with `hpc` taken as
CA1. Depth within LS and travelling waves are blocked as
`metadata_insufficient`, the optogenetic HFOs and the CA1 depth of neurons as
`data_missing`, replay, seqNMF and the content-independent comparison as
`methods_underspecified`, and the model and two per-session claims, which have
7 and 4 recordings against 53 because this attempt's events hold few LS
spikes, as `other`. Some outcomes rest on weak ground: the event count of
`fig1c-event-count` matches at 31,984 against 29,955 but is probably a
coincidence, as DT7 contributes most events and the count depends on the
channel; the two `fig4b` claims rest on 106 pairs in 10 recordings against
7,172 in 53 sessions; the `fig7e` outcomes come largely from counting spikes
from ripple start to stop, and with a fixed +-25 ms window the CA1-spike and
duration values are 24.7% and 17.8%; and the tolerances of
`fig1f-shorter-than-ripples` are the paper's SDs, which makes them wide.
After round 1 the HFO analyses were repeated on the LS channel re-referenced
within its shank, and apart from the share of events on the same sample as a
ripple no result moved towards the paper. The author used the
author manuscript in PubMed Central (PMC6952543), whose supplementary figures
were not available.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The files hold no detected LS HFOs or hippocampal ripples,
nor the detection channels and parameters, which the Methods say are stored
with each event structure, so every analysis of events has to detect them
anew and the channels cannot be matched to the paper's. In this attempt's
detection 35% of LS HFOs within 50 ms of a CA1 ripple fall on the same 0.8 ms
sample as the ripple (71% in DT8, 62% in DT2, 7% in DT9), and the CA1-LS
phase difference is consistent even at random times (median phase-locking
value 0.134 against about 0.021 for random phases); re-referencing the LS
channel lowers the same-sample share to 4.1%, which points to a signal
common to the LS and hippocampal channels, such as the reference, which the
files do not document. The units carry no waveforms, no channel and no
quality metric, so the CA1 depth of each neuron cannot be estimated and
single units cannot be told from multi-unit clusters; 11 units fire above 50
Hz on average, and wide-band data are in 27 of the 98 files, with 1579 of
2778 hippocampal units having none. Electrode x, y and z are NaN in every
file, and neither the probe geometry and its orientation nor the relative
depth of each recording within LS is given. The 10 files with `ca3`
electrodes hold no CA1 channel, which the paper's CA3 recordings used to
detect ripples, and the paper reports 25 CA3 and LS recordings against 10
here. Other findings: nine files store units without a location column, so
their 268 units cannot be assigned to a region; `hpc` does not say whether a
site is in CA1, and four DT7 files label all electrodes `unknown`; the two
rats of the optogenetic experiments are not in the dandiset; 25 units in 10
files have spike times out of order (1 to 2782 inversions each); the paper's
Key Resources point to a repository that holds only the Figure 8 model and
the code of the 2018 paper; and the paper gives the HFO band as both 120-180
and 120-200 Hz and cites wrong figure numbers in its Methods. Spikes, LFP,
sleep states and trials are consistent with one clock, and no recording is
deposited twice.

The run took about 18 minutes against the 10-minute aim, as loading each
file's chunk index takes about 33 s, and the date rolled over during the run,
so the given date was kept. Untracked files in the repository root, which the
author took to be sandbox placeholders, were left alone. The author's points
on the protocol: no guidance for a dandiset that lacks the intermediate
products the results depend on; a paper's stated SD used as tolerance, which
gives wide bounds; no threshold for too few units under a claim's own rule;
clock-check examples that do not fit continuous sleep recordings; an `inputs`
field framed around data, used here for code read only for parameters; no
block reason for a model claim; no rule on whether `measured` should use one
reading for all quantities; a step that assumes linked code exists; a
two-part criterion with no partial outcome; a runtime aim that a 1.5 TB
dandiset cannot meet; and a date that rolled over during the run.

## End of run

12 turns, 1 minutes, result: success.
