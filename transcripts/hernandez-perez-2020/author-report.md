I've finished steps 1 to 5 and run the handover (step 6). `python tools/entry.py all entries/hernandez-perez-2020` passes with 0 errors, and the notebook runs from a clean environment in 93 s. I haven't verified my own work and haven't committed anything. New files are `entries/hernandez-perez-2020/` and `attempts/hernandez-perez-2020-01.yaml`.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig2d-phase-shift-rate | reproduced (27.32 deg/mm, p = 0.031) |
| fig2d-linear-fit | reproduced (r2 = 0.778) |
| fig2a-all-rats | reproduced |
| fig2e-phase-locking-high | reproduced, assumed (0.946) |
| fig2e-phase-locking-decrease | reproduced, assumed (-0.0675 per mm) |
| fig2c-coherence | reproduced (0.677, all pairs) |
| fig2f-coherence-decrease | not reproduced (0.211 per mm, about 3 times the paper's) |
| fig2g-power-no-change | reproduced |
| fig3-along-not-across-layers | blocked, data_missing |
| fig4d-mua-phase-shift, fig4d-mua-matches-lfp | blocked, data_missing |
| fig5c-rise-decay-gradient | partially reproduced (-0.17 dorsal against the paper's -0.43) |
| fig5c-peak-trough-gradient, fig5-dorsal-sawtooth, fig5-ventral-rise-not-peak | reproduced |
| fig6b-delay-by-phase | partially reproduced (the rising phase, not the peak, has the longest delay) |
| fig6c-delay-phase-slope | partially reproduced, assumed (slope in range, R2 = 0.67) |
| fig6b-hilbert-between-limits | reproduced, assumed |
| fig7-asymmetry-delay | not reproduced, assumed (6.07 against 3.56 ms/mm) |
| fig7-residual-delay | not reproduced |
| fig8c-relative-delay-flat, fig8d-absolute-delay-slope, fig8-correlation-strength | not reproduced |
| fig8-coupled-oscillators | partially reproduced (what the criterion's "otherwise" gives) |

**2. Dataset, assumptions and questions**
- **Contents:** one LFP matrix per rat at 500 Hz, with 5 or 6 channels each. There are no units, electrode positions, channel selections, broadband signal, multi-unit recordings or laminar array.
- **Units:** rats 1, 4, 5 and 6 hold integers (rat 5 reaches 32767, the int16 limit), so they look like ADC counts. Rats 2 and 3 hold non-integers about five times smaller, which fits µV. Applied to the stored values, the paper's 400 µV theta threshold selects nothing in rats 2 and 3.
- **The one assumption** ("assumed" above): I put all rats on one scale by dividing rats 2 and 3 by 0.195 µV per bit, so the threshold can be applied to all six. Under this reading, rats 2 to 6 give 3200 to 6286 dorsal cycles and rat 1 gives 815, against the paper's 3500 to 5000. The notebook shows every outcome without the threshold as well.
- **Version:** CRCNS has no versions, so it is recorded as `unversioned`, and the MD5 sums from the bucket are printed in the notebook.
- **Figure 8:** the per-cycle relation between delay and frequency changes sign depending on whether the period runs to the next peak or from the previous one. A centred period that doesn't use the reference peak's time mostly removes it, so shared timing noise is the likely cause.
- **Findings recorded:** two `metadata_insufficient`, one `data_missing`, one `other` (durations of 20 to 33.5 min against 25-min trials) and one `paper_inconsistency` (the "rank sum" statistics, an n = 3 test that cannot give p = 0.03, and the coherence slope's sign).
- **Questions for the paper's authors** (`methods_unavailable`): the units and threshold scale, which epochs the phase locking used, how the Figure 8 period was defined, and how cycles were matched across channels.
- **Questions to a reader:** none.

**3. Protocol points**
1. The protocol has no rule for a unit that is missing or inconsistent between files when a method threshold depends on it. I treated it as a method detail the paper leaves open and adopted a reading as an assumption.
2. Some criteria define only "reproduced" (fig6b, fig6c, fig5c-rise-decay). Where one part fails and the others hold, I used the protocol's definition of `partially_reproduced` ("holds only in part") and said so in the notes.
3. fig8-coupled-oscillators' criterion gives "partially reproduced" even though neither prediction holds. I followed it and said so in the notes.
4. The claims file's own readings (O1 b, O2 b) need metadata the dataset doesn't have. The protocol doesn't say how to record a reading that can't be run; I recorded each as a deviation.
5. The "Develop on a subset" step was trivial here: the full run took 90 s and 0.9 GB.

**4. Runtime and failures:** the work took 16:54 to about 17:25 UTC. The first check failed because the helper didn't name the version `unversioned`; I added it. Nothing else failed.
