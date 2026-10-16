**Verifier report, round 2: attempt 000114-carcea-2021-01**

**1. Outcomes**

The claims file has 19 claims and the attempt record has 19 outcomes. I agree with all 19 under the claims-file criteria:

- **Reproduced (1):** label-link.
- **Partially reproduced (3):** ed7a-nest-entry-fraction, ed7a-dam-retrieval-fraction, fig1j-shepherding-rate.
- **Not reproduced (3):** ed7a-shepherding-fraction, fig2j-shepherded-entry, ed8a-dam-retrieval-rate.
- **Blocked, data missing (10):** ot-pvn-units, ed6-dam-vs-pup, fig1cd-retrieval-onset, fig2a-dreadd, fig3fg-observational-learning, fig3ij-observation-units, fig4c-ac-photometry, fig4f-pvn-ac-correlation, fig4jk-oxytocin-in-ac, ed9-colliculus.
- **Blocked, metadata insufficient (2):** fig2f-virgin-chasing, fig4i-projection-photometry.

Three of these depend on a choice the criterion makes, and a variant in the notebook would change them:

- **ed7a-nest-entry-fraction:** cell 21 drops the 20 units above the code's own limit of 1,048,500 spikes and gets 42/174 = 24.1%. That is inside both tolerances (23.9–29.2 and 23.6–28.8), so this variant would reproduce.
- **fig2j-shepherded-entry:** cell 30 leaves out V116 03102018 and gets a median difference of 10.8 with p = 0.0237. That meets the criterion's test, so this variant would reproduce.
- **ed7a-dam-retrieval-fraction:** see 3a below.

**2. Sentences the outputs do not support**

- **Cell 34, fig1j conclusion:** "so the low rate does not come from sessions scored only in part." Cell 9 shows only that annotations of *any* label span each session, and most of those are "Mother in nest". Cell 10 itself says this "does not show that every event in a session was annotated." The record's notes ("consistent with sessions scored in full") are worded correctly.
- **Cell 44, Summary:** "The draft holds the same spike times, events and series as the pinned version in all 30 files." Cell 15 compares only the shape and rate of the ecephys series, not the voltage values. Cell 0 makes the same claim ("compares the spike times, events and series of every draft file").
- **Cell 37 and the ed8a notes:** "close to the 0.17 per hour the paper gives for singly housed dams." The legend of Extended Data Fig. 8a (saved under `paper/PMC8387235.txt`) gives 0.2 ± 0.1 events/h (N = 5). The value 0.17 is hard-coded in cell 36 and I could not find it in the paper text. The Source Data were not available to me.
- **Record, label-link notes:** "but 9.9% in V116 and 0 of 3 in V118, where the label marks dwells with medians of 1103.7 to 2492.7 s." The V118 median is 64.1 s (cell 17). Cell 18 correctly limits the statement to V116.
- **Cell 22 and the record's nest-entry notes:** "most in V116 03092018 (16 of 29 overlap shepherding)." By count, V110 has the most overlaps (20 of 72, cell 21). The sentence holds only as a proportion.
- **Record, fig1j response:** "end at or after the recording's end except V118 03192018 (9.89 against 10.50 h)." Three V116 sessions also end 0.01–0.02 h early (cell 9). Cell 10 says "within 0.6 h", but V118 03192018 is 0.61 h short.
- **README:** "It takes about two minutes." Cell 45 prints 190 s.
- **Cell 0 (introduction):** "sorted units for four of them in 8 of 17 files." Cells 1 and 3 show 14 ecephys files.
- **Omission in the record's nest-entry notes and in cell 22:** both report 24.1% without saying it is inside both tolerances, although they do say this for the "V111 once" variant.

All other numbers in the conclusions, the Summary, the README table and the record notes match the printed outputs. The README's count of 10 data_missing and 2 metadata_insufficient claims also matches the record.

**Whether the record gives my round-1 reasons in my own words:** it does for 18 of the 19 claims. In the nest-entry reason, "V116 03102018 … holds 17 of 26 activations" reads as 17 of the 26 activated units. What I meant, and what cell 20 shows, is 17 of that session's 26 units. My round-1 wording was ambiguous too; "17 of its 26 units" would be correct.

**3. Round-1 points**

**Resolved:**
- **1 (empty episodes):** cells 21, 24 and 27 add the variant with empty episodes counted as 0, and a Poisson null at 1.0–2.3% activated. That null gives 12 suppressed of 132 for dam retrieval, which confirms the suppressed counts are unreliable.
- **2 (V111 03032018 independence):** the pairwise coincidence is now printed (median 71%). Even if the 9 units were one neuron, the result would be 5/124, Fisher p = 0.030, still partially reproduced.
- **3 (V111 counted three times):** variants are shown.
- **6 and 7 (the "Virgin in rest" split and the 40 s cap):** both are disclosed in the conclusions.
- **8–11:** these did not bear on conclusions.
- **Section C:** `unit_name` values, annotation coverage, the fig4i and fig2f outputs, baseline overlap, empty-episode counts and unit coincidence are all now printed. The draft comparison now covers all 30 files.

**Still bearing on a conclusion:**

a. **Dam retrieval in V111 03032018 may come from a silent baseline.** For the session's single episode, the median change over all 31 units is 98.1 (cell 27), while the session's median rate is 15.4 Hz (cell 5). That means most units were nearly silent in the 10 s baseline, which points to a gap in the recording or the spike sorting, not a response. If the 9 activated units there are an artifact, the result is about 4/123, p ≈ 0.06, and the outcome becomes not reproduced. Two outputs would settle it: the per-unit spike counts in the baseline and in the episode, and the population spike count in the 60 s around the episode.

b. **No shared clock (point 4) is still unresolved.** The fig2j outcome depends on keeping V116 03102018 (p = 0.0237 without it), and the nest-entry fraction falls to 14.9% without it.

c. **Coverage is shown only for all labels together (point 5, partly resolved).** The rate claims need coverage of shepherding and retrieval scoring specifically. The first and last times and the largest gap of the virgin labels and "Mom agressing" per session would test this. The cell 34 sentence should be softened until then.

d. **The 24.1% nest-entry variant should be stated as inside tolerance** in the notes and in cell 22.

e. **The 0.17/h comparison value for singly housed dams** should be sourced or replaced with the legend's 0.2 ± 0.1. This does not change the ed8a outcome.
