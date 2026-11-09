I finished steps 1 to 6 of the Author section (handover built), and the run took about 30 minutes (02:52 to 03:21 UTC). Of the 29 claims, 15 were tested: 5 reproduced, 5 partially reproduced and 5 not reproduced. The other 14 are blocked because the data the paper used for them is not in the dataset. `python tools/entry.py all` passes with 0 errors, and the notebook runs from a clean environment in 96 to 102 s. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| sessions-and-cells | not reproduced: 56 sessions and 1499 cells under the inclusion rule, against 63 and 1,692 |
| rules-learned | not reproduced: right arm 3 rats, lit 4, left 3, dark 1 (paper 4, 4, 2, 1) |
| learning-sessions | not reproduced: no reading gives 9 to 11 sessions over four rats |
| fig1b-signal-components | partially reproduced: 285 signal (out of tolerance), 730 nonsignal; per session the same as the paper |
| fig2b-post-greater-than-pre | reproduced: p < 0.005 in all three groups under all four readings |
| supp5-sws-only | partially reproduced (assumed): SWS effect p = 0.014, and non-SWS post > pre (p = 0.04) |
| supp6-pre-post-sws-alike | reproduced for SWS duration and firing rate; the LFP measures cannot be tested |
| fig2b-encoding-correlation | not reproduced: r² 0.38 to 0.42 against 0.61 (r itself is 0.62) |
| fig2b-pre-weaker | partially reproduced: the slope difference does not reach p < 1e-20 |
| fig2e-skewness | not reproduced |
| fig2f-tail-contribution | partially reproduced: 1 or 2 of 3 groups in range |
| supp10-no-coactivation | reproduced |
| supp11-shuffle-control | partially reproduced: the highest group differs between pre and post (p = 0.03) |
| fig6b-down-up | reproduced for the reactivation part (assumed); the SPWR part is not tested |
| supp12-behavior-unchanged | reproduced |
| supp8, fig5a to 5e, replay-in-delta, fig6a, fig6c, fig6d, fig7b, fig7b-controls, fig7c, fig7d (14 claims) | blocked: `data_missing` |

**2. The dataset, assumptions and questions**

- **What it holds.** One archive, `mPFC_Data.tar.gz`, with 86 sessions (rat 15, 14; rat 18, 14; rat 19, 11; rat 20, 47). There is no LFP, no ripple, delta-wave or spindle times, and no tetrode for each cell.
- **Session counts.** Under the paper's inclusion rule, rats 18 and 20 match the paper's per-rat counts exactly. Rat 19 has one session fewer, and rat 15 six fewer; the data set holds only 14 rat-15 sessions in total. Earlier in the run I said rat 19 matched too; that was wrong.
- **Learning sessions.** The data description lists 10 learning sessions from four rats, which matches the paper's count. Two of them (201227 and 201229) fail the paper's 4-minute SWS rule when measured with the dataset's own SWS intervals.
- **Other findings.** Sessions without SWS store a [0, 0] interval or an empty file. Cell types look implausible in 200107 (all unknown) and 200209 (all interneurons). In 5 sessions, spikes continue after the position record ends. Position units and the bounds of the rest epochs are not given.
- **Clock checks.** Position and spikes both decode the chosen arm better with the real trial times than with times shifted by 30 s. The spike check does not establish the clock in 18 sessions. All of this is recorded under `findings`.
- **Version.** CRCNS has no versions, so the version is recorded as `unversioned` and the archive is pinned by its MD5, which matches the bucket's ETag.
- **Assumptions:**
  - The rest epochs run from the start of the recording to the awake epoch, and from its end to the end of the position record. A 30-minute variant gives the same outcome for supp5.
  - For fig6b, "pre is lower" is compared over the window where the post rise is significant. Compared by the largest value, pre is not lower.
- **Questions for the paper's authors** (three `methods_unavailable` findings):
  - Is the z-transform taken over the whole rest epoch or over SWS bins only? Both were run, and no outcome changes.
  - How were the rest epochs bounded and DOWN states defined?
  - Which tests were used for Fig. 2b, 2e and Supp. 11D, and is 0.61 an r or an r²?
- **Questions to a reader:** none.

**3. Where the protocol was unclear**

1. `archives.md` describes opening a zip in place, but this dataset is a single tar.gz, which cannot be read by range requests. I streamed it in order, in memory, once per run (about 60 s).
2. Expected values that are only sample sizes, such as fig2b's group counts, conflict with a criterion that defines "reproduced" without them. I followed the criterion and recorded the counts mismatch as a deviation.
3. There is no rule for a claim where only some parts can be tested (supp6, fig6b). I based the outcome on the testable part and said so in the notes.
4. `measured` is defined only for when several readings match. When none matched, I recorded the paper-supported or first-listed reading and said which.
5. `depends_on` covers only blocked dependencies. fig1b and supp12 depend on claims that were not reproduced; I used the paper's stated rule and the data description's learning list, and recorded both as deviations.
6. For supp11 I computed the exact mean over all permutations instead of 1000 shuffles per bin. On one session it agrees with 1000 real shuffles (-0.0082 against -0.0086). This is recorded as a deviation.

**4. Runtime and failures**

The total was about 30 minutes, and nothing failed. Deleting `__pycache__` worked, but deleting the empty `.claude/` folder in the entry directory needed approval and was denied. It holds no files, so git ignores it. Untracked dotfiles at the repository root (`.bashrc`, `.idea`, `scripts` and others) were left alone.

Files are in `entries/crcns-pfc-6-peyrache-2009/`:
- reproduce_peyrache_2009.ipynb
- pfc6.py
- entry.yaml
- README.md
- requirements.in
- requirements.lock.txt

The attempt record is `attempts/crcns-pfc-6-peyrache-2009-01.yaml`.
