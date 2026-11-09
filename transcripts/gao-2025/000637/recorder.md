# 000637 · recorder · run 41189504087

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/000637 transcripts/000637; python tools/readme_row.py 000637; cat attempts/000637-gao-2025-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '000637' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))"
```

```
<persisted-output>
Output too large (67.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/87734ed2-d186-405e-a415-09320f51cba2/tool-results/bsv900day.txt

Preview (first 2KB):
docs/pilot-notes/000633-kim-2023-01.md
docs/pilot-notes/000579-tseng-2022-01.md
docs/pilot-notes/000632-kim-2023-01.md
docs/pilot-notes/000631-kim-2023-01.md
docs/pilot-notes/000483-sit-2023-01.md
claims/000637:
10.1523-jneurosci.2218-24.2025.yaml

transcripts/000637:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=/home/runner/.claude/projects/-home-runner-work-encore-encore/87734ed2-d186-405e-a415-09320f51cba2/tool-results/bsv900day.txt; sed -n 30,400p $f | grep -v '^  notebook' | head -c 70000 | tail -c +1 | grep -nE "^- claim|outcome:|blocked_by" | sort | uniq -c | sort -rn | head; head -20 README.md | grep -n "|"; grep -n "000637\|catalyst" -i README.md | head
```

```
1 99:  outcome: blocked
      1 98:- claim: fig4-fsu-no-change
      1 90:  blocked_by: data_missing
      1 89:  outcome: blocked
      1 88:- claim: fig4-30hz-pom-rsu-delayed
      1 77:  blocked_by: data_missing
      1 76:  outcome: blocked
      1 75:- claim: fig4-30hz-s1-rsu-inhibition
      1 65:  blocked_by: data_missing
      1 64:  outcome: blocked
3:Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
31:please [open an issue](https://github.com/catalystneuro/encore/issues).
97:of lanes, each taking the next dandiset (those converted by CatalystNeuro
```

**Agent calls Bash**

```bash
cd  cat tools/readme_row.py | head -60; cat attempts/000637-gao-2025-01.yaml | grep -E "outcome:|blocked_by:" | sort | uniq -c; grep -n "000637" -A25 targets/dandisets.json | head -40
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
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; for f in 000633-kim-2023-01.md 000579-tseng-2022-01.md 000632-kim-2023-01.md 000631-kim-2023-01.md 000483-sit-2023-01.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (37.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/87734ed2-d186-405e-a415-09320f51cba2/tool-results/br1apmp8k.txt

Preview (first 2KB):
=== 000633-kim-2023-01.md
# 000633, Kim et al. 2023

Two claims reproduced, none partially, none not reproduced and five blocked on
the dataset, with one more reproduced and four more blocked that also need
outside data. The first verification round agreed with 11 of the 12 outcomes
and the second with all 12, so there was no third round. It pins version
0.231013.2226, the only published version; the paper cites none. The paper,
Kim, Semenov, Kiester, Keppler, Ibey, Bixler, Colunga Biancatelli and Pakhomov
in the International Journal of Molecular Sciences, electroporates monolayers
of bovine pulmonary artery endothelial (BPAE) cells with nanosecond pulses
through arrays of hollow needles and measures YO-PRO-1 (YP) uptake as the
direction of the electric field changes between pulses; the dandiset's title
names the experiment of Figure 4, a triangular array given trains of single
pulses on one base electrode or paired pulses on the two base electrodes in
alternation, at 833 kHz and 4 kV. The claims were written from the version of
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -E "^  notes:|^- claim" -A12 attempts/000637-gao-2025-01.yaml | grep -v "notebook:" | head -c 30000
```

```
- claim: unit-counts
  outcome: blocked
  blocked_by: data_missing
  notes: The dandiset's Units tables hold spike times only, with no waveforms, waveform features, electrodes
    or cell-type labels (data check), so units cannot be classified as RSUs or FSUs by the initial phase
    and afterhyperpolarization of their waveforms (Methods, Neuronal type classification). The waveforms
    of these units are not public anywhere else that the attempt could find; the paper's data statement
    names dandiset 000946, whose rats (BH494 to BH594, 20 rats) are not those of 000637 (BH401 to BH477). No recording
    holds POm units (each file has one 32-channel probe with electrode locations 'unknown', and the description
    names only S1). As a variant, S1 units with more than 2,000 spikes, all cell types together, number
    4,642 in the PRF series at 200 us (4,023 at 5 V), 1,088 at 3000 Hz and 862 at 30 Hz, against the paper's
    S1 RSU plus FSU sums of 1,297, 366 and 209, about 3.6 times as many; so the dataset's units are not,
    or not only, the units the paper counted. The S1 totals already rule out reproduced whatever classification
    were applied. Each S1 RSU plus FSU pair would sum to the dataset's total (4,642, 1,088, 862) against
    the paper's 1,297, 366 and 209, so at most one count of each S1 pair could match, at most 9 of the 12 counts
    in all, below the criterion's 10. The outcome stays blocked because the six POm counts cannot be computed.
--
- claim: fig4-s1-rsu-timelocked-3000
  outcome: blocked
  blocked_by: data_missing
[... 328 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '/^findings:/,$p' attempts/000637-gao-2025-01.yaml; grep -c "^- claim" attempts/000637-gao-2025-01.yaml
```

```
<persisted-output>
Output too large (38.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/87734ed2-d186-405e-a415-09320f51cba2/tool-results/booswgon3.txt

Preview (first 2KB):
findings:
- kind: data_missing
  statement: The Units tables hold spike times only, with no waveforms, waveform features, electrode assignments
    or quality metrics, so the units cannot be classified as regular- or fast-spiking as the paper does,
    and every finding of the paper is about one or the other.
- kind: data_missing
  statement: The dandiset holds one S1 probe per recording. It has no POm or auditory cortex units, no
    recording identified as sham or as targeting CG1, and of the paper's duty-cycle series only the four conditions
    whose pulse duration is 100, 200 or 400 us, the three pulse durations the description lists (3000 Hz
    at 30 and 60%, 30 Hz at 0.6%, 1500 Hz at 60%).
- kind: other
  statement: The recordings cannot be linked to those the paper analysed. The paper's data statement names
    dandiset 000946, whose rats (BH494 to BH594, 20 rats) are not those of 000637 (BH401 to BH477), and 000637
    has about 3.6 times as many S1 units over the paper's 2,000 spike threshold in the PRF series at 200
    us as the paper reports S1 RSUs and FSUs (4,642 against 1,297). Which of these recordings, if any,
    the paper used is not stated.
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '/^findings:/,$p' attempts/000637-gao-2025-01.yaml | head -c 9000
```

```
findings:
- kind: data_missing
  statement: The Units tables hold spike times only, with no waveforms, waveform features, electrode assignments
    or quality metrics, so the units cannot be classified as regular- or fast-spiking as the paper does,
    and every finding of the paper is about one or the other.
- kind: data_missing
  statement: The dandiset holds one S1 probe per recording. It has no POm or auditory cortex units, no
    recording identified as sham or as targeting CG1, and of the paper's duty-cycle series only the four conditions
    whose pulse duration is 100, 200 or 400 us, the three pulse durations the description lists (3000 Hz
    at 30 and 60%, 30 Hz at 0.6%, 1500 Hz at 60%).
- kind: other
  statement: The recordings cannot be linked to those the paper analysed. The paper's data statement names
    dandiset 000946, whose rats (BH494 to BH594, 20 rats) are not those of 000637 (BH401 to BH477), and 000637
    has about 3.6 times as many S1 units over the paper's 2,000 spike threshold in the PRF series at 200
    us as the paper reports S1 RSUs and FSUs (4,642 against 1,297). Which of these recordings, if any,
    the paper used is not stated.
- kind: metadata_error
  statement: The description says each recording has 500 trials; 73 of the 292 files have fewer (230 in
    45 files, 425 in 13, 375 in 11, and 252 to 400 in four).
- kind: metadata_error
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
cd  y=attempts/000637-gao-2025-01.yaml; grep -n "^- date\|^  by:\|agrees: false" $y; grep -c "agrees: true" $y; grep -n "^[a-z_]*:" $y; sed -n '/^- claim: unit-counts/,+0p' $y; grep -n "^- claim" $y | head -5
```

```
428:- date: '2026-10-31'
430:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
612:- date: '2026-10-31'
614:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
62
1:schema_version: 2
2:id: 000637-gao-2025-01
3:dataset:
8:paper: doi:10.1523/jneurosci.2218-24.2025
9:date: '2026-10-31'
10:entry: 000637-gao-2025
11:provenance:
22:outcomes:
397:findings:
427:verifications:
- claim: unit-counts
23:- claim: unit-counts
42:- claim: fig4-s1-rsu-timelocked-3000
56:- claim: fig4-pom-rsu-timelocked-3000
67:- claim: fig4-post-3000
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 612,640p attempts/000637-gao-2025-01.yaml; grep -n "response:" attempts/000637-gao-2025-01.yaml | sed -n '32,62p' | grep -v "No change of outcome.$"
```

```
- date: '2026-10-31'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 2. The full executed notebook of the revised run, with its conclusion cells and summary, the helper
    module, the claims file, the README and the attempt record; the verifier also read the paper. Text fixes in
    reply that touch no claim are in cells 12 (91 to 94%; the 23 of 25 rats comparison limited to 201 to 268 ms),
    14 (code comment), 25 and the summary (mean N2 60 to 86%), and the summary (missing full stop).
  results:
  - claim: unit-counts
    agrees: true
    outcome: blocked
    reason: 'I agree. The Units tables hold only spike_times, and cell 7 lists the full HDF5 tree of every file;
      every claim needs RSU/FSU labels. Reproduced is ruled out under the claims file: k-means puts every unit over
      2,000 spikes into one of two classes, so each S1 pair must add up to the dataset totals of 4,642, 1,088 and
      862 (cell 18); the highest pair sums the tolerances allow are 1,427, 403 and 230, so at most one count per
      pair can match, 9 of 12 at most, below the criterion''s 10. Blocked and not not_reproduced is correct
      because the six POm counts cannot be computed.'
    response: Outcome kept. The verifier found that no cell printed the subjects of 000946. The notebook now queries
      the archive for the top-level folders of 000946 (version 0.250829.1249) and 000637 and prints them (unit-counts
      section); 000946 holds 20 rats, BH494 to BH594, none shared with 000637. The range BH494 to BH535 given before
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000637; wc -c *-report.md; cat author-report.md
```

```
632 answer-report.md
 1401 author-answers-report.md
 4802 author-report.md
 2887 author-revise-1-report.md
 2463 author-revise-2-report.md
 2621 claims-check-report.md
 3884 claims-report.md
 7871 verifier-1-report.md
 5811 verifier-2-report.md
32372 total
# Report: author run on DANDI:000637 (Gao et al. 2025)

All 30 claims are blocked as `data_missing`: none of them can be tested on this dataset. The entry runs cleanly: `entry.py all` gives 0 errors and the notebook takes 332 s. The handover is built in `executed/000637-gao-2025/handover/`.

## 1. Outcomes

| Claims | Outcome | Main reason |
|---|---|---|
| unit-counts | blocked, data_missing | No waveforms, so no RSU/FSU split; no POm units |
| fig4 S1 claims (3000 Hz time-locked, post-sonication, 30 Hz inhibition) | blocked, data_missing | No cell types (and no POm for fig4-post-3000) |
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000637; for f in author-revise-1-report.md verifier-1-report.md verifier-2-report.md author-revise-2-report.md claims-report.md claims-check-report.md answer-report.md author-answers-report.md; do echo "=== $f"; cat $f; done; ls -la --time-style=+%T | sort -k6
```

```
=== author-revise-1-report.md
The verifier agreed with all 31 outcomes, so none changed: every claim is still `blocked` (`data_missing`). The entry re-ran with `python tools/entry.py all entries/000637-gao-2025` and passed with 0 errors, and `check` passes. The notebook's statements match the new outputs.

**What I added or corrected, by report point:**
- **B1:** the claim count is corrected from 30 to 31 in the notebook's opening cell, its summary and the README.
- **B2, B3:** a new result cell after the unit-counts cell, also added to that claim's notes, does two things:
  - It shows the S1 totals already rule out "reproduced": at most 9 of the 12 counts could match, and the criterion needs 10. The outcome stays blocked because the six POm counts can't be computed.
  - It weighs whether 000637 holds the paper's recordings at all: the paper's data statement names 000946, the paper used 28 rats (16 + 12) against 25 here, and there are 3.6 times as many S1 units (3.1 times at 5 V).
- **C (asked-for outputs):** the data check now lists the full HDF5 tree of all 292 files, the text fields under `general` and `general/subject`, the electrode columns, depths and group descriptions, and the Units table description. Nothing else is stored: no waveforms, and no field naming a target, sham or CG1. The one electrode group's location is "brain area", and every electrode has depth 0. I added this to the metadata finding.
- **B7:** the identifier's voltage field values are printed and asserted. Only 5, 7, 35 and 55 occur, so reading two digits as tenths of a volt only affects 3.5 and 5.5 V.
- **B5:** a new time-course plot over the whole trial shows the rate stays raised for about 1 s after onset. That is why the windows shifted by 1.2 s sit below their shifted pre-window. The text now calls the shift a contrast with the true onsets, not a null.
- **B4:** a check on simulated Poisson units with no response shows reading N1 is unbiased. Reading N2 gives 19% at 3 Hz, 56–58% at 10 
[... 264 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; wc -w 000633-kim-2023-01.md 000579-tseng-2022-01.md 000632-kim-2023-01.md 000631-kim-2023-01.md 000483-sit-2023-01.md; cat 000579-tseng-2022-01.md 000483-sit-2023-01.md; grep -l "converted by CatalystNeuro" *.md | head -3; head -3 001754-knierim-2000-02.md
```

```
1423 000633-kim-2023-01.md
 1390 000579-tseng-2022-01.md
 1225 000632-kim-2023-01.md
 1230 000631-kim-2023-01.md
 1237 000483-sit-2023-01.md
 6505 total
# 000579, Tseng et al. 2022

Ten claims reproduced, four partially, one not reproduced and 28 blocked. The
first verification round agreed with 38 of 43 outcomes and the second with all
43, and a third round, held on the one change of outcome proposed after the
second, agreed with it. It pins version 0.230728.1727, the only published
version; the paper cites none. The paper, Tseng, Chettih, Arlt, Barroso-Luque
and Harvey in Neuron, images six posterior cortical areas (V1, PM, AM, MM, RSC
and A) with two photons in eight mice running a virtual Y-maze whose cue-choice
rule switches within a session, describes the mice's strategies with LSTM
models, and compares the areas through a Poisson GLM of each neuron and through
population decoders. The claims were written from the accepted author
manuscript in PubMed Central (PMC9357051) and its supplement, without the
version of record or a main-text PDF, and from GLM_Tensorflow at commit
[... 213 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/000637/*.yaml; grep -n "^  - id:\|^- id:" claims/000637/*.yaml | wc -l
```

```
# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23):e2218242025, on dandiset 000637.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record as served by PubMed Central (PMC12139594), full text with
# Materials and Methods, Results, figure legends and Discussion (paper/10.1523-jneurosci.2218-24.2025.txt).
# The paper has no supplement. No PDF was supplied. The equation defining the directional spike time
# tiling coefficient (dSTTC) is lost in the text ("The definition for dSTTC is as follows:" is followed
# by the prose that defines its terms, without the formula); its form is treated as open below.
# The paper links no analysis code (no repository and no code availability statement in the text),
# so no code was read.
#
# Data the paper used (Materials and Methods). Male Wistar rats (Hsd WI), 250 to 350 g, 3 to 6 months,
# under 2% isoflurane. Group 1 (N = 16): two 32-channel NeuroNexus probes, one in S1 (AP -2, ML 2.5,
# 40 degrees, 1 to 1.3 mm deep, layers III to V) and one in POm (AP -4.5, ML 2.6, 20 degrees, 5.8 mm).
# Group 2 (N = 12, auditory confound): probes in S1 and auditory cortex (AC; AP -4.5, ML 6.5).
# tFUS from a 128-element random array (H276, 1.5 MHz) steered to S1; ultrasound duration (UD) 67 ms;
# intersonication interval 2.5 s with 10% jitter; 500 trials per parameter; condition order randomized.
# Conditions: PRF 30, 300, 1500, 3000 and 4500 Hz at constant 200 us pulse duration (which gives DC 0.6,
# 6, 30, 60 and 90%); DC 0.6, 6, 30, 60 and 90% at 3000 Hz and at 30 Hz PRF; PRFs at constant 60% DC;
[... 21 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000637-gao-2025-01.md",
 "content": "# 000637, Gao et al. 2025\n\nNo claims reproduced, none partially, none not reproduced and 31 blocked. The\nfirst verification round agreed with all 31 outcomes and the second with all\n31, so there was no third round. It pins version 0.250829.1249, the latest\npublished one; the paper cites no version of 000637, and all five published\nversions hold the same files with the same digests. The paper, Gao,\nRamachandran, Yu and He in the Journal of Neuroscience, steers transcranial\nfocused ultrasound (tFUS) from a 128-element array to S1 in anesthetized rats,\nrecords with 32-channel probes in S1 and POm (16 rats) or in S1 and auditory\ncortex (AC, 12 rats, the auditory confound group), splits sorted units into\nregular-spiking (RSU) and fast-spiking (FSU) units by k-means on their\nwaveforms, and compares their responses across PRF and duty-cycle series,\nagainst sham and CG1 control sessions, and through the correlation of S1 with\nPOm and AC (dSTTC and STTC). The claims were written from the version of\nrecord in PubMed Central (PMC12139594), with no supplement and no PDF; the\ndSTTC equation is lost from the text, and the paper links no code. No claim\ncould be tested: all 31 are blocked as `data_missing`, as every one needs the\nRSU and FSU split, and most also need POm or AC units, sham or CG1 sessions or\nduty cycles the dandiset does not hold. `unit-counts` stays blocked because\nits six POm counts cannot be computed, though the S1 totals alone rule out\nreproduced (at most 9 of the 12 counts could match, below the criterion's 10).\nThe author's first run counted 30 claims, corrected to 31 after round 1. The\nauthor asked a reader no questions, so the answer run and the following author\nrun changed nothing. Round 1 found the miscount, that the notebook did not ask\nwhether 000637 holds the paper's recordings or note that the S1 totals rule\nout reproduced, that reading N2 of the shared spiking method is biased\ndownward for low-rate units (16 to 23% at 3 Hz on simulated units with no\nresponse), that the onsets shifted by 1.2 s are not a null, and that the\npooled increase in the BASELINE recordings went undiscussed; it asked for the\nfull HDF5 tree and text fields of every file, which were added and show\nnothing beyond spike times. In reply the N2 bias was put to a reader. Round 2\nfound that no cell printed the subjects of 000946, and printing them corrected\nthe range given for them from BH494 to BH535 to BH494 to BH594; it also found\na wrong explanation of which duty-cycle conditions are present and several\nsmall ranges that did not match the printed output, all corrected. The\nauthor's run took about 26 minutes (07:59 to 08:25 UTC) and nothing failed;\nthe notebook took 332 s, most of it streaming the 292 files, and 211 s in the\nlast run.\n\nThe Units tables hold spike times only, with no waveforms, waveform features,\nelectrode assignments or quality metrics, so the units cannot be classified as\nregular- or fast-spiking as the paper does, and every finding of the paper is\nabout one or the other; the waveforms are not public anywhere else the attempt\ncould find. The dandiset holds one S1 probe per recording and no POm or AC\nunits, no recording identified as sham or as targeting CG1, and of the paper's\nduty-cycle series only the four conditions whose pulse duration is 100, 200 or\n400 us, the three pulse durations the description lists (3000 Hz at 30 and\n60%, 30 Hz at 0.6%, 1500 Hz at 60%). The recordings cannot be linked to those\nthe paper analysed: the paper's data statement names dandiset 000946, whose\nrats (BH494 to BH594, 20 rats) are not those of 000637 (BH401 to BH477), the\ndandiset has 25 rats against the paper's 16 + 12, and 000637 has about 3.6\ntimes as many S1 units over the paper's 2,000 spike threshold in the PRF\nseries at 200 us as the paper reports S1 RSUs and FSUs (4,642 against 1,297).\nThe description says each recording has 500 trials; 73 of the 292 files have\nfewer (230 in 45 files, 425 in 13, 375 in 11, and 252 to 400 in four). The\ndescription calls 100, 200 and 400 us the ultrasound durations and says the\npulse duration was kept at 67 ms, the reverse of the paper's terms and the\nfile identifiers, and a 600 us recording (BH446) and recordings at 3.5, 5.5 and\n7 V are present and not described. The stimulation condition is coded only in\neach file's identifier; the trials tables have start and stop times only, the\nelectrode locations are all 'unknown', the one electrode group's location is\n'brain area', every electrode has z = 0, and all 292 files share the session\ndescription \"Neural Spikes for S1 tFUS\". Three recordings named BASELINE\n(BH458, BH460, BH461; 500 trials each) are not described; pooled over their\n119 units, against the paper's 84 S1 units in sham, the rate rises at 134 to\n268 ms under the signed-rank test, which would weigh against\n`fig5-sham-no-response` if they were the paper's sham sessions. The trial\nstarts behave as tFUS onsets: 74% of units fire more in the 0 to 67 ms after\nonset than in the 67 ms before, against 43% with onsets shifted by 1.2 s, 23\nof 25 rats show the delayed response at 201 to 268 ms, and intertrial\nintervals are 2.25 to 2.75 s, as the paper states. No unit was deposited\ntwice. Pooling all S1 units across cell types, a variant that decides nothing,\nevery PRF raises the 0 to 67 ms rate and 300 to 4500 Hz raise the 201 to 268\nms rate.\n\nThe author's points on the protocol: `data_missing` is reserved for data not\npublic anywhere else, and the paper's own deposit, 000946, is public but holds\nother animals, so `data_missing` was used as the waveforms of 000637's units\nare public nowhere; there is no outcome or finding kind for a target dataset\nthat may not be the paper's data, and it was recorded as a finding of kind\n`other`; there is no guidance on tagging analyses that decide no claim, and\nthey were tagged `variant:...`; and the protocol requires one notebook section\nper tested claim and is silent when none is tested.\n"
}
```

```
File created successfully at: docs/pilot-notes/000637-gao-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -nP "—|–|\brather\b|\*\*" docs/pilot-notes/000637-gao-2025-01.md; wc -w docs/pilot-notes/000637-gao-2025-01.md; git status --short
```

```
1061 docs/pilot-notes/000637-gao-2025-01.md
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
?? docs/pilot-notes/000637-gao-2025-01.md
?? scripts
```

**Agent**

I wrote `docs/pilot-notes/000637-gao-2025-01.md` and changed no other file; nothing is committed. All 31 claims are blocked. The untracked dotfiles and `scripts` folder that `git status` lists were there before this run (the author's reports mention them), and I left them alone.

# 000637, Gao et al. 2025

No claims reproduced, none partially, none not reproduced and 31 blocked. The first verification round agreed with all 31 outcomes and the second with all 31, so there was no third round. It pins version 0.250829.1249, the latest published one; the paper cites no version of 000637, and all five published versions hold the same files with the same digests. The paper, Gao, Ramachandran, Yu and He in the Journal of Neuroscience, steers transcranial focused ultrasound (tFUS) from a 128-element array to S1 in anesthetized rats, records with 32-channel probes in S1 and POm (16 rats) or in S1 and auditory cortex (AC, 12 rats, the auditory confound group), splits sorted units into regular-spiking (RSU) and fast-spiking (FSU) units by k-means on their waveforms, and compares their responses across PRF and duty-cycle series, against sham and CG1 control sessions, and through the correlation of S1 with POm and AC (dSTTC and STTC). The claims were written from the version of record in PubMed Central (PMC12139594), with no supplement and no PDF; the dSTTC equation is lost from the text, and the paper links no code. No claim could be tested: all 31 are blocked as `data_missing`, as every one needs the RSU and FSU split, and most also need POm or AC units, sham or CG1 sessions or duty cycles the dandiset does not hold. `unit-counts` stays blocked because its six POm counts cannot be computed, though the S1 totals alone rule out reproduced (at most 9 of the 12 counts could match, below the criterion's 10). The author's first run counted 30 claims, corrected to 31 after round 1. The author asked a reader no questions, so the answer run and the following author run changed nothing. Round 1 found the miscount, that the notebook did not ask whether 000637 holds the paper's recordings or note that the S1 totals rule out reproduced, that reading N2 of the shared spiking method is biased downward for low-rate units (16 to 23% at 3 Hz on simulated units with no response), that the onsets shifted by 1.2 s are not a null, and that the pooled increase in the BASELINE recordings went undiscussed; it asked for the full HDF5 tree and text fields of every file, which were added and show nothing beyond spike times. In reply the N2 bias was put to a reader. Round 2 found that no cell printed the subjects of 000946, and printing them corrected the range given for them from BH494 to BH535 to BH494 to BH594; it also found a wrong explanation of which duty-cycle conditions are present and several small ranges that did not match the printed output, all corrected. The author's run took about 26 minutes (07:59 to 08:25 UTC) and nothing failed; the notebook took 332 s, most of it streaming the 292 files, and 211 s in the last run.

The Units tables hold spike times only, with no waveforms, waveform features, electrode assignments or quality metrics, so the units cannot be classified as regular- or fast-spiking as the paper does, and every finding of the paper is about one or the other; the waveforms are not public anywhere else the attempt could find. The dandiset holds one S1 probe per recording and no POm or AC units, no recording identified as sham or as targeting CG1, and of the paper's duty-cycle series only the four conditions whose pulse duration is 100, 200 or 400 us, the three pulse durations the description lists (3000 Hz at 30 and 60%, 30 Hz at 0.6%, 1500 Hz at 60%). The recordings cannot be linked to those the paper analysed: the paper's data statement names dandiset 000946, whose rats (BH494 to BH594, 20 rats) are not those of 000637 (BH401 to BH477), the dandiset has 25 rats against the paper's 16 + 12, and 000637 has about 3.6 times as many S1 units over the paper's 2,000 spike threshold in the PRF series at 200 us as the paper reports S1 RSUs and FSUs (4,642 against 1,297). The description says each recording has 500 trials; 73 of the 292 files have fewer (230 in 45 files, 425 in 13, 375 in 11, and 252 to 400 in four). The description calls 100, 200 and 400 us the ultrasound durations and says the pulse duration was kept at 67 ms, the reverse of the paper's terms and the file identifiers, and a 600 us recording (BH446) and recordings at 3.5, 5.5 and 7 V are present and not described. The stimulation condition is coded only in each file's identifier; the trials tables have start and stop times only, the electrode locations are all 'unknown', the one electrode group's location is 'brain area', every electrode has z = 0, and all 292 files share the session description "Neural Spikes for S1 tFUS". Three recordings named BASELINE (BH458, BH460, BH461; 500 trials each) are not described; pooled over their 119 units, against the paper's 84 S1 units in sham, the rate rises at 134 to 268 ms under the signed-rank test, which would weigh against `fig5-sham-no-response` if they were the paper's sham sessions. The trial starts behave as tFUS onsets: 74% of units fire more in the 0 to 67 ms after onset than in the 67 ms before, against 43% with onsets shifted by 1.2 s, 23 of 25 rats show the delayed response at 201 to 268 ms, and intertrial intervals are 2.25 to 2.75 s, as the paper states. No unit was deposited twice. Pooling all S1 units across cell types, a variant that decides nothing, every PRF raises the 0 to 67 ms rate and 300 to 4500 Hz raise the 201 to 268 ms rate.

The author's points on the protocol: `data_missing` is reserved for data not public anywhere else, and the paper's own deposit, 000946, is public but holds other animals, so `data_missing` was used as the waveforms of 000637's units are public nowhere; there is no outcome or finding kind for a target dataset that may not be the paper's data, and it was recorded as a finding of kind `other`; there is no guidance on tagging analyses that decide no claim, and they were tagged `variant:...`; and the protocol requires one notebook section per tested claim and is silent when none is tested.

## End of run

16 turns, 1 minutes, result: success.
