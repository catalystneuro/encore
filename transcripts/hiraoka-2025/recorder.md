# hiraoka-2025 · recorder · run 44993606711

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/hiraoka-2025/; python tools/readme_row.py hiraoka-2025; ls summaries | head
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
| [000044](https://dandiarchive.org/dandiset/000044) | [Hiraoka et al. 2025](https://doi.org/10.1063/5.0296506) | 7 | 0 | 2 | 0 | [`hiraoka-2025`](entries/hiraoka-2025) |
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 asari-2009-02; do echo "=== $f"; cat $f.md; done; head -20 ../../README.md | grep -i "|" | head -3; cat ../../summaries/asari-2009-02.md ../../summaries/amjad-2025-01.md
```

```
<persisted-output>
Output too large (35.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/364be354-8b99-4f88-83ea-feb0dfb7e485/tool-results/brygdi6kn.txt

Preview (first 2KB):
=== amjad-2025-01
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
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/hiraoka-2025-01.yaml claims/hiraoka-2025.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for e in (it if isinstance(it,list) else it.values()):
  if '000044' in json.dumps(e): print(json.dumps(e,indent=1))
"
```

```
Exit code 1
cat: attempts/hiraoka-2025-01.yaml: No such file or directory
cat: claims/hiraoka-2025.yaml: No such file or directory
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import json;d=json.load(open('targets/dandisets.json'))
                            ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'targets/dandisets.json'
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/364be354-8b99-4f88-83ea-feb0dfb7e485/tool-results/brygdi6kn.txt"
}
```

```
1	=== amjad-2025-01
2	# 002013, Amjad et al. 2025
3	
4	Seven claims reproduced, one partially and five blocked on the dandiset,
5	plus one claim linking the dandiset to the paper's Zenodo deposit,
6	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
7	agreed with every outcome. The paper describes microinvasive probes for
8	recording dopamine and electrical activity in monkeys; the beta burst,
9	reward and unit isolation claims reproduce, the dopamine reward effect
10	weakly (p = 0.023, and not in the stored trial-aligned `da`).
11	
12	The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
13	the same conversion as 002014), and many findings are the same: each event
14	is stored about five times, once per overlapping trial window; trial
15	conditions are not in the trials table; the FSCV table columns carry no
16	units and the raw FSCV current is labelled amperes with values in the
17	thousands; the bipolar LFP is stored in volts with a conversion factor that
18	makes it picovolts; and the raw ephys of one session and the spike times of
19	Monkey P are on different clocks from the rest of the file, by 9831.35 s and
20	6800.666 s, with nothing saying so. In addition, one session's trial-aligned
[... 481 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/hiraoka-2025-01.yaml; echo ====; cat claims/hiraoka-2025.yaml; echo ====; python -c "
import json;d=json.load(open('targets/dandisets.json'))
def walk(x):
  if isinstance(x,dict):
    if any('000044' == str(v) or '000044' in str(v)[:40] for v in x.values() if not isinstance(v,(dict,list))): print(json.dumps(x,indent=1)); return
    for v in x.values(): walk(v)
  elif isinstance(x,list):
    for v in x: walk(v)
walk(d)"
```

```
<persisted-output>
Output too large (67.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/364be354-8b99-4f88-83ea-feb0dfb7e485/tool-results/bk5lbgtqh.txt

Preview (first 2KB):
schema_version: 3
id: hiraoka-2025-01
datasets:
- archive: dandi
  id: '000044'
  version: 0.210812.1516
  doi: 10.48324/dandi.000044/0.210812.1516
  relation: reuses
paper: doi:10.1063/5.0296506
date: 2026-11-21
entry: hiraoka-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/364be354-8b99-4f88-83ea-feb0dfb7e485/tool-results/bk5lbgtqh.txt"
}
```

```
1	schema_version: 3
2	id: hiraoka-2025-01
3	datasets:
4	- archive: dandi
5	  id: '000044'
6	  version: 0.210812.1516
7	  doi: 10.48324/dandi.000044/0.210812.1516
8	  relation: reuses
9	paper: doi:10.1063/5.0296506
10	date: 2026-11-21
11	entry: hiraoka-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 793 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/364be354-8b99-4f88-83ea-feb0dfb7e485/tool-results/bk5lbgtqh.txt",
 "offset": 814
}
```

```
814	  - fig2-neuron-merging-heavy-tail
815	  criterion: The figure plots P(k) times the mean of k against k over the mean of k. The paper
816	    shows the collapse by eye, and it is supported by the fitted tails ("This is supported by
817	    fitting power-law tails"). How to measure it is open, and two readings are named. (a) The
818	    complementary cumulative distributions of k over its mean for the pairs of Figure 2 (delta'
819	    = 55, 100, 180, 330, 590 ms, each with delta = 3.3, 5.9 and 11 delta') differ by no more
820	    than a factor of 2 at every point where all are above 10^-3. (b) The gamma estimates of
821	    those pairs lie within +/- 0.5 of their median. Reproduced when either holds. The curves
822	    and the estimates are shown.
823	- id: fig2-exponents-above-two
824	  statement: In most cases both gamma and the burst-size exponent at the smaller timescale
825	    exceed 2, so the scaling relation reduces to beta at delta equal to the smaller of gamma
826	    and beta at delta', which agrees with the observations.
827	  source: Section III, paragraphs 8 and 9 (Eqs. 7 and 8); Figure 2
828	  quote: Since γδδ′, βδ′ > 2 in most cases as shown in Fig. 2, we have
829	  depends_on:
830	  - fig2-neuron-beta-stable
831	  - fig2-neuron-merging-heavy-tail
832	  criterion: For the representative unit and each pair of fig2-neuron-merging-heavy-tail, with
833	    the fit of O3. (1) In more than half of the pairs, both gamma and beta at delta' exceed 2.
[... 195 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Dandiset |\|^| Dataset\|^| Archive" README.md | head; sed -n 1,80p tools/readme_row.py
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
cd transcripts/hiraoka-2025; wc -w *-report.md; cat author-report.md
```

```
1099 author-report.md
  579 author-revise-1-report.md
  527 author-revise-2-report.md
  501 claims-check-report.md
  557 claims-report.md
 1709 verifier-1-report.md
 1047 verifier-2-report.md
 6019 total
## Report: hiraoka-2025 author run (Hiraoka and Jo 2025 on DANDI:000044)

Steps 1 to 5 are done and the handover package is built. `python tools/entry.py all entries/hiraoka-2025` reports 0 errors and all three notebooks pass from a clean environment. I did not commit anything.

### 1. Outcome per claim

| Claim | Outcome | Notes |
|---|---|---|
| fig2-neuron-representative-sequence | reproduced | "Unit 9" is row 9 counted from 0 (id 18): 228 356 spikes, τmin 1.050 ms, τmax 18 229.7 ms. It is the only matching unit. |
| fig2-iet-broad | reproduced | The IETs span 4.24 decades. |
| fig2-neuron-burst-size-heavy-tail | reproduced (assumed) | Power law supported at 40 of 40 timescales with the KS-xmin fits. With xmin = 1 it would only be partially reproduced. |
| fig2-neuron-beta-stable | partially reproduced | Median β is 2.354 and 27 of 34 estimates are in the band. β reaches about 2.9 at 55 ms, so the range rule fails. |
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/hiraoka-2025; for f in author-revise-1-report.md author-revise-2-report.md verifier-1-report.md verifier-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-revise-1-report.md
I worked through every point in the round-1 report. The entry ran clean with `tools/entry.py all`: all four notebooks pass, the longest taking 50 minutes. The conclusions match the executed outputs, and `entry.py check` reports no errors.

**What changed in the outcomes**
- **fig2-neuron-beta-stable:** now `not_reproduced` (was `partially_reproduced`), as the verifier gave. The criterion has no partial outcome and neither of its readings holds.
- **fig2-neuron-merging-collapse:** now `not_reproduced` (was `reproduced`), resting on an assumption (`assumed: true`). Without the cap no fit stays within the 0.5 band: the closest misses at 0.538, against 0.490 with the cap.
- **fig2-other-neurons-similar:** now `reproduced` (was `not_reproduced`), as the verifier gave. The criterion counts a pass under any one fit reading, and my round-1 choice of the discrete KS fit overrode that. Only the continuous fit from xmin = 1 passes (0.883 to 0.906), so the notes call it fragile.
- **fig2-neuron-merging-heavy-tail:** kept `reproduced`, with the verifier's disagreement recorded. Without the cap, the discrete KS fit still keeps the γ IQR below 0.5 (0.378 and 0.415).
- **The two blocked claims:** kept as they were, with the disagreements recorded.
  - Wikipedia stays `too_large`: the claim is "data elsewhere", for which the protocol does not use `data_missing`.
  - Earthquakes stay `other`: the catalog has no versioned release, and the protocol only allows pinned outside data.
- **The other seven:** unchanged. fig2-neuron-burst-size-heavy-tail no longer needs an assumption, because every KS reading gives it.

**What I added or corrected**
- **The cap on the exponent (problem 1):** the verifier was right. The locked powerlaw 2.0.0 caps the exponent at 3 by default, and the cap also moves the choice of xmin. The fits now leave the exponent unbounded, as in the method the paper cites (Clauset et al.). The capped fits run beside them as a variant, and the 
[... 139 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/hiraoka-2025-01.md",
 "content": "# hiraoka-2025, Hiraoka et al. 2025\n\nSeven claims reproduced on the dandiset, none partially, two not reproduced\nand none blocked; of the five claims on data elsewhere, counted apart, the\ntwo on the model's sequences are partially reproduced, the equivalence of\nthe model's two algorithms is not reproduced, and the Wikipedia and\nearthquake claims are blocked, as `too_large` and `other`. Two outcomes,\n`fig2-neuron-merging-collapse` and `fig4-model-heavy-tails`, rest on an\nassumption. The first verification round agreed with 11 of the 14 outcomes\nas they stood and the second with all 14; nothing was proposed after the\nsecond, so there was no third round. The record pins version 0.210812.1516,\nwhich the paper cites; the latest published version is 0.261106.0236, which\nrenumbers the units and renames the cell types. The paper, Hiraoka and Jo,\n\"Hierarchical organization of bursty trains in event sequences\"\n(doi:10.1063/5.0296506), builds burst trees from event sequences, with\nbursts at each timescale delta merging into bursts at larger ones, and\nreports for a hippocampal unit of Grosmark and Buzsaki, for the most\nfrequent Wikipedia editor and for a cluster of Southern California\nearthquakes that burst sizes and merging numbers are heavy-tailed across\ntimescales, that the burst-size exponent beta is stable (about 2.35 for\nthe neuron, up to about 3000 ms), that rescaled merging-number\ndistributions collapse, and that a scaling relation links the exponents;\na model generates such sequences by an incremental and an equivalent\ndecremental algorithm. The claims were written from a text whose abstract\nand references are the version of record and whose body is the arXiv\npreprint (2508.18281v1), with no PDF, so the figure panels were read only\nfrom the labels the text keeps; the paper links no code and gives no\nversion of the powerlaw package its fits cite. Reproduced are the\nrepresentative sequence (\"unit 9\" is row 9 counted from 0, id 18, with\n228 356 spikes, tau_min 1.050 ms and tau_max 18 229.7 ms, the only\nmatching unit), the span of 4.24 decades of the IETs, the heavy-tailed\nburst sizes (supported at 8 of 8 and 40 of 40 timescales under the KS\nfits, at none on shuffled IETs), the fall of beta above 3000 ms with gamma\n(rho -0.829, p = 0.042, on 6 points), the heavy-tailed merging numbers\n(interquartile range of gamma 0.378 and 0.415 under the discrete KS fit),\nthe exponents above two and the other neurons, which pass only under the\ncontinuous fit from xmin = 1 (502 of 554 and 502 of 562 pyramidal units),\nwith exponents far from the paper's 2.35 and called fragile. Not\nreproduced are the stability of beta (median 2.354, but 3.349 at 55 ms, a\nrange of 1.079 against 0.47; within the band only from about 130 to 3000\nms) and the collapse (largest deviation 0.538 with the exponent unbounded,\n0.490 capped at 3, against 0.5; the verifier reads it as undetermined\nbetween the two). The model's sequences were generated from the paper's\npseudocode: the heavy tails hold for two of the three timescale series\nunder the claim's seed, one of three tau_max values is within tolerance,\nand the two algorithms differ at every relevant timescale as Section IV\nsets them up, with a calibrated test across runs also finding them\ndifferent (p = 0.0079). The author's first run gave 7 reproduced, 3\npartially, 2 not reproduced and 2 blocked, with the discrete KS fit\nadopted where the readings disagreed. Round 1 found that the locked\npowerlaw 2.0.0 caps the exponent at 3 and lets the cap move the choice of\nxmin, that the paper's representative unit is labelled inhibitory while\nthe claim on other neurons uses the excitatory units only, that the\nadopted fit overrode the claims file's one-reading rule, and that the KS\ncriterion of the equivalence claim rejects two runs of one algorithm; in\nreply every fit was rerun with the exponent unbounded and the capped fits\nbeside it, all 690 units were fitted, a calibrated test was added as a\nvariant, and three outcomes changed: `fig2-neuron-beta-stable` to not\nreproduced and `fig2-other-neurons-similar` to reproduced, as the verifier\ngave, and `fig2-neuron-merging-collapse` to not reproduced; the verifier's\npartial for `fig2-neuron-merging-heavy-tail` and its data_missing for the\nWikipedia claim were recorded as disagreements, and the earthquake count\nit asked for was not made, the catalog having no pinned release. Round 2\nfound sentences the outputs did not support (0.08 for the pyramidal\nfraction, 41 grid points, an unprinted burst count at 6300 ms and a\n45-minute run time), asked why the model claims are partial when their\ncriteria define no partial outcome, and rated the unsorted spike trains\nminor, all taken up, with the equivalence criterion put to a reader in\n`questions/hiraoka-2025.yaml`. The author's run took about 2 h 06 min\n(21:20 to 23:26 UTC); its first `entry.py all` failed the check because\nthe simulated claims had no `inputs`, which were added. The notebooks ran\nin 2.3, 27.7 and 16.3 min at first, with peak memory under 1 GB, and the\nlongest of the four took 50 minutes at the end. Untracked placeholder\nfiles in the repository root, which the author did not create, were left\nuntouched.\n\nThe dataset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).\nThe paper's \"unit 9\" cannot be found by its number: the units table ids of\nthe cited version (id 18 for that row) differ from those of the latest\n(id 119, with a cluster_id of 19), neither holds the paper's number, and\nthe unit is found only as a row position whose spike count and IETs match\nFigure 2. That unit is labelled inhibitory in the cited version and\ninterneuron in the latest, though the paper describes its data as\npyramidal cells and does not say which units it analysed; under the KS\nfits the inhibitory units show the paper's pattern far more often than the\npyramidal ones (0.68 to 0.74 of 128 against 0.23 to 0.45 of 562; in\nAchilles-10252013 alone 0.76 to 0.88 of 17 against 0.08 to 0.34 of 120),\nand whether the claim's set should hold them is asked of a reader. In\nBuddy-06272013, Cicero-09012014 and Gatsby-08022013 the spike train of\nunit id 2 is two sorted runs, the first of exactly 65 536 spikes (131 072\nin Gatsby-08022013), which suggests a fault in the conversion; the trains\nare sorted before use, and leaving them out changes no fraction by more\nthan 0.003. In Gatsby-08022013, 263 976 spikes (4.7%) fall after the end\nof the last epoch (30 413.6 s), up to 32 002.4 s. The maze position series\nstores its sampling interval (0.0256 s) in the attribute rate, which NWB\ndefines in Hz. The epochs differ from the paper's 45 minutes of maze and\nfour hours of rest each, with maze epochs of 0.57 to 1.54 h and first rest\nperiods of 2.98 to 5.37 h. No spike train is deposited twice, and the\nspikes and the maze position share a clock (r = 0.618 at zero shift). In\nthe paper, Eq. 16 is not the memory function Eq. 9 gives for the zeta\ndistribution of Eq. 15 (q(1) is 0.354 against 0.255), so the two\nalgorithms as set up are not statistically equivalent. Questions are put\nto the paper's authors: which power-law fit was used, discrete or\ncontinuous and with which xmin; which grid of timescales and which units\nwere analysed; which distribution the decremental algorithm drew from; and\nwhich release of powerlaw was used and whether the exponent was bounded.\n\nThe author's points on the protocol: the claims file's one-reading rule\ncovers only claims on exponents, and for claims that count tests a reading\nwas adopted as an assumption; `inputs` are required for `data: elsewhere`\nclaims even when the data are simulated from the paper's own algorithms,\nand the paper's DOI was given as the source; no `blocked_by` fits public\noutside data with no versioned release, and `other` was used; for the\nWikipedia data the protocol forbids `data_missing` on a `data: elsewhere`\nclaim though the paper's data are public nowhere, and `too_large` was\nused without timing a fetch; it is unclear how `seed_sensitive` applies\nwhen different readings change outcome under different seeds; there is no\nprovision for a criterion whose reference shows it rejects identical\nalgorithms, and it was applied as written; and any edit, even to a\nmarkdown conclusion, forces a full rerun of the entry (46 min).\n"
}
```

```
File created successfully at: docs/pilot-notes/hiraoka-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/hiraoka-2025-01.md",
 "content": "In the hippocampal spike train the paper features, burst sizes and merging numbers are heavy-tailed across timescales, and the scaling relation between their exponents holds. The burst-size exponent stays near the reported 2.35 only above about 130 ms, and the rescaled merging-number distributions narrowly miss collapsing, on a fit setting the paper does not give. Other neurons share the pattern only under a fit poorly suited to integer counts. The Wikipedia and earthquake findings could not be tested, as the edit histories were never deposited and the catalog has no fixed version. In the model, heavy tails held for some timescale series only, and the two algorithms differ because the paper's memory function does not match its merging distribution.\n"
}
```

```
File created successfully at: summaries/hiraoka-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/hiraoka-2025-01.md; grep -c "—\|rather" docs/pilot-notes/hiraoka-2025-01.md summaries/hiraoka-2025-01.md; git status --short
```

```
119 summaries/hiraoka-2025-01.md
docs/pilot-notes/hiraoka-2025-01.md:0
summaries/hiraoka-2025-01.md:0
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
?? docs/pilot-notes/hiraoka-2025-01.md
?? scripts
?? summaries/hiraoka-2025-01.md
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "summaries/hiraoka-2025-01.md",
 "old_string": "stays near the reported 2.35",
 "new_string": "stays near the paper's 2.35"
}
```

```
The file summaries/hiraoka-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "summaries/hiraoka-2025-01.md",
 "old_string": "In the hippocampal spike train the paper features,",
 "new_string": "In the paper's example hippocampal neuron,"
}
```

```
The file summaries/hiraoka-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

I wrote both files and changed nothing else; nothing is committed. `python tools/readme_row.py hiraoka-2025` gives 7 reproduced, 0 partially, 2 not reproduced and 0 blocked. The summary is 116 words.

`docs/pilot-notes/hiraoka-2025-01.md`:

# hiraoka-2025, Hiraoka et al. 2025

Seven claims reproduced on the dandiset, none partially, two not reproduced and none blocked; of the five claims on data elsewhere, counted apart, the two on the model's sequences are partially reproduced, the equivalence of the model's two algorithms is not reproduced, and the Wikipedia and earthquake claims are blocked, as `too_large` and `other`. Two outcomes, `fig2-neuron-merging-collapse` and `fig4-model-heavy-tails`, rest on an assumption. The first verification round agreed with 11 of the 14 outcomes as they stood and the second with all 14; nothing was proposed after the second, so there was no third round. The record pins version 0.210812.1516, which the paper cites; the latest published version is 0.261106.0236, which renumbers the units and renames the cell types. The paper, Hiraoka and Jo, "Hierarchical organization of bursty trains in event sequences" (doi:10.1063/5.0296506), builds burst trees from event sequences, with bursts at each timescale delta merging into bursts at larger ones, and reports for a hippocampal unit of Grosmark and Buzsaki, for the most frequent Wikipedia editor and for a cluster of Southern California earthquakes that burst sizes and merging numbers are heavy-tailed across timescales, that the burst-size exponent beta is stable (about 2.35 for the neuron, up to about 3000 ms), that rescaled merging-number distributions collapse, and that a scaling relation links the exponents; a model generates such sequences by an incremental and an equivalent decremental algorithm. The claims were written from a text whose abstract and references are the version of record and whose body is the arXiv preprint (2508.18281v1), with no PDF, so the figure panels were read only from the labels the text keeps; the paper links no code and gives no version of the powerlaw package its fits cite. Reproduced are the representative sequence ("unit 9" is row 9 counted from 0, id 18, with 228 356 spikes, tau_min 1.050 ms and tau_max 18 229.7 ms, the only matching unit), the span of 4.24 decades of the IETs, the heavy-tailed burst sizes (supported at 8 of 8 and 40 of 40 timescales under the KS fits, at none on shuffled IETs), the fall of beta above 3000 ms with gamma (rho -0.829, p = 0.042, on 6 points), the heavy-tailed merging numbers (interquartile range of gamma 0.378 and 0.415 under the discrete KS fit), the exponents above two and the other neurons, which pass only under the continuous fit from xmin = 1 (502 of 554 and 502 of 562 pyramidal units), with exponents far from the paper's 2.35 and called fragile. Not reproduced are the stability of beta (median 2.354, but 3.349 at 55 ms, a range of 1.079 against 0.47; within the band only from about 130 to 3000 ms) and the collapse (largest deviation 0.538 with the exponent unbounded, 0.490 capped at 3, against 0.5; the verifier reads it as undetermined between the two). The model's sequences were generated from the paper's pseudocode: the heavy tails hold for two of the three timescale series under the claim's seed, one of three tau_max values is within tolerance, and the two algorithms differ at every relevant timescale as Section IV sets them up, with a calibrated test across runs also finding them different (p = 0.0079). The author's first run gave 7 reproduced, 3 partially, 2 not reproduced and 2 blocked, with the discrete KS fit adopted where the readings disagreed. Round 1 found that the locked powerlaw 2.0.0 caps the exponent at 3 and lets the cap move the choice of xmin, that the paper's representative unit is labelled inhibitory while the claim on other neurons uses the excitatory units only, that the adopted fit overrode the claims file's one-reading rule, and that the KS criterion of the equivalence claim rejects two runs of one algorithm; in reply every fit was rerun with the exponent unbounded and the capped fits beside it, all 690 units were fitted, a calibrated test was added as a variant, and three outcomes changed: `fig2-neuron-beta-stable` to not reproduced and `fig2-other-neurons-similar` to reproduced, as the verifier gave, and `fig2-neuron-merging-collapse` to not reproduced; the verifier's partial for `fig2-neuron-merging-heavy-tail` and its data_missing for the Wikipedia claim were recorded as disagreements, and the earthquake count it asked for was not made, the catalog having no pinned release. Round 2 found sentences the outputs did not support (0.08 for the pyramidal fraction, 41 grid points, an unprinted burst count at 6300 ms and a 45-minute run time), asked why the model claims are partial when their criteria define no partial outcome, and rated the unsorted spike trains minor, all taken up, with the equivalence criterion put to a reader in `questions/hiraoka-2025.yaml`. The author's run took about 2 h 06 min (21:20 to 23:26 UTC); its first `entry.py all` failed the check because the simulated claims had no `inputs`, which were added. The notebooks ran in 2.3, 27.7 and 16.3 min at first, with peak memory under 1 GB, and the longest of the four took 50 minutes at the end. Untracked placeholder files in the repository root, which the author did not create, were left untouched.

The dataset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb). The paper's "unit 9" cannot be found by its number: the units table ids of the cited version (id 18 for that row) differ from those of the latest (id 119, with a cluster_id of 19), neither holds the paper's number, and the unit is found only as a row position whose spike count and IETs match Figure 2. That unit is labelled inhibitory in the cited version and interneuron in the latest, though the paper describes its data as pyramidal cells and does not say which units it analysed; under the KS fits the inhibitory units show the paper's pattern far more often than the pyramidal ones (0.68 to 0.74 of 128 against 0.23 to 0.45 of 562; in Achilles-10252013 alone 0.76 to 0.88 of 17 against 0.08 to 0.34 of 120), and whether the claim's set should hold them is asked of a reader. In Buddy-06272013, Cicero-09012014 and Gatsby-08022013 the spike train of unit id 2 is two sorted runs, the first of exactly 65 536 spikes (131 072 in Gatsby-08022013), which suggests a fault in the conversion; the trains are sorted before use, and leaving them out changes no fraction by more than 0.003. In Gatsby-08022013, 263 976 spikes (4.7%) fall after the end of the last epoch (30 413.6 s), up to 32 002.4 s. The maze position series stores its sampling interval (0.0256 s) in the attribute rate, which NWB defines in Hz. The epochs differ from the paper's 45 minutes of maze and four hours of rest each, with maze epochs of 0.57 to 1.54 h and first rest periods of 2.98 to 5.37 h. No spike train is deposited twice, and the spikes and the maze position share a clock (r = 0.618 at zero shift). In the paper, Eq. 16 is not the memory function Eq. 9 gives for the zeta distribution of Eq. 15 (q(1) is 0.354 against 0.255), so the two algorithms as set up are not statistically equivalent. Questions are put to the paper's authors: which power-law fit was used, discrete or continuous and with which xmin; which grid of timescales and which units were analysed; which distribution the decremental algorithm drew from; and which release of powerlaw was used and whether the exponent was bounded.

The author's points on the protocol: the claims file's one-reading rule covers only claims on exponents, and for claims that count tests a reading was adopted as an assumption; `inputs` are required for `data: elsewhere` claims even when the data are simulated from the paper's own algorithms, and the paper's DOI was given as the source; no `blocked_by` fits public outside data with no versioned release, and `other` was used; for the Wikipedia data the protocol forbids `data_missing` on a `data: elsewhere` claim though the paper's data are public nowhere, and `too_large` was used without timing a fetch; it is unclear how `seed_sensitive` applies when different readings change outcome under different seeds; there is no provision for a criterion whose reference shows it rejects identical algorithms, and it was applied as written; and any edit, even to a markdown conclusion, forces a full rerun of the entry (46 min).

`summaries/hiraoka-2025-01.md`:

In the paper's example hippocampal neuron, burst sizes and merging numbers are heavy-tailed across timescales, and the scaling relation between their exponents holds. The burst-size exponent stays near the paper's 2.35 only above about 130 ms, and the rescaled merging-number distributions narrowly miss collapsing, on a fit setting the paper does not give. Other neurons share the pattern only under a fit poorly suited to integer counts. The Wikipedia and earthquake findings could not be tested, as the edit histories were never deposited and the catalog has no fixed version. In the model, heavy tails held for some timescale series only, and the two algorithms differ because the paper's memory function does not match its merging distribution.

## End of run

16 turns, 2 minutes, $1.03 at API prices, result: success.
