# 001199 · recorder · run 41370799120

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/001199/ transcripts/001199/; python tools/readme_row.py 001199; cat attempts/001199-gao-2025-01.yaml
```

```
<persisted-output>
Output too large (53.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/76d21ecd-7459-4858-ab07-d7586e465e22/tool-results/bjeqyapoj.txt

Preview (first 2KB):
docs/pilot-notes/001276-silkuniene-2025-01.md
docs/pilot-notes/001193-zhu-2022-01.md
docs/pilot-notes/001277-silkuniene-2025-01.md
docs/pilot-notes/001074-kalugin-2026-01.md
docs/pilot-notes/001065-dembrow-2024-01.md
claims/001199/:
10.1523-jneurosci.2218-24.2025.yaml

transcripts/001199/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cat /home/runner/.claude/projects/-home-runner-work-encore-encore/76d21ecd-7459-4858-ab07-d7586e465e22/tool-results/bjeqyapoj.txt | sed -n '40,400p'; grep -n "^| Dataset\|^| Dandiset\|^|---" README.md | head
```

```
paper: doi:10.1523/jneurosci.2218-24.2025
date: 2026-11-01
entry: 001199-gao-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/41291066974
inputs:
- what: The asset list (paths only) of dandiset 000946, the repository the paper's Methods name for
    all its data, read to compare its rats and session dates with those of 001199. Used for the
    notes of the subjects claim and a finding; no measurement is taken from it.
  source: DANDI:000946 version 0.250829.1249 (doi:10.48324/dandi.000946/0.250829.1249)
outcomes:
[... 341 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '400,700p' /home/runner/.claude/projects/-home-runner-work-encore-encore/76d21ecd-7459-4858-ab07-d7586e465e22/tool-results/bjeqyapoj.txt; head -30 README.md | grep "|"; for f in $(git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5); do echo "== $f"; cat $f; done; cat docs/pilot-notes/001754-knierim-2000-02.md | head -5
```

```
<persisted-output>
Output too large (57.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/76d21ecd-7459-4858-ab07-d7586e465e22/tool-results/bvqbiimtf.txt

Preview (first 2KB):
      session''s areas now come from units with more than 2,000 spikes, with every unit as a variant, and a variant leaves out the 2025 cohort (counts 2 and 0). The counts are 6 and 6 under
      every reading.'
  - claim: fig2-target-artifact
    agrees: true
    outcome: blocked
    reason: 'There is no raw voltage, no waveforms and no target-determination trials. I confirmed this in
      the archive API: every one of the 229 assets measures only ElectrodeGroup and Units, and no file
      is over 7.8 MB.'
    response: 'No change needed.'
  - claim: fig4-unit-counts
    agrees: false
    outcome: not_reproduced
    reason: 'Upper bounds from cell 13 settle this without RSU/FSU types. The claims file excludes non-paper
      pressures, so only the 5 V files count (plus 2025 files, whose voltage is unknown). Those hold
      76 POm units at 3,000 Hz (233 RSUs alone need at least 209.7), 53 POm units at 30 Hz (need at
      least 170.1), 201 S1 units at 3,000 Hz (need at least 280.8) and 186 S1 units at 30 Hz (RSUs
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Round\|^- date\|^  reviewed" attempts/001199-gao-2025-01.yaml | head -30; grep -n "agrees: false" attempts/001199-gao-2025-01.yaml | wc -l; grep -n "^|" README.md | head -3
```

```
345:- date: '2026-11-02'
348:  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
650:- date: '2026-11-02'
653:  reviewed: 'Round 2. The full executed notebook after the round-1 revision, the helper module, the claims
873:- date: '2026-11-02'
876:  reviewed: Round 3. The one proposed change of outcome (fig5-unit-counts, to blocked, data_missing) and
4
```

**Agent calls Bash**

```bash
cd  sed -n 640,700p attempts/001199-gao-2025-01.yaml; sed -n 860,1000p attempts/001199-gao-2025-01.yaml; grep -n "agrees: false" -A3 attempts/001199-gao-2025-01.yaml; grep -rn "Reproduced\|Partial" README.md | head -3
```

```
are missing and the column holds no type to interpret.'
  - claim: fig11d-ac-to-s1-3000
    agrees: true
    outcome: blocked
    reason: 'Each needs RSU/FSU types. celltype_label is described as "1 = RSU, 2 = FSU" but holds only 0,
      "S1" or "POm", and there are no waveforms (cells 4–5; the API agrees). No untyped part of these
      criteria can be tested. The verifier gives the block as metadata_insufficient.'
    response: 'Kept blocked. The data check now prints per-file value counts of celltype_label (no 1 or 2 in
      any of the 96 files). blocked_by is kept as data_missing, as for fig6-unit-counts: the waveforms
      are missing and the column holds no type to interpret.'
- date: '2026-11-02'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: 'Round 2. The full executed notebook after the round-1 revision, the helper module, the claims
    file and the attempt record, with the paper. The verifier agreed with 34 of the 35 outcomes and disagreed
    with fig5-unit-counts, which it would block as data_missing. It also listed sentences not supported
    by the printed outputs: the format_error finding''s normalized rate of 4,224% and "one to seven places
    per unit" (now printed; the 4,224% is removed), the files with 400 and 149 trials (now printed), the
    per-rat counts at 10 and 15 V behind the BH594 sentence (now printed, and the sentence names BH594
    and BH615), and those under fig11b-ac-responses.'
[... 99 more lines not kept]
```

**Agent**

Now the README column order and the recent notes for shape.

**Agent calls Bash**

```bash
cd  grep -n "| Dandiset\|| Dataset\|Reproduced |" README.md | head -3; for f in docs/pilot-notes/001276-silkuniene-2025-01.md docs/pilot-notes/001193-zhu-2022-01.md docs/pilot-notes/001074-kalugin-2026-01.md; do echo "== $f"; cat $f; done; head -3 docs/pilot-notes/001754-knierim-2000-02.md; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.values()) if '001199' in json.dumps(x)];print(json.dumps(e,indent=1)[:1500])"
```

```
== docs/pilot-notes/001276-silkuniene-2025-01.md
# 001276, Silkuniene et al. 2025

Eight claims reproduced on the dataset (two on an assumption), four partially
(one on an assumption), two not reproduced (both on an assumption) and eight
blocked, two for missing data and six as other; the one claim on outside
inputs, `fig1e-field-simulation`, is blocked for missing data. The first
verification round agreed with 22 of the 23 outcomes as they stood and the
second with 21, and the second revision proposed two changes, so a third round
reviewed those two and agreed with both. It pins version 0.250701.1609, the
only published version; the paper cites none. The paper, Silkuniene, Silkunas,
Pakhomova, Semenov and Pakhomov, "MHz compression of pulse packets facilitates
remote focusing of electroporation" in Bioelectrochemistry, delivers packets of
600 ns pulses through four needle electrodes to monolayers of CT26 and CHO-K1
cells and measures YO-PRO-1 (YP) uptake along the diagonals of the electrode
square, and the dataset holds 54 wells, the burst-number series of Figure 7 at
0.2 MHz plus CANCAN and control wells at 1 Hz, each file one stitched 19190 x
19190 image. The claims were written from the author manuscript (PMC12331426),
which lists no supplement, without seeing the figures; the paper links no code.
Of the Figure 7 claims, `fig7cf-fwhm-with-bursts` reproduces but fragilely, both
[... 361 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
def walk(x):
  if isinstance(x,dict):
    if x.get('dandiset')=='001199': print(json.dumps(x,indent=1))
    else: [walk(v) for v in x.values()]
  elif isinstance(x,list): [walk(v) for v in x]
walk(d)"; grep -n "^| Dandiset\|^| \[" README.md | head -2; grep -n "Dandiset |" README.md; wc -c transcripts/001199/*report.md; head -40 claims/001199/*.yaml
```

```
{
 "dandiset": "001199",
 "name": "Neural Pathways Modulation in the Anesthetized Rat Elicited by Trials of Transcranial Focused Ultrasound Stimulation",
 "published_version": "0.250829.1250",
 "asset_count": 229,
 "size_gb": 0.32,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Rattus norvegicus - Norway rat"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.1523/jneurosci.2218-24.2025",
   "title": "Transcranial Focused Ultrasound Modulates Feedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively Activating Excitatory Neurons",
   "relation": "IsDescribedBy",
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001199; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md verifier-3-report.md author-revise-3-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (32.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/76d21ecd-7459-4858-ab07-d7586e465e22/tool-results/by4dkgtu6.txt

Preview (first 2KB):
=== author-report.md
I've completed steps 1 to 5 and the handover (step 6). The entry passes `python tools/entry.py all` (the notebook runs in 205 s), and the handover package is in `executed/001199-gao-2025/handover/`. Nothing is committed.

The main result: this dandiset probably does not hold the paper's recordings. Its 13 rats were recorded from August 2024 to July 2025, after the paper's preprint of June 2024. The paper's Methods name dandiset 000946 for its data, and that dandiset lists 20 other rats recorded in 2023 and 2024; only BH594 is in both. On top of that, the files hold spike times only, with no waveforms, so the paper's RSU/FSU typing cannot be repeated, and every session uses 200 µs pulses, so the duty-cycle series is absent.

**1. Outcomes (35 claims)**

| Claim | Outcome |
|---|---|
| subjects | partially reproduced: 6 rats with S1+POm (paper 16) and 6 with S1+AC (paper 12); two rats are in both groups |
| fig11b-ac-responses | not reproduced: 194 AC units (paper 453); no Kruskal–Wallis test significant at 0.01; only 1,500 Hz during sonication is significant, and only under one reading (R1/T2); nothing is significant after sonication |
| fig2-target-artifact | blocked, `data_missing`: no raw voltage or target-determination trials |
| 20 claims on RSUs/FSUs (Fig. 4–6, 10A–C, 11C–D) | blocked, `data_missing`: no waveforms or type labels |
| 12 duty-cycle claims (fig7-9-unit-counts, Fig. 7–9, 10D–F) | blocked, `data_missing`: only PD 200 µs; types also missing |

**2. Findings, assumptions, questions**
[... 5 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/76d21ecd-7459-4858-ab07-d7586e465e22/tool-results/by4dkgtu6.txt"
}
```

```
1	=== author-report.md
2	I've completed steps 1 to 5 and the handover (step 6). The entry passes `python tools/entry.py all` (the notebook runs in 205 s), and the handover package is in `executed/001199-gao-2025/handover/`. Nothing is committed.
3	
4	The main result: this dandiset probably does not hold the paper's recordings. Its 13 rats were recorded from August 2024 to July 2025, after the paper's preprint of June 2024. The paper's Methods name dandiset 000946 for its data, and that dandiset lists 20 other rats recorded in 2023 and 2024; only BH594 is in both. On top of that, the files hold spike times only, with no waveforms, so the paper's RSU/FSU typing cannot be repeated, and every session uses 200 µs pulses, so the duty-cycle series is absent.
5	
6	**1. Outcomes (35 claims)**
7	
8	| Claim | Outcome |
9	|---|---|
10	| subjects | partially reproduced: 6 rats with S1+POm (paper 16) and 6 with S1+AC (paper 12); two rats are in both groups |
11	| fig11b-ac-responses | not reproduced: 194 AC units (paper 453); no Kruskal–Wallis test significant at 0.01; only 1,500 Hz during sonication is significant, and only under one reading (R1/T2); nothing is significant after sonication |
12	| fig2-target-artifact | blocked, `data_missing`: no raw voltage or target-determination trials |
13	| 20 claims on RSUs/FSUs (Fig. 4–6, 10A–C, 11C–D) | blocked, `data_missing`: no waveforms or type labels |
14	| 12 duty-cycle claims (fig7-9-unit-counts, Fig. 7–9, 10D–F) | blocked, `data_missing`: only PD 200 µs; types also missing |
15	
16	**2. Findings, assumptions, questions**
17	- **Type labels:** a `celltype_label` column is described as "1 = RSU, 2 = FSU" but holds 0 or the area name (S1/POm); 133 files have no such column.
18	- **Missing conditions:** there is no CG1 control at 3,000 Hz.
19	- **Undescribed conditions:** sessions at 10 and 15 V, stimulation at POm, and 64-channel probes; the paper used two 32-channel probes at 5 V.
20	- **Pressure metadata:** the pressure field read
[... 251 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Reproduced\|reproduced |" README.md | head -3; grep "^  outcome:" attempts/001199-gao-2025-01.yaml | sort | uniq -c; grep -c "blocked_by: data_missing" attempts/001199-gao-2025-01.yaml; grep -n "assumed" attempts/001199-gao-2025-01.yaml | head
```

```
32   outcome: blocked
      3   outcome: not_reproduced
32
228:  assumed: true
710:      should be blocked (data_missing), or else carry assumed: true with the assumption stated, that the
844:      assumptions stated only as deviations, not as assumed: true, that the 2025 files were recorded at
854:    response: 'Outcome kept, now with assumed: true; the two deviations on the 2025 voltage and onsets
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001199-gao-2025-01.md",
 "content": "# 001199, Gao et al. 2025\n\nNo claim reproduced, none partially, three not reproduced (one on an\nassumption) and 32 blocked, all 32 for missing data. The first verification\nround agreed with 32 of the 35 outcomes as they stood and the second with 34,\nand the second revision proposed one change, so a third round reviewed it and\nagreed. It pins version 0.250829.1250; all four published versions and the\ndraft hold the same 229 files and differ only in contributor order. The paper,\nGao, Ramachandran, Yu and He, \"Transcranial Focused Ultrasound Modulates\nFeedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively\nActivating Excitatory Neurons\" in the Journal of Neuroscience, steers 1.5 MHz\nultrasound to S1 in anesthetized rats while recording S1 and POm, and S1 and\nauditory cortex (AC) in a second group, with two 32-channel probes, and sorts\nunits into RSUs and FSUs from their waveforms across series of PRF and duty\ncycle; the dataset holds sorted spike times and trial tables from 13 rats. The\nclaims were written from the version of record as served by PubMed Central,\nwhich has no supplement; the paper links no code, and its Methods name\ndandiset 000946 as the repository of all its data. `subjects` is not\nreproduced: 6 rats have simultaneous S1 and POm recordings (paper 16) and 6\nhave S1 and AC (paper 12), under every reading, and the rats cannot be a subset\nof the paper's, every S1 file listing a 64-channel A1x64-Edge probe (or H9),\ntwo rats (BH648, BH658) being in both groups and none of the ten being in\n000946. `fig4-unit-counts` is not reproduced on upper bounds from untyped\nunits: in the claims file's sessions at most 4 of the 8 counts can be within\n10%, where a partial result needs 6. `fig11b-ac-responses` is not reproduced\non the assumptions that the 2025 sessions were at 5 V and that their trial\nstarts are the sonication onsets: 194 AC units in 7 rats (paper 453), no\nKruskal-Wallis test significant at 0.01 (p 0.013 to 0.74), only 1,500 Hz during\nsonication significant and only under R1 and T2, and no PRF above baseline\nafter sonication. The other 32 claims are blocked as `data_missing`: 18 on RSUs\nand FSUs for want of waveforms or type labels, the duty-cycle series of\nFigures 7 to 9 and 10D to 10F, the raw voltage of Figure 2, and\n`fig5-unit-counts` and `fig5b-cg1-control-no-response` for want of a CG1\ncontrol at 3,000 Hz. The author's first run gave `subjects` as partially\nreproduced, `fig11b-ac-responses` as not reproduced and 33 blocked. The author\nasked a reader nothing, so the answer and author-answers runs changed nothing.\nRound 1 disagreed with `subjects`, `fig4-unit-counts` and `fig5-unit-counts`,\nwhich moved to not reproduced, gave `metadata_insufficient` for 17 blocked\nclaims, and asked whether the 2025 trial starts are onsets; in reply the main\ncounts were restricted to the 5 V files plus every 2025 file, the \"none extra\"\nevidence was printed, and a lagged correlogram and an untyped S1 positive\ncontrol were added. Round 2 withdrew `metadata_insufficient`, disagreed with\n`fig5-unit-counts`, since CG1 sessions at 300 and 4,500 Hz cannot bound control\nsessions at 3,000 Hz that were not deposited, asked that `fig11b-ac-responses`\nbe marked assumed and that the T2 rise of 2025 S1 units be reported, and found\nsentences the outputs did not support (the 4,224% rate, the places out of order\nper unit, the files with 400 and 149 trials, a delayed rise from about 125 ms,\nthe BH594 counts at 10 and 15 V, the R2 means without BH654), all corrected or\nprinted. The second revision proposed `blocked` for `fig5-unit-counts`, and\nround 3 agreed, noting that `fig5b-cg1-control-no-response` is the direct\nparallel and `fig7-9-unit-counts` not quite one. The author's run took about\n50 minutes (08:59 to 09:48 UTC) with nothing failing, an early bug on unsorted\nspike times having been fixed; the notebook ran in 205 s at first, 94 s after\nthe author-answers run, 133 s after round 1, 116 s after round 2 and 147 s at\nthe end. `tools/build_site.py` and `tools/site_assets/progress.js` were found\nmodified and left untouched.\n\nThe dandiset names the paper as the description of its data, but its 13 rats\nwere recorded from August 2024 to July 2025, after the paper's preprint of June\n2024, and of them only BH594 has a file in dandiset 000946, which lists 20 rats\nrecorded from August 2023 to April 2024; it also holds conditions the paper does\nnot describe (10 and 15 V, stimulation at POm, 64-channel probes with and\nwithout z-coating, 2 mm offsets). The files hold spike times only, with no\nspike waveforms and no RSU or FSU labels, so the paper's typing of units cannot\nbe repeated, and of the 20 claims on RSUs and FSUs 18 cannot be tested. The\nunits column celltype_label is described as \"label 1 = RSU, label 2 = FSU\", but\nno file holds a 1 or a 2 (1,272 units labelled 0, 414 POm and 773 S1): it holds\n0 in the 49 files of BH590 and BH594 and the area of the unit in the 47 files of\nBH596 and BH615, and the 133 files of the 2025 cohort have no such column. Every\nstimulated file has a pulse duration of 200 us, so the duty-cycle series are\nabsent, as are the target-determination trials and raw voltage of Figure 2 and\na CG1 control at 3,000 Hz (CG1 sessions are at 300 and 4,500 Hz). In the 2025\ncohort, which holds every AC recording, the spikes lock to the trial starts no\nmore than to starts shifted by 1.25 s (true above shifted in 7 of 108\nstimulated files), and the population correlogram peaks within 0 to 400 ms of\nthe trial start in 4 of 108 stimulated files, against 39 of 92 in the 2024\ncohort, with no other lag within 60 s at which the files lock; untyped S1 units\nof the 2025 cohort show a weak rise at 30 and 1,500 Hz (means 107 to 109%), so\nsome sessions lock, and for the others the files cannot tell missing responses\nfrom trial times that are not onsets. The data_collection field gives\n\"PRESSURE:67V\" in most 2024 files whatever voltage the identifier gives (the 67\nis the ultrasound duration), and the 2025 files state no pressure or voltage\nanywhere. The stimulation targets \"S1-6\", \"NEW\", \"y-1\" and \"SEP\" and the\nidentifier tags of the 2024 files are explained nowhere, and electrode\nlocations are \"unknown\" in every file. In the 2025 cohort session_start_time\ndoes not date the session, two probe files of one session having start times\nminutes apart and the BH608 sham pair five months apart (2025-02-06 and\n2025-07-11), and one file is named ses-None; in the BH608 30 Hz session the S1\nfile gives stimulation at S1 and the POm file, sharing its trial table, at\n\"SEP\". In 64 units of 16 files of the 2025 cohort the spike times are not in\nincreasing order (one to seven places per unit), and they are sorted on\nreading. The files sub-BH646_ses-None and sub-BH646_ses-20250308T003900 hold\nthe same recording (AC at 30 Hz). The S1 files list 64-channel A1x64-Edge\nprobes where the paper used two 32-channel A1x32-Poly3 probes, four BH590 files\nname a device \"H9\", and the description gives 500 trials per recording where\nmost files hold 499 and some 113 to 480. No question is put to the paper's\nauthors, every reading giving the same outcome; the data owners could state the\nvoltage and the trial timing of the 2025 sessions.\n\nThe author's points on the protocol: it has no rule for a dataset that may not\nhold the paper's data when the paper names another dandiset, and 001199 was\ntested as the claims file says with the mismatch recorded as a finding; step\n1.4 does not say whether another dandiset's file list may be read just to\nidentify rats, and 000946's asset paths were listed under `inputs`; with\nwaveforms absent and the label column mislabelled the claims could be\n`data_missing` or `metadata_insufficient`, and `data_missing` was chosen; it\ndoes not say how a failed clock check bears on a claim whose result is an\nabsence of response; \"none extra\" in the subjects criterion cannot be checked\nwithout the paper's list of rats; the claims file's Bonferroni factor B1 is\nambiguous, and factors of 5, 10 and 15 were run; and it records format errors\nwithout saying whether to repair them, and the spike times were sorted.\n"
}
```

```
File created successfully at: docs/pilot-notes/001199-gao-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/001199-gao-2025-01.md",
 "old_string": "blocked as `data_missing`: 18 on RSUs\nand FSUs for want",
 "new_string": "blocked as `data_missing`: 17 on RSUs\nand FSUs for want"
}
```

```
The file docs/pilot-notes/001199-gao-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -n "—\|rather\|\*\*" docs/pilot-notes/001199-gao-2025-01.md
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
?? docs/pilot-notes/001199-gao-2025-01.md
?? scripts
```

**Agent**

I wrote the notes in `docs/pilot-notes/001199-gao-2025-01.md` and changed no other file. Nothing is committed. The working tree already had untracked files at the repository root (`scripts`, `.idea`, shell profiles and others) before I started; they aren't mine, and I left them alone.

# 001199, Gao et al. 2025

No claim reproduced, none partially, three not reproduced (one on an
assumption) and 32 blocked, all 32 for missing data. The first verification
round agreed with 32 of the 35 outcomes as they stood and the second with 34,
and the second revision proposed one change, so a third round reviewed it and
agreed. It pins version 0.250829.1250; all four published versions and the
draft hold the same 229 files and differ only in contributor order. The paper,
Gao, Ramachandran, Yu and He, "Transcranial Focused Ultrasound Modulates
Feedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively
Activating Excitatory Neurons" in the Journal of Neuroscience, steers 1.5 MHz
ultrasound to S1 in anesthetized rats while recording S1 and POm, and S1 and
auditory cortex (AC) in a second group, with two 32-channel probes, and sorts
units into RSUs and FSUs from their waveforms across series of PRF and duty
cycle; the dataset holds sorted spike times and trial tables from 13 rats. The
claims were written from the version of record as served by PubMed Central,
which has no supplement; the paper links no code, and its Methods name
dandiset 000946 as the repository of all its data. `subjects` is not
reproduced: 6 rats have simultaneous S1 and POm recordings (paper 16) and 6
have S1 and AC (paper 12), under every reading, and the rats cannot be a subset
of the paper's, every S1 file listing a 64-channel A1x64-Edge probe (or H9),
two rats (BH648, BH658) being in both groups and none of the ten being in
000946. `fig4-unit-counts` is not reproduced on upper bounds from untyped
units: in the claims file's sessions at most 4 of the 8 counts can be within
10%, where a partial result needs 6. `fig11b-ac-responses` is not reproduced
on the assumptions that the 2025 sessions were at 5 V and that their trial
starts are the sonication onsets: 194 AC units in 7 rats (paper 453), no
Kruskal-Wallis test significant at 0.01 (p 0.013 to 0.74), only 1,500 Hz during
sonication significant and only under R1 and T2, and no PRF above baseline
after sonication. The other 32 claims are blocked as `data_missing`: 17 on RSUs
and FSUs for want of waveforms or type labels, the duty-cycle series of
Figures 7 to 9 and 10D to 10F, the raw voltage of Figure 2, and
`fig5-unit-counts` and `fig5b-cg1-control-no-response` for want of a CG1
control at 3,000 Hz. The author's first run gave `subjects` as partially
reproduced, `fig11b-ac-responses` as not reproduced and 33 blocked. The author
asked a reader nothing, so the answer and author-answers runs changed nothing.
Round 1 disagreed with `subjects`, `fig4-unit-counts` and `fig5-unit-counts`,
which moved to not reproduced, gave `metadata_insufficient` for 17 blocked
claims, and asked whether the 2025 trial starts are onsets; in reply the main
counts were restricted to the 5 V files plus every 2025 file, the "none extra"
evidence was printed, and a lagged correlogram and an untyped S1 positive
control were added. Round 2 withdrew `metadata_insufficient`, disagreed with
`fig5-unit-counts`, since CG1 sessions at 300 and 4,500 Hz cannot bound control
sessions at 3,000 Hz that were not deposited, asked that `fig11b-ac-responses`
be marked assumed and that the T2 rise of 2025 S1 units be reported, and found
sentences the outputs did not support (the 4,224% rate, the places out of order
per unit, the files with 400 and 149 trials, a delayed rise from about 125 ms,
the BH594 counts at 10 and 15 V, the R2 means without BH654), all corrected or
printed. The second revision proposed `blocked` for `fig5-unit-counts`, and
round 3 agreed, noting that `fig5b-cg1-control-no-response` is the direct
parallel and `fig7-9-unit-counts` not quite one. The author's run took about
50 minutes (08:59 to 09:48 UTC) with nothing failing, an early bug on unsorted
spike times having been fixed; the notebook ran in 205 s at first, 94 s after
the author-answers run, 133 s after round 1, 116 s after round 2 and 147 s at
the end. `tools/build_site.py` and `tools/site_assets/progress.js` were found
modified and left untouched.

The dandiset names the paper as the description of its data, but its 13 rats
were recorded from August 2024 to July 2025, after the paper's preprint of June
2024, and of them only BH594 has a file in dandiset 000946, which lists 20 rats
recorded from August 2023 to April 2024; it also holds conditions the paper does
not describe (10 and 15 V, stimulation at POm, 64-channel probes with and
without z-coating, 2 mm offsets). The files hold spike times only, with no
spike waveforms and no RSU or FSU labels, so the paper's typing of units cannot
be repeated, and of the 20 claims on RSUs and FSUs 18 cannot be tested. The
units column celltype_label is described as "label 1 = RSU, label 2 = FSU", but
no file holds a 1 or a 2 (1,272 units labelled 0, 414 POm and 773 S1): it holds
0 in the 49 files of BH590 and BH594 and the area of the unit in the 47 files of
BH596 and BH615, and the 133 files of the 2025 cohort have no such column. Every
stimulated file has a pulse duration of 200 us, so the duty-cycle series are
absent, as are the target-determination trials and raw voltage of Figure 2 and
a CG1 control at 3,000 Hz (CG1 sessions are at 300 and 4,500 Hz). In the 2025
cohort, which holds every AC recording, the spikes lock to the trial starts no
more than to starts shifted by 1.25 s (true above shifted in 7 of 108
stimulated files), and the population correlogram peaks within 0 to 400 ms of
the trial start in 4 of 108 stimulated files, against 39 of 92 in the 2024
cohort, with no other lag within 60 s at which the files lock; untyped S1 units
of the 2025 cohort show a weak rise at 30 and 1,500 Hz (means 107 to 109%), so
some sessions lock, and for the others the files cannot tell missing responses
from trial times that are not onsets. The data_collection field gives
"PRESSURE:67V" in most 2024 files whatever voltage the identifier gives (the 67
is the ultrasound duration), and the 2025 files state no pressure or voltage
anywhere. The stimulation targets "S1-6", "NEW", "y-1" and "SEP" and the
identifier tags of the 2024 files are explained nowhere, and electrode
locations are "unknown" in every file. In the 2025 cohort session_start_time
does not date the session, two probe files of one session having start times
minutes apart and the BH608 sham pair five months apart (2025-02-06 and
2025-07-11), and one file is named ses-None; in the BH608 30 Hz session the S1
file gives stimulation at S1 and the POm file, sharing its trial table, at
"SEP". In 64 units of 16 files of the 2025 cohort the spike times are not in
increasing order (one to seven places per unit), and they are sorted on
reading. The files sub-BH646_ses-None and sub-BH646_ses-20250308T003900 hold
the same recording (AC at 30 Hz). The S1 files list 64-channel A1x64-Edge
probes where the paper used two 32-channel A1x32-Poly3 probes, four BH590 files
name a device "H9", and the description gives 500 trials per recording where
most files hold 499 and some 113 to 480. No question is put to the paper's
authors, every reading giving the same outcome; the data owners could state the
voltage and the trial timing of the 2025 sessions.

The author's points on the protocol: it has no rule for a dataset that may not
hold the paper's data when the paper names another dandiset, and 001199 was
tested as the claims file says with the mismatch recorded as a finding; step
1.4 does not say whether another dandiset's file list may be read just to
identify rats, and 000946's asset paths were listed under `inputs`; with
waveforms absent and the label column mislabelled the claims could be
`data_missing` or `metadata_insufficient`, and `data_missing` was chosen; it
does not say how a failed clock check bears on a claim whose result is an
absence of response; "none extra" in the subjects criterion cannot be checked
without the paper's list of rats; the claims file's Bonferroni factor B1 is
ambiguous, and factors of 5, 10 and 15 were run; and it records format errors
without saying whether to repair them, and the spike times were sorted.

## End of run

14 turns, 2 minutes, result: success.
