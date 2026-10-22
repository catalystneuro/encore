The checker passes after my edits: `claims/001863/10.1101-2025.07.09.663970.yaml: 35 claims, 35 quotes, 43 statistical values, 0 problems`.

To check the criteria's code details, I cloned the authors' repository at the commit the file cites (aa80af0a). The code matches what the criteria say it does: the 40-trial session filter, counting only odor trials for Figure 1D, the 5 min bin labels, paired signed-rank tests for every speed comparison, the one-sided KS test, the four faulty sniff sessions, the permutation test (seed 123, edge bins dropped), 48 px occupancy bins and the 2400 s session time. All statements, sources and statistics match the paper, and every main finding has a claim.

**Changes, by claim**
- **fig2a-correct-port-duration-doi-odor, fig2c-incorrect-port-duration:** the `test` names now read "Wilcoxon rank sum test", as the Results give it. The Bonferroni adjustment comes from the Methods and is still recorded under `corrected`.
- **fig4abc-sniff-frequency-higher:** the criterion said the 5th to 95th percentile sniff exclusion was applied per session, citing the code. The MATLAB code that does it is not in the repository, so this is now open, with two readings: per session, and over all sessions of a condition.
- **fig5ab-occupancy-similar:** "not reproduced" used to require DOI to be higher on every measure. A significant difference in either direction contradicts "similar occupancy", so I dropped the direction condition.
- **iti-false-report-no-difference:** the Results describe the event as entering the reward port, while the Methods define it as crossing the decision line. I added the Results' version as a variant; the Methods' definition still decides.

**Open (recorded in `checks`)**
- **fig1c-accuracy-time-bins:** the statement covers the 25 to 30 min bin, but the paper gives no p-value for it. That bin is reported, not judged.
- **Figure 3 speed claims:** the Results name the rank-sum test, while the Methods and the code use the paired signed-rank test. The criteria follow the Methods and code and show the rank-sum test as a variant.
- **fig5ab-occupancy-similar:** the paper reports no test. The entropy and corner measures, and the corner sizes, are readings of the prediction the paper states, not the paper's own method.

**Ready:** yes. The new `checks` entry records `ready: true`. Nothing is committed or pushed. The working tree also has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others); I left them alone.
