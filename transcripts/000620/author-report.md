The attempt is finished: 6 claims reproduced in full and a seventh resting on an assumption, 4 partially reproduced, 1 not reproduced and 14 blocked (13 too large to run, 1 because the paper's method is unclear). Both notebooks pass `tools/entry.py all`. The record is `attempts/000620-watters-2026-01.yaml`, the handover package is in `executed/000620-watters-2026/handover/`, and nothing is committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| fig1b-performance-load | reproduced (reading (a) gives exactly the code's printed P 0.953/0.930/0.692, E 0.928/0.759/0.561) |
| fig1c-reaction-times | reproduced |
| ext1-misbinding-errors | reproduced, `assumed: true` (rests on the code's correctness radius, see 2) |
| triangle-unit-counts | reproduced (4,688 / 2,937 / 1,751, 10 + 14 sessions, exact) |
| ring-unit-counts | reproduced (3,052 / 1,712 / 1,340 against 3,051 / 1,712 / 1,339) |
| ext2-stimulus-delay-activity | reproduced |
| fig5ab-ring-behavior | reproduced |
| fig2b-selectivity-range | partially reproduced (position AUCs meet the "wide range" rule; identity AUCs fall short of its 0.7 cut-off) |
| fig5cd-ring-tuning | partially reproduced (receptive fields vary as claimed; the AUC part fails) |
| fig5e-signal-noise-ring | partially reproduced (holds for P and pooled, not for E) |
| ext3ab-decoding | partially reproduced (position decodes far above control; identity does not) |
| ext3c-decoder-orthogonality | not reproduced (synthetic data without slots do give near-90° angles, but Triangle neural medians are 106.7° and 106.5°) |
| fig2d-signal-noise-triangle | blocked, methods_underspecified (the Methods' version reproduces; the code's version fails for E's lowest bin; the criterion says differing methods block the claim) |
| fig4a, ext6, ext5, fig4b, nslots, ext11, ext7, fig4c, fig4d, ext8, fig5f, fig5g, fig5h | blocked, too_large (one step of the paper's models takes about 0.87 s, so one fit is 2.4 h and fig4a alone about 230 days; no fit was started) |

## 2. Dataset findings, assumptions, questions

**Version.** I pinned 0.261019.2000, the latest published version; the paper cites none, and all published versions hold the same 142 assets.

**Findings about the dataset:**
- **Correctness radius.** The task rewarded every completed trial with a closed-loop error under 0.2 arena widths (4.8°) and none above. That matches the code, not the 2.4° in the Methods.
- **Cue phase.** It lasts 250 ms in the data, against 180 ms in the Methods. `response_time` reads as saccade onset: 47.9% of completed trials fall before the response phase, and some fall before cue onset. Its description does not say which event it marks.
- **Electrode locations.** Every electrodes table gives the location "unknown"; brain area comes only from the probe name.
- **Undescribed sessions.** Perle 2022-06-06 (2-object trials only, with spike sorting) and 2022-06-08 (behaviour only) are in the dandiset but not the paper. The code's Ring model comparison drops Elgar 09-18 and 09-19.
- **Unit labels.** Two thirds of the paper's "well-isolated neurons" are labelled multi-unit. Its counts also skip the Methods' 500-trial stability rule.
- **AUC p-value.** The code's p-value is a resampled-label null of 5,000 draws, not the Methods' 1,000 shuffles.
- **No problems found** with duplicate recordings, spike-time sorting, or spikes outside stable intervals. The clock check passes in every session; for Elgar 2022-08-23 it rests on the delay window only.

**Assumption.** For ext1 I used the 0.2 radius, because it is what the task rewarded and what the code that made Extended Data Fig. 1 uses.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which signal correlation does Fig. 2d show, the Methods' or the code's?
- Which correctness radius was used: 2.4° (Methods) or 4.8° (code and reward data)?
- How were the Fig. 2b AUCs cross-validated?

**Questions to a reader:** none.

## 3. Protocol points

1. The fig2d criterion says differing methods block the claim, while step 1.6 allows adopting the best-supported reading as an assumption. I followed the criterion and blocked it.
2. Several criteria (fig2b, fig5cd, fig5e, ext3ab) give no rule for a partial result. I used the protocol's general definition of partially reproduced.
3. T2 (the correctness radius) is left open with no rule for when readings disagree. I applied step 1.6 and backed the choice with the reward data.
4. "Every sentence backed by a printed number" does not fit timings that vary between runs. I wrote them as "about".
5. The protocol does not say how to treat a clock check that fails in one window but passes in another (Elgar 2022-08-23). I reported it as established through the delay window only.
6. Estimating the cost of PyTorch models without installing torch in the locked environment is not covered. I timed a numpy step of the same sizes and stated it as a lower bound.
7. It is unclear whether reference values printed by the paper's code may be cited in a Result when they appear only in the claims text shown in the notebook. I cited them only that way.
8. Changing markdown after a run means a full re-run (about 26 min) to keep the executed copy matching the committed notebook. I re-ran.

## 4. Runtime and failures

- **Runtime.** The run took about 2 h 30 min (18:25 to 20:51 UTC). The main notebook runs in about 9 min and the decoding notebook in about 16 min, over the 10-minute aim but under the 60-minute limit.
- **Fixed along the way:**
  - The first decoding run failed on an identity-label dtype.
  - The exact Ring noise-correlation method took 17 min until I changed it to one neighbour sort per session.
- **Not fixed:**
  - The harness left an empty `entries/000620-watters-2026/.claude/` directory, and removing it needed a permission that was denied.
  - An untracked `scripts` device node at the repo root predates the run; I left it alone.
