I've finished the round-1 revision. The final `python tools/entry.py all entries/malfatti-2026` passed: 0 check errors, and the notebook ran in 7.3 min with 4.0 GB peak memory. All conclusions now match the new numbers, and the record passes the attempt schema.

**Outcome changes**
- **fig4fh-gamma-session13:** partially reproduced → not reproduced, as the verifier gave it. I dropped the "realigned" reading (moving four mice's prehension onsets by about 8 s) because the verifier is right that it is circular and confounded with genotype. All LFP claims are now judged on the files as deposited, where neither gamma genotype effect holds (low gamma p 0.17 to 0.40, high gamma p 0.14 to 0.19). The `assumed` flag is removed.
- **The 21 imaging claims:** the reason changes from `too_large` to `data_missing`. No traces or cells are deposited, and the paper does not give the CNMF-E parameters or the cell-matching threshold needed to derive them again.
- Every other outcome is unchanged.

**What I added or corrected**
- **Leaving out the four offset mice:** this is now a variant for every LFP claim, as the verifier asked. It gives the same outcomes. The realigned reading is still shown, only for comparison.
- **fig4d-theta-genotype:** the notes now say the outcome rests on the criterion's choice of test. The rank-based test alone would give a theta genotype p below 0.05 in 4 of the 6 deposited readings.
- **Miniscope tracking table:** added the per-file table the verifier asked for. The left paw and its first finger are both well tracked in a median of only 0.2% of frames, against 1.4% and 2.4% in the other two groups. The median file has 9.7 prehensions per 10 min, against 66.8 and 117.2. The prehension-overlap claim also has a new variant leaving out 67109 (38% of all prehensions), plus results per mouse and averaged over mice. It stays partially reproduced, and its notes now say the failing magnitudes may come from poor detection.
- **Session numbering:** behaviour sessions after 5 are now renumbered +1, as the paper's code does. No test changes.
- **Session 5 split:** the data check now prints the tracking start time (0 s in all 13 session-5 files), and a new deviation records that the code's per-mouse split times are not public.
- **Start dates:** the "dated December 2021" wording is gone. 65 of the 66 LFP files give a start time of 23:59:5x on the last day of a month, which looks like a placeholder. This is a new minor finding, added at the end.
- **Smaller points:** I noted that the "before" and "during" windows overlap in time, and that the duplicated-session variant only reproduces the paper's degrees of freedom.
- **The 8 s offset finding:** downgraded from critical to major. The files hold no sync trace, so the offset is consistent with the data but not shown.
- **Records:** added the round-1 `verifications` block, with the verifier's reasons and my responses. I also updated the README and the notebook summary.

**What I did not do**
- I did not check the rank-based test against R's nparLD, because R is not installed here.
- Nothing can settle which 6 miniscope mice the paper used, whether the 8 s offset is real, what the LFP channel holds, or the per-mouse split times. Neither the paper nor the files say.
- I added no reader questions, because the verifier reported no misreading of the claims file.
- I left `runtime_minutes: 11` in `entry.yaml`, since changing it would force another full run.
- Some dotfiles (`.bashrc`, `.profile` and others) and `scripts/` appeared untracked at the repository root. I didn't create them; they look like sandbox artefacts, so I left them alone.
- Nothing is committed.
