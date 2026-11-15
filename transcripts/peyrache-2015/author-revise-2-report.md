No outcome changed, since round 2 doesn't allow it. Two changes are written under `proposed` for the third verification round. The full entry re-ran with `python tools/entry.py all entries/peyrache-2015`: all three notebooks pass and the check reports 0 errors. Every changed conclusion matches the printed numbers.

**Proposed changes of outcome**
- **fig5e-readout-windows: blocked (too_large) → partially_reproduced.** The verifier was right that the printed timing did not support the block. The GLM notebook printed 12.2 minutes, not the 21.1 I had written. I ran the dense window grid in a new notebook, `glm_windows_peyrache_2015.ipynb` (24.8 min, 26 windows, PoS targets only). The median best windows are 168 ms (waking), 178 ms (REM) and 63 ms (SWS), against 123, 133 and 79. None is within tolerance, but SWS is the shortest in every variant, which the criterion calls partially reproduced.
- **fig4d-ole-near-bayesian: not_reproduced → partially_reproduced.** I decoded the hd-b ensembles (27 ADn, 11 PoS), as the verifier asked. The covariance OLE then beats the signal OLE in both structures: p = 0.019 in ADn and 0.042 in PoS. It stays more than 25% worse than the Bayesian decoder in PoS (1.76), so only the first part holds. With hd-a ensembles the claim is still not reproduced.

**Assumption revised.** The verifier found the signal OLE I had adopted unreasonable: it errs by up to 103°, worse than the 90° expected by chance. The adopted signal OLE now puts the observed variances on the diagonal, with the earlier version shown as a variant. fig4e stays not reproduced under every reading: the ratio is 0.99, and ADn against PoS gives p = 0.28 and 0.82. decoding-tracks-hd also reports the hd-b ensembles and stays reproduced.

**Corrected text**, in the notebooks, README and record:
- All GLM timing claims now point to the run times the notebooks print.
- Cell 15: the "8 of 10" sentence.
- The summary: Mouse20 has 48 units against the table's 49.
- fig7: the first binomial reading fails (p = 0.064); only the second holds (p = 0.0009).
- fig6b: `measured` is now 1476 pooled pairs, with 492 per state.
- fig2f: the fits at 1.5e-14 deg/s are now counted and described as effectively 0.
- fig3a: the rate-a sentence now applies to hd-a only.
- The OLE `methods_unavailable` finding is updated.
- The round-1 responses that gave the 21-minute timing now say it was wrong.

**Added**
- `questions/peyrache-2015.yaml`, with two questions for a reader:
  - the fig4d wording of the signal Q;
  - the recording-sample criterion, which defines no partial outcome.
- The round-2 entry under `verifications`, covering all 35 claims in the verifier's words. For fig5e-readout-windows it is marked as a disagreement with no outcome given, as the report names none.
- `entry.yaml` lists the new notebook, and the runtimes are updated.

**Not done**
- The GLM all-cell readings were not run.
- For the claims the verifier only called borderline, I changed nothing beyond what the notes already say.
- The record omits a qualifier from one of the verifier's round-1 reasons (fig3b). I noted this in the round-2 response and left the round-1 text as it was.
