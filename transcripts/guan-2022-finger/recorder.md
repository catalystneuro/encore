# 000252 · recorder · run 41847544367

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 000252; ls claims/000252 transcripts/000252; cat attempts/000252-guan-2022-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '000252' in json.dumps(x)];print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (256.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d0d06cf6-e5eb-45fc-9ef7-1e1f11abc6e2/tool-results/bznoi8fgv.txt

Preview (first 2KB):
docs/pilot-notes/001868-kim-2026-01.md
docs/pilot-notes/001882-yuan-2025-01.md
docs/pilot-notes/001767-chantranupong-2023-01.md
docs/pilot-notes/001845-shukla-2026-01.md
docs/pilot-notes/001749-padilla-coreano-2022-01.md
| [000252](https://dandiarchive.org/dandiset/000252) | [Guan et al. 2022](https://doi.org/10.1101/2022.12.07.22283227) | 9 | 1 | 1 | 8 | [`000252-guan-2022`](entries/000252-guan-2022) |
claims/000252:
10.1101-2022.12.07.22283227.yaml

transcripts/000252:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/000252-guan-2022-01.yaml; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else d[0].keys())
E
```

```
<persisted-output>
Output too large (34.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d0d06cf6-e5eb-45fc-9ef7-1e1f11abc6e2/tool-results/baaoftcxi.txt

Preview (first 2KB):
schema_version: 2
id: 000252-guan-2022-01
dataset:
  archive: dandi
  id: "000252"
  version: 0.230408.2207
  doi: 10.48324/dandi.000252/0.230408.2207
paper: doi:10.1101/2022.12.07.22283227
date: 2026-11-04
entry: 000252-guan-2022
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 40 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d0d06cf6-e5eb-45fc-9ef7-1e1f11abc6e2/tool-results/baaoftcxi.txt"
}
```

```
1	schema_version: 2
2	id: 000252-guan-2022-01
3	dataset:
4	  archive: dandi
5	  id: "000252"
6	  version: 0.230408.2207
7	  doi: 10.48324/dandi.000252/0.230408.2207
8	paper: doi:10.1101/2022.12.07.22283227
9	date: 2026-11-04
10	entry: 000252-guan-2022
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
[... 576 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in docs/pilot-notes/001868-kim-2026-01.md docs/pilot-notes/001882-yuan-2025-01.md docs/pilot-notes/001767-chantranupong-2023-01.md docs/pilot-notes/001845-shukla-2026-01.md docs/pilot-notes/001749-padilla-coreano-2022-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "== $f"; cat $f; done; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
for t in d['targets']:
    if '000252' in json.dumps(t): print(json.dumps(t,indent=1)[:3000])
E
```

```
<persisted-output>
Output too large (54.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d0d06cf6-e5eb-45fc-9ef7-1e1f11abc6e2/tool-results/bzr0lgu27.txt

Preview (first 2KB):
== docs/pilot-notes/001868-kim-2026-01.md
# 001868, Kim et al. 2026

Sixteen claims reproduced (three on an assumption), four partially, four not
reproduced and 19 blocked, 17 as metadata insufficient and two for missing
data. All 43 claims are on the dandiset. The first verification round agreed
with 38 of the 43 outcomes as they stood and the second with all 43; nothing
was proposed after the second, so there was no third round. It pins version
0.260715.2016, which the paper's data statement cites, the only published
version, with the draft identical to it. The paper, Kim, Lycke, Zolotavin,
Montes, Xie and Luan, "Learning induces activation-mechanism-dependent neural
plasticity in an intracortical microstimulation task" in Science Advances,
trains six Thy1-GCaMP6s mice, implanted with a 32-channel ultraflexible NET in
S1 under a cranial window, to report microstimulation by a wheel turn over
weeks 0 to 4, and follows the evoked spiking and two-photon calcium responses
against six control mice stimulated without behaviour; the dandiset holds 85
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d0d06cf6-e5eb-45fc-9ef7-1e1f11abc6e2/tool-results/bzr0lgu27.txt"
}
```

```
1	== docs/pilot-notes/001868-kim-2026-01.md
2	# 001868, Kim et al. 2026
3	
4	Sixteen claims reproduced (three on an assumption), four partially, four not
5	reproduced and 19 blocked, 17 as metadata insufficient and two for missing
6	data. All 43 claims are on the dandiset. The first verification round agreed
7	with 38 of the 43 outcomes as they stood and the second with all 43; nothing
8	was proposed after the second, so there was no third round. It pins version
9	0.260715.2016, which the paper's data statement cites, the only published
10	version, with the draft identical to it. The paper, Kim, Lycke, Zolotavin,
11	Montes, Xie and Luan, "Learning induces activation-mechanism-dependent neural
12	plasticity in an intracortical microstimulation task" in Science Advances,
13	trains six Thy1-GCaMP6s mice, implanted with a 32-channel ultraflexible NET in
14	S1 under a cranial window, to report microstimulation by a wheel turn over
15	weeks 0 to 4, and follows the evoked spiking and two-photon calcium responses
16	against six control mice stimulated without behaviour; the dandiset holds 85
17	assets (7.5 GB) in NWB of the processed electrophysiology, behaviour and imaging,
18	with 55 behavioural sessions and the control animals' files. The claims were
19	written from the version of record in Europe PMC (PMC13544205) and the
20	supplement, which holds figure legends only, and from the paper's code
[... 759 more lines not kept]
```

**Agent**

Read the five recent notes and the attempt record; now reading the run reports and the claims file.

**Agent calls Bash**

```bash
cd transcripts/000252; wc -c *-report.md; ls -l --time-style=full-iso *-report.md | awk '{print $7, $9}'; head -c 1500 ../../claims/000252/*.yaml
```

```
673 answer-report.md
 2044 author-answers-report.md
 5229 author-report.md
 3726 author-revise-1-report.md
 2623 author-revise-2-report.md
 2637 claims-check-report.md
 3963 claims-report.md
 8615 verifier-1-report.md
 7368 verifier-2-report.md
36878 total
14:27:12.687742964 answer-report.md
14:27:12.687742964 author-answers-report.md
14:27:12.687742964 author-report.md
14:27:12.687742964 author-revise-1-report.md
14:27:12.688258845 author-revise-2-report.md
14:27:11.040228763 claims-check-report.md
14:27:11.041515028 claims-report.md
14:27:12.689258863 verifier-1-report.md
14:27:12.689258863 verifier-2-report.md
# Claims for Guan et al., "Compositional coding of individual finger movements in human posterior
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000252; for f in author answer author-answers verifier-1 author-revise-1 verifier-2 author-revise-2; do echo "=== $f"; cat $f-report.md; done
```

```
<persisted-output>
Output too large (29.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d0d06cf6-e5eb-45fc-9ef7-1e1f11abc6e2/tool-results/bizf2bbed.txt

Preview (first 2KB):
=== author
I finished steps 1 to 5 for DANDI:000252 against the claims file, and the handover package is built. `python tools/entry.py all` passed with 0 errors, and the executed outputs were identical to my development run. Of the 19 claims, 9 were reproduced, 1 partially reproduced, 1 not reproduced and 8 blocked; two outcomes rest on assumptions. The work is not verified yet, since the verifier comes next, and nothing was committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| tenfinger-recording-counts | reproduced (the paper's counts are those before the 0.5 Hz exclusion) |
| tenfinger-pooled-npcc-neurons | reproduced (1114 units, paper 1111) |
| tenfinger-discriminative-fraction | not reproduced (at most 48.9 / 38.1 / 65.6% against 66 / 57 / 78%) |
| tenfinger-decoding-accuracy | reproduced (72 / 70 / 79% against 70 / 66 / 75%) |
| tenfinger-error-structure | reproduced |
| fig8b-matching-closer | reproduced, resting on an assumption |
| fig8a-npcc-index-distinct | reproduced |
| fig8e-hand-ccgp | reproduced |
| fig8e-finger-ccgp | reproduced under O9 (b); J-MC misses the 0.9 margin of O9 (a) |
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d0d06cf6-e5eb-45fc-9ef7-1e1f11abc6e2/tool-results/bizf2bbed.txt"
}
```

```
1	=== author
2	I finished steps 1 to 5 for DANDI:000252 against the claims file, and the handover package is built. `python tools/entry.py all` passed with 0 errors, and the executed outputs were identical to my development run. Of the 19 claims, 9 were reproduced, 1 partially reproduced, 1 not reproduced and 8 blocked; two outcomes rest on assumptions. The work is not verified yet, since the verifier comes next, and nothing was committed.
3	
4	## 1. Outcomes
5	
6	| Claim | Outcome |
7	|---|---|
8	| tenfinger-recording-counts | reproduced (the paper's counts are those before the 0.5 Hz exclusion) |
9	| tenfinger-pooled-npcc-neurons | reproduced (1114 units, paper 1111) |
10	| tenfinger-discriminative-fraction | not reproduced (at most 48.9 / 38.1 / 65.6% against 66 / 57 / 78%) |
11	| tenfinger-decoding-accuracy | reproduced (72 / 70 / 79% against 70 / 66 / 75%) |
12	| tenfinger-error-structure | reproduced |
13	| fig8b-matching-closer | reproduced, resting on an assumption |
14	| fig8a-npcc-index-distinct | reproduced |
15	| fig8e-hand-ccgp | reproduced |
16	| fig8e-finger-ccgp | reproduced under O9 (b); J-MC misses the 0.9 margin of O9 (a) |
17	| jppc-finger-ccgp-low | partially reproduced, resting on an assumption; p < 0.001 in only 1 of 8 readings |
18	| figs11-jppc-lower-matched-size | reproduced |
19	| fig4c, fig4e, fig5a, fig5bcd, fig5e | blocked, data_missing (alternating-cues task not in the dataset) |
20	| fig6-online-bmi, figs6, figs7 | blocked, data_missing (BMI sessions not in the dataset) |
[... 246 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/000252/*.yaml; sed -n 20,80p $f; grep -n -i "check\|author\|Guan\|^  - id\|^- id" $f | head -60
```

```
# meant to hold the ten-finger (right and left hand) task; whether it also holds the
# contralateral-only, reaction-time and BMI sessions is for the author to find.
#
# Data the paper used.
# - Participants. N, tetraplegic woman (C3-C4, AIS-A), one working 96-channel Utah array in left
#   PPC at the junction of the intraparietal and postcentral sulci (PC-IP), called N-PPC. J,
#   tetraplegic man (C4-C5), two 96-channel arrays recorded simultaneously, J-PPC in the superior
#   parietal lobule and J-MC near the hand knob of left motor cortex.
# - Ten-finger press task (Figure 3, 7, 8). Text-cued, instructed delay, all ten fingers (R or L
#   hand; t, i, m, r, p) interleaved in each run-block. N, 100 trials per session over 10
#   sessions; J, 100 trials per session over 2 sessions. N-PPC 111 neurons per session (102 to
#   119), 1111 pooled; J-PPC 160 (159 to 160); J-MC 130 (120 to 130).
# - Alternating-cues task with delay (Figures 1, 4, 5). Right-hand fingers T, I, M, R, P and a
#   No-Go X, Spatial-Cue and Text-Cue variants interleaved. N, 120 trials per session over 4
#   sessions (480); J, 112 per session (96 to 120) over 3 sessions (336). N-PPC 118 neurons per
#   session (111 to 128); J-PPC 103 (92 to 116); J-MC 93 (90 to 95). The legends correct for 466,
#   308 and 278 neurons pooled.
# - Reaction-time task with randomized cue location (Figure 2, 6). 3 x 4 letter grid, 48 trials per
#   run-block, decoded finger shown 1.5 s after the cue. Online BMI, N 4016 trials over 9 sessions
#   (previously reported in ref 46), J 1488 trials over 8 sessions (right hand), J 336 trials over
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/000252/*.yaml; sed -n 80,103p $f; sed -n 625,700p $f; grep -n -i "fig8e-finger\|O9" $f | head; git log --oneline -3 -- questions/000252.yaml
```

```
#   (ref 60). The paper says only "linear decoders".
# - O8 Within-condition (standard) finger-type accuracy that bounds finger-type CCGP. (a) a 5-class
#   finger decoder trained and tested within each hand by stratified 8-fold cross-validation,
#   averaged over hands (the "within-hand accuracy" of Results, last paragraph); (b) a 5-class
#   finger-type decoder over the trials of both hands, cross-validated the same way.
# - O9 "Close to" standard accuracy (Figure 8e). The paper prints no margin. (a) CCGP at least 0.9
#   of the standard accuracy; (b) the CCGP to accuracy ratio above that of J-PPC finger-type, which
#   the paper calls much lower (36% against 65%, ratio 0.55).
# - O10 Features of the retrospective single-array BMI decoder. (a) threshold crossing rates per
#   electrode in [0.5, 1.5] s after the cue, as online; (b) sorted neurons in the same window.
# - O11 Analysis window of the ten-finger analyses (selectivity, decoding, distances, CCGP). The
#   Results and legends of Figures 7 and 8 do not name it. The Go window is used, as the Feature
#   Extraction default for movement execution and as the Results compare these results with the
#   contralateral-only movement-period results ("Similar to the contralateral-only results"). No
#   other reading is supported by the text.
#
# Tolerances. 10% of each reported value, except where the paper gives a confidence interval or a
# spread, as each claim says.
schema_version: 2
dataset:
[... 30 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000252-guan-2022-01.md",
 "content": "# 000252, Guan et al. 2022\n\nNine claims reproduced (one on an assumption), one partially (on an\nassumption), one not reproduced and eight blocked, all eight for missing data.\nAll 19 claims are on the dandiset. The first verification round agreed with all\n19 outcomes and the second with all 19; nothing was proposed after the second,\nso there was no third round. It pins version 0.230408.2207, the only published\nversion, with the draft listing the same assets. The paper, Guan et al.,\n\"Compositional coding of individual finger movements in human posterior\nparietal cortex and motor cortex enables ten-finger decoding\", a bioRxiv\npreprint, records sorted single neurons from Utah arrays in two tetraplegic\nparticipants, N (one array in left PPC, N-PPC) and J (J-PPC and J-MC), during\nattempted finger presses of both hands, with an alternating-cues task and\nonline BMI sessions besides; the dandiset holds 12 NWB files of the ten-finger\npress task, 10 sessions of N and 2 of J with 100 trials each. The claims were\nwritten from version 1 of the preprint as bioRxiv JATS XML, without a PDF; the\npaper links no code and names rsatoolbox and DABEST. The check made eight\nchanges, among them a new reading O11 that fixes the Go window for the\nten-finger analyses, and left three points open. The ten-finger claims could be\ntested and the alternating-cues and BMI claims could not. Reproduced are\n`tenfinger-recording-counts` and `tenfinger-pooled-npcc-neurons` (1114 N-PPC\nunits, paper 1111), both on the counts before the 0.5 Hz exclusion, which the\nMethods apply to all analyses (943 and 930 after it, outside tolerance);\n`tenfinger-decoding-accuracy` (72.2%, 69.5% and 78.5% for N-PPC, J-PPC and\nJ-MC under O1 (a) and O2 (a), chance 10%); `tenfinger-error-structure` (76.6%,\n72.1% and 62.8% of errors adjacent or matching); `fig8a-npcc-index-distinct`\nin all 18 readings; `fig8e-hand-ccgp` and `fig8e-finger-ccgp` (p = 1/1002, the\nlatter through O9 (b), as J-MC fails the 0.9 margin of O9 (a));\n`figs11-jppc-lower-matched-size` (J-PPC 0.253 to 0.338 against at least 0.472);\nand `fig8b-matching-closer` (N-PPC 1.42, J-MC 3.06, J-PPC 0.22 with its CI\nincluding 0) on the assumption that the noise passed to rsatoolbox is the\nprecision of each partition mean, without which the values are about a fifth\nas large and the claim would be partial. `jppc-finger-ccgp-low` is partial on\nthe assumption that the standard accuracy is computed on the same\npseudo-population as CCGP: J-PPC finger CCGP is 0.290 to 0.380, p is below\n0.001 in only one of eight readings, and there the within-hand accuracy (0.850)\nis outside the tolerance of 65%; with the per-session accuracy (0.680 to 0.690)\nthe same reading is reproduced. `tenfinger-discriminative-fraction` is not\nreproduced: under O1 (a) 47.8%, 38.1% and 65.1% of neurons are discriminative\nagainst the paper's 66%, 57% and 78%, uncorrected p gives at most 56.1%, 46.5%\nand 68.8%, and only a 1 s window from the Go cue (60.8%, 56.8% and 82.9%), a\nvariant outside O11, comes within tolerance. The five alternating-cues claims\nand the three BMI claims are blocked for missing data. The author's first run\ngave the same outcomes, with the same two assumptions. The author asked no\nquestions of a reader, so the answer and author-answers runs changed nothing.\nRound 1 found that the fig8b magnitude rests on the x5 scaling (5.46 times the\ntrue value on synthetic data), that the per-session standard accuracy of\n`jppc-finger-ccgp-low` had been run for one reading only, that the J-PPC p\nvalue is fragile, that the O6 (b) null is conservative, that figs11 ran only O1\n(a), that the window of the discriminative fraction was not swept and that\nDANDI:000147 was not examined; in reply a synthetic check of the scale and the\nRDM ranges were added, the per-session accuracy and the null counts were\nprinted for every reading, the window was swept, figs11 was run under O1 (b)\nand DANDI:000147 was checked, while the O6 (b) null was left as a deviation, as\nfixing it would take about 100 times as long. Round 2 found that calling the\npseudo-population the better-supported choice is a judgement call, that the\nclaims file corrects J's two arrays separately where the Methods correct over\neach participant's neurons, and sentences the outputs did not support (a\nshuffled-label range of 0.07 to 0.17 where the outputs give 0.04 to 0.17,\n\"FDR per session gives no more\" where it gives up to 0.3 points more, a run\ntime of fourteen minutes, an RDM range from 0.00 and the contents of\nDANDI:000147, printed by no cell); in reply the text was corrected, a cell\nprinting DANDI:000147 was added and the correction question went to a reader in\n`questions/000252.yaml`. The author's session ran from 12:02 to 12:29 UTC; a\nsingular noise matrix and a sortedness check that read the wrong array were\nfixed during development. The notebook ran in about 6.8 minutes at first, 416 s\nafter the author-answers run and 661 s at the end, and the executed copy was\nbuilt before the last markdown-only edits. The untracked files in the\nrepository root were left alone.\n\nThe dandiset holds only the ten-finger press task: the alternating-cues task\n(Figures 1, 4 and 5, Supplementary Figures 2 to 5) and J's online BMI sessions\n(Figure 6b, Supplementary Figures 6 and 7) are not in it, though the paper's\nData Availability names only this dandiset, and the trial table has no decoder\noutput. Its metadata say it continues DANDI:000147, which holds 10 files of\nsubject P1 from 2018 with a BCI finger-press task and appears to hold N's BMI\nsessions of ref 46, but no alternating-cues task and nothing of J. In 1509 of\n1692 units the spike times are not stored in increasing time order, which NWB\nexpects. The files name the participants P1 (the paper's N) and N1 (the\npaper's J) with no mapping to the paper's labels, so N1 is not participant N\nand the mapping follows only from the sex and electrode locations. The trial\ncolumns Run, TrialNumber, cue_on_time, cue_off_time and go_on_time have no\ndescription, and the Delay screen onset is implied only by cue_off_time. The\npaper's per-session unit counts match the units before the 0.5 Hz exclusion,\nand the J-MC session of 2019-02-12 has 139 units against the paper's stated\nmaximum of 130. Questions are put to the paper's authors: how the noise\nprecision was passed to rsatoolbox for the cross-validated Mahalanobis\ndistance; whether the standard accuracy compared with CCGP was computed on the\npseudo-population or per session; what the 1001 label shuffles permuted and\nhow trials of different sessions were matched; and which window, exclusion and\ncorrection gave the discriminative fractions.\n\nThe author's points on the protocol: the claims file's readings O3 and O4 did\nnot cover how the toolbox is called, which changes values about fivefold, so a\nreading from the toolbox's documentation was adopted as an assumption with the\nunscaled result as a variant; criteria that count a claim reproduced under one\nreading made fig8e-finger reproduced though O9 (a) fails and jppc partial\nthrough one reading of eight; step 1.4 does not say whether to look at a\nrelated dandiset the claims file does not name, such as 000147, so only its\nmetadata were read and the claims kept as data_missing; and there is no rule\nfor a pseudo-population null over random pairings, so each shuffle drew a new\nmatching, recorded as a deviation.\n"
}
```

```
File created successfully at: docs/pilot-notes/000252-guan-2022-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -c -e "—" -e "rather" -e "\*\*" docs/pilot-notes/000252-guan-2022-01.md
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
?? docs/pilot-notes/000252-guan-2022-01.md
?? scripts
0
```

**Agent**

I've written the notes in `docs/pilot-notes/000252-guan-2022-01.md` and changed no other file. The `catalystneuro` field for this dataset is empty, so the second paragraph does not open with the CatalystNeuro sentence. The sources give only "Guan et al." and no full author list, so the heading and the text use that. Nothing is committed. This is the text:

# 000252, Guan et al. 2022

Nine claims reproduced (one on an assumption), one partially (on an assumption), one not reproduced and eight blocked, all eight for missing data. All 19 claims are on the dandiset. The first verification round agreed with all 19 outcomes and the second with all 19; nothing was proposed after the second, so there was no third round. It pins version 0.230408.2207, the only published version, with the draft listing the same assets. The paper, Guan et al., "Compositional coding of individual finger movements in human posterior parietal cortex and motor cortex enables ten-finger decoding", a bioRxiv preprint, records sorted single neurons from Utah arrays in two tetraplegic participants, N (one array in left PPC, N-PPC) and J (J-PPC and J-MC), during attempted finger presses of both hands, with an alternating-cues task and online BMI sessions besides; the dandiset holds 12 NWB files of the ten-finger press task, 10 sessions of N and 2 of J with 100 trials each. The claims were written from version 1 of the preprint as bioRxiv JATS XML, without a PDF; the paper links no code and names rsatoolbox and DABEST. The check made eight changes, among them a new reading O11 that fixes the Go window for the ten-finger analyses, and left three points open. The ten-finger claims could be tested and the alternating-cues and BMI claims could not. Reproduced are `tenfinger-recording-counts` and `tenfinger-pooled-npcc-neurons` (1114 N-PPC units, paper 1111), both on the counts before the 0.5 Hz exclusion, which the Methods apply to all analyses (943 and 930 after it, outside tolerance); `tenfinger-decoding-accuracy` (72.2%, 69.5% and 78.5% for N-PPC, J-PPC and J-MC under O1 (a) and O2 (a), chance 10%); `tenfinger-error-structure` (76.6%, 72.1% and 62.8% of errors adjacent or matching); `fig8a-npcc-index-distinct` in all 18 readings; `fig8e-hand-ccgp` and `fig8e-finger-ccgp` (p = 1/1002, the latter through O9 (b), as J-MC fails the 0.9 margin of O9 (a)); `figs11-jppc-lower-matched-size` (J-PPC 0.253 to 0.338 against at least 0.472); and `fig8b-matching-closer` (N-PPC 1.42, J-MC 3.06, J-PPC 0.22 with its CI including 0) on the assumption that the noise passed to rsatoolbox is the precision of each partition mean, without which the values are about a fifth as large and the claim would be partial. `jppc-finger-ccgp-low` is partial on the assumption that the standard accuracy is computed on the same pseudo-population as CCGP: J-PPC finger CCGP is 0.290 to 0.380, p is below 0.001 in only one of eight readings, and there the within-hand accuracy (0.850) is outside the tolerance of 65%; with the per-session accuracy (0.680 to 0.690) the same reading is reproduced. `tenfinger-discriminative-fraction` is not reproduced: under O1 (a) 47.8%, 38.1% and 65.1% of neurons are discriminative against the paper's 66%, 57% and 78%, uncorrected p gives at most 56.1%, 46.5% and 68.8%, and only a 1 s window from the Go cue (60.8%, 56.8% and 82.9%), a variant outside O11, comes within tolerance. The five alternating-cues claims and the three BMI claims are blocked for missing data. The author's first run gave the same outcomes, with the same two assumptions. The author asked no questions of a reader, so the answer and author-answers runs changed nothing. Round 1 found that the fig8b magnitude rests on the x5 scaling (5.46 times the true value on synthetic data), that the per-session standard accuracy of `jppc-finger-ccgp-low` had been run for one reading only, that the J-PPC p value is fragile, that the O6 (b) null is conservative, that figs11 ran only O1 (a), that the window of the discriminative fraction was not swept and that DANDI:000147 was not examined; in reply a synthetic check of the scale and the RDM ranges were added, the per-session accuracy and the null counts were printed for every reading, the window was swept, figs11 was run under O1 (b) and DANDI:000147 was checked, while the O6 (b) null was left as a deviation, as fixing it would take about 100 times as long. Round 2 found that calling the pseudo-population the better-supported choice is a judgement call, that the claims file corrects J's two arrays separately where the Methods correct over each participant's neurons, and sentences the outputs did not support (a shuffled-label range of 0.07 to 0.17 where the outputs give 0.04 to 0.17, "FDR per session gives no more" where it gives up to 0.3 points more, a run time of fourteen minutes, an RDM range from 0.00 and the contents of DANDI:000147, printed by no cell); in reply the text was corrected, a cell printing DANDI:000147 was added and the correction question went to a reader in `questions/000252.yaml`. The author's session ran from 12:02 to 12:29 UTC; a singular noise matrix and a sortedness check that read the wrong array were fixed during development. The notebook ran in about 6.8 minutes at first, 416 s after the author-answers run and 661 s at the end, and the executed copy was built before the last markdown-only edits. The untracked files in the repository root were left alone.

The dandiset holds only the ten-finger press task: the alternating-cues task (Figures 1, 4 and 5, Supplementary Figures 2 to 5) and J's online BMI sessions (Figure 6b, Supplementary Figures 6 and 7) are not in it, though the paper's Data Availability names only this dandiset, and the trial table has no decoder output. Its metadata say it continues DANDI:000147, which holds 10 files of subject P1 from 2018 with a BCI finger-press task and appears to hold N's BMI sessions of ref 46, but no alternating-cues task and nothing of J. In 1509 of 1692 units the spike times are not stored in increasing time order, which NWB expects. The files name the participants P1 (the paper's N) and N1 (the paper's J) with no mapping to the paper's labels, so N1 is not participant N and the mapping follows only from the sex and electrode locations. The trial columns Run, TrialNumber, cue_on_time, cue_off_time and go_on_time have no description, and the Delay screen onset is implied only by cue_off_time. The paper's per-session unit counts match the units before the 0.5 Hz exclusion, and the J-MC session of 2019-02-12 has 139 units against the paper's stated maximum of 130. Questions are put to the paper's authors: how the noise precision was passed to rsatoolbox for the cross-validated Mahalanobis distance; whether the standard accuracy compared with CCGP was computed on the pseudo-population or per session; what the 1001 label shuffles permuted and how trials of different sessions were matched; and which window, exclusion and correction gave the discriminative fractions.

The author's points on the protocol: the claims file's readings O3 and O4 did not cover how the toolbox is called, which changes values about fivefold, so a reading from the toolbox's documentation was adopted as an assumption with the unscaled result as a variant; criteria that count a claim reproduced under one reading made fig8e-finger reproduced though O9 (a) fails and jppc partial through one reading of eight; step 1.4 does not say whether to look at a related dandiset the claims file does not name, such as 000147, so only its metadata were read and the claims kept as data_missing; and there is no rule for a pseudo-population null over random pairings, so each shuffle drew a new matching, recorded as a deviation.

## End of run

13 turns, 2 minutes, $0.90 at API prices, result: success.
