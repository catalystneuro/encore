I've revised the attempt for verifier round 1. Three outcomes changed, the other 30 stay blocked, and the re-run with `python tools/entry.py all entries/000946-gao-2025` passed: 0 errors, notebook ran in 264 s. Its numbers were the same as my earlier run.

**Outcomes changed (all three as the verifier proposed)**
- **fig4-unit-counts and fig6-unit-counts: blocked → not_reproduced.** The k-means typing puts every unit in one of two clusters, so RSU + FSU is just the number of units with more than 2000 spikes. If an area's total is more than 10% off the paper's, no split can give the reproduced or the partial outcome. The notebook now has its own section for these two claims. It shows the totals under every session selection the identifiers allow (each S1 selection with and without suffixed recordings, plus the S1_R and S1BF files; POm with and without POM_S1BF), plus a breakdown by rat and suffix.
  - POm is outside 10% under every selection: 352 or 339 against 250 at 3000 Hz, 315 against 232 at 30 Hz, and 1470 or 1447 against 1019 over the five PRFs.
  - The POm units come from all 10 POm rats, so dropping one rat or one suffixed recording does not explain the excess.
- **fig11b-ac-responses: partially_reproduced → blocked (methods_underspecified).** The four readings give different outcomes, and the claims file header blocks a claim when they do. I withdrew the assumption that picked one reading.
  - None of the four readings reproduces the claim.
  - The notebook now combines the four verdicts under the header's rule and prints the result.

**Added or corrected**
- **Output the verifier asked for:**
  - SEMs for fig11b.
  - A leave-one-rat-out run under two of the readings. The verdict ranges from reproduced to not reproduced depending on which rat is left out; 300 Hz is lowest in all twelve runs.
  - Every AC recording by rat and pulse duration. The seventh AC rat, BH532, has no PD 200 µs recording, and BH538's AC_1 and AC_2 files are at PD 40 µs.
- **Deviation:** pooling across rats mixes PRF with rat in fig11b; this is now recorded.
- **Questions for a reader:** I created `questions/000946.yaml` with the verifier's two points about the claims file:
  - whether the per-trial normalization reading N2 is one the paper allows (it is biased low);
  - whether the baseline reading B1 is, since it is a constant 100% under N1.

  I did not change the claim.
- **Findings, notebook header, summary and README:** updated to the new outcomes and counts. The failure-to-reproduce sentence is already in both the README and the summary.
- **Round 1 in the record:** recorded under `verifications` for all 33 claims, with the verifier's reasons and my responses. It disagreed on 3 claims and agreed on 30.

**Not done**
- I could not check whether any M1- or POm-aimed session corresponds to the CG1 control: no metadata gives probe or target coordinates. The claim stays blocked on cell types either way.
- I left the claims file unchanged, as required.
- Nothing is committed or pushed.
