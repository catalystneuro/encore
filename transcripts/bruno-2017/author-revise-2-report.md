I've handled every point in the round-2 report, re-run the entry with `python tools/entry.py all` (it passes, 39.6 min), and recorded round 2 under `verifications`. Nothing is committed.

**Outcomes.** None changed, as round 2 requires.
- **fig6d-decode-p10:** I agree with the verifier that this should be not reproduced. The criterion and the paper both require all nine responses, and preparation 4, bout 1 fails under every reading, history range and windowing. The record keeps partially reproduced and adds a `proposed` change to `not_reproduced` with the reason, so a third verification round is needed for this one claim.
- **fig3h and fig7gh:** the verifier accepted partially reproduced for both, so both stay.

**Something new the re-run showed.** The P10 decoding gives different numbers on different runs.
- With longer histories, the forecasts blow up in many windows, up to about 1e13 spikes/s, the cap set by clipping the model's log-rate at 30.
- A mean of the per-window errors that includes those windows depends on tiny rounding differences. Nudging the inputs by one part in a billion halved one such mean, from 5.3e11 to 2.8e11.
- So the error figures, and the history picked from them, can shift. For preparation 4, bout 1, the verifier's copy had a mean error of 7.6e6 and this run gives 13.3. The fig6s2 test for own/le80 moved from p = 0.91 to 0.50.
- The conclusions hold in both runs: 8 of 9 responses pass for fig6d, and for fig6s2 the 90% models are never better.
- Runs on this machine repeat exactly: three runs gave identical numbers. If the workflow runs on other hardware, the decoding numbers may differ again.
- I added a notebook cell that counts these windows and runs the rounding test. The fig6d and fig6s2 conclusions and notes now use this run's numbers and say they are sensitive. `apl.py` only gained a stored maximum forecast per window; the fitting itself is unchanged.

**Other corrections:**
- **fig3h:** now states that the code's removal rule under the adopted reading keeps 19 periods with 18 returning, which meets the criterion. It is reported, not judged, because the criterion uses the Methods' rule, which I quote. It also says the criterion has no partial outcome and why partial is kept.
- **fig4c:** the "consistent with" sentence is fixed. The two means are 2.3 s apart against a 1 s tolerance, so neither the means nor the correlation support it.
- **fig7gh:** says that with the code's exclusion rule, pooled/min80 has a significant slope (p = 0.028 and 0.029).
- **Dimension ranges:** fixed in cells 21 and 22 and the Summary: 21 to 76 overall, 21 to 41 with / sqrt(12), 33 to 76 with / 12.
- **Small fixes:**
  - the fig7s2 record entry now has `notebook` and `output` fields;
  - the README runtime now says about 40 minutes;
  - the round-1 fig4c reason no longer cites the B.11 note the verifier had not given as a reason;
  - the README and Summary tables and the notebook header mention the proposed change.

**Not done:**
- No questions were added, since the verifier found no place where the claims file misreads the paper.
- The fig7s2 ensemble port still isn't checked against MATLAB, because MATLAB isn't available here; the record says so.
- I didn't make the decoding stable, for example by changing how the model is fitted. That would change the method in a round where outcomes are frozen, so I only reported the problem.

There are untracked dotfiles and folders in the repository root (`.bashrc`, `.idea`, `scripts` and others) that I didn't create; I left them alone.
