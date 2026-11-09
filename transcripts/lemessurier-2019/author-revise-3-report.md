The verifier agreed with both proposed changes in round 3, so both outcomes changed and no proposals are left.

**Outcomes changed:**
- **`figs3-1-l4-nh-tuning`**: partially reproduced → not reproduced. The criterion only allows partial when both 0-75 µm values are within tolerance and neither absence test is significant, and no reading meets that. The notes and the notebook's conclusion still say the failure comes from the inflated NH L2/3 eBW fraction. Because the eBW definition is unresolved, it may be a failure of this attempt and not of the paper.
- **`fig5eh-l23-correlation-gradient-at-edge`**: partially reproduced → reproduced. Every condition of the criterion holds under both ways of calling a cell responsive. The verifier's two caveats are now in the notes and the notebook's conclusion:
  - The noise part passes on differences of 0.0004 to 0.002 that can't be told from zero, and in round 1 it failed under the Methods' test.
  - The claims file turns the paper's "substantially" against "modestly" into a plain sign comparison. That is already raised in `questions/crcns-ssc-10.yaml`.

The tally is now 14 reproduced, 11 partially reproduced, 8 not reproduced and 1 blocked.

**Files updated:**
- `attempts/crcns-ssc-10-lemessurier-2019-01.yaml`: both `proposed` blocks removed, both outcomes and their notes updated, and a round-3 entry added under `verifications`. It has one result per claim reviewed, each with `agrees: true`, the verifier's outcome, its reason and my response.
- The notebook: conclusion cells 62 and 111 and the Summary table.
- `README.md`: the two rows in the outcome table.

**Run:** `python tools/entry.py all entries/crcns-ssc-10-lemessurier-2019` passed with 0 errors in about 19 minutes. In the re-run, cells 61 and 110 give the same numbers that the record and the conclusions quote.

Nothing is committed. `git status` also shows some untracked files I did not create (`.bashrc`, `.profile`, `.idea`, `scripts` and others), probably from the runner environment. I left them alone, and they shouldn't be committed with this revision.
