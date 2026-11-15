I answered the one question and changed the claims file. `claims_check.py` passes on 21 claims, 19 quotes and 2 statistical values with 0 problems, and both YAML files load.

`questions/asari-2009.yaml` was not on this branch, which shares no history with `main`. I copied it from `origin/main`, where it holds one unanswered question. The claims file was identical on both branches, so the question applies here as it stands.

**fig2-example-long-context: claims file changed.**
- **Why:** the claims file was wrong to say the paper does not identify the example cell and probe. The Figure 2A legend gives the cell's reliability over its natural sounds ("0.61 ± 0.07") and the probe's ("0.74 ± 0.08"), and Figure 2B's red trace is "the one shown in A".
- **Matching:** the criterion now finds the example by those values. Where several probes qualify, it takes the one closest to both.
- **Time boundary:** the Results say the responses "diverged again after about 4 s". The boundary therefore takes the protocol's default 10% tolerance, giving 3.6 s, the same rule the file already uses for `fig7-example-frequency-context`.
- **Result rule:** the claim is reproduced when there are significant periods before 2 s and after 3.6 s, and no significant time point between 2 and 3.6 s. The strict reading (nothing significant between 2 and 4 s) is still reported.

I set `answered: 2026-11-15`. Nothing is committed or pushed.
