Round 3 is applied. Both notebooks pass (`reproduce_silkuniene_2025.ipynb` in 2744 s, `earlier_findings.ipynb` in 448 s). Nothing is committed.

**Outcomes changed (the verifier agreed with six of the seven proposals):**
- fig3a-centre-enhanced: blocked (data_missing) to partially_reproduced. I also made the verifier's correction: at 1 Hz, 3 of 16 readings fail under pooling (a).
- fig3-lorentzian-profile: blocked (data_missing) to partially_reproduced.
- fig4b-40-fold-ratio: blocked (data_missing) to reproduced, resting on the background footprint (`assumed`). The note now gives both sides of the first listed combination (39.4 left, 33.4 right) and says the evidence is weak, because the footprint choice alone moves the ratio across the whole 36 to 44 band.
- fig6d-longer-pulses-sharper-peak: reproduced (assumed) to not_reproduced. I removed `assumed`, because the outcome is the same under both regression-point readings and with only B2 left out or with all wells kept.
- fig6d-600-900-differ-from-300: partially_reproduced to blocked (methods_underspecified). I removed its `measured` values, which came from the darkest-footprint reading that the claims file no longer names.
- fig7cf-fwhm-with-bursts: reproduced (assumed) to blocked (methods_underspecified).

**Proposal that stands:** fig3bc-rate-suppresses-off-target keeps its verified outcome, blocked (data_missing). The proposal to change it to reproduced stays under `proposed`, now with the verifier's view added. The verifier would block it as methods_underspecified, because the paper's Fig. 3B legend fixes pooling (a), and under (a) the result depends on the footprint.

**Other updates:**
- Round 3 is recorded under `verifications`, with seven results.
- The notebook conclusions and summary, the README and the attempt notes now give these outcomes.
- The verifier reported two places where the claims file misreads the paper. I added both to `questions/silkuniene-2025.yaml` for a reader: the pooling for fig3bc and fig3-lorentzian, and the one-combination rule for the footprint in fig4b.

**Check status:** `python tools/entry.py all entries/silkuniene-2025` crashed, because this checkout has no `attempts/silkuniene-2025-03.yaml`; the previous run hit the same crash. So I ran the check with that missing file skipped, then ran `entry.py run` on its own. The outcome rules (outcomes against the last agreed round) pass.

Five schema errors remain, none from this round:
- one about the missing earlier record;
- four about fields the schema in this checkout does not allow: `datasets` and `severity` on finding 12, and `cause`, `confidence` and `supports` on three reconciliation outcomes.

I had put `blocked_by` in three round-3 results, which the schema does not allow. I removed it, and the fig3bc reason now says "Would give blocked (methods_underspecified)".
