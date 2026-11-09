# 000249 · recorder · run 40969157424

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 000249; ls transcripts/000249/ claims/000249/; cat attempts/000249-schiavo-2020-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '000249' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))"
```

```
<persisted-output>
Output too large (137.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d4205655-2246-41d9-aedc-1804a085d8c6/tool-results/bg3soxtca.txt

Preview (first 2KB):
docs/pilot-notes/000231-rodgers-2022-01.md
docs/pilot-notes/000140-churchland-2010-01.md
docs/pilot-notes/000129-makin-2018-01.md
docs/pilot-notes/000138-churchland-2010-01.md
docs/pilot-notes/000139-churchland-2010-01.md
| [000249](https://dandiarchive.org/dandiset/000249) | [Schiavo et al. 2020](https://doi.org/10.1038/s41586-020-2807-6) | 0 | 0 | 0 | 32 (+1) | [`000249-schiavo-2020`](entries/000249-schiavo-2020) |
claims/000249/:
10.1038-s41586-020-2807-6.yaml

transcripts/000249/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000249-schiavo-2020-01.yaml; grep -n "^| Dandiset\|^| Dataset\|^|---" README.md | head -3; python -c "
import json;d=json.load(open('targets/dandisets.json'))
import sys
s=json.dumps(d)
i=s.find('\"000249\"'); print(s[i-200:i+1500])"
```

```
<persisted-output>
Output too large (138.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d4205655-2246-41d9-aedc-1804a085d8c6/tool-results/bwm6zm2m3.txt

Preview (first 2KB):
schema_version: 2
id: 000249-schiavo-2020-01
dataset:
  archive: dandi
  id: 000249
  version: 0.230423.1416
  doi: 10.48324/dandi.000249/0.230423.1416
paper: doi:10.1038/s41586-020-2807-6
date: '2026-10-29'
entry: 000249-schiavo-2020
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c attempts/000249-schiavo-2020-01.yaml claims/000249/* transcripts/000249/*report.md docs/pilot-notes/000231-rodgers-2022-01.md docs/pilot-notes/001754-knierim-2000-02.md; sed -n 1,12p README.md | grep -n "|" ; grep -n "outcome:" attempts/000249-schiavo-2020-01.yaml | sort -k3 | uniq -c -f2 | head; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list))
for x in it:
  if str(x.get('id','')).endswith('000249') or x.get('dandiset')=='000249': print(json.dumps(x,indent=1)[:3000])
E
```

```
140029 attempts/000249-schiavo-2020-01.yaml
 63092 claims/000249/10.1038-s41586-020-2807-6.yaml
   727 transcripts/000249/answer-report.md
  1386 transcripts/000249/author-answers-report.md
  5045 transcripts/000249/author-report.md
  3690 transcripts/000249/author-revise-1-report.md
  3057 transcripts/000249/author-revise-2-report.md
  4542 transcripts/000249/claims-check-report.md
  3338 transcripts/000249/claims-report.md
  9050 transcripts/000249/verifier-1-report.md
  6384 transcripts/000249/verifier-2-report.md
  7642 docs/pilot-notes/000231-rodgers-2022-01.md
  2530 docs/pilot-notes/001754-knierim-2000-02.md
250512 total
    123 1004:    outcome: blocked
      3 1131:    outcome: not_reproduced
      3 1121:    outcome: partially_reproduced
      3 1249:    outcome: reproduced
{
 "dandiset": "000249",
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
grep -m3 -n "^| " README.md; grep -E "^    outcome:" attempts/000249-schiavo-2020-01.yaml | sort | uniq -c; grep -E "^  outcome:|^- claim:" attempts/000249-schiavo-2020-01.yaml | head -60; sed -n 1,80p tools/readme_row.py | grep -n "+"
```

```
82     outcome: blocked
      2     outcome: not_reproduced
      2     outcome: partially_reproduced
      2     outcome: reproduced
- claim: subject-group-link
  outcome: partially_reproduced
- claim: fig1a-isi-distribution
  outcome: blocked
- claim: fig1c-warm-vs-cold
  outcome: blocked
- claim: fig1c-salient-isis-retrieved
  outcome: blocked
- claim: fig1c-slow-and-single-not-retrieved
  outcome: blocked
- claim: ed2a-dams-evs-similar
  outcome: blocked
- claim: ed2b-latency-slow-longer
  outcome: blocked
- claim: fig4c-ch575-retrieve-slow
  outcome: blocked
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,70p tools/readme_row.py; grep -cE "^- claim:" attempts/000249-schiavo-2020-01.yaml; awk '/^- claim:/{c=$3} /^  outcome:/{print $2}' attempts/000249-schiavo-2020-01.yaml | sort | uniq -c
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
[... 55 more lines not kept]
```

**Agent**

So far: the row is 0 reproduced, 0 partial, 0 not reproduced, 32 (+1) blocked. Next I'm reading the reports and recent notes.

**Agent calls Bash**

```bash
cat docs/pilot-notes/000231-rodgers-2022-01.md docs/pilot-notes/000140-churchland-2010-01.md docs/pilot-notes/000129-makin-2018-01.md docs/pilot-notes/001754-knierim-2000-02.md | head -c 14000
```

```
# 000231, Rodgers et al. 2022

Twenty-three claims reproduced, none partially, six not reproduced and ten
blocked, all on the dataset. It pins version 0.220904.1554, which the paper
cites and which is the only published version. The paper, Rodgers in
Scientific Data, is a data descriptor for 115 sessions of 15 head-fixed mice
doing whisker-based shape discrimination or detection, with whisker video, pose
tracking, contacts and, in 44 sessions, neural recordings from barrel cortex;
it reports no statistical tests. The claims were written from the version of
record as served by Europe PMC, without its figures, and from the paper's
UsageNotes.ipynb (cxrodgers/NwbDandiData2022 at commit 33d610b). The counts of
mice, sessions, frames and neural hours, the task rules, the trials table, the
video and neural timebases, the units and electrodes, the pose and contact
tables, the file layout and the subjects were tested. `response-window-timing`,
`neural-video-alignment`, `behavior-clock-drift` and the three tracking error
claims are blocked as `data_missing`, as the motor times, the sync pulse
channels, the Arduino logs and the curated training sets are not deposited;
`reward-and-timeout` and `session-min-trials` are blocked as
`methods_underspecified`, as the criterion's readings disagree (a timeout of
12.21 s or 8.34 s; a smallest session of 84 or 101 trials), and the two claims
[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000249; for f in author-report.md claims-report.md claims-check-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done; ls -la --time-style=full-iso
```

```
<persisted-output>
Output too large (38.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d4205655-2246-41d9-aedc-1804a085d8c6/tool-results/bdi0ec48m.txt

Preview (first 2KB):
=== author-report.md
I've done steps 1 to 6 of the Author protocol for DANDI:000249. The entry is in `entries/000249-schiavo-2020/` and the record is `attempts/000249-schiavo-2020-01.yaml`. `entry.py all` passes with 0 errors (the notebook runs in 89 s), and the handover is built. Nothing is committed.

The main result is that the dandiset itself supports almost nothing. It holds raw, unaligned two-photon movies with no ROIs, no stimulus times and no record of the order in which the calls were played. So all 20 imaging claims are blocked, and only the link claim could be tested on the dandiset's own data. The other tested claims use the whole-cell, slice and operant recordings in the figshare collection the dandiset links, which the claims file marks `data: elsewhere`.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| subject-group-link | partially reproduced |
| fig1g-ipsc-depress-faster | not reproduced (rests on an assumption) |
| fig1i-operant-prototypes, ed5b-press-count-unchanged | blocked: methods underspecified (the readings the criterion names disagree) |
| ed6ef-epsc-tuning, fig2j-ie-ratio-tracks-isi, fig2k-ipsc-exceeds-epsc-575 | not reproduced |
| fig2h-epsc-enhanced-ev | partially reproduced |
| fig2i-ipsc-weaker-nv | blocked: methods underspecified (largest 5 trials vs largest 10 give different outcomes) |
| ed9b-oxytocin-enhances-spiking | reproduced (rests on an assumption) |
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d4205655-2246-41d9-aedc-1804a085d8c6/tool-results/bdi0ec48m.txt"
}
```

```
1	=== author-report.md
2	I've done steps 1 to 6 of the Author protocol for DANDI:000249. The entry is in `entries/000249-schiavo-2020/` and the record is `attempts/000249-schiavo-2020-01.yaml`. `entry.py all` passes with 0 errors (the notebook runs in 89 s), and the handover is built. Nothing is committed.
3	
4	The main result is that the dandiset itself supports almost nothing. It holds raw, unaligned two-photon movies with no ROIs, no stimulus times and no record of the order in which the calls were played. So all 20 imaging claims are blocked, and only the link claim could be tested on the dandiset's own data. The other tested claims use the whole-cell, slice and operant recordings in the figshare collection the dandiset links, which the claims file marks `data: elsewhere`.
5	
6	**1. Outcomes**
7	
8	| Claim | Outcome |
9	|---|---|
10	| subject-group-link | partially reproduced |
11	| fig1g-ipsc-depress-faster | not reproduced (rests on an assumption) |
12	| fig1i-operant-prototypes, ed5b-press-count-unchanged | blocked: methods underspecified (the readings the criterion names disagree) |
13	| ed6ef-epsc-tuning, fig2j-ie-ratio-tracks-isi, fig2k-ipsc-exceeds-epsc-575 | not reproduced |
14	| fig2h-epsc-enhanced-ev | partially reproduced |
15	| fig2i-ipsc-weaker-nv | blocked: methods underspecified (largest 5 trials vs largest 10 give different outcomes) |
16	| ed9b-oxytocin-enhances-spiking | reproduced (rests on an assumption) |
17	| ed6h-dams-evs-epsc-similar | blocked: metadata insufficient |
18	| 20 imaging claims, fig3-retrieval-onset-range | blocked: metadata insufficient |
19	| 11 behaviour claims, fig1a-isi-distribution, ed4d-response-tracks-isi-probability | blocked: data missing |
20	
[... 312 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -nE "^\s+data:|kind: link" claims/000249/*.yaml | awk '{print $NF}' | sort | uniq -c; grep -nE "^[a-z_]+:" attempts/000249-schiavo-2020-01.yaml
```

```
10 elsewhere
      1 link
      1 with_inputs
      1 with_labels
1:schema_version: 2
2:id: 000249-schiavo-2020-01
3:dataset:
8:paper: doi:10.1038/s41586-020-2807-6
9:date: '2026-10-29'
10:entry: 000249-schiavo-2020
11:provenance:
22:inputs:
37:outcomes:
649:findings:
711:verifications:
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000249-schiavo-2020-01.yaml",
 "offset": 649,
 "limit": 65
}
```

```
649	findings:
650	- kind: data_missing
651	  statement: The NWB files hold only raw, unaligned two-photon movies. There are no ROIs or fluorescence traces,
652	    no stimulus times, no trial tables and no record of which call each trial played (pseudorandom order, Methods),
653	    so none of the paper's 20 imaging findings can be tested from the dandiset. The figshare imaging items
654	    hold the same movies.
655	- kind: data_missing
656	  statement: The behavioural data of Figs. 1c, 4c-e and Extended Data Figs. 2 and 8-9 (pup retrieval, latencies,
657	    y-maze) and the vocalization recordings of Fig. 1a are in neither the dandiset nor the figshare collection it
658	    links. The paper's figshare DOI 10.35092/yhjc.c.5037737 does not resolve.
659	- kind: metadata_insufficient
660	  statement: Groups (experienced or naive, dam, CH+575, opto-OT, cell type, hemisphere) are given only in free-text
661	    experiment descriptions; the indicator and location fields are "unknown" in every file, and the start of cohousing,
662	    needed for retrieval onset, is not recorded.
663	- kind: metadata_error
664	  statement: Three recordings (sessions of 2018-03-08 named plus24hrs_postexp1) are deposited under both sub-NV58
665	    and sub-NV63, with the same start times and frames; nothing says to which mouse they belong.
666	- kind: metadata_error
667	  statement: Subjects EV56 and EV62 are described as NV56 and NV62 in their own experiment descriptions, and the
668	    five tones-only mice carry no experience group in theirs; the figshare item titles give it (EV56_Experienced_Exc
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,30p claims/000249/*.yaml; grep -n "with_labels\|with_inputs" -B30 claims/000249/*.yaml | grep -E "id:|data:"
```

```
# Claims for Schiavo, Valtcheva, Bair-Marshall, Song, Martin & Froemke (2020), Nature 587, 426-431,
# on dandiset 000249.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23, protocol
# pilot-10 as stated in docs/protocol.md.
#
# Text read: the NIH author manuscript in PubMed Central (PMC7677212, NIHMS1609780), as served by
# ncbi_pmc: main text, Methods, the ten Extended Data figure legends and the four main figure legends.
# It is the accepted manuscript, not the version of record, and its title reads "Innate and plastic
# mechanisms in auditory cortex for maternal behavior". The paper has no separate supplement beyond
# Extended Data; the source data Excel sheet it mentions was not available and no claim relies on it.
# No PDF was read.
#
# Code. The paper's data and code statements point to figshare doi:10.35092/yhjc.c.5037737, which
# did not resolve on 2026-10-23 (doi.org, DataCite and the figshare API all return not found). The
# dandiset links figshare collection doi:10.6084/m9.figshare.c.5043830.v6, same title as the
# manuscript. Its only code item is "Behavior code" (doi:10.6084/m9.figshare.13054076.v1), read in
# full; it holds MATLAB scripts (KAMB_OperantTask_prototypes.m, _fast.m, _slows.m, a circuit loader
# and a date helper) and RPvdsEx circuits that run the operant task. They run 30 min sessions (1800 s)
# and append to a csv the time of every polling sample at which the touch sensor reads a touch; they
# hold no analysis. No analysis code for imaging, whole-cell or behaviour was found, so every method
[... 16 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000249-schiavo-2020-01.md",
 "content": "# 000249, Schiavo et al. 2020\n\nNo claims reproduced, none partially, none not reproduced and 32 blocked on\nthe dataset, with one more blocked that also needs outside data. It pins\nversion 0.230423.1416. The paper, Schiavo, Valtcheva, Bair-Marshall, Song,\nMartin and Froemke in Nature, studies maternal behaviour in mouse auditory\ncortex: pup retrieval by dams and by virgin females cohoused with them, two-photon\nimaging of responses to pup calls whose inter-syllable intervals (ISIs) were\nvaried, whole-cell recordings of excitation and inhibition, and oxytocin's\nrole in the plasticity. The claims were written from the NIH author manuscript\nin PubMed Central (PMC7677212), not the version of record; the paper's code and\ndata DOI (10.35092/yhjc.c.5037737) does not resolve, no analysis code was\nfound, and the claims check made 20 corrections before the attempt. The\ndandiset holds only the two-photon imaging, so the 20 imaging claims and\n`fig3-retrieval-onset-range` are blocked as `metadata_insufficient`, and\n`fig1a-isi-distribution`, the behaviour claims and\n`ed4d-response-tracks-isi-probability` as `data_missing`. The link claim\n`subject-group-link` is partially reproduced: every subject has a figshare\nitem titled with its mouse id (54 of 54) and 7 of the 9 group counts match the\npaper, but no file says which call each trial played. Ten claims use the\nwhole-cell, slice and operant recordings of the figshare collection the\ndandiset links (doi:10.6084/m9.figshare.c.5043830.v6) and are left out of the\ncounts: `ed9b-oxytocin-enhances-spiking` is reproduced and\n`fig1g-ipsc-depress-faster` not reproduced, each resting on an assumption;\n`fig1i-operant-prototypes` and `ed5b-press-count-unchanged` are blocked as\n`methods_underspecified`, as the readings disagree; `ed6h-dams-evs-epsc-similar`\nis blocked as `metadata_insufficient`; and the five in vivo whole-cell claims\nare blocked as `other`. The author's first run had four of those five as not\nreproduced and `fig2h-epsc-enhanced-ev` as partially reproduced. Round 1 found\nthat the measure failed its own positive control (only 1 of 12 EV and 2 of 14\nNV EPSC cells showed a call-evoked current of the expected sign) and that the\npre-call window gave the same experienced against naive differences, and the\nauthor found the call onset fell a median 193 ms late in 51 of 83 files, fixed\nit, and moved the five claims to blocked; its points also led to the groups\nread from the figshare titles, per-cell traces aligned to onset, the\ninclusion-rule counts, the slice pulse times checked against the stimulus\nartefacts (91.8% within 1 ms) and the oxytocin labels printed. Round 2 agreed\nwith all 44 outcomes, so there was no third round; it found wording the\nnumbers did not support, among them \"no current that follows the calls\" where\n13 of 110 files show a sweep-locked deflection against 5.5 expected, an\nout-of-date imaging sentence in all 20 imaging notes and a call rate recorded\nas a metadata error where 10.24 s is 0.098 Hz, which were corrected. No\nquestions were put to a reader, so the answer run and the following author\nrun changed nothing. The author's run took about 33 minutes (03:32 to 04:05\nUTC) and nothing failed; in the last revision a run failed once on a dropped\nfigshare connection and the downloads now retry. The notebook ran in 89 s at\nfirst and in 356 s in the last run.\n\nThe NWB files hold only raw, unaligned two-photon movies, with no ROIs or\nfluorescence traces, no stimulus times, no trial tables and no record of which\ncall each trial played, so none of the paper's 20 imaging findings can be\ntested; the movies recur every 40 frames (10.24 s, 0.098 Hz) and in 31 of 38\nthree-call movies folding at three trial periods stands above two and four, as\na fixed cycle of three calls would, though the Methods say the order was\npseudorandom and no file says which call sits at which position. The pup\nretrieval, latency and y-maze data and the vocalization recordings are in\nneither the dandiset nor the figshare collection. Groups are given only in\nfree-text experiment descriptions, the indicator and location fields are\n\"unknown\" in every file, and the start of cohousing is not recorded. Three\nrecordings (sessions of 2018-03-08 named plus24hrs_postexp1) are deposited\nunder both sub-NV58 and sub-NV63 with the same start times and frames, and\nEV56 and EV62 are described as NV56 and NV62 in their own experiment\ndescriptions. In the in vivo whole-cell recordings the current almost never\nfollows the played calls: the evoked measure is in the expected direction at\np < 0.05 in 2 of 39 cell recordings (3 of 39 before the call), 3 of the 13\nfiles with a sweep-locked deflection, from two cells (190326_e1 and\n190313_e2), carry an inward current from about 0.4 s after onset, the Methods'\ninclusion rule keeps at most 1 of 39, and the experienced recordings are about\ntwice as noisy as the naive ones (baseline s.d. 11.4 against 5.3 pA). The\nmicrophone channel shows the morph ISIs as 125, 275 and 575 ms with the\nprototype, as the figure legends say, played in a fixed order, where the\nMethods give 125, 225 and 575 ms. The whole-cell spreadsheet of experienced\nfemales does not say which cells come from dams; file 19424013 is listed at\n-70 mV but carries about +560 pA throughout; two listed files (193260007 and\n19o11005) are not deposited; and the operant touch-time files print five\nsignificant digits, so after 1000 s of a session they step by 0.1 s. Two\nquestions are put to the paper's authors: which gap between touch samples ends\na lever press and which sessions were compared, and how a significant PSC was\ndefined for the inclusion rule, how many of the \"largest 5-10 evoked trials\"\nwere averaged and how ranked, and which Dunn comparison family Extended Data\nFig. 9b used.\n\nThe author's points on the protocol: the claims file says to block when\nreadings disagree while step 1.6 allows adopting the best-supported reading as\nan assumption; the clock check does not fit files with no stimulus times, so\nthe microphone channel was used to time the calls; the protocol has no rule\nfor a measure taken exactly as the Methods define it that turns out to track\nnoise; and `docs/archives.md` has no figshare section, and its ABF files cannot\nbe streamed with the usual tools.\n"
}
```

```
File created successfully at: docs/pilot-notes/000249-schiavo-2020-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/000249-schiavo-2020-01.md",
 "old_string": "The author's first run had four of those five as not\nreproduced and `fig2h-epsc-enhanced-ev` as partially reproduced.",
 "new_string": "The author's first run had three of those five as not\nreproduced, `fig2h-epsc-enhanced-ev` as partially reproduced and\n`fig2i-ipsc-weaker-nv` as blocked as `methods_underspecified`."
}
```

```
The file docs/pilot-notes/000249-schiavo-2020-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
git status --short; grep -c "—\|rather\|\*\*" docs/pilot-notes/000249-schiavo-2020-01.md
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
?? docs/pilot-notes/000249-schiavo-2020-01.md
?? scripts
0
```

**Agent**

I wrote `docs/pilot-notes/000249-schiavo-2020-01.md` and changed no other file. The untracked dotfiles and folders at the repository root were there before this run, and I left them alone. Nothing is committed.

# 000249, Schiavo et al. 2020

No claims reproduced, none partially, none not reproduced and 32 blocked on
the dataset, with one more blocked that also needs outside data. It pins
version 0.230423.1416. The paper, Schiavo, Valtcheva, Bair-Marshall, Song,
Martin and Froemke in Nature, studies maternal behaviour in mouse auditory
cortex: pup retrieval by dams and by virgin females cohoused with them, two-photon
imaging of responses to pup calls whose inter-syllable intervals (ISIs) were
varied, whole-cell recordings of excitation and inhibition, and oxytocin's
role in the plasticity. The claims were written from the NIH author manuscript
in PubMed Central (PMC7677212), not the version of record; the paper's code and
data DOI (10.35092/yhjc.c.5037737) does not resolve, no analysis code was
found, and the claims check made 20 corrections before the attempt. The
dandiset holds only the two-photon imaging, so the 20 imaging claims and
`fig3-retrieval-onset-range` are blocked as `metadata_insufficient`, and
`fig1a-isi-distribution`, the behaviour claims and
`ed4d-response-tracks-isi-probability` as `data_missing`. The link claim
`subject-group-link` is partially reproduced: every subject has a figshare
item titled with its mouse id (54 of 54) and 7 of the 9 group counts match the
paper, but no file says which call each trial played. Ten claims use the
whole-cell, slice and operant recordings of the figshare collection the
dandiset links (doi:10.6084/m9.figshare.c.5043830.v6) and are left out of the
counts: `ed9b-oxytocin-enhances-spiking` is reproduced and
`fig1g-ipsc-depress-faster` not reproduced, each resting on an assumption;
`fig1i-operant-prototypes` and `ed5b-press-count-unchanged` are blocked as
`methods_underspecified`, as the readings disagree; `ed6h-dams-evs-epsc-similar`
is blocked as `metadata_insufficient`; and the five in vivo whole-cell claims
are blocked as `other`. The author's first run had three of those five as not
reproduced, `fig2h-epsc-enhanced-ev` as partially reproduced and
`fig2i-ipsc-weaker-nv` as blocked as `methods_underspecified`. Round 1 found
that the measure failed its own positive control (only 1 of 12 EV and 2 of 14
NV EPSC cells showed a call-evoked current of the expected sign) and that the
pre-call window gave the same experienced against naive differences, and the
author found the call onset fell a median 193 ms late in 51 of 83 files, fixed
it, and moved the five claims to blocked; its points also led to the groups
read from the figshare titles, per-cell traces aligned to onset, the
inclusion-rule counts, the slice pulse times checked against the stimulus
artefacts (91.8% within 1 ms) and the oxytocin labels printed. Round 2 agreed
with all 44 outcomes, so there was no third round; it found wording the
numbers did not support, among them "no current that follows the calls" where
13 of 110 files show a sweep-locked deflection against 5.5 expected, an
out-of-date imaging sentence in all 20 imaging notes and a call rate recorded
as a metadata error where 10.24 s is 0.098 Hz, which were corrected. No
questions were put to a reader, so the answer run and the following author
run changed nothing. The author's run took about 33 minutes (03:32 to 04:05
UTC) and nothing failed; in the last revision a run failed once on a dropped
figshare connection and the downloads now retry. The notebook ran in 89 s at
first and in 356 s in the last run.

The NWB files hold only raw, unaligned two-photon movies, with no ROIs or
fluorescence traces, no stimulus times, no trial tables and no record of which
call each trial played, so none of the paper's 20 imaging findings can be
tested; the movies recur every 40 frames (10.24 s, 0.098 Hz) and in 31 of 38
three-call movies folding at three trial periods stands above two and four, as
a fixed cycle of three calls would, though the Methods say the order was
pseudorandom and no file says which call sits at which position. The pup
retrieval, latency and y-maze data and the vocalization recordings are in
neither the dandiset nor the figshare collection. Groups are given only in
free-text experiment descriptions, the indicator and location fields are
"unknown" in every file, and the start of cohousing is not recorded. Three
recordings (sessions of 2018-03-08 named plus24hrs_postexp1) are deposited
under both sub-NV58 and sub-NV63 with the same start times and frames, and
EV56 and EV62 are described as NV56 and NV62 in their own experiment
descriptions. In the in vivo whole-cell recordings the current almost never
follows the played calls: the evoked measure is in the expected direction at
p < 0.05 in 2 of 39 cell recordings (3 of 39 before the call), 3 of the 13
files with a sweep-locked deflection, from two cells (190326_e1 and
190313_e2), carry an inward current from about 0.4 s after onset, the Methods'
inclusion rule keeps at most 1 of 39, and the experienced recordings are about
twice as noisy as the naive ones (baseline s.d. 11.4 against 5.3 pA). The
microphone channel shows the morph ISIs as 125, 275 and 575 ms with the
prototype, as the figure legends say, played in a fixed order, where the
Methods give 125, 225 and 575 ms. The whole-cell spreadsheet of experienced
females does not say which cells come from dams; file 19424013 is listed at
-70 mV but carries about +560 pA throughout; two listed files (193260007 and
19o11005) are not deposited; and the operant touch-time files print five
significant digits, so after 1000 s of a session they step by 0.1 s. Two
questions are put to the paper's authors: which gap between touch samples ends
a lever press and which sessions were compared, and how a significant PSC was
defined for the inclusion rule, how many of the "largest 5-10 evoked trials"
were averaged and how ranked, and which Dunn comparison family Extended Data
Fig. 9b used.

The author's points on the protocol: the claims file says to block when
readings disagree while step 1.6 allows adopting the best-supported reading as
an assumption; the clock check does not fit files with no stimulus times, so
the microphone channel was used to time the calls; the protocol has no rule
for a measure taken exactly as the Methods define it that turns out to track
noise; and `docs/archives.md` has no figshare section, and its ABF files cannot
be streamed with the usual tools.

## End of run

15 turns, 1 minutes, result: success.
