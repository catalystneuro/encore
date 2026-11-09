# 000945 · recorder · run 41251506079

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/000945/ claims/000945/; python tools/readme_row.py 000945; cat attempts/000945-ramachandran-2025-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for e in (it if isinstance(it,list) else it.values()):
  if '000945' in json.dumps(e)[:300]: print(json.dumps(e,indent=1))
"
```

```
<persisted-output>
Output too large (46.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7e2db9f8-eb03-4e61-acb5-d7116e647ad2/tool-results/b1r3k0osi.txt

Preview (first 2KB):
docs/pilot-notes/000774-hickman-2026-01.md
docs/pilot-notes/000689-li-2022-01.md
docs/pilot-notes/000943-clark-2024-01.md
docs/pilot-notes/000875-pakhomov-2023-01.md
docs/pilot-notes/000688-perich-2018-01.md
claims/000945/:
10.1088-1741-2552-adbb1f.yaml

transcripts/000945/:
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
cd  f=/home/runner/.claude/projects/-home-runner-work-encore-encore/7e2db9f8-eb03-4e61-acb5-d7116e647ad2/tool-results/b1r3k0osi.txt; sed -n 30,400p $f; for n in docs/pilot-notes/000774-hickman-2026-01.md docs/pilot-notes/000689-li-2022-01.md docs/pilot-notes/000943-clark-2024-01.md docs/pilot-notes/000875-pakhomov-2023-01.md docs/pilot-notes/000688-perich-2018-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "== $n"; cat $n; done
```

```
<persisted-output>
Output too large (63.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7e2db9f8-eb03-4e61-acb5-d7116e647ad2/tool-results/bvbsv3ofi.txt

Preview (first 2KB):
verifier-3-report.md
verifier-3.md
| [000945](https://dandiarchive.org/dandiset/000945) | [Ramachandran et al. 2025](https://doi.org/10.1088/1741-2552/adbb1f) | 1 | 1 | 11 | 9 | [`000945-ramachandran-2025`](entries/000945-ramachandran-2025) |
schema_version: 2
id: 000945-ramachandran-2025-01
dataset:
  archive: dandi
  id: "000945"
  version: 0.250213.2212
  doi: 10.48324/dandi.000945/0.250213.2212
paper: doi:10.1088/1741-2552/adbb1f
date: 2026-10-31
entry: 000945-ramachandran-2025
provenance:
  kind: agent
  accountable:
[... 31 more lines not kept]
```

**Agent**

Output is large; I'll read files directly.

**Agent calls Read**

```json
{
 "file_path": "attempts/000945-ramachandran-2025-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000945-ramachandran-2025-01
3	dataset:
4	  archive: dandi
5	  id: "000945"
6	  version: 0.250213.2212
7	  doi: 10.48324/dandi.000945/0.250213.2212
8	paper: doi:10.1088/1741-2552/adbb1f
9	date: 2026-10-31
10	entry: 000945-ramachandran-2025
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
[... 739 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for n in docs/pilot-notes/000774-hickman-2026-01.md docs/pilot-notes/000689-li-2022-01.md docs/pilot-notes/000943-clark-2024-01.md docs/pilot-notes/000875-pakhomov-2023-01.md docs/pilot-notes/000688-perich-2018-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "== $n"; cat $n; done; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for e in (it if isinstance(it,list) else it.values()):
  if '000945' in json.dumps(e)[:300]: print(json.dumps(e,indent=1))
"
```

```
<persisted-output>
Output too large (40.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7e2db9f8-eb03-4e61-acb5-d7116e647ad2/tool-results/bhl70gex8.txt

Preview (first 2KB):
== docs/pilot-notes/000774-hickman-2026-01.md
# 000774, Hickman et al. 2026

Eleven claims reproduced, three partially, seven not reproduced and 21
blocked. The first verification round agreed with 40 of the 42 outcomes and
the second with 38, and a third round, held on the four changes of outcome
proposed after the second, agreed with all four. It pins version
0.260520.1753, the version the paper cites and the only published version.
The paper, Hickman, Hughes, Sahai, Miles and Denman in Cell Reports, records
units in nine awake, head-fixed mice with three Neuropixels 1.0 probes
inserted around a 16-channel stimulating electrode in layer 5 of left V1,
gives single biphasic pulses of 5, 25, 50 and 100 uA, cathodal, anodal or
bipolar, and relates the evoked potential, direct responses, FS and RS
classes, the modulation of the wider circuit and its dimensionality to
amplitude and distance; four further mice with chronic electrodes learn to
detect the pulses in a lick task. The claims were written from the NIH author
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7e2db9f8-eb03-4e61-acb5-d7116e647ad2/tool-results/bhl70gex8.txt"
}
```

```
1	== docs/pilot-notes/000774-hickman-2026-01.md
2	# 000774, Hickman et al. 2026
3	
4	Eleven claims reproduced, three partially, seven not reproduced and 21
5	blocked. The first verification round agreed with 40 of the 42 outcomes and
6	the second with 38, and a third round, held on the four changes of outcome
7	proposed after the second, agreed with all four. It pins version
8	0.260520.1753, the version the paper cites and the only published version.
9	The paper, Hickman, Hughes, Sahai, Miles and Denman in Cell Reports, records
10	units in nine awake, head-fixed mice with three Neuropixels 1.0 probes
11	inserted around a 16-channel stimulating electrode in layer 5 of left V1,
12	gives single biphasic pulses of 5, 25, 50 and 100 uA, cathodal, anodal or
13	bipolar, and relates the evoked potential, direct responses, FS and RS
14	classes, the modulation of the wider circuit and its dimensionality to
15	amplitude and distance; four further mice with chronic electrodes learn to
16	detect the pulses in a lick task. The claims were written from the NIH author
17	manuscript (PMC13404931) and Document S1, without Table S1, and from the
18	paper's code at commit c4aaa60. 21 claims were tested; the 11 evoked-potential
19	and saturation claims of Figures 1 to 3, S1 and S2 are blocked as
20	`data_missing`, as they rest on the raw AP band, and so are the 10 behaviour
[... 561 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c transcripts/000945/*-report.md claims/000945/*; ls -la --time-style=full-iso transcripts/000945/ | head -30; python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d))
it=d if isinstance(d,list) else list(d.values())
" ; grep -n '"000945"' -A25 targets/dandisets.json | head -40
```

```
545 transcripts/000945/answer-report.md
 2232 transcripts/000945/author-answers-report.md
 5581 transcripts/000945/author-report.md
 4003 transcripts/000945/author-revise-1-report.md
 2912 transcripts/000945/author-revise-2-report.md
 1446 transcripts/000945/author-revise-3-report.md
 2642 transcripts/000945/claims-check-report.md
 3867 transcripts/000945/claims-report.md
10322 transcripts/000945/verifier-1-report.md
 6739 transcripts/000945/verifier-2-report.md
 3294 transcripts/000945/verifier-3-report.md
34517 claims/000945/10.1088-1741-2552-adbb1f.yaml
78100 total
total 620
drwxr-xr-x   2 runner runner   4096 2026-10-31 23:12:20.831578126 +0000 .
drwxr-xr-x 233 runner runner   4096 2026-10-31 23:12:20.173571787 +0000 ..
-rw-r--r--   1 runner runner    545 2026-10-31 23:12:20.830075894 +0000 answer-report.md
-rw-r--r--   1 runner runner   4970 2026-10-31 23:12:20.830578116 +0000 answer.md
-rw-r--r--   1 runner runner   2232 2026-10-31 23:12:20.830578116 +0000 author-answers-report.md
-rw-r--r--   1 runner runner  10613 2026-10-31 23:12:20.830578116 +0000 author-answers.md
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000945; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md verifier-3-report.md author-revise-3-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (36.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7e2db9f8-eb03-4e61-acb5-d7116e647ad2/tool-results/bvov3ovoc.txt

Preview (first 2KB):
=== author-report.md
I've finished steps 1 to 6 for DANDI:000945. Of the 22 claims, 2 were reproduced, 2 partially reproduced, 15 not reproduced and 3 blocked. The entry passes `check` and its notebook runs clean in 60 s; the handover package is built. Nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| fig3-cell-type-sorting | partially reproduced: two recordings match 28 FSU / 32 RSU / 60 units using the dataset's own labels; the k-means sorting can't be checked (no waveforms) |
| fig4-rsu-time-locked-both-states | blocked, data_missing (no sham) |
| fig4hi-fsu-delayed-latency | not reproduced (p = 0.018 to 0.85; anesthetized mean 0.38 to 0.52 s against 0.24 ± 0.08) |
| fig4h-awake-latency-wider | not reproduced (awake spread is wider in only 10 of 16 readings, by at most 0.02 s) |
| fig5a-rsu-time-locked-prf-awake | not reproduced (peak at 3000 Hz, not 1500 Hz) |
| fig5c-rsu-time-locked-prf-anesth | not reproduced |
| rsu-time-locked-anesthesia-factor | not reproduced (p ≈ 0.011 to 0.018, and anesthesia raises the response) |
| fig5bd-fsu-time-locked-no-prf | not reproduced (FSU do differ across PRF) |
| fig5e, fig5f, fig5gh | not reproduced |
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7e2db9f8-eb03-4e61-acb5-d7116e647ad2/tool-results/bvov3ovoc.txt"
}
```

```
1	=== author-report.md
2	I've finished steps 1 to 6 for DANDI:000945. Of the 22 claims, 2 were reproduced, 2 partially reproduced, 15 not reproduced and 3 blocked. The entry passes `check` and its notebook runs clean in 60 s; the handover package is built. Nothing is committed.
3	
4	### 1. Outcomes
5	
6	| Claim | Outcome |
7	|---|---|
8	| fig3-cell-type-sorting | partially reproduced: two recordings match 28 FSU / 32 RSU / 60 units using the dataset's own labels; the k-means sorting can't be checked (no waveforms) |
9	| fig4-rsu-time-locked-both-states | blocked, data_missing (no sham) |
10	| fig4hi-fsu-delayed-latency | not reproduced (p = 0.018 to 0.85; anesthetized mean 0.38 to 0.52 s against 0.24 ± 0.08) |
11	| fig4h-awake-latency-wider | not reproduced (awake spread is wider in only 10 of 16 readings, by at most 0.02 s) |
12	| fig5a-rsu-time-locked-prf-awake | not reproduced (peak at 3000 Hz, not 1500 Hz) |
13	| fig5c-rsu-time-locked-prf-anesth | not reproduced |
14	| rsu-time-locked-anesthesia-factor | not reproduced (p ≈ 0.011 to 0.018, and anesthesia raises the response) |
15	| fig5bd-fsu-time-locked-no-prf | not reproduced (FSU do differ across PRF) |
16	| fig5e, fig5f, fig5gh | not reproduced |
17	| delayed-anesthesia-factor | reproduced, resting on assumption Rep2 |
18	| fig6ad-time-adjacent-batch | blocked, data_missing (second batch of rats absent) |
19	| fig6ef-rsu-ispta-rise-then-fall | partially reproduced, resting on assumption W2 |
20	| fig6fh, fig5a-1500-highest | not reproduced |
[... 277 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000945/10.1088-1741-2552-adbb1f.yaml",
 "limit": 80
}
```

```
1	# Claims for Ramachandran, Gao, Yttri, Yu & He (2025) on dandiset 000945.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol as stated in docs/protocol.md.
4	# Source: the version of record (J Neural Eng 22(2) 026022, PMC11920894), full text as served by
5	# Europe PMC: Abstract, Introduction, Methods, Results, figure legends and Discussion. No PDF was
6	# supplied. The supplementary materials (headpiece design, surgery, training, hydrophone scanning,
7	# supplementary figures 2 and 4, supplementary table 1 of ISPTA values) were not supplied. No
8	# claim rests on them: the analysis methods and the ISPTA of each PRF condition are given in the
9	# main text (Methods 2.3 to 2.6). The paper links no analysis code (it names "custom code" in
10	# MATLAB R2019a with FieldTrip), so no code was read.
11	#
12	# Data the paper used, as it reports them. Adult male Wistar rats, awake and head-fixed, with a
13	# chronic 32-channel micro-electrode array in S1; tFUS from a 128-element array (f0 1.5 MHz,
14	# 114 kPa peak-to-peak in situ at 15 V), ultrasound duration 67 ms, one trial every 2.5 s with
15	# 10% jitter, 505 trials per parameter set, the first 5 cut (500 used). TDT recordings at 24 kHz,
16	# bandpass 300 Hz to 5 kHz, units sorted in Offline Sorter. Batch 1 (10 rats): awake PRF series
17	# at 30, 300, 1500, 3000 and 4500 Hz with 200 us tone-burst duration (TBD), at about 7 months;
18	# the same PRF series under isoflurane at 9 months; awake DC series at 1500 Hz with TBD 40, 200
19	# and 400 us (DC 6, 30 and 60%) at 10 months. Batch 2 (5 rats, 7 months): awake and anesthetized
20	# recordings at a low PRF and 1500 Hz with 200 us TBD, and a sham at 1500 Hz aimed off target at
[... 60 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000945-ramachandran-2025-01.md",
 "content": "# 000945, Ramachandran et al. 2025\n\nOne claim reproduced, one partially, 11 not reproduced and nine blocked. The\nfirst verification round agreed with 17 of the 22 outcomes and the second\nwith 20, and a third round, held on the two changes of outcome proposed after\nthe second, agreed with both. It pins version 0.250213.2212, the version the\npaper cites; all five published versions hold the same 75 files. The paper,\nRamachandran, Gao, Yttri, Yu and He in the Journal of Neural Engineering,\nrecords sorted units in S1 of awake, head-fixed rats with a chronic\n32-channel array during transcranial focused ultrasound, sorts them into\nregular spiking (RSU) and fast spiking (FSU) units by k-means on two waveform\ndurations, and compares time-locked and delayed responses across pulse\nrepetition frequency (PRF), duty cycle (DC) and isoflurane anesthesia, with a\nsham aimed off target. The claims were written from the version of record in\nEurope PMC (PMC11920894), without the supplementary materials, and the paper\nlinks no code. 13 claims were tested on the dataset's own cell-type labels;\n`fig3-cell-type-sorting`, `fig4-rsu-time-locked-both-states`,\n`fig5e-rsu-delayed-prf-awake`, `fig6ad-time-adjacent-batch`,\n`fig7a-rsu-time-locked-dc` and `fig7c-rsu-delayed-dc` are blocked as\n`data_missing`, for want of waveforms, the sham, the second batch of rats or\nthe DC series' own 30% recordings, and `fig4h-awake-latency-wider`,\n`fig6ef-rsu-ispta-rise-then-fall` and `sham-no-auditory-response` as\n`methods_underspecified`, the first two because the claims file's readings\ndisagree. `delayed-anesthesia-factor` reproduces on an assumption of one\nrecording per rat and condition, the anesthetized mean being lower for RSU (p\n= 4.2e-09 to 1.8e-08) and FSU (p = 0.0012 to 0.0015); with every recording\nFSU gives p = 0.038 to 0.041 and the claim is partial at best.\n`fig7d-fsu-delayed-dc` is partial, 60% being above 6% (corrected p = 0.015)\nwith both below baseline (99.6% and 98.2%) and the sham part untested. Among\nthe not reproduced, the highest time-locked RSU mean is at 3000 Hz (107.7 to\n108.7%), not 1500 Hz (98.1 to 98.7%); anesthesia raises the time-locked RSU\nresponse (102.6 to 102.9% against 100.1 to 100.4%), and with only BH498 and\nBH512 the effect disappears (p = 0.425); FSU time-locked responses differ\nacross PRF (Kruskal-Wallis p = 1.8e-12 awake, 5.5e-04 anesthetized); no\nreading gives awake FSU latencies later at p < 0.001 (p 0.018 to 0.92); and\nat 6% DC the time-locked RSU mean (176.3 to 180.8%) is above that at 60%\n(147.1 to 147.5%). The author's first run gave 2 reproduced, 2 partially, 15\nnot reproduced and 3 blocked. The author asked a reader no questions, so the\nanswer run and the following author run changed nothing. Round 1 disagreed\nwith fig3, which it gave as blocked since both outcomes of its criterion need\nthe waveform clusters, with fig4h and fig6ef, where the notebook had adopted\none reading against the claims file's rule for disagreeing readings, with\nfig7c, decided by substitute 30% recordings, and with fig7d, reproduced with\nan untested sham part; it also found that the recording dates of the repeat\nrecordings were never printed and that most anesthetized tests rest on two\nrats. In reply the dates were printed, which showed three of the ten `_2`\nrecordings to start before their pair, a reading keeping the earliest of each\npair (Rep3) and one with no 30% group (C0) were added, and fig3 was given a\nbase rate. Round 2 disagreed with fig5e and fig7a, which could still be\npartial if the untested sham or 30% parts held, and found sentences the\noutputs did not support (twelve second copies where there are eleven, spike\ncounts said to match in every pair, and substitute dates true only of the\nsame rats' recordings), which were corrected; the author added the Rep1\nresult without the doubly filed recording (FSU p = 0.048 to 0.052) but kept\nit as partial, as the RSU part holds alone. The author proposed blocked for\nthe two, and round 3 agreed. The author's run took about 23 minutes (21:25 to\n21:48 UTC) and nothing failed; the helper was later fixed to decode start\ntimes stored as arrays in the unlabelled anesthetized files. The notebook ran\nin 60 s at first, 64 s after the answer, 92 s after round 1, about 90 s after\nround 2 and 56 s in the last run.\n\nThe sham condition and the second batch of five rats are not in the\ndandiset, and only part of the first batch is: the awake PRF series covers\nseven rats, the anesthetized PRF series three (BH498 at five PRFs, BH512\nwithout 30 Hz, BH521 at three PRFs, unlabelled) and the awake DC series three\nrats at 6% and 60% only, where the paper describes ten rats for each series.\nThe DC series' own 30% recordings are missing; the only 1500 Hz, 200 us\nrecordings are the PRF series', those of the same rats made three to five\nmonths earlier and those of the other rats from August 2023 to 6 March 2024.\nThe files hold no waveforms, voltage traces or electrode positions, so the\ncell-type sorting cannot be repeated or checked; with the deposited labels\ntwo of 59 recordings match the paper's counts, against 3.84 expected by\nchance, and FSU have the higher median baseline rate in 46 of 59 labelled\nrecordings. The labelled anesthetized units come from two rats, so state and\nPRF effects there are partly rat effects. Eleven files are second copies of\nother recordings: the five anesthetized BH498 recordings are deposited under\nBH498 without labels and under subject folder BH497 with labels, four\nanesthetized BH512 recordings under BH512 without labels and under BH514\nwith labels, BH512_1500_200_anes2 is a third copy sorted differently and\ndated two months later (spike counts 905,554 against 926,883), and\nBH498_30_200 and BH508_30_200_2 share all 203 trial times and 18,860 spike\ntimes, with session start times 6.5 hours apart, so which rat that recording\nbelongs to cannot be established. The description says the repeat\nrecordings were \"taken a few months after the original ones\", but three of\nthe ten `_2` recordings start before their unsuffixed pair. The labelled\ncopies of anesthetized recordings are described as \"Awake S1 Stimulation by\ntFUS\", every file gives the age P24W where the paper gives 7, 9 and 10 months\nand the description 8 to 10 and 12 months, and electrode columns carry\nplaceholders (\"my description\", \"brain area\"). PRF, tone-burst duration and\nanesthesia state are coded only in the identifier, the trial table's\nstop_time (always 2.2 s after start_time) is not described, and the files do\nnot say which 500 of the 505 trials delivered they hold. Fifteen anesthetized\nfiles have no cell-type labels, among them all of BH521's and BH512's DC\nrecordings, and five recordings hold fewer than 500 trials (203, 238, 328 and\n339). Only 10 of 64 recordings show a population rise in the 67 ms\ntime-locked window. Questions are put to the paper's authors: whether the\nrepeat recordings were part of the analysis, and if not which of each pair\nwas; whether a window off the 35.7 ms bin edges was measured from exact spike\ntimes or from the overlapping bins; and whether the first latency bin allowed\nafter the 67 ms of ultrasound is the first starting at or after 67 ms or the\nfirst ending after it.\n\nThe author's points on the protocol: fig3's criterion has no branch for\ncounts that match while the feature part cannot be tested, and blocking it\nwould block every claim that uses cell types by the dependency rule, so the\nfirst run gave it as partial; the claims file's header covers a missing\nanesthetized sham but not the awake one, and the same rule was applied as a\ndeviation; step 1.6 covers readings for gaps in the paper but not choices the\ndataset forces, such as the repeats and the missing 30% recordings, and every\nreading was run with one adopted as an assumption; fig4h's criterion asks for\nevery reading while step 1.6 says to adopt the best-supported one, and the\ncriterion was followed; and nothing covers recordings with fewer trials than\nthe paper describes, which were used as they are with a finding.\n"
}
```

```
File created successfully at: docs/pilot-notes/000945-ramachandran-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  sed -i 's/that most anesthetized tests rest on two/that the anesthetized cell-type tests rest on two/' docs/pilot-notes/000945-ramachandran-2025-01.md; grep -nE '—|rather|\*\*' docs/pilot-notes/000945-ramachandran-2025-01.md; git status --short
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
?? docs/pilot-notes/000945-ramachandran-2025-01.md
?? scripts
```

**Agent**

I wrote the notes to `docs/pilot-notes/000945-ramachandran-2025-01.md` and changed no other file. Nothing is committed. `git status` also lists some untracked files I didn't create (`.bashrc`, `.idea`, `scripts` and others); I left them alone.

# 000945, Ramachandran et al. 2025

One claim reproduced, one partially, 11 not reproduced and nine blocked. The
first verification round agreed with 17 of the 22 outcomes and the second
with 20, and a third round, held on the two changes of outcome proposed after
the second, agreed with both. It pins version 0.250213.2212, the version the
paper cites; all five published versions hold the same 75 files. The paper,
Ramachandran, Gao, Yttri, Yu and He in the Journal of Neural Engineering,
records sorted units in S1 of awake, head-fixed rats with a chronic
32-channel array during transcranial focused ultrasound, sorts them into
regular spiking (RSU) and fast spiking (FSU) units by k-means on two waveform
durations, and compares time-locked and delayed responses across pulse
repetition frequency (PRF), duty cycle (DC) and isoflurane anesthesia, with a
sham aimed off target. The claims were written from the version of record in
Europe PMC (PMC11920894), without the supplementary materials, and the paper
links no code. 13 claims were tested on the dataset's own cell-type labels;
`fig3-cell-type-sorting`, `fig4-rsu-time-locked-both-states`,
`fig5e-rsu-delayed-prf-awake`, `fig6ad-time-adjacent-batch`,
`fig7a-rsu-time-locked-dc` and `fig7c-rsu-delayed-dc` are blocked as
`data_missing`, for want of waveforms, the sham, the second batch of rats or
the DC series' own 30% recordings, and `fig4h-awake-latency-wider`,
`fig6ef-rsu-ispta-rise-then-fall` and `sham-no-auditory-response` as
`methods_underspecified`, the first two because the claims file's readings
disagree. `delayed-anesthesia-factor` reproduces on an assumption of one
recording per rat and condition, the anesthetized mean being lower for RSU (p
= 4.2e-09 to 1.8e-08) and FSU (p = 0.0012 to 0.0015); with every recording
FSU gives p = 0.038 to 0.041 and the claim is partial at best.
`fig7d-fsu-delayed-dc` is partial, 60% being above 6% (corrected p = 0.015)
with both below baseline (99.6% and 98.2%) and the sham part untested. Among
the not reproduced, the highest time-locked RSU mean is at 3000 Hz (107.7 to
108.7%), not 1500 Hz (98.1 to 98.7%); anesthesia raises the time-locked RSU
response (102.6 to 102.9% against 100.1 to 100.4%), and with only BH498 and
BH512 the effect disappears (p = 0.425); FSU time-locked responses differ
across PRF (Kruskal-Wallis p = 1.8e-12 awake, 5.5e-04 anesthetized); no
reading gives awake FSU latencies later at p < 0.001 (p 0.018 to 0.92); and
at 6% DC the time-locked RSU mean (176.3 to 180.8%) is above that at 60%
(147.1 to 147.5%). The author's first run gave 2 reproduced, 2 partially, 15
not reproduced and 3 blocked. The author asked a reader no questions, so the
answer run and the following author run changed nothing. Round 1 disagreed
with fig3, which it gave as blocked since both outcomes of its criterion need
the waveform clusters, with fig4h and fig6ef, where the notebook had adopted
one reading against the claims file's rule for disagreeing readings, with
fig7c, decided by substitute 30% recordings, and with fig7d, reproduced with
an untested sham part; it also found that the recording dates of the repeat
recordings were never printed and that the anesthetized cell-type tests rest on two
rats. In reply the dates were printed, which showed three of the ten `_2`
recordings to start before their pair, a reading keeping the earliest of each
pair (Rep3) and one with no 30% group (C0) were added, and fig3 was given a
base rate. Round 2 disagreed with fig5e and fig7a, which could still be
partial if the untested sham or 30% parts held, and found sentences the
outputs did not support (twelve second copies where there are eleven, spike
counts said to match in every pair, and substitute dates true only of the
same rats' recordings), which were corrected; the author added the Rep1
result without the doubly filed recording (FSU p = 0.048 to 0.052) but kept
it as partial, as the RSU part holds alone. The author proposed blocked for
the two, and round 3 agreed. The author's run took about 23 minutes (21:25 to
21:48 UTC) and nothing failed; the helper was later fixed to decode start
times stored as arrays in the unlabelled anesthetized files. The notebook ran
in 60 s at first, 64 s after the answer, 92 s after round 1, about 90 s after
round 2 and 56 s in the last run.

The sham condition and the second batch of five rats are not in the
dandiset, and only part of the first batch is: the awake PRF series covers
seven rats, the anesthetized PRF series three (BH498 at five PRFs, BH512
without 30 Hz, BH521 at three PRFs, unlabelled) and the awake DC series three
rats at 6% and 60% only, where the paper describes ten rats for each series.
The DC series' own 30% recordings are missing; the only 1500 Hz, 200 us
recordings are the PRF series', those of the same rats made three to five
months earlier and those of the other rats from August 2023 to 6 March 2024.
The files hold no waveforms, voltage traces or electrode positions, so the
cell-type sorting cannot be repeated or checked; with the deposited labels
two of 59 recordings match the paper's counts, against 3.84 expected by
chance, and FSU have the higher median baseline rate in 46 of 59 labelled
recordings. The labelled anesthetized units come from two rats, so state and
PRF effects there are partly rat effects. Eleven files are second copies of
other recordings: the five anesthetized BH498 recordings are deposited under
BH498 without labels and under subject folder BH497 with labels, four
anesthetized BH512 recordings under BH512 without labels and under BH514
with labels, BH512_1500_200_anes2 is a third copy sorted differently and
dated two months later (spike counts 905,554 against 926,883), and
BH498_30_200 and BH508_30_200_2 share all 203 trial times and 18,860 spike
times, with session start times 6.5 hours apart, so which rat that recording
belongs to cannot be established. The description says the repeat
recordings were "taken a few months after the original ones", but three of
the ten `_2` recordings start before their unsuffixed pair. The labelled
copies of anesthetized recordings are described as "Awake S1 Stimulation by
tFUS", every file gives the age P24W where the paper gives 7, 9 and 10 months
and the description 8 to 10 and 12 months, and electrode columns carry
placeholders ("my description", "brain area"). PRF, tone-burst duration and
anesthesia state are coded only in the identifier, the trial table's
stop_time (always 2.2 s after start_time) is not described, and the files do
not say which 500 of the 505 trials delivered they hold. Fifteen anesthetized
files have no cell-type labels, among them all of BH521's and BH512's DC
recordings, and five recordings hold fewer than 500 trials (203, 238, 328 and
339). Only 10 of 64 recordings show a population rise in the 67 ms
time-locked window. Questions are put to the paper's authors: whether the
repeat recordings were part of the analysis, and if not which of each pair
was; whether a window off the 35.7 ms bin edges was measured from exact spike
times or from the overlapping bins; and whether the first latency bin allowed
after the 67 ms of ultrasound is the first starting at or after 67 ms or the
first ending after it.

The author's points on the protocol: fig3's criterion has no branch for
counts that match while the feature part cannot be tested, and blocking it
would block every claim that uses cell types by the dependency rule, so the
first run gave it as partial; the claims file's header covers a missing
anesthetized sham but not the awake one, and the same rule was applied as a
deviation; step 1.6 covers readings for gaps in the paper but not choices the
dataset forces, such as the repeats and the missing 30% recordings, and every
reading was run with one adopted as an assumption; fig4h's criterion asks for
every reading while step 1.6 says to adopt the best-supported one, and the
criterion was followed; and nothing covers recordings with fewer trials than
the paper describes, which were used as they are with a finding.

## End of run

12 turns, 2 minutes, result: success.
