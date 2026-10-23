There was one open question, and I answered it. `claims_check.py` passes with 0 problems. Nothing is committed.

**fig2-event-counts: how is the "power <0 dB" segment rule computed? Is it (b1), (b2) or (b3)?** The paper mostly doesn't say. The Methods compute "log-transformed spectral power density for each segment", which is one spectrum per 10 s segment. That fits (b1) or (b2), not a test over time within the segment like (b3).

- **What the paper and code don't give:** the spectral estimate, the frequencies the 0 dB test uses, whether it is judged on the mean over electrodes or per electrode, and whether the 3 SD are over one subject's segments or all subjects'. The code at 04c6faf has no such step.
- **Units:** the paper does give a hint here. It puts power without baseline subtraction at about 10-50 dB, which fits microvolts and not volts.
- **Criterion change:** the fig2-event-counts criterion now makes (b1) the main reading. It allows (b2) and a 3 SD taken over all subjects' segments, and keeps (b3) as a variant because it serves the paper's stated aim of removing segments with missing data.
- **Misquote:** the question's quoted passage has the Methods wrong. It says "the power spectral density" where the paper says "log-transformed spectral power density". I noted this in the answer.

The claim's statement and expected values are unchanged.
