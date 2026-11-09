# 000037 · recorder · run 39870712621

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 000037; ls claims/000037 transcripts/000037; cat attempts/000037-gillon-2023-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if '000037' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (51.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6e911029-6a06-454c-abcc-6d1f3e4a78b4/tool-results/b9uya7hbi.txt

Preview (first 2KB):
docs/pilot-notes/000036-mayner-2022-01.md
docs/pilot-notes/000003-senzai-2017-01.md
docs/pilot-notes/000004-chandravadia-2020-01.md
docs/pilot-notes/000005-yu-2016-01.md
docs/pilot-notes/000005-yu-2016-02.md
| [000037](https://dandiarchive.org/dandiset/000037) | [Gillon et al. 2023](https://doi.org/10.1038/s41597-023-02214-y) | 22 (+2) | 1 | 1 | 7 (+1) | [`000037-gillon-2023`](entries/000037-gillon-2023) |
claims/000037:
10.1038-s41597-023-02214-y.yaml

transcripts/000037:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/000037-gillon-2023-01.yaml; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else d[0].keys())
E
```

```
<persisted-output>
Output too large (51.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6e911029-6a06-454c-abcc-6d1f3e4a78b4/tool-results/bcwd5iw4u.txt

Preview (first 2KB):
schema_version: 2
id: 000037-gillon-2023-01
dataset:
  archive: dandi
  id: "000037"
  version: 0.230426.0054
  doi: 10.48324/dandi.000037/0.230426.0054
paper: doi:10.1038/s41597-023-02214-y
date: 2026-10-22
entry: 000037-gillon-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6e911029-6a06-454c-abcc-6d1f3e4a78b4/tool-results/bcwd5iw4u.txt"
}
```

```
1	schema_version: 2
2	id: 000037-gillon-2023-01
3	dataset:
4	  archive: dandi
5	  id: "000037"
6	  version: 0.230426.0054
7	  doi: 10.48324/dandi.000037/0.230426.0054
8	paper: doi:10.1038/s41597-023-02214-y
9	date: 2026-10-22
10	entry: 000037-gillon-2023
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code (GitHub Actions)
17	    model: claude-opus-5-5
18	    protocol: pilot-10
19	  runner:
20	    platform: GitHub Actions
[... 906 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in docs/pilot-notes/000036-mayner-2022-01.md docs/pilot-notes/000003-senzai-2017-01.md docs/pilot-notes/000004-chandravadia-2020-01.md docs/pilot-notes/000005-yu-2016-01.md docs/pilot-notes/000005-yu-2016-02.md; do echo "== $f"; cat $f; done; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
for t in d['targets']:
  if '000037' in str(t.get('id','')) or '000037' in json.dumps(t)[:100]: print(json.dumps(t,indent=1))
E
grep -n "+" tools/readme_row.py | head -30
```

```
<persisted-output>
Output too large (31.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6e911029-6a06-454c-abcc-6d1f3e4a78b4/tool-results/bmrazqdlt.txt

Preview (first 2KB):
== docs/pilot-notes/000036-mayner-2022-01.md
# 000036, Mayner et al. 2022

Fourteen claims reproduced, one partially, one not reproduced and five
blocked on the dandiset, with one more reproduced and four more blocked on the
dandiset together with the paper's Zenodo deposit. It pins version
0.230515.1917. The claims were written from the full text of the version of
record as served by Europe PMC, without the Extended Data images; the claims
check found 0 problems in 26 claims and made the design-sessions criterion
count a dataset of the 44 analysed sessions as reproduced, and the author added
the link claim `session-link`, so the file has 27 claims. The author asked no
questions, so the answer steps changed nothing. Round 1 gave its own outcome
for each claim from the notebooks with their conclusions and summaries removed
and agreed with 26 of 27; it gave `design-sessions` as reproduced, as the
paper's 45 sessions are all present with its counts, and the author changed it
from partially reproduced. Round 1 also gave `other` as the reason for the
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6e911029-6a06-454c-abcc-6d1f3e4a78b4/tool-results/bmrazqdlt.txt"
}
```

```
1	== docs/pilot-notes/000036-mayner-2022-01.md
2	# 000036, Mayner et al. 2022
3	
4	Fourteen claims reproduced, one partially, one not reproduced and five
5	blocked on the dandiset, with one more reproduced and four more blocked on the
6	dandiset together with the paper's Zenodo deposit. It pins version
7	0.230515.1917. The claims were written from the full text of the version of
8	record as served by Europe PMC, without the Extended Data images; the claims
9	check found 0 problems in 26 claims and made the design-sessions criterion
10	count a dataset of the 44 analysed sessions as reproduced, and the author added
11	the link claim `session-link`, so the file has 27 claims. The author asked no
12	questions, so the answer steps changed nothing. Round 1 gave its own outcome
13	for each claim from the notebooks with their conclusions and summaries removed
14	and agreed with 26 of 27; it gave `design-sessions` as reproduced, as the
15	paper's 45 sessions are all present with its counts, and the author changed it
16	from partially reproduced. Round 1 also gave `other` as the reason for the
17	five L0 event claims, where the author kept `not_runnable`, which round 2
18	accepted. Round 2 agreed with all 27, so there was no third round. The paper,
19	"Measuring Stimulus-Evoked Neurophysiological Differentiation in Distinct
20	Populations of Neurons in Mouse Visual Cortex" in eNeuro, images excitatory
[... 472 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,70p tools/readme_row.py; head -60 claims/000037/*.yaml; wc -l transcripts/000037/*report.md
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
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000037; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done; cd ../..; grep -n "data: \|^  - id:\|^- id:" claims/000037/*.yaml | grep -B1 "data:"
```

```
<persisted-output>
Output too large (33KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6e911029-6a06-454c-abcc-6d1f3e4a78b4/tool-results/buri1qckl.txt

Preview (first 2KB):
=== author-report.md
I've finished steps 1 to 5 of the Author section and ran the handover (step 6). The entry is `entries/000037-gillon-2023/`, with the record in `attempts/000037-gillon-2023-01.yaml` and three questions in `questions/000037.yaml`. `entry.py check` and `all` both pass, and the notebook ran in 431 s. Nothing is committed.

**(1) Outcomes (35 claims)**

| Claim | Outcome |
|---|---|
| table1-subjects, cohorts-by-plane, sex-split, sessions-total | reproduced |
| table2-sessions | not reproduced: 43 of 50 sessions agree in every recorded field; 45 were needed for partial |
| qc-failures | blocked, metadata_insufficient (the files hold no QC status) |
| session-schedule, acquisition-rates, roi-noise-rejection, roi-count-ranges | reproduced |
| imaging-depths | not reproduced: 433414 is at 60 µm, and the criterion admits only 50 or 75 |
| tracked-roi-totals, tracked-sessions-overlap | reproduced |
| fig8a and fig8b final matches and conflicts (4 claims) | reproduced |
| fig8-somata-less-order-dependent | blocked, data_missing |
| gabor-sequence-structure | partially reproduced: 13 of 340,000 images in 4 sessions fall outside 300 ms ±10% |
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6e911029-6a06-454c-abcc-6d1f3e4a78b4/tool-results/buri1qckl.txt"
}
```

```
1	=== author-report.md
2	I've finished steps 1 to 5 of the Author section and ran the handover (step 6). The entry is `entries/000037-gillon-2023/`, with the record in `attempts/000037-gillon-2023-01.yaml` and three questions in `questions/000037.yaml`. `entry.py check` and `all` both pass, and the notebook ran in 431 s. Nothing is committed.
3	
4	**(1) Outcomes (35 claims)**
5	
6	| Claim | Outcome |
7	|---|---|
8	| table1-subjects, cohorts-by-plane, sex-split, sessions-total | reproduced |
9	| table2-sessions | not reproduced: 43 of 50 sessions agree in every recorded field; 45 were needed for partial |
10	| qc-failures | blocked, metadata_insufficient (the files hold no QC status) |
11	| session-schedule, acquisition-rates, roi-noise-rejection, roi-count-ranges | reproduced |
12	| imaging-depths | not reproduced: 433414 is at 60 µm, and the criterion admits only 50 or 75 |
13	| tracked-roi-totals, tracked-sessions-overlap | reproduced |
14	| fig8a and fig8b final matches and conflicts (4 claims) | reproduced |
15	| fig8-somata-less-order-dependent | blocked, data_missing |
16	| gabor-sequence-structure | partially reproduced: 13 of 340,000 images in 4 sessions fall outside 300 ms ±10% |
17	| visual-flow-structure, session-stimulus-durations, inconsistent-fractions, inconsistent-blocks | reproduced |
18	| fig5-example-responses | blocked, methods_underspecified (question asked) |
19	| fig5-consistent-vs-inconsistent | blocked through its dependency on the claim above (its own test gives partial) |
20	| fig6-behaviour-all-mice, fig7a-snr-above-1, fig7a-source-link, fig9-onset-offset-transients | reproduced |
[... 254 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000037-gillon-2023-01.md",
 "content": "# 000037, Gillon et al. 2023\n\nTwenty-two claims reproduced, one partially, one not reproduced and seven\nblocked on the dandiset, with two more reproduced and one more blocked on the\ndandiset together with the paper's code repository. It pins version\n0.230426.0054, which the paper's reference 13 cites by DOI in the Crossref\nrecord; version 0.240209.1623 has the same blobs plus a CHANGES file. The\npaper, a data descriptor in Scientific Data that reports no statistical\nanalyses, describes two-photon calcium imaging of somata and distal apical\ndendrites of L2/3 and L5 neurons in primary visual cortex of 13 mice over 50\nsessions, in which Gabor sequences and visual flow are shown with occasional\ninconsistent stimuli. The subjects and sessions, imaging depths and rates, ROI\ncounts and tracking, the Fig. 8 matching examples, the stimulus structure and\ntiming, behaviour, SNR, the grey screen transients of Fig. 9, file sizes and\nthe link to the Fig. 7a source data were tested. `qc-failures` is blocked as\n`metadata_insufficient`, as no file holds a QC result,\n`fig8-somata-less-order-dependent` as `data_missing`, as per-ordering matching\ncounts are published for 2 of 13 mice, and `fig5-example-responses`,\n`fig7a-snr-stable`, `fig7b-signal-stable` and `fig7c-correlations-similar` as\n`methods_underspecified`, because the criteria's readings disagree.\n`table2-sessions` is not reproduced, as 43 of 50 sessions agree in every\nrecorded field against the 45 needed for partial, and\n`gabor-sequence-structure` is partially reproduced, as 13 of 340000 images in\n4 sessions fall outside 300 ms +/- 10%. The author put three questions to a\nreader; the answer widened the L2/3 dendritic depth in `imaging-depths` to the\nMethods' 50 to 75 um, which moved it from not reproduced to reproduced, and\nadded readings to `fig5-example-responses` and\n`fig7c-high-correlation-fraction` without changing their outcomes. Rounds 1\nand 2 each agreed with 33 of 35 outcomes: both would give\n`fig5-consistent-vs-inconsistent` as partially reproduced and\n`fig7c-high-correlation-fraction` as not reproduced (0.0178% pooled against\n0.005 to 0.015%), which the author kept blocked because they depend on blocked\nclaims (protocol author step 1.5), recording what each claim's own test gives.\nRound 2 found statements the outputs did not support, among them start times\ncalled evening Pacific times, Supplementary Table 1's notes cited but not\nprinted and a run time of about seven minutes against 664 s printed; these\nwere corrected, no change was proposed, and there was no third round. The\nfirst loader took 16 minutes on the chunked dendritic files, and streaming\neach whole file into memory with parallel HTTP range requests brought the\nnotebook to 417 to 431 s, 695 s after the answers and about 11 minutes (670\nand 665 s) in the last runs.\n\nThe session start times are stated with a Pacific offset (-07:00 or -08:00),\nbut their clock values are those Supplementary Table 1 gives as UTC, for all\n50 sessions, so four sessions (412933 session 765427689, and 418779's three\nsessions) start a day after Table 2's imaging date and the date of birth\nimplied by 418779's age is a day after Table 1's; read as UTC all 50 dates\nagree, and the files hold no other wall-clock time to settle it. The three\nsessions of mouse 433414 are recorded at a depth of 60 um where Table 2 and\nSupplementary Table 1 give 75 um. The files hold no QC result, local session\nnumber or stimulus seed, so the paper's 33 analysed sessions (local sessions 1\nto 3 that passed QC, from 11 mice) can only be selected with Supplementary\nTable 1, an outside table to which the dandiset's description points; none of\nthe 23 small datasets and attributes under general and at the top level of\neach file mentions QC. The imaging plane is not recorded and follows from the\ndepth, the field of view in um is not recorded, and the visual flow square\nsize and position are given in pixels of the unwarped stimulus with no screen\ngeometry to convert them to the degrees the paper states, though their ratio,\n6.09 per second, is within 3% of the paper's 50/8 = 6.25. The per-ordering ROI\nmatching counts behind Fig. 8 are published for two mice only, and the\npaper's modified matching code is not linked. Other findings: the dF/F of the\n28 dendritic sessions is stored gzip-compressed in small chunks (991 to 1994\nframes by 5 to 26 ROIs) with the chunk index spread through the file, which\nmakes streaming it through remfile and h5py slow, where the 22 somatic files\nstore it contiguous; and in two sessions the response to grey screen\ntransitions does not exceed the 99th percentile of the responses at shifted\ntimes (777496949, 15 ROIs, above 94.6% of them; 838633305, which failed QC and\nwhose experimental notes say the laser was set to 800 nm, while the file\nstates 910 nm), so their alignment to the trial table could not be shown,\nthough it is shown in the other 48. Where the files do hold the paper's\nvalues they agree closely: every ROI's SNR is within 1% of the Fig. 7a source\ndata (largest relative difference 3.4e-05), and no recording is deposited\ntwice.\n\nThe author's points on the protocol: the claims file gives no version to pin,\nso the DOI was taken from the Crossref reference; the rule that blocks a claim\ndepending on a blocked claim also blocks dependents whose own test is fully\nspecified when the parent is blocked only on its decision rule; step 1.6\ncovers missing method details, not an ambiguous decision rule inside a\ncriterion; an author has no channel for a criterion stricter than the claim's\nown statement; the gabor-sequence-structure criterion has no partial rule; the\nseveral-readings rule covers the paper's text, not ambiguous metadata in the\ndataset such as the time zone, which decides table2-sessions; streaming\nthrough remfile and h5py was too slow for the chunked files; the `data`\ncategories have no slot for the paper's own supplementary table used to\nselect sessions; the notebook may not read local paths, so it cannot check\nSupplementary Table 1 against Tables 1 and 2; and the suggested clock checks\ndo not fit this design, so the response at grey screen transitions was\ncompared against 500 time-shifted copies.\n"
}
```

```
File created successfully at: docs/pilot-notes/000037-gillon-2023-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/000037-gillon-2023-01.md",
 "old_string": "though it is shown in the other 48. Where the files do hold the paper's\nvalues they agree closely: every ROI's SNR is within 1% of the Fig. 7a source\ndata (largest relative difference 3.4e-05), and no recording is deposited\ntwice.",
 "new_string": "though it is shown in the other 48. Every ROI's SNR is within 1% of the Fig.\n7a source data (largest relative difference 3.4e-05), and no recording is\ndeposited twice."
}
```

```
The file docs/pilot-notes/000037-gillon-2023-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -nE "—|rather|\*\*" docs/pilot-notes/000037-gillon-2023-01.md; git status --short
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
?? docs/pilot-notes/000037-gillon-2023-01.md
?? scripts
```

**Agent**

I wrote the notes in `docs/pilot-notes/000037-gillon-2023-01.md` and changed no other file. Nothing is committed. The repository root also has untracked dotfiles and a `scripts/` directory; I didn't create them and left them alone. The `catalystneuro` field for 000037 is empty, so the second paragraph doesn't open with the conversion sentence.

# 000037, Gillon et al. 2023

Twenty-two claims reproduced, one partially, one not reproduced and seven blocked on the dandiset, with two more reproduced and one more blocked on the dandiset together with the paper's code repository. It pins version 0.230426.0054, which the paper's reference 13 cites by DOI in the Crossref record; version 0.240209.1623 has the same blobs plus a CHANGES file. The paper, a data descriptor in Scientific Data that reports no statistical analyses, describes two-photon calcium imaging of somata and distal apical dendrites of L2/3 and L5 neurons in primary visual cortex of 13 mice over 50 sessions, in which Gabor sequences and visual flow are shown with occasional inconsistent stimuli. The subjects and sessions, imaging depths and rates, ROI counts and tracking, the Fig. 8 matching examples, the stimulus structure and timing, behaviour, SNR, the grey screen transients of Fig. 9, file sizes and the link to the Fig. 7a source data were tested. `qc-failures` is blocked as `metadata_insufficient`, as no file holds a QC result, `fig8-somata-less-order-dependent` as `data_missing`, as per-ordering matching counts are published for 2 of 13 mice, and `fig5-example-responses`, `fig7a-snr-stable`, `fig7b-signal-stable` and `fig7c-correlations-similar` as `methods_underspecified`, because the criteria's readings disagree. `table2-sessions` is not reproduced, as 43 of 50 sessions agree in every recorded field against the 45 needed for partial, and `gabor-sequence-structure` is partially reproduced, as 13 of 340000 images in 4 sessions fall outside 300 ms +/- 10%. The author put three questions to a reader; the answer widened the L2/3 dendritic depth in `imaging-depths` to the Methods' 50 to 75 um, which moved it from not reproduced to reproduced, and added readings to `fig5-example-responses` and `fig7c-high-correlation-fraction` without changing their outcomes. Rounds 1 and 2 each agreed with 33 of 35 outcomes: both would give `fig5-consistent-vs-inconsistent` as partially reproduced and `fig7c-high-correlation-fraction` as not reproduced (0.0178% pooled against 0.005 to 0.015%), which the author kept blocked because they depend on blocked claims (protocol author step 1.5), recording what each claim's own test gives. Round 2 found statements the outputs did not support, among them start times called evening Pacific times, Supplementary Table 1's notes cited but not printed and a run time of about seven minutes against 664 s printed; these were corrected, no change was proposed, and there was no third round. The first loader took 16 minutes on the chunked dendritic files, and streaming each whole file into memory with parallel HTTP range requests brought the notebook to 417 to 431 s, 695 s after the answers and about 11 minutes (670 and 665 s) in the last runs.

The session start times are stated with a Pacific offset (-07:00 or -08:00), but their clock values are those Supplementary Table 1 gives as UTC, for all 50 sessions, so four sessions (412933 session 765427689, and 418779's three sessions) start a day after Table 2's imaging date and the date of birth implied by 418779's age is a day after Table 1's; read as UTC all 50 dates agree, and the files hold no other wall-clock time to settle it. The three sessions of mouse 433414 are recorded at a depth of 60 um where Table 2 and Supplementary Table 1 give 75 um. The files hold no QC result, local session number or stimulus seed, so the paper's 33 analysed sessions (local sessions 1 to 3 that passed QC, from 11 mice) can only be selected with Supplementary Table 1, an outside table to which the dandiset's description points; none of the 23 small datasets and attributes under general and at the top level of each file mentions QC. The imaging plane is not recorded and follows from the depth, the field of view in um is not recorded, and the visual flow square size and position are given in pixels of the unwarped stimulus with no screen geometry to convert them to the degrees the paper states, though their ratio, 6.09 per second, is within 3% of the paper's 50/8 = 6.25. The per-ordering ROI matching counts behind Fig. 8 are published for two mice only, and the paper's modified matching code is not linked. Other findings: the dF/F of the 28 dendritic sessions is stored gzip-compressed in small chunks (991 to 1994 frames by 5 to 26 ROIs) with the chunk index spread through the file, which makes streaming it through remfile and h5py slow, where the 22 somatic files store it contiguous; and in two sessions the response to grey screen transitions does not exceed the 99th percentile of the responses at shifted times (777496949, 15 ROIs, above 94.6% of them; 838633305, which failed QC and whose experimental notes say the laser was set to 800 nm, while the file states 910 nm), so their alignment to the trial table could not be shown, though it is shown in the other 48. Every ROI's SNR is within 1% of the Fig. 7a source data (largest relative difference 3.4e-05), and no recording is deposited twice.

The author's points on the protocol: the claims file gives no version to pin, so the DOI was taken from the Crossref reference; the rule that blocks a claim depending on a blocked claim also blocks dependents whose own test is fully specified when the parent is blocked only on its decision rule; step 1.6 covers missing method details, not an ambiguous decision rule inside a criterion; an author has no channel for a criterion stricter than the claim's own statement; the gabor-sequence-structure criterion has no partial rule; the several-readings rule covers the paper's text, not ambiguous metadata in the dataset such as the time zone, which decides table2-sessions; streaming through remfile and h5py was too slow for the chunked files; the `data` categories have no slot for the paper's own supplementary table used to select sessions; the notebook may not read local paths, so it cannot check Supplementary Table 1 against Tables 1 and 2; and the suggested clock checks do not fit this design, so the response at grey screen transitions was compared against 500 time-shifted copies.

## End of run

12 turns, 2 minutes, result: success.
