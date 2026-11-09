I worked through the round-2 report. **No outcome changed and none is proposed**, since the verifier agreed with all 41. The record still has 13 reproduced, 3 partially reproduced, 3 not reproduced and 22 blocked. I re-ran `python tools/entry.py all entries/001687-xiao-2026` after the last edit: it passes with 0 errors, in about 30 minutes. The numbers matched the previous run. Round 2 is recorded under `verifications` with all 41 claims, each with the verifier's reason in its own words and my response. Nothing is committed.

**New output the verifier asked for**
- **Probe tip (figs4j):** cell 87 now prints the electrodes table's description of `probe_site`: "1-based probe site index (site 1 = tip)". Cells 10 and 48 no longer print "tip" from their own text. The deposit's metadata states it, so this is not an assumption and figs4j stays unflagged.
- **Two cutting sessions with trials after the gap (cell 71):** the deposited trials are raw passes 21 to 220 and 51 to 250, out of 400; 200 raw passes come before the gap. If the deposit's distances are moved to raw passes 1 to 200, no unit in either session is distance-tuned (10 and 9 are tuned as deposited). The metadata_error finding now cites these outputs.
- **Order of distances (cell 87):** each block, as long as the session's number of distances, contains each distance once in 1,263 of 1,279 blocks, and in every block of 66 of 67 sessions. "Fresh random permutation" is replaced by wording these counts support, in the notes, the finding, cell 88 and the summary.

**Wording corrected to match the outputs**
- **figs4j:** p is 3.48e-25, not 3.85e-25.
- **fig3-overall, window (ii):** under 10-fold the combined group is out of tolerance and the map group is within; under 15 splits both are out.
- **Cell 72:** dropping the post-gap trials changes counts by at most 2 under BH-FDR and at most 3 under the uncorrected variant.
- **Cell 8:** the deposit labels differ for 41 units it calls unresponsive, plus 12 other units in the crosstab.
- **SNR:** I now say 75 of the 768 deposit-labelled responsive units also have SNR below 5. So the low SNR of the 18 extra units does not show that the deposit applied an SNR criterion. The deviation now says SNR is not applied because it is an approximation.
- **Cutting claims:** removed the out-of-date sentence "was not attempted" from all six notes.
- **figs4l deviation:** now gives the BH-FDR numbers (127, 82, 39).
- **fig4b-cut-wall-firing-reduced:** cell 79 and the notes now report the 79-unit subset meeting the criterion. The claim stays blocked because:
  - it is not known which subset stands for the paper's units;
  - the code's reading needs post-cut distances, which are not recorded;
  - it depends on a blocked claim.
- **Block reason for the cutting claims:** I kept `metadata_insufficient`, because `selection_undocumented` is only a finding kind and cannot be used as a block reason. The notes say so.

**New questions for a reader** (added to `questions/001687.yaml`; the claims are unchanged):
- **fig4b-cut-wall-firing-reduced:** the expected tolerance is 1.338, but the criterion says the larger spread, 2.986, is used.
- **fig6-model-telc-loses-map:** the paper's 590 and 636 come from the code's 99-point grid, not the nine bins the criterion names. Both pass.

**Not done**
- **B1 (claims file log):** I did not edit the claims file, because it is the reader's. The reader's 2026-11-03 change is recorded in the answer in `questions/001687.yaml`, but the claims file's own log still needs an entry, and that is the reader's to add.
- **B2 (fig2-distance-tuned-counts):** the question from round 1 is still waiting for a reader's answer, so this claim stays not reproduced as tested.
