No outcome changed in this round, as the protocol requires. The verifier disagreed with two outcomes, and I recorded both changes under `proposed` for a third round to review:

- **figs3-1-l4-nh-tuning**: stays partially reproduced; proposed not reproduced. The claim's own partial clause can't be met under any reading. Under E1 and E2 the eBW test is significant (p = 0.036 and 0.0051). Under E3 it is not, but the L4 value is 82.1%, outside 73 ± 7.3. figs2-1 and fig4ae fail their partial clauses the same way and are already scored not reproduced. The verifier withdrew its own round-1 recommendation of partial.
- **fig5eh-l23-correlation-gradient-at-edge**: stays partially reproduced; proposed reproduced. After the re-run, every condition of the claims-file test holds in both responsiveness readings. The permutation test I added (noise p = 0.96 and 0.81) is not part of that test, so it stays in the notes as a caveat.

In the notebook, a paragraph under each of those two results sets out the analysis behind the proposal.

**Text corrected to match the outputs:**
- **Run time** (notebook cell 0 and README): now the range over the last three runs, 7 to 10 minutes of streaming and 14 to 24 minutes in all.
- **README, fig2a row**: now names the blank-median z-score as well as the stored p-values.
- **Notebook summary**: the NH L4 values match only under E1 and E2. Under E3 the L4 value is 82.1%, outside tolerance.
- **fig5a (cell 105 and record notes)**: the gaps to the paper's values are now given for each reading: 0.035 to 0.078 with the Methods' test, and 0.047 to 0.096 with the stored p-values.
- **Responsiveness finding in the record**: only the L2/3 cell counts match either test; no reading matches the L4 counts.
- **figs5-2 (cell 121 and record notes)**:
  - None of the response differences is significant (p from 0.30 to 0.93).
  - At r = 0 the rebuild finds 815 and 460 responsive L2/3 cells, against 850 and 472 in the main analysis.
  - The drop comes from 89 L2/3 cells whose rebuilt traces contain invalid (non-numeric) values; the code counts them as unresponsive at every weight.
- **fig7c (cell 130 and record notes)**: performance does not rise steadily with ensemble size under the "member columns, normalisation (a)" combination. The criterion needs only one combination where it rises, and the other three qualify.

**Added:**
- A question in `questions/crcns-ssc-10.yaml` for a reader on fig5eh: the claims file's test compares two differences without testing them. I did not change the claim.
- A round-2 entry under `verifications` in the attempt record covering all 34 claims. It gives the verifier's reasons in its own words and what I changed in reply.

**Runs:** `python tools/entry.py all` passed three times (after each round of text edits), with 0 errors from the checks. The key numbers were identical in every run, and the last executed copy matches the final text.

**Not done:** The untracked files in the repository root (`.bashrc`, `.idea`, `scripts`, and others) were not created by me, and I left them alone. Nothing is committed, as instructed.
