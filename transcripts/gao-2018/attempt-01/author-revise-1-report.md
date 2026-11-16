I've worked through every point in the round-1 report, and six outcomes changed. I re-ran the entry with `python tools/entry.py all entries/gao-2018`: the check found 0 errors and the notebook ran from a clean environment in 320 s. The conclusions match the new numbers, and the round is recorded under `verifications` with all 45 claims.

**Outcome changes (all after round 1, so allowed):**

| Claim | Was | Now | Why |
|---|---|---|---|
| fig2cd-selectivity-emerges-gradually | blocked, methods underspecified | partially reproduced | Agrees with the verifier. The paper says the epoch that fixes each neuron's preference doesn't matter, but the response-epoch peak appears with only one of the three epochs. |
| fig3d-alm-altered-by-cn-inhibition | partially reproduced | not reproduced | Agrees. The data hold more neurons than the paper, so the count is judged. Both the count (270) and the latency (14.1 to 22.3 ms) miss. |
| fig3e-alm-increase-decrease | reproduced | partially reproduced | Agrees. The counts (158 and 112) miss; only the increase fraction (0.585) matches. |
| cd-captures-selectivity | reproduced | partially reproduced | Agrees. Under the notebook's chosen reading the selectivity matches (62.1%) but the variance doesn't (34.2%). |

The totals are now 9 reproduced, 6 partially reproduced, 4 not reproduced and 26 blocked.

**Disagreements kept and recorded:**
- **fig3e-alm-mean-rate-unchanged** stays partially reproduced. The "no change" part holds by the unpaired test (p = 0.214). The rate level misses, and that level depends on which neurons are counted: the files hold many slow neurons.
- **fig4-fastigial-activation-alm-latency** stays partially reproduced. The fast latency holds (2.07 ms by bin start); only the count of modulated neurons misses.

**Corrected or added:**
- **A bug, found while checking B1:** the last 127 trials of BAYLORCD8 20171020 (120 of them without an early lick) come after its units' recording ends and hold no spikes. The first run counted them as silent trials. They are now left out of the neural analyses and recorded as a finding. Only the photo-inhibition numbers moved.
- **Why the files hold more neurons (B1):** the data check now prints every units-table column and every group in the files. There is no quality or isolation field, the acquisition and processing groups are empty (so no lick channel), and the paper gives no per-session counts. Rate figures show how many slow neurons the files hold.
- **fig3f, repeated over 20 random draws (B2):** in the last 500 ms the criterion is met in 15 of 20 draws with 5 preference trials of each type, and 13 of 20 with 10 of each. It stays reproduced, and is no longer marked as resting on an assumption.
- **fig2cd, held-out selection (B4):** selecting neurons on one half of the trials and measuring on the other gives the same pattern.
- **fig4f and fig4g (B5):** a variant tests lick-right and lick-left trials separately, and a comparison with a single pre-onset bin is added. fig4f still holds. Much of the late dentate effect in fig4g follows the mix of lick directions, but the outcome stays not reproduced on the claims file's readings.
- **When the photo-inhibition effect starts (B6):** a per-code time course shows the ALM change starting about 30 ms after delay onset for CN photo-inhibition, against 4 ms for fastigial photo-activation. A time course of the two inhibition codes over the delay is also added.
- **Sensitivity run (B9):** dropping the five sessions that failed the clock check changes no outcome. One thing to know: without them, the fig3d bootstrap latency falls to 9.9 ms, inside tolerance. The count still misses and the observed onset stays at 25 ms, so the outcome holds, but that latency is fragile.
- **fig1l early licks (B10):** now tested, with no change (two-sided p = 0.59). The claim stays blocked because lick rates and video aren't in the files.
- **Smaller additions:** a check that early-lick trials keep their stimulation code. Text that wrongly said the fraction is judged when the data hold more neurons is corrected in the record and the notebook summary.

**Not done:**
- No questions for a reader were filed. The verifier didn't report a place where the claims file misreads the paper; its question about single-trial versus averaged variance is a gap in the paper itself.
- I didn't run `handover`, since round 2 gets the full executed notebook.
- I didn't commit, and I left alone the change to `tools/entry.py` and the untracked dotfiles and `scripts/` in the repository root; none of them are mine.
