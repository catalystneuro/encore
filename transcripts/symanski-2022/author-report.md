I've finished steps 1 to 5 of the Author protocol and run the handover (step 6). The notebook runs clean from a fresh environment in 30 minutes. Its printed output matches, line for line, the development pass the conclusions were written from.

## 1. Outcomes (47 claims)

| Outcome | Claims |
|---|---|
| Reproduced (18) | fig1b, fig1c, fig2d-beta-power, fig2e-beta-coherence, fig2e-beta-coherence-odor-vs-reward, fig2f, fig2s1f, fig3s1c, fig5d, fig5s1de, fig5s1fh, fig5e, fig5f, fig5s2, fig7-field-counts, fig7s1b, fig7f, fig7s1f |
| Partially reproduced (11) | fig1d, fig2e-rr-coherence, fig2d-power-odor-vs-reward, fig2s2d, unit-counts, fig3-selective-fraction, fig3ij, fig5c, fig5gh, fig5-rr-more-than-beta, fig7b |
| Not reproduced (9) | fig2d-rr-power, fig4c, fig4d, fig6d, fig6c, fig7c, fig7s1e, fig7d, fig7e |
| Blocked, data missing (3) | fig1s1e (no thermocouple signal), fig1s1f and fig2g (no air-only sessions) |
| Blocked, methods underspecified (6) | fig2e-rr-coherence-odor-vs-reward, fig2de and fig2s1e (the two readings the criterion names give different outcomes); fig3s1e and fig6e-glm (the paper's two readings differ here); fig6e-with-interneurons (depends on the blocked fig6e-glm) |

## 2. The dataset, assumptions and questions

**Dataset.** I pinned version 0.250815.1203. The paper cites no version, and the two published versions hold identical assets (same IDs and sizes), differing only in metadata.
- **Unit regions are encoded wrongly.** The units table's `electrodes` column holds tetrode numbers, not rows of the electrode table. Read as rows (the NWB default), 131 units land on OB tetrodes, which had no units. Read as tetrode numbers, the files give 915 CA1 and 508 PFC units, close to the paper's 934 and 508 active units.
- **Only the active units are deposited.** The paper recorded 1,309 CA1 and 717 PFC units; the dataset does not say it holds a subset.
- **Missing from the trial table:** odor identity and chosen well. I read the side from position, which agrees with the rewarded well on 99.85% of rewarded trials, and inferred the odor from it.
- **Missing altogether:** spike waveforms (so interneurons are typed by firing rate alone), the thermocouple, the air-only sessions and the sleep epochs.
- **Smaller problems:**
  - Electrode group names and labels disagree in every file.
  - The LFP is stored twice per file, which doubles the dataset to 95 GB.
  - Position in CS39 session 02 is on a different scale from the other CS39 days.
  - Four CS42 trials end after the last LFP sample.
- **What matches the paper:** the files hold 3,174 rewarded trials, exactly the paper's count of odor-cued correct trials, and 26 long-maze sessions from 6 rats.

**Assumptions** (marked `assumed` where they bear on an outcome):
- I estimated the epoch mean and s.d. used for z-scoring and the ripple threshold from 120 s of random windows per day, because reading whole recordings would not fit the time limit.
- The filters are Butterworth (order 2 for beta and RR, 4 for ripples); the paper gives no order.
- The T-maze linearization is my own construction.
- For the GLM, a session needs at least one qualifying cell; the paper gives no minimum.

**Questions for the paper's authors** are recorded as two `methods_unavailable` findings. They ask which pipeline and which statistical test produced each Figure 2 panel, the windows and frequency range for the theta shift, the SI definition behind Figure 3i-j, the GLM window alignment and minimum ensemble size, the z-scoring period, the filter order, and the epochs used for the interneuron rate.

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. When one reading gives "partial" and the other "not reproduced", it is unclear whether the readings "differ". I treated a difference in degree as a difference and blocked (fig2e-rr-coherence-odor-vs-reward).
2. Several criteria give no rule for a partial result (fig2d-rr, fig2s2d, fig5-rr-more-than-beta). I used partially reproduced when the main effect held in part, and not reproduced otherwise.
3. For absence claims, the protocol says to judge on "the paper's test", but for fig2de the paper names two tests. I followed the claims file and blocked when the tests disagreed.
4. A claim that depends on a blocked claim is blocked even though its analysis ran (fig6e-with-interneurons). I reported its numbers in the notes.
5. The unit-counts note that "totals compare what was deposited" is ambiguous. I compared the deposited totals with the paper's active-unit counts.
6. The clock check for continuous LFP asks for label shifting, which would mean re-reading the LFP. I used a spike-time shift control (436 against 133 responsive units) plus task-locked LFP contrasts, and reported the LFP as consistent with a shared clock, not shown.
7. Monte Carlo noise can move results across p = 0.05 (fig5e bootstrap; the subsampling in fig2de). The protocol only says to fix seeds, so I also printed the spread over other seeds.
8. Expected values that the criterion does not judge (the fig5d counts) are recorded as measured and flagged in the notes.
9. Whole-file processing could not fit the time limit, and the protocol does not say whether that kind of approximation is a method choice. I recorded it as an assumption.
10. Contrary to the protocol's rule against saving data to disk, during development I cached the streamed LFP windows (6.8 GB) and the parsed sessions in the temp directory to iterate faster. The notebook itself streams everything.

## 4. Runtime and failures

The run took 01:10 to 03:35 UTC (about 2 h 25 min); the notebook alone takes 30 minutes. `entry.py check` reports 0 errors, the run passed, and the handover is in `executed/001539-symanski-2022/handover/`. Nothing failed in the final run; the bugs I hit during development were fixed before it. I made no commits.
