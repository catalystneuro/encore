**Verification report: Martel et al. 2025 (DANDI:001174), round 2**

The claims file lists 23 claims. The attempt record has 23 outcomes and 23 verification entries, one for each claim.

### 1. Outcomes and assumptions

I agree with all 23 stated outcomes:
- **Reproduced (8):** cell-counts, fig1d-rate-no-change, fig1e-ieicv-no-change, fig1f-amplitude-u-sma-spont-higher, fig1d-rate-m1-above-sma-u, fig3-synchronized-pairs-exist, fig3ab-synchrony-not-distance, fig3c-sync-no-condition-change.
- **Not reproduced (2):** zenodo-descriptors-link, fig1f-amplitude-m1-above-sma-u-task.
- **Blocked (13):** cells-tracked-18pct (metadata_insufficient); the six Fig. 2 and Fig. S1 claims (data_missing); fig4a, fig4b and fig4c (methods_underspecified); the two histology claims (other).
- fig4d-sequence-measures-vary is reproduced, which brings the reproduced count to 9 of 23.

No outcome is marked `assumed: true`, so there are no assumptions to judge.

Three outcomes need a comment:
- **fig4a and fig4b (blocked, methods_underspecified).** On the sweep evidence I agree: in reproduce_martel_2025 cell 13, no setting gives the paper's own Fig. 4D counts, even in the two task slices whose events match the paper's table. However, the criterion's own rule gives not_reproduced when every reading fails. The notes explain the departure ("Changed from not_reproduced after verification"), but the `deviations` do not list it as a departure from the criterion. They should.
- **fig4c (blocked).** I agree. The claims file names the code's double-counting step as the main method. Under that step, with the within-session and stratified tests, every reading finds no difference. With the pooled test of reading (ii), the readings disagree. So the claim is blocked under either test choice. The notes rest the blocking mainly on the documented-dedupe variant. They would be stronger if they said that the pooled test and the within-session test of reading (ii) disagree, and that the within-session test was chosen after verification.
- **Histology (blocked_by: other).** The author says the protocol does list not_runnable, contrary to my round-1 point. I cannot see the protocol. "other" is reasonable for both histology claims.

### 2. Sentences the printed outputs do not support

Almost all conclusion sentences match the printed outputs, including the per-session tables, the sweep and the fig4c tests. The exceptions:

- **reproduce_martel_2025 cell 57, Summary:** "The paper's Jaccard and Figure 4D tables count fewer cells than the dandiset has in four sessions."
  - That holds for the Jaccard table (cell 45).
  - The Figure 4D table has fewer cells in three sessions only (sequences cell 18). V 2023-03-09 has 11 in both. The attempt record's `selection_undocumented` finding states this correctly.
- **sequences cell 25, Summary:** lists Q 2022-10-03 and Q 2022-12-01 only. It leaves out V 2023-03-16 (table 13, dandiset 14; cell 18). This is incomplete rather than wrong.
- **reproduce cell 40 and the attempt record's notes:** "Most of the gap comes from U SMA 2023-03-07 and 2023-03-14."
  - By the SMA task median this holds: 3.193 falls to 3.133, against the table's 3.124 (cells 34–36).
  - By the p-value it does not: 0.099 falls to 0.041, against the table's 0.014, which is less than half the gap on a log scale.
  - The wording should say which measure it means.
- **Attempt record finding `other`:** "consistent with events lost when they were put on the frame grid." No output shows this mechanism. Cell 13 shows only that one-frame IEIs are rarer (3.9% against 11.9%). Cell 15's weaker wording ("events missing from the dandiset's event arrays") is supported.
- **README:** "About twenty-two minutes" for the sequences notebook. The printed timings alone add up to 632 + 246 + 685 s, about 26 minutes (cells 5, 9, 13).

**My round-1 reasons in the attempt record.** The `verifications` entries give them faithfully and in substance, with the problems and could-not-check items attached to the relevant claims. The `outcome` values are mine, including not_reproduced for fig4a and fig4b. The one point the author disputes, the not_runnable reason for histology, is answered in the response.

### 3. Round-1 points

**Resolved:**
- **P1, cell-counts.** The notes and cell 18 now say that reading (i) compares the paper's table with its text.
- **P2, the two U SMA sessions.** Cell 14 shows they are not a swap of conditions. Cell 36 reruns the tests without them: fig1f-u-sma gives p = 0.0078, and the rate tests give p = 1.9e-05 and 2e-06.
- **P3, TTL check.** Cell 8 now opens all 45 files and lists variableMeasured for all assets.
- **P4, sweep.** 32 settings were run; fig4a and fig4b are now blocked (see section 1).
- **P6, fig4c reading (ii).** It is now tested within each session and stratified by session (cell 23).
- **P9, chance level.** Cells 47–48 list the eight SMA session-conditions at or below 0.05.
- **P10, extra cells.** Recorded as the `selection_undocumented` finding.
- **P8 and P11.** Recorded as deviations.
- **Could-not-check items now checked:**
  - `roi_ids`: 0..n-1 in all 45 files.
  - The two U SMA sessions.
  - The Zenodo aligned-activity table: the classification was run on it in cell 42.
  - fig4c by session.
  - The fig4a and fig4b parameter sweep.

**Remaining, where it bears on a conclusion:**
- **fig4c.** The outcome turns on the double-counting step. sequences.py and the `code_mismatch` finding say the MATLAB step writes 2 into a logical array and so removes nothing. I still cannot see identify_sequences.m to confirm this. If it is confirmed, and the within-session test is accepted as the reading, every reading agrees and fig4c would be reproduced. If the step works as its comments describe, the stratified tests find sequence pairs closer (permutation p = 0.0025 and 0.0105) and the claim stays blocked.
- **fig1f-amplitude-m1-above-sma-u-task.** The outcome stands on the claims file's method. It is decided by two U SMA sessions whose deposited events appear to come from a different event detection: without them, p = 0.041 uncorrected and q = 0.082. A finding records this. The outcome reflects the deposit, not the paper's analysis.

**Remaining, not affecting a conclusion:**
- **Fig. 2 check (cell 42).** Method Z run on the paper's own z-scored windows gives 20 modulated Q SMA cells, against the paper's 43. The class split is 14 direction-related and 6 not, against 32 and 11. For U M1 at target onset it gives 6 modulated and 3 direction-related, against 4 and 0. This suggests the claims file's method Z is not the paper's procedure. The six claims are blocked as data_missing anyway, but no finding or question records the mismatch, and one should.
- **permfun.R** (joined series or each part shifted) is still unverified by me. Agreement with the paper's Jaccard table is good: r = 0.950.

I found no place where the claims file misreads the paper. One related point: the Figure 4D table gives n.a. for Q 2022-09-15's first spontaneous 10 min and 13 for its second, but the deposited spontaneous file of that session lasts only 10 min. So the spontaneous half of fig4a may not be testable on the dandiset at all. The `paper_inconsistency` finding records this.
