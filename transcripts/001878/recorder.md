# 001878 · recorder · run 39227289455

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001878 --write; git diff; ls transcripts/001878/ claims/001878/; cat attempts/001878-sun-2021-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '001878' in json.dumps(x)];print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (214.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/92a314c0-b9a0-481d-a540-f3e8f0d898e7/tool-results/bojyrcbc5.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 91ca402..a84626c 100644
--- a/README.md
+++ b/README.md
@@ -100,6 +100,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001550](https://dandiarchive.org/dandiset/001550) | [Pagan et al. 2025](https://doi.org/10.1038/s41586-024-08433-6) | 11 (+2) | 2 | 0 (+1) | 0 | [`001550-pagan-2025`](entries/001550-pagan-2025) |
 | [001692](https://dandiarchive.org/dandiset/001692) | [Bouabid et al. 2026](https://doi.org/10.64898/2026.01.20.700614) | 18 | 8 | 3 | 0 | [`001692-bouabid-2026`](entries/001692-bouabid-2026) |
 | [001699](https://dandiarchive.org/dandiset/001699) | [Moore et al. 2025](https://doi.org/10.1101/2025.01.09.632139) | 14 | 7 | 5 | 1 | [`001699-moore-2025`](entries/001699-moore-2025) |
+| [001878](https://dandiarchive.org/dandiset/001878) | [Sun et al. 2021](https://doi.org/10.22002/d1.1991) | 4 (+1) | 2 (+1) | 0 | 0 | [`001878-sun-2021`](entries/001878-sun-2021) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001878/:
10.22002-d1.1991.yaml

transcripts/001878/:
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001878-sun-2021-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '001878' in json.dumps(x)];print(json.dumps(e,indent=1))"; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (213.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/92a314c0-b9a0-481d-a540-f3e8f0d898e7/tool-results/bgnm2cdah.txt

Preview (first 2KB):
schema_version: 1
id: 001878-sun-2021-01
dandiset: "001878"
dandiset_version: draft
paper: doi:10.22002/d1.1991
date: 2026-10-19
entry: 001878-sun-2021
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001878-sun-2021-01.yaml"
}
```

```
1	schema_version: 1
2	id: 001878-sun-2021-01
3	dandiset: "001878"
4	dandiset_version: draft
5	paper: doi:10.22002/d1.1991
6	date: 2026-10-19
7	entry: 001878-sun-2021
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: The CalMS21 dataset as deposited by the paper's authors (version 1.0), streamed from its zips
18	    with range requests. The pose, confidence scores and annotations of every sequence of Tasks 1 to 3
19	    and the unlabeled set, used for the link claim, the confidence-based pose-error claim and all
20	    claims with data elsewhere; the directory of task1_videos_mp4.zip, used to compare the size of the
[... 598 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else len(d))
"; grep -n '"001878"' targets/dandisets.json | head; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
6246:   "dandiset": "001878",
3633:### 001172, Lohani et al. 2022
3722:### 001528, Hadjas et al. 2025
3803:### 001538, Zhai et al. 2025
3902:### 001550, Pagan et al. 2025
4011:### 001692, Bouabid et al. 2026
4116:### 001699, Moore et al. 2025
4226 docs/pilot-notes.md
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 3722
}
```

```
File content (273.8KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "targets/dandisets.json",
 "offset": 6240,
 "limit": 40
}
```

```
6240	     "preprint": false
6241	    }
6242	   ],
6243	   "catalystneuro": []
6244	  },
6245	  {
6246	   "dandiset": "001878",
6247	   "name": "Standardized behavioral segmentation datasets",
6248	   "published_version": null,
6249	   "asset_count": 6,
6250	   "size_gb": 0.23,
6251	   "data_standards": [
6252	    "Neurodata Without Borders (NWB)"
6253	   ],
6254	   "species": [
6255	    "Mus musculus - House mouse"
6256	   ],
6257	   "approaches": [],
6258	   "papers": [
6259	    {
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs; awk 'NR>=3722' pilot-notes.md | cut -c1-3000 | head -c 60000
```

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/92a314c0-b9a0-481d-a540-f3e8f0d898e7/tool-results/bj8x6rv3s.txt

Preview (first 2KB):
### 001528, Hadjas et al. 2025

Twelve claims reproduced, five partially, three not reproduced and five
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 24 of the 25; it would
call `fig5-anxa1-dls-inhibited` not reproduced. The author kept it blocked as
`data_missing`, since at the deposited 5 and 4 mice three of its six Wilcoxon
tests cannot reach p < 0.05 and the paper's own W of -36 and -55 fix its n at
8 and 10, and round 2 accepted this. Round 2 agreed with all 25 and nothing was
proposed, so there was no third round. The paper, a bioRxiv preprint, reports
that STN and PPN inputs excite SNr GABA neurons and Vglut2+ dopamine neurons,
which are resilient in Parkinson's disease, while they inhibit dopamine release
in DLS and the DLS terminals of the vulnerable Anxa1+ neurons, and that
TH+/ANXA1+ neurons are reduced in human PD tissue. The group sizes, the SNr
GABA and pan-DA responses to train duration and frequency, the opposite TS and
DLS responses, the DLS rebound and 5 Hz increase, and the Vglut2 and Anxa1
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/92a314c0-b9a0-481d-a540-f3e8f0d898e7/tool-results/bj8x6rv3s.txt"
}
```

```
1	### 001528, Hadjas et al. 2025
2	
3	Twelve claims reproduced, five partially, three not reproduced and five
4	blocked on the dandiset. Round 1 gave its own outcome for each claim from the
5	notebook with its conclusions removed and agreed with 24 of the 25; it would
6	call `fig5-anxa1-dls-inhibited` not reproduced. The author kept it blocked as
7	`data_missing`, since at the deposited 5 and 4 mice three of its six Wilcoxon
8	tests cannot reach p < 0.05 and the paper's own W of -36 and -55 fix its n at
9	8 and 10, and round 2 accepted this. Round 2 agreed with all 25 and nothing was
10	proposed, so there was no third round. The paper, a bioRxiv preprint, reports
11	that STN and PPN inputs excite SNr GABA neurons and Vglut2+ dopamine neurons,
12	which are resilient in Parkinson's disease, while they inhibit dopamine release
13	in DLS and the DLS terminals of the vulnerable Anxa1+ neurons, and that
14	TH+/ANXA1+ neurons are reduced in human PD tissue. The group sizes, the SNr
15	GABA and pan-DA responses to train duration and frequency, the opposite TS and
16	DLS responses, the DLS rebound and 5 Hz increase, and the Vglut2 and Anxa1
17	terminal and cell-body responses were tested on the fiber photometry
18	recordings. The four human tissue claims are blocked as `data_missing`.
19	`cohort-sizes` is not reproduced (10 of 16 counts match, 11 with the Vglut2
20	STN count explained, against the 12 needed), `fig3g-da-ppn-duration` is not
[... 486 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../transcripts/001878; wc -c *report.md; cat author-report.md
```

```
6602 author-report.md
 3415 author-revise-1-report.md
 2248 author-revise-2-report.md
 9433 verifier-1-report.md
 4302 verifier-2-report.md
26000 total
I did steps 1 to 5 and ran the handover (step 6). The entry is `entries/001878-sun-2021`, the claims are in `claims/001878/10.22002-d1.1991.yaml`, and the attempt record is `attempts/001878-sun-2021-01.yaml`. `entry.py check` reports 0 errors and `all` passed. Nothing is committed.

The target DOI (10.22002/D1.1991) points to the CaltechDATA dataset record, not a paper. I used the full open-access text of the paper that describes the dataset: Sun et al. 2021, arXiv:2104.02710v4 (NeurIPS Datasets and Benchmarks), including its appendix and datasheet. The text is saved under `paper/`.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| format-keypoints | dandiset | partially reproduced (every confidence value is NaN) |
| resident-is-black | dandiset | reproduced (resident darker in 746 of 746 sampled frames) |
| task1-vocab | dandiset | reproduced |
| task1-video | dandiset | reproduced |
| contact-during-social-behaviors | dandiset | reproduced (this session has no attack frames) |
| pose-errors-close-fast | dandiset | partially reproduced: more errors when the mice are close, fewer (not more) when they move fast |
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001878; for f in verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== verifier-1-report.md
**A. Outcomes** (22 claims in the claims file: 10 reproduced, 6 partially reproduced, 6 blocked)

| Claim | My outcome | Reason |
|---|---|---|
| format-keypoints | partially_reproduced | Cell 16: 14 correctly named series, pixels, 30 Hz, all coordinates inside 1024 x 570. But all 333,340 confidence values are NaN, and the criterion's partial rule covers exactly that case. |
| resident-is-black | reproduced | Cell 18: with 746 frames ≥60 px apart and the 12 px patch, the resident is darker in 1.000 of frames (median grey 46 vs 251). This holds in every minute and every patch-size variant. |
| task1-vocab | reproduced | Cell 20: codes {attack 0, investigation 1, mount 2, other 3} and annotator "CalMS21 annotator 0". Cell 7: bouts tile 0 to 793.67 s with no gaps, so 0 unlabelled frames, and `frame_labels` raises on overlap. |
| task1-video | reproduced | Cells 9 and 22: 1024 x 570, 30 fps, 23,810 frames decoded, equal to the pose count. Motion energy peaks at lag 0. CaltechDATA also holds 89 Task 1 mp4s (70 + 19). |
| contact-during-social-behaviors | reproduced | Cell 24, nose-to-intruder minus other: investigation −354.6 px (CI −407 to −293), mount −361.0 px (CI −412 to −304). Attack has 0 frames in this session, so it is untested, as the criterion allows. |
| pose-errors-close-fast | partially_reproduced | Cell 26, factor 3 at 10%: errors are higher in close frames (+0.115, CI 0.064 to 0.179) but lower in fast frames (−0.020, CI −0.033 to −0.008). The same pattern holds in every variant. |
| link-mouse071 | reproduced | Cell 28: 23,810 frames in both, max coordinate difference 0 px, frame labels agree on 23,810 of 23,810. The CaltechDATA confidence scores (0.03 to 0.98) are absent from the dandiset. |
| pose-errors-close-fast-confidence | partially_reproduced | Cell 30: median confidence is lower in close frames (−0.091, CI −0.107 to −0.074) but higher in fast frames (+0.018, CI 0.012 to 0.025). The link it depends on is reproduced. |
| tab
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A8 'Counts are of claims' README.md; head -40 claims/001878/10.22002-d1.1991.yaml; grep -n 'data:' claims/001878/10.22002-d1.1991.yaml | sort | uniq -c | head -40; git status --short
```

```
105:Counts are of claims that rest on the dandiset, including those that take
106-names for its own codes from elsewhere. Claims that also use data from
107-outside the dandiset are counted apart, in brackets. Claims on data the
108-paper deposited in other archives are not in this table; the dashboard
109-shows them on each dandiset's page.
110-
111-## Agent runs
112-
113-Attempts by agents are made in GitHub Actions, one role at a time, on the
# Claims for the CalMS21 dataset (Sun et al. 2021) on dandiset 001878.
#
# The target's DOI, 10.22002/D1.1991, is the CaltechDATA record of the dataset, not a paper. The
# paper that describes the dataset and is cited by that record is Sun, Karigo, Chakraborty,
# Mohanty, Wild, Sun, Chen, Anderson, Perona, Yue and Kennedy (2021), "The Multi-Agent Behavior
# Dataset: Mouse Dyadic Social Interactions", NeurIPS 2021 Datasets and Benchmarks track,
# arXiv:2104.02710v4. Its full text is open access and was used, including the appendix with the
# datasheet (Appendix B), the data format (C), the dataset preparation (D) and the results tables.
#
# Dandiset 001878 is a collection of conversions from three source datasets. It holds one CalMS21
# sequence, the Task 1 test sequence mouse071 (pose, annotations as bouts, and the video). The rest
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 001878, Sun et al. 2021

Four claims reproduced and two partially on the dandiset, none not reproduced
or blocked. With outside data, counted apart: one reproduced and one partially
reproduced. Fourteen claims on the CalMS21 files on CaltechDATA: five
reproduced, three partially and six blocked. Round 1 gave its own outcome for
each claim from the notebook with its conclusions removed and agreed with all
22, but would give `data_missing` as the reason for blocking
`fig7-errors-at-transitions` and `fig11-annotator-similarity`; the author kept
`methods_underspecified`, since fig7 depends on the blocked baseline of
`table1-architectures` and fig11's matrix is a model output, named the missing
deposits as a second reason, and round 2 accepted this. Round 2 agreed with all
22 and nothing was proposed, so there was no third round. The target DOI
(10.22002/D1.1991) is the CaltechDATA record of the CalMS21 dataset, so the
author used the paper that describes it, a NeurIPS 2021 Datasets and
Benchmarks paper (arXiv:2104.02710v4), which presents pose and frame-level
behaviour annotations of a resident and an intruder mouse in three tasks, an
unlabeled set and baseline models. The keypoint format, the resident's coat
colour, the behaviour vocabulary, the video, contact during investigation and
mount, and pose errors when the mice are close or fast were tested on the
dandiset's one CalMS21 sequence, the link to CaltechDATA and the
confidence-based pose errors with CaltechDATA's scores, and the counts and
label fractions of Tables 5 to 7 and Figure 4B, the dataset size and the
difficulty of Task 3 behaviours on CaltechDATA. The six model benchmark claims
are blocked as `methods_underspecified`, as the baseline code the paper links
did not answer and the top entries' code is not linked. Both pose-error claims
are partially reproduced: errors are higher in the closest 10% of frames
(difference 0.115, interval 0.064 to 0.179, and confidence -0.091) but lower in
the fastest (difference -0.020, interval -0.033 to -0.008, and confidence
0.018), the reverse of the claim. `table5-task2-counts` is partially reproduced
on one count, 139,122 frames where Table 5 gives 139,112;
`table6-task1-label-fractions` because attack is 2.765009%, 0.000009 outside a
tolerance of half a unit of the last digit, and reproduced under the default
10%; and `table10-task3-difficulty` because the bout-length correlation is not
significant (0.321, p = 0.249; 0.607, p = 0.083). Some outcomes rest on weak
ground: `fig4b-task2-label-fractions` stays within 0.05 for annotator 1 attack
(3.2468% against 3.2) with up to 4 more attack frames, and the pose-error proxy
counts body lengths outside widened quartiles, which a hunched posture in mount
could also produce, though flagged close frames have lower confidence and eight
drawn at random show tracking errors by eye.

The dandiset was converted by CatalystNeuro (Heberto Mayorquin of CatalystNeuro
is a contributor). It has no published version, and the attempt used the draft
as modified on 2026-06-25T18:32:10Z. For CalMS21 it holds one sequence, the
Task 1 test sequence mouse071, out of 574 sequences on CaltechDATA, and its
description presents a collection of datasets without saying that only one
CalMS21 sequence is included or why this one was chosen. Its keypoints are
identical to CaltechDATA's and its labels agree on all 23,810 frames, but the
confidence field of all 14 pose series is present with all 333,340 values NaN,
where CaltechDATA's copy has them (0.03 to 0.98). The behaviour catalogue has
an empty definition for attack, investigation, mount and other; the two mice
are stored as one subject with strain C57BL/6, sex unknown and age P0D/, so the
intruder's strain (BALB/c) and the residents' sex are not recorded; the session
start time is a placeholder (2024-01-01T00:00); and `centroid_speed`, with the
bout columns that reduce it, is the speed of the midpoint of the two mice, which
its description does not make clear. Other findings: the video (184 MB) is a
re-encoding of CaltechDATA's (964 MB), with the same frame count, size and rate,
and the dandiset does not say so; the dandiset links the dataset DOI as
IsDerivedFrom but not the paper; on CaltechDATA the 574 sequences hold 450
distinct recordings, 93 of the 109 Task 3 test sequences are Task 1 training
recordings, five Task 1 test recordings (mouse071 among them) appear as six
Task 3 training sequences, and four Task 2 recordings are in the training set
of one of annotators 3 and 4 and the test set of the other, while the paper
treats each sequence as an independent observation and the CaltechDATA readme
says the sets are split by animal identity; the paper's datasheet says the raw
videos are not included, while Section 3.1 says the Task 1 videos are released,
and gives the licence as CC-BY-NC-SA, where CaltechDATA and the dandiset give
CC-BY 4.0; and the baseline code the paper links
(gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines) is not reachable
and no archived copy was found.

The notebook ran in 180 s in the first clean run, 247 s after round 1 and 4.4
minutes after round 2. While preparing, PyAV could not open the video URL and
was given a remote file object, and HEAD requests to CaltechDATA's presigned
URLs returned 403, so the helper used GET. After round 2 the first two re-runs
failed when CaltechDATA handed out a signed URL that had already expired, and
the helper now waits for a fresh one. Round 2 found statements the outputs did
not support, among them that most flagged frames fall in mount, where mount
holds 304 of 657, and six Task 1 test recordings where there are five, and
these were corrected. Untracked files in the repository root that the author
did not create were left alone. The author's points on the protocol: a target
DOI that is a dataset and not a paper; no published version to pin; a dandiset
that is a partial copy of the paper's own deposit, tested as `elsewhere`; a
link rule that assumes outside labels mapped onto dandiset units; a default
10% tolerance too loose for counts and percentages of a deposited file, with no
rule for rounding against truncation; a dandiset lacking a variable a claim
needs, so the pose-error claim was split in two; no rule for choosing between
two block reasons; no repository or commit to record for unreachable code;
claims that are themselves data checks; a duplicate check written for the
dandiset and run on the outside data; and the paper's own numbers used in an
analysis.
EOF
git diff --stat
```

```
README.md           |  1 +
 docs/pilot-notes.md | 92 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 93 insertions(+)
```

**Agent**

I ran `python tools/readme_row.py 001878 --write`, which added the 001878 row to the README table: 4 (+1) reproduced, 2 (+1) partially reproduced, 0 not reproduced, 0 blocked. I then added the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed.

The dandiset's `catalystneuro` field names a contributor, not a repository. So the opening sentence of the second paragraph follows the wording the 001699 subsection used in the same case.

### 001878, Sun et al. 2021

Four claims reproduced and two partially on the dandiset, none not reproduced
or blocked. With outside data, counted apart: one reproduced and one partially
reproduced. Fourteen claims on the CalMS21 files on CaltechDATA: five
reproduced, three partially and six blocked. Round 1 gave its own outcome for
each claim from the notebook with its conclusions removed and agreed with all
22, but would give `data_missing` as the reason for blocking
`fig7-errors-at-transitions` and `fig11-annotator-similarity`; the author kept
`methods_underspecified`, since fig7 depends on the blocked baseline of
`table1-architectures` and fig11's matrix is a model output, named the missing
deposits as a second reason, and round 2 accepted this. Round 2 agreed with all
22 and nothing was proposed, so there was no third round. The target DOI
(10.22002/D1.1991) is the CaltechDATA record of the CalMS21 dataset, so the
author used the paper that describes it, a NeurIPS 2021 Datasets and
Benchmarks paper (arXiv:2104.02710v4), which presents pose and frame-level
behaviour annotations of a resident and an intruder mouse in three tasks, an
unlabeled set and baseline models. The keypoint format, the resident's coat
colour, the behaviour vocabulary, the video, contact during investigation and
mount, and pose errors when the mice are close or fast were tested on the
dandiset's one CalMS21 sequence, the link to CaltechDATA and the
confidence-based pose errors with CaltechDATA's scores, and the counts and
label fractions of Tables 5 to 7 and Figure 4B, the dataset size and the
difficulty of Task 3 behaviours on CaltechDATA. The six model benchmark claims
are blocked as `methods_underspecified`, as the baseline code the paper links
did not answer and the top entries' code is not linked. Both pose-error claims
are partially reproduced: errors are higher in the closest 10% of frames
(difference 0.115, interval 0.064 to 0.179, and confidence -0.091) but lower in
the fastest (difference -0.020, interval -0.033 to -0.008, and confidence
0.018), the reverse of the claim. `table5-task2-counts` is partially reproduced
on one count, 139,122 frames where Table 5 gives 139,112;
`table6-task1-label-fractions` because attack is 2.765009%, 0.000009 outside a
tolerance of half a unit of the last digit, and reproduced under the default
10%; and `table10-task3-difficulty` because the bout-length correlation is not
significant (0.321, p = 0.249; 0.607, p = 0.083). Some outcomes rest on weak
ground: `fig4b-task2-label-fractions` stays within 0.05 for annotator 1 attack
(3.2468% against 3.2) with up to 4 more attack frames, and the pose-error proxy
counts body lengths outside widened quartiles, which a hunched posture in mount
could also produce, though flagged close frames have lower confidence and eight
drawn at random show tracking errors by eye.

The dandiset was converted by CatalystNeuro (Heberto Mayorquin of CatalystNeuro
is a contributor). It has no published version, and the attempt used the draft
as modified on 2026-06-25T18:32:10Z. For CalMS21 it holds one sequence, the
Task 1 test sequence mouse071, out of 574 sequences on CaltechDATA, and its
description presents a collection of datasets without saying that only one
CalMS21 sequence is included or why this one was chosen. Its keypoints are
identical to CaltechDATA's and its labels agree on all 23,810 frames, but the
confidence field of all 14 pose series is present with all 333,340 values NaN,
where CaltechDATA's copy has them (0.03 to 0.98). The behaviour catalogue has
an empty definition for attack, investigation, mount and other; the two mice
are stored as one subject with strain C57BL/6, sex unknown and age P0D/, so the
intruder's strain (BALB/c) and the residents' sex are not recorded; the session
start time is a placeholder (2024-01-01T00:00); and `centroid_speed`, with the
bout columns that reduce it, is the speed of the midpoint of the two mice, which
its description does not make clear. Other findings: the video (184 MB) is a
re-encoding of CaltechDATA's (964 MB), with the same frame count, size and rate,
and the dandiset does not say so; the dandiset links the dataset DOI as
IsDerivedFrom but not the paper; on CaltechDATA the 574 sequences hold 450
distinct recordings, 93 of the 109 Task 3 test sequences are Task 1 training
recordings, five Task 1 test recordings (mouse071 among them) appear as six
Task 3 training sequences, and four Task 2 recordings are in the training set
of one of annotators 3 and 4 and the test set of the other, while the paper
treats each sequence as an independent observation and the CaltechDATA readme
says the sets are split by animal identity; the paper's datasheet says the raw
videos are not included, while Section 3.1 says the Task 1 videos are released,
and gives the licence as CC-BY-NC-SA, where CaltechDATA and the dandiset give
CC-BY 4.0; and the baseline code the paper links
(gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines) is not reachable
and no archived copy was found.

The notebook ran in 180 s in the first clean run, 247 s after round 1 and 4.4
minutes after round 2. While preparing, PyAV could not open the video URL and
was given a remote file object, and HEAD requests to CaltechDATA's presigned
URLs returned 403, so the helper used GET. After round 2 the first two re-runs
failed when CaltechDATA handed out a signed URL that had already expired, and
the helper now waits for a fresh one. Round 2 found statements the outputs did
not support, among them that most flagged frames fall in mount, where mount
holds 304 of 657, and six Task 1 test recordings where there are five, and
these were corrected. Untracked files in the repository root that the author
did not create were left alone. The author's points on the protocol: a target
DOI that is a dataset and not a paper; no published version to pin; a dandiset
that is a partial copy of the paper's own deposit, tested as `elsewhere`; a
link rule that assumes outside labels mapped onto dandiset units; a default
10% tolerance too loose for counts and percentages of a deposited file, with no
rule for rounding against truncation; a dandiset lacking a variable a claim
needs, so the pose-error claim was split in two; no rule for choosing between
two block reasons; no repository or commit to record for unreachable code;
claims that are themselves data checks; a duplicate check written for the
dandiset and run on the outside data; and the paper's own numbers used in an
analysis.

## End of run

13 turns, 1 minutes, result: success.
