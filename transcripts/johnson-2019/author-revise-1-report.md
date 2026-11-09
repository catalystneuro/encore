The round-1 revision is finished. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, notebook passed in 33.5 min), and every conclusion, the summary, the README and the attempt record now match the new outputs. Nothing is committed.

**Outcome changes.** Round 1 doesn't bind outcomes, so these are changed directly, each with its reason under `response`:
- **erp-no-condition-difference: reproduced → not reproduced** (still resting on the neighbour/alpha assumption). The ERP segments are now zero-padded before filtering, as the Methods and the claim's criterion say. Under the adopted reading, S2 identity-vs-temporal has a cluster at p = 0.041. The analysis run in round 1 (whole-epoch filtering) gives 0.031 with this run's random seed, against 0.053 before. So the flip is mostly Monte Carlo noise around 0.05, and the notes say so.
- **fig4a-delta-theta-shift: partially reproduced → not reproduced.** With a corrected null (below), no subject is above zero under either PSI reading.
- **fig4c-alpha-beta-shift: not reproduced → partially reproduced**, resting on PSI reading (b). It meets the partial bar by the letter: 6 of 7 subjects below zero, and the pair-level F is 97.9. But the subject means are only −1.35 to 0.46, and on subject means the effect reverses sign (p = 0.27). The notes say this plainly.
- **directional-pairs: reproduced → not reproduced.** With the corrected null only 1 and 74 pairs (reading b) or 78 and 104 (reading a) are directional, against the paper's 1008 and 984. Trial-shuffled data give about the same counts.
- The other 13 outcomes are unchanged. power-low-frequencies now passes under every neighbour reading, but only if the 2-Hz end of the range counts as a local maximum, so that is recorded as the assumption.

**What I added or corrected, by verifier problem.**
- **PSI null (problem 1).** The z-scores are now calibrated: the null shuffles one signal's frequencies and recomputes the same statistic, as the Methods describe. The paper's own code's null is kept only as a comparison variant. A new check pairs each PFC trial with another trial's parietal data. On those shuffled pairs the corrected null flags 6–7% under reading (a) (0.1% in delta-theta under reading b), against 90–92% for the code's null.
- **Code variants (problems 2 and 3).** The no-conjugate "code" variants are labelled as not a reading and decide no outcome. The replicate per-bin nulls are gone.
- **Scripts (problem 4).** The notebook now prints the relevant lines of the deposited scripts. They contain no cluster test at all, so neither the neighbour rule nor the alpha per tail is set anywhere.
- **ERP and power method (problems 5 and 6).** Power and time-resolved PSI now use the zero-padded segment as the main reading, because the Methods outrank the scripts. The scripts' whole-epoch windows are a variant. The ERP test adds three variants: per-trial baseline, the Results' 1–30 Hz band-pass, and whole-epoch filtering.
- **Delay timing (problem 7).** ERP and power are also run on the 900-ms-delay trials only.
- **Other output the verifier asked for.**
  - Per-subject power percentages under every reading.
  - A local-maximum result with the 2-Hz end excluded (problem 9).
  - Subject-level tests next to the pair-level PSI models (problem 10).
  - Runs longer than 100 ms, printed separately.
- **Question for a reader (problem 8).** I created `questions/crcns-fcx-3.yaml` asking whether "sustained" means at least 100 ms (Methods) or more than 100 ms (Figure 5 legend). No outcome changes either way.
- **Findings.** The code-mismatch finding now covers psianalysis.m's null. The two questions for the paper's authors and the timing finding are updated with the new numbers.
- **Record.** The round is recorded under `verifications`, with all 17 claims marked as agreed, as the report gave them, and runtime raised to 35 min in `entry.yaml`.

**Not done.** I did not add the cue-locked high-gamma traces per delay group. The 900-ms-only variants cover how the timing issue bears on the results.
