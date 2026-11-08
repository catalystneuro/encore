Round 3 is applied and recorded. `python tools/entry.py all entries/crcns-hc-11-grosmark-2016` passed: 0 check errors, and the notebook ran in 55.5 minutes, under the 60-minute limit. The outputs match the numbers in the updated conclusions. Nothing is committed.

**Outcomes changed (the verifier agreed with these four):**
- **figs16c-low-rate-coding:** partially reproduced → not reproduced. The notes now include the verifier's two additions: under split (c, ii) the field-count test also fails (p = 0.21), and under the PRE-rate splits the gain measure divides by the same PRE rate used to split the cells, which may explain part of the reversal.
- **fig4d-slow-cells-replay:** partially reproduced → not reproduced. The notes say the comparison uses point estimates with 100 shuffles per template, and that some gaps are small (low 0.062 against high 0.055).
- **figs11-cluster-quality-similar:** blocked → reproduced. I removed `blocked_by`, added `assumed: true` plus the `notebook` and `output` fields, and the notes say the result covers cluster quality and stability only. Waveforms were not compared, and the measure has little power.
- **fig2e-plastic-removal:** reproduced → partially reproduced.

For figs16c and fig4d I removed `assumed: true`, because the outcome no longer depends on picking split (a, i). fig2e keeps the flag because its groups still rest on the P-a reading.

**Proposal that stands:**
- **fig4c-coactivation-by-rate** stays reproduced, the outcome round 2 agreed with. The proposal to change it to partially reproduced remains, with the verifier's view added to its reason. The verifier would give not reproduced: under pooled ranks only the slow-firing condition fails, and the claims file's partial clause doesn't cover that case. Any change waits for a new attempt.

I also updated the notebook conclusions, header and summary, the entry README and the claim notes. Round 3 is recorded under `verifications` with one result for each of the five claims.
