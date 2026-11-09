# Report: author run on DANDI:000637 (Gao et al. 2025)

All 30 claims are blocked as `data_missing`: none of them can be tested on this dataset. The entry runs cleanly: `entry.py all` gives 0 errors and the notebook takes 332 s. The handover is built in `executed/000637-gao-2025/handover/`.

## 1. Outcomes

| Claims | Outcome | Main reason |
|---|---|---|
| unit-counts | blocked, data_missing | No waveforms, so no RSU/FSU split; no POm units |
| fig4 S1 claims (3000 Hz time-locked, post-sonication, 30 Hz inhibition) | blocked, data_missing | No cell types (and no POm for fig4-post-3000) |
| fig4 POm claims, fig4-fsu-no-change | blocked, data_missing | No POm units, no cell types |
| fig5 sham, fig5 CG1 control | blocked, data_missing | No sham-labelled or CG1-targeted recordings; no cell types |
| fig6a, fig6b (S1) | blocked, data_missing | No cell types (all five PRFs at 200 us are present) |
| fig6c, fig6d (POm) | blocked, data_missing | No POm units |
| fig7a–d, fig8a–b, fig9a–b | blocked, data_missing | No cell types; most duty cycles are absent; no POm for 7c and 7d |
| fig10a–ef (dSTTC and STTC) | blocked, data_missing | Need S1 and POm pairs |
| fig11b–d | blocked, data_missing | No auditory cortex units |

## 2. What the dataset holds

- **Contents:** 292 files from 25 rats (BH401 to BH477), one 32-channel probe per file, all in S1. The units have spike times only: no waveforms, no electrode for each unit, and every electrode location is "unknown". The trials tables have start and stop times only, and the stimulation condition is coded only in each file's identifier.
- **Pinned version:** 0.250829.1249, the latest published one. The paper cites no version of 000637; its data statement names a different dandiset, 000946. The notebook shows that all five published versions have the same files with the same digests.
- **Not the paper's units:**
  - 000946 holds other rats (BH494 to BH535).
  - 000637 has 4,642 S1 units over the paper's 2,000-spike threshold in the PRF series at 200 us. The paper reports 1,297 S1 RSUs and FSUs combined, so 000637 has about 3.6 times as many.
  - No recording could be linked to the paper's.
- **Metadata errors:**
  - 73 of the 292 files have fewer than the 500 trials the description states.
  - The description swaps pulse duration and ultrasound duration.
  - Recordings at 600 us and at 3.5, 5.5 and 7 V exist but are not described.
  - Three recordings named BASELINE have no description saying what they are.
- **Checks that held:**
  - The trial starts behave as tFUS onsets. 74% of units fire more in the 0 to 67 ms after onset than in the 67 ms before, against 43% with onsets shifted by 1.2 s; 23 of 25 rats show the effect. Intertrial intervals are 2.25 to 2.75 s, as the paper states.
  - No unit was deposited twice.
- **Pooled variant (decides no claim):** pooling all S1 units across cell types, every PRF raises the 0 to 67 ms rate, and 300 to 4500 Hz raise the 201 to 268 ms rate.
- **Assumptions, questions:** no outcome rests on an assumption. There are no questions for the paper's authors and none for a reader.

## 3. Where the protocol was unclear

1. **`elsewhere` against `data_missing`.** The protocol says to use `data_missing` only when the data are "not public anywhere else". The paper's own deposit, 000946, is public, but it is a separate target in this registry with the same paper and holds different animals. I used `data_missing`, because the waveforms of 000637's own units are not public anywhere. I said so in the notes and left the claims' `data` fields unchanged.
2. **A target dataset that may not be the paper's data.** The protocol has no outcome or finding kind for this. I recorded it as a finding of kind `other` and gave the unit-count comparison as evidence.
3. **Analyses shown for blocked claims.** There is no guidance on tagging analyses that decide no claim. I tagged them `variant:...`, and gave the unit-counts cell the `claim:unit-counts` tag even though that claim is blocked.
4. **Untested claims in the notebook.** The protocol requires one section per tested claim and is silent when none is tested. The notebook has a header table, the data checks, a table of the conditions each claim needs against those present, the variants, and a summary.

## 4. Runtime and failures

- The run took about 26 minutes (07:59 to 08:25 UTC).
- The notebook takes about 5.5 minutes, most of it streaming the 292 files.
- Nothing failed.
- `git status` also lists untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them untouched.

Files are in `entries/000637-gao-2025/`:
- `reproduce_gao_2025.ipynb`
- `tfus.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/000637-gao-2025-01.yaml`.
