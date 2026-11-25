I've revised the attempt for every point in the round-1 report. No outcome changed: the verifier agreed with all 13, and the five tested claims keep the same result on the re-run numbers. The entry re-ran cleanly with `python tools/entry.py all entries/choi-2025` (0 check errors), and the notebook text and attempt record match the new outputs.

**Outcomes and their new numbers**
- **fig8a:** still reproduced. The ratios for trial 133 are unchanged (2.025 and 2.199). The reference over all successful trials is now 1.259.
- **fig8b:** still reproduced, V to RW difference 0.758, p = 0.0028.
- **fig9a:** still reproduced.
- **fig9bc:** still reproduced.
- **fig9d:** still partially reproduced, p = 0.112. No variant reaches p < 0.05 now: the one that did (15 to 30 Hz with N = 2) moved from 0.0496 to 0.052.
- **The other 8 claims:** still blocked as `data_missing`.

The numbers moved because I fixed the verifier's first point: the last trial (id 1411), whose span has no end, is no longer counted as a successful trial. The trial classes now match the paper's Zenodo lists exactly (451 large, 499 small), and the special handling of that trial in fig9a is gone.

**Outputs the verifier asked for, now in the notebook**
- **Trial start times:** every `midpoint_time` equals a trial-start event exactly (largest difference 0.000000 s).
- **The 11812.1 s clock offset:** the claims file reports it from an earlier dataset version. In this version the LFP correlation at that offset is r −0.12 to −0.02, against 0.89 to 0.94 at 0 to 1 ms, so the 0.5 ms offset I used holds.
- **LFP spectra:** the raw c7b−c5c signal has strong lines at the FSCV scan rate (10 Hz) and its harmonics. The stored LFP has these removed and otherwise equals the raw signal. That is why it kept only about 0.15 of the raw SD in the beta band, as the verifier suspected.
- **FSCV timing (`iox` against the raw scans):** a kernel fitted over 36 trials shows `iox` follows the raw current near 0.6 V with no shift beyond a few tenths of a second. It is smoothed over about the preceding 2.4 s, and the file doesn't document that smoothing. I added this as a new minor finding at the end of the list.
- **Dopamine detail:** dopamine aligned to RW for large and small trials, the trial-133 samples from −5 to +5 s, and the mean traces at 0.5 s steps.
- **Spike timing against the FSCV scans:** V falls at every phase of the scan cycle. Each 100 ms PSTH bin spans one whole cycle, so the FSCV blanking can't cause the dip and peak after V.
- **fig9d:** the mean power ratio over 0 to 0.5 s is printed (0.841 large, 0.885 small).

**Corrections to the text and record**
- The fig8b notes now say that the claim's "especially between the value cue display and reward" does not hold: the difference after RW is as large or larger.
- The fig9bc notes now say the paper never calls the spikes a single unit.
- I updated the findings on clocks, LFP preprocessing and trial classes in place, so their order and numbers are unchanged.
- I recorded the round under `verifications` and updated the README.

**Questions for a reader**
I created `questions/choi-2025.yaml` with two questions on these points:
- **fig9bc:** the statement adds "consistent with a single unit", which the paper doesn't say, and the refractory test cannot fail on these spikes.
- **fig8b:** the criterion doesn't test the "especially" part of the claim.

**Not changed**
- **recordings-two-monkeys** stays blocked. The verifier's own outcome is blocked too, and the claim has no criterion for one monkey.
- **fig9d** stays partial. The criterion compares medians, and the verifier agreed.
- I didn't change any claim's statement, criterion or expected values, and I didn't commit anything.
