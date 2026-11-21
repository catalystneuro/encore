No outcome changed. The verifier disagreed with the only proposal in round 3, so it stands.

**Proposal that stands**
- **fig7d-contacts-exceeding-baseline** stays `not_reproduced`, and the proposed change to blocked (methods_underspecified) remains under `proposed`. The verifier gave two reasons:
  - The claims file blocks a claim only when its readings disagree. Here all 16 readings agree (none hold), so as written the criterion gives not_reproduced.
  - The evidence behind the proposal is the paper's own Fig. 7d series, and those are means over three mice. Averaging inflates the count, as the paper's Opsin (+) panel shows: 25 of 25 contacts in the group mean against 15.7 per mouse. So that evidence makes 2.7 per mouse hard to reconcile with the rule but does not rule it out.

  I added the verifier's view to the proposal's reason.

**Other changes**
- **Question for a reader:** the verifier pointed out that the claims file fixes which baseline values the bootstrap resamples (the 1 s steps) as a standard choice, though the paper's Methods don't say. It would block the claim if that were listed as an open reading. Following the protocol, I put this to a reader as a new question in `questions/prakash-2022.yaml`. The existing methods_unavailable finding and the cell 30 numbers stay, as the verifier recommended.
- **Text updated:** the claim's notes, notebook cell 31, the notebook summary and the entry README now match.
- **Round 3 recorded** under `verifications`: agrees false, outcome not_reproduced, the verifier's reason and my response.
- **Run time text:** the first run took 51 min, longer than the 46 min the README and notebook cell 0 gave. I corrected both, which required a second run.

`python tools/entry.py all entries/prakash-2022` ran twice and passed both times (3073 s and 3101 s, 0 check errors). The fig7d numbers in the new run are unchanged: 25 of 25 and 20 of 25 contacts, 19 with 10 s blocks. Nothing is committed.

Several placeholder files (`.bashrc`, `.mcp.json`, `scripts` and others) showed up untracked in the repo root. They were created when this run started, not by my edits, so I left them alone and they shouldn't be committed.
