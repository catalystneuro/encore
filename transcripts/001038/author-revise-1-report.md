No outcome changed in round 1. The verifier's 29 outcomes all agree with the record; the only disagreements are the reasons given for the three blocked claims. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, 107 s), and every number in the updated conclusions and notes matches the new executed notebook. Round 1 is recorded under `verifications` in `attempts/001038-azcorra-2023-01.yaml`, one result per claim, with the verifier's reasons in its own words and a response to each.

**What I corrected**
- **fig5ab-transient-scaling:** the main result now uses only the recomputed onsets that also appear in the file's stored onsets. The stored ones already exclude the 5 s after every reward, as the paper's code does, so this is a closer match to the code. The new ratios are 241, 246 and 232%, against 239, 266 and 222% before; the old onsets are kept as a variant. Vglut2 and Anxa1 are now outside tolerance, so the outcome stays partially reproduced, and the measured values, notes and deviation are updated. The ratio over recordings with both quintiles, which the verifier asked about, is the same.
- **Blocked claims:** the header and summary now name the blocked reasons by their category names (`not_runnable`, `other`).

**Output added at the verifier's request**
- **Locomotion overcount:** counts after each step split by location, by single or dual fiber, and by sessions with or without stimuli, plus recordings per mouse and two variant counts. The extra recordings are spread across every split, and no variant gives the paper's counts. The paper's preprocessing code also excludes and crops some recordings by hand, which can't be repeated, so the cause is still not found.
- **ed9k denominator:** the 160 striatal components capture 100.00% of the SNc data's total variance, so the percentages are not inflated.
- **RewardNoRest:** each rest row is its reward row shifted 0.01 s with the same duration. The 2647 onsets left equal rewards minus rest rewards in every file, so there are no false onsets.
- **Deceleration peak timing:** mean triggered averages with the paper's peak times marked. The peaks of the means are 0.44 and 0.27 s, still later than the paper's 0.35 and 0.23 s; the cause is not found.
- **DAT air puff:** per mouse and per location under both windows. Mouse means run from −3.83 to 6.03; the cause of the gap from the paper is not found.
- **ed1h depth:** depth follows the DV coordinate (rho 0.92), consistent with depth from the brain surface. Deep bands starting at 2.75 or 2.9 mm give a negative mean, so the failing part rests on the 5 recordings deeper than 3 mm.
- **Smaller points:** the fig4i results with at least 1 or 2 rewards of each size, a one-to-one cluster mapping for the k-means (also 92.6%), and the circular means for fig2l.

**What I did not change, and why**
- **Long and short reward offset (point 7):** the one-bin offset is how the paper's code builds these signals.
- **Wrap-around NaN fill (point 14):** this ports the code's `circshift`, which also wraps.
- **fig4g-reward-response and fig4i-reward-size:** kept as partially reproduced. The claims file fixed the Methods' response windows as the main result before the analysis; the verifier gave the same outcome.
- **Blocked reasons:** I kept `not_runnable` for the two snRNA-seq claims, because the R software can't be installed in the entry's locked environment. I kept `other` for the histology claim, because the protocol never uses `data_missing` for data that are public in another archive. The partial snRNA test the verifier proposed is what `snrna-anxa1-within-aldh1a1` already tests.

I saved the paper's full text under `paper/` (not committed) and committed nothing. `git status` also lists several untracked dotfiles and a `scripts` directory that I did not create; I left them alone.
