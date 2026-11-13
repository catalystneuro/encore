# burman-2023 · recorder · run 42826764707

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/burman-2023/; python tools/readme_row.py burman-2023; ls summaries | head
```

```
docs/pilot-notes/shi-2013-01.md
docs/pilot-notes/crcns-fcx-2-johnson-2018-01.md
docs/pilot-notes/crcns-fcx-3-johnson-2019-01.md
docs/pilot-notes/crcns-apl-1-bruno-2017-01.md
docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
answer-report.md
answer.md
author-answers-report.md
author-answers.md
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
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; for f in shi-2013-01 crcns-fcx-2-johnson-2018-01 crcns-fcx-3-johnson-2019-01 crcns-apl-1-bruno-2017-01 crcns-ssc-10-lemessurier-2019-01; do echo "=== $f"; cat $f.md; done; cd ../..; grep -n -B3 "000458\|^| Dandiset" README.md | head; cat summaries/README.md; cat summaries/amjad-2025-01.md summaries/bech-2026-01.md
```

```
=== shi-2013-01
# shi-2013, Shi et al. 2013

Seven claims reproduced, five partially, 13 not reproduced and three blocked,
two for insufficient metadata and one for missing data; eleven outcomes rest on
an assumption, among them `hold-vision-main-effect`, `cv2-larger-nv`,
`fig6-decoding-nvnv` and `decoding-v-better-than-nv`. The first verification
round agreed with 26 of the 28 outcomes and disagreed on `fig4-indx1-means` and
`rate-variance-nv-higher`, both of which it held not reproduced, and the second
agreed with all 28, withdrawing both disagreements; nothing was proposed after
the second, so there was no third round. CRCNS does not version data sets, so
the version is recorded as unversioned with the data set's DOI
(10.6080/K0CZ353K). The paper, Shi, Apker and Buneo in the Journal of
Neurophysiology (109:2097-2107), records single neurons in superficial area 5 of
the superior parietal lobule in two rhesus monkeys (X and B) holding the arm at
eight targets in a 3D virtual environment, with the hand cursor visible (V) or
blanked (NV) during the hold, and reports that V and NV endpoints rarely differ,
that 39% of neurons have a position effect in the hold and only 13% a vision
effect, that vision mostly suppresses activity (INDX1 and INDX2), that rate
variance, Fano factor and CV2 are larger in NV, and that a maximum-likelihood
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/burman-2023-01.yaml claims/burman-2023.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for x in (it if isinstance(it,list) else it.values()):
  if '000458' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (327.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/472e6d7c-cb84-4905-bbc2-a7121703abf1/tool-results/b8txrchas.txt

Preview (first 2KB):
schema_version: 3
id: burman-2023-01
datasets:
- archive: dandi
  id: "000458"
  version: 0.230317.0039
  doi: 10.48324/dandi.000458/0.230317.0039
  relation: reuses
paper: doi:10.1016/j.neuron.2023.08.005
date: '2026-11-10'
entry: burman-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
ls -t docs/pilot-notes | head; git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 12; ls docs/pilot-notes | grep -i "crcns\|knierim"; wc -c docs/pilot-notes/*.md | sort -n | tail -3
```

```
zheng-2022-01.md
zhai-2025-01.md
zhuang-2025-01.md
zhu-2022-01.md
zaki-2024-01.md
yu-2017-01.md
yu-2016-01.md
yu-2016-02.md
yemini-2021-02.md
yuan-2025-01.md
docs/pilot-notes/shi-2013-01.md
docs/pilot-notes/crcns-fcx-2-johnson-2018-01.md
docs/pilot-notes/crcns-fcx-3-johnson-2019-01.md
docs/pilot-notes/crcns-apl-1-bruno-2017-01.md
docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
docs/pilot-notes/crcns-hc-28-jadhav-2016-01.md
docs/pilot-notes/crcns-hc-13-yu-2017-01.md
docs/pilot-notes/crcns-vim-3-mannion-2015-01.md
docs/pilot-notes/crcns-ssc-8-goncalves-2013-01.md
docs/pilot-notes/crcns-hc-14-girardeau-2017-01.md
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; ls | grep -E "johnson-201[89]|bruno-2017|lemessurier"; for f in johnson-2018-01 lemessurier-2019-01; do echo "=== $f"; cat $f.md; done; head -3 knierim-2000-02.md
```

```
bruno-2017-01.md
johnson-2018-01.md
johnson-2019-01.md
lemessurier-2019-01.md
=== johnson-2018-01
# crcns-fcx-2, Johnson et al. 2018

Five claims reproduced, none partially, seven not reproduced and nine blocked,
all for methods underspecified; three outcomes rest on an assumption,
`behavior-no-difficulty-difference`, `erp-no-condition-difference` and
`psi-theta-shift`. The first verification round agreed with 19 of the 21
outcomes and disagreed on behavior-no-difficulty-difference and psi-theta-shift,
both of which it held partial, and the second agreed with all 21, though it
questioned the label of the nine blocked claims; nothing was proposed after the
second, so there was no third round. CRCNS does not version data sets, so the
version is recorded as unversioned with the data set's DOI (10.6080/K0VX0DQD)
and the MD5 sums in the notebook header. The paper, Johnson, Adams, Solbakk,
Endestad, Larsson, Ivanovic, Meling, Lin and Knight in PLoS Biology (16,
e2004274), records intracranial EEG from the medial temporal lobe (MTL), lateral
prefrontal cortex (PFC) and orbitofrontal cortex (OFC) in ten adults with
[... 229 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
a=yaml.safe_load(open('attempts/burman-2023-01.yaml'))
print(list(a.keys()))
for o in a['outcomes']:
    print(o['claim'],o['outcome'],[k for k in o if k not in('claim','outcome','notes','notebook','output')], len(o.get('notes','')))
E
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'entry', 'provenance', 'inputs', 'outcomes', 'findings', 'verifications']
dataset-sessions-link reproduced [] 991
fig4c-sample partially_reproduced ['measured', 'deviations'] 1042
fig4d-synchrony-lower-awake partially_reproduced ['measured', 'deviations'] 1106
fig4d-entropy-higher-awake partially_reproduced ['measured', 'deviations'] 793
fig4-rate-higher-awake reproduced ['deviations'] 376
figs6-rate-regressed reproduced ['deviations'] 557
fig4f-model-hyperpolarizing-less-activity reproduced ['deviations'] 384
fig4h-model-synchrony partially_reproduced ['measured', 'deviations'] 816
fig4h-model-entropy partially_reproduced ['measured', 'deviations'] 709
figs7-model-decoding reproduced ['deviations'] 1054
figs4-intrinsic-properties blocked ['blocked_by'] 1172
fig1b-perforation-rs blocked ['blocked_by'] 356
fig1h-vu-egaba blocked ['blocked_by'] 356
fig1i-vu-rmp blocked ['blocked_by'] 356
fig1j-vu-df blocked ['blocked_by'] 356
figs2-ramp-equals-step blocked ['blocked_by'] 356
figs3-egaba-unrelated-amplitude-rs blocked ['blocked_by'] 356
rm-awake-lower blocked ['blocked_by'] 356
fig2c-vm-depolarized blocked ['blocked_by'] 356
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat tools/readme_row.py | head -80; grep -n "Reproduced\|^| Dandiset\|^| Data" README.md | head
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
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
c=yaml.safe_load(open('claims/burman-2023.yaml'))
print({k:v for k,v in c.items() if k!='claims'})
for x in c['claims']:
    print('---',x['id'],x.get('kind'),x.get('data'),'|',{k:x[k] for k in x if k in('figure','location','source','where','central')})
    print(' ',str(x.get('statement',x.get('claim','')))[:400])
E
```

```
{'schema_version': 2, 'paper': 'doi:10.1016/j.neuron.2023.08.005', 'checks': [{'date': datetime.date(2026, 11, 10), 'kind': 'agent', 'model': 'claude-opus-5-5', 'ready': True, 'changes': ["Opening comment and the where fields of fig4f-model-hyperpolarizing-less-activity, fig4h-model-synchrony, fig4h-model-entropy and figs7-model-decoding. The simulation gist id was wrong (2ce61e4e790e... does not exist); the author's gist with that file and revision f6a05661 is 2ce61e4e57c7659b727d30e3e1e0128f.", 'Opening comment N7, and the criteria of fig4c-sample, fig4d-synchrony-lower-awake, fig4d-entropy-higher-awake, fig4-rate-higher-awake and figs6-rate-regressed. They counted a claim as reproduced when any of the four area and rate readings matched, while the Methods and the gist disagree on both (and on the waveform cut); the protocol (Reader, step 2) has the Methods give the main result and the code a variant, so each claim is now judged under A1F1, with the gist readings shown as variants.', 'Opening comment N6. The Methods\' population of "all recorded neurons" is open (the Figure 4C legend calls the 662 kept neurons recorded neurons); the gist, read at revision 43a13d89, builds it from the N2 units before any rate exclusion, so that is now stated, with kept units only as a variant.', 'figs6-rate-regressed criterion. Partial reproduction when the regression readings differed is replaced by the protocol rule (the author adopts the reading the paper best supports, as an assumption).', "fig4f-model-hyperpolarizing-less-activity criterion. The 18 of 20 runs rule is not in the paper; the activity comparison now uses the paired t test over pooled neurons that the paper applies to the model's per-neuron measures in Figure 4H, with the per-run count reported.", 'Checked against the gists. Analysis gist a77bcf5e at 43a13d89 matches N1 to N7 as written (stop_time, 2 to 12 ms, waveform_duration > 0.4, location[:3] in estim_target_region, np.sum of spike times in get_firing_rate, en
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
a=yaml.safe_load(open('attempts/burman-2023-01.yaml'))
for o in a['outcomes'][:12]:
    print('===',o['claim'],o['outcome']); print(yaml.safe_dump({k:v for k,v in o.items() if k not in('claim','outcome','notebook','output')},width=200,allow_unicode=True))
print(a['outcomes'][12].get('blocked_by'), a['outcomes'][12]['notes'])
E
```

```
=== dataset-sessions-link reproduced
notes: All 17 files the gist lists are in version 0.230317.0039, each with spike_times, location and waveform_duration in its units table, stimulus_type, behavioral_epoch, is_valid, estim_target_region
  and stop_time in its trials table, and awake and isoflurane electrical trials. They hold 16 subjects (sub-569073 twice, one MOs and one SSp session). Unit ids equal row numbers in every file, so the gist's
  keying of units by row and lookup by id select the same units. The version holds seven more files, six with EEG only and sub-599017 with units and SSp stimulation, which the gist does not read. The clock
  check covers all 17 files. In 33 of 34 file and condition pairs, spikes 2 to 12 ms after the pulse exceed those of the same window 1.5 s before and after it (1.5 to 39 times, Wilcoxon p below 0.001);
  the exception is the awake trials of sub-569069_ses-20210312 (1.55 against 1.45 spikes per trial, p = 0.59), whose isoflurane trials, on the same file clock, pass (2.2 times, p = 2e-12).

=== fig4c-sample partially_reproduced
deviations:
- Judged under the Methods reading A1F1, as the claims file requires. The paper's numbers come out exactly under the gist's rate (A1F2, A2F2), which sums spike latencies where a count is expected; this
  claim holds fully only under that variant.
- Trials of all stimulus currents and depths of a session are pooled and times are taken from stop_time, as the claims file (N3) gives from the gist; the Methods say only "following an electrical stimulus".
  Timing from start_time, the pulse onset 0.4 ms earlier, is run as a variant under A1F1, with 734 units kept and 131 excluded, and synchrony, entropy, the rate test and the regressions keep their direction.
- The Methods' waveform cut (>= 0.4 ms) and the gist's (> 0.4 ms) select the same units, as no unit has a duration of exactly 0.4 ms; readings A1 and A2 also select the same 865 units, as the SSp sessions
  hold only SSp-ll and SSp-tr units.
m
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
a=yaml.safe_load(open('attempts/burman-2023-01.yaml'))
print(yaml.safe_dump(a['findings'],width=200,allow_unicode=True))
v=a['verifications']
print(type(v), len(v))
for x in v:
    print(yaml.safe_dump({k:(val if k!='outcomes' else '...') for k,val in x.items()},width=200,allow_unicode=True)[:3000])
E
```

```
- kind: code_mismatch
  statement: The paper's analysis code computes the evoked firing rate used for the exclusion (below 0.1 Hz or above 200 Hz) as the sum of the spikes' latencies in ms (np.sum of spike_times) over trials
    times 10 ms, where the Methods describe an average evoked firing rate. With this rate the dataset gives the paper's sample exactly (662 kept, 203 excluded, median 34 per recording, 1 to 93) and its
    Figure 4D means (synchrony 0.325 and 0.393, entropy 1.347 and 1.111); with the spike-count rate it gives 721 kept and 144 excluded. The 200 Hz bound thus acted on spike-count rates near 45 Hz.
- kind: selection_undocumented
  statement: Version 0.230317.0039 holds 18 files with units and electrical stimulation awake and under isoflurane; the paper uses 17. sub-599017_ses-20220210 (943 units, SSp stimulation, 718 awake and
    720 isoflurane valid trials) is not in the paper's code list, and the paper does not say why. Six further files hold EEG only, with no units.
- kind: data_missing
  statement: The paper's gramicidin perforated patch recordings (Figures 1 to 3, S1 to S5), which carry most of its findings, are not in DANDI:000458 nor in any other dandiset found; the paper offers them
    on request. 24 of its claims cannot be tested.
- kind: code_mismatch
  statement: The Methods select regular spiking units with a waveform duration of 0.4 ms or more, the code more than 0.4 ms, and the Methods name the areas SSp-ll, SSp-tr and MOs where the code takes every
    unit whose location begins with the stimulated region. Neither difference changes the units selected in this dataset.
- kind: methods_unavailable
  statement: For the multi-compartment model of Figure S4 (figs4-intrinsic-properties), which measure of the simulated ramp estimates of synaptic E_GABAAR, under the anesthetized and awake membrane properties
    of Table 2, is compared with what, and what result shows that the membrane properties "could not explain" the measured difference
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
a=yaml.safe_load(open('attempts/burman-2023-01.yaml'))
for i,x in enumerate(a['verifications']):
    r=x['results']; print(i, len(r), sum(1 for y in r if y['agrees']), [y['claim'] for y in r if not y['agrees']], [k for k in x if k!='results'])
    for y in r[4:12]: print('  ',y['claim'],'|',y['reason'][:500],'||',y.get('response','')[:500])
E
python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:3] if isinstance(d,dict) else d[0].keys())
"
```

```
0 35 35 [] ['date', 'kind', 'by', 'reviewed']
   fig4-rate-higher-awake | Under A1F1, 14.0 Hz awake against 7.59 Hz isoflurane, paired t = 12.4, p far below 0.05; holds under every reading, and 15 of 17 recordings go the same way. The p values print as 0.00e+00 because they are rounded before formatting (B4). || The p values are now formatted before rounding (A1F1 p = 5.75e-32), in the notebook and the notes. Outcome unchanged.
   figs6-rate-regressed | Under A1F1 synchrony is negative and entropy positive under R1, R2 and R3, all p < 1e-10, and the same under every variant. The Figure S6 legend was not available, so it could not see which regression the paper used. || No change.
   fig4f-model-hyperpolarizing-less-activity | 8.785 Hz hyperpolarizing against 19.468 Hz shunting, paired p about 0; lower in 20 of 20 runs. network.py is checked only against its own whole-run-stimulus mode, not against the gist, and that Brian 2 rereads eta from the mutated namespace is supported only indirectly by the summed weights. || The gist is now run unmodified on the small run with the same seed (network.run_gist, a sanity cell); it gives the same 19,093 excitatory spikes and the same per-neuron rate, entropy and synchrony for all 800 neurons. Each full run now records eta from the plastic synapses' compiled code after each run, 0.1 for balancing and 0 for the test in all 20. Outcome unchanged.
   fig4h-model-synchrony | Shunting 0.7833 is inside tolerance; hyperpolarizing 0.8789 is outside (0.880 to 0.882); shunting is lower, p about 0, in 20 of 20 runs. The tolerance, the paper's SEM over 16,000 pooled neurons, is too tight for runs with different seeds; the run-to-run SE of a 20-run mean is 0.0013, and the miss is 1.6 of these, so the partial outcome comes from the criterion, not the model (B2, a point about the claims file). || The notebook now prints the run-to-run SE of the 20-run mean and each mean's distance from the paper's value in units of it (hyperpolarizing 0.0013, 1
[... 14 more lines not kept]
```

**Agent**

Both verification rounds agreed with all 35 outcomes. Next I'm reading the dandisets entry and the reports.

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(list(d))
for k,v in d.items():
  if isinstance(v,(list,dict)):
    it=v if isinstance(v,list) else list(v.values())
    for x in it:
      if '000458' in json.dumps(x)[:300]: print(json.dumps(x,indent=1)[:3000])
"; ls -la transcripts/burman-2023/; cat transcripts/burman-2023/author-report.md
```

```
['schema_version', 'generated', 'source', 'counts', 'targets']
{
 "dandiset": "000458",
 "name": "Simultaneous electroencephalography, extracellular electrophysiology, and cortical electrical stimulation in head-fixed mice",
 "published_version": "0.230317.0039",
 "asset_count": 24,
 "size_gb": 361.48,
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
   "doi": "10.7554/elife.84630",
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/burman-2023; for f in claims-report claims-check-report answer-report author-answers-report verifier-1-report author-revise-1-report verifier-2-report author-revise-2-report; do echo "=== $f"; cat $f.md; done
```

```
<persisted-output>
Output too large (30KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/472e6d7c-cb84-4905-bbc2-a7121703abf1/tool-results/bctxjrilt.txt

Preview (first 2KB):
=== claims-report
I've written `claims/burman-2023.yaml`. The quote checker reports 35 claims, 34 quotes, 27 statistical values and 0 problems. Nothing was committed.

**Text read.** The version of record (open access, Europe PMC PMC11913778): main text, the legends of Figures 1 to 4, and the STAR Methods with Tables 1 and 2. **The supplement (Figures S1 to S7 and their legends) is not in the text, and there is no PDF.** I went ahead because the main results, including every number for Figure 4A to 4D, are in the main text. Only `figs6-rate-regressed` needs a method found only in the supplement. Claims on S2 to S5 and S7 rest on the main-text sentences that cite those figures, and their tests are unknown.

**Code read:**
- Neuropixels analysis gist `a77bcf5e`, revision 43a13d89. It names DANDI:000458 version 0.230317.0039 and the 17 sessions.
- Network simulation gist `2ce61e4e`, revision f6a05661.
- The `richardjburman/burman-et-al-2022---Awake-EGABAAR` repository at a404c3e: the NEURON model for Figure S4.

**Claims:**
- **Counts:** 35 claims. 34 have quotes; the one without is the link claim (`dataset-sessions-link`), which checks that the 17 sessions are in the dataset with the fields the code uses. 24 claims carry statistics (27 entries), 25 have expected values, and all 35 have criteria.
- **Testable on DANDI:000458:** 6 claims (the session link, the sample counts, synchrony, entropy, firing rate, and Figure S6).
- **Not testable:** 24 patch-clamp claims (Figures 1 to 3, S2, S3, S5). DANDI:000458 is only the Claar et al. Neuropixels data, and the paper deposits its own recordings nowhere ("available on request").
- **Model claims:** 5, marked `data: elsewhere` and pointing at the simulation code (Figure 4F/H, S4, S7).

[... 5 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/472e6d7c-cb84-4905-bbc2-a7121703abf1/tool-results/bctxjrilt.txt"
}
```

```
1	=== claims-report
2	I've written `claims/burman-2023.yaml`. The quote checker reports 35 claims, 34 quotes, 27 statistical values and 0 problems. Nothing was committed.
3	
4	**Text read.** The version of record (open access, Europe PMC PMC11913778): main text, the legends of Figures 1 to 4, and the STAR Methods with Tables 1 and 2. **The supplement (Figures S1 to S7 and their legends) is not in the text, and there is no PDF.** I went ahead because the main results, including every number for Figure 4A to 4D, are in the main text. Only `figs6-rate-regressed` needs a method found only in the supplement. Claims on S2 to S5 and S7 rest on the main-text sentences that cite those figures, and their tests are unknown.
5	
6	**Code read:**
7	- Neuropixels analysis gist `a77bcf5e`, revision 43a13d89. It names DANDI:000458 version 0.230317.0039 and the 17 sessions.
8	- Network simulation gist `2ce61e4e`, revision f6a05661.
9	- The `richardjburman/burman-et-al-2022---Awake-EGABAAR` repository at a404c3e: the NEURON model for Figure S4.
10	
11	**Claims:**
12	- **Counts:** 35 claims. 34 have quotes; the one without is the link claim (`dataset-sessions-link`), which checks that the 17 sessions are in the dataset with the fields the code uses. 24 claims carry statistics (27 entries), 25 have expected values, and all 35 have criteria.
13	- **Testable on DANDI:000458:** 6 claims (the session link, the sample counts, synchrony, entropy, firing rate, and Figure S6).
14	- **Not testable:** 24 patch-clamp claims (Figures 1 to 3, S2, S3, S5). DANDI:000458 is only the Claar et al. Neuropixels data, and the paper deposits its own recordings nowhere ("available on request").
15	- **Model claims:** 5, marked `data: elsewhere` and pointing at the simulation code (Figure 4F/H, S4, S7).
16	
17	**Details left open, and the readings named:**
18	- **Area selection:** (A1) the Methods' annotations SSp-ll, SSp-tr or MOs; (A2) the code's first three characters of `location` matched against `estim_ta
[... 219 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -60 claims/burman-2023.yaml; grep -n "^# " attempts/burman-2023-01.yaml | head
```

```
# Claims for Burman, Brodersen, Raimondo, Sen & Akerman (2023), Neuron 111, 3531-3540,
# "Active cortical networks promote shunting fast synaptic inhibition in vivo", on dandiset 000458.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read. The version of record (open access, CC BY), full text from Europe PMC (PMC11913778),
# in paper/10.1016-j.neuron.2023.08.005.txt: Summary, Introduction, Results, the legends of
# Figures 1 to 4, Discussion, STAR Methods with Tables 1 and 2, and Data and code availability.
# The supplement (Document S1, Figures S1 to S7 and their legends) is not in the text, and no PDF
# was supplied. No claim on the dandiset needs it except figs6-rate-regressed, whose method is
# only in the Figure S6 legend; that claim names readings. The claims on Figures S2 to S5 and S7
# rest on the main-text sentences that cite them, and their tests are not known here.
#
# Code read. (1) gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf, revision
# 43a13d89441b7f56e835e84fa5811d9567917daf, burman_et_al_2023_neuropixel_data_analysis.py: reads
# the 17 NWB sessions of DANDI:000458 (version 0.230317.0039, named in its docstring) and writes,
# per unit, evoked firing rate, peri-stimulus histogram entropy and synchrony for the awake and
# isoflurane epochs. It does not hold the exclusion step, the statistics or the plots.
# (2) gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f, revision
# f6a05661c10051560aa381e334099efd8521617b, burman_et_al_2023_neuronal_network_simulation.py: the
[... 40 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/burman-2023-01.md",
 "content": "# burman-2023, Burman et al. 2023\n\nOn the dandiset two claims reproduced, three partially, none not reproduced and\n24 blocked, all 24 for missing data; no outcome rests on an assumption. These\ncounts leave out the link check `dataset-sessions-link` (reproduced) and the\nfive model claims, whose data the paper's code generates: of those\n`fig4f-model-hyperpolarizing-less-activity` and `figs7-model-decoding`\nreproduced, `fig4h-model-synchrony` and `fig4h-model-entropy` are partial and\n`figs4-intrinsic-properties` is blocked, for methods underspecified. Both\nverification rounds agreed with all 35 outcomes, and nothing was proposed after\nthe second, so there was no third round. The paper, Burman, Brodersen, Raimondo,\nSen and Akerman in Neuron (111, 3531-3540), uses gramicidin perforated patch\nrecordings of L2/3 pyramidal neurons in mouse V1 to report that synaptic\nE_GABAAR is more depolarized and fast inhibition shunting in awake cortex\n(Figures 1 to 3), and reanalyses the Allen Institute Neuropixels recordings of\nClaar et al. in DANDI:000458, with a network model, to report that neurons are\nless synchronous with the population and more variable in their evoked spike\ntimes awake than under isoflurane (Figure 4). The claims were written from the\nversion of record (PMC11913778) as Europe PMC text without a PDF or the\nsupplement (Figures S1 to S7 and their legends), and from the paper's\nNeuropixels analysis gist, its network simulation gist and its NEURON model\nrepository; the claims check corrected the simulation gist's id, made each\ndataset claim be judged under the Methods reading (A1F1) with the gist's\nreadings as variants, and replaced two criteria rules not in the paper, for 35\nclaims. Only the six Neuropixels claims and the model claims could be tested.\nReproduced are `fig4-rate-higher-awake` (14.00 against 7.59 Hz over 721 units,\np = 5.75e-32) and `figs6-rate-regressed`, where all three regression readings\nagree with p below 1e-10. Partial are `fig4c-sample` (721 kept and 144 excluded\nagainst 662 and 203), `fig4d-synchrony-lower-awake` (0.3188 against 0.3862,\nthe awake mean just below 0.325 +- 0.005) and `fig4d-entropy-higher-awake`\n(1.3887 against 1.1502 nats, both outside tolerance), each with the direction\nand test holding. The model's hyperpolarizing means miss their tolerances by\n0.0011 and 0.0024, 1.6 and 1.9 standard errors of a 20-run mean, as the\ntolerance, the paper's SEM over pooled neurons, is narrower than the spread\nbetween seeds. Blocked are the 24 patch-clamp claims and figs4, whose\ncomparison is only in the unread Figure S4 legend. The author asked no\nquestions of a reader at first, so the answer and author-answers runs changed\nnothing. Round 1 held that the three partial outcomes reflect the paper's own\nrate code, that the model tolerances are too tight for runs with different\nseeds, that figs4's block reason did not mention the public NEURON model, that\np-values printed as zero and that the clock check covered 2 of 17 files; in\nreply both gists were run unmodified on the loaded data and agreed with the\nattempt's code, the clock check was extended to all 17 files, figs4 moved from\n`other` to methods_underspecified with a question to the paper's authors, and\nthe first two points went as questions to a reader in\n`questions/burman-2023.yaml`, still unanswered. Round 2 found sentences the\noutputs did not support, among them a decoding t that differed between\nexecutions and a start_time variant described where it was not run; in reply\nthe decoding was traced to ties among nearest neighbours that break differently\non different runners (t = 16.35 to 17.22 under five other orders, shunting\nhigher in 20 of 20 runs each time), the start_time variant was run for every\nclaim, and a third question, on the fig4c criterion's partial case, went to a\nreader. The author's run took about 2 h 10 min; the notebooks ran in 123 s and\n1903 s at first, 201 s and 1585 s after the author-answers run, 142 s and 949 s\nafter round 1 and 152 s and 1028 s after round 2. During development a parallel\ntest with 2 repeats failed, as 5-fold cross-validation needs 5, and the loader\ncrashed on the six files with no units table; nothing failed in the final runs.\n\nThe paper's gramicidin perforated patch recordings (Figures 1 to 3, S1 to S5),\nwhich carry most of its findings, are not in DANDI:000458 nor in any other\ndandiset found, and the paper offers them on request, so 24 of its claims\ncannot be tested. The paper's analysis code computes the evoked firing rate\nused for the exclusion (below 0.1 Hz or above 200 Hz) as the sum of the spikes'\nlatencies in ms over trials times 10 ms, where the Methods describe an average\nevoked firing rate; with this rate the dataset gives the paper's sample exactly\n(662 kept, 203 excluded, median 34 per recording, 1 to 93) and its Figure 4D\nmeans (synchrony 0.325 and 0.393, entropy 1.347 and 1.111), and with the\nspike-count rate it gives 721 kept and 144 excluded, so the 200 Hz bound acted\non spike-count rates near 45 Hz. The paper's entropy means are over the 597\nunits defined in both conditions, though it gives n = 662. Version\n0.230317.0039 holds 18 files with units and electrical stimulation awake and\nunder isoflurane, and the paper uses 17; sub-599017_ses-20220210 (943 units,\nSSp stimulation, 718 awake and 720 isoflurane valid trials) is not in the\npaper's code list, and the paper does not say why. Six further files hold EEG\nonly, with no units. The Methods select regular spiking units with a waveform\nduration of 0.4 ms or more, the code more than 0.4 ms, and the Methods name the\nareas SSp-ll, SSp-tr and MOs where the code takes every unit whose location\nbegins with the stimulated region; neither difference changes the units\nselected in this dataset. Unit ids equal row numbers in every file, so the\ngist's keying of units by row and lookup by id select the same units. In 33 of\n34 file and condition pairs evoked spikes exceed those of shifted windows; the\nexception is the awake trials of sub-569069_ses-20210312 (1.55 against 1.45\nspikes per trial, p = 0.59), whose isoflurane trials pass. A question is put to\nthe paper's authors: for the model of Figure S4, which measure of the simulated\nramp estimates of synaptic E_GABAAR is compared with what, and what result\nshows that the membrane properties \"could not explain\" the measured difference.\n\nThe author's points on the protocol: there is no block reason for a claim whose\nmethod lives only in a supplement that was not supplied; the Methods reading\ndecides the outcome even when the code's reading reproduces the paper exactly;\n\"fix every random seed\" conflicts with a criterion that takes the gist's seeds,\nwhich are none; the protocol says nothing about changing an outside input's\ncode, as was done to hold the simulation's 4 GB stimulus array in memory; it has\nno rule for stochastic simulations whose pooled-neuron SEM is narrower than the\nspread between seeds; the clock-check guidance of decoding a task variable is\nheavier than needed here; and `entry.py check` requires every notebook to name\nthe dataset, including the simulation-only one.\n"
}
```

```
File created successfully at: docs/pilot-notes/burman-2023-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; python - <<'E'
p='burman-2023-01.md'; s=open(p).read()
s=s.replace("readings as variants, and replaced two criteria rules not in the paper, for 35\nclaims.","readings as variants, and replaced two criterion rules, one of them not in the\npaper, for 35 claims.")
s=s.replace("the start_time variant was run for every\nclaim,","the start_time variant was run for every\ndataset claim,")
open(p,'w').write(s)
E
grep -n "criterion rules\|every$\|dataset claim," burman-2023-01.md; grep -c "—\|rather" burman-2023-01.md
```

```
24:readings as variants, and replaced two criterion rules, one of them not in the
51:higher in 20 of 20 runs each time), the start_time variant was run for every
52:dataset claim, and a third question, on the fig4c criterion's partial case, went to a
0
```

**Agent calls Bash**

```bash
cd  cat > summaries/burman-2023-01.md <<'E'
The paper's central patch-clamp findings, that synaptic GABAA receptor reversal is more depolarized and inhibition shunting in awake cortex and that blocking local network activity undoes this, could not be tested, as those recordings are not deposited. Its Neuropixels finding that neurons are less synchronous and more variable in spike timing awake than under isoflurane held up in direction and test, with means slightly off. The paper's exact numbers come out only with the firing rate its analysis code computes, not the one its Methods describe (144 units excluded against 203). In the network model, shunting inhibition gave lower synchrony, higher entropy and better decoding in every run, with two means just outside tight tolerances. Higher awake firing and the rate-regressed control also held.
E
wc -w summaries/burman-2023-01.md; git status --short
```

```
124 summaries/burman-2023-01.md
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
?? docs/pilot-notes/burman-2023-01.md
?? scripts
?? summaries/burman-2023-01.md
```

**Agent calls Bash**

```bash
cd  cat > summaries/burman-2023-01.md <<'E'
The paper's central patch-clamp findings, that synaptic GABAA receptor reversal is more depolarized and inhibition shunting in awake cortex and that blocking local network activity undoes this, could not be tested, as those recordings are not deposited. Its Neuropixels finding that neurons are less synchronous and more variable in spike timing awake than under isoflurane held up in direction and test, with means slightly off. The paper's exact numbers come out only with the firing rate its code computes, not the one its Methods describe (144 units excluded against 203). In the network model, shunting inhibition gave lower synchrony, higher entropy and better decoding in every run, two means falling just outside tight tolerances. Higher awake firing and the rate-regressed control also held.
E
wc -w summaries/burman-2023-01.md; cat docs/pilot-notes/burman-2023-01.md
```

```
123 summaries/burman-2023-01.md
# burman-2023, Burman et al. 2023

On the dandiset two claims reproduced, three partially, none not reproduced and
24 blocked, all 24 for missing data; no outcome rests on an assumption. These
counts leave out the link check `dataset-sessions-link` (reproduced) and the
five model claims, whose data the paper's code generates: of those
`fig4f-model-hyperpolarizing-less-activity` and `figs7-model-decoding`
reproduced, `fig4h-model-synchrony` and `fig4h-model-entropy` are partial and
`figs4-intrinsic-properties` is blocked, for methods underspecified. Both
verification rounds agreed with all 35 outcomes, and nothing was proposed after
the second, so there was no third round. The paper, Burman, Brodersen, Raimondo,
Sen and Akerman in Neuron (111, 3531-3540), uses gramicidin perforated patch
recordings of L2/3 pyramidal neurons in mouse V1 to report that synaptic
E_GABAAR is more depolarized and fast inhibition shunting in awake cortex
(Figures 1 to 3), and reanalyses the Allen Institute Neuropixels recordings of
Claar et al. in DANDI:000458, with a network model, to report that neurons are
less synchronous with the population and more variable in their evoked spike
times awake than under isoflurane (Figure 4). The claims were written from the
version of record (PMC11913778) as Europe PMC text without a PDF or the
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > summaries/burman-2023-01.md <<'E'
The paper's central patch-clamp findings, that synaptic GABAA receptor reversal is more depolarized and inhibition shunting in awake cortex and that blocking local network activity undoes this, could not be tested, as those recordings are not deposited. Its Neuropixels finding that neurons are less synchronous and more variable in spike timing awake than under isoflurane held up in direction and test, with means slightly off. The paper's exact numbers come out only with the firing rate its code computes, not the one its Methods describe (144 units excluded against 203). In the network model, shunting inhibition gave lower synchrony, higher entropy and better decoding in every run, two means just outside tight tolerances. Higher awake firing and the rate-regressed control also held.
E
wc -w summaries/burman-2023-01.md
python - <<'E'
p='docs/pilot-notes/burman-2023-01.md'; s=open(p).read()
s=s.replace("paper, for 35 claims. Only the six Neuropixels claims and the model claims could be tested.\n","paper, for 35 claims. Only the six Neuropixels claims and the model claims\ncould be tested.\n")
s=s.replace("dataset claim, and a third question, on the fig4c criterion's partial case, went to a\nreader.","dataset claim, and a third question, on the fig4c criterion's partial case,\nwent to a reader.")
open(p,'w').write(s)
E
awk 'length>80' docs/pilot-notes/burman-2023-01.md
```

```
122 summaries/burman-2023-01.md
went to a reader. The author's run took about 2 h 10 min; the notebooks ran in 123 s and
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='docs/pilot-notes/burman-2023-01.md'; s=open(p).read()
s=s.replace("went to a reader. The author's run took about 2 h 10 min; the notebooks ran in 123 s and\n1903 s at first,","went to a reader. The author's run took about 2 h 10 min; the notebooks ran in\n123 s and 1903 s at first,")
open(p,'w').write(s)
E
cat > summaries/burman-2023-01.md <<'E'
The paper's central patch-clamp findings, that synaptic GABAA receptor reversal is more depolarized and inhibition shunting in awake cortex and that blocking local network activity undoes this, could not be tested, as those recordings are not deposited. Its Neuropixels finding that neurons are less synchronous and more variable in spike timing awake than under isoflurane held up in direction and test, with means slightly off. Exact numbers come out only with the firing rate the paper's code computes, not the Methods' rate (144 units excluded against 203). The network model's shunting inhibition gave lower synchrony, higher entropy and better decoding in every run, two means just outside tight tolerances. Higher awake firing and the rate-regressed control also held.
E
wc -w summaries/burman-2023-01.md; awk 'length>80' docs/pilot-notes/burman-2023-01.md
```

```
118 summaries/burman-2023-01.md
123 s and 1903 s at first, 201 s and 1585 s after the author-answers run, 142 s and 949 s
```

**Agent calls Bash**

```bash
cd  sed -n 40,60p docs/pilot-notes/burman-2023-01.md
```

```
rate code, that the model tolerances are too tight for runs with different
seeds, that figs4's block reason did not mention the public NEURON model, that
p-values printed as zero and that the clock check covered 2 of 17 files; in
reply both gists were run unmodified on the loaded data and agreed with the
attempt's code, the clock check was extended to all 17 files, figs4 moved from
`other` to methods_underspecified with a question to the paper's authors, and
the first two points went as questions to a reader in
`questions/burman-2023.yaml`, still unanswered. Round 2 found sentences the
outputs did not support, among them a decoding t that differed between
executions and a start_time variant described where it was not run; in reply
the decoding was traced to ties among nearest neighbours that break differently
on different runners (t = 16.35 to 17.22 under five other orders, shunting
higher in 20 of 20 runs each time), the start_time variant was run for every
dataset claim, and a third question, on the fig4c criterion's partial case,
went to a reader. The author's run took about 2 h 10 min; the notebooks ran in
123 s and 1903 s at first, 201 s and 1585 s after the author-answers run, 142 s and 949 s
after round 1 and 152 s and 1028 s after round 2. During development a parallel
test with 2 repeats failed, as 5-fold cross-validation needs 5, and the loader
crashed on the six files with no units table; nothing failed in the final runs.

[... 2 more lines not kept]
```

**Agent**

I wrote both files, `docs/pilot-notes/burman-2023-01.md` and `summaries/burman-2023-01.md`, and changed nothing else. Nothing is committed.

# burman-2023, Burman et al. 2023

On the dandiset two claims reproduced, three partially, none not reproduced and 24 blocked, all 24 for missing data; no outcome rests on an assumption. These counts leave out the link check `dataset-sessions-link` (reproduced) and the five model claims, whose data the paper's code generates: of those `fig4f-model-hyperpolarizing-less-activity` and `figs7-model-decoding` reproduced, `fig4h-model-synchrony` and `fig4h-model-entropy` are partial and `figs4-intrinsic-properties` is blocked, for methods underspecified. Both verification rounds agreed with all 35 outcomes, and nothing was proposed after the second, so there was no third round. The paper, Burman, Brodersen, Raimondo, Sen and Akerman in Neuron (111, 3531-3540), uses gramicidin perforated patch recordings of L2/3 pyramidal neurons in mouse V1 to report that synaptic E_GABAAR is more depolarized and fast inhibition shunting in awake cortex (Figures 1 to 3), and reanalyses the Allen Institute Neuropixels recordings of Claar et al. in DANDI:000458, with a network model, to report that neurons are less synchronous with the population and more variable in their evoked spike times awake than under isoflurane (Figure 4). The claims were written from the version of record (PMC11913778) as Europe PMC text without a PDF or the supplement (Figures S1 to S7 and their legends), and from the paper's Neuropixels analysis gist, its network simulation gist and its NEURON model repository; the claims check corrected the simulation gist's id, made each dataset claim be judged under the Methods reading (A1F1) with the gist's readings as variants, and replaced two criterion rules, one of them not in the paper, for 35 claims. Only the six Neuropixels claims and the model claims could be tested. Reproduced are `fig4-rate-higher-awake` (14.00 against 7.59 Hz over 721 units, p = 5.75e-32) and `figs6-rate-regressed`, where all three regression readings agree with p below 1e-10. Partial are `fig4c-sample` (721 kept and 144 excluded against 662 and 203), `fig4d-synchrony-lower-awake` (0.3188 against 0.3862, the awake mean just below 0.325 +- 0.005) and `fig4d-entropy-higher-awake` (1.3887 against 1.1502 nats, both outside tolerance), each with the direction and test holding. The model's hyperpolarizing means miss their tolerances by 0.0011 and 0.0024, 1.6 and 1.9 standard errors of a 20-run mean, as the tolerance, the paper's SEM over pooled neurons, is narrower than the spread between seeds. Blocked are the 24 patch-clamp claims and figs4, whose comparison is only in the unread Figure S4 legend. The author asked no questions of a reader at first, so the answer and author-answers runs changed nothing. Round 1 held that the three partial outcomes reflect the paper's own rate code, that the model tolerances are too tight for runs with different seeds, that figs4's block reason did not mention the public NEURON model, that p-values printed as zero and that the clock check covered 2 of 17 files; in reply both gists were run unmodified on the loaded data and agreed with the attempt's code, the clock check was extended to all 17 files, figs4 moved from `other` to methods_underspecified with a question to the paper's authors, and the first two points went as questions to a reader in `questions/burman-2023.yaml`, still unanswered. Round 2 found sentences the outputs did not support, among them a decoding t that differed between executions and a start_time variant described where it was not run; in reply the decoding was traced to ties among nearest neighbours that break differently on different runners (t = 16.35 to 17.22 under five other orders, shunting higher in 20 of 20 runs each time), the start_time variant was run for every dataset claim, and a third question, on the fig4c criterion's partial case, went to a reader. The author's run took about 2 h 10 min; the notebooks ran in 123 s and 1903 s at first, 201 s and 1585 s after the author-answers run, 142 s and 949 s after round 1 and 152 s and 1028 s after round 2. During development a parallel test with 2 repeats failed, as 5-fold cross-validation needs 5, and the loader crashed on the six files with no units table; nothing failed in the final runs.

The paper's gramicidin perforated patch recordings (Figures 1 to 3, S1 to S5), which carry most of its findings, are not in DANDI:000458 nor in any other dandiset found, and the paper offers them on request, so 24 of its claims cannot be tested. The paper's analysis code computes the evoked firing rate used for the exclusion (below 0.1 Hz or above 200 Hz) as the sum of the spikes' latencies in ms over trials times 10 ms, where the Methods describe an average evoked firing rate; with this rate the dataset gives the paper's sample exactly (662 kept, 203 excluded, median 34 per recording, 1 to 93) and its Figure 4D means (synchrony 0.325 and 0.393, entropy 1.347 and 1.111), and with the spike-count rate it gives 721 kept and 144 excluded, so the 200 Hz bound acted on spike-count rates near 45 Hz. The paper's entropy means are over the 597 units defined in both conditions, though it gives n = 662. Version 0.230317.0039 holds 18 files with units and electrical stimulation awake and under isoflurane, and the paper uses 17; sub-599017_ses-20220210 (943 units, SSp stimulation, 718 awake and 720 isoflurane valid trials) is not in the paper's code list, and the paper does not say why. Six further files hold EEG only, with no units. The Methods select regular spiking units with a waveform duration of 0.4 ms or more, the code more than 0.4 ms, and the Methods name the areas SSp-ll, SSp-tr and MOs where the code takes every unit whose location begins with the stimulated region; neither difference changes the units selected in this dataset. Unit ids equal row numbers in every file, so the gist's keying of units by row and lookup by id select the same units. In 33 of 34 file and condition pairs evoked spikes exceed those of shifted windows; the exception is the awake trials of sub-569069_ses-20210312 (1.55 against 1.45 spikes per trial, p = 0.59), whose isoflurane trials pass. A question is put to the paper's authors: for the model of Figure S4, which measure of the simulated ramp estimates of synaptic E_GABAAR is compared with what, and what result shows that the membrane properties "could not explain" the measured difference.

The author's points on the protocol: there is no block reason for a claim whose method lives only in a supplement that was not supplied; the Methods reading decides the outcome even when the code's reading reproduces the paper exactly; "fix every random seed" conflicts with a criterion that takes the gist's seeds, which are none; the protocol says nothing about changing an outside input's code, as was done to hold the simulation's 4 GB stimulus array in memory; it has no rule for stochastic simulations whose pooled-neuron SEM is narrower than the spread between seeds; the clock-check guidance of decoding a task variable is heavier than needed here; and `entry.py check` requires every notebook to name the dataset, including the simulation-only one.

Summary (`summaries/burman-2023-01.md`, 118 words):

The paper's central patch-clamp findings, that synaptic GABAA receptor reversal is more depolarized and inhibition shunting in awake cortex and that blocking local network activity undoes this, could not be tested, as those recordings are not deposited. Its Neuropixels finding that neurons are less synchronous and more variable in spike timing awake than under isoflurane held up in direction and test, with means slightly off. Exact numbers come out only with the firing rate the paper's code computes, not the Methods' rate (144 units excluded against 203). The network model's shunting inhibition gave lower synchrony, higher entropy and better decoding in every run, two means just outside tight tolerances. Higher awake firing and the rate-regressed control also held.

## End of run

23 turns, 2 minutes, $1.06 at API prices, result: success.
