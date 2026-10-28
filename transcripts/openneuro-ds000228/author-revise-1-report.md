I've changed three outcomes to agree with the verifier and added the outputs it asked for. The entry was re-run with `python tools/entry.py all` (0 errors, notebook passes in 223 s), and `entry.py check` passes on the updated record. Nothing is committed.

**Outcome changes** (the verifier was right in each case):
- **irc-williams**: partially reproduced → not reproduced. The criterion has no partial outcome. Two tests the paper reports as not significant come out significant here: within-Pain against Scene (p = .0098) and within-Pain against M1 (p = .0043).
- **rc-child-adult-timecourse**: partially reproduced → not reproduced. Three correlations miss the paper's p bounds: ToM 3yo (.0076 against < .0005), Pain 3yo (7.1e-13 against < 1e-15) and Pain 4yo (4.0e-12 against < 1e-13). The notebook now checks each age group against its own bound. Judged only at the Bonferroni alpha of .01 it would be partially reproduced, and the notes say so.
- **maturity-across**: partially reproduced → not reproduced. Within-Pain significantly predicts Pain maturity under every reading (p = .0054 to .018), and the criterion requires it not to.

Totals now: inter-region correlations 6 partially reproduced and 9 not; reverse correlation 1 reproduced, 3 partially and 4 not; functional maturity 3 reproduced and 1 not. The README and the notebook's summary table show these counts.

**Added or corrected:**
- **Offset in the inter-region correlations (problem 1).** It is still unexplained. The new outputs show:
  - The ROI masks are in MNI mm, centred on the stated coordinates.
  - The images are int16 with no scaling.
  - Of the diagnostic variants (adult means printed in the notebook), none within the paper's described method closes the gap.
  - Only adding a shared ToM and Pain signal as a regressor, which is not the paper's method, pushes the across-network value past the paper's (to -.382). So the offset points to a shared signal the paper's processing removed and this one does not.
  - The adult and 3-year-old mean 13×13 matrices are printed; Fig. 2 shows them only as colours, so a pair-by-pair comparison isn't possible.
- **Absence claims that flip between readings (problem 3).** The notebook now states the rule: such a claim is judged under the reading the paper best supports, marked as assumed, with every reading shown. This is the same main reading the verifier used, so those four outcomes stay as they were.
- **rc-overlap reading (b)** now uses 159-TR timecourses as the claims file says. The found events give p < .001 (0 of 1000 permutations), and the outcome is unchanged.
- **irc-3yo-homologous**: the ranking is printed for all eight readings. RTPJ-LTPJ ranks fourth under each.
- **Summary cell**: it is now its own cell, so the handover removes it. I checked that it does.
- **replication-sample**: added the README check. Its replicated events cover every table event except P08, P09 and P11. The claim stays blocked.
- The `verifications` round is recorded for all 42 claims (39 agreed, 3 disagreed), with the verifier's reasons and my responses.

**Not done:**
- I added no reader questions, because the report names no place where the claims file misreads the paper.
- rc-3yo-events stays partially reproduced, resting on the assumption that z-normalization spans all 168 TRs. The verifier agreed with that outcome but noted it would be not reproduced under the other reading; the notes record this.
- Per-participant ART artifact counts were not recomputed from the raw images; only the deposited indicators are used.
- hand-coded-events already had `blocked_by: other`, as the verifier suggested.
