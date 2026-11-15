I've made the round-1 revision. One outcome changed, and the entry passes `entry.py check` and a clean `entry.py all` run (155 s). All other numbers are the same as before.

**Outcome changed**
- **fig3-example-vs-neuron: blocked (data_missing) → reproduced, resting on an assumption.** The verifier asked for a search for right-hippocampus units on channel 140 that prefer phones. That search led to the paper's own Figure 3 scripts (`export.py` and `import.py` at commit 1d95162). They name session 144 as `TWH103_111918`, and the dandiset's only session from that subject is 2009 (2018-11-01). Session 2009 has two units on channel 140, both in the right hippocampus.
  - Unit 2 is the third unit that passes the code's selectivity test, which is the one `import.py` plots. It is strongly selective (ANOVA p = 1.3e-09) and fires most to phones (9.10 Hz against at most 2.70 Hz).
  - Unit 1, the other reading of "cell 3", is selective (p = 0.027) but prefers small animals.
  - Both links (144 to 2009, cell 3 to unit 2) are recorded as assumptions, with the rejected unit shown. Round 2 will review this change. The session 144 part of the data_missing finding is replaced by a paper_inconsistency finding.

**Kept, with reasons recorded**
- **ms-cells-proportion and dual-cells-proportion stay not_reproduced** (problem 1). The criterion makes the Methods text the main reading and the code's choices a variant. The verifier itself found that reading faithful to the text, so I did not ask a reader. The text/code mismatch was already a code_mismatch finding.
- **fig5f-site-proportions** (problem 2): the verifier says the claim recasts the paper's sentence as a CS against TWH comparison. I added this as a question for a reader in `questions/chandravadia-2020.yaml` and left the claim and its outcome unchanged.

**Added or corrected**
- **Notebook header:** it now says 0.220126.1852 is the most recent published version, not the only one with the 87 sessions. The data check shows that 0.220126.1851 has the same paths, blobs and sizes.
- **New printed output the verifier asked for:**
  - the impedance column's stored type (float64 in all 87 files) and its values (NaN for all 887 electrodes);
  - the per-file table, printed in two parts so it is no longer cut off;
  - the patient tables as parsed from Europe PMC, in full;
  - the category names by session;
  - a check that the learning block has the smaller experiment id, which holds in 87 of 87 files.
- **fig5d-confidence-accuracy:** added the MATLAB version of the dynamic high/low confidence split as a variant (78.3% against 60.4%, p = 1.2e-13). No change of outcome.
- **Helper fixes:**
  - The selectivity test now returns 0 when every category's rates are constant but the means differ (problem 6). No count changed.
  - Added retries on the archive, OSF and Europe PMC requests. My first two runs failed on a 500 from the archive and an OSF timeout.
- **Attempt record:** a `verifications` round 1 entry for all 25 claims, with the verifier's reasons and my responses, plus the updated notes, deviations and findings. The README is updated too.

**Not done**
- Problem 5 (Unix timestamps reveal the recording day) already had a finding, so I changed nothing for it.
- Nothing is committed, as instructed.
