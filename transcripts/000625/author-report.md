I did steps 1 to 6 for dandiset 000625. The entry passes `check`, runs from a clean environment in 451 s, and the handover package is built in `executed/000625-geiller-2020/handover/`. I used the full text, from the NIH author manuscript on PubMed Central (PMC7736348); the supplementary figures were not available. I pinned version 0.231114.0019, the most recent published one, because the paper cites no version. The only other published version (0.231114.0017) has the same three assets and differs only in its description text.

**(1) Outcomes per claim** (26 claims: 4 reproduced, 5 partially reproduced, 5 not reproduced, 12 blocked)

| Claim | Outcome |
|---|---|
| fig1-cells-per-mouse | Partially reproduced: 231 ROIs is in the paper's range; 74 identified is below it |
| fig2c-most-positive | Reproduced: 0.095 negative among the six subtypes (tolerance 0.088 to 0.108) |
| fig2c-cck-negative | Reproduced: 6 of 15 CCKC negative against 1 of 59 others, p = 0.00017 |
| fig2c-subtypes-differ | Reproduced: ANOVA p = 0.0015 |
| fig2c-ngfc-less-modulated | Not reproduced: p = 0.58 |
| s2-lags | Not reproduced |
| s2-cck-run-stop | Partially reproduced: CCKC stay flat at run stops while others drop, but do not rise |
| fig4-fraction-spatial | Not reproduced: 1.0% with the peak rule, 69.8% without, against 17.5% |
| fig4-fraction-negative | Not reproduced: 66.4% against 12.7% |
| fig4d-decoding | Not reproduced: the criterion holds in 1 of 3 sessions |
| fig4f-selectivity-no-difference | Reproduced: ANOVA p = 0.17 |
| fig4h-pvbc-more-stable | Not reproduced: PVBC 0.678, SomC 0.736 |
| s6-within-session-order | Partially reproduced: CCKC lowest, but PVBC is second to SomC |
| s6-later-lower-above-chance | Partially reproduced: lower in every pair, above chance only for the same-day pair |
| fig1-depth, fig2d, s3, fig3 ×2, fig5 ×2, fig6 ×2, fig7 ×2 | Blocked: data missing |
| fig4e-bic-recurrence | Blocked: other (only 3 BiC) |

**(2) What I found about the dandiset**
- It holds one of the paper's 16 mice (tg19) in three random-foraging sessions: 231 ROIs, 74 of them in one of the paper's six subtypes. No cell depth, LFP, licking, novel-context, goal-oriented or VIP data.
- The stated imaging rate (5.7981 Hz) is wrong for sessions 21324 and 21322. At that rate, population activity does not follow running (r = 0.16 and 0.09). Fitted rates of 4.395 and 4.385 Hz give r = 0.72 and 0.87, and make all three sessions about 898 s long. The fit recovers the stated rate for 21333.
- The dF/F unit is given as "lumens". The Fluorescence series is the same HDF5 object as DfOverF, so there is no raw fluorescence.
- The subtype table has 232 rows for 231 ROIs, and its column description reads "Recording location in Middle Earth". The labels NOTHING and UNIDENTIFIED, and the reward and water intervals, have no description.
- All three sessions say "session 1 of 4"; the fourth is missing.
- Nothing links ROIs across sessions. The data are consistent with the same index being the same cell, but do not show it.
- No duplicate recordings were found.
- The emission wavelength is given as 920 nm (the same as excitation), and the age as P60D, where the paper gives 3 to 5 months.

**(3) Where the protocol was unclear, wrong or missing something**
1. Step 1.7 says to write criteria before running a claim's analysis, but testing the helper module is in effect running it. My trial run showed the velocity and place-field fractions and one decoding error before I wrote the criteria. I listed these in the claims file's opening comment.
2. Nothing covers a wrong sampling rate. I fitted the rate from the population–speed relation, which is partly circular for the velocity claims. I recorded it as a deviation and showed the stated clock as a variant.
3. The shifted-label check runs on the fitted clock, which comes from the same signal. I added an independent support: the fitted rates make all three sessions the same length as the one whose stated rate fits.
4. There is no rule for whether ROI identity across sessions has to be shown before averaging over sessions. I tested it, took the dandiset's description as the working assumption, and showed results per session too.
5. "Decide now which claims are blocked" conflicts with `other` (too few units), which can only be known after a selection. I put minimum counts in the criteria, blocked the BiC claim from the data check, and kept the others as tested.
6. A claim can rest on two readings when one of them selects almost no cells. For decoding, selectivity and fig4h, I fixed in the criteria a fallback to the rule without the peak when fewer than 5 cells qualify.
7. It is unclear whether a criterion that holds only in part is "partially" or "not reproduced". I used partially reproduced when a named part held, such as CCKC lowest but PVBC not highest.
8. Nothing says whether a code repository that was only read counts under `inputs`. I recorded it there, since its lap definition is used.
9. Nothing says to add the attempt to the README's "Attempts so far" table. I did not.

**(4) Runtime and what failed**
- The session took about 64 minutes; the notebook takes 451 s.
- pynwb 4.2.0 could not load the files' cached namespaces (an ElectrodesTable conflict), so the helper reads the files with h5py.
- The paper's LinearSVC decoder took 17 minutes for one session. I replaced it with a one-vs-one linear SVC (19 s), recorded as a deviation.
- Untracked files I did not create are in the repository root: `.bashrc`, `.profile`, `.gitconfig`, `.idea`, `.vscode`, `.mcp.json`, `scripts` and others. Exclude them before the workflow commits, or they will be committed.
