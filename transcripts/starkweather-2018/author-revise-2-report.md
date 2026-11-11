No outcome changed and nothing is under `proposed`. The verifier agreed with all 32 outcomes in round 2 (20 reproduced, 12 blocked as `data_missing`), and I found no reason to change any of them. I re-ran the entry with `python tools/entry.py all`: the checks pass with 0 errors and the notebook runs (267 s). Every number it prints is the same as before, so the conclusions still match the outputs.

**Corrected or added**
- **fig7ijk, reading (b):** cell 82 and the notes said reading (b) "gives the same". They now give its own numbers: a task 1 slope of −0.015 and 49 of 50 task 2 slopes positive.
- **Summary (cell 89):** it said "most F and p values to two digits". It now says most F values agree to two digits and the p values to their order of magnitude, about half to two digits.
- **fig5f-task2-significant-slopes-shift:** cell 48 and the notes no longer say trial-by-trial baseline "follows the Methods' wording"; they say the Methods' wording fits either reading. The claim that this reading recovers the paper's numbers is limited to the listed counts and the two Fisher p values, and they now say this claim gives 8 significant negative SalB slopes where the paper prints 9.
- **README:** "about five minutes" and "7.9 MB zip" were never printed. It now gives the runtime this run printed (267 s) and no zip size.
- **Reader question for fig7ijk:** the question in `questions/starkweather-2018.yaml` now also quotes the Figure 7 legend ("…whereas the timing-impaired model (K) does not"). The claim is unchanged.
- **Port check (C2):** I fetched the MATLAB code at d667730 and compared the parts the verifier said were unchecked line by line with `belief_td.py`: `blur_matrix`, `blur_vector`, the transition and observation matrices, the observation series, and the indexing in `simulate` against `Organize_for_Plotting.m`. I found no difference. The fig7cd deviation and the response record this as my own check, not an independent one.
- **Round 1 record:** the verifier's points B7 and C3 now appear in its round-1 reason under fig4a, and the results of its synthetic checks under `reviewed`.
- **Round 2 record:** added under `verifications`, one entry per claim with the verifier's agreement, its outcome, its reason in its own words, and my response.

**Not done**
- **No MATLAB comparison:** neither MATLAB nor Octave is available here, so the port is still not checked against an actual MATLAB run.
- **fig7ijk stays open:** it stays reproduced on the criterion as written. The verifier notes the paper's "abolished" is stronger than that criterion, and only a reader can change the claim. The fig5f baseline assumption stays open until the paper's authors answer the existing `methods_unavailable` question.

Nothing was committed, as instructed.
