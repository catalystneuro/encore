# crcns-ia-1 · recorder · run 41916843665

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py crcns-ia-1; ls claims/crcns-ia-1/ transcripts/crcns-ia-1/; cat attempts/crcns-ia-1-eyherabide-2008-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if 'ia-1' in json.dumps(x): print(json.dumps(x,indent=1))"
```

```
<persisted-output>
Output too large (85.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/c9c61486-2fd1-4ec9-b234-eb5c6d272c56/tool-results/blxkcv4ht.txt

Preview (first 2KB):
docs/pilot-notes/crcns-hc-9-quattrocolo-2013-01.md
docs/pilot-notes/000252-guan-2022-01.md
docs/pilot-notes/001868-kim-2026-01.md
docs/pilot-notes/001882-yuan-2025-01.md
docs/pilot-notes/001767-chantranupong-2023-01.md
| [CRCNS:ia-1](https://crcns.org/data-sets/ia/ia-1) | [Eyherabide et al. 2008](https://doi.org/10.3389/neuro.10.003.2008) | 11 | 5 | 7 | 3 | [`crcns-ia-1-eyherabide-2008`](entries/crcns-ia-1-eyherabide-2008) |
claims/crcns-ia-1/:
10.3389-neuro.10.003.2008.yaml

transcripts/crcns-ia-1/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd  F=/home/runner/.claude/projects/-home-runner-work-encore-encore/c9c61486-2fd1-4ec9-b234-eb5c6d272c56/tool-results/blxkcv4ht.txt; grep -n "catalystneuro\|^{" $F | head; wc -l $F; grep -n "| Dataset\|^| ---" README.md | head -3; for f in crcns-hc-9-quattrocolo-2013-01 000252-guan-2022-01 001868-kim-2026-01 001882-yuan-2025-01 001767-chantranupong-2023-01 001754-knierim-2000-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done
```

```
<persisted-output>
Output too large (47KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/c9c61486-2fd1-4ec9-b234-eb5c6d272c56/tool-results/b2eebpcw5.txt

Preview (first 2KB):
53:    url: https://github.com/catalystneuro/encore/actions/runs/41885596452
1297 /home/runner/.claude/projects/-home-runner-work-encore-encore/c9c61486-2fd1-4ec9-b234-eb5c6d272c56/tool-results/blxkcv4ht.txt
=== crcns-hc-9-quattrocolo-2013-01
# crcns-hc-9, Quattrocolo et al. 2013

One claim reproduced (on an assumption), none partially, none not reproduced
and 25 blocked, all 25 for missing data. The first verification round agreed
with all 26 outcomes and the second with all 26; nothing was proposed after the
second, so there was no third round. CRCNS does not version data sets, so the
version is recorded as unversioned and pinned by the MD5 of the zip, which
matches `checksums.md5`. The paper, Quattrocolo and Maccaferri, "Novel
GABAergic Circuits Mediating Excitation/Inhibition of Cajal-Retzius Cells in
the Developing Hippocampus" in the Journal of Neuroscience, records
Cajal-Retzius cells and their GABAergic inputs in acute hippocampal slices of
CXCR4-EGFP and Sst-IRES-Cre;ChR2(H134R)-EYFP mice aged P10 to P19, with paired
recordings, optogenetic stimulation of O-LM cells, cell-attached recordings and
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/c9c61486-2fd1-4ec9-b234-eb5c6d272c56/tool-results/b2eebpcw5.txt"
}
```

```
1	53:    url: https://github.com/catalystneuro/encore/actions/runs/41885596452
2	1297 /home/runner/.claude/projects/-home-runner-work-encore-encore/c9c61486-2fd1-4ec9-b234-eb5c6d272c56/tool-results/blxkcv4ht.txt
3	=== crcns-hc-9-quattrocolo-2013-01
4	# crcns-hc-9, Quattrocolo et al. 2013
5	
6	One claim reproduced (on an assumption), none partially, none not reproduced
7	and 25 blocked, all 25 for missing data. The first verification round agreed
8	with all 26 outcomes and the second with all 26; nothing was proposed after the
9	second, so there was no third round. CRCNS does not version data sets, so the
10	version is recorded as unversioned and pinned by the MD5 of the zip, which
11	matches `checksums.md5`. The paper, Quattrocolo and Maccaferri, "Novel
12	GABAergic Circuits Mediating Excitation/Inhibition of Cajal-Retzius Cells in
13	the Developing Hippocampus" in the Journal of Neuroscience, records
14	Cajal-Retzius cells and their GABAergic inputs in acute hippocampal slices of
15	CXCR4-EGFP and Sst-IRES-Cre;ChR2(H134R)-EYFP mice aged P10 to P19, with paired
16	recordings, optogenetic stimulation of O-LM cells, cell-attached recordings and
17	dynamic clamp; the data set holds one zip of three ATF files, one per O-LM cell
18	of Figure 7, each with 15 one-second current steps recorded at 20 kHz. The
19	claims were written from the extracted text of the version of record, which
20	printed the signs =, < and > as a replacement character, as the PDF could not
[... 648 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Dataset |" README.md | head -2; sed -n 1,80p tools/readme_row.py; F=/home/runner/.claude/projects/-home-runner-work-encore-encore/c9c61486-2fd1-4ec9-b234-eb5c6d272c56/tool-results/blxkcv4ht.txt; sed -n 1270,1297p $F
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
[... 86 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-ia-1-eyherabide-2008-01.yaml"
}
```

```
1	schema_version: 2
2	id: crcns-ia-1-eyherabide-2008-01
3	dataset:
4	  archive: crcns
5	  id: ia-1
6	  version: unversioned
7	  doi: 10.6080/K0BG2KWB
8	paper: doi:10.3389/neuro.10.003.2008
9	date: '2026-11-04'
10	entry: crcns-ia-1-eyherabide-2008
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
[... 773 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-ia-1-eyherabide-2008-01.yaml",
 "offset": 794,
 "limit": 200
}
```

```
794	    paper does not say so.
795	- kind: data_missing
796	  statement: Data1 holds no threshold, best frequency or f-I measurement for its cells, though the paper's
797	    model (Eq. 2) uses the measured threshold s_TH and the descriptor says the best frequency was determined
798	    from f-I curves.
799	- kind: identifier_missing
800	  statement: Data1 does not record the animal; the paper's 23 animals can only be matched to the 23 recording
801	    dates of the seven-protocol sessions by assuming one animal per date. Two experiments (03-01-15-aa,
802	    03-06-27-ae) are missing from singlecells.txt.
803	- kind: metadata_insufficient
804	  statement: 28 sessions use the stimuli gaussModality_co200 and lmd_co200 and 6 use cutoffs of 50 and
805	    1600 Hz; the descriptor does not describe these stimuli and the paper does not use them. 28 sessions
806	    sorted off-line have no header, so their target rate and pause are not recorded, and in 25 of them
807	    each trial block runs on into the pause (spikes up to 2.76 s), which the descriptor does not mention.
808	    The file Data1/firing_rates is not described; it gives each spike file's trial count and a rate with
809	    a +/- value of 57 to 189 Hz that is not the trial-to-trial SD of the rate.
810	- kind: metadata_error
811	  statement: The descriptor says the 1 s trials number 98 to 533; the files hold 69 to 503. The intensity
812	    in three trial headers differs from cell.dat by more than 1 dB (03-04-11-aa sig2, 03-04-16-ae sig2,
813	    03-04-23-ae sig1, up to 6.6 dB), and six sessions of 03-01-30-ad, 03-02-25-ac and 03-02-25-aj had
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d))
s=json.dumps(d)
import re
i=s.find('ia-1'); print(s[max(0,i-1500):i+1500])"; head -60 claims/crcns-ia-1/*.yaml; grep -c "^  - id:\|^- id:" claims/crcns-ia-1/*.yaml
```

```
<class 'dict'>
{"schema_version": 1, "generated": "2026-10-31T12:28:44+00:00", "source": "https://api.dandiarchive.org/api", "counts": {"public_dandisets": 668, "with_a_paper": 291, "with_a_published_version": 249, "papers": 303, "converted_by_catalystneuro": 51}, "targets": [{"dandiset": "000003", "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells", "published_version": "0.260218.2052", "asset_count": 101, "size_gb": 2559.25, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["House mouse"], "approaches": ["electrophysiological approach", "behavioral approach"], "papers": [{"doi": "10.1016/j.neuron.2016.12.011", "title": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells", "relation": "IsDescribedBy", "resource_type": "JournalArticle", "preprint": false}], "catalystneuro": ["contributor Baker, Cody of CatalystNeuro"]}, {"dandiset": "000004", "name": "A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task", "published_version": "0.220126.1852", "asset_count": 87, "size_gb": 6.2, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Human"], "approaches": ["electrophysiological approach"], "papers": [{"doi": "10.1038/s41597-020-0415-9", "title": "A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task", "relation": "IsDescribedBy", "resource_type": "JournalA
# Claims for Eyherabide, Rokem, Herz & Samengo (2008), "Burst firing is a neural code in an
# insect auditory system", Frontiers in Computational Neuroscience, on CRCNS data set ia-1
# (doi:10.6080/K0BG2KWB).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-04, protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record in PubMed Central (PMC2525941, open access), from Europe PMC
# full-tex
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
for t in d['targets']:
  s=json.dumps(t)
  if 'ia-1' in s or 'crcns' in s.lower() and 'ia' in str(t.get('dandiset','')): print(s)
print([k for k in d if k!='targets'])
print(set(t.get('archive') for t in d['targets']))"; sed -n 786,794p attempts/crcns-ia-1-eyherabide-2008-01.yaml; grep -n "crcns" docs/pilot-notes/crcns-hc-9-quattrocolo-2013-01.md | head
```

```
['schema_version', 'generated', 'source', 'counts']
{None}
findings:
- kind: selection_undocumented
  statement: The paper keeps 86 of 132 sessions by a trial-to-trial rate SD below 35 Hz and a rate near
    100 Hz. In Data1 the SD rule keeps 115 of the 116 sessions of the paper's seven protocols (and all
    116 with whole-trial rates), and nothing marks which sessions the paper kept. Leaving out also the
    9 sessions with fewer than 98 trials and the off-line sorted sessions keeps 89, with 47, 6, 7, 7,
    8, 7 and 7 per protocol against Table 1's 43, 6, 7, 7, 8, 7 and 8, and bursting sessions per protocol
    equal to Table 1's in six of seven, which suggests the paper used only on-line sorted sessions; the
    paper does not say so.
1:# crcns-hc-9, Quattrocolo et al. 2013
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-ia-1-eyherabide-2008-01.yaml",
 "offset": 993,
 "limit": 280
}
```

```
993	    outcome: reproduced
994	    reason: 'Cell 48: 43/71 sessions decrease monotonically, and the mean tau_n goes 5.75, 4.13, 2.88,
995	      -0.55 ms. tau_4 is negative (problem 2: the maximum falls after burst onset, which does not fit
996	      latency); a tau < 0 search reading was not run.'
997	    response: No change of outcome. With the maximum searched before the onset (now the main reading)
998	      the mean tau_n over selection (c) is 5.80, 4.23, 3.32 and 2.67 ms, none negative; only 20 of 53
999	      sessions decrease at every step, so the outcome rests on reading (b).
1000	  - claim: fig8e-sigma-minimum
1001	    agrees: true
1002	    outcome: not_reproduced
1003	    reason: 'Cell 50: the mean SD of the minimum''s position is 1.87 to 2.64 ms (tolerance up to 1.1).
1004	      Times cutoff it is 0.32 to 0.43, against 0.05 +/- 0.005. Problem 3: n = 4 rests on 2 to 20 segments
1005	      in many sessions, which inflates the spread of the minimum positions.'
1006	    response: No change of outcome. With at least 20 or 50 bursts of each n the SD is 2.14 and 1.74 ms
1007	      over selection (c) (1.46 over selection (a)), still outside.
1008	  - claim: sigma-n-below-sta-sigma
1009	    agrees: true
1010	    outcome: reproduced
1011	    reason: 'Cell 52, reading (a): 98.6% of sessions; ratio 1.60 (SD 0.28). Problem 4: the minimum over
1012	      800 time points of an SD estimated from few segments is biased low, which makes the 98.6% and the
[... 254 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/crcns-ia-1/author-report.md"
}
```

```
1	I've done steps 1 to 6 of the Author section for CRCNS ia-1 and run the handover. The entry passes `check` and runs clean in 248 s; nothing is committed. Files written: `entries/crcns-ia-1-eyherabide-2008/` (notebook, `ia1.py`, `entry.yaml`, `README.md`, lock files) and `attempts/crcns-ia-1-eyherabide-2008-01.yaml`. The verifier's package is in `executed/crcns-ia-1-eyherabide-2008/handover/`.
2	
3	**(1) Outcomes**
4	
5	| Claim | Outcome |
6	|---|---|
7	| data-sessions-and-trials | partially reproduced (assumed) |
8	| table1-sessions-per-protocol | not reproduced |
9	| firing-rate-uniform | reproduced |
10	| threshold-population | blocked: data_missing |
11	| table1-bursting-sessions | not reproduced |
12	| table1-isolated-spikes | partially reproduced (assumed) |
13	| table1-burst-length | not reproduced |
14	| fig5-burst-probability-vs-stimulus | reproduced (assumed) |
15	| fig3-correlation-shape | reproduced (assumed) |
16	| method-correlation-error | reproduced (assumed) |
17	| model-matches-classification | blocked: data_missing |
18	| fig6-bursts-less-correlated | reproduced (assumed) |
19	| fig7ab-information-per-burst-increases | partially reproduced (assumed) |
20	| fig7cd-occurrence-decreases | partially reproduced (assumed) |
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/crcns-ia-1; for f in answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md verifier-3-report.md author-revise-3-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (32.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/c9c61486-2fd1-4ec9-b234-eb5c6d272c56/tool-results/bjncqkokb.txt

Preview (first 2KB):
=== answer-report.md
There were no questions to answer, so I changed nothing.

- `questions/crcns-ia-1.yaml` doesn't exist. The `questions/` folder has a file for `crcns-ret-1` but none for `crcns-ia-1`.
- The author run (commit cff0dab156) says "No questions to a reader." in `transcripts/crcns-ia-1/author-report.md:56`. Its open method questions are addressed to the paper's authors, not a reader: they are in the `methods_unavailable` finding in `attempts/crcns-ia-1-eyherabide-2008-01.yaml:582`.

I left `claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml` untouched and didn't create a questions file. Since nothing was edited, I didn't run `python tools/claims_check.py`.
=== author-answers-report.md
There were no questions to act on, so I changed no claims, notebook cells, conclusions or attempt record.

**Questions:** `questions/crcns-ia-1.yaml` doesn't exist. My earlier author run asked a reader nothing: its open method questions are for the paper's authors and sit in the `methods_unavailable` finding of `attempts/crcns-ia-1-eyherabide-2008-01.yaml`. The later `answer` run found nothing to answer and left the claims file alone. The claims file was last changed by the claims-check run (9263cfc6ec), before my author run, so every claim is as I tested it.

**What each answer changed:** nothing, because there were no answers. Every outcome stays as recorded:

| Claim | Outcome (earlier = now) |
|---|---|
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/c9c61486-2fd1-4ec9-b234-eb5c6d272c56/tool-results/bjncqkokb.txt",
 "offset": 40
}
```

```
40	| fig10-burst-n-vs-height | not reproduced (assumed) |
41	| firing-rate-no-effect-on-limit | reproduced (assumed) |
42	| model-reproduces-coding-trends | blocked: data_missing |
43	
44	Totals are unchanged: 11 reproduced, 6 partially reproduced, 6 not reproduced, 3 blocked.
45	
46	**Entry commands:**
47	- **`lock`:** rewrote `requirements.lock.txt` with no change to its content, so git shows no diff.
48	- **`all`:** 0 errors. The notebook passed from a clean environment in 358 s; the earlier run took 248 s.
49	- **`handover`:** wrote the verifier's package to `executed/crcns-ia-1-eyherabide-2008/handover`.
50	
51	I didn't verify my own work, and nothing is committed or pushed. The untracked dotfiles and `scripts/` at the repository root were there before I started and I left them alone.
52	
53	**Blind rule:** to confirm there were no questions, I read the answer run's report and the end of its transcript (`transcripts/crcns-ia-1/answer*.md`). The protocol's blind rule says author runs should not read transcripts. Those files only say there were no questions to answer, and I changed nothing because of them.
54	=== verifier-1-report.md
55	**A. Outcomes** (26 claims, from the claims file)
56	
57	| Claim | Outcome | Reason |
58	|---|---|---|
59	| data-sessions-and-trials | partially_reproduced | Cell 9 matches on cells (37), recording dates as animals (23), max trials (503), mean trials (160.3) and mean rate SD (6.48 Hz). It misses on kept sessions (115, needs 86±8.6) and fewest trials (69, needs 98±9.8). The 132 recorded is matched only by "Gaussian AM stimuli, any cutoff" (122), not by the seven protocols (116). |
[... 205 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,120p claims/crcns-ia-1/*.yaml | grep -n -i "check\|open\|change" ; grep -n -i "checked\|claims check\|# Check" claims/crcns-ia-1/*.yaml | head
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/crcns-ia-1-eyherabide-2008-01.md",
 "content": "# crcns-ia-1, Eyherabide et al. 2008\n\nEleven claims reproduced (ten on an assumption), five partially (all five on\nan assumption), seven not reproduced (three on an assumption) and three\nblocked, all three for missing data. The first verification round agreed with\n25 of the 26 outcomes as they stood and the second with 25; one change of\noutcome was proposed after the second, and a third round agreed with it. CRCNS\ndoes not version data sets, so the version is recorded as unversioned and the\nzip is pinned by the MD5 in `checksums.md5`, which the helper checks against\nthe S3 ETag. The paper, Eyherabide, Rokem, Herz and Samengo, \"Burst firing is a\nneural code in an insect auditory system\" in Frontiers in Computational\nNeuroscience, records auditory receptor axons in the tympanal nerve of\nLocusta migratoria intracellularly, 37 cells from 23 animals stimulated with\nGaussian amplitude-modulated tones in seven protocols, identifies bursts from\nthe spike-train correlation function and measures what bursts of each length\nencode; the data set holds Data1 (2003), which its description names as\nanalysed in this paper, with the stimulus files, and Data2 (2004), unpublished.\nThe claims were written from the version of record in PubMed Central\n(PMC2525941) as Europe PMC XML, without a PDF, so values shown only in figures\ncould not be read; the paper has no supplement and links no code. The burst,\ncorrelation, information and burst-triggered average claims could be tested;\n`threshold-population` and the two model claims could not, as Data1 holds no\nthreshold s_TH. Reproduced are `firing-rate-uniform` (107.1 Hz, SD 14.5 Hz,\nANOVA p = 0.814), `fig5-burst-probability-vs-stimulus` (P(n = 1) lowest at\n100 Hz and 12 dB), `fig3-correlation-shape`, `method-correlation-error`\n(2.63% of the span of C_s), `fig6-bursts-less-correlated` (ratio 1.99),\n`fig7ef-jitter-independent-of-n` (86.9% of 61 sessions),\n`fig8-latency-decreases` (5.80, 4.23, 3.32 and 2.67 ms),\n`sigma-n-below-sta-sigma` (98.1%, ratio 1.596), `fig9-nbta-not-concatenated-1bta`,\n`fig9c-population-nbta` (3.13, 7.03 and 8.46 dB over 7 sessions from 7\ndistinct cells) and `firing-rate-no-effect-on-limit`. Partial are\n`data-sessions-and-trials` (37 cells, 23 dates, 503 most trials, mean 160.3\nand SD 6.48 Hz match; 115 kept sessions and 69 fewest trials do not),\n`fig7ab-information-per-burst-increases` (mean slope 2.22 bits, significant in\n63 of 64 sessions), `fig7cd-occurrence-decreases` (-2.82, significant in 63 of\n64), `direct-method-comparison` (R = 0.967, but 10.2% lost and the direct\nmethod higher in 74 of 89) and `fig8-nbta-differ` (the ANOVA holds in 53 of\n53, the time-domain count is 38 against 50 +/- 5). Not reproduced are the\nthree Table 1 count claims, `table1-isolated-spikes` (4 of 7 within\ntolerance), `table1-burst-length` (8 of 19), `fig7gh-information-rate` (slope\n-46.5 bits/s, 35.5% carried by bursts with n > 1), `fig8e-sigma-minimum`\n(2.37 ms against 0.4 +/- 0.7) and `fig10-burst-n-vs-height` (7 sessions,\n10.9%). Most outcomes rest on two assumptions: the first peak of C_s taken as\nits largest value below 5 ms, as the first local maximum falls on the\nrefractory plateau, and a main population, selection (c), of 89 sessions that\nleaves out sessions under 98 trials and those sorted off-line. The author's\nfirst run gave the same outcomes except that `table1-isolated-spikes` was\npartially reproduced, and it used the 115 sessions of selection (a). The\nauthor asked no questions of a reader, so the answer and author-answers runs\nchanged nothing. Round 1 disagreed on `table1-isolated-spikes` and found that\n115 sessions were kept against 86 with no exclusion tried, that the nBTA\nmaximum was searched up to +15 ms, giving a negative mean tau_4, that the\nminimum of two bursts per n was not stated, that sigma_n could be biased by\nsample size, that the plug-in information had no shuffle control, and that the\nfig10 counts were identical under both widths T; in reply the exclusions were\ntabulated and selection (c) adopted, which made `table1-bursting-sessions`\npartially reproduced, `table1-isolated-spikes` became not reproduced, the\nmaximum was searched before onset, results with 20 and 50 bursts, a\nsize-matched control (94.3%) and a shifted-onset baseline were added, and a\npeak reading after the plateau (61 of 89 bursting) was added. Round 2\ndisagreed on `table1-bursting-sessions`, as selection (c) was fitted partly to\nits own expected values, and found sentences the outputs did not support (all\nof `data-sessions-and-trials` within tolerance under selection (c), which comes\nfrom 29 cells on 18 dates, the rise of I_n(1) called estimator bias, and the\nspike-triggered average peaking before the spike in every session); in reply\nthe text was corrected, the 17 tau_n values on the 0 ms edge were printed, and\nthe change to not reproduced was proposed, which round 3 accepted. The\nauthor's run went from 18:18 to about 19:00 UTC; two development runs failed on\nbugs that were fixed (an array size and a plot-range count). The notebook ran\nin 248 s at first, 358 s after the author-answers run, about 9 minutes after\nrounds 1 and 2 and 410 s at the end. The untracked files in the repository root\nwere left alone.\n\nThe paper keeps 86 of 132 sessions by a trial-to-trial rate SD below 35 Hz and\na rate near 100 Hz, but in Data1 the SD rule keeps 115 of the 116 sessions of\nthe paper's seven protocols, and nothing marks which sessions the paper kept;\nleaving out also the 9 sessions with fewer than 98 trials and the off-line\nsorted sessions keeps 89, with 47, 6, 7, 7, 8, 7 and 7 per protocol against\nTable 1's 43, 6, 7, 7, 8, 7 and 8, which suggests the paper used only on-line\nsorted sessions, though the paper does not say so. Data1 holds no threshold,\nbest frequency or f-I measurement, though the paper's model uses the measured\nthreshold and the descriptor says the best frequency was determined from f-I\ncurves. Data1 does not record the animal, so the paper's 23 animals can be\nmatched to the 23 recording dates only by assuming one animal per date, and two\nexperiments (03-01-15-aa, 03-06-27-ae) are missing from singlecells.txt. 28\nsessions use the stimuli gaussModality_co200 and lmd_co200 and 6 use cutoffs of\n50 and 1600 Hz, which the descriptor does not describe and the paper does not\nuse. 28 sessions sorted off-line have no header, so their target rate and pause\nare not recorded, and in 25 of them each trial block runs on into the pause\n(spikes up to 2.76 s). The file Data1/firing_rates is not described, and its\n+/- value of 57 to 189 Hz is not the trial-to-trial SD of the rate. The\ndescriptor gives 98 to 533 trials, where the files hold 69 to 503; the\nintensity in three trial headers differs from cell.dat by more than 1 dB (up\nto 6.6 dB), and six sessions of 03-01-30-ad, 03-02-25-ac and 03-02-25-aj had\n450 ms pauses where the paper states 700 ms. The paper counts bursting\nsessions three ways, 63 with n > 1 in Table 1, 59 bursting cells for Figure 7B\nand 58 bursting sessions for Figure 8, without saying why. Questions are put\nto the paper's authors: which maximum is the first peak of C_s and what sigma\nand N are in its error bar; which rule besides the rate SD removed the sessions\nnot among the 86; how events were formed for the jitter; whether the mean\nstimulus was subtracted before summing 1BTAs in Eq. 15; what separates a peak\nof C_s for the shapes of Figure 3; whether the nBTA maximum giving tau_n was\nsearched before burst onset and how many bursts of each n a session needed;\nand whether I_n(1) was corrected for the bias of the plug-in estimate.\n\nThe author's points on the protocol: \"pin the most recent published version\"\ndoes not fit an unversioned archive, so `unversioned` was recorded and the MD5\nchecked against the ETag; it does not say whether the author may add a reading\nthe claims file does not list, so a third reading of sigma and N and the\nexclusion of tau = 0 were added and marked as assumptions; many criteria define\nonly \"reproduced\", so \"partially\" was given when the effect held and some\nexpected values matched; there is no rule for expected session counts when the\ndataset keeps more sessions than the paper did; it is unclear whether picking\none of the claims file's own readings counts as an assumption, so `assumed`\nwas set wherever the outcome depends on the burst reading; and the data-check\nexamples assume a task with trials and labels, so for stimulus-driven data the\nspike-triggered average against a 100 ms-shifted stimulus was used as the\ncontrast.\n"
}
```

```
File created successfully at: docs/pilot-notes/crcns-ia-1-eyherabide-2008-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -n -i "—\|rather\|actually\|genuinely" docs/pilot-notes/crcns-ia-1-eyherabide-2008-01.md; git status --short
```

```
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
?? docs/pilot-notes/crcns-ia-1-eyherabide-2008-01.md
?? scripts
```

**Agent**

I wrote the note in `docs/pilot-notes/crcns-ia-1-eyherabide-2008-01.md` and changed no other file. `targets/dandisets.json` lists only DANDI datasets and has no entry for CRCNS:ia-1, so it has no `catalystneuro` field to report and the second paragraph does not open with the CatalystNeuro sentence. The claims file and the reports I was allowed to use say nothing about the claims check, so the note leaves that check out. Nothing is committed.

# crcns-ia-1, Eyherabide et al. 2008

Eleven claims reproduced (ten on an assumption), five partially (all five on
an assumption), seven not reproduced (three on an assumption) and three
blocked, all three for missing data. The first verification round agreed with
25 of the 26 outcomes as they stood and the second with 25; one change of
outcome was proposed after the second, and a third round agreed with it. CRCNS
does not version data sets, so the version is recorded as unversioned and the
zip is pinned by the MD5 in `checksums.md5`, which the helper checks against
the S3 ETag. The paper, Eyherabide, Rokem, Herz and Samengo, "Burst firing is a
neural code in an insect auditory system" in Frontiers in Computational
Neuroscience, records auditory receptor axons in the tympanal nerve of
Locusta migratoria intracellularly, 37 cells from 23 animals stimulated with
Gaussian amplitude-modulated tones in seven protocols, identifies bursts from
the spike-train correlation function and measures what bursts of each length
encode; the data set holds Data1 (2003), which its description names as
analysed in this paper, with the stimulus files, and Data2 (2004), unpublished.
The claims were written from the version of record in PubMed Central
(PMC2525941) as Europe PMC XML, without a PDF, so values shown only in figures
could not be read; the paper has no supplement and links no code. The burst,
correlation, information and burst-triggered average claims could be tested;
`threshold-population` and the two model claims could not, as Data1 holds no
threshold s_TH. Reproduced are `firing-rate-uniform` (107.1 Hz, SD 14.5 Hz,
ANOVA p = 0.814), `fig5-burst-probability-vs-stimulus` (P(n = 1) lowest at
100 Hz and 12 dB), `fig3-correlation-shape`, `method-correlation-error`
(2.63% of the span of C_s), `fig6-bursts-less-correlated` (ratio 1.99),
`fig7ef-jitter-independent-of-n` (86.9% of 61 sessions),
`fig8-latency-decreases` (5.80, 4.23, 3.32 and 2.67 ms),
`sigma-n-below-sta-sigma` (98.1%, ratio 1.596), `fig9-nbta-not-concatenated-1bta`,
`fig9c-population-nbta` (3.13, 7.03 and 8.46 dB over 7 sessions from 7
distinct cells) and `firing-rate-no-effect-on-limit`. Partial are
`data-sessions-and-trials` (37 cells, 23 dates, 503 most trials, mean 160.3
and SD 6.48 Hz match; 115 kept sessions and 69 fewest trials do not),
`fig7ab-information-per-burst-increases` (mean slope 2.22 bits, significant in
63 of 64 sessions), `fig7cd-occurrence-decreases` (-2.82, significant in 63 of
64), `direct-method-comparison` (R = 0.967, but 10.2% lost and the direct
method higher in 74 of 89) and `fig8-nbta-differ` (the ANOVA holds in 53 of
53, the time-domain count is 38 against 50 +/- 5). Not reproduced are the
three Table 1 count claims, `table1-isolated-spikes` (4 of 7 within
tolerance), `table1-burst-length` (8 of 19), `fig7gh-information-rate` (slope
-46.5 bits/s, 35.5% carried by bursts with n > 1), `fig8e-sigma-minimum`
(2.37 ms against 0.4 +/- 0.7) and `fig10-burst-n-vs-height` (7 sessions,
10.9%). Most outcomes rest on two assumptions: the first peak of C_s taken as
its largest value below 5 ms, as the first local maximum falls on the
refractory plateau, and a main population, selection (c), of 89 sessions that
leaves out sessions under 98 trials and those sorted off-line. The author's
first run gave the same outcomes except that `table1-isolated-spikes` was
partially reproduced, and it used the 115 sessions of selection (a). The
author asked no questions of a reader, so the answer and author-answers runs
changed nothing. Round 1 disagreed on `table1-isolated-spikes` and found that
115 sessions were kept against 86 with no exclusion tried, that the nBTA
maximum was searched up to +15 ms, giving a negative mean tau_4, that the
minimum of two bursts per n was not stated, that sigma_n could be biased by
sample size, that the plug-in information had no shuffle control, and that the
fig10 counts were identical under both widths T; in reply the exclusions were
tabulated and selection (c) adopted, which made `table1-bursting-sessions`
partially reproduced, `table1-isolated-spikes` became not reproduced, the
maximum was searched before onset, results with 20 and 50 bursts, a
size-matched control (94.3%) and a shifted-onset baseline were added, and a
peak reading after the plateau (61 of 89 bursting) was added. Round 2
disagreed on `table1-bursting-sessions`, as selection (c) was fitted partly to
its own expected values, and found sentences the outputs did not support (all
of `data-sessions-and-trials` within tolerance under selection (c), which comes
from 29 cells on 18 dates, the rise of I_n(1) called estimator bias, and the
spike-triggered average peaking before the spike in every session); in reply
the text was corrected, the 17 tau_n values on the 0 ms edge were printed, and
the change to not reproduced was proposed, which round 3 accepted. The
author's run went from 18:18 to about 19:00 UTC; two development runs failed on
bugs that were fixed (an array size and a plot-range count). The notebook ran
in 248 s at first, 358 s after the author-answers run, about 9 minutes after
rounds 1 and 2 and 410 s at the end. The untracked files in the repository root
were left alone.

The paper keeps 86 of 132 sessions by a trial-to-trial rate SD below 35 Hz and
a rate near 100 Hz, but in Data1 the SD rule keeps 115 of the 116 sessions of
the paper's seven protocols, and nothing marks which sessions the paper kept;
leaving out also the 9 sessions with fewer than 98 trials and the off-line
sorted sessions keeps 89, with 47, 6, 7, 7, 8, 7 and 7 per protocol against
Table 1's 43, 6, 7, 7, 8, 7 and 8, which suggests the paper used only on-line
sorted sessions, though the paper does not say so. Data1 holds no threshold,
best frequency or f-I measurement, though the paper's model uses the measured
threshold and the descriptor says the best frequency was determined from f-I
curves. Data1 does not record the animal, so the paper's 23 animals can be
matched to the 23 recording dates only by assuming one animal per date, and two
experiments (03-01-15-aa, 03-06-27-ae) are missing from singlecells.txt. 28
sessions use the stimuli gaussModality_co200 and lmd_co200 and 6 use cutoffs of
50 and 1600 Hz, which the descriptor does not describe and the paper does not
use. 28 sessions sorted off-line have no header, so their target rate and pause
are not recorded, and in 25 of them each trial block runs on into the pause
(spikes up to 2.76 s). The file Data1/firing_rates is not described, and its
+/- value of 57 to 189 Hz is not the trial-to-trial SD of the rate. The
descriptor gives 98 to 533 trials, where the files hold 69 to 503; the
intensity in three trial headers differs from cell.dat by more than 1 dB (up
to 6.6 dB), and six sessions of 03-01-30-ad, 03-02-25-ac and 03-02-25-aj had
450 ms pauses where the paper states 700 ms. The paper counts bursting
sessions three ways, 63 with n > 1 in Table 1, 59 bursting cells for Figure 7B
and 58 bursting sessions for Figure 8, without saying why. Questions are put
to the paper's authors: which maximum is the first peak of C_s and what sigma
and N are in its error bar; which rule besides the rate SD removed the sessions
not among the 86; how events were formed for the jitter; whether the mean
stimulus was subtracted before summing 1BTAs in Eq. 15; what separates a peak
of C_s for the shapes of Figure 3; whether the nBTA maximum giving tau_n was
searched before burst onset and how many bursts of each n a session needed;
and whether I_n(1) was corrected for the bias of the plug-in estimate.

The author's points on the protocol: "pin the most recent published version"
does not fit an unversioned archive, so `unversioned` was recorded and the MD5
checked against the ETag; it does not say whether the author may add a reading
the claims file does not list, so a third reading of sigma and N and the
exclusion of tau = 0 were added and marked as assumptions; many criteria define
only "reproduced", so "partially" was given when the effect held and some
expected values matched; there is no rule for expected session counts when the
dataset keeps more sessions than the paper did; it is unclear whether picking
one of the claims file's own readings counts as an assumption, so `assumed`
was set wherever the outcome depends on the burst reading; and the data-check
examples assume a task with trials and labels, so for stimulus-driven data the
spike-triggered average against a 100 ms-shifted stimulus was used as the
contrast.

## End of run

16 turns, 2 minutes, $1.16 at API prices, result: success.
