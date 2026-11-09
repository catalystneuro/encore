**Round 2 verifier report: Eyherabide et al. (2008) on CRCNS ia-1, attempt crcns-ia-1-eyherabide-2008-01**

Counts come from the claims file and the attempt record: 26 claims and 26 outcomes. Of these, 9 are reproduced, 6 partially reproduced, 8 not reproduced and 3 blocked (data_missing). 20 outcomes carry `assumed: true`.

## 1. Outcomes and assumptions

I agree with 25 of the 26 outcomes. I disagree with one.

**table1-bursting-sessions (partially_reproduced, assumed): I disagree; it should be not_reproduced.**
- Under selection (c) the counts are 40/47, 1/6, 7/7, 6/7, 7/8, 3/7, 0/7, so 6 of 7 are within tolerance (cell 21).
- Selection (c) drops off-line sorted sessions, and nothing in the paper supports that (`grep` of `paper/` finds no mention). Cell 7 says the exclusion "is taken because, with it, the kept sessions per protocol and the bursting sessions per protocol come close to Table 1". So the selection was tuned on this claim's own expected values.
- The record does not credit (c) for table1-sessions-per-protocol or data-sessions-and-trials ("chosen in part from these counts"), yet credits it here. That is inconsistent.
- Under every selection the criterion supports (a: 2 of 7; b: 2 of 7), the outcome is not reproduced. Selection (c) should be shown as a variant.

**The other outcomes I agree with.** Notes on their assumptions:
- **Selection (c) as an assumption.** It is stated in every affected outcome. As a population for the downstream claims it is a reasonable sensitivity choice, and almost every downstream outcome is the same under selection (a), as the record shows. Its trial exclusion has a textual basis (Methods: "N ranging between 98 and 503"); its off-line exclusion does not.
- **data-sessions-and-trials (assumed: one animal per date; 122 as "recorded").** Both assumptions are stated and reasonable.
- **fig8-latency-decreases (reproduced, assumed).** This rests on reading (b) and on searching for the maximum before onset. Both are stated. "No negative tau_n" holds by construction, because the search ends at 0. In 13 of the 53 sessions, 17 τ_n values sit exactly on the 0 ms edge (cell 65: printed -0.00). The mean τ_4 of 2.67 ms includes those clipped values. The mean still decreases under both searches, so the outcome stands, but the record should say this.
- **fig7ab-information-per-burst-increases (partially_reproduced).** This follows the criterion's plug-in formula, as stated.
- **fig3, method-correlation-error, fig9, fig7ef.** The assumptions are stated and reasonable: prominence 0.2; τ=0 left out of the span; mean subtracted in Eq. 15; event reading (b).
- **firing-rate-uniform, table1-isolated-spikes, table1-burst-length.** Each carries an "Assumed because…" selection deviation but no `assumed: true` flag. Each outcome holds under every population, so no flag is needed, but the wording is inconsistent.

## 2. Text against outputs

These statements are not supported by the printed numbers:

- **Cell 11, and the data-sessions-and-trials notes:** selection (c) "keeps 89 sessions … all within tolerance" / "every value within tolerance". Cell 10 prints 29 cells and 18 dates for kept (c), against 37 ± 3.7 and 23 ± 2.3. The claim holds only if cells and animals are counted over all sessions, and the text should say so.
- **Cell 46, the fig7ab notes and the Summary:** "The rise of I_n(1) with n … is therefore accounted for by the bias of that estimate"; Summary: "so that rise is estimator bias".
  - A train whose onsets are shifted has lost its stimulus locking. Its rate is spread over more bins, so its plug-in bias is at least that of the locked data.
  - "Shifted slope > data slope" (2.59 against 2.22; data higher in 3/64) therefore shows that the bias is as large as the rise. It does not show that the whole rise is bias.
  - "Is of the order of the bias" is what cells 45 and 54 support. Cell 55's "a large part of these rates is estimator bias" is acceptable.
- **Summary, dataset bullet:** "the STA peaks 5.6 ms (median) before the spike in every session". Cell 6 prints a latency range of "-0.0 to 9.95", so in at least one session the maximum sits at 0.
- **Summary, Population bullet:** "Selection (c) is the population from table1-bursting-sessions on". Cell 17 and the record already use (c) as the main population for firing-rate-uniform.
- **fig8-latency notes and cell 66:** "with no negative tau_n" is true only by construction (see section 1).
- **Cell 78 and the fig9c notes:** "7 bursting protocol-5 sessions …, the paper's seven cells". The notebook does not show that the 7 sessions come from 7 distinct cells: 03-04-23-aa and 03-04-23-ah are on the same date.

I checked every other number in the "**Result:**" cells, the Summary, the README and the record notes against cells 3–84 and found them correct. That includes the record's new fig10 note that the flag differs in 2 sessions "one each way", which matches the side-by-side table in cell 80.

**My round-1 reasons in the record.** The `verifications` entries give my round-1 reasons close to verbatim. The problem numbers are attached to the matching claims, and the reasons are faithful. One omission: under fig8-nbta-differ the record quotes problem 7 without my label that it does not affect a conclusion.

## 3. Round-1 points

**Resolved:**
- **3 (minimum bursts):** stated as an assumption, and results at 20 and 50 bursts are shown.
- **4 (size bias of σ_n):** a size-matched control (94.3%, ratio 1.517) and per-n ratios were added.
- **5 (peak reading a):** reading (c) was added; 61 of 89 sessions burst.
- **7 (ANOVA):** acknowledged in the text.
- **8 (fig10 identical counts):** explained in cell 80.
- **9 (prominence):** the outcome is marked as resting on it.
- **10 (trial blocks):** checked in cell 3; `firing_rates` read.

**Partly resolved:**
- **1 (selection):** the exclusions were tried and tabulated. Using selection (c) for table1-bursting-sessions makes that outcome circular (section 1).
- **2 (τ search):** the before-onset reading was added and fig10 was re-run (still not reproduced). The maximum is clipped at 0 in 13 of 53 sessions, so the nBTA peak for n = 3–4 still falls at or after onset in a quarter of the sessions.
- **6 (bias):** the baseline was added. The conclusion drawn from it goes further than the comparison supports.

**What remains that bears on a conclusion:**
- **table1-bursting-sessions:** the outcome rests on a selection fitted to Table 1. It should be not_reproduced, consistent with table1-sessions-per-protocol.
- **fig8-latency-decreases:** reproduced, but the record should state the 13 sessions clipped at τ = 0. A count of sessions with τ_1 > τ_2 > τ_3 among unclipped values would settle how much of the decrease the clipping forces.

The claims file: in the passages I checked this round (Methods, Electrophysiology paragraphs 4–5), I found no misreading.
