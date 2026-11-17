I've finished steps 1 to 6 for `entries/dijk-2018`. The entry check passes with 0 errors, the clean run passes (275 s, peak memory about 0.25 GB), and the handover package is built in `executed/dijk-2018/handover/`. Nothing is committed. The record is `attempts/dijk-2018-01.yaml`.

**1. Outcomes (44 claims: 22 reproduced, 5 partially reproduced, 13 not reproduced, 4 blocked)**

| Outcome | Claims |
|---|---|
| Reproduced | fig1b-stability-dg-below-ca-removal, fig1-rate-remapping-no-difference, fig1c-field-rate-change-no-difference (a), speed-no-difference (a), fig3c-stability-no-difference (a), fig3c-replication-vs-relocation (a), fig3c-stability-vs-environment, fig4b-room-preference-pretraining (a), fig4c-ipos-before-avoidance, fig4d-room-maps-uncorrelated (a), figs2a-pc-pairs-no-change, standardized-rates-no-difference (a), overdispersion-similar (a), network-consistency-overall (a), fig5d1-pc-int-tau-no-difference, fig5d2-pc-int-change-relocation (a), figs2bc-other-timescales (a), fig5d3-independent-pairs-increase (a), fig5d4-positive-pairs-decrease (a), correlation-not-speed, fig6c-no-increase-before-errors, fig6-inset-rate-changes (a) |
| Partially reproduced | tables1-dg-ca-similar, fig3b-avoidance-learning, fig3d-rate-remapping-task (a), fig4d-room-ipos-near-active-zone, pc-int-fraction-increased (a) |
| Not reproduced | fig1-single-field-proportion (a), fig1-field-number-scaling (a), fig3b-shock-off-avoidance, tables2-firing-quality-similar, interneuron-rate-remapping (a), ipos-speed-correlation, fig5b-network-consistency-zones, pc-int-pair-classes, negative-pairs-no-change (a), fig5e1-correlation-near-zone, fig5e2-e4-change-near-zone, fig5e1-inset-rate-change-near-zone, fig6b-correlation-before-avoidance |
| Blocked, data missing | fig2c-cfos-reduced, fig2d-conflict-deficit, fig2-quadrant-preference, fig2e-shock-off-deficit (the optogenetic mice are not in the data set) |

(a) means the outcome rests on an assumption (`assumed: true`).

**2. Dataset, assumptions and questions**

- **Version:** hc-17 has one published copy, under `live/` (`data.zip`, MD5 b577c885…). It is recorded as `unversioned`, and the header says why.
- **What matches the paper:** the data set's Excel cell lists give exactly the paper's counts (45 DG and 20 CA place cells; 42 DG place cells and 21 interneurons in 6 mice). The pair totals also match (152 place cell-interneuron and 133 place cell pairs). The speed test gives F(2,13) = 1.94, p = 0.18, the paper's df and values.
- **Findings about the data:**
  - The optogenetic experiments of Figure 2 are not in the data set.
  - Sessions are missing: WT15, WT16 and WT19 have no second pretraining session, and WT16 has no training 1 recording.
  - One environment session (140731_WT15_testbox2) repeats the positions of testbox1, with two of its four units identical. I counted it once.
  - The shock-off recordings of WT15 and WT16 log shocks.
  - For WT15, WT16 and WT19 the conflict zone is 170° from the training zone, not the 180° the paper states.
  - The descriptor says the maps are 256 x 256; they are 32 x 32.
  - The smoothed maps (`RmSm`/`ArSm`) and the file variants (`_4`, `.times`, `0spks`) are not described, and one file is misnamed.
  - WT19's pretraining session lasts 30 min, not 20.
  - Table S1 and S2 values labelled bits/s match bits per spike in these data.
- **Assumptions adopted** (every alternative reading is also run in the notebook):
  - Rate maps on the data set's own 8-pixel grid.
  - Session pairs for the shock manipulations (M11 in the claims file): every pretraining-training pair for shock addition, and both training sessions against conflict for relocation. This rests on the paper's sentence that these analyses "used data collected during both the training 1 and training 2 sessions".
  - Positional information on 8-pixel locations.
  - Consecutive 5-s episodes for overdispersion and network consistency.
  - Pair classes from Kendall's own test on both pretraining sessions joined.
  - A unit keeps its tetrode and cluster name across the sessions of a day.
- **Questions for the authors** (recorded as three `methods_unavailable` findings): the place field definition and map smoothing; which session pairs form the manipulations; the Ipos location size; the 5-s episodes; and the test used to class correlated pairs.
- **Questions to a reader:** none.

**3. Where the protocol was unclear or did not fit**

1. CRCNS has no versions to pin. I recorded `unversioned` and the MD5 sum, as archives.md says.
2. The clock check expects trial tables, but these sessions are continuous. I compared split-half rate maps against positions shifted by 60 s. The check passes in 80 of 82 sessions, and I named the 2 where it could not be shown.
3. Two rules conflict. Reader step 3 says a claim is reproduced if any reading the criterion lists matches; author step 1.6 says to adopt the best-supported reading. For fig3b-avoidance-learning the criterion lists two readings but says only one fits the paper's df. I judged on that one and marked the claim partially reproduced.
4. The protocol does not say what happens to claims that depend on a not-reproduced claim (it only covers blocked ones). I tested the class-dependent claims under an adopted class reading.
5. Several criteria are pass or fail, but only part of the claim holds. I used `partially_reproduced` for those.
6. The protocol says to count duplicated recordings once, but here the duplicate was only partial (same positions, half the units identical). I dropped the later copy.
7. JMP's Kenward-Roger df and mixed-model Fisher's LSD cannot be rebuilt in Python. I used Wald F tests, with paired or pooled-error LSD, and stated this as a deviation.

**4. Runtime and failures**

The run took from 02:34 to about 03:42 UTC. The notebook runs in 4.6 min. Nothing failed in the final run. During development I fixed a few bugs: a misnamed file that broke the parser, singular mixed-model fits, and an LSD computed on an empty group.
