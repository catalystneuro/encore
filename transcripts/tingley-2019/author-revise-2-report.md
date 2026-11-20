No outcome changed and none is proposed, so no third verification round is needed. The verifier agreed with all 39 outcomes. The entry was re-run with `python tools/entry.py all entries/tingley-2019`: the checks report 0 errors and all four notebooks pass. Every number I quote below comes from that run.

**Outcomes and flags**
- **dataset-composition:** now marked `assumed: true`. Two of the four counts within tolerance only count under choices I made: units labelled `hpc` counted as CA1 (38 recordings; the `ca3_channel` flag gives 29), and `ripplesALL` counted as CA1 ripples (55; `CA1Ripples` alone gives 47). The record, the LFP notebook's result and the Summary now say that without either choice only 3 of 6 counts are within tolerance, which would be not reproduced.
- **fig4b-hfo-above-behav:** kept as reproduced and assumed. The text now says it fails only in the 4 of 16 readings with raw counts and maze-traversal (BEHAV) time taken over the whole span. With raw counts and BEHAV inside trials, both parts also hold.

**Text corrected**
- **Main notebook, Figure 4 result:** the false "BEHAV medians are 10 to 100 times" sentence is replaced. The Figure 4 table now prints means as well as medians: the means are 13.1 to 83.0 for BEHAV against 0.60 to 0.85 for the pre-maze epoch (PRE), while the medians are comparable.
- **fig7e-state:** the bound is now "binomial p at most 1.23e-8" in the notebook and the record.
- **"one waveform per unit":** corrected in the Summary, the fig7e-ca1-depth notes, the finding and the round-1 response. In the one file listed per animal, units in the DT1, DT2 and DT8 files hold one 32-sample `raw_waveform`; those in the DT5, DT7 and DT9 files hold none.
- **Run times:** updated in the README and `entry.yaml`. The Figure 7E notebook took 24 minutes before and 30 minutes in this run; the README says about 25. I left it there because editing the README would invalidate the run stamp, and a second full run (about 110 minutes) would not have finished before the 01:47 cut-off.

**Added**
- **Whole-epoch inclusion variant for Figure 4:** a new cell in the main notebook applies the pair-inclusion rule to all spikes of the pre- and post-maze epochs, keeping the cross-correlograms from spikes during HFOs.
  - It keeps 10,159 to 15,732 pairs in 54 sessions, against 361 to 503 under the claims file's readings and 7,172 in 53 in the paper.
  - The pre-maze and post-maze epochs then differ in 4 of the 8 normalized readings, all with the 5 ms SD kernel (p 0.00047 to 0.0082, r about -0.02).
  - Under this variant fig4b-pre-post-unchanged would not hold in every reading. It is not one of the claims file's readings, so the outcome stays as tested and the variant is reported in the notes and conclusions of the Figure 4 claims.
- **Two questions for a reader** in `questions/tingley-2019.yaml`:
  - whether the inclusion rule should also be read over the whole epoch;
  - that the Figure 7E criterion ("within tolerance under one of 16 combinations") can hardly fail.
- **Round 2 in `verifications`:** all 39 claims, with the verifier's reasons in its own words and my responses.

**Not done**
- The jitter test was not run under the whole-epoch variant, as the notebook says.
- Nothing has been committed or pushed.
