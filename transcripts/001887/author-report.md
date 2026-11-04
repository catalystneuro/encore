I finished steps 1 to 6 of the Author protocol for DANDI:001887. `tools/entry.py check` reports 0 errors, the notebook ran from a clean environment in 30.1 min (limit 60), and the handover is built in `executed/001887-gabriel-2025/handover/`. Nothing is committed.

The main finding is that dandiset 001887 holds no calcium imaging, so every claim was tested on the paper's own Zenodo record of analysed data (doi:10.5281/zenodo.13381210, which the paper's Methods name). Those claims are counted apart from the dandiset.

**1. Outcomes** (43 claims: 42 from the claims file plus one link claim I added)

| Claim | Outcome |
|---|---|
| zenodo-dandiset-link (added) | partially reproduced (25 of 30 sessions) |
| data-neurons | reproduced (1394, 847, 1031, 967: exact) |
| data-registered-cells, fig1o-tone-to-mixed, fig1o-nonmod-to-mixed | blocked, data_missing |
| fig1e, fig1f, fig1g | reproduced |
| fig1h-latency | reproduced (assumed: corrected tone times) |
| fig1kl-overall-encoding-similar | blocked, methods_underspecified |
| fig1kl-day1-categories-similar | not reproduced |
| disc-tone-cells-baseline | blocked, methods_underspecified |
| fig1k-mixed-day2 | not reproduced (24.5% against 32.1%; paper 51% against 25%) |
| fig1p-platform-exit-excited-day2 | partially reproduced (p = 0.044, but 77/84 cells against 104/100) |
| fig1q, fig1pq, figs1h | reproduced |
| fig1r-mixed-exit-day1 | reproduced (assumed: reading M2) |
| figs2-innate-behaviors | blocked, not_runnable |
| fig2-day1-tone-stronger, fig2f | reproduced |
| fig2-day2-tone-further | reproduced (assumed: reading H1) |
| fig2e-modulation-entries | not reproduced (p = 0.086) |
| fig3a-decoding-shock-gt-ns, fig3a-decoding-before-tone | reproduced (assumed: the Methods' F1 coding) |
| fig3a-decoding-peak-preshock | not reproduced (peak at 32.6 s, in the shock epoch) |
| fig3b-feature-cells-enhance | not reproduced (assumed: the Methods' F1 coding) |
| fig3c-nonmod-cells-worsen | blocked, methods_underspecified |
| fig4b-hybrid-model-best | reproduced |
| figs3gh-behavior-similar | reproduced |
| 13 CILDS claims (fig4e to fig4l, figs3ab, cd, ef, figs4ab, cd) | blocked, not_runnable (CILDS is MATLAB only) |

**2. What was found about the dataset**
- **What it holds:** the 30 NWB files hold no imaging. They hold trial tables, external videos, and behaviour labels for only F1 and F2 on day 1.
- **Errors in the files:**
  - F7's day 2 file was converted from M7's session file (identical trial table, 12 shocks for a non-shocked mouse).
  - F3 day 1 (non-shocked) lists 9 shock trials.
  - F1 and F2 give the conversion date (2026-08-25) as the session start time.
- **Zenodo record:** it has 9 and 7 mice on day 1 and 7 and 7 on day 2, where the paper reports 11, 9, 8 and 8. It has no cell registration and no jumping or rearing labels.
- **Tone timing:** the paper's code places tones at 25 frames/s, but in six sessions (F5, M5, F6 on both days) the camera ran at 28 to 30 frames/s, so the tone windows drift. Placed by the camera timestamps instead, the success rule agrees with the hand-scored outcomes on 56 of 60 trials, against 45 with the paper's windows. I used the timestamp windows throughout and showed the paper's as a variant.
- **Assumptions** (marked `assumed: true`):
  - fig1h: the timestamp-placed tone windows.
  - fig1r: reading M2, the code's split of mixed cells.
  - fig2-day2: H1, cells pooled as in the cumulative histograms.
  - fig3a, fig3a-before-tone, fig3b: the Methods' decoding coding (success as positive class, min-max normalised F1). The Methods take precedence over the code; under the code's coding the fig3a result fails.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Which frames make up the BL, D1 and D2 periods, and what does the unpublished ROC routine do?
  - How is a mixed cell counted to give 51% against 25%?
  - Which class is positive in the decoding F1, how is F1 normalised, and what is in the unpublished file of decoding cell sets?
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. All claims defaulted to `data: dataset`, but the data sit in another public archive. I added `data: elsewhere` and `where` to 39 claims and added one link claim. No statement, expected value or criterion changed. The protocol does not say whether the author may set `data`.
2. A link claim is meant for matching outside data to the dataset. Here no tested claim needs a match, so I added one anyway to report whether the dandiset is the paper's data; no claim depends on it.
3. The protocol contradicts itself on criterion readings that disagree: reader step 3 says "reproduced under any reading", author step 1.6 says adopt one reading or block. Where the claims file says disagreeing readings mean methods_underspecified, I followed it. Otherwise I adopted the reading the paper best supports, marked as an assumption.
4. The protocol does not say whether a tone-time correction the data force counts as an assumption. I marked it as one only where the outcome depends on it (fig1h).
5. The clock check could not be shown for the calcium: the population response to the shock is too small. I reported the calcium clock as consistent with the timestamps, not shown.

**4. Runtime and failures**
- About 2 h 55 min to the handover (01:38 to 04:33 UTC).
- My first decoding run used a process pool and hung until the 60-minute command timeout, losing an hour. Decoding now runs sequentially and takes 15 of the notebook's 30 minutes.
- Zenodo throttles single streams to about 1 MB/s, so the helper fetches each file in parallel byte ranges (about 30 MB/s).
- For development only, I cached reduced arrays in `$TMPDIR`. The entry streams everything.
- Device-node entries (`.bashrc`, `scripts` and others) in the repository root come from the sandbox, not from me.

Files are in `entries/001887-gabriel-2025/`:
- reproduce_gabriel_2025.ipynb
- pma.py
- entry.yaml
- requirements.in
- requirements.lock.txt
- README.md

Also changed: `attempts/001887-gabriel-2025-01.yaml` (new) and `claims/001887/10.1016-j.cub.2025.01.010.yaml` (edited).
