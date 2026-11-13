I finished steps 1 to 6 of the Author section: the entry is `entries/crcns-ac-4-holdgraf-2016/`, the record is `attempts/crcns-ac-4-holdgraf-2016-01.yaml`, and `entry.py check` and `all` pass. The handover is built. Nothing is committed and I did not verify my own work.

Of 26 claims, 10 are reproduced, 5 partially reproduced, 5 not reproduced and 6 blocked. The biggest gap is the eSTRF electrode selection: only 9 electrodes qualify against the paper's 53, so every eSTRF claim rests on 9 electrodes from three subjects. That may be a failure of this attempt, not of the paper.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| behav-no-context-baseline, behav-context-enhancement, supp1a-linguistic-context, supp1a-speaker-no-difference, supp1b-filter-type, supp5a-behaviour-over-trials | blocked, `data_missing` |
| speech-r-count | reproduced (101 Speech-R; 3 of 12 readings match; 377 electrodes against the paper's 468) |
| fig3b-hfb-increase-after | reproduced (cluster 0.36 to 1.28 s, P = 0.0001) |
| supp3a-pink-noise-no-hfb-change | reproduced (smallest cluster P = 0.09; but the effect size equals the speech triplets', 0.041 z) |
| supp5b-hfb-stable-over-session | not reproduced (negative slope, interval excludes 0) |
| fig4a-coherence-after-higher | reproduced, rests on an assumption |
| fig4b-coherence-sentence-specific | reproduced, rests on an assumption (0 to 1 s also significant, unlike the paper) |
| strf-r-count | not reproduced (9 against 53) |
| included-electrode-count | not reproduced (9 against 41) |
| fig8-mtf-matches-filter | partially reproduced, rests on an assumption (holds in BEFORE and AFTER, not in the shift) |
| fig9-rms-increase | partially reproduced (direction and P < 0.05 hold; the paper's scale is unknown) |
| fig9-middle-generalizes-after | reproduced (0.051, P = 0.021, n = 9) |
| fig10-partial-correlation | partially reproduced (0.31 against 0.18, P = 0.011) |
| fig10b-similarity-correlates | not reproduced (r = 0.63, P = 0.07) |
| fig10c-stg-location | reproduced (51.7% on STG, a small margin) |
| supp3b-pink-noise-no-pcorr-change | blocked, `other` (no included electrode in the pink noise subjects) |
| supp6a-connectivity-increase | partially reproduced, rests on an assumption (frontal P = 0.031, temporal P = 0.094) |
| supp6a-after-closer-to-middle | reproduced, rests on an assumption |
| supp6b-no-pac-change | reproduced (P = 0.14) |
| supp7-envelope-coherence | not reproduced (no temporal theta effect; a frontal effect, P = 0.0012) |
| supp4-hfb-power-increase | reproduced |

### 2. Dataset, assumptions, questions

**What the dataset holds:**
- 7 subjects with 416 channels (377 good). The paper has 524 recorded and 468 kept, and nothing says which channels were dropped.
- The subject names (S01 to S13) have no mapping to the paper's S1 to S7.
- Stored values are not in the stated millivolts: about 300 in S01 and about 1e8 in the others.
- The behavioural control data are absent.
- The stimulus audio is included and on the recording clock, although the dataset's own notebook says it is not available. S07's audio track is longer than its recording.
- `bad` spans in the events tables are undocumented, and two triplets are incomplete.
- Version: unversioned, the single `live/` copy (descriptor v0.6), with the MD5s printed in the notebook header.

**Assumptions:**
- The Speech-R z-score is the code's z-score by non-event times. It is the only one of three readings that gives counts near 92.
- The ridge parameter is the mode below the top of the grid: the plain mode always falls on the grid edge.
- Coherence uses three tapers (NW = 2), because MNE's default gives one taper on 400 ms windows.
- For fig8, "low" and "high" modulation regions are split at the plane's median.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How HFB was z-scored for the Speech-R selection.
- How the ridge mode and the STRF-R R2 bound were computed.
- What multitaper bandwidth the coherence used.
- What scale the RMS in Figure 9c is on.

**Questions for a reader:** none.

### 3. Where the protocol was unclear or missing something
1. The `methods_unavailable` finding kind is for the dataset, but the questions are about the paper. I used it as the protocol says.
2. It does not say what happens when a dependent claim's selection, here `included-electrode-count`, is not reproduced but not blocked. I tested the dependents on this attempt's 9 electrodes and said so in their notes.
3. A criterion's readings (z-score, window, trials) gave different outcomes. I followed "reproduced if any reading matches" and used the first matching reading in the criterion's order for the later claims.
4. "Too few units under the claim's own rule" only names `other` as an example. I used `other` for supp3b, where zero units qualified.
5. It does not say how to report a selection threshold whose dataset total differs (377 against 468 electrodes). I reported the total and did not judge it, as the criterion says.

### 4. Runtime and failures
- About 65 minutes in all (07:53 to 08:56 UTC). The notebook runs in 12.7 minutes with a peak of about 2.9 GB.
- Nothing failed in the final run.
- One command, reading a saved output file through sed and grep, was denied for lack of approval. I read the file with the Read tool instead.
- The working tree also has untracked dotfiles at the repo root (`.bashrc`, `.gitconfig` and others) and a modified `tools/build_site.py`. They were there before this run and I left them alone; the workflow should keep them out of the commit.
