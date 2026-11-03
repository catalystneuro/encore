I tested 13 of the 35 claims on this dataset (including one I added) and blocked the other two; 21 claims on other archives' data were tested or blocked. The entry passes `entry.py all` with 0 errors (the notebook runs in about 3 minutes), and the handover package is built in `executed/001751-liu-2026/handover/`. The dataset alone can't test Fig. 5: its files have no cell types, connection labels or soma positions. Those come from a table in the paper's code (`metadata_multiPatch.xlsx`, AIC_proj at commit 44cd8a6), and that table's counts disagree with the paper's.

**1. Outcomes**

| Claim | Data | Outcome |
|---|---|---|
| code-table-link (added by me) | dataset + code's labels | reproduced |
| fig5d-connectivity-totals | same | not reproduced (26 connections against 31; 295 cells against 377; 1,416 pairs, within tolerance) |
| fig5-pc-to-pc | same | not reproduced (18 of 743 against 24 of 503) |
| fig5-ven-outputs-absent | same | not reproduced (the table marks one VEN-to-PC connection, with a 1 mV response in the data) |
| fig5-pc-to-ven | same | partially reproduced (1 connection as stated, but 145 pairs against 200) |
| fig5-pc-in | same | partially reproduced (2 and 4 connections as stated, but 84 and 86 pairs against 65) |
| fig5-in-to-ven-absent | same | reproduced |
| fig5i-ven-sparse-local-connectivity | same | partially reproduced (every VEN rate is lower, but no rate is within tolerance) |
| fig5fg-example-slice | same | reproduced |
| fig5-pair-distances | same | blocked: data missing |
| fig5-pc-rate-comparable-primate | with outside inputs | blocked: methods underspecified (its own criterion says so) |
| fig5b-psc-frequency, fig5c-psc-amplitude, fig3e-phase-peak-index, fig4j-eepsp-amplitude, ven-map-et-ct | elsewhere | reproduced |
| fig4d-sodium-current | elsewhere (DANDI:001750) | reproduced, resting on an assumption |
| fig8a-metabolite-gradient, fig8de-glycolytic-bias, fig6f-g-ven-subtype-mapping | elsewhere | partially reproduced |
| fig3c-ais-distance-length, patchseq-mapping | elsewhere | blocked: metadata insufficient |
| fig4j-eepsp-latency | elsewhere | blocked: other (the table has no latencies) |
| ven-firing-rate-variability | elsewhere | blocked: methods underspecified (its own criterion) |
| 11 others (sequencing reads, morphology, NEURON models, DANDI:001746) | elsewhere | blocked: other, not attempted |

**2. The dataset, assumptions and questions**
- **Version:** I pinned 0.260825.0222, the only published version; it has the same content as the draft.
- **Metadata errors:**
  - Responses are stated at 1 Hz; the data are at 25 kHz.
  - The stimulus rate unit is "millisecond".
  - The stimulus amplitude is stored as 2 "amperes"; the Methods say 2 nA.
  - Every file names Elec_8 as the stimulated electrode, but the cell that actually fires is on channel 8 in only 35 of 301 files.
  - Every file has the same placeholder start time, 2018-01-01.
- **Repeated recordings:** none found.
- **Code table against the files:**
  - 13 dandiset files are not in the table.
  - 6 pairs are listed twice and 7 cells have two different types.
  - 2 connections have projection labels that don't match their channels, and the stated connection count disagrees with the annotations in 4 of 52 slices.
- **Sweeps:** only 119 of 301 files have more than the 20 sweeps the Methods require.
- **Other code tables differ in size from the paper:** 23 eEPSP pairs (paper 26), 558 metabolites (581), 120 and 500 AIS values (108 and 430), 14 and 15 VEN subtypes (10 and 11).
- **Assumptions:**
  - fig4d: the peak current is taken 0.2 to 3 ms after the voltage step. With windows ending at 5 or 10 ms, p rises to 0.096.
  - fig4j: the table's rows are already the monosynaptic responses the Methods select.
- **Questions for the paper's authors** (recorded as findings): what rule decides a connection, and which pairs and cells make up the paper's 1,292 and 377; and which window and steps give the Na+ current peak.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. It doesn't say whether marking claims `data: with_labels` and adding `depends_on` counts as changing the claims file. I did both, as the claims file's header anticipated; statements, expected values and criteria are unchanged.
2. Connection annotations are expert judgements, not just names for codes, yet they had to be counted as `with_labels`. I recorded that they decide the outcome.
3. Claims on data elsewhere that weren't tried for lack of scope have no fitting block reason; `too_large` and `data_missing` both seemed wrong. I used `other`, with a note on each.
4. Some elsewhere claims name a raw archive, but the paper's code holds per-cell tables of the same data. I tested on those tables and recorded it as a deviation.
5. There is no rule for a claim that is only partly testable (patchseq-mapping: the excitatory half can be tested, the inhibitory half can't). I blocked it and put the excitatory numbers in the notes.
6. It isn't clear when unmatched denominators make an outcome partial rather than not reproduced. I used partial when the connection counts matched and only the pair counts were off.

**4. Runtime and failures**
The run took about 1 h 50 min (13:41 to about 15:30 UTC). Nothing failed in the final run. During development I fixed a clash between a column name and a pingouin method, and a header-row offset when reading the AIS table. Untracked dotfiles (`.bashrc`, `.idea` and others) appeared in the repository root; I didn't create them on purpose and left them alone. Nothing is committed.
