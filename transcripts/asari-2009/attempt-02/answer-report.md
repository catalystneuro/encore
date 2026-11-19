There was one question, and I amended the claims file to answer it.

`questions/asari-2009.yaml` wasn't on this branch. It exists on `origin/main`, added after this replicate branch was cut, so I copied it from there into the working tree and answered it. `python tools/claims_check.py` passes: 21 claims, 19 quotes, 0 problems. Nothing is committed.

**fig2-example-long-context: claims file changed.** The criterion said the example cell and probe aren't identified, but the paper does identify them:
- The Figure 2 legend gives the probe's reliability (0.74 ± 0.08) and the cell's reliability over all its natural sounds (0.61 ± 0.07).
- The Results say this was over "the seven natural sound fragments tested in this cell".
- Panel B's red trace is "the one shown in A".

The criterion now tests only the probe of the cell that matches these values within 10% (the closest if several match), and the claim is not testable if none matches. Before, any of 20 candidate probes could reproduce it.

I also applied the protocol's 10% tolerance to the time windows, because the Results say the traces "diverged again after about 4 s". That matches how the file already reads "about 4 s" in fig7-example-frequency-context. The claim is now reproduced when the probe has significant periods before 2 s, none between 2.2 and 3.6 s, and one starting after 3.6 s. The source now names the Figure 2A legend.

From the question's own numbers, the identified probe's late period starts at 3.97 s, so this tolerance decides its outcome. The author should rerun the claim on that probe.
