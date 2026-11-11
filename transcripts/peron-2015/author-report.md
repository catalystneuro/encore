Peron 2015 is done: 2 of the 43 claims were tested (1 reproduced, 1 not reproduced) and 41 are blocked. Most claims can't be tested because CRCNS ssc-1 holds only a small part of the paper's data and none of the labels the analyses need. The entry runs clean (`tools/entry.py all`: 0 errors, notebook passes in 29 s) and the handover is in `executed/peron-2015/handover/`.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| results-trials-per-session | reproduced: 290.2 pooled, 272.5 as the mean of per-mouse means; the paper gives 245 ± 71 |
| results-whisking-amplitude | not reproduced: 74.7°, 29.0° and 26.9° under the three readings; the paper gives 55.5 ± 13.3 |
| table-s1-roi-counts, results-gaba-fraction, fig4d-gaba-reward-cue, fig2e, fig1e, fig1g, supp-trim, figs4 | blocked, `data_missing` |
| fig2-core-counts and 17 claims comparing layers, cell classes or columns | blocked, `metadata_insufficient` (rule M6 of the claims file) |
| 3 neuropil/L4 axon, 8 learning and 3 anesthetized claims | blocked, `data_missing` |
| methods-event-detection (outside data) | blocked, `methods_underspecified` |

**2. The dataset, assumptions and questions**
- **What it holds:** 5 sessions from 3 of the paper's 8 mice (an197522, an229717, an229719). That is 26,761 ROIs, against 108,374 in Table S1; per mouse it is 20% to 72% of the Table S1 count. The spared whiskers match Table S1. The version is recorded as `unversioned` (CRCNS has no versions), and the MD5 of each file read matches `checksums.md5`.
- **What the descriptor promises but isn't there:** no calcium events, no raw fluorescence, no `vol_xxx` multi-session files, and no layer, cell-class, column or plane-depth labels. There is also no learning, L4 axon, anesthetized, dendrite-soma, training or reference-stack data.
- **Smaller descriptor errors:** one undescribed subvolume is a single plane at 29 Hz, and many subvolumes have ROIs on fewer than three planes. The structure is called `eventSeriesArrayHash`, not `eventSeriesHash`, and one file is named `sesssion.mat`.
- **Checks that passed:** no recording is deposited twice. Subvolume fov_06 of an229719 appears in both of that mouse's sessions, with the same ROI ids but different recordings, so it is counted once.
- **Clock check:** in an197522's 2013-03-10 session, the touch response could not be shown to share the trial clock. No tested claim uses dF/F.
- **Assumption:** reading (c) of whisking amplitude needs a band before the Hilbert transform, which the paper doesn't give; I used 6 to 30 Hz. The 4 to 30 and 8 to 25 Hz bands give the same outcome, so the outcome doesn't rest on this choice.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - How was the 55.5° whisking amplitude measured? Twice the peak Hilbert amplitude gives 53.7°, inside the tolerance, but the criterion doesn't list that measure.
  - How was the event detector validated: which Chen 2013 recordings, how they were degraded, and which windows? CRCNS cai-1 holds such recordings.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. A per-mouse count claim when most of each mouse's sessions aren't deposited: neither "test what's there" nor `data_missing` clearly fits. I chose `data_missing` and printed the counts in the notes.
2. The CRCNS imaging tarballs (165 GB) can only be listed by streaming through them; nothing in the guide covers that. I listed one tarball in full while preparing and said so in the notebook ("not run here").
3. The `entry.py check` requires the string `unversioned` to appear in the notebook or helper; docs/archives.md doesn't say so. I added `VERSION = "unversioned"` to the helper.
4. For a blocked claim whose numbers can still be shown (ROI counts), it isn't clear where they belong. I put them in an untagged data-check cell.

**4. Runtime and failures**
- About 20 minutes of work. The notebook runs in 29 s with 0.86 GB peak memory.
- One run failed: a regex I used to strip bold text also broke a `**` dict unpacking in a code cell. I fixed it and re-ran; the run now passes.
- Untracked files I didn't create (`.bashrc`, `.profile`, `.vscode`, `scripts/` and others) are in the repo root. I left them alone, but the commit step may pick them up.

Files are in `entries/peron-2015/`:
- `reproduce_peron_2015.ipynb`
- `ssc1.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The attempt record is `attempts/peron-2015-01.yaml`.
