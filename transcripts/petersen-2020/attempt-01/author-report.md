The attempt on dandiset 000059 is finished up to the handover. The entry, claims file and attempt record are written, and `tools/entry.py all` passes (0 errors, notebook runs in 366 s). The verifier package is in `executed/000059-petersen-2020/handover/`. Nothing was committed. I used the paper's full text (the PMC7442698 author manuscript, from NCBI efetch, saved under `paper/`), but not the supplement, which could not be downloaded. The pinned version is 0.250624.0444: the paper cites no version; this is the latest, and it has the same blobs as 0.230907.2101, while the first version (0.210812.1514) has no trials table.

**1. Outcomes (38 claims: 12 reproduced, 16 partially, 9 not reproduced, 1 blocked)**

| Claim | Outcome |
|---|---|
| session-structure | reproduced |
| cooling-time-course | partially (minimum after 121 s, not 60 s) |
| fig2g theta frequency vs temperature | reproduced (R = 0.789) |
| fig2h theta power vs temperature | not reproduced (R = −0.056) |
| fig2j frequency more consistent across rats than power | reproduced |
| fig2i theta lower during cooling | partially (power lower than pre only) |
| 12% theta decrease | partially (8.9 to 9.2%) |
| fig6d errors about 3-fold | partially (2.3-fold, P = 3e-7; MS22 P = 0.064) |
| fig6e errors recover | reproduced |
| fig6c worst performance 4 to 8 trials after onset | reproduced (trial 7) |
| fig6f, fig6g errors vs temperature, vs theta | partially (R ≈ −0.84 and −0.87, stronger than −0.35) |
| fig6h errors vs theta power | partially (1 rat, not 2) |
| fig6i errors not related to speed | not reproduced (3 of 5 rats correlate) |
| fig4e speed falls within session | reproduced |
| fig5 speed, control vs cooling | partially |
| place cell rates fall 11 to 12%; interneuron rates fall 14% | partially (about 7 to 9%) |
| interneuron oscillation frequency slows | reproduced |
| suppl1g waveforms unchanged | not reproduced (small changes; drift not excluded) |
| fig4b fp and fLFP fall and recover | reproduced (all six means; 361 fields vs the paper's 365) |
| fig4c, fig4a, fig3d, fig3e correlations | partially (weaker R, or 3 of 4 values) |
| fig4ac fp − fLFP preserved | not reproduced (falls 0.13 Hz; ratio is preserved) |
| fig3c field size correlated | reproduced (R = 0.8197, at the 0.819 edge) |
| fig3f information unchanged | not reproduced (small drop, P = 0.014) |
| fig3hi population vector scale unchanged | reproduced |
| fig4d precession slope decreases | partially |
| fig4gh fp depends on speed more than fLFP | reproduced |
| fig5d pair correlogram period lengthens | partially (lengthens; 109 ms, not 85) |
| fig5cg compression falls | not reproduced (0.27 cm/ms; P = 0.055) |
| fig5h time lags increase | reproduced |
| fig5i phase lags, fig5j fraction active, fig5k spikes per cycle unchanged | not reproduced (all three) |
| hippocampal temperature | blocked: data missing |

**2. What was found about the dandiset**
- **Temperature not recorded:** in the 9 MS10 sessions and the 2 control sessions of 2018-07-19, the temperature is a smooth curve from exactly 17 to 37 °C (one is a constant 37 °C). The paper's code lists no thermocouple for these sessions. Nothing in the files says the curve is modelled.
- **Controls labelled as cooled:** the two 180719 sessions, which the code calls controls without cooling, carry cooling-state labels. Their theta slows by −0.20 and +0.44 Hz against a median of −0.82 Hz in cooled sessions.
- **Missing or incomplete sessions:** 6 of the paper's 53 sessions are missing. MS21-180627 has no cooling-state column and MS21-180712 has no trials.
- **Missing metadata:**
  - No cell types, no place fields, and every electrode location is "unknown".
  - In 7 sessions every unit is "unsorted".
  - The trial state "Cooling off" is not described anywhere.
- **Spike–position clock:** in MS21-180621 and MS22-180621 spikes carry no spatial information, so the shared clock could not be established and I left them out of the unit claims.
- **Paper inconsistencies:** the Figure 5H legend gives P = 8e-5 by a sign-rank test with n = 10 sessions, which an exact test cannot produce (minimum about 0.002). The Discussion's 12% theta decrease does not match the Results' 8.4 to 7.7 Hz (about 8%).

**3. Where the protocol was unclear, wrong or missing something**
1. **Criterion revised after a pilot:** a one-session pilot showed the fig5d method measured the correlogram's envelope, not theta. I revised the criterion before any cross-session run and recorded it in the claims header and the deviations.
2. **Sessions the paper's code excludes:** the protocol does not say whether to use sessions the paper's code leaves out, or modelled data. I followed the code's session lists and showed the other sessions as variants.
3. **Clock check fails after claims are written:** the protocol says to name such sessions, not whether to exclude them. I excluded the two 180621 sessions at the data check and amended the set definition in the claims file.
4. **Outside code that only selects sessions:** none of `with_labels` or `with_inputs` fits code that only picks sessions and parameters. I kept `data: dandiset` and listed the code repository and commit under `inputs`.
5. **Tolerance from a stated spread:** using the paper's SD across fields as the tolerance on a mean is very loose (fig4b, fig5-speed). I followed the rule as written.
6. **No partial rule in a criterion:** for fig5-speed I applied the protocol's general definition of partially reproduced.
7. **Absence claims with no named test:** I used the paper's stated default tests. Rank-sum tests over about 10,000 theta cycles are nearly always significant, so I showed per-session tests as variants.
8. **Per-rat tests that cannot reach 0.05:** an exact signed-rank test with 5 sessions cannot reach P < 0.05. The fig6d criterion judges only rats with at least 6 sessions.
9. **Continuous value on the tolerance edge:** fig3c is reported as reproduced and flagged with its variants.
10. **Full text without the supplement:** the protocol covers full text or abstract only. I tested supplementary results only where the main text states them.
11. **`measured` when no reading matches:** the protocol is silent. I recorded the first reading.
12. **Format conflict:** the example entry and the protocol's notebook outline use bold labels, which conflicts with your instruction. I removed them.

**4. Runtime and failures**
- **Runtime:** the notebook takes about 6 minutes (366 s) in CI, streaming in parallel. I ran it three times, and the outputs were identical apart from the session's own run time.
- **Paper downloads:** Europe PMC full-text XML returned HTTP 500, PMC pages returned a captcha, and the supplement could not be retrieved anywhere. NCBI efetch worked for the main text.
- **Untracked files:** `git status` lists dotfiles such as `.bashrc`, `.idea` and `scripts`. They are `/dev/null` devices the sandbox mounts over masked paths, not files from this run, and the commit should leave them out.
