I finished steps 1 to 6 by 23:51 UTC, about 1 h 10 min into the 5 h window. Only one of the 33 claims could be tested: the dataset has no spike waveforms and no cell types, and the paper's RSU/FSU split depends on them. The entry passes its checks and runs from a clean environment in 258 s, and the handover is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig11b-ac-responses | Partially reproduced (`assumed: true`) |
| fig4-unit-counts, fig6-unit-counts | Blocked, data_missing (area totals shown in the notes) |
| fig4a, fig4b, fig4-postsonication-3000, fig4-30hz-responses, fig4-fsu-no-change | Blocked, data_missing |
| fig5a-sham-no-change, fig5b-cg1-control-no-change | Blocked, data_missing (also no sham or CG1 sessions marked) |
| fig6a (2 claims), fig6b, fig6c, fig6d | Blocked, data_missing |
| fig7a to fig7d, fig8a, fig8b, fig9a, fig9b | Blocked, data_missing |
| fig10a to fig10f | Blocked, data_missing |
| fig11c-ac-to-s1-30hz, fig11d-ac-to-s1-3000 | Blocked, data_missing (the S1 units need cell types) |
| pathway-follows-local-prf, auditory-confound-low-prf | Blocked, because they depend on blocked claims |

**Fig. 11B (auditory cortex neurons):**
- **What matches:** under the adopted reading, the after-sonication set is exactly 30, 1500, 3000 and 4500 Hz, 300 Hz has the lowest response in both windows, and both Kruskal-Wallis tests are significant.
- **What does not:**
  - During sonication, 4500 Hz is also above baseline, so that set has one PRF more than the paper's.
  - The dataset gives 633 AC units with more than 2000 spikes, against the paper's 453.

## 2. The dataset
- **No cell types:** no file holds waveforms. `celltype_label` is described as 1 = RSU and 2 = FSU, but it is 0 in all 1516 files that have it, and the other 34 files lack the column.
- **Duplicates:** 734 of the 1550 unit files are copies of another file, with identical spike times and trial starts. I counted the 816 distinct recordings once each.
- **Sham and control sessions:** none is marked as sham or as aimed at CG1, so Fig. 5 cannot be found.
- **Rats:** 10 have POm recordings and 7 have AC recordings, where the paper reports 16 and 12.
- **Extra data:** there are M1 recordings and sessions with tFUS aimed at M1 or POm, which the paper does not describe.
- **Smaller metadata problems:**
  - The two area files of one session have identical trials but different `session_start_time` values.
  - The area is given only in free-text notes.
  - The PRF and PD field is empty in 33 recordings; the identifier supplies them there.
- **STTC files:** their arrays have no dimension for the dt values their description lists, and they name no units.
- **Clock check:** firing changes after the trial starts and not when the starts are shifted by 1 s, so the trial times share the spike clock.
- **Version:** I pinned 0.250829.1249, the latest. The paper cites the dandiset without a version, and all six versions list the same files.

**Assumption, and the question for the paper's authors** (recorded as a `methods_unavailable` finding):
- The paper does not say how the normalized rate is computed or what the baseline sample is. I adopted the ratio of mean rates over trials, compared with the 67 ms before stimulation.
- The alternative averages per-trial ratios over trials with a nonzero baseline. It reads 50 to 62% even with no stimulus, so it cannot be a rate normalized to the pre-stimulus period.
- The readings give different outcomes for Fig. 11B, and the notebook shows all of them.

I asked a reader no questions.

## 3. Protocol gaps
1. **Almost everything blocked:** the protocol does not address a dataset where one missing variable (cell type) blocks nearly every claim. I blocked each claim as data_missing and showed untyped results as variants that decide nothing.
2. **A reading that is an artefact:** step 1.6 says to run every reading, but one of the claims file's readings is biased by construction. I ran it, showed the bias against shifted trial starts, and adopted the other reading as an assumption.
3. **Extra data:** there is no rule for a dataset holding experiments the paper does not describe. I recorded it as an `other` finding.
4. **Header in the notebook:** the protocol does not name a header field for the reason the version was chosen. I put it in the notebook header.
5. **Untracked files at the repo root:** `.bashrc`, `scripts` and others are sandbox device mounts created before this run. I left them alone. The workflow should not commit them.

## 4. Runtime and failures
- The notebook takes about 4.3 min; reading all 1920 file headers and hashing the duplicate pairs take most of that.
- My first survey used threads and took 28 min, because h5py runs one call at a time across threads; the helper uses processes instead.
- One early notebook run failed on a pandas type error, which I fixed.
- Nothing failed in the final run.

Files are in `entries/000946-gao-2025/`:
- `reproduce_gao_2025.ipynb`
- `tfus.py`

The attempt record is `attempts/000946-gao-2025-01.yaml`.
