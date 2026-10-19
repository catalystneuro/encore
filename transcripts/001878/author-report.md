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
| link-mouse071 | with inputs | reproduced (keypoints identical, labels agree on all 23,810 frames) |
| pose-errors-close-fast-confidence | with inputs | partially reproduced: same pattern as above |
| table5-task1-counts | elsewhere | reproduced |
| table5-task2-counts | elsewhere | partially reproduced (one count is 139,122 in the data, 139,112 in the paper) |
| table5-task3-counts | elsewhere | reproduced |
| table6-task1-label-fractions | elsewhere | partially reproduced (attack is 2.765009%, 0.000009 outside the tolerance I set) |
| fig4b-task2-label-fractions | elsewhere | reproduced |
| table7-task3-label-fractions | elsewhere | reproduced |
| dataset-size | elsewhere | reproduced |
| table10-task3-difficulty | elsewhere | partially reproduced (the bout-length correlation is not significant) |
| Six model-benchmark claims | elsewhere | blocked (methods_underspecified) |

## 2. What was found about the dandiset

- **No published version.** Only a draft exists, last modified 2026-06-25T18:32:10Z.
- **One CalMS21 sequence.** The dandiset combines three source datasets. For CalMS21 it holds only the Task 1 test sequence mouse071, out of 574 sequences in the full dataset. The other two NWB files come from keypoint-MoSeq and the Mlost benchmark.
- **The sequence is a faithful copy except for the scores.** Its pose and labels match CaltechDATA exactly, and its video shares the pose's clock (motion correlation peaks at lag 0).
- **Confidence scores missing.** The confidence field exists for all 14 keypoints, but all 333,340 values are NaN.
- **Metadata gaps:**
  - The behavior catalogue has empty definitions.
  - The two mice are stored as one subject: strain C57BL/6 only, sex unknown, age `P0D/`.
  - The session start time is a placeholder (2024-01-01).
  - `centroid_speed` is the speed of the midpoint of the two mice, not of either animal, and its description does not say so.
  - The video was re-encoded (184 MB against CaltechDATA's 964 MB) without a note.
  - The paper itself is not linked, only the dataset DOI.
- **About the CaltechDATA deposit:**
  - The 574 sequences hold only 450 distinct recordings.
  - Some repeats cross training and test splits, including four Task 2 recordings between annotators 3 and 4.
  - The paper's datasheet gives the licence as CC-BY-NC-SA, while the deposit and the dandiset say CC-BY 4.0.
  - The datasheet says raw videos are not included; Section 3.1 and the deposit include them.
  - The baseline code the paper links (gitlab.aicrowd.com) does not respond, and I found no archived copy of the repository.

## 3. Where the protocol was unclear, wrong or missing something

1. **The target DOI is a dataset, not a paper.** I used the paper that describes the dataset and kept the target DOI as the `paper` key.
2. **No published version to pin.** The protocol covers drafts only for repeat attempts. I pinned the draft by the blob id of each asset (the helper stops if one changes) and recorded the modification time.
3. **The dandiset is a partial copy of the paper's own deposit.** I made the dataset-level claims `elsewhere`, tested on CaltechDATA, though "elsewhere" in the protocol reads as a different archive from the paper's.
4. **The link rule assumes outside labels mapped onto dandiset units.** Here the dandiset record is itself a copy of an outside record, so I made it a `with_inputs` link claim comparing the two copies.
5. **Default 10% tolerance is too loose for counts in a deposited file.** I used 0 for counts and half a unit of the last reported digit for percentages, with the reason given. That makes Table 6 partial, and the protocol does not say how to treat rounding against truncation.
6. **The dandiset lacks a variable a claim needs.** The scores are on CaltechDATA, so I split the pose-error claim in two: a dandiset-only version with a geometric error measure, and a `with_inputs` version using the CaltechDATA scores.
7. **Two block reasons both apply** (code unreachable, and training time). The protocol gives no rule for choosing; I used `methods_underspecified` and mentioned the other in the notes.
8. **No repository or commit to record for the paper's code** because it is unreachable. I recorded this as a `methods_unavailable` finding.
9. **Several claims are themselves data checks** (format, vocabulary, video). I saw their values during step 2, before writing criteria, and said so in the claims file's opening comment.
10. **The duplicate check is written for the dandiset.** I also ran it on the 22 GB of outside data, and used "each recording counted once" as one reading of the paper's totals.
11. **The paper's own numbers used in an analysis** (Table 10 F1 scores). I treated them as reference values, not as `inputs`.

## 4. Runtime and failures

- The notebook runs in 180 s in the clean environment. About 120 s of that is streaming all CalMS21 JSON from CaltechDATA by range requests, and 32 s is decoding the video.
- gitlab.aicrowd.com timed out, with and without the sandbox.
- Two problems were fixed along the way: PyAV could not open the video URL directly, so I pass it a remote file object; and HEAD requests to CaltechDATA's 60-second presigned URLs return 403, so the helper uses GET.
- Untracked dotfiles (`.bashrc`, `.gitconfig`, `.mcp.json` and others) and a character device named `scripts` are at the repository root. The device was already there when I started and I did not create the dotfiles; I left both alone.
