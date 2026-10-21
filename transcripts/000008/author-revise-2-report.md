No outcome changed. The verifier agreed with all 35 stated outcomes in round 2, so nothing went under `proposed`. The counts stay at 25 reproduced, 4 partially reproduced, 1 not reproduced and 5 blocked.

**Corrected (all text the printed numbers did not support):**
- **Ephys cell 7:** the unsupported "-150 to +80, resting near -65" is gone. It now gives the printed per-file baselines (-78.5 to -54.7, 5th to 95th percentile) and says the ±1,025 extremes come from one file, 20190625_sample_13.
- **Sequencing cell 3:** "a few percent higher in most cells" is replaced by the printed median ratio of 1.035 and the 5th to 95th percentile range of 0.384 to 3.078.
- **Ephys cell 74 and the hold-time-yield notes:** they now say the DandiIcephysMetadata and subject fields were listed for all files, and the entries under `general` for one file only.
- **README:**
  - The two table rows now say the dandiset has 1,328 cells and 1,283 depths, which the criteria accept.
  - The run times now read 10 to 16 minutes for each of the ephys and transcriptomics notebooks (15.8 and 16.1 min this run) and about 5 minutes for the sequencing notebook.

**Re-run and record:**
- `python tools/entry.py all entries/000008-scala-2021` passed all three notebooks with 0 errors.
- The numbers behind every conclusion are unchanged, for example fig4b r = 0.339, p = 0.0113 and fig5d exact p = 0.0497.
- The Brain Image Library again gave no answer (ConnectTimeout, 2026-10-21 04:49 UTC).
- Round 2 is recorded under `verifications` with a result for all 35 claims and the verifier's reasons in its own words. `entry.py check` passes.

**Not done:**
- **Seed dependence of fig5d, fragility of fig5b and ed8, fig1a allowance:** no outcome changes in round 2, and fig5d and fig1a rest on open reader questions in `questions/000008.yaml`. I recorded each of these and left the outcome as verified.
- **Listing `general` across all files:** I corrected the wording instead. A full listing would need the per-file reader in `scala.py` changed and all files read again, and it would not change the conclusion.
- **Points tied to no claim:** the verifier's two general helper points (B2 and B9) still have no entry of their own, because the schema has no place for remarks outside a claim. B2 is noted under ed6-it-et-room-features. I filed the data-check points under the nearest claims (link-ephys-features, rnaseq-depth, cohort-cells-mice) and said so in each reason.
- **Ephys notebook text:** its markdown still says the slow step takes "about 15 minutes on four cores". Changing it would have needed another full run of about 35 minutes for a sentence the verifier did not flag.
- **Untracked files:** some dotfiles and folders I did not create (`.bashrc`, `.idea`, `scripts` and others) appeared in the working tree. I left them alone.

Nothing is committed.
