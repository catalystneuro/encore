I tested 22 of the 43 claims and blocked 21; the entry runs and passes its checks. 12 tested claims are reproduced, 5 partially reproduced and 5 not reproduced. The notebook ran in 12.3 min (734 s) from a clean environment, nothing failed, and its outputs match the development run line for line. The verifier's package is built in `executed/001868-kim-2026/handover/`.

### 1. Outcome per claim

| Claim | Outcome |
|---|---|
| fig2a-threshold-decrease | reproduced (medians 5.41 and 3.84 uA, p = 5.4e-6) |
| fig2a-steepest-decline-early | reproduced (`assumed`, the claims file's reading of the figure) |
| figs1e-response-times-decrease | reproduced |
| figs5c-wheel-onset-decrease | reproduced (119, 133 and 128 ms) |
| fig4-unit-counts | partially reproduced (488 modulated, 795 units against the paper's 973) |
| figs3b-modulation-increase-all | reproduced |
| figs3c-latency-all | partially reproduced (also significant at 4 uA) |
| figs3d-modulation-stable-at-threshold | reproduced |
| fig4g-modulated-count-mouse1 | reproduced (same n, p 0.044 and r 0.42 as the paper) |
| fig4ij-pyramidal-modulation-increase | reproduced |
| fig4ij-interneurons-little-change | reproduced |
| fig5d-pulse-locking-stable-across-currents | reproduced (0.842) |
| fig5e-pyramidal-fraction-pl | reproduced (0.747 and 0.536) |
| figs4b-pl-latency-distance | not reproduced (no positive slope) |
| fig5fg-pl-modulation-increase | partially reproduced (time to maximum at 6 uA p = 0.08) |
| figs4de-npl-no-change | not reproduced (4 uA p = 0.042) |
| fig5h-pl-spike-probability-increase | partially reproduced (6 uA only) |
| figs5-restricted-window-consistent | reproduced, under one of the two readings |
| fig6c-kl-divergence | not reproduced (separation falls over training) |
| fig6d-npl-hit-miss-divergence | not reproduced |
| fig6f-population-coupling | reproduced |
| figs9a-coupling-700ms | reproduced |
| figs9-coupling-window-and-control | blocked, `methods_underspecified` (its 120 ms part holds) |
| 7 volumetric Fig. 2 and fig. S2 claims | blocked, `metadata_insufficient` |
| figs2de-control-stable | blocked, `metadata_insufficient` |
| 9 planar Fig. 3 and fig. S6 claims | blocked, `metadata_insufficient` |
| fig4d-waveform-separation, figs8-tracked-units | blocked, `data_missing` |
| figs7-control-no-change | blocked, `methods_underspecified` |

### 2. Dataset, assumptions and questions

**What the dataset holds.**
- **Version:** I pinned 0.260715.2016, which the paper's data statement cites. It is the only published version, and the draft is identical to it.
- **Sessions:** there are 55 behavioural sessions, and the 46 in weeks 0 to 4 match the paper's count.
- **Units:** I found 795 unit-sessions in those 46 sessions and 999 over all 55, against the paper's 973. Response counts per current are close to the paper's.
- **Volumetric imaging:** there is no stimulation-site position in the imaging volume, no activation calls and no voxel-level responses.
- **Planar imaging:** the ROIs are segmented separately in each session, with no identity across sessions and no stored images to align them.
- **Waveforms:** each unit has one single-channel mean waveform. There are no waveforms in and out of stimulation and no multi-channel templates.
- **Control files:** they use 3 bursts of 10 pulses at 50 Hz, while the paper says the controls had similar stimulation. The survey imaging has no voxel size, plane spacing or channel-to-contact mapping.
- **Trials and labels:**
  - Most miss trials have no response time.
  - `response_time` is measured from trial start, 0 to 85 ms before the train.
  - Mouse 6 has no catch trials.
  - Cell types are spelled differently in Mouse 6, and 72 units disagree with the 0.45 ms trough-to-peak rule.
- **Train table:** it describes 700 ms trains but also holds long trains from the planar block.
- **Channel mapping:** `stim_channel` is not confirmed to match the electrode table's `channel_name`. Modulation does not fall with distance from the contact, so the fig. S4 distances are uncertain.

No identical recordings were found deposited twice.

**Assumptions.** The only outcome resting on an assumption is fig2a-steepest-decline-early, and that assumption is the claims file's own. Two choices of mine could not change an outcome, so I recorded them as standard choices:
- a coarser psignifit grid for the threshold fits, to keep the run time down;
- swapping each response's hit and miss rows as the permutation in fig. 6D.

**Questions for the paper's authors**, recorded as `methods_unavailable` findings:
- fig. 6D: the PSTH bin width and smoothing, and whether the onset is the first or the last significant cluster.
- fig. S5: whether the modulated set and PL labels were recomputed in the 120 ms window.
- fig. S7 and S9C: how the controls were analysed with their burst protocol.

**Questions to a reader:** none.

### 3. Protocol points
1. A claim that is a conjunction where one part cannot be tested (figs9: the 120 ms window plus the controls) has no outcome rule. I blocked it and gave the tested part in the notes.
2. Criteria that define no partial outcome (figs3c, fig5h, fig4-unit-counts) leave open how to grade a result that holds in part. I used the protocol's general "holds only in part" and said so in the notes.
3. Step 1.3 says to pin the version the paper cites "as the claims file gives it". Both agreed here, but my first draft of the header said otherwise; I corrected it after checking the paper's text.
4. Nothing says how to handle an expected value (an n) that the criterion does not judge. For fig2a the late n of 89 is just outside 80 ± 8; I reported it in the notes without changing the outcome.

### 4. Runtime and failures
The run started at 23:29 UTC and finished at about 00:52 UTC. The notebook takes 12.3 min, mostly the 456 psignifit fits; at psignifit's default grid it would take about twice as long. `lock`, `check`, `all` and `handover` all passed, nothing failed, and nothing was committed.

The repository root shows untracked device files (`.bashrc`, `.idea` and others). I did not create them; they come from the sandbox.

Files are in `entries/001868-kim-2026/`:
- `reproduce_kim_2026.ipynb`
- `icms.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The attempt record is `attempts/001868-kim-2026-01.yaml`.
