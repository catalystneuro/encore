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
